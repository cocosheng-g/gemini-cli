import subprocess
import json
import datetime
import os
import re
import time
import sys

# Target repository
TARGET_REPO = 'google-gemini/gemini-cli'

# Maintainers list for TEAM_STATS
MAINTAINERS = {
    "Adib234": "A.K.M. Adib",
    "cocosheng-g": "Coco Sheng",
    "cynthialong0-0": "Cynthia Long",
    "devr0306": "Dev Randalpura",
    "ivanporty": "Ivan Port",
    "kschaab": "Keith Schaab",
    "ruomengz": "Ruomeng Zhang",
    "scidomino": "Tommaso Sciortino",
    "spencer426": "Spencer Tang",
    "sripasg": "Sri Pasumarthi"
}

# Bot accounts to ignore in reviewer stats
BOT_BLACKLIST = {
    "google-gemini-bot",
    "gemini-cli[bot]",
    "github-actions[bot]",
    "gemini-code-assist"
}

# Thresholds
STALE_ASSIGNMENT_DAYS = 14
STALE_BLOCKED_PR_DAYS = 14

UNASSIGN_COMMENT = (
    "Hi @{author}, this issue is being unassigned due to 2 weeks of inactivity "
    "(either no linked PR was opened or no updates were provided). "
    "To keep the 'Help Wanted' list manageable, we are freeing this up for other contributors. "
    "Feel free to comment if you are still working on this and would like to be re-assigned!"
)

CLOSE_PR_COMMENT = (
    "Hi @{author}, this pull request is being closed because it has been stale for >14 days "
    "with unresolved conflicts or test failures. The linked issue is also being unassigned "
    "to allow other contributors to pick it up. "
    "Feel free to re-open this PR or comment on the issue if you resume work!"
)

# Specific oncaller teams
ONCALLER_TEAMS = {
    'gemini-cli-prompt-approvers',
    'gemini-cli-askmode-approvers',
    'gemini-cli-docs'
}

SEARCH_QUERY = f'repo:{TARGET_REPO} is:issue label:area/core,area/extensions,area/site label:"help wanted" sort:updated-desc'

ISSUES_QUERY = """
query($searchQuery: String!, $cursor: String) {
  search(query: $searchQuery, type: ISSUE, first: 100, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      ... on Issue {
        number title url updatedAt state
        assignees(first: 10) { nodes { login } }
        timelineItems(itemTypes: CROSS_REFERENCED_EVENT, last: 50) {
          nodes {
            ... on CrossReferencedEvent {
              source {
                ... on PullRequest {
                  number state mergedAt updatedAt url title
                  author { login }
                  assignees(first: 5) { nodes { login } }
                  repository { nameWithOwner }
                  reviewRequests(first: 10) { nodes { requestedReviewer { __typename ... on User { login } ... on Team { slug } } } }
                  latestReviews(last: 10) { nodes { author { login } state updatedAt } }
                }
              }
            }
          }
        }
      }
    }
  }
}
"""

def get_pr_batch_query(pr_numbers):
    owner, repo = TARGET_REPO.split('/')
    fragments = []
    for i, num in enumerate(pr_numbers):
        fragments.append(f"""
            pr{i}: pullRequest(number: {num}) {{
                number url title state createdAt updatedAt mergedAt
                author {{ login }}
                assignees(first: 5) {{ nodes {{ login }} }}
                mergeable
                statusCheckRollup {{ state }}
                closingIssuesReferences(first: 10) {{ nodes {{ number }} }}
                reviewRequests(first: 10) {{ nodes {{ requestedReviewer {{ __typename ... on User {{ login }} ... on Team {{ slug }} }} }} }}
                latestReviews(last: 10) {{ nodes {{ author {{ login }} state updatedAt }} }}
                comments(last: 20) {{ nodes {{ author {{ login }} publishedAt }} }}
                commits(last: 10) {{ nodes {{ commit {{ committedDate author {{ user {{ login }} }} }} }} }}
                timelineItems(last: 10, itemTypes: [REOPENED_EVENT, READY_FOR_REVIEW_EVENT]) {{
                    nodes {{ __typename ... on ReopenedEvent {{ createdAt }} ... on ReadyForReviewEvent {{ createdAt }} }}
                }}
            }}
        """)
    return f"query {{ repository(owner: \"{owner}\", name: \"{repo}\") {{ {' '.join(fragments)} }} }}"

def gh_api_graphql(query, variables=None, retries=3):
    cmd = ['gh', 'api', 'graphql']
    if variables:
        for k, v in variables.items():
            if v is not None: cmd.extend(['-F', f'{k}={v}'])
    cmd.extend(['-f', f'query={query}'])
    
    for i in range(retries):
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return json.loads(result.stdout)
        print(f"LOG: gh api graphql failed (attempt {i+1}/{retries}): {result.stderr.strip()}")
        if i < retries - 1:
            time.sleep(2 ** i) # Exponential backoff
    return None

def parse_date(date_str):
    if not date_str: return None
    return datetime.datetime.fromisoformat(date_str.replace('Z', '+00:00'))

def sanitize(text):
    if not text: return ""
    return re.sub(r'[\s|]+', ' ', text).strip()

def get_author_activity(pr):
    author = pr.get('author', {}).get('login')
    latest = pr.get('updatedAt')
    for c in pr.get('comments', {}).get('nodes', []):
        if c.get('author', {}).get('login') == author:
            latest = max(latest, c['publishedAt'])
    for commit in pr.get('commits', {}).get('nodes', []):
        c = commit.get('commit', {})
        if c.get('author', {}).get('user', {}).get('login') == author:
            latest = max(latest, c['committedDate'])
    return latest

def get_reviewer_activity(pr):
    latest = ""
    author = pr.get('author', {}).get('login')
    for rev in pr.get('latestReviews', {}).get('nodes', []):
        login = rev.get('author', {}).get('login')
        if login and login != author and login not in BOT_BLACKLIST:
            latest = max(latest, rev['updatedAt'])
    for c in pr.get('comments', {}).get('nodes', []):
        login = c.get('author', {}).get('login')
        if login and login != author and login not in BOT_BLACKLIST:
            latest = max(latest, c['publishedAt'])
    return latest

def get_status_label(pr):
    if pr['state'] == 'MERGED': return "🟣 Merged"
    if pr['state'] == 'CLOSED': return "⚪ Closed"
    if pr.get('isDraft'): return "🔘 Draft"
    if pr['mergeable'] == 'CONFLICTING': return "🔴 Blocked: Merge Conflict"
    rollup = pr.get('statusCheckRollup')
    if rollup and rollup.get('state') in ['FAILURE', 'ERROR']: return "🔴 Blocked: Test Failure"
    return "🟢 Active"

def get_status_priority(label):
    if "Blocked" in label: return 0
    if "Active" in label: return 1
    return 2

def automate_cleanup(stale_assignments, stale_blocked_prs):
    if not stale_assignments and not stale_blocked_prs:
        print("LOG: No stale items to clean up.")
        return
    
    # 1. Handle Stale Assignments (Issues with no PR)
    if stale_assignments:
        print(f"LOG: Automating cleanup for {len(stale_assignments)} stale assignments...")
        for item in stale_assignments:
            issue_no = item['issue_no']
            for user in item['assignees']:
                print(f"LOG: Unassigning @{user} from #{issue_no}...")
                comment = UNASSIGN_COMMENT.format(author=user)
                subprocess.run(['gh', 'issue', 'comment', str(issue_no), '--body', comment, '-R', TARGET_REPO], capture_output=True)
                subprocess.run(['gh', 'issue', 'edit', str(issue_no), '--remove-assignee', user, '-R', TARGET_REPO], capture_output=True)

    # 2. Handle Stale Blocked PRs (Close PR + Unassign Issue)
    if stale_blocked_prs:
        print(f"LOG: Automating cleanup for {len(stale_blocked_prs)} stale blocked PRs...")
        for item in stale_blocked_prs:
            pr_no = item['pr_no']
            issue_no = item['issue_no']
            author = item['author']
            
            print(f"LOG: Closing stale PR #{pr_no} and unassigning #{issue_no} from @{author}...")
            comment = CLOSE_PR_COMMENT.format(author=author)
            subprocess.run(['gh', 'pr', 'comment', str(pr_no), '--body', comment, '-R', TARGET_REPO], capture_output=True)
            subprocess.run(['gh', 'pr', 'close', str(pr_no), '-R', TARGET_REPO], capture_output=True)
            subprocess.run(['gh', 'issue', 'edit', str(issue_no), '--remove-assignee', author, '-R', TARGET_REPO], capture_output=True)

def main():
    print(f"LOG: Starting dashboard generation for {TARGET_REPO}...")
    
    all_issue_nodes = []
    cursor = None
    page = 1
    while True:
        print(f"LOG: Fetching issue page {page}...")
        res = gh_api_graphql(ISSUES_QUERY.replace('first: 100', 'first: 50'), {"searchQuery": SEARCH_QUERY, "cursor": cursor})
        if not res:
            print("LOG: Critical fetch failure. Exiting to prevent incomplete dashboard.")
            sys.exit(1)
        
        search_data = res['data']['search']
        all_issue_nodes.extend(search_data['nodes'])
        print(f"LOG: Loaded {len(search_data['nodes'])} issues from this page.")
        if not search_data['pageInfo']['hasNextPage']: break
        cursor = search_data['pageInfo']['endCursor']
        page += 1
    
    print(f"LOG: Total issues fetched: {len(all_issue_nodes)}")

    # Map issue info and collect PRs for detailed fetching
    issue_to_info = {i['number']: i for i in all_issue_nodes}
    issue_to_pr_info = {} # Maps issue_no to list of PR info from ISSUES_QUERY
    pr_to_fetch = set()
    
    for i in all_issue_nodes:
        pr_infos = []
        for e in i['timelineItems']['nodes']:
            if not e.get('source'): continue
            s = e['source']
            if 'number' in s and s.get('repository', {}).get('nameWithOwner') == TARGET_REPO:
                pr_infos.append(s)
                if s['state'] == 'OPEN':
                    pr_to_fetch.add(s['number'])
        issue_to_pr_info[i['number']] = pr_infos

    print(f"LOG: Fetching full details for {len(pr_to_fetch)} OPEN PRs...")
    pr_details = {}
    pr_list = sorted(list(pr_to_fetch))
    for i in range(0, len(pr_list), 20):
        batch = pr_list[i:i+20]
        res = gh_api_graphql(get_pr_batch_query(batch))
        if res and 'data' in res:
            repo_data = res['data']['repository']
            for j in range(len(batch)):
                pr_obj = repo_data.get(f'pr{j}')
                if pr_obj: pr_details[pr_obj['number']] = pr_obj
    
    print(f"LOG: Successfully loaded detailed info for {len(pr_details)} PRs.")

    now = datetime.datetime.now(datetime.timezone.utc)
    report_start = (now - datetime.timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)

    # Lists for HELP_ISSUES_TRIAGE.md
    oncaller_attention = []
    stale_assignments = []
    blocked_stale_prs = []
    initial_pickup = []
    followup_needed = []
    waiting_for_author = []
    recently_assigned = []
    active_blocked_prs = []
    unowned_prs = []
    available_pickup = []

    # Member stats for TEAM_STATS.md
    member_stats = {login: {"name": name, "weekly_closed": 0, "open_queue": [], "history": []} for login, name in MAINTAINERS.items()}
    processed_prs_for_history = set()

    print("LOG: Categorizing issues and PRs...")
    for issue_no, pr_infos in issue_to_pr_info.items():
        issue = issue_to_info[issue_no]
        issue_title = sanitize(issue['title'])
        issue_url = issue['url']
        issue_updated_at = parse_date(issue['updatedAt'])
        assignees = [a['login'] for a in issue['assignees']['nodes']]
        
        found_open_pr = False
        has_active_work = False
        
        for s in pr_infos:
            pr_no = s['number']
            pr = pr_details.get(pr_no, s)
            
            human_reviewers = set()
            special_teams = set()
            author = pr['author']['login']
            pr_assignees = [a['login'] for a in pr.get('assignees', {}).get('nodes', [])]
            
            # Reviewer collection
            if 'reviewRequests' in pr:
                nodes = pr.get('reviewRequests', {}).get('nodes', [])
                for req in nodes:
                    rr = req.get('requestedReviewer')
                    if not rr:
                        # Fallback: if GraphQL fails to populate the node (common in Actions)
                        try:
                            pr_json = json.loads(subprocess.check_output(['gh', 'pr', 'view', str(pr_no), '--json', 'reviewRequests', '-R', TARGET_REPO], stderr=subprocess.STDOUT))
                            fallback_nodes = pr_json.get('reviewRequests', [])
                            for f_rr in fallback_nodes:
                                if 'login' in f_rr: # User
                                    if f_rr['login'] != author and f_rr['login'] not in BOT_BLACKLIST: human_reviewers.add(f_rr['login'])
                                elif 'slug' in f_rr: # Team
                                    team_name = f_rr['slug'].split('/')[-1]
                                    if team_name in ONCALLER_TEAMS:
                                        print(f"LOG: Found special team request (via fallback): {team_name} on PR #{pr_no}")
                                        special_teams.add(team_name)
                        except Exception:
                            pass
                        break
                    
                    typename = rr.get('__typename')
                    if typename == 'User':
                        login = rr.get('login')
                        if login and login != author and login not in BOT_BLACKLIST: human_reviewers.add(login)
                    elif typename == 'Team':
                        slug = rr.get('slug', '')
                        team_name = slug.split('/')[-1]
                        if team_name in ONCALLER_TEAMS:
                            print(f"LOG: Found special team request: {team_name} on PR #{pr_no}")
                            special_teams.add(team_name)
            
            for rev in pr.get('latestReviews', {}).get('nodes', []):
                if rev.get('author'):
                    login = rev['author']['login']
                    if login != author and login not in BOT_BLACKLIST: human_reviewers.add(login)

            # 1. Maintainer Stats logic
            if pr['state'] != 'OPEN':
                if pr_no not in processed_prs_for_history:
                    updated_at = parse_date(pr.get('mergedAt') or pr.get('updatedAt'))
                    for r_login in human_reviewers:
                        if r_login in member_stats and updated_at and updated_at >= report_start:
                            member_stats[r_login]["weekly_closed"] += 1
                            member_stats[r_login]["history"].append({"number": pr['number'], "title": sanitize(pr.get('title', 'PR')), "url": pr.get('url', f"https://github.com/{TARGET_REPO}/pull/{pr['number']}"), "state": pr['state'], "issue_no": issue_no, "updated": pr.get('updatedAt', '')[:10]})
                    processed_prs_for_history.add(pr_no)
                continue

            pr_title = sanitize(pr['title'])
            latest_author_act_iso = get_author_activity(pr)
            latest_rev_act_iso = get_reviewer_activity(pr)
            status_label = get_status_label(pr)

            # TEAM_STATS Active Queue
            for r_login in human_reviewers:
                if r_login in member_stats:
                    member_stats[r_login]["open_queue"].append({"number": pr['number'], "title": pr_title, "url": pr['url'], "state": pr['state'], "updated": latest_author_act_iso[:10], "issue_no": issue_no, "status_label": status_label, "priority": get_status_priority(status_label)})

            # 2. Dashboard Logic
            if issue['state'] != 'OPEN': continue
            
            # --- CRITICAL FILTER: Only consider PRs officially linked to close this issue ---
            is_officially_linked = False
            if 'closingIssuesReferences' in pr:
                linked_nums = [n['number'] for n in pr['closingIssuesReferences']['nodes']]
                if issue_no in linked_nums: is_officially_linked = True
            
            if not is_officially_linked: continue

            # Specialized Approval Required check (Capture regardless of ownership)
            if special_teams:
                print(f"LOG: Issue #{issue_no} / PR #{pr_no} categorized as Specialized Approval. Teams: {special_teams}")
                oncaller_attention.append({"issue_md": f"[#{issue_no} {issue_title}]({issue_url})", "pr_no": pr_no, "pr_url": pr['url'], "pr_title": pr_title, "teams": sorted(list(special_teams)), "reviewers": sorted(list(human_reviewers)), "last_update": latest_author_act_iso[:10], "issue_no": issue_no})
                # If it's a specialized approval item, we don't put it in Unowned PRs even if unowned
                found_open_pr = True
            else:
                # Enforce ownership for other high-priority triage lists
                is_owned = (author in assignees) or any(pa in assignees for pa in pr_assignees)
                if not is_owned:
                    unowned_prs.append({"issue_md": f"[#{issue_no} {issue_title}]({issue_url})", "pr_no": pr_no, "pr_url": pr['url'], "pr_title": pr_title, "author": author, "assignees": pr_assignees, "issue_assignees": assignees, "last_update": latest_author_act_iso[:10]})
                    continue
                found_open_pr = True
            
            # If we reached here, it's either Specialized Approval or Owned PR
            is_blocked = "Blocked" in status_label
            author_acted_last = not latest_rev_act_iso or latest_author_act_iso > latest_rev_act_iso
            
            if is_blocked:
                if (now - datetime.datetime.fromisoformat(latest_author_act_iso.replace('Z', '+00:00'))).days >= STALE_BLOCKED_PR_DAYS:
                    blocked_stale_prs.append({"issue_no": issue_no, "issue_md": f"[#{issue_no} {issue_title}]({issue_url})", "pr_no": pr['number'], "pr_url": pr['url'], "pr_title": pr_title, "reason": status_label.split(': ')[1], "author": pr['author']['login'], "days_stale": (now - datetime.datetime.fromisoformat(latest_author_act_iso.replace('Z', '+00:00'))).days})
                else:
                    active_blocked_prs.append({"issue_md": f"[#{issue_no} {issue_title}]({issue_url})", "pr_no": pr['number'], "pr_url": pr['url'], "pr_title": pr_title, "author": pr['author']['login'], "reason": status_label.split(': ')[1], "last_update": latest_author_act_iso[:10]})
                has_active_work = True
            elif author_acted_last:
                item = {"issue_md": f"[#{issue_no} {issue_title}]({issue_url})", "pr_no": pr['number'], "pr_url": pr['url'], "pr_title": pr_title, "last_update": latest_author_act_iso[:10], "reviewers": sorted(list(human_reviewers))}
                if not human_reviewers:
                    initial_pickup.append(item)
                else:
                    item["reviewers"] = sorted(list(human_reviewers))
                    item["status"] = "Review Requested" if not latest_rev_act_iso else "Author Updated"
                    followup_needed.append(item)
                has_active_work = True
            else:
                waiting_for_author.append({"issue_md": f"[#{issue_no} {issue_title}]({issue_url})", "pr_no": pr['number'], "pr_url": pr['url'], "pr_title": pr_title, "reviewers": sorted(list(human_reviewers)), "last_feedback": latest_rev_act_iso[:10]})
                has_active_work = True

        if has_active_work or issue['state'] != 'OPEN': continue
        days_idle = (now - issue_updated_at).days
        if not assignees:
            available_pickup.append({"issue_md": f"[#{issue_no} {issue_title}]({issue_url})", "days_idle": days_idle})
        else:
            if days_idle >= STALE_ASSIGNMENT_DAYS:
                stale_assignments.append({"issue_no": issue_no, "issue_md": f"[#{issue_no} {issue_title}]({issue_url})", "assignees": assignees, "days_stale": days_idle})
            else:
                recently_assigned.append({"issue_md": f"[#{issue_no} {issue_title}]({issue_url})", "assignees": assignees, "last_update": issue['updatedAt'][:10]})

    print("LOG: Sorting results...")
    oncaller_attention.sort(key=lambda x: (", ".join(x['teams']), x['issue_no']))
    initial_pickup.sort(key=lambda x: (x['last_update'], x['issue_md']))
    followup_needed.sort(key=lambda x: (x['last_update'], x['issue_md']))
    waiting_for_author.sort(key=lambda x: (x['last_feedback'], x['issue_md']))
    recently_assigned.sort(key=lambda x: (x['last_update'], x['issue_md']))
    active_blocked_prs.sort(key=lambda x: (x['last_update'], x['issue_md']))
    unowned_prs.sort(key=lambda x: (x['last_update'], x['issue_md']))

    # --- Write HELP_ISSUES_TRIAGE.md ---
    print("LOG: Generating HELP_ISSUES_TRIAGE.md...")
    open_issues_count = len([i for i in all_issue_nodes if i['state'] == 'OPEN'])
    md_rev = f"# 🔎 Gemini CLI Help Wanted Triage Dashboard\n\n*Last Synchronized: {now.strftime('%Y-%m-%d %H:%M')} (UTC)*\n\n"
    md_rev += f"**Total Issues Tracked: {open_issues_count} open issues**\n\n"
    
    md_rev += "## 🚨 Needs Oncaller Attention\n"

    md_rev += f"\n<details>\n<summary><b>🆕 Awaiting Reviewer Pickup ({len(initial_pickup)})</b> — <i>Pick up one of these new PRs.</i></summary>\n\n**Criteria: New PRs with no reviewers yet, author acted last.**\n\n| Issue | Linked PR | Last Update |\n| :--- | :--- | :--- |\n"
    for i in initial_pickup: md_rev += f"| {i['issue_md']} | [#{i['pr_no']}]({i['pr_url']}) | `{i['last_update']}` |\n"
    if not initial_pickup: md_rev += "| - | - | - |\n"
    md_rev += "</details>\n"

    md_rev += f"\n<details>\n<summary><b>🛡️ Specialized Approval Required ({len(oncaller_attention)})</b> — <i>Specialized approval required.</i></summary>\n\n**Criteria: PRs requesting review from specialized teams (e.g., docs, prompts).**\n\n| Issue | Linked PR | Required Teams | Human Reviewers |\n| :--- | :--- | :--- | :--- |\n"
    for i in oncaller_attention: md_rev += f"| {i['issue_md']} | [#{i['pr_no']}]({i['pr_url']}) | {', '.join([f'`{t}`' for t in i['teams']])} | {', '.join(['@'+r for r in i['reviewers']]) if i['reviewers'] else '_None_'} |\n"
    if not oncaller_attention: md_rev += "| - | - | - | - |\n"
    md_rev += "</details>\n"

    md_rev += f"\n<details>\n<summary><b>🚩 Stale Assignments ({len(stale_assignments)})</b> — <i>Auto-cleanup.</i></summary>\n\n**Criteria: Assigned issues with no open PR, idle for >{STALE_ASSIGNMENT_DAYS} days.**\n\n| Issue | Assignee | Days Stale |\n| :--- | :--- | :--- |\n"
    for i in stale_assignments: md_rev += f"| {i['issue_md']} | @{', @'.join(i['assignees'])} | {i['days_stale']} |\n"
    if not stale_assignments: md_rev += "| - | - | - |\n"
    md_rev += "</details>\n"

    md_rev += f"\n<details>\n<summary><b>🚧 Blocked & Stale PRs ({len(blocked_stale_prs)})</b> — <i>Auto-cleanup.</i></summary>\n\n**Criteria: PRs with conflicts or failures untouched for >{STALE_BLOCKED_PR_DAYS} days.**\n\n| Issue | PR | Reason | Author | Days Stale |\n| :--- | :--- | :--- | :--- | :--- |\n"
    for i in blocked_stale_prs: md_rev += f"| {i['issue_md']} | [#{i['pr_no']}]({i['pr_url']}) | {i['reason']} | @{i['author']} | {i['days_stale']} |\n"
    if not blocked_stale_prs: md_rev += "| - | - | - | - | - |\n"
    md_rev += "</details>\n"

    md_rev += "\n## 🛠️ Active Development\n"

    md_rev += f"\n<details>\n<summary><b>⌛ Awaiting Reviewer Follow-up ({len(followup_needed)})</b> — <i>Reviewers, please follow up.</i></summary>\n\n**Criteria: Review in progress, author has responded to latest feedback.**\n\n| Issue | Linked PR | Reviewers | Status | Last Update |\n| :--- | :--- | :--- | :--- | :--- |\n"
    for i in followup_needed: md_rev += f"| {i['issue_md']} | [#{i['pr_no']}]({i['pr_url']}) | {', '.join(['@'+r for r in i['reviewers']])} | {i['status']} | `{i['last_update']}` |\n"
    if not followup_needed: md_rev += "| - | - | - | - | - |\n"
    md_rev += "</details>\n"

    md_rev += f"\n<details>\n<summary><b>✍️ Awaiting Author Action ({len(waiting_for_author)})</b> — <i>Waiting for contributor.</i></summary>\n\n**Criteria: Reviewer acted last, waiting for contributor to address comments.**\n\n| Issue | Linked PR | Reviewers | Last Feedback |\n| :--- | :--- | :--- | :--- |\n"
    for i in waiting_for_author: md_rev += f"| {i['issue_md']} | [#{i['pr_no']}]({i['pr_url']}) | {', '.join(['@'+r for r in i['reviewers']]) if i['reviewers'] else '_None (Team only)_'} | `{i['last_feedback']}` |\n"
    if not waiting_for_author: md_rev += "| - | - | - | - |\n"
    md_rev += "</details>\n"

    md_rev += f"\n<details>\n<summary><b>🛠️ Active Development: Recently Assigned ({len(recently_assigned)})</b> — <i>Assigned < 14 days ago.</i></summary>\n\n**Criteria: Issues assigned < {STALE_ASSIGNMENT_DAYS} days ago, no PR yet.**\n\n| Issue | Assignee | Last Update |\n| :--- | :--- | :--- |\n"
    for i in recently_assigned: md_rev += f"| {i['issue_md']} | @{', @'.join(i['assignees'])} | `{i['last_update']}` |\n"
    if not recently_assigned: md_rev += "| - | - | - |\n"
    md_rev += "</details>\n"

    md_rev += f"\n<details>\n<summary><b>🛠️ Active Development: Blocked PRs ({len(active_blocked_prs)})</b> — <i>Active work with blockers.</i></summary>\n\n**Criteria: Active PRs with conflicts or failures updated within {STALE_BLOCKED_PR_DAYS} days.**\n\n| Issue | Linked PR | Author | Reason | Last Update |\n| :--- | :--- | :--- | :--- | :--- |\n"
    for i in active_blocked_prs: md_rev += f"| {i['issue_md']} | [#{i['pr_no']}]({i['pr_url']}) | @{i['author']} | {i['reason']} | `{i['last_update']}` |\n"
    if not active_blocked_prs: md_rev += "| - | - | - | - | - |\n"
    md_rev += "</details>\n"

    md_rev += "\n## 🌱 Community & Backlog\n"

    md_rev += f"\n<details>\n<summary><b>🌱 Available for Pickup ({len(available_pickup)})</b> — <i>Open for contributors.</i></summary>\n\n**Criteria: Open issues with no assignee and no active PR.**\n\n| Issue | Days Idle |\n| :--- | :--- |\n"
    for i in available_pickup: md_rev += f"| {i['issue_md']} | {i['days_idle']} |\n"
    if not available_pickup: md_rev += "| - | _None_ |\n"
    md_rev += "</details>\n"

    md_rev += f"\n<details>\n<summary><b>⚠️ Unowned PRs ({len(unowned_prs)})</b> — <i>Ownership mismatch.</i></summary>\n\n**Criteria: PRs where author/assignee does not match the linked issue's assignee.**\n\n| Issue | Linked PR | PR Author | Issue Assignee | Last Update |\n| :--- | :--- | :--- | :--- | :--- |\n"
    for i in unowned_prs:
        pr_auth = f"@{i['author']}"
        iss_assign = f"@{', @'.join(i['issue_assignees'])}" if i['issue_assignees'] else "_Unassigned_"
        md_rev += f"| {i['issue_md']} | [#{i['pr_no']}]({i['pr_url']}) | {pr_auth} | {iss_assign} | `{i['last_update']}` |\n"
    if not unowned_prs: md_rev += "| - | - | - | - | - |\n"
    md_rev += "</details>\n"

    md_rev += "\n---\n*Dashboard maintained by automated triage script.*"
    with open("HELP_ISSUES_TRIAGE.md", "w") as f: f.write(md_rev)

    # --- Write TEAM_STATS.md ---
    print("LOG: Generating TEAM_STATS.md...")
    md_stats = f"# 📊 Gemini CLI Weekly Team Review Stats\n\n*Reporting Period: **Monday {report_start.strftime('%Y-%m-%d')}** to Today*\n*Last Updated: {now.strftime('%Y-%m-%d %H:%M')} (UTC)*\n\n"
    md_stats += "## 📈 Weekly Summary\n| Maintainer | Closed/Merged (Week) | Current Open Queue |\n| :--- | :--- | :--- |\n"
    for login, data in sorted(member_stats.items(), key=lambda x: x[1]['weekly_closed'], reverse=True):
        md_stats += f"| **{data['name']}** (@{login}) | **{data['weekly_closed']}** | {len(data['open_queue'])} |\n"

    md_stats += f"\n### 🆕 Awaiting Reviewer Pickup ({len(initial_pickup)})\n**Action: Pick up one of these new PRs.** All tests passing, no conflicts.\n\n| Issue | Linked PR | Last Update |\n| :--- | :--- | :--- |\n"
    for i in initial_pickup: md_stats += f"| {i['issue_md']} | [#{i['pr_no']}]({i['pr_url']}) | `{i['last_update']}` |\n"
    if not initial_pickup: md_stats += "| - | - | - |\n"

    md_stats += "\n---\n## 👤 Individual Review Queues\n"
    for login, data in sorted(member_stats.items(), key=lambda x: x[1]['name']):
        history_count = len(data['history'])
        summary = f"<b>{data['name']} (@{login})</b> — 🟢 Active Queue ({len(data['open_queue'])})"
        if history_count > 0: summary += f" | 🔴 Recently Closed ({history_count})"
        
        md_stats += f"\n<details>\n<summary>{summary}</summary>\n"
        
        md_stats += "\n#### 🟢 Active Queue\n| PR | Issue | Title | Status & Next Step | Updated |\n| :--- | :--- | :--- | :--- | :--- |\n"
        for p in sorted(data['open_queue'], key=lambda x: (x['priority'], datetime.datetime.fromisoformat(x['updated']).timestamp() * -1)):
            md_stats += f"| [#{p['number']}]({p['url']}) | [#{p['issue_no']}](https://github.com/{TARGET_REPO}/issues/{p['issue_no']}) | {p['title']} | {p['status_label']} | `{p['updated']}` |\n"
        if not data['open_queue']: md_stats += "| - | - | _No active reviews._ | - | - |\n"
        
        if data['history']:
            md_stats += "\n#### 🔴 Recently Closed (Since Monday)\n| PR | Issue | Title | Status | Closed Date |\n| :--- | :--- | :--- | :--- | :--- |\n"
            for p in sorted(data['history'], key=lambda x: x['updated'], reverse=True):
                md_stats += f"| [#{p['number']}]({p['url']}) | [#{p['issue_no']}](https://github.com/{TARGET_REPO}/issues/{p['issue_no']}) | {p['title']} | `{p['state']}` | `{p['updated']}` |\n"
        
        md_stats += "\n</details>\n"

    md_stats += "\n---\n*Report generated by automated triage script.*"
    with open("TEAM_STATS.md", "w") as f: f.write(md_stats)
    print("LOG: Dashboard generation complete.")

    automate_cleanup(stale_assignments, blocked_stale_prs)

if __name__ == "__main__":
    main()

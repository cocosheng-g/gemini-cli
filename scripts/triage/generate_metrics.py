import subprocess
import json
import datetime
import os
import sys

TARGET_REPO = 'google-gemini/gemini-cli'

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
            import time
            time.sleep(2 ** i)
    return None

def parse_date(date_str):
    if not date_str: return None
    return datetime.datetime.fromisoformat(date_str.replace('Z', '+00:00'))

def main():
    now = datetime.datetime.now(datetime.timezone.utc)
    thirty_days_ago = now - datetime.timedelta(days=30)
    
    SEARCH_QUERY = f'repo:{TARGET_REPO} is:issue label:area/core,area/extensions,area/site label:"help wanted"'
    
    ISSUES_QUERY = """
    query($searchQuery: String!, $cursor: String) {
      search(query: $searchQuery, type: ISSUE, first: 30, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          ... on Issue {
            number state createdAt closedAt
            comments(last: 30) { nodes { author { login } publishedAt } }
            timelineItems(itemTypes: CROSS_REFERENCED_EVENT, first: 30) {
              nodes {
                ... on CrossReferencedEvent {
                  source {
                    ... on PullRequest {
                      number state createdAt mergedAt closedAt
                      author { login }
                      reviews(last: 20) { nodes { author { login } createdAt state } }
                      comments(last: 30) { nodes { author { login } publishedAt } }
                      commits(last: 10) { nodes { commit { committedDate author { user { login } } } } }
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
    
    all_issues = []
    cursor = None
    
    print("LOG: Fetching issues for metrics calculation...")
    while True:
        res = gh_api_graphql(ISSUES_QUERY, {"searchQuery": SEARCH_QUERY, "cursor": cursor})
        if not res: break
        search_data = res['data']['search']
        all_issues.extend(search_data['nodes'])
        if not search_data['pageInfo']['hasNextPage']: break
        cursor = search_data['pageInfo']['endCursor']
        
    new_issues = 0
    closed_issues = 0
    new_prs = 0
    merged_prs = 0
    unmerged_closed_prs = 0
    
    ttfr_list = []
    ttm_list = []
    
    seen_prs = set()
    contributors = {}
    
    # Initialize daily bins (30 days) to capture precise daily metrics
    days_labels = []
    display_labels = []
    opened_by_day = {}
    merged_by_day = {}
    new_issues_by_day = {}
    closed_unmerged_by_day = {}
    ttfr_by_day_lists = {}
    ttm_by_day_lists = {}
    active_contributors_by_day = {}
    
    open_issues_snapshot = {}
    closed_issues_snapshot = {}
    
    for i in range(30):
        d = thirty_days_ago + datetime.timedelta(days=i)
        d_label = d.strftime('%m-%d')
        days_labels.append(d_label)
        # To prevent x-axis overlapping, use only the day (2 chars). 
        # Append zero-width spaces to ensure uniqueness for Mermaid parsing.
        display_labels.append(f"{d.strftime('%d')}{chr(0x200B) * i}")
        
        opened_by_day[d_label] = 0
        merged_by_day[d_label] = 0
        new_issues_by_day[d_label] = 0
        closed_unmerged_by_day[d_label] = 0
        ttfr_by_day_lists[d_label] = []
        ttm_by_day_lists[d_label] = []
        active_contributors_by_day[d_label] = set()
        open_issues_snapshot[d_label] = 0
        closed_issues_snapshot[d_label] = 0

    def get_bin_label(date_obj):
        delta = (date_obj - thirty_days_ago).days
        if 0 <= delta < 30:
            return days_labels[delta]
        return None

    BOTS = {"google-gemini-bot", "gemini-cli[bot]", "github-actions[bot]", "gemini-code-assist"}
    
    for issue in all_issues:
        created_at = parse_date(issue['createdAt'])
        if created_at >= thirty_days_ago:
            new_issues += 1
            d_label = get_bin_label(created_at)
            if d_label: new_issues_by_day[d_label] += 1
            
        if issue['state'] == 'CLOSED' and issue['closedAt']:
            closed_at = parse_date(issue['closedAt'])
            if closed_at >= thirty_days_ago:
                closed_issues += 1
                
        for c in issue.get('comments', {}).get('nodes', []):
            c_author = c.get('author', {}).get('login') if c.get('author') else None
            if c_author and c_author not in BOTS:
                c_time = parse_date(c['publishedAt'])
                if c_time >= thirty_days_ago:
                    d_label = get_bin_label(c_time)
                    if d_label:
                        if c_author not in contributors: contributors[c_author] = {'opened': 0, 'merged': 0, 'closed': 0}
                        active_contributors_by_day[d_label].add(c_author)
                
        for event in issue.get('timelineItems', {}).get('nodes', []):
            if not event or not event.get('source') or 'number' not in event['source']: continue
            pr = event['source']
            if pr['number'] in seen_prs: continue
            seen_prs.add(pr['number'])
            
            pr_created = parse_date(pr['createdAt'])
            pr_author = pr.get('author', {}).get('login') if pr.get('author') else None
            
            if pr_author and pr_author not in BOTS:
                if pr_author not in contributors:
                    contributors[pr_author] = {'opened': 0, 'merged': 0, 'closed': 0}
            
            if pr_created >= thirty_days_ago:
                new_prs += 1
                d_label = get_bin_label(pr_created)
                if pr_author and pr_author not in BOTS:
                    contributors[pr_author]['opened'] += 1
                    if d_label: active_contributors_by_day[d_label].add(pr_author)
                if d_label: opened_by_day[d_label] += 1
                
            first_review_time = None
            for rev in pr.get('reviews', {}).get('nodes', []):
                r_author = rev.get('author', {}).get('login') if rev.get('author') else None
                if r_author and r_author not in BOTS:
                    r_time = parse_date(rev['createdAt'])
                    if r_time >= thirty_days_ago:
                        r_label = get_bin_label(r_time)
                        if r_label:
                            if r_author not in contributors: contributors[r_author] = {'opened': 0, 'merged': 0, 'closed': 0}
                            active_contributors_by_day[r_label].add(r_author)
                    if r_author != pr_author:
                        if not first_review_time or r_time < first_review_time:
                            first_review_time = r_time
            
            for c in pr.get('comments', {}).get('nodes', []):
                c_author = c.get('author', {}).get('login') if c.get('author') else None
                if c_author and c_author not in BOTS:
                    c_time = parse_date(c['publishedAt'])
                    if c_time >= thirty_days_ago:
                        c_label = get_bin_label(c_time)
                        if c_label:
                            if c_author not in contributors: contributors[c_author] = {'opened': 0, 'merged': 0, 'closed': 0}
                            active_contributors_by_day[c_label].add(c_author)
                    if c_author != pr_author:
                        if not first_review_time or c_time < first_review_time:
                            first_review_time = c_time
            
            for commit_node in pr.get('commits', {}).get('nodes', []):
                commit_author = commit_node.get('commit', {}).get('author', {}).get('user', {}).get('login') if commit_node.get('commit', {}).get('author', {}).get('user') else None
                if commit_author and commit_author not in BOTS:
                    commit_time = parse_date(commit_node['commit']['committedDate'])
                    if commit_time >= thirty_days_ago:
                        commit_label = get_bin_label(commit_time)
                        if commit_label:
                            if commit_author not in contributors: contributors[commit_author] = {'opened': 0, 'merged': 0, 'closed': 0}
                            active_contributors_by_day[commit_label].add(commit_author)
                        
            if first_review_time and first_review_time >= thirty_days_ago:
                ttfr_val = (first_review_time - pr_created).total_seconds() / 3600.0
                ttfr_list.append(ttfr_val)
                review_label = get_bin_label(first_review_time)
                if review_label: ttfr_by_day_lists[review_label].append(ttfr_val)
                    
            if pr['state'] == 'MERGED' and pr['mergedAt']:
                merged_at = parse_date(pr['mergedAt'])
                if merged_at >= thirty_days_ago:
                    merged_prs += 1
                    d_label = get_bin_label(merged_at)
                    if pr_author and pr_author not in BOTS:
                        contributors[pr_author]['merged'] += 1
                        if d_label: active_contributors_by_day[d_label].add(pr_author)
                    if d_label: merged_by_day[d_label] += 1
                    ttm_val = (merged_at - pr_created).total_seconds() / 3600.0 / 24.0
                    ttm_list.append(ttm_val)
                    if d_label: ttm_by_day_lists[d_label].append(ttm_val)
                    
            elif pr['state'] == 'CLOSED' and pr['closedAt']:
                pr_closed = parse_date(pr['closedAt'])
                if pr_closed >= thirty_days_ago:
                    unmerged_closed_prs += 1
                    d_label = get_bin_label(pr_closed)
                    if pr_author and pr_author not in BOTS:
                        contributors[pr_author]['closed'] += 1
                        if d_label: active_contributors_by_day[d_label].add(pr_author)
                    if d_label: closed_unmerged_by_day[d_label] += 1
                    
    avg_ttfr = sum(ttfr_list) / len(ttfr_list) if ttfr_list else 0
    avg_ttm = sum(ttm_list) / len(ttm_list) if ttm_list else 0

    # Calculate point-in-time open/closed issue snapshots
    for i in range(30):
        day_end = thirty_days_ago + datetime.timedelta(days=i, hours=23, minutes=59, seconds=59)
        d_label = days_labels[i]
        for issue in all_issues:
            created_at = parse_date(issue['createdAt'])
            if created_at and created_at <= day_end:
                closed_at = parse_date(issue.get('closedAt'))
                if issue['state'] == 'CLOSED' and closed_at and closed_at <= day_end:
                    closed_issues_snapshot[d_label] += 1
                else:
                    open_issues_snapshot[d_label] += 1

    ttfr_data = [round(sum(ttfr_by_day_lists[d]) / len(ttfr_by_day_lists[d]), 1) if ttfr_by_day_lists[d] else 0 for d in days_labels]
    ttm_data = [round(sum(ttm_by_day_lists[d]) / len(ttm_by_day_lists[d]), 1) if ttm_by_day_lists[d] else 0 for d in days_labels]
    
    active_contributors_data = [len(active_contributors_by_day[d]) for d in days_labels]
    avg_opened_data = [round(opened_by_day[d] / len(active_contributors_by_day[d]), 1) if active_contributors_by_day[d] else 0 for d in days_labels]
    avg_merged_data = [round(merged_by_day[d] / len(active_contributors_by_day[d]), 1) if active_contributors_by_day[d] else 0 for d in days_labels]
    
    conversion_rate = merged_prs / new_prs * 100 if new_prs > 0 else 0
    dropoff_rate = unmerged_closed_prs / (merged_prs + unmerged_closed_prs) * 100 if (merged_prs + unmerged_closed_prs) > 0 else 0
    
    end_d = thirty_days_ago + datetime.timedelta(days=29)
    date_range_str = f"{thirty_days_ago.strftime('%b %d')} - {end_d.strftime('%b %d')}"
    
    md = f"# 📈 Gemini CLI Contribution Metrics Dashboard\n\n"
    md += f"*Generated on {now.strftime('%Y-%m-%d')} (UTC). Reflects activity from the last 30 days.*\n\n"
    
    opened_data = [opened_by_day[d] for d in days_labels]
    merged_data = [merged_by_day[d] for d in days_labels]
    new_issues_data = [new_issues_by_day[d] for d in days_labels]
    closed_unmerged_data = [closed_unmerged_by_day[d] for d in days_labels]
    open_issues_data = [open_issues_snapshot[d] for d in days_labels]
    closed_issues_data = [closed_issues_snapshot[d] for d in days_labels]

    md += "## 🚀 Velocity & Throughput\n"
    md += "Tracks the sheer volume of contribution activity over the past 30 days.\n\n"

    md += "### Help Wanted Backlog (Daily Snapshot)\n"
    md += "> **Legend:** 📊 Bar = Total Open Issues | 📈 Line = Cumulative Closed Issues\n\n"
    md += "```mermaid\n"
    md += "---\nconfig:\n  xyChart:\n    showDataLabel: true\n---\n"
    md += "xychart-beta\n"
    md += f'    title "Help Wanted Backlog ({date_range_str})"\n'
    md += f'    x-axis {json.dumps(display_labels, ensure_ascii=False)}\n'
    md += '    y-axis "Count"\n'
    md += f'    bar {open_issues_data}\n'
    md += f'    line {closed_issues_data}\n'
    md += "```\n\n"

    md += "### PRs Opened vs Merged\n"
    md += "> **Legend:** 📊 Bar = PRs Opened | 📈 Line = PRs Merged\n\n"
    md += "```mermaid\n"
    md += "---\nconfig:\n  xyChart:\n    showDataLabel: true\n---\n"
    md += "xychart-beta\n"
    md += f'    title "PR Activity ({date_range_str})"\n'
    md += f'    x-axis {json.dumps(display_labels, ensure_ascii=False)}\n'
    md += '    y-axis "Count"\n'
    md += f'    bar {opened_data}\n'
    md += f'    line {merged_data}\n'
    md += "```\n\n"
    
    md += "| Metric | Last 30 Days | Target / Goal | Calculation |\n"
    md += "| :--- | :--- | :--- | :--- |\n"
    md += f"| 🛠️ PRs Opened | **{new_prs}** | - | Number of new PRs opened linked to a `help wanted` issue. |\n"
    md += f"| 🟣 PRs Merged | **{merged_prs}** | Track closely to Opened | Number of those linked PRs that were successfully merged. |\n"
    md += f"| ⚪ PRs Closed (Unmerged) | **{unmerged_closed_prs}** | - | Number of those linked PRs that were closed without merging (e.g. abandoned, stale). |\n"
    md += f"| 🔄 Issue to PR Conversion Rate | **{conversion_rate:.1f}%** | > 50% | Percentage of opened PRs that successfully get merged (`Merged / Opened`). |\n\n"
    
    md += "## ⏱️ Efficiency & Bottlenecks\n"
    md += "Measures the speed and responsiveness of the maintainer team in processing community PRs.\n\n"
    
    md += "### Time to First Review (TTFR) Trend\n"
    md += "> **Legend:** 📈 Line = Average Time to First Review (in hours) for PRs reviewed on that day\n\n"
    md += "```mermaid\n"
    md += "---\nconfig:\n  xyChart:\n    showDataLabel: true\n---\n"
    md += "xychart-beta\n"
    md += f'    title "Average TTFR per Day (Hours)"\n'
    md += f'    x-axis {json.dumps(display_labels, ensure_ascii=False)}\n'
    md += '    y-axis "Hours"\n'
    md += f'    line {ttfr_data}\n'
    md += "```\n\n"
    
    md += "### Time to Merge (TTM) Trend\n"
    md += "> **Legend:** 📈 Line = Average Time to Merge (in days) for PRs successfully merged on that day\n\n"
    md += "```mermaid\n"
    md += "---\nconfig:\n  xyChart:\n    showDataLabel: true\n---\n"
    md += "xychart-beta\n"
    md += f'    title "Average TTM per Day (Days)"\n'
    md += f'    x-axis {json.dumps(display_labels, ensure_ascii=False)}\n'
    md += '    y-axis "Days"\n'
    md += f'    line {ttm_data}\n'
    md += "```\n\n"
    
    md += "| Metric | Average | Target / Goal | Calculation |\n"
    md += "| :--- | :--- | :--- | :--- |\n"
    md += f"| ⚡ Time to First Review (TTFR) | **{avg_ttfr:.1f} hours** | < 168 hours (1 week) | Average time from PR creation until the first comment or review from a maintainer. |\n"
    md += f"| 🚢 Time to Merge (TTM) | **{avg_ttm:.1f} days** | < 14 days (2 weeks) | Average time from PR creation to when it is successfully merged into the codebase. |\n\n"
    
    md += "## 👥 Contributor Engagement\n"
    active_contributors_count = len(contributors)
    avg_prs_opened = sum(c['opened'] for c in contributors.values()) / active_contributors_count if active_contributors_count > 0 else 0
    avg_prs_merged = sum(c['merged'] for c in contributors.values()) / active_contributors_count if active_contributors_count > 0 else 0

    md += "> **Legend:** 📊 Bar = Number of unique active contributors (opened, merged, closed, reviewed, commented, or committed)\n\n"
    md += "```mermaid\n"
    md += "---\nconfig:\n  xyChart:\n    showDataLabel: true\n---\n"
    md += "xychart-beta\n"
    md += f'    title "Active Contributors"\n'
    md += f'    x-axis {json.dumps(display_labels, ensure_ascii=False)}\n'
    md += '    y-axis "Count"\n'
    md += f'    bar {active_contributors_data}\n'
    md += "```\n\n"

    md += "> **Legend:** 📈 Line = Avg PRs Opened per Active Contributor\n\n"
    md += "```mermaid\n"
    md += "---\nconfig:\n  xyChart:\n    showDataLabel: true\n---\n"
    md += "xychart-beta\n"
    md += f'    title "Avg PRs Opened per Contributor"\n'
    md += f'    x-axis {json.dumps(display_labels, ensure_ascii=False)}\n'
    md += '    y-axis "PRs"\n'
    md += f'    line {avg_opened_data}\n'
    md += "```\n\n"

    md += "> **Legend:** 📈 Line = Avg PRs Merged per Active Contributor\n\n"
    md += "```mermaid\n"
    md += "---\nconfig:\n  xyChart:\n    showDataLabel: true\n---\n"
    md += "xychart-beta\n"
    md += f'    title "Avg PRs Merged per Contributor"\n'
    md += f'    x-axis {json.dumps(display_labels, ensure_ascii=False)}\n'
    md += '    y-axis "PRs"\n'
    md += f'    line {avg_merged_data}\n'
    md += "```\n\n"

    md += "| Metric | Value | Target / Goal | Calculation |\n"
    md += "| :--- | :--- | :--- | :--- |\n"
    md += f"| 🧑‍💻 Total Active Contributors | **{active_contributors_count}** | Steady Growth | Number of unique human contributors who opened, merged, closed, reviewed, commented, or committed to a PR or Issue in the last 30 days. |\n"
    md += f"| 📈 Avg PRs Opened | **{avg_prs_opened:.1f}** | 1.0 PR | Total PRs opened divided by total active contributors over 30 days. |\n"
    md += f"| 🎯 Avg PRs Merged | **{avg_prs_merged:.1f}** | 1.0 PR | Total PRs merged divided by total active contributors over 30 days. |\n\n"

    md += "---\n*Metrics maintained by automated daily script.*"
    
    os.makedirs("triage", exist_ok=True)
    with open("triage/CONTRIBUTION_METRICS.md", "w") as f:
        f.write(md)
        
    print("LOG: Metrics generation complete.")

if __name__ == "__main__":
    main()

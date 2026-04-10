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
      search(query: $searchQuery, type: ISSUE, first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          ... on Issue {
            number state createdAt closedAt
            timelineItems(itemTypes: CROSS_REFERENCED_EVENT, first: 100) {
              nodes {
                ... on CrossReferencedEvent {
                  source {
                    ... on PullRequest {
                      number state createdAt mergedAt closedAt
                      author { login }
                      reviews(first: 100) { nodes { author { login } createdAt state } }
                      comments(first: 100) { nodes { author { login } publishedAt } }
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
    
    # Initialize daily bins
    days_labels = []
    opened_by_day = {}
    merged_by_day = {}
    
    for i in range(30):
        d = (thirty_days_ago + datetime.timedelta(days=i)).strftime('%m-%d')
        days_labels.append(d)
        opened_by_day[d] = 0
        merged_by_day[d] = 0

    BOTS = {"google-gemini-bot", "gemini-cli[bot]", "github-actions[bot]", "gemini-code-assist"}
    
    for issue in all_issues:
        created_at = parse_date(issue['createdAt'])
        if created_at >= thirty_days_ago:
            new_issues += 1
            
        if issue['state'] == 'CLOSED' and issue['closedAt']:
            closed_at = parse_date(issue['closedAt'])
            if closed_at >= thirty_days_ago:
                closed_issues += 1
                
        for event in issue.get('timelineItems', {}).get('nodes', []):
            if not event or not event.get('source') or 'number' not in event['source']: continue
            pr = event['source']
            if pr['number'] in seen_prs: continue
            seen_prs.add(pr['number'])
            
            pr_created = parse_date(pr['createdAt'])
            pr_author = pr.get('author', {}).get('login') if pr.get('author') else None
            
            if pr_created >= thirty_days_ago:
                new_prs += 1
                d_label = pr_created.strftime('%m-%d')
                if d_label in opened_by_day: opened_by_day[d_label] += 1
                
                first_review_time = None
                for rev in pr.get('reviews', {}).get('nodes', []):
                    r_author = rev.get('author', {}).get('login') if rev.get('author') else None
                    if r_author and r_author != pr_author and r_author not in BOTS:
                        r_time = parse_date(rev['createdAt'])
                        if not first_review_time or r_time < first_review_time:
                            first_review_time = r_time
                
                for c in pr.get('comments', {}).get('nodes', []):
                    c_author = c.get('author', {}).get('login') if c.get('author') else None
                    if c_author and c_author != pr_author and c_author not in BOTS:
                        c_time = parse_date(c['publishedAt'])
                        if not first_review_time or c_time < first_review_time:
                            first_review_time = c_time
                            
                if first_review_time:
                    ttfr_list.append((first_review_time - pr_created).total_seconds() / 3600.0)
                    
            if pr['state'] == 'MERGED' and pr['mergedAt']:
                merged_at = parse_date(pr['mergedAt'])
                if merged_at >= thirty_days_ago:
                    merged_prs += 1
                    d_label = merged_at.strftime('%m-%d')
                    if d_label in merged_by_day: merged_by_day[d_label] += 1
                    ttm_list.append((merged_at - pr_created).total_seconds() / 3600.0 / 24.0)
                    
            elif pr['state'] == 'CLOSED' and pr['closedAt']:
                pr_closed = parse_date(pr['closedAt'])
                if pr_closed >= thirty_days_ago:
                    unmerged_closed_prs += 1
                    
    avg_ttfr = sum(ttfr_list) / len(ttfr_list) if ttfr_list else 0
    avg_ttm = sum(ttm_list) / len(ttm_list) if ttm_list else 0
    
    conversion_rate = merged_prs / new_prs * 100 if new_prs > 0 else 0
    dropoff_rate = unmerged_closed_prs / (merged_prs + unmerged_closed_prs) * 100 if (merged_prs + unmerged_closed_prs) > 0 else 0
    
    md = f"# 📈 Gemini CLI Contribution Metrics Dashboard\n\n"
    md += f"*Generated on {now.strftime('%Y-%m-%d')} (UTC). Reflects activity from the last 30 days.*\n\n"
    
    opened_data = [opened_by_day[d] for d in days_labels]
    merged_data = [merged_by_day[d] for d in days_labels]

    md += "## 📊 Daily PR Activity\n"
    md += "```mermaid\n"
    md += "xychart-beta\n"
    md += f'    title "PRs Opened vs Merged (Last 30 Days)"\n'
    md += f'    x-axis {json.dumps(days_labels)}\n'
    md += '    y-axis "Count"\n'
    md += f'    bar {opened_data}\n'
    md += f'    line {merged_data}\n'
    md += "```\n\n"
    
    md += "## 🚀 Velocity & Throughput\n"
    md += "Tracks the sheer volume of contribution activity over the past 30 days.\n\n"
    md += "| Metric | Last 30 Days | Calculation |\n"
    md += "| :--- | :--- | :--- |\n"
    md += f"| 🆕 New Help Wanted Issues | **{new_issues}** | Number of new issues created with the `help wanted` label. |\n"
    md += f"| 🛠️ PRs Opened | **{new_prs}** | Number of new PRs opened linked to a `help wanted` issue. |\n"
    md += f"| 🟣 PRs Merged | **{merged_prs}** | Number of those linked PRs that were successfully merged. |\n"
    md += f"| ⚪ PRs Closed (Unmerged) | **{unmerged_closed_prs}** | Number of those linked PRs that were closed without merging (e.g. abandoned, stale). |\n"
    md += f"| 🔄 Issue to PR Conversion Rate | **{conversion_rate:.1f}%** | Percentage of opened PRs that successfully get merged (`Merged / Opened`). |\n\n"
    
    md += "## ⏱️ Efficiency & Bottlenecks\n"
    md += "Measures the speed and responsiveness of the maintainer team in processing community PRs.\n\n"
    md += "| Metric | Average | Calculation |\n"
    md += "| :--- | :--- | :--- |\n"
    md += f"| ⚡ Time to First Review (TTFR) | **{avg_ttfr:.1f} hours** | Average time from PR creation until the first comment or review from a maintainer. (Target: < 24h) |\n"
    md += f"| 🚢 Time to Merge (TTM) | **{avg_ttm:.1f} days** | Average time from PR creation to when it is successfully merged into the codebase. |\n\n"
    
    md += "## ❤️ Community Health\n"
    md += "Indicates the general success and retention rate of contributors attempting to resolve issues.\n\n"
    md += "| Metric | Rate | Calculation |\n"
    md += "| :--- | :--- | :--- |\n"
    md += f"| 📉 Author Drop-off Rate | **{dropoff_rate:.1f}%** | Percentage of closed PRs that were abandoned or unmerged out of all resolved PRs (`Unmerged / Total Closed`). High drop-off could mean tasks are too hard or setup is complex. |\n\n"
    
    md += "---\n*Metrics maintained by automated daily script.*"
    
    os.makedirs("triage", exist_ok=True)
    with open("triage/CONTRIBUTION_METRICS.md", "w") as f:
        f.write(md)
        
    print("LOG: Metrics generation complete.")

if __name__ == "__main__":
    main()

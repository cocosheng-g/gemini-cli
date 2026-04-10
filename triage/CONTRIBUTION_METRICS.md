# 📈 Gemini CLI Contribution Metrics Dashboard

*Generated on 2026-04-10 (UTC). Reflects activity from the last 30 days.*

## 🚀 Velocity & Throughput
Tracks the sheer volume of contribution activity over the past 30 days.

### Daily Volume Activity
> **Legend:** 📊 Bar = PRs Opened | 📈 Line 1 = PRs Merged | 📉 Line 2 = PRs Closed (Unmerged)

```mermaid
xychart-beta
    title "PRs Opened vs Merged vs Closed (Unmerged)"
    x-axis ["03/11-03/13", "03/14-03/16", "03/17-03/19", "03/20-03/22", "03/23-03/25", "03/26-03/28", "03/29-03/31", "04/01-04/03", "04/04-04/06", "04/07-04/09"]
    y-axis "Count"
    bar [23, 24, 12, 13, 8, 6, 5, 3, 3, 26]
    line [12, 0, 5, 1, 5, 3, 1, 4, 0, 7]
    line [9, 38, 4, 4, 11, 6, 6, 1, 4, 41]
```

### Daily New Issues
> **Legend:** 📊 Bar = New Help Wanted Issues

```mermaid
xychart-beta
    title "New Help Wanted Issues"
    x-axis ["03/11-03/13", "03/14-03/16", "03/17-03/19", "03/20-03/22", "03/23-03/25", "03/26-03/28", "03/29-03/31", "04/01-04/03", "04/04-04/06", "04/07-04/09"]
    y-axis "Count"
    bar [12, 18, 10, 1, 0, 0, 2, 0, 0, 2]
```

| Metric | Last 30 Days | Calculation |
| :--- | :--- | :--- |
| 🆕 New Help Wanted Issues | **45** | Number of new issues created with the `help wanted` label. |
| 🛠️ PRs Opened | **123** | Number of new PRs opened linked to a `help wanted` issue. |
| 🟣 PRs Merged | **38** | Number of those linked PRs that were successfully merged. |
| ⚪ PRs Closed (Unmerged) | **124** | Number of those linked PRs that were closed without merging (e.g. abandoned, stale). |
| 🔄 Issue to PR Conversion Rate | **30.9%** | Percentage of opened PRs that successfully get merged (`Merged / Opened`). |

## ⏱️ Efficiency & Bottlenecks
Measures the speed and responsiveness of the maintainer team in processing community PRs.

### Time to First Review (TTFR) Trend
> **Legend:** 📈 Line = Average Time to First Review (in hours) for PRs opened on that day

```mermaid
xychart-beta
    title "Average TTFR per Day (Hours)"
    x-axis ["03/11-03/13", "03/14-03/16", "03/17-03/19", "03/20-03/22", "03/23-03/25", "03/26-03/28", "03/29-03/31", "04/01-04/03", "04/04-04/06", "04/07-04/09"]
    y-axis "Hours"
    line [142.0, 290.5, 160.1, 244.7, 84.3, 38.7, 133.3, 67.2, 16.9, 7.1]
```

### Time to Merge (TTM) Trend
> **Legend:** 📈 Line = Average Time to Merge (in days) for PRs opened on that day

```mermaid
xychart-beta
    title "Average TTM per Day (Days)"
    x-axis ["03/11-03/13", "03/14-03/16", "03/17-03/19", "03/20-03/22", "03/23-03/25", "03/26-03/28", "03/29-03/31", "04/01-04/03", "04/04-04/06", "04/07-04/09"]
    y-axis "Days"
    line [6.3, 0, 11.0, 1.7, 11.4, 11.5, 2.9, 20.8, 0, 29.5]
```

| Metric | Average | Calculation |
| :--- | :--- | :--- |
| ⚡ Time to First Review (TTFR) | **162.1 hours** | Average time from PR creation until the first comment or review from a maintainer. (Target: < 24h) |
| 🚢 Time to Merge (TTM) | **13.6 days** | Average time from PR creation to when it is successfully merged into the codebase. |

## ❤️ Community Health
Indicates the general success and retention rate of contributors attempting to resolve issues.

### Drop-off Trend
> **Legend:** 📊 Bar = Number of PRs closed without merging (e.g. abandoned, stale)

```mermaid
xychart-beta
    title "PRs Closed Without Merge (Drop-off)"
    x-axis ["03/11-03/13", "03/14-03/16", "03/17-03/19", "03/20-03/22", "03/23-03/25", "03/26-03/28", "03/29-03/31", "04/01-04/03", "04/04-04/06", "04/07-04/09"]
    y-axis "Count"
    bar [9, 38, 4, 4, 11, 6, 6, 1, 4, 41]
```

| Metric | Rate | Calculation |
| :--- | :--- | :--- |
| 📉 Author Drop-off Rate | **76.5%** | Percentage of closed PRs that were abandoned or unmerged out of all resolved PRs (`Unmerged / Total Closed`). High drop-off could mean tasks are too hard or setup is complex. |

---
*Metrics maintained by automated daily script.*
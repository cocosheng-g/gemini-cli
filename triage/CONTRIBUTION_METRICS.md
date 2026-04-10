# 📈 Gemini CLI Contribution Metrics Dashboard

*Generated on 2026-04-10 (UTC). Reflects activity from the last 30 days.*

## 🚀 Velocity & Throughput
Tracks the sheer volume of contribution activity over the past 30 days.

### PRs Opened
> **Legend:** 📊 Bar = Number of PRs opened

```mermaid
xychart-beta
    title "PRs Opened (Last 30 Days)"
    x-axis ["Mar11-15", "Mar16-20", "Mar21-25", "Mar26-30", "Mar31-04", "Apr05-09"]
    y-axis "Count"
    bar [40, 25, 14, 10, 4, 29]
```

### PRs Merged
> **Legend:** 📊 Bar = Number of PRs successfully merged

```mermaid
xychart-beta
    title "PRs Merged (Last 30 Days)"
    x-axis ["Mar11-15", "Mar16-20", "Mar21-25", "Mar26-30", "Mar31-04", "Apr05-09"]
    y-axis "Count"
    bar [12, 6, 5, 3, 5, 7]
```

### PRs Closed (Unmerged)
> **Legend:** 📊 Bar = Number of PRs closed without merging (e.g., abandoned, stale)

```mermaid
xychart-beta
    title "PRs Closed Without Merging (Last 30 Days)"
    x-axis ["Mar11-15", "Mar16-20", "Mar21-25", "Mar26-30", "Mar31-04", "Apr05-09"]
    y-axis "Count"
    bar [46, 8, 12, 9, 5, 44]
```

### Daily New Issues
> **Legend:** 📊 Bar = New Help Wanted Issues

```mermaid
xychart-beta
    title "New Help Wanted Issues"
    x-axis ["Mar11-15", "Mar16-20", "Mar21-25", "Mar26-30", "Mar31-04", "Apr05-09"]
    y-axis "Count"
    bar [25, 15, 1, 2, 0, 2]
```

| Metric | Last 30 Days | Calculation |
| :--- | :--- | :--- |
| 🆕 New Help Wanted Issues | **45** | Number of new issues created with the `help wanted` label. |
| 🛠️ PRs Opened | **122** | Number of new PRs opened linked to a `help wanted` issue. |
| 🟣 PRs Merged | **38** | Number of those linked PRs that were successfully merged. |
| ⚪ PRs Closed (Unmerged) | **124** | Number of those linked PRs that were closed without merging (e.g. abandoned, stale). |
| 🔄 Issue to PR Conversion Rate | **31.1%** | Percentage of opened PRs that successfully get merged (`Merged / Opened`). |

## ⏱️ Efficiency & Bottlenecks
Measures the speed and responsiveness of the maintainer team in processing community PRs.

### Time to First Review (TTFR) Trend
> **Legend:** 📈 Line = Average Time to First Review (in hours) for PRs opened on that day

```mermaid
xychart-beta
    title "Average TTFR per Day (Hours)"
    x-axis ["Mar11-15", "Mar16-20", "Mar21-25", "Mar26-30", "Mar31-04", "Apr05-09"]
    y-axis "Hours"
    line [209.8, 211.8, 179.6, 61.5, 99.0, 9.2]
```

### Time to Merge (TTM) Trend
> **Legend:** 📈 Line = Average Time to Merge (in days) for PRs opened on that day

```mermaid
xychart-beta
    title "Average TTM per Day (Days)"
    x-axis ["Mar11-15", "Mar16-20", "Mar21-25", "Mar26-30", "Mar31-04", "Apr05-09"]
    y-axis "Days"
    line [6.3, 9.5, 11.4, 11.5, 17.2, 29.5]
```

| Metric | Average | Calculation |
| :--- | :--- | :--- |
| ⚡ Time to First Review (TTFR) | **163.7 hours** | Average time from PR creation until the first comment or review from a maintainer. (Target: < 24h) |
| 🚢 Time to Merge (TTM) | **13.6 days** | Average time from PR creation to when it is successfully merged into the codebase. |

## ❤️ Community Health
Indicates the general success and retention rate of contributors attempting to resolve issues.

| Metric | Rate | Calculation |
| :--- | :--- | :--- |
| 📉 Author Drop-off Rate | **76.5%** | Percentage of closed PRs that were abandoned or unmerged out of all resolved PRs (`Unmerged / Total Closed`). High drop-off could mean tasks are too hard or setup is complex. |

### 👥 Contributor Engagement
> **Legend:** 📊 Bar = Number of unique active contributors (opened, merged, or closed a PR)

```mermaid
xychart-beta
    title "Active Contributors"
    x-axis ["Mar11-15", "Mar16-20", "Mar21-25", "Mar26-30", "Mar31-04", "Apr05-09"]
    y-axis "Count"
    bar [67, 31, 23, 18, 11, 55]
```

> **Legend:** 📈 Line = Avg PRs Opened per Active Contributor

```mermaid
xychart-beta
    title "Avg PRs Opened per Contributor"
    x-axis ["Mar11-15", "Mar16-20", "Mar21-25", "Mar26-30", "Mar31-04", "Apr05-09"]
    y-axis "PRs"
    line [0.6, 0.8, 0.6, 0.6, 0.4, 0.5]
```

> **Legend:** 📈 Line = Avg PRs Merged per Active Contributor

```mermaid
xychart-beta
    title "Avg PRs Merged per Contributor"
    x-axis ["Mar11-15", "Mar16-20", "Mar21-25", "Mar26-30", "Mar31-04", "Apr05-09"]
    y-axis "PRs"
    line [0.2, 0.2, 0.2, 0.2, 0.5, 0.1]
```

| Metric | Value | Calculation |
| :--- | :--- | :--- |
| 🧑‍💻 Total Active Contributors | **150** | Number of unique human contributors who opened, merged, or closed a PR in the last 30 days. |
| 📈 Avg PRs Opened | **0.8** | Total PRs opened divided by total active contributors over 30 days. |
| 🎯 Avg PRs Merged | **0.3** | Total PRs merged divided by total active contributors over 30 days. |

---
*Metrics maintained by automated daily script.*
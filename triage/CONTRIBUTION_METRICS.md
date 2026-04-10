# 📈 Gemini CLI Contribution Metrics Dashboard

*Generated on 2026-04-10 (UTC). Reflects activity from the last 30 days.*

## 🚀 Velocity & Throughput
Tracks the sheer volume of contribution activity over the past 30 days.

### Daily Volume Activity
```mermaid
xychart-beta
    title "PRs Opened vs Merged vs Closed (Unmerged)"
    x-axis ["03-11", "03-12", "03-13", "03-14", "03-15", "03-16", "03-17", "03-18", "03-19", "03-20", "03-21", "03-22", "03-23", "03-24", "03-25", "03-26", "03-27", "03-28", "03-29", "03-30", "03-31", "04-01", "04-02", "04-03", "04-04", "04-05", "04-06", "04-07", "04-08", "04-09"]
    y-axis "Count"
    bar [6, 5, 7, 8, 5, 13, 5, 3, 6, 3, 5, 4, 2, 5, 2, 1, 2, 3, 2, 1, 2, 2, 1, 1, 0, 0, 3, 2, 7, 9]
    line [7, 3, 2, 0, 0, 0, 3, 1, 1, 1, 0, 0, 0, 2, 3, 1, 2, 0, 0, 0, 0, 1, 4, 0, 0, 0, 0, 0, 3, 2]
    line [2, 2, 2, 3, 36, 1, 1, 2, 2, 0, 3, 1, 3, 3, 4, 1, 1, 2, 3, 2, 3, 1, 1, 0, 1, 0, 3, 0, 4, 29]
```

### Daily New Issues
```mermaid
xychart-beta
    title "New Help Wanted Issues"
    x-axis ["03-11", "03-12", "03-13", "03-14", "03-15", "03-16", "03-17", "03-18", "03-19", "03-20", "03-21", "03-22", "03-23", "03-24", "03-25", "03-26", "03-27", "03-28", "03-29", "03-30", "03-31", "04-01", "04-02", "04-03", "04-04", "04-05", "04-06", "04-07", "04-08", "04-09"]
    y-axis "Count"
    bar [1, 5, 4, 3, 3, 11, 4, 8, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0]
```

| Metric | Last 30 Days | Calculation |
| :--- | :--- | :--- |
| 🆕 New Help Wanted Issues | **45** | Number of new issues created with the `help wanted` label. |
| 🛠️ PRs Opened | **123** | Number of new PRs opened linked to a `help wanted` issue. |
| 🟣 PRs Merged | **37** | Number of those linked PRs that were successfully merged. |
| ⚪ PRs Closed (Unmerged) | **124** | Number of those linked PRs that were closed without merging (e.g. abandoned, stale). |
| 🔄 Issue to PR Conversion Rate | **30.1%** | Percentage of opened PRs that successfully get merged (`Merged / Opened`). |

## ⏱️ Efficiency & Bottlenecks
Measures the speed and responsiveness of the maintainer team in processing community PRs.

### Time to First Review (TTFR) Trend
```mermaid
xychart-beta
    title "Average TTFR per Day (Hours)"
    x-axis ["03-11", "03-12", "03-13", "03-14", "03-15", "03-16", "03-17", "03-18", "03-19", "03-20", "03-21", "03-22", "03-23", "03-24", "03-25", "03-26", "03-27", "03-28", "03-29", "03-30", "03-31", "04-01", "04-02", "04-03", "04-04", "04-05", "04-06", "04-07", "04-08", "04-09"]
    y-axis "Hours"
    line [82.9, 214.0, 150.2, 162.4, 392.1, 281.1, 209.4, 234.5, 146.0, 37.1, 272.7, 177.9, 421.4, 140.5, 0.0, 0, 0.0, 96.7, 13.8, 0, 209.6, 162.8, 0.0, 134.3, 0, 0, 16.9, 27.7, 7.8, 6.3]
```

### Time to Merge (TTM) Trend
```mermaid
xychart-beta
    title "Average TTM per Day (Days)"
    x-axis ["03-11", "03-12", "03-13", "03-14", "03-15", "03-16", "03-17", "03-18", "03-19", "03-20", "03-21", "03-22", "03-23", "03-24", "03-25", "03-26", "03-27", "03-28", "03-29", "03-30", "03-31", "04-01", "04-02", "04-03", "04-04", "04-05", "04-06", "04-07", "04-08", "04-09"]
    y-axis "Days"
    line [3.1, 3.8, 21.2, 0, 0, 0, 11.0, 19.7, 2.4, 1.7, 0, 0, 0, 6.0, 14.9, 18.4, 8.1, 0, 0, 0, 0, 2.9, 20.8, 0, 0, 0, 0, 0, 20.3, 13.7]
```

| Metric | Average | Calculation |
| :--- | :--- | :--- |
| ⚡ Time to First Review (TTFR) | **162.1 hours** | Average time from PR creation until the first comment or review from a maintainer. (Target: < 24h) |
| 🚢 Time to Merge (TTM) | **11.3 days** | Average time from PR creation to when it is successfully merged into the codebase. |

## ❤️ Community Health
Indicates the general success and retention rate of contributors attempting to resolve issues.

### Drop-off Trend
```mermaid
xychart-beta
    title "PRs Closed Without Merge (Drop-off)"
    x-axis ["03-11", "03-12", "03-13", "03-14", "03-15", "03-16", "03-17", "03-18", "03-19", "03-20", "03-21", "03-22", "03-23", "03-24", "03-25", "03-26", "03-27", "03-28", "03-29", "03-30", "03-31", "04-01", "04-02", "04-03", "04-04", "04-05", "04-06", "04-07", "04-08", "04-09"]
    y-axis "Count"
    bar [2, 2, 2, 3, 36, 1, 1, 2, 2, 0, 3, 1, 3, 3, 4, 1, 1, 2, 3, 2, 3, 1, 1, 0, 1, 0, 3, 0, 4, 29]
```

| Metric | Rate | Calculation |
| :--- | :--- | :--- |
| 📉 Author Drop-off Rate | **77.0%** | Percentage of closed PRs that were abandoned or unmerged out of all resolved PRs (`Unmerged / Total Closed`). High drop-off could mean tasks are too hard or setup is complex. |

---
*Metrics maintained by automated daily script.*
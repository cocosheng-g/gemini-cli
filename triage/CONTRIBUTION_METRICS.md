# 📈 Gemini CLI Contribution Metrics Dashboard

*Generated on 2026-04-10 (UTC). Reflects activity from the last 30 days.*

## 🚀 Velocity & Throughput
Tracks the sheer volume of contribution activity over the past 30 days.

### PRs Opened
> **Legend:** 📊 Bar = Number of PRs opened

```mermaid
xychart-beta
    title "PRs Opened (Last 30 Days)"
    x-axis ["03-11", "  ", "   ", "03-14", "     ", "      ", "03-17", "        ", "         ", "03-20", "           ", "            ", "03-23", "              ", "               ", "03-26", "                 ", "                  ", "03-29", "                    ", "                     ", "04-01", "                       ", "                        ", "04-04", "                          ", "                           ", "04-07", "                             ", "                              "]
    y-axis "Count"
    bar [10, 5, 7, 7, 11, 6, 4, 7, 1, 7, 3, 3, 4, 3, 1, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0, 1, 2, 8, 5, 13]
```

### PRs Merged
> **Legend:** 📊 Bar = Number of PRs successfully merged

```mermaid
xychart-beta
    title "PRs Merged (Last 30 Days)"
    x-axis ["03-11", "  ", "   ", "03-14", "     ", "      ", "03-17", "        ", "         ", "03-20", "           ", "            ", "03-23", "              ", "               ", "03-26", "                 ", "                  ", "03-29", "                    ", "                     ", "04-01", "                       ", "                        ", "04-04", "                          ", "                           ", "04-07", "                             ", "                              "]
    y-axis "Count"
    bar [8, 4, 0, 0, 0, 0, 4, 1, 0, 1, 0, 0, 1, 1, 3, 1, 2, 0, 0, 0, 1, 1, 3, 0, 0, 0, 0, 1, 2, 4]
```

### PRs Closed (Unmerged)
> **Legend:** 📊 Bar = Number of PRs closed without merging (e.g., abandoned, stale)

```mermaid
xychart-beta
    title "PRs Closed Without Merging (Last 30 Days)"
    x-axis ["03-11", "  ", "   ", "03-14", "     ", "      ", "03-17", "        ", "         ", "03-20", "           ", "            ", "03-23", "              ", "               ", "03-26", "                 ", "                  ", "03-29", "                    ", "                     ", "04-01", "                       ", "                        ", "04-04", "                          ", "                           ", "04-07", "                             ", "                              "]
    y-axis "Count"
    bar [2, 3, 3, 3, 34, 1, 1, 3, 0, 3, 1, 0, 6, 4, 1, 0, 3, 3, 2, 1, 3, 0, 1, 0, 1, 2, 1, 3, 4, 34]
```

### Daily New Issues
> **Legend:** 📊 Bar = New Help Wanted Issues

```mermaid
xychart-beta
    title "New Help Wanted Issues"
    x-axis ["03-11", "  ", "   ", "03-14", "     ", "      ", "03-17", "        ", "         ", "03-20", "           ", "            ", "03-23", "              ", "               ", "03-26", "                 ", "                  ", "03-29", "                    ", "                     ", "04-01", "                       ", "                        ", "04-04", "                          ", "                           ", "04-07", "                             ", "                              "]
    y-axis "Count"
    bar [4, 5, 3, 3, 10, 5, 6, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
```

| Metric | Last 30 Days | Calculation |
| :--- | :--- | :--- |
| 🆕 New Help Wanted Issues | **45** | Number of new issues created with the `help wanted` label. |
| 🛠️ PRs Opened | **122** | Number of new PRs opened linked to a `help wanted` issue. |
| 🟣 PRs Merged | **38** | Number of those linked PRs that were successfully merged. |
| ⚪ PRs Closed (Unmerged) | **123** | Number of those linked PRs that were closed without merging (e.g. abandoned, stale). |
| 🔄 Issue to PR Conversion Rate | **31.1%** | Percentage of opened PRs that successfully get merged (`Merged / Opened`). |

## ⏱️ Efficiency & Bottlenecks
Measures the speed and responsiveness of the maintainer team in processing community PRs.

### Time to First Review (TTFR) Trend
> **Legend:** 📈 Line = Average Time to First Review (in hours) for PRs opened on that day

```mermaid
xychart-beta
    title "Average TTFR per Day (Hours)"
    x-axis ["03-11", "  ", "   ", "03-14", "     ", "      ", "03-17", "        ", "         ", "03-20", "           ", "            ", "03-23", "              ", "               ", "03-26", "                 ", "                  ", "03-29", "                    ", "                     ", "04-01", "                       ", "                        ", "04-04", "                          ", "                           ", "04-07", "                             ", "                              "]
    y-axis "Hours"
    line [156.7, 139.2, 143.1, 287.4, 283.1, 307.7, 175.2, 174.4, 0.0, 223.1, 237.2, 281.0, 177.7, 22.0, 0, 0.0, 96.7, 0.0, 27.6, 209.6, 162.8, 0.0, 134.3, 0, 0, 0.0, 25.4, 11.7, 0.0, 4.7]
```

### Time to Merge (TTM) Trend
> **Legend:** 📈 Line = Average Time to Merge (in days) for PRs opened on that day

```mermaid
xychart-beta
    title "Average TTM per Day (Days)"
    x-axis ["03-11", "  ", "   ", "03-14", "     ", "      ", "03-17", "        ", "         ", "03-20", "           ", "            ", "03-23", "              ", "               ", "03-26", "                 ", "                  ", "03-29", "                    ", "                     ", "04-01", "                       ", "                        ", "04-04", "                          ", "                           ", "04-07", "                             ", "                              "]
    y-axis "Days"
    line [3.1, 12.8, 0, 0, 0, 0, 13.2, 2.4, 0, 1.7, 0, 0, 3.1, 9.0, 14.9, 18.4, 8.1, 0, 0, 0, 2.9, 0.0, 27.7, 0, 0, 0, 0, 0.2, 30.4, 36.3]
```

| Metric | Average | Calculation |
| :--- | :--- | :--- |
| ⚡ Time to First Review (TTFR) | **163.7 hours** | Average time from PR creation until the first comment or review from a maintainer. (Target: < 24h) |
| 🚢 Time to Merge (TTM) | **13.6 days** | Average time from PR creation to when it is successfully merged into the codebase. |

## ❤️ Community Health
Indicates the general success and retention rate of contributors attempting to resolve issues.

| Metric | Rate | Calculation |
| :--- | :--- | :--- |
| 📉 Author Drop-off Rate | **76.4%** | Percentage of closed PRs that were abandoned or unmerged out of all resolved PRs (`Unmerged / Total Closed`). High drop-off could mean tasks are too hard or setup is complex. |

### 👥 Contributor Engagement
> **Legend:** 📊 Bar = Number of unique active contributors (opened, merged, or closed a PR)

```mermaid
xychart-beta
    title "Active Contributors"
    x-axis ["03-11", "  ", "   ", "03-14", "     ", "      ", "03-17", "        ", "         ", "03-20", "           ", "            ", "03-23", "              ", "               ", "03-26", "                 ", "                  ", "03-29", "                    ", "                     ", "04-01", "                       ", "                        ", "04-04", "                          ", "                           ", "04-07", "                             ", "                              "]
    y-axis "Count"
    bar [14, 10, 8, 10, 37, 7, 9, 8, 1, 7, 3, 3, 9, 7, 5, 3, 7, 4, 4, 2, 4, 2, 4, 0, 1, 2, 1, 8, 8, 41]
```

> **Legend:** 📈 Line = Avg PRs Opened per Active Contributor

```mermaid
xychart-beta
    title "Avg PRs Opened per Contributor"
    x-axis ["03-11", "  ", "   ", "03-14", "     ", "      ", "03-17", "        ", "         ", "03-20", "           ", "            ", "03-23", "              ", "               ", "03-26", "                 ", "                  ", "03-29", "                    ", "                     ", "04-01", "                       ", "                        ", "04-04", "                          ", "                           ", "04-07", "                             ", "                              "]
    y-axis "PRs"
    line [0.7, 0.5, 0.9, 0.7, 0.3, 0.9, 0.4, 0.9, 1.0, 1.0, 1.0, 1.0, 0.4, 0.4, 0.2, 0.7, 0.3, 0.5, 0.5, 1.0, 0.2, 1.0, 0.2, 0, 0.0, 0.5, 2.0, 1.0, 0.6, 0.3]
```

> **Legend:** 📈 Line = Avg PRs Merged per Active Contributor

```mermaid
xychart-beta
    title "Avg PRs Merged per Contributor"
    x-axis ["03-11", "  ", "   ", "03-14", "     ", "      ", "03-17", "        ", "         ", "03-20", "           ", "            ", "03-23", "              ", "               ", "03-26", "                 ", "                  ", "03-29", "                    ", "                     ", "04-01", "                       ", "                        ", "04-04", "                          ", "                           ", "04-07", "                             ", "                              "]
    y-axis "PRs"
    line [0.6, 0.4, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.0, 0.1, 0.0, 0.0, 0.1, 0.1, 0.6, 0.3, 0.3, 0.0, 0.0, 0.0, 0.2, 0.5, 0.8, 0, 0.0, 0.0, 0.0, 0.1, 0.2, 0.1]
```

| Metric | Value | Calculation |
| :--- | :--- | :--- |
| 🧑‍💻 Total Active Contributors | **150** | Number of unique human contributors who opened, merged, or closed a PR in the last 30 days. |
| 📈 Avg PRs Opened | **0.8** | Total PRs opened divided by total active contributors over 30 days. |
| 🎯 Avg PRs Merged | **0.3** | Total PRs merged divided by total active contributors over 30 days. |

---
*Metrics maintained by automated daily script.*
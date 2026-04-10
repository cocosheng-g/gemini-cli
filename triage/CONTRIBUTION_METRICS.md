# 📈 Gemini CLI Contribution Metrics Dashboard

*Generated on 2026-04-10 (UTC). Reflects activity from the last 30 days.*

## 🚀 Velocity & Throughput
Tracks the sheer volume of contribution activity over the past 30 days.

### PRs Opened vs Merged vs Closed (Unmerged)
> **Legend:** 📊 Bar = PRs Opened | 📈 Line 1 = PRs Merged | 📉 Line 2 = PRs Closed (Unmerged)

```mermaid
---
config:
  xyChart:
    showDataLabel: true
---
xychart-beta
    title "PR Activity (Mar 11 - Apr 09)"
    x-axis ["11", "12​", "13​​", "14​​​", "15​​​​", "16​​​​​", "17​​​​​​", "18​​​​​​​", "19​​​​​​​​", "20​​​​​​​​​", "21​​​​​​​​​​", "22​​​​​​​​​​​", "23​​​​​​​​​​​​", "24​​​​​​​​​​​​​", "25​​​​​​​​​​​​​​", "26​​​​​​​​​​​​​​​", "27​​​​​​​​​​​​​​​​", "28​​​​​​​​​​​​​​​​​", "29​​​​​​​​​​​​​​​​​​", "30​​​​​​​​​​​​​​​​​​​", "31​​​​​​​​​​​​​​​​​​​​", "01​​​​​​​​​​​​​​​​​​​​​", "02​​​​​​​​​​​​​​​​​​​​​​", "03​​​​​​​​​​​​​​​​​​​​​​​", "04​​​​​​​​​​​​​​​​​​​​​​​​", "05​​​​​​​​​​​​​​​​​​​​​​​​​", "06​​​​​​​​​​​​​​​​​​​​​​​​​​", "07​​​​​​​​​​​​​​​​​​​​​​​​​​​", "08​​​​​​​​​​​​​​​​​​​​​​​​​​​​", "09​​​​​​​​​​​​​​​​​​​​​​​​​​​​​"]
    y-axis "Count"
    bar [10, 7, 5, 7, 11, 6, 4, 7, 1, 7, 3, 3, 4, 3, 1, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0, 1, 2, 8, 5, 13]
    line [8, 4, 0, 0, 0, 0, 4, 1, 0, 1, 0, 0, 1, 2, 2, 2, 1, 0, 0, 0, 1, 1, 3, 0, 0, 0, 0, 1, 2, 4]
    line [2, 3, 3, 3, 34, 1, 1, 3, 0, 3, 1, 0, 6, 4, 1, 0, 3, 3, 2, 1, 3, 0, 1, 0, 1, 2, 1, 3, 4, 34]
```

### Daily New Issues
> **Legend:** 📊 Bar = New Help Wanted Issues

```mermaid
---
config:
  xyChart:
    showDataLabel: true
---
xychart-beta
    title "New Help Wanted Issues"
    x-axis ["11", "12​", "13​​", "14​​​", "15​​​​", "16​​​​​", "17​​​​​​", "18​​​​​​​", "19​​​​​​​​", "20​​​​​​​​​", "21​​​​​​​​​​", "22​​​​​​​​​​​", "23​​​​​​​​​​​​", "24​​​​​​​​​​​​​", "25​​​​​​​​​​​​​​", "26​​​​​​​​​​​​​​​", "27​​​​​​​​​​​​​​​​", "28​​​​​​​​​​​​​​​​​", "29​​​​​​​​​​​​​​​​​​", "30​​​​​​​​​​​​​​​​​​​", "31​​​​​​​​​​​​​​​​​​​​", "01​​​​​​​​​​​​​​​​​​​​​", "02​​​​​​​​​​​​​​​​​​​​​​", "03​​​​​​​​​​​​​​​​​​​​​​​", "04​​​​​​​​​​​​​​​​​​​​​​​​", "05​​​​​​​​​​​​​​​​​​​​​​​​​", "06​​​​​​​​​​​​​​​​​​​​​​​​​​", "07​​​​​​​​​​​​​​​​​​​​​​​​​​​", "08​​​​​​​​​​​​​​​​​​​​​​​​​​​​", "09​​​​​​​​​​​​​​​​​​​​​​​​​​​​​"]
    y-axis "Count"
    bar [5, 5, 3, 2, 10, 5, 6, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
```

| Metric | Last 30 Days | Target / Goal | Calculation |
| :--- | :--- | :--- | :--- |
| 🆕 New Help Wanted Issues | **45** | Steady / Growing | Number of new issues created with the `help wanted` label. |
| 🛠️ PRs Opened | **122** | - | Number of new PRs opened linked to a `help wanted` issue. |
| 🟣 PRs Merged | **38** | Track closely to Opened | Number of those linked PRs that were successfully merged. |
| ⚪ PRs Closed (Unmerged) | **123** | - | Number of those linked PRs that were closed without merging (e.g. abandoned, stale). |
| 🔄 Issue to PR Conversion Rate | **31.1%** | > 50% | Percentage of opened PRs that successfully get merged (`Merged / Opened`). |

## ⏱️ Efficiency & Bottlenecks
Measures the speed and responsiveness of the maintainer team in processing community PRs.

### Time to First Review (TTFR) Trend
> **Legend:** 📈 Line = Average Time to First Review (in hours) for PRs opened on that day

```mermaid
---
config:
  xyChart:
    showDataLabel: true
---
xychart-beta
    title "Average TTFR per Day (Hours)"
    x-axis ["11", "12​", "13​​", "14​​​", "15​​​​", "16​​​​​", "17​​​​​​", "18​​​​​​​", "19​​​​​​​​", "20​​​​​​​​​", "21​​​​​​​​​​", "22​​​​​​​​​​​", "23​​​​​​​​​​​​", "24​​​​​​​​​​​​​", "25​​​​​​​​​​​​​​", "26​​​​​​​​​​​​​​​", "27​​​​​​​​​​​​​​​​", "28​​​​​​​​​​​​​​​​​", "29​​​​​​​​​​​​​​​​​​", "30​​​​​​​​​​​​​​​​​​​", "31​​​​​​​​​​​​​​​​​​​​", "01​​​​​​​​​​​​​​​​​​​​​", "02​​​​​​​​​​​​​​​​​​​​​​", "03​​​​​​​​​​​​​​​​​​​​​​​", "04​​​​​​​​​​​​​​​​​​​​​​​​", "05​​​​​​​​​​​​​​​​​​​​​​​​​", "06​​​​​​​​​​​​​​​​​​​​​​​​​​", "07​​​​​​​​​​​​​​​​​​​​​​​​​​​", "08​​​​​​​​​​​​​​​​​​​​​​​​​​​​", "09​​​​​​​​​​​​​​​​​​​​​​​​​​​​​"]
    y-axis "Hours"
    line [156.7, 150.2, 129.4, 287.4, 283.1, 307.7, 175.2, 174.4, 0.0, 223.1, 237.2, 281.0, 177.7, 22.0, 0, 0.0, 96.7, 0.0, 27.6, 209.6, 162.8, 0.0, 134.3, 0, 0, 0.0, 25.4, 11.7, 0.0, 4.9]
```

### Time to Merge (TTM) Trend
> **Legend:** 📈 Line = Average Time to Merge (in days) for PRs successfully merged on that day

```mermaid
---
config:
  xyChart:
    showDataLabel: true
---
xychart-beta
    title "Average TTM per Day (Days)"
    x-axis ["11", "12​", "13​​", "14​​​", "15​​​​", "16​​​​​", "17​​​​​​", "18​​​​​​​", "19​​​​​​​​", "20​​​​​​​​​", "21​​​​​​​​​​", "22​​​​​​​​​​​", "23​​​​​​​​​​​​", "24​​​​​​​​​​​​​", "25​​​​​​​​​​​​​​", "26​​​​​​​​​​​​​​​", "27​​​​​​​​​​​​​​​​", "28​​​​​​​​​​​​​​​​​", "29​​​​​​​​​​​​​​​​​​", "30​​​​​​​​​​​​​​​​​​​", "31​​​​​​​​​​​​​​​​​​​​", "01​​​​​​​​​​​​​​​​​​​​​", "02​​​​​​​​​​​​​​​​​​​​​​", "03​​​​​​​​​​​​​​​​​​​​​​​", "04​​​​​​​​​​​​​​​​​​​​​​​​", "05​​​​​​​​​​​​​​​​​​​​​​​​​", "06​​​​​​​​​​​​​​​​​​​​​​​​​​", "07​​​​​​​​​​​​​​​​​​​​​​​​​​​", "08​​​​​​​​​​​​​​​​​​​​​​​​​​​​", "09​​​​​​​​​​​​​​​​​​​​​​​​​​​​​"]
    y-axis "Days"
    line [3.1, 12.8, 0, 0, 0, 0, 13.2, 2.4, 0, 1.7, 0, 0, 3.1, 16.5, 10.4, 9.5, 15.6, 0, 0, 0, 2.9, 0.0, 27.7, 0, 0, 0, 0, 0.2, 30.4, 36.3]
```

| Metric | Average | Target / Goal | Calculation |
| :--- | :--- | :--- | :--- |
| ⚡ Time to First Review (TTFR) | **162.1 hours** | < 168 hours (1 week) | Average time from PR creation until the first comment or review from a maintainer. |
| 🚢 Time to Merge (TTM) | **13.6 days** | < 14 days (2 weeks) | Average time from PR creation to when it is successfully merged into the codebase. |

## ❤️ Community Health
Indicates the general success and retention rate of contributors attempting to resolve issues.

| Metric | Rate | Target / Goal | Calculation |
| :--- | :--- | :--- | :--- |
| 📉 Author Drop-off Rate | **76.4%** | < 20% | Percentage of closed PRs that were abandoned or unmerged out of all resolved PRs (`Unmerged / Total Closed`). High drop-off could mean tasks are too hard or setup is complex. |

### 👥 Contributor Engagement
> **Legend:** 📊 Bar = Number of unique active contributors (opened, merged, closed, reviewed, commented, or committed)

```mermaid
---
config:
  xyChart:
    showDataLabel: true
---
xychart-beta
    title "Active Contributors"
    x-axis ["11", "12​", "13​​", "14​​​", "15​​​​", "16​​​​​", "17​​​​​​", "18​​​​​​​", "19​​​​​​​​", "20​​​​​​​​​", "21​​​​​​​​​​", "22​​​​​​​​​​​", "23​​​​​​​​​​​​", "24​​​​​​​​​​​​​", "25​​​​​​​​​​​​​​", "26​​​​​​​​​​​​​​​", "27​​​​​​​​​​​​​​​​", "28​​​​​​​​​​​​​​​​​", "29​​​​​​​​​​​​​​​​​​", "30​​​​​​​​​​​​​​​​​​​", "31​​​​​​​​​​​​​​​​​​​​", "01​​​​​​​​​​​​​​​​​​​​​", "02​​​​​​​​​​​​​​​​​​​​​​", "03​​​​​​​​​​​​​​​​​​​​​​​", "04​​​​​​​​​​​​​​​​​​​​​​​​", "05​​​​​​​​​​​​​​​​​​​​​​​​​", "06​​​​​​​​​​​​​​​​​​​​​​​​​​", "07​​​​​​​​​​​​​​​​​​​​​​​​​​​", "08​​​​​​​​​​​​​​​​​​​​​​​​​​​​", "09​​​​​​​​​​​​​​​​​​​​​​​​​​​​​"]
    y-axis "Count"
    bar [24, 24, 17, 20, 47, 27, 24, 23, 7, 17, 5, 10, 22, 21, 15, 22, 25, 11, 20, 13, 12, 11, 8, 3, 6, 10, 9, 19, 47, 78]
```

> **Legend:** 📈 Line = Avg PRs Opened per Active Contributor

```mermaid
---
config:
  xyChart:
    showDataLabel: true
---
xychart-beta
    title "Avg PRs Opened per Contributor"
    x-axis ["11", "12​", "13​​", "14​​​", "15​​​​", "16​​​​​", "17​​​​​​", "18​​​​​​​", "19​​​​​​​​", "20​​​​​​​​​", "21​​​​​​​​​​", "22​​​​​​​​​​​", "23​​​​​​​​​​​​", "24​​​​​​​​​​​​​", "25​​​​​​​​​​​​​​", "26​​​​​​​​​​​​​​​", "27​​​​​​​​​​​​​​​​", "28​​​​​​​​​​​​​​​​​", "29​​​​​​​​​​​​​​​​​​", "30​​​​​​​​​​​​​​​​​​​", "31​​​​​​​​​​​​​​​​​​​​", "01​​​​​​​​​​​​​​​​​​​​​", "02​​​​​​​​​​​​​​​​​​​​​​", "03​​​​​​​​​​​​​​​​​​​​​​​", "04​​​​​​​​​​​​​​​​​​​​​​​​", "05​​​​​​​​​​​​​​​​​​​​​​​​​", "06​​​​​​​​​​​​​​​​​​​​​​​​​​", "07​​​​​​​​​​​​​​​​​​​​​​​​​​​", "08​​​​​​​​​​​​​​​​​​​​​​​​​​​​", "09​​​​​​​​​​​​​​​​​​​​​​​​​​​​​"]
    y-axis "PRs"
    line [0.4, 0.3, 0.3, 0.3, 0.2, 0.2, 0.2, 0.3, 0.1, 0.4, 0.6, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.0, 0.0, 0.1, 0.2, 0.4, 0.1, 0.2]
```

> **Legend:** 📈 Line = Avg PRs Merged per Active Contributor

```mermaid
---
config:
  xyChart:
    showDataLabel: true
---
xychart-beta
    title "Avg PRs Merged per Contributor"
    x-axis ["11", "12​", "13​​", "14​​​", "15​​​​", "16​​​​​", "17​​​​​​", "18​​​​​​​", "19​​​​​​​​", "20​​​​​​​​​", "21​​​​​​​​​​", "22​​​​​​​​​​​", "23​​​​​​​​​​​​", "24​​​​​​​​​​​​​", "25​​​​​​​​​​​​​​", "26​​​​​​​​​​​​​​​", "27​​​​​​​​​​​​​​​​", "28​​​​​​​​​​​​​​​​​", "29​​​​​​​​​​​​​​​​​​", "30​​​​​​​​​​​​​​​​​​​", "31​​​​​​​​​​​​​​​​​​​​", "01​​​​​​​​​​​​​​​​​​​​​", "02​​​​​​​​​​​​​​​​​​​​​​", "03​​​​​​​​​​​​​​​​​​​​​​​", "04​​​​​​​​​​​​​​​​​​​​​​​​", "05​​​​​​​​​​​​​​​​​​​​​​​​​", "06​​​​​​​​​​​​​​​​​​​​​​​​​​", "07​​​​​​​​​​​​​​​​​​​​​​​​​​​", "08​​​​​​​​​​​​​​​​​​​​​​​​​​​​", "09​​​​​​​​​​​​​​​​​​​​​​​​​​​​​"]
    y-axis "PRs"
    line [0.3, 0.2, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.4, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.1]
```

| Metric | Value | Target / Goal | Calculation |
| :--- | :--- | :--- | :--- |
| 🧑‍💻 Total Active Contributors | **400** | Steady Growth | Number of unique human contributors who opened, merged, closed, reviewed, commented, or committed to a PR or Issue in the last 30 days. |
| 📈 Avg PRs Opened | **0.3** | > 1.5 PRs | Total PRs opened divided by total active contributors over 30 days. |
| 🎯 Avg PRs Merged | **0.1** | > 1.5 PRs | Total PRs merged divided by total active contributors over 30 days. |

---
*Metrics maintained by automated daily script.*
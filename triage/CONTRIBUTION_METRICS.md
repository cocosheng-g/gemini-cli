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
> **Legend:** 📈 Line = Average Time to First Review (in hours) for PRs reviewed on that day

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
    line [57.2, 322.3, 9.4, 155.9, 853.3, 170.5, 154.0, 18.6, 166.5, 298.7, 239.3, 229.2, 298.1, 253.1, 303.8, 244.4, 432.9, 232.3, 346.4, 308.2, 348.9, 234.5, 351.9, 1042.8, 270.1, 237.2, 0.0, 104.2, 251.5, 586.1]
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
| ⚡ Time to First Review (TTFR) | **376.3 hours** | < 168 hours (1 week) | Average time from PR creation until the first comment or review from a maintainer. |
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
    bar [39, 37, 24, 21, 52, 31, 32, 24, 15, 27, 9, 11, 24, 27, 21, 26, 29, 13, 21, 16, 14, 14, 9, 10, 6, 10, 9, 19, 49, 86]
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
    line [0.3, 0.2, 0.2, 0.3, 0.2, 0.2, 0.1, 0.3, 0.1, 0.3, 0.3, 0.3, 0.2, 0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.0, 0.1, 0.2, 0.4, 0.1, 0.2]
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
    line [0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.3, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0]
```

| Metric | Value | Target / Goal | Calculation |
| :--- | :--- | :--- | :--- |
| 🧑‍💻 Total Active Contributors | **405** | Steady Growth | Number of unique human contributors who opened, merged, closed, reviewed, commented, or committed to a PR or Issue in the last 30 days. |
| 📈 Avg PRs Opened | **0.3** | > 1.5 PRs | Total PRs opened divided by total active contributors over 30 days. |
| 🎯 Avg PRs Merged | **0.1** | > 1.5 PRs | Total PRs merged divided by total active contributors over 30 days. |

---
*Metrics maintained by automated daily script.*
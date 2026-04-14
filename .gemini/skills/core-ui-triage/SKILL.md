---
name: github-issue-triage
description: Analyzes and cleans up GitHub issues. DO NOT trigger this skill automatically. ONLY use when the user explicitly mentions "github-issue-triage", or explicitly asks to "triage issues", "clean up old issues", or "triage this issue".
---

# GitHub Issue Triage

This skill provides workflows for finding, analyzing, and triaging GitHub issues to maintain a clean and actionable backlog.

## Oncaller Manual: How to use this skill

This skill is designed to assist the weekly oncaller with triaging the issue backlog. You can run the automation scripts in two modes:

### 1. Dry-Run Mode (Recommended for testing)
Use this mode to preview the changes the automation *would* make without actually modifying the repository.
- **What it does:** Simulates the triage process, logs the intended actions (e.g., adding labels, unassigning users, closing PRs), but safely skips the API calls that modify state.
- **How to trigger:** When manually dispatching the workflow from the GitHub Actions UI, set the `dry_run` input to `true`. Or, if running scripts locally, append the `--dry-run` flag (e.g., `npm run triage -- --dry-run`).

### 2. Normal (Production) Mode
Use this mode to apply the triage changes directly to the repository.
- **What it does:** Automatically labels issues, unassigns inactive contributors, closes stale PRs, and posts automated comments to communicate these actions.
- **How to trigger:** This runs automatically via scheduled cron jobs. To run manually, dispatch the workflow with `dry_run` set to `false`.

## Phase 1: Discovery (Optional)

If the user asks you to "triage issues" or "clean up old issues" without providing a specific issue URL, you must first find candidate issues.

Run the following script to get a list of issues:
`node scripts/find_issues.cjs <owner/repo>` (e.g., `node scripts/find_issues.cjs google-gemini/gemini-cli`)

You may optionally pass a custom search string and limit.
`node scripts/find_issues.cjs <owner/repo> "<search_string>" <limit>`

Pick the first issue from the list to triage and proceed to Phase 2. If the user provided a specific issue URL, start at Phase 2 directly.

## Phase 2: Analysis

For the target issue, you must run the analysis script to gather metadata and determine staleness/inactivity heuristics.

Run:
`node scripts/analyze_issue.cjs <issue_url> "<optional_comma_separated_maintainers>"`

Read the JSON output carefully.
- If `is_stale` is `true`, the issue has already been marked as stale and should be closed according to the rules in Phase 3.
- Take note of `inactive_over_30_days`, `inactive_over_60_days`, `is_epic`, and other boolean flags.

## Phase 3: Triage Execution

After analyzing the issue and receiving the JSON output, you MUST consult the detailed triage rules to determine the next steps.

Read the rules in [references/triage_rules.md](references/triage_rules.md) and execute the appropriate steps. You must follow the steps sequentially.

If a step instructs you to **STOP EXECUTION**, you must conclude your work on this issue and not proceed to subsequent steps. If you are triaging a batch of issues, you may move on to the next issue in the list.

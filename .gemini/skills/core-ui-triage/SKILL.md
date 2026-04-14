---
name: github-issue-triage
description: Analyzes and cleans up GitHub issues. DO NOT trigger this skill automatically. ONLY use when the user explicitly mentions "github-issue-triage", or explicitly asks to "triage issues", "clean up old issues", or "triage this issue".
---

# GitHub Issue Triage

This skill provides workflows for finding, analyzing, and triaging GitHub issues to maintain a clean and actionable backlog.

## Oncaller Manual: How to use this skill

This skill is designed to assist the weekly oncaller with triaging the issue backlog.

### 1. Setup

Before using this skill or its associated scripts, you must check out the correct branch where these tools are maintained.

```bash
git checkout automation/core-ui-triage
```
* **Explanation:** All the required triage scripts, policies, and markdown rules live on this branch.

### 2. Triage with Dry-Run Mode (Recommended for testing)

Use this mode to preview the changes the automation *would* make without actually modifying the repository. Simulates the triage process, logs the intended actions (e.g., adding labels, unassigning users, closing PRs), but safely skips the API calls that modify state.

**Option A (Plan Mode via CLI):**
```bash
gemini --approval-mode plan
# Then ask: "triage issue #123"
```
* **Explanation:** The agent will analyze the issue and propose actions in a written plan without executing modifying shell commands.

**Option B (Natural Language via CLI):**
```text
Activate the github-issue-triage skill and triage issue #123 in dry-run mode. Do not execute any modifying shell commands, just output the actions you would take.
```
* **Explanation:** By explicitly instructing the agent, it will bypass modifying commands.

**Option C (Local Scripts):**
```bash
npm run triage -- --dry-run
```
* **Explanation:** If running scripts locally in your terminal, append the `--dry-run` flag.

**Option D (GitHub Actions):**
* **Explanation:** When manually dispatching the workflow from the GitHub Actions UI, set the `dry_run` input to `true`.

### 3. Triage with Normal (Production) Mode

Use this mode to apply the triage changes directly to the repository. It automatically labels issues, unassigns inactive contributors, closes stale PRs, and posts automated comments to communicate these actions.

**Option A (Interactive CLI):**
```bash
gemini
# Then ask: "triage issue #123"
```
* **Explanation:** The agent will fully execute the triage rules, including making API calls to modify the issue state.

**Option B (GitHub Actions / Cron):**
* **Explanation:** This runs automatically via scheduled cron jobs. To run manually, dispatch the workflow from the GitHub Actions UI with `dry_run` set to `false`.

## Phase 1: Discovery (Optional)

If the user asks you to "triage issues" or "clean up old issues" without providing a specific issue URL, you must first find candidate issues within the scope of this skill.

This skill ONLY triages issues that match the following criteria:
- State: Open
- Labels: `area/core`, `area/extensions`, or `area/site`
- Sorted by: Recently updated

To retrieve the list of candidate issues, run the following GitHub CLI command:
`gh issue list --repo google-gemini/gemini-cli --search "is:issue state:open label:area/core,area/extensions,area/site sort:updated-desc"`

Pick the first issue from the list to triage and proceed to Phase 2. If the user provided a specific issue URL, start at Phase 2 directly.

## Phase 2: Analysis

For the target issue, you must run the analysis script to gather metadata and determine staleness/inactivity heuristics.

Run:
`node .gemini/skills/core-ui-triage/scripts/analyze_issue.cjs <issue_url> "<optional_comma_separated_maintainers>"`

Read the JSON output carefully.
- If `is_stale` is `true`, the issue has already been marked as stale and should be closed according to the rules in Phase 3.
- Take note of `inactive_over_30_days`, `inactive_over_60_days`, `is_epic`, and other boolean flags.

## Phase 3: Triage Execution

After analyzing the issue and receiving the JSON output, you MUST consult the detailed triage rules to determine the next steps.

Read the rules in [references/triage_rules.md](references/triage_rules.md) and execute the appropriate steps. You must follow the steps sequentially.

If a step instructs you to **STOP EXECUTION**, you must conclude your work on this issue and not proceed to subsequent steps. If you are triaging a batch of issues, you may move on to the next issue in the list.

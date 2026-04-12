# 🔎 Gemini CLI Help Wanted Triage Dashboard

*Last Synchronized: 2026-04-12 19:39 (UTC)*

> This dashboard tracks the status of `help wanted` issues and their linked PRs to help maintainers efficiently review external contributions, unblock stale items, and ensure timely feedback.

**Total Issues Tracked: 180 open issues**

## 🚨 Needs Oncaller Attention

<details>
<summary><b>🆕 Awaiting Reviewer Pickup (19)</b> — <i>Help contributors get their code merged!</i></summary>

**These contributors are waiting for your feedback! All tests are passing and there are no conflicts. Please try to pick up PRs with the oldest last update time first.**

| Issue | Linked PR | Last Update |
| :--- | :--- | :--- |
| [#22591 fix(cli): mapToDisplay uses unbounded JSON.stringify for ErroredToolCall description](https://github.com/google-gemini/gemini-cli/issues/22591) | [#22594](https://github.com/google-gemini/gemini-cli/pull/22594) | `2026-04-08` |
| [#19713 Fix unsafe type assertions in CLI Config (Phase 3.1)](https://github.com/google-gemini/gemini-cli/issues/19713) | [#24905](https://github.com/google-gemini/gemini-cli/pull/24905) | `2026-04-09` |
| [#20385 Terminal output flooded with repeated '0c/' string](https://github.com/google-gemini/gemini-cli/issues/20385) | [#24596](https://github.com/google-gemini/gemini-cli/pull/24596) | `2026-04-09` |
| [#21546 web_fetch: pressing Ctrl+C while a URL is loading causes silent retries instead of immediate cancellation](https://github.com/google-gemini/gemini-cli/issues/21546) | [#24320](https://github.com/google-gemini/gemini-cli/pull/24320) | `2026-04-09` |
| [#22417 CLI accepts positional prompt with --prompt-interactive and handles the conflict inconsistently](https://github.com/google-gemini/gemini-cli/issues/22417) | [#22418](https://github.com/google-gemini/gemini-cli/pull/22418) | `2026-04-09` |
| [#22589 fix(cli): all Executing subagent tool calls dropped from UI state, breaking task-tree hierarchy](https://github.com/google-gemini/gemini-cli/issues/22589) | [#22590](https://github.com/google-gemini/gemini-cli/pull/22590) | `2026-04-09` |
| [#22757 A GEMINI.md file already exists but empty and never commited](https://github.com/google-gemini/gemini-cli/issues/22757) | [#25010](https://github.com/google-gemini/gemini-cli/pull/25010) | `2026-04-09` |
| [#22932 `/extensions update ...` needs meaningful version info.](https://github.com/google-gemini/gemini-cli/issues/22932) | [#23105](https://github.com/google-gemini/gemini-cli/pull/23105) | `2026-04-09` |
| [#16391 Bug: Clickable URLs in inline Markdown include trailing punctuation especially Chinese punctuations, leading to broken navigation](https://github.com/google-gemini/gemini-cli/issues/16391) | [#25098](https://github.com/google-gemini/gemini-cli/pull/25098) | `2026-04-10` |
| [#19919 "Failed to persist policy" error despite correct permissions](https://github.com/google-gemini/gemini-cli/issues/19919) | [#21541](https://github.com/google-gemini/gemini-cli/pull/21541) | `2026-04-10` |
| [#20968 Windows PowerShell Output Encoding Bug](https://github.com/google-gemini/gemini-cli/issues/20968) | [#25102](https://github.com/google-gemini/gemini-cli/pull/25102) | `2026-04-10` |
| [#21686 Typing unmapped keys in Vim Normal mode inserts characters into input field](https://github.com/google-gemini/gemini-cli/issues/21686) | [#25139](https://github.com/google-gemini/gemini-cli/pull/25139) | `2026-04-10` |
| [#22421 fix(cli): /chat subcommand usage strings incorrectly reference /resume](https://github.com/google-gemini/gemini-cli/issues/22421) | [#25091](https://github.com/google-gemini/gemini-cli/pull/25091) | `2026-04-10` |
| [#24211 Hardcoded padding in terminal title causes trailing spaces in tmux pane_title](https://github.com/google-gemini/gemini-cli/issues/24211) | [#25109](https://github.com/google-gemini/gemini-cli/pull/25109) | `2026-04-10` |
| [#18727 Already selected allow for this session, but still prompted for each operation](https://github.com/google-gemini/gemini-cli/issues/18727) | [#25176](https://github.com/google-gemini/gemini-cli/pull/25176) | `2026-04-11` |
| [#18152 the dark grey color used for past commands has very low contrast and is difficult to read.](https://github.com/google-gemini/gemini-cli/issues/18152) | [#25223](https://github.com/google-gemini/gemini-cli/pull/25223) | `2026-04-12` |
| [#19758 ![high](https://www.gstatic.com/codereviewagent/high-priority.svg)](https://github.com/google-gemini/gemini-cli/issues/19758) | [#25222](https://github.com/google-gemini/gemini-cli/pull/25222) | `2026-04-12` |
| [#21370 bug: Linuxbrew installations not detected in getInstallationInfo](https://github.com/google-gemini/gemini-cli/issues/21370) | [#21376](https://github.com/google-gemini/gemini-cli/pull/21376) | `2026-04-12` |
| [#22351 Improve diagnostics and error handling for malformed streaming responses](https://github.com/google-gemini/gemini-cli/issues/22351) | [#22352](https://github.com/google-gemini/gemini-cli/pull/22352) | `2026-04-12` |
</details>

<details>
<summary><b>🛡️ Specialized Approval Required (22)</b> — <i>Specialized approval required.</i></summary>

**Criteria: PRs requesting review from specialized teams (e.g., docs, prompts).**

| Issue | Linked PR | Required Teams | Human Reviewers | Status |
| :--- | :--- | :--- | :--- | :--- |
| [#16122 Feature Request: Add gemini update command](https://github.com/google-gemini/gemini-cli/issues/16122) | [#24080](https://github.com/google-gemini/gemini-cli/pull/24080) | `gemini-cli-askmode-approvers` | @mrpmohiburrahman | 👀 Needs Maintainer Approval |
| [#18708 feat: Add /undo command to revert last conversation turn](https://github.com/google-gemini/gemini-cli/issues/18708) | [#20027](https://github.com/google-gemini/gemini-cli/pull/20027) | `gemini-cli-askmode-approvers` | @mrpmohiburrahman | 👀 Needs Maintainer Approval |
| [#19717 Fix unsafe type assertions in VS Code Companion (Phase 4.2)](https://github.com/google-gemini/gemini-cli/issues/19717) | [#19815](https://github.com/google-gemini/gemini-cli/pull/19815) | `gemini-cli-askmode-approvers`, `gemini-cli-prompt-approvers` | @Adib234, @mrpmohiburrahman | 👀 Needs Maintainer Approval |
| [#18067 Feature Proposal: Unified Native Voice Input Architecture (Local-First)](https://github.com/google-gemini/gemini-cli/issues/18067) | [#18499](https://github.com/google-gemini/gemini-cli/pull/18499) | `gemini-cli-docs` | @jacob314, @mrpmohiburrahman, @scidomino | 👀 Needs Maintainer Approval |
| [#18751 feat(ui): support custom preferred themes for automatic light/dark switching](https://github.com/google-gemini/gemini-cli/issues/18751) | [#18753](https://github.com/google-gemini/gemini-cli/pull/18753) | `gemini-cli-docs` | _None_ | 👀 Needs Maintainer Review |
| [#19969 Provide a way to control the standard names of hooks and skills folder via gemini-extension.json of an extension](https://github.com/google-gemini/gemini-cli/issues/19969) | [#25008](https://github.com/google-gemini/gemini-cli/pull/25008) | `gemini-cli-docs` | _None_ | 👀 Needs Maintainer Review |
| [#20404 Keybindings Customization](https://github.com/google-gemini/gemini-cli/issues/20404) | [#25227](https://github.com/google-gemini/gemini-cli/pull/25227) | `gemini-cli-docs` | _None_ | 👀 Needs Maintainer Review |
| [#20500 feat(cli): add mention view shortcuts](https://github.com/google-gemini/gemini-cli/issues/20500) | [#25060](https://github.com/google-gemini/gemini-cli/pull/25060) | `gemini-cli-docs` | _None_ | 👀 Needs Maintainer Review |
| [#20847 Feature request: --session-id flag to set session UUID at launch](https://github.com/google-gemini/gemini-cli/issues/20847) | [#24976](https://github.com/google-gemini/gemini-cli/pull/24976) | `gemini-cli-docs` | _None_ | 👀 Needs Maintainer Review |
| [#21036 UX Improvement for /chat save.](https://github.com/google-gemini/gemini-cli/issues/21036) | [#21439](https://github.com/google-gemini/gemini-cli/pull/21439) | `gemini-cli-docs` | _None_ | 👀 Needs Maintainer Review |
| [#21084 External editor support: unclear error messages, missing editors, incomplete documentation](https://github.com/google-gemini/gemini-cli/issues/21084) | [#21090](https://github.com/google-gemini/gemini-cli/pull/21090) | `gemini-cli-docs` | @jacob314 | 👀 Needs Maintainer Approval |
| [#22928 [Feature Request] Option to hide '/skills' from the primary slash command menu](https://github.com/google-gemini/gemini-cli/issues/22928) | [#25178](https://github.com/google-gemini/gemini-cli/pull/25178) | `gemini-cli-docs` | _None_ | 👀 Needs Maintainer Review |
| [#12345 Add AGENTS.md to the context filename list by default](https://github.com/google-gemini/gemini-cli/issues/12345) | [#24913](https://github.com/google-gemini/gemini-cli/pull/24913) | `gemini-cli-docs`, `gemini-cli-prompt-approvers` | _None_ | 👀 Needs Maintainer Review |
| [#17235 Missing JSON schema key intermittently](https://github.com/google-gemini/gemini-cli/issues/17235) | [#21963](https://github.com/google-gemini/gemini-cli/pull/21963) | `gemini-cli-prompt-approvers` | _None_ | 👀 Needs Maintainer Review |
| [#24933 Add `/rewind <user-message-index>` to rewind to a specific message](https://github.com/google-gemini/gemini-cli/issues/24933) | [#25150](https://github.com/google-gemini/gemini-cli/pull/25150) | `gemini-cli-docs` | _None_ | ✍️ Needs Author Update (Comments) |
| [#24838 StreamableHTTPTransport fails when endpoint requires POST (e.g., n8n native MCP)](https://github.com/google-gemini/gemini-cli/issues/24838) | [#24847](https://github.com/google-gemini/gemini-cli/pull/24847) | `gemini-cli-prompt-approvers` | @cocosheng-g | ✍️ Needs Author Update (Comments) |
| [#11462 Consider adding visual regression testing for terminal UI components](https://github.com/google-gemini/gemini-cli/issues/11462) | [#20695](https://github.com/google-gemini/gemini-cli/pull/20695) | `gemini-cli-askmode-approvers` | @hoteye | 🔴 Test Failure |
| [#19649 extend /copy to capture output also from slash commands](https://github.com/google-gemini/gemini-cli/issues/19649) | [#19825](https://github.com/google-gemini/gemini-cli/pull/19825) | `gemini-cli-askmode-approvers` | @lesteral, @mrpmohiburrahman | 🔴 Merge Conflict |
| [#21221 Proposal: Interruptible responses for experimental voice mode](https://github.com/google-gemini/gemini-cli/issues/21221) | [#21226](https://github.com/google-gemini/gemini-cli/pull/21226) | `gemini-cli-docs` | _None_ | 🔴 Merge Conflict |
| [#22035 Allow wrapping tool descriptions to prevent truncation in the UI](https://github.com/google-gemini/gemini-cli/issues/22035) | [#21964](https://github.com/google-gemini/gemini-cli/pull/21964) | `gemini-cli-docs` | _None_ | 🔴 Merge Conflict |
| [#19711 Fix unsafe type assertions in Core Tool Execution (Phase 2.1)](https://github.com/google-gemini/gemini-cli/issues/19711) | [#19755](https://github.com/google-gemini/gemini-cli/pull/19755) | `gemini-cli-prompt-approvers` | @devr0306 | 🔴 Merge Conflict |
| [#20755 Shell Tool Trailing Newline Trimming](https://github.com/google-gemini/gemini-cli/issues/20755) | [#23705](https://github.com/google-gemini/gemini-cli/pull/23705) | `gemini-cli-prompt-approvers` | @mrpmohiburrahman | 🔴 Merge Conflict |
</details>

<details>
<summary><b>🚩 Stale Assignments (0)</b> — <i>Auto-cleanup.</i></summary>

**Criteria: Assigned issues with no open PR, idle for >14 days.**

| Issue | Assignee | Days Stale |
| :--- | :--- | :--- |
| - | - | - |
</details>

<details>
<summary><b>🚧 Blocked & Stale PRs (0)</b> — <i>Auto-cleanup.</i></summary>

**Criteria: PRs with conflicts or failures untouched for >14 days will receive a warning comment tagging the author. If there is no response for 1 week, it will be considered blocked & stale and auto-cleaned up.**

| Issue | PR | Reason | Author | Days Stale |
| :--- | :--- | :--- | :--- | :--- |
| - | - | - | - | - |
</details>

## 🛠️ Active Development

<details>
<summary><b>⌛ Awaiting Reviewer Follow-up (5)</b> — <i>Reviewers, please follow up.</i></summary>

**Criteria: Review in progress, author has responded to latest feedback.**

| Issue | Linked PR | Reviewers | Status | Last Update |
| :--- | :--- | :--- | :--- | :--- |
| [#20948 Suggestion: Feature Request: Add "Last Edited Buffer" to command history to prevent data loss on accidental deletion.](https://github.com/google-gemini/gemini-cli/issues/20948) | [#21215](https://github.com/google-gemini/gemini-cli/pull/21215) | @devr0306 | Author Updated | `2026-04-10` |
| [#15503 feat: github colorblind themes](https://github.com/google-gemini/gemini-cli/issues/15503) | [#15504](https://github.com/google-gemini/gemini-cli/pull/15504) | @cocosheng-g | Author Updated | `2026-04-11` |
| [#24893 bug: fetchJson allows unbounded redirects due to post-increment operator](https://github.com/google-gemini/gemini-cli/issues/24893) | [#24896](https://github.com/google-gemini/gemini-cli/pull/24896) | @scidomino | Author Updated | `2026-04-11` |
| [#18023 Auto update with pnpm installation doesn't work well](https://github.com/google-gemini/gemini-cli/issues/18023) | [#22748](https://github.com/google-gemini/gemini-cli/pull/22748) | @cocosheng-g | Author Updated | `2026-04-12` |
| [#24898 Gemini CLI crashes on an SQL INSERT (I think) in prompt](https://github.com/google-gemini/gemini-cli/issues/24898) | [#25009](https://github.com/google-gemini/gemini-cli/pull/25009) | @scidomino | Author Updated | `2026-04-12` |
</details>

<details>
<summary><b>✍️ Awaiting Author Action (6)</b> — <i>Waiting for contributor.</i></summary>

**Criteria: Reviewer acted last, waiting for contributor to address comments.**

| Issue | Linked PR | Reviewers | Last Feedback |
| :--- | :--- | :--- | :--- |
| [#20655 Token estimation falls through to generic fallback for audio/video parts](https://github.com/google-gemini/gemini-cli/issues/20655) | [#20658](https://github.com/google-gemini/gemini-cli/pull/20658) | @mrpmohiburrahman | `2026-04-05` |
| [#22610 bug: ui.loadingPhrases: 'off' is ignored by the UI](https://github.com/google-gemini/gemini-cli/issues/22610) | [#22618](https://github.com/google-gemini/gemini-cli/pull/22618) | _None (Team only)_ | `2026-04-09` |
| [#22612 bug: Bun runtime fails to keep child processes alive due to 'detached: true'](https://github.com/google-gemini/gemini-cli/issues/22612) | [#22620](https://github.com/google-gemini/gemini-cli/pull/22620) | _None (Team only)_ | `2026-04-09` |
| [#22321 Feature Request: Add 'list' subcommand to '/commands' to show loaded command files](https://github.com/google-gemini/gemini-cli/issues/22321) | [#22324](https://github.com/google-gemini/gemini-cli/pull/22324) | @cocosheng-g, @jkcinouye, @marsam2489-lang | `2026-04-12` |
| [#22611 bug: Stale 'Thinking...' state persists after response completion](https://github.com/google-gemini/gemini-cli/issues/22611) | [#22619](https://github.com/google-gemini/gemini-cli/pull/22619) | @cocosheng-g | `2026-04-12` |
| [#24337 fix(cli): make slash-command IDE status subscription cleanup-safe](https://github.com/google-gemini/gemini-cli/issues/24337) | [#24397](https://github.com/google-gemini/gemini-cli/pull/24397) | @scidomino | `2026-04-12` |
</details>

<details>
<summary><b>🛠️ Active Development: Recently Assigned (64)</b> — <i>Assigned < 14 days ago.</i></summary>

**Criteria: Issues assigned < 14 days ago, no PR yet.**

| Issue | Assignee | Last Update |
| :--- | :--- | :--- |
| [#15585 Avoid Ambiguous Width Characters](https://github.com/google-gemini/gemini-cli/issues/15585) | @jacob314 | `2026-03-30` |
| [#18390 Add vim mode cursor shape indicator and setting](https://github.com/google-gemini/gemini-cli/issues/18390) | @PyaaZz | `2026-03-30` |
| [#15383 Policy engine docs and behavior mismatch](https://github.com/google-gemini/gemini-cli/issues/15383) | @kotaitos | `2026-04-04` |
| [#16359 Improve handling of unrecognized keys in settings.json](https://github.com/google-gemini/gemini-cli/issues/16359) | @sky021 | `2026-04-04` |
| [#11707 Fix flaky file-system.test.ts: should replace multiple instances of a string](https://github.com/google-gemini/gemini-cli/issues/11707) | @rishisulakhe | `2026-04-06` |
| [#20385 Terminal output flooded with repeated '0c/' string](https://github.com/google-gemini/gemini-cli/issues/20385) | @Aaxhirrr | `2026-04-06` |
| [#18444 feat: Support default values in extension configuration prompts](https://github.com/google-gemini/gemini-cli/issues/18444) | @TravisHaa | `2026-04-07` |
| [#18152 the dark grey color used for past commands has very low contrast and is difficult to read.](https://github.com/google-gemini/gemini-cli/issues/18152) | @Nixxx19 | `2026-04-08` |
| [#19713 Fix unsafe type assertions in CLI Config (Phase 3.1)](https://github.com/google-gemini/gemini-cli/issues/19713) | @skainguyen1412 | `2026-04-08` |
| [#19734 Fix unsafe type assertions in CLI UI (Phase 6)](https://github.com/google-gemini/gemini-cli/issues/19734) | @akanoao | `2026-04-08` |
| [#19758 ![high](https://www.gstatic.com/codereviewagent/high-priority.svg)](https://github.com/google-gemini/gemini-cli/issues/19758) | @Nixxx19 | `2026-04-08` |
| [#19875 Ability to specify a model name within a custom /command](https://github.com/google-gemini/gemini-cli/issues/19875) | @mrinank1301 | `2026-04-08` |
| [#20647 Feature Request: Standardize Extension Command Formatting and Introduce Hierarchical Menus](https://github.com/google-gemini/gemini-cli/issues/20647) | @Famous077 | `2026-04-08` |
| [#20761 add Vertex AI region override to support preview models](https://github.com/google-gemini/gemini-cli/issues/20761) | @Famous077 | `2026-04-08` |
| [#21216 feat(cli): introduce experimental voice mode architecture skeleton](https://github.com/google-gemini/gemini-cli/issues/21216) | @Sangini-spec | `2026-04-08` |
| [#21277 [FEATURE PROPOSAL]: Persistent Session Scratchpad via /memo command](https://github.com/google-gemini/gemini-cli/issues/21277) | @ProthamD | `2026-04-08` |
| [#21297 bug(command/skills): Interactive Consent Dialog Persists After Successful Workspace Skill Installation](https://github.com/google-gemini/gemini-cli/issues/21297) | @manavmax | `2026-04-08` |
| [#21370 bug: Linuxbrew installations not detected in getInstallationInfo](https://github.com/google-gemini/gemini-cli/issues/21370) | @Aarchi-07 | `2026-04-08` |
| [#21389 Make Jetbrains IDEs as editor options](https://github.com/google-gemini/gemini-cli/issues/21389) | @SoLoHiC | `2026-04-08` |
| [#22351 Improve diagnostics and error handling for malformed streaming responses](https://github.com/google-gemini/gemini-cli/issues/22351) | @junaiddshaukat | `2026-04-08` |
| [#22417 CLI accepts positional prompt with --prompt-interactive and handles the conflict inconsistently](https://github.com/google-gemini/gemini-cli/issues/22417) | @AshwinSaklecha | `2026-04-08` |
| [#22490 Feature: Configurable window title length and padding options](https://github.com/google-gemini/gemini-cli/issues/22490) | @daehyeok | `2026-04-08` |
| [#22589 fix(cli): all Executing subagent tool calls dropped from UI state, breaking task-tree hierarchy](https://github.com/google-gemini/gemini-cli/issues/22589) | @TravisHaa | `2026-04-08` |
| [#22591 fix(cli): mapToDisplay uses unbounded JSON.stringify for ErroredToolCall description](https://github.com/google-gemini/gemini-cli/issues/22591) | @TravisHaa | `2026-04-08` |
| [#22757 A GEMINI.md file already exists but empty and never commited](https://github.com/google-gemini/gemini-cli/issues/22757) | @student-ankitpandit | `2026-04-08` |
| [#15840 Alternate Buffer SettingsDialog](https://github.com/google-gemini/gemini-cli/issues/15840) | @psinha40898 | `2026-04-09` |
| [#16530 Robust WSL Support](https://github.com/google-gemini/gemini-cli/issues/16530) | @ChandanKT-git | `2026-04-09` |
| [#17834 Website landing and extensions page flash when theme is set to light](https://github.com/google-gemini/gemini-cli/issues/17834) | @PrafulVRaj | `2026-04-09` |
| [#19919 "Failed to persist policy" error despite correct permissions](https://github.com/google-gemini/gemini-cli/issues/19919) | @krishdef7 | `2026-04-09` |
| [#20364 feat(cli): Add /mds command to view memory and agent files](https://github.com/google-gemini/gemini-cli/issues/20364) | @Oerum | `2026-04-09` |
| [#20908 Gemini CLI should have a repo provided 'recommended extensions' configuration](https://github.com/google-gemini/gemini-cli/issues/20908) | @manas-raj999 | `2026-04-09` |
| [#21527 Failed to check if file is binary: /home/sumeet/korl-webapp-next/skills/typescript-expert EISDIR: illegal operation on a directory, read │ │ ⚠ Failed to check if file is binary: /home/sumeet/korl-webapp-next/skills/web-performance-optimization EISDIR: ille](https://github.com/google-gemini/gemini-cli/issues/21527) | @ProthamD | `2026-04-09` |
| [#21546 web_fetch: pressing Ctrl+C while a URL is loading causes silent retries instead of immediate cancellation](https://github.com/google-gemini/gemini-cli/issues/21546) | @ProthamD | `2026-04-09` |
| [#21548 Disabling of extensions doesn't work](https://github.com/google-gemini/gemini-cli/issues/21548) | @ProthamD | `2026-04-09` |
| [#21764 Include available sessions in error when --resume gets invalid ID](https://github.com/google-gemini/gemini-cli/issues/21764) | @Zahed-Riyaz | `2026-04-09` |
| [#21993 Dev tools: filtering and searching](https://github.com/google-gemini/gemini-cli/issues/21993) | @M-DEV-1 | `2026-04-09` |
| [#22185 Copy + pasta](https://github.com/google-gemini/gemini-cli/issues/22185) | @manavmax | `2026-04-09` |
| [#22421 fix(cli): /chat subcommand usage strings incorrectly reference /resume](https://github.com/google-gemini/gemini-cli/issues/22421) | @skainguyen1412 | `2026-04-09` |
| [#22932 `/extensions update ...` needs meaningful version info.](https://github.com/google-gemini/gemini-cli/issues/22932) | @Br1an67 | `2026-04-09` |
| [#24211 Hardcoded padding in terminal title causes trailing spaces in tmux pane_title](https://github.com/google-gemini/gemini-cli/issues/24211) | @tusaryan | `2026-04-09` |
| [#7989 Provide an official way to add comments in GEMINI.md](https://github.com/google-gemini/gemini-cli/issues/7989) | @JagjeevanAK | `2026-04-09` |
| [#11438 The ripgrep tool should prefer the system ripgrep, when possible.](https://github.com/google-gemini/gemini-cli/issues/11438) | @M-DEV-1 | `2026-04-10` |
| [#12634 Feature: Extension-Contributed Configuration Settings](https://github.com/google-gemini/gemini-cli/issues/12634) | @singhaditya73 | `2026-04-10` |
| [#12878 Optionalize node-pty with external backend to support static/musl Node](https://github.com/google-gemini/gemini-cli/issues/12878) | @kartikangiras | `2026-04-10` |
| [#16391 Bug: Clickable URLs in inline Markdown include trailing punctuation especially Chinese punctuations, leading to broken navigation](https://github.com/google-gemini/gemini-cli/issues/16391) | @yuvrajangadsingh | `2026-04-10` |
| [#20968 Windows PowerShell Output Encoding Bug](https://github.com/google-gemini/gemini-cli/issues/20968) | @ishaanxgupta | `2026-04-10` |
| [#22671 Numeric Keypad (NumLock) unresponsive in VS Code Integrated Terminal (Linux Fedora KDE Plasma)](https://github.com/google-gemini/gemini-cli/issues/22671) | @Gitanaskhan26 | `2026-04-10` |
| [#22738 [Windows/WezTerm] Shift+Tab and fallback F10 fail to cycle approval mode (Keystroke logs included)](https://github.com/google-gemini/gemini-cli/issues/22738) | @Gitanaskhan26 | `2026-04-10` |
| [#22920 AgentLoopContext is incompatible with Config type](https://github.com/google-gemini/gemini-cli/issues/22920) | @SupunGeethanjana | `2026-04-10` |
| [#23018 ACP: Execute tool call title field contains conversational text.](https://github.com/google-gemini/gemini-cli/issues/23018) | @jasonmatthewsuhari | `2026-04-10` |
| [#24923 run_shell_command: stdout lost on fast commands due to child.on('exit') vs child.on('close') race in shellExecutionService](https://github.com/google-gemini/gemini-cli/issues/24923) | @tusaryan | `2026-04-10` |
| [#24991 Support custom seatbelt profiles in ~/.gemini](https://github.com/google-gemini/gemini-cli/issues/24991) | @flexponsive | `2026-04-10` |
| [#13973 feat: smarter redaction in filename presentation](https://github.com/google-gemini/gemini-cli/issues/13973) | @Champbreed | `2026-04-11` |
| [#16091 Spam loop `Editor is not supported: ${currentPreference}` when the `preferredEditor` is an invalid value](https://github.com/google-gemini/gemini-cli/issues/16091) | @Niralisj | `2026-04-11` |
| [#18727 Already selected allow for this session, but still prompted for each operation](https://github.com/google-gemini/gemini-cli/issues/18727) | @ahsanfarooq210 | `2026-04-11` |
| [#19663 Feature Request: support multiple .env files](https://github.com/google-gemini/gemini-cli/issues/19663) | @umyhabibaa | `2026-04-11` |
| [#19983 Bug Report: CLI Configuration & UX Inconsistency](https://github.com/google-gemini/gemini-cli/issues/19983) | @h30s | `2026-04-11` |
| [#21366 When searchung in /resume and using search /: cannot select filtered result, since "enter" is put in search term and thereforce no mean of selecting desired resume point](https://github.com/google-gemini/gemini-cli/issues/21366) | @f-pieri | `2026-04-11` |
| [#21686 Typing unmapped keys in Vim Normal mode inserts characters into input field](https://github.com/google-gemini/gemini-cli/issues/21686) | @Rajeshpatel07 | `2026-04-11` |
| [#14928 gemini mcp list connects to MCP servers](https://github.com/google-gemini/gemini-cli/issues/14928) | @ayush-devcore | `2026-04-12` |
| [#16550 Command line recall doesn't remember in-flight edits if you accidentally scroll up too far](https://github.com/google-gemini/gemini-cli/issues/16550) | @abhishekblue | `2026-04-12` |
| [#21925 Gemini CLI shows the hand icon indicating that Action is required even when it is not required](https://github.com/google-gemini/gemini-cli/issues/21925) | @sanatan0511 | `2026-04-12` |
| [#22784 Bug Description: The grep_search tool fails with a spawn EFTYPE error on Windows (win32). It appears the underlying ripgrep binary is either incompatible with the current OS/architecture or corrupted.](https://github.com/google-gemini/gemini-cli/issues/22784) | @manas-raj999 | `2026-04-12` |
| [#24729 The newly created file is not detected by the @ function.](https://github.com/google-gemini/gemini-cli/issues/24729) | @prassamin | `2026-04-12` |
</details>

<details>
<summary><b>🛠️ Active Development: Blocked PRs (10)</b> — <i>Active work with blockers.</i></summary>

**Criteria: Active PRs with conflicts or failures updated within 14 days.**

| Issue | Linked PR | Author | Reason | Last Update |
| :--- | :--- | :--- | :--- | :--- |
| [#15691 LLM outputs tables which are broken and truncated](https://github.com/google-gemini/gemini-cli/issues/15691) | [#24113](https://github.com/google-gemini/gemini-cli/pull/24113) | @Debadri-das | Merge Conflict | `2026-04-05` |
| [#12137 Login url is truncated](https://github.com/google-gemini/gemini-cli/issues/12137) | [#24853](https://github.com/google-gemini/gemini-cli/pull/24853) | @Aaxhirrr | Merge Conflict | `2026-04-07` |
| [#20888 AskUser format code without borders](https://github.com/google-gemini/gemini-cli/issues/20888) | [#21254](https://github.com/google-gemini/gemini-cli/pull/21254) | @Hamdanbinhashim | Merge Conflict | `2026-04-08` |
| [#22565 CLI fails to ignore large binary files (.pak, .rpa), causing 192MB+ context bloat and silent timeouts](https://github.com/google-gemini/gemini-cli/issues/22565) | [#22793](https://github.com/google-gemini/gemini-cli/pull/22793) | @elliotllliu | Test Failure | `2026-04-08` |
| [#16559 Most /slash command args counts are not validated](https://github.com/google-gemini/gemini-cli/issues/16559) | [#25069](https://github.com/google-gemini/gemini-cli/pull/25069) | @krishdef7 | Merge Conflict | `2026-04-09` |
| [#22929 False command conflicts when launching from home directory (workspace and user commands resolve to same path)](https://github.com/google-gemini/gemini-cli/issues/22929) | [#23069](https://github.com/google-gemini/gemini-cli/pull/23069) | @Br1an67 | Test Failure | `2026-04-09` |
| [#20606 Clean up unsafe returns suppressions](https://github.com/google-gemini/gemini-cli/issues/20606) | [#20668](https://github.com/google-gemini/gemini-cli/pull/20668) | @M-DEV-1 | Merge Conflict | `2026-04-10` |
| [#20675 [Bug]: Interactive shell does not show properly on Windows 10 when using arrow keys in external subshell prompts (v0.31.0)](https://github.com/google-gemini/gemini-cli/issues/20675) | [#23505](https://github.com/google-gemini/gemini-cli/pull/23505) | @KumarADITHYA123 | Test Failure | `2026-04-10` |
| [#21264 docs(core): Add missing JSDoc comments to core utility functions](https://github.com/google-gemini/gemini-cli/issues/21264) | [#21270](https://github.com/google-gemini/gemini-cli/pull/21270) | @poyrazK | Test Failure | `2026-04-10` |
| [#22844 Fix TypeScript execution in “CLI: Run Current File” debug configuration](https://github.com/google-gemini/gemini-cli/issues/22844) | [#25220](https://github.com/google-gemini/gemini-cli/pull/25220) | @AjayBora002 | Test Failure | `2026-04-12` |
</details>

## 🌱 Community & Backlog

<details>
<summary><b>🌱 Available for Pickup (62)</b> — <i>Open for contributors.</i></summary>

**Criteria: Open issues with no assignee and no active PR.**

| Issue | Days Idle |
| :--- | :--- |
| [#22125 `gemini extensions link` should return exit code 0 if extension is already installed](https://github.com/google-gemini/gemini-cli/issues/22125) | 0 |
| [#22274 Bug: image paste fails in WSL2 when clipboard exposes image/bmp and XDG_SESSION_TYPE is unset](https://github.com/google-gemini/gemini-cli/issues/22274) | 0 |
| [#24547 'U+FFFD' character in file broken by `replace` tool](https://github.com/google-gemini/gemini-cli/issues/24547) | 0 |
| [#24675 Tables in screenReader mode break](https://github.com/google-gemini/gemini-cli/issues/24675) | 1 |
| [#22627 Feature request: Mermaid diagram preview for generated mermaid code](https://github.com/google-gemini/gemini-cli/issues/22627) | 1 |
| [#12824 Optimize github app installation](https://github.com/google-gemini/gemini-cli/issues/12824) | 1 |
| [#17437 Before confirming changes, I used CTRL + S to see the differences in the file; it no longer works.](https://github.com/google-gemini/gemini-cli/issues/17437) | 1 |
| [#2353 Option to choose shell (PowerShell) on Windows](https://github.com/google-gemini/gemini-cli/issues/2353) | 1 |
| [#14623 [Doc/UI Mismatch] "Session Retention" setting is missing from `/settings` UI but present in documentation](https://github.com/google-gemini/gemini-cli/issues/14623) | 2 |
| [#21560 Detected terminal name: iTerm2 3.6.8 │ │ │ │ ℹ Loading extension: nanobanana │ │ ⚠ [STARTUP] Cannot start phase 'load_builtin_commands': phase is already active. Call end() before starting again. (x2) ▄│ │ ⚠ [STARTUP] Phase 'load_builtin_commands' was star](https://github.com/google-gemini/gemini-cli/issues/21560) | 2 |
| [#18612 [VSCode Plugin] Unable to change root directory](https://github.com/google-gemini/gemini-cli/issues/18612) | 2 |
| [#18654 Enhanced Copy Workflow via External Editor Integration](https://github.com/google-gemini/gemini-cli/issues/18654) | 2 |
| [#19387 should trust a folder if the rule matches the realpath flakes on windows](https://github.com/google-gemini/gemini-cli/issues/19387) | 2 |
| [#12083 Container name collisions due to sequential numbering in container name generation](https://github.com/google-gemini/gemini-cli/issues/12083) | 2 |
| [#19985 CLI hangs/freezes when using `@filename:line` or `@filename:range` syntax](https://github.com/google-gemini/gemini-cli/issues/19985) | 2 |
| [#19583 feat(policy): support granular skill activation permissions](https://github.com/google-gemini/gemini-cli/issues/19583) | 2 |
| [#18388 Delete option for MCP](https://github.com/google-gemini/gemini-cli/issues/18388) | 2 |
| [#15430 CLI ignores GOOGLE_GEMINI_BASE_URL and forces Cloud Auth/Endpoints](https://github.com/google-gemini/gemini-cli/issues/15430) | 2 |
| [#17677 Session resume requires at least one human message to work](https://github.com/google-gemini/gemini-cli/issues/17677) | 2 |
| [#16282 [Core] Handle EISDIR error when GEMINI.md is a directory during memory discovery](https://github.com/google-gemini/gemini-cli/issues/16282) | 2 |
| [#12468 Bug Report: run_shell_command output is garbled for Japanese characters on Windows](https://github.com/google-gemini/gemini-cli/issues/12468) | 2 |
| [#16248 All Shell commands fail with "Command terminated by signal: 1"](https://github.com/google-gemini/gemini-cli/issues/16248) | 2 |
| [#19282 Run "/extensions update google-workspace" failed](https://github.com/google-gemini/gemini-cli/issues/19282) | 2 |
| [#14940 Auto-completion keeps requesting gemini-2.5-flash-lite even when using gemini-3.0, causing infinite "usage limit reached" warnings](https://github.com/google-gemini/gemini-cli/issues/14940) | 2 |
| [#15618 Vim mode should align with Bash vim mode, NOT Vim editor](https://github.com/google-gemini/gemini-cli/issues/15618) | 2 |
| [#18165 Termux Bug](https://github.com/google-gemini/gemini-cli/issues/18165) | 2 |
| [#21340 feat: Add configurable shell executable for run_shell_command on Windows](https://github.com/google-gemini/gemini-cli/issues/21340) | 2 |
| [#20730 gemini is not able to view files that exist, and I am not able to tag them (despite not being gitignored/geminiignored)](https://github.com/google-gemini/gemini-cli/issues/20730) | 2 |
| [#20661 [Bug] run_shell_command returns garbled Chinese text for the Agent, while referenced files (@filename) work correctly](https://github.com/google-gemini/gemini-cli/issues/20661) | 2 |
| [#18345 RFC: Standardize "Reload/Refresh" Command Naming Conventions](https://github.com/google-gemini/gemini-cli/issues/18345) | 2 |
| [#16124 /restart command](https://github.com/google-gemini/gemini-cli/issues/16124) | 2 |
| [#18087 [Safety Critical] Input Handling Flaws deny 'Emergency Stop' on Touch Interfaces (Inequitable Keybindings)](https://github.com/google-gemini/gemini-cli/issues/18087) | 2 |
| [#18593 Valid chat JSON missing from `/resume` list; forcing resume with `--resume` loads incorrect Session ID](https://github.com/google-gemini/gemini-cli/issues/18593) | 2 |
| [#20480 Feature: evolve --resume to support resuming sessions from any folder via session ID](https://github.com/google-gemini/gemini-cli/issues/20480) | 3 |
| [#21406 [Ask User] Copy Paste Multi-Line String Error](https://github.com/google-gemini/gemini-cli/issues/21406) | 3 |
| [#21568 deleteSession() does not clean tool output directories (UUID / filename mismatch)](https://github.com/google-gemini/gemini-cli/issues/21568) | 3 |
| [#21328 Add delete as an alias for /extensions uninstall](https://github.com/google-gemini/gemini-cli/issues/21328) | 3 |
| [#21400 Add an update command](https://github.com/google-gemini/gemini-cli/issues/21400) | 3 |
| [#21390 Support priority paygo on gemini-cli via vertex](https://github.com/google-gemini/gemini-cli/issues/21390) | 3 |
| [#18871 [Feat] Add a command to delete current session upon exit](https://github.com/google-gemini/gemini-cli/issues/18871) | 3 |
| [#20227 feat(cli): Add ability to cycle through models and mark favorites](https://github.com/google-gemini/gemini-cli/issues/20227) | 3 |
| [#18884 Error updating google workspace extension](https://github.com/google-gemini/gemini-cli/issues/18884) | 3 |
| [#18914 [Android/Termux] Fix duplicate UI and repeated auth prompts caused by relauncher loop and resize remounting](https://github.com/google-gemini/gemini-cli/issues/18914) | 3 |
| [#19868 "context.fileFiltering.customIgnoreFilePaths" setting breaks file completion when using @](https://github.com/google-gemini/gemini-cli/issues/19868) | 3 |
| [#18487 A2A Server should support multiple workspace directories](https://github.com/google-gemini/gemini-cli/issues/18487) | 3 |
| [#20838 CTRL-z removes unfinished open questions in AskUser tool](https://github.com/google-gemini/gemini-cli/issues/20838) | 3 |
| [#22452 BUG: CI_* env var scrub not applied in dev mode (`npm run start`) — interactive mode hangs](https://github.com/google-gemini/gemini-cli/issues/22452) | 3 |
| [#22079 extensions install fails to find gemini-extension.json from GitHub URL](https://github.com/google-gemini/gemini-cli/issues/22079) | 3 |
| [#22541 Theme Dialog preview theme is not reverted when quitting via double Ctrl+C and Ctrl+D](https://github.com/google-gemini/gemini-cli/issues/22541) | 3 |
| [#21505 docs(sdk): add JSDoc to exported interfaces in packages/sdk/src/types.ts](https://github.com/google-gemini/gemini-cli/issues/21505) | 3 |
| [#22130 [UI] Refactor Hardcoded Layout Constants in ThemeDialog](https://github.com/google-gemini/gemini-cli/issues/22130) | 4 |
| [#22029 Pasting something and throwing me error](https://github.com/google-gemini/gemini-cli/issues/22029) | 4 |
| [#22309 Home Dir Warning - Even when in subfolder of home dir?](https://github.com/google-gemini/gemini-cli/issues/22309) | 4 |
| [#22001 Terminal Instance Resource Retention in ShellExecutionService](https://github.com/google-gemini/gemini-cli/issues/22001) | 4 |
| [#21602 Request: Wrap long prompts in Tool Confirmation Screen instead of truncating](https://github.com/google-gemini/gemini-cli/issues/21602) | 4 |
| [#21477 bug: TUI hangs indefinitely on "Initializing..." — IdeClient.getInstance() blocks BuiltinCommandLoader in bare terminal](https://github.com/google-gemini/gemini-cli/issues/21477) | 4 |
| [#19249 feat: emit token usage metadata via ACP extNotification in zed-integration](https://github.com/google-gemini/gemini-cli/issues/19249) | 4 |
| [#19835 Support for live streaming in custom discovered tools](https://github.com/google-gemini/gemini-cli/issues/19835) | 4 |
| [#16341 Copy text button](https://github.com/google-gemini/gemini-cli/issues/16341) | 4 |
| [#19602 Feature: Manually provide new session UUID via command line arg](https://github.com/google-gemini/gemini-cli/issues/19602) | 4 |
| [#18990 Feature Request: The CLI input prompt does not support Tab-completion for file paths, which makes working with files inconvenient. Please consider adding this standard shell feature to improve usability.](https://github.com/google-gemini/gemini-cli/issues/18990) | 5 |
| [#18385 Support Git Submodules in Extensions](https://github.com/google-gemini/gemini-cli/issues/18385) | 5 |
</details>

<details>
<summary><b>⚠️ Unowned PRs (11)</b> — <i>Ownership mismatch.</i></summary>

**Criteria: PRs where author/assignee does not match the linked issue's assignee.**

| Issue | Linked PR | PR Author | Issue Assignee | Last Update |
| :--- | :--- | :--- | :--- | :--- |
| [#21142 feat(cli): add /stats perf subcommand for memory and startup timing display](https://github.com/google-gemini/gemini-cli/issues/21142) | [#21141](https://github.com/google-gemini/gemini-cli/pull/21141) | @neeraj-par | @ved015 | `2026-03-11` |
| [#18895 CLI cannot use fresh token in MCP OAuth](https://github.com/google-gemini/gemini-cli/issues/18895) | [#23493](https://github.com/google-gemini/gemini-cli/pull/23493) | @nivbrook | @sahilkirad | `2026-03-23` |
| [#21836 [Bug]: ripgrep ENOENT on Termux due to incompatible binary](https://github.com/google-gemini/gemini-cli/issues/21836) | [#21840](https://github.com/google-gemini/gemini-cli/pull/21840) | @imadraude | @student-ankitpandit | `2026-03-23` |
| [#19710 Fix unsafe type assertions in Core Utilities (Phase 1.2: JSON & Config)](https://github.com/google-gemini/gemini-cli/issues/19710) | [#23628](https://github.com/google-gemini/gemini-cli/pull/23628) | @KumarADITHYA123 | @Yuvraj-cyborg | `2026-03-24` |
| [#21230 feat: visualize tool and /visualize command](https://github.com/google-gemini/gemini-cli/issues/21230) | [#24192](https://github.com/google-gemini/gemini-cli/pull/24192) | @student-ankitpandit | @lucumango | `2026-03-30` |
| [#19675 Make the CLI more friendly with tmux](https://github.com/google-gemini/gemini-cli/issues/19675) | [#19705](https://github.com/google-gemini/gemini-cli/pull/19705) | @Nixxx19 | @apfine | `2026-04-05` |
| [#21729 Bug: A2A server GET /tasks/metadata missing return after 501 response — causes ERR_HTTP_HEADERS_SENT crash with GCS task store](https://github.com/google-gemini/gemini-cli/issues/21729) | [#24293](https://github.com/google-gemini/gemini-cli/pull/24293) | @garagon | @yashodipmore | `2026-04-08` |
| [#22193 Gemini CLI doesn't maintain keyboard focus when VS Code extension closes a diff](https://github.com/google-gemini/gemini-cli/issues/22193) | [#23215](https://github.com/google-gemini/gemini-cli/pull/23215) | @iiitutu | @gjuggler | `2026-04-09` |
| [#22934 test(acp): add missing coverage for extensions command error paths](https://github.com/google-gemini/gemini-cli/issues/22934) | [#23060](https://github.com/google-gemini/gemini-cli/pull/23060) | @Br1an67 | @sahilkirad | `2026-04-09` |
| [#16220 chore: ESLint Suppression Audit](https://github.com/google-gemini/gemini-cli/issues/16220) | [#25086](https://github.com/google-gemini/gemini-cli/pull/25086) | @achaljhawar | @ChandanKT-git | `2026-04-10` |
| [#22691 Ability to specify the exact workspace directory without walking up file tree](https://github.com/google-gemini/gemini-cli/issues/22691) | [#22861](https://github.com/google-gemini/gemini-cli/pull/22861) | @sea212 | @ak91456 | `2026-04-10` |
</details>

---
*Dashboard maintained by automated triage script.*
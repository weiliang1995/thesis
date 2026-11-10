# Methodology revision TODO

This list tracks cross-chapter consistency checks and pending review items. It is not part of the thesis manuscript.

## After PR #1 is merged

- [ ] Check `chapters/01-introduction/1.6.2-research-limitations.md`: it currently mentions "story points" as a task-complexity factor, whereas `chapters/04-research-methodology/4.1.2-task-selection-classification-and-developer-assignment.md` uses pre-task estimated engineering effort, task scope, and dependencies. Confirm which were actually used and align the wording. Do not insert "story points" into the methodology unless the data supports it.
- [ ] Recheck Chapter 1 / Methodology terminology and metrics after merging PR #1. In particular, preserve the baseline-versus-Trade-Harness workflow comparison without claiming the baseline lacks native agent capabilities.

## Methodology #8: literature and operationalization (author review needed)

- [ ] Review Wood (1986), "Task complexity: Definition of the construct" (DOI: 10.1016/0749-5978(86)90044-0) for task scope and coordination/dependency dimensions.
- [ ] Review Jørgensen (2004), "A Review of Studies on Expert Estimation of Software Development Effort" (DOI: 10.1016/S0164-1212(02)00156-5) for expert-based pre-task effort estimation.
- [ ] Review OpenAI (2024), "Introducing SWE-bench Verified" (https://openai.com/index/introducing-swe-bench-verified/) for engineer-estimated task resolution time as a difficulty annotation practice; do not present it as a peer-reviewed validation of this study's thresholds.
- [ ] Document that the Simple (≤1 day), Medium (>1–≤4 days), Complex (>4 days) time bands are study-specific operational definitions, not thresholds established by the cited papers. Define treatment of fractional-day estimates and confirm that *estimated effort before starting* is distinct from observed delivery lead time.

## RQ2 / Testing: decisions and deferred checks (2026-11-09)

- [x] Keep RQ2 focused on **software quality outcomes** of the complete workflow comparison. Do not claim that differences in defect density or test pass rate directly establish a causal effect of context/memory management alone. No separate context/memory metric or exploratory defect taxonomy is planned for now.
- [x] Both workflow conditions use the same **team-prescribed testing process and JSON test-case document format**. Each real development task has its **own** task-specific test cases; a task is implemented once, not repeated in both conditions. The agent parses the JSON test cases, generates test code, and runs E2E tests through Playwright MCP. Baseline developers coordinate access/execution using native agent capabilities; Trade-Harness orchestrates this through its workflow rules.
- [x] **Both conditions are instructed to allow at most three E2E test-script correction loops**, and the agent returns its final report when the limit is reached. Baseline receives this rule through developer prompts/project instructions; Trade-Harness enforces it through predefined workflow controls. A loop follows an E2E failure, reviews whether the generated test script is wrong, corrects test code when warranted, and reruns testing; it does **not** edit business code. Confirm from actual execution traces whether baseline followed the cap and how initial runs vs. retries were counted.
- [x] 4.2.2 now defines **Final E2E Test Pass Rate** using passed cases over all task-specific applicable JSON cases (including failed or unexecuted cases in the denominator). The measured result is the final report after permitted test-script correction loops and before development handoff.
- [ ] Verify that existing E2E reports can be reconciled with the full task-specific JSON case list; distinguish unavailable reports from a measured zero-pass result.
- [x] **Include E2E Test-Script Correction Loop Count as a supplementary process metric** alongside RQ2 quality outcomes, without adding a research question or treating loop count as a direct software-quality measure. One counted loop consists of diagnosing a failed E2E run, correcting generated *test script* code, and rerunning; the initial test run and business-code changes are not correction loops.
- [ ] Specify how correction loop count is extracted from available baseline and Trade-Harness records, including cases with zero loops, unresolved failures, and incomplete logs. Both receive a three-loop instruction, but only Trade-Harness enforces the limit programmatically. Report observed over-limit baseline runs transparently as possible instruction-compliance deviations; never infer context-window/memory root cause without supporting evidence. Consider task complexity and final pass rate when interpreting loop counts.
- [ ] Check whether the three-loop instruction and its differing enforcement affect final E2E pass rates; document treatment of incomplete or failed tasks. Check that unresolved product-code failures remain reported rather than being suppressed by altering test assertions. Do not add unmeasured first-pass metrics retroactively.
- [x] Clarified 4.1.3 testing paragraph: each development task has its own JSON test-case document; conditions share testing protocol and tools, not the same task or test-case contents.
- [ ] When chapters are drafted, audit **Problem Statement 1.2.2 → RO2 → RQ2 → Methodology 4.1.3/4.2.2 → Results/Discussion** to distinguish mechanism-level rationale (context, memory, dependencies, validation) from workflow-level observed quality outcomes. Update terminology consistently if E2E replaces integration testing.
- [ ] In 4.3 Threats to Validity, explain that whole-workflow comparison does not isolate individual Trade-Harness layers and task-specific E2E tests can vary in coverage. Do not present speculative agent-caused defects as confirmed.

- [ ] Verify the actual Claude Code instruction mechanism used for the baseline: the native project-instruction file is normally `CLAUDE.md`, rather than assuming an `AGENTS.md` file is automatically loaded. The shared three-loop rule must be supplied through a mechanism demonstrably available during the study (prompt or project instructions). See Claude Code configuration documentation.
- [ ] Verify the final measured test report preserves all required JSON scenarios; generated code may require correction, but expected outcomes must not be rewritten merely to obtain a passing result.
- [ ] If **Baseline E2E execution logs show more than three test-script correction loops**, describe this in Results/Discussion only as an observed failure to comply with the stated iteration constraint (or a deviation from the intended procedure), conditional on verifying the rule was available to the agent and that loop counts are comparable. This may illustrate a practical limitation of instruction-based coordination; do **not** infer context-window overflow, compaction, memory loss, or another root cause without supporting evidence. Also document any protocol deviations and their effect on comparability.
- [ ] For E2E failure handling in 4.2.2, define operational categories where records support them: **test-script error**, **business implementation defect**, **environment/dependency failure**, and **undetermined**. Use observable evidence and avoid forcing ambiguous failures into an agent-caused defect category; if no reliable classification is available, report that limitation rather than inventing classifications.
- [x] 4.2.2 counts only final passing cases in E2E numerator; failed, unexecuted and unresolved cases remain in the JSON-case denominator, and test expectations must not be rewritten to force passes. Missing final reports are distinguished from measured zero-pass outcomes.
- [ ] When analyzing actual E2E reports, document invalid runs and environment-related failures separately wherever reliable failure labels exist; do not infer unsupported root causes.

## Section 4.2 decisions and cross-section checks (2026-11-09)

- [x] **Delivery lead time** runs from Jira *In Progress* to the intermediate *Development Complete* status marking the end of developer-owned work. QA waiting, QA testing, and test-environment deployment after handoff are excluded. Section 4.2.1 updated.
- [x] 4.1.3 was aligned to the *Development Complete* endpoint (in addition to its Changed LOC and changed-KLOC metric wording).
- [ ] Review all remaining chapters for "QA staging" / "test environment deployment" endpoint discrepancies; verify exact Jira status name from exported data and define handling of reopened issues or repeated status transitions in 4.2.5 if present.
- [x] **Feature-development scope confirmed in discussion:** include both new feature implementation and enhancements to existing features; exclude standalone bug fixes and independent refactoring tasks. This is the intended eligibility definition, not a claim that all already-collected tasks satisfy it.
- [ ] **Deferred to actual data analysis:** check whether the feature-development-only sample adequately covers both developers, both workflows, and all three complexity levels; document any exclusions consistently, without selecting tasks based on observed outcomes. When finalizing eligibility wording, align 4.1.2, 4.1.4, data analysis, limitations and task examples; verify the rule was not retrospectively chosen to favor a result.
- [x] Author confirms QA defects are linked to development Jira issues and existing enterprise LLM gateway usage can be associated with tasks. Specify the exact extraction and joining procedure in 4.2.4 rather than treating source availability as an unresolved assumption.

## Section 4.2.2 defect-density operationalization (confirmed in discussion)

- [x] Use task-level **Changed LOC = Added LOC + absolute value of Deleted LOC** from the final attributable GitLab production-code diff (count a modified line as a deletion plus an addition under Git diff conventions). Proposed defect density: confirmed task-linked defects / (Changed LOC / 1000). Define zero-Changed-LOC handling rather than dividing by zero.
- [x] **Retain legitimate high-defect-density outliers**, including very small changes that introduce defects. Do not drop cases solely for extreme ratios. Report raw defect counts and changed LOC alongside density, consider group-level aggregation, and discuss unusually high-density cases where evidence permits.
- [x] 4.2.2 limits defect counts to confirmed Jira-linked feature defects available by the dataset extraction cutoff, without speculative long-term bug attribution rules.
- [ ] Record the actual **defect-data extraction cutoff date** in data-preparation/collection methodology once the dataset is finalized; briefly note unequal post-completion observation periods in 4.3 if relevant. Do not attribute defects personally to the agent without evidence.
- [ ] Validate Jira issue linkage, defect deduplication, exclusion of non-production code from changed-LOC calculations, and handling of bugs whose attribution to the original feature change remains uncertain. Clarify whether the intended outcome is QA-detected defects only or includes later confirmed issues available by data extraction.

## Section 4.2.3 token metrics (2026-11-10)

- [x] **Use Changed LOC = Added LOC + |Deleted LOC|** for both defect density and LOC per million tokens; use the final task-attributable production-code diff in both measures. This reports code-change volume per token, not net code growth or functional productivity.
- [x] **Gateway tokens are only available as task-linked input and output counts**, not by planning, code generation, validation, sub-agent, Trade-Harness stage, or cache activity. Token total for the study is the recorded input plus output tokens; do not invent cache or agent-stage breakdowns. Use available gateway-recorded USD usage charges for per-issue cost and group averages.
- [x] Gateway logging is now described in 4.2.4.4 using only confirmed input tokens, output tokens, and usage cost. The earlier unsupported cache-behaviour and activity-level attribution claims were removed.
- [ ] In 4.2.5, document incomplete gateway links, missing or zero token totals, and issues without cost records transparently; do not silently interpret missing usage as zero. Review possible unmatched usage and the effects of incomplete records on comparisons.

## Section 4.2.4 sources and traceability (2026-11-10)

- [x] An existing AI-development dashboard consolidates Jira task information, GitLab code-change measures, and enterprise gateway input/output token and usage-cost data. These are still the underlying source systems; avoid claiming all records were fetched directly from their APIs.
- [x] Task-specific JSON cases and agent-generated E2E reports are separate from that dashboard. Reports reside in the development repository's `docs/e2e-test` directory and are **named using the branch name** (file extension not confirmed).
- [x] Sections 4.2.4.1–4.2.4.4 now cover Jira, GitLab, E2E records, and gateway respectively. The original gateway subsection was renumbered to 4.2.4.4.
- [ ] Validate how branch names link to Jira issues (including issues with multiple branches), which dashboard fields establish assigned workflow/developer/complexity, and which source records are available for verifying ambiguous task joins.
- [x] The author confirms that saved branch-named E2E reports under `docs/e2e-test` **record correction loop count**. Section 4.2.4.3 has been updated to identify the reports as the source of this supplementary metric.
- [ ] When preparing the actual dataset, verify report counts match the agreed definition (test-script correction-and-rerun cycles, excluding the initial run and business-code fixes), including zero loops and cases that exceed the three-loop instruction.
- [ ] Confirm whether all final E2E report entries can be reconciled against task-specific JSON test-case documents, and the handling of a missing or duplicate branch-named report in 4.2.5.

## Research design decisions confirmed in discussion

- Technical lead allocates real tasks based on business domain, estimated effort and team operating constraints.
- During the 12-week study, each of the two developers is intended to receive tasks under both workflows within each complexity level, as evenly as feasible. This is balancing, not randomization.
- Planned additions: Section 4.1.4 Experimental Procedure and Section 4.3 Threats to Validity.
- Do not edit manuscript sections until the author reviews and approves the proposed wording.

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
- [ ] In 4.2.2, assess whether to rename **Integration Testing Pass Rate** to **E2E Test Pass Rate** based on the actual reports. Proposed primary measurement is the final pass rate after permitted agent corrections and before QA handoff. Define denominator against the task's required JSON test cases (including unexecuted cases) rather than only generated/passed tests; verify available reporting supports this.
- [ ] Check availability and comparability of **test-script correction loop count** for Baseline and Trade-Harness. Both share a three-loop instruction, but only Trade-Harness has a programmatically enforced gate; assess prompt compliance and logs. Count only test-script diagnosis/correction/re-execution, not business-code fixes. Loop count is a possible descriptive process indicator, not automatically a new RQ2 quality metric.
- [ ] Check whether the three-loop instruction and its differing enforcement affect final E2E pass rates; document treatment of incomplete or failed tasks. Check that unresolved product-code failures remain reported rather than being suppressed by altering test assertions. Do not add unmeasured first-pass metrics retroactively.
- [x] Clarified 4.1.3 testing paragraph: each development task has its own JSON test-case document; conditions share testing protocol and tools, not the same task or test-case contents.
- [ ] When chapters are drafted, audit **Problem Statement 1.2.2 → RO2 → RQ2 → Methodology 4.1.3/4.2.2 → Results/Discussion** to distinguish mechanism-level rationale (context, memory, dependencies, validation) from workflow-level observed quality outcomes. Update terminology consistently if E2E replaces integration testing.
- [ ] In 4.3 Threats to Validity, explain that whole-workflow comparison does not isolate individual Trade-Harness layers and task-specific E2E tests can vary in coverage. Do not present speculative agent-caused defects as confirmed.

- [ ] Verify the actual Claude Code instruction mechanism used for the baseline: the native project-instruction file is normally `CLAUDE.md`, rather than assuming an `AGENTS.md` file is automatically loaded. The shared three-loop rule must be supplied through a mechanism demonstrably available during the study (prompt or project instructions). See Claude Code configuration documentation.
- [ ] Verify the final measured test report preserves all required JSON scenarios; generated code may require correction, but expected outcomes must not be rewritten merely to obtain a passing result.
- [ ] If **Baseline E2E execution logs show more than three test-script correction loops**, describe this in Results/Discussion only as an observed failure to comply with the stated iteration constraint (or a deviation from the intended procedure), conditional on verifying the rule was available to the agent and that loop counts are comparable. This may illustrate a practical limitation of instruction-based coordination; do **not** infer context-window overflow, compaction, memory loss, or another root cause without supporting evidence. Also document any protocol deviations and their effect on comparability.
- [ ] For E2E failure handling in 4.2.2, define operational categories where records support them: **test-script error**, **business implementation defect**, **environment/dependency failure**, and **undetermined**. Use observable evidence and avoid forcing ambiguous failures into an agent-caused defect category; if no reliable classification is available, report that limitation rather than inventing classifications.
- [ ] Clarify which E2E outcomes count toward Final E2E Pass Rate, and how unresolved failures, test scripts that could not execute, and missing cases are represented. Failed business behavior must not be converted to a pass by changing the required JSON expectations. Keep outcome measurement separate from whether an agent correctly diagnosed the failure.

## Section 4.2 decisions and cross-section checks (2026-11-09)

- [x] **Delivery lead time** runs from Jira *In Progress* to the intermediate *Development Complete* status marking the end of developer-owned work. QA waiting, QA testing, and test-environment deployment after handoff are excluded. Section 4.2.1 updated.
- [ ] Align 4.1.3 and any other references currently saying "QA staging" or "test environment deployment" with the *Development Complete* endpoint; use the exact Jira status label when exporting data. Define handling of reopened issues or repeated status transitions in 4.2.5 if present.
- [x] **Feature-development scope confirmed in discussion:** include both new feature implementation and enhancements to existing features; exclude standalone bug fixes and independent refactoring tasks. This is the intended eligibility definition, not a claim that all already-collected tasks satisfy it.
- [ ] **Deferred to actual data analysis:** check whether the feature-development-only sample adequately covers both developers, both workflows, and all three complexity levels; document any exclusions consistently, without selecting tasks based on observed outcomes. When finalizing eligibility wording, align 4.1.2, 4.1.4, data analysis, limitations and task examples; verify the rule was not retrospectively chosen to favor a result.
- [x] Author confirms QA defects are linked to development Jira issues and existing enterprise LLM gateway usage can be associated with tasks. Specify the exact extraction and joining procedure in 4.2.4 rather than treating source availability as an unresolved assumption.

## Research design decisions confirmed in discussion

- Technical lead allocates real tasks based on business domain, estimated effort and team operating constraints.
- During the 12-week study, each of the two developers is intended to receive tasks under both workflows within each complexity level, as evenly as feasible. This is balancing, not randomization.
- Planned additions: Section 4.1.4 Experimental Procedure and Section 4.3 Threats to Validity.
- Do not edit manuscript sections until the author reviews and approves the proposed wording.

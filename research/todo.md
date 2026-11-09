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
- [x] **Three-loop limit applies to Trade-Harness only**; Baseline has no enforced three-loop cap and developers control iteration using native Claude Code. This is an intervention characteristic, not a controlled condition. Still to confirm the definition of one loop (test run vs. fix-and-retest cycle) and what happens when Trade-Harness reaches the cap.
- [ ] In 4.2.2, assess whether to rename **Integration Testing Pass Rate** to **E2E Test Pass Rate** based on the actual reports. Proposed primary measurement is the final pass rate after permitted agent corrections and before QA handoff. Define denominator against the task's required JSON test cases (including unexecuted cases) rather than only generated/passed tests; verify available reporting supports this.
- [ ] Check availability and comparability of **correction loop count** for Baseline and Trade-Harness. Trade-Harness has a maximum of three correction loops, while Baseline is developer-directed and not subject to this cap. Therefore, counts are censored/limited by design in Trade-Harness and cannot be treated as directly comparable without clear measurement and interpretation; prefer descriptive reporting unless justified. This is not automatically a new RQ2 software-quality metric.
- [ ] Check whether a three-loop limit creates a ceiling on final E2E pass rates and whether incomplete or failed tasks are retained in analysis. Do not add unmeasured first-pass metrics retroactively.
- [ ] Correct the illustrative testing paragraph in 4.1.3 if it implies identical test-case *contents* across different tasks. Use common procedure/format rather than same test cases.
- [ ] When chapters are drafted, audit **Problem Statement 1.2.2 → RO2 → RQ2 → Methodology 4.1.3/4.2.2 → Results/Discussion** to distinguish mechanism-level rationale (context, memory, dependencies, validation) from workflow-level observed quality outcomes. Update terminology consistently if E2E replaces integration testing.
- [ ] In 4.3 Threats to Validity, explain that whole-workflow comparison does not isolate individual Trade-Harness layers and task-specific E2E tests can vary in coverage. Do not present speculative agent-caused defects as confirmed.

## Research design decisions confirmed in discussion

- Technical lead allocates real tasks based on business domain, estimated effort and team operating constraints.
- During the 12-week study, each of the two developers is intended to receive tasks under both workflows within each complexity level, as evenly as feasible. This is balancing, not randomization.
- Planned additions: Section 4.1.4 Experimental Procedure and Section 4.3 Threats to Validity.
- Do not edit manuscript sections until the author reviews and approves the proposed wording.

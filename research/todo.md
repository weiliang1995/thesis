# Methodology revision TODO

This list tracks cross-chapter consistency checks and pending review items. It is not part of the thesis manuscript.

## After PR #1 is merged

- [ ] Check `chapters/01-introduction/1.6.2-research-limitations.md`: it currently mentions "story points" as a task-complexity factor, whereas `chapters/04-research-methodology/4.1.2-task-selection-classification-and-developer-assignment.md` uses pre-task estimated engineering effort, task scope, and dependencies. Confirm which were actually used and align the wording. Do not insert "story points" into the methodology unless the data supports it.
- [ ] Recheck Chapter 1 / Methodology terminology and metrics after merging PR #1. In particular, preserve the baseline-versus-Trade-Harness workflow comparison without claiming the baseline lacks native agent capabilities.

## Methodology #8: literature and operationalization (author review needed)

- [ ] Review Wood (1986), "Task complexity: Definition of the construct" (DOI: 10.1016/0749-5978(86)90044-0) for task scope and coordination/dependency dimensions.
- [ ] Review Jørgensen (2004), "A Review of Studies on Expert Estimation of Software Development Effort" (DOI: 10.1016/S0164-1212(02)00156-5) for expert-based pre-task effort estimation.
- [ ] Review OpenAI (2024), "Introducing SWE-bench Verified" (https://openai.com/index/introducing-swe-bench-verified/) for engineer-estimated task resolution time as a difficulty annotation practice; do not present it as a peer-reviewed validation of this study's thresholds.
- [ ] Document that the Simple (≤1 day), Medium (2–4 days), Complex (>4 days) time bands are study-specific operational definitions, not thresholds established by the cited papers. Define treatment of fractional-day estimates and confirm that *estimated effort before starting* is distinct from observed delivery lead time.

## Research design decisions confirmed in discussion

- Technical lead allocates real tasks based on business domain, estimated effort and team operating constraints.
- During the 12-week study, each of the two developers is intended to receive tasks under both workflows within each complexity level, as evenly as feasible. This is balancing, not randomization.
- Planned additions: Section 4.1.4 Experimental Procedure and Section 4.3 Threats to Validity.
- Do not edit manuscript sections until the author reviews and approves the proposed wording.

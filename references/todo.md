# Literature and product-documentation reading TODO

These are **candidate sources and evidence checks**, not approved additions to the thesis bibliography. Read and decide whether to cite before editing `references/references.md` or adding new citations to the thesis. Existing bibliography entries are explicitly identified. Every entry includes its proposed use and boundaries.

## A. Developer-managed prompting and supervision (Chapter 1.2.1; Chapter 2.1)

### A1. Nam et al. (2025) — NEW candidate

- **Reference:** Nam et al. (2025). *Prompting LLMs for Code Editing: Struggles and Remedies*. https://arxiv.org/abs/2504.20196
- **Suggested use:** 1.2.1 (Workflow Coordination and Delivery Efficiency), 2.1 (Autonomy/Orchestration and Human-in-the-Loop).
- **Possible evidence:** Repeated prompting and missing information in developer prompts during AI-assisted code editing.
- **Limitation:** The observed IDE code-transform workflow is not equivalent to the study's Claude Code CLI baseline; it cannot demonstrate that Trade-Harness improves delivery time.
- [ ] Read original study and decide whether to cite.

### A2. Vaithilingam et al. (2022) — ALREADY in main bibliography

- **Reference:** Vaithilingam, P., Zhang, T., & Glassman, E. L. (2022). *Expectation vs. Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models*. https://doi.org/10.1145/3491101.3519665
- **Suggested use:** 1.2.1, 2.1.
- **Possible evidence:** Understanding, evaluating, modifying, and debugging AI-generated code still require developer work.
- **Limitation:** An early code-generation usability study, not a comparison of agentic CLI workflows.
- [ ] Read original study and decide whether to cite in these sections.

### A3. Existing sources requiring claim checks

- [ ] **Otten et al. (2025)** — already in `references/references.md`. Confirm exact observations about multi-turn prompting and developer practices before relying on them in 1.1.1 / 1.2.1 / 2.1. https://arxiv.org/abs/2510.06000
- [ ] **Song et al. (2024)** — already in `references/references.md`. Check which version supports any coordination/integration-time percentage; do not mix percentages from different versions or measures. Suggested: 1.2.1 / 2.1. https://arxiv.org/abs/2410.02091

## B. Complex engineering tasks and project-specific constraints (Chapter 1.1.3; Chapter 2; Chapter 3)

### B1. Tang et al. (2026) — NEW candidate; HIGH PRIORITY

- **Reference:** Tang, N., Chen, C., Xu, G., Shi, Y., Huang, Y., McMillan, C., Dong, T., & Li, T. J.-J. (2026). *How Coding Agents Fail Their Users: A Large-Scale Analysis of Developer-Agent Misalignment in 20,574 Real-World Sessions*. EMNLP 2026. https://aclanthology.org/2026.emnlp-main.1011/ (DOI: 10.18653/2026.emnlp-main.1011)
- **Suggested use:** **1.1.3(B)** (project-specific workflow constraints and developer-agent misalignment); 1.2.1 (supervision); 2.1 (human-in-the-loop); optionally 3 (limitations of existing systems).
- **Possible evidence:** Observational study of developer pushback across 20,574 agent sessions, including project understanding, user intent, rule following, action boundaries, and explicit developer corrections.
- **Limitation:** Misalignment episodes are operationalized through *visible developer pushback*. This does not show that every native agent fails, that project-specific configuration is unavailable, or that Trade-Harness eliminates these problems. Check sampling, definitions, and denominator before quoting rates.
- [ ] Read methods, findings, and limitations; decide which specific claims are justified.

### B2. Deng et al. (2026) — NEW candidate; HIGH PRIORITY

- **Reference:** Deng, X., et al. (2026). *SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?* ICML 2026, PMLR 306, 23917–23934. https://proceedings.mlr.press/v306/deng26f.html
- **Suggested use:** **1.1.3(A)** (complex multi-file tasks and repository dependencies); 2.2 (context), 3 (benchmark comparison).
- **Possible evidence:** Controlled benchmark covering 1,865 complex software engineering problems; performance gaps on multi-file engineering and cross-file/integration reasoning compared with simpler problem types.
- **Limitation:** Benchmark observations do not establish a monotonic relationship between repository size and failure, nor directly measure the study's enterprise front-end delivery metrics.
- [ ] Check task categories, evaluation settings, and limits of generalization.

### B3. Galster et al. (2026) — NEW candidate; HIGH PRIORITY

- **Reference:** Galster, M., Mohsenimofidi, S., Lulla, J. L., Abubakar, M. A., Treude, C., & Baltes, S. (2026). *Configuring Agentic AI Coding Tools: An Exploratory Study*. AIware 2026, pp. 11–20. https://doi.org/10.1145/3805760.3814887
- **Suggested use:** **1.1.3(B)** (existing native configuration mechanisms and observed adoption), **1.5.2** (accurate baseline and intervention distinction); possibly Chapter 2.
- **Possible evidence:** Claude Code and other agents already support repository-level context, skills, subagents, rules, settings, hooks, and integrations. A survey of repository configurations finds that more advanced mechanisms are less widely used than simple context files.
- **Limitation:** Adoption is not effectiveness; do not claim Claude Code lacks these features. **Use the final published paper** when reporting sample numbers (published abstract reports 2,853 repositories; some preprints report 2,926). Do not mix editions.
- [ ] Read published version, verify categories and any version-sensitive statistics.

## C. Non-determinism, context and orchestration cost (Chapter 1.1.3–1.1.4; Chapter 2)

### C1. Atıl et al. (2025) — NEW candidate

- **Reference:** Atıl, B., et al. (2025). *Non-Determinism of “Deterministic” LLM System Settings in Hosted Environments*. Eval4NLP 2025, pp. 135–148. https://aclanthology.org/2025.eval4nlp-1.12/
- **Suggested use:** **1.1.3(C)** (nondeterministic model outputs); **1.1.4** (distinguish deterministic orchestration from model determinism).
- **Possible evidence:** Repeated calls to hosted LLM APIs can vary even under settings expected to be deterministic.
- **Limitation:** This does not show that all Claude Sonnet 4.6 invocations behave identically or non-identically under the study settings; avoid inferring deterministic outcomes from workflow controls.
- [ ] Read experiment design and decide wording.

### C2. Gloaguen et al. (2026) — NEW candidate; HIGH PRIORITY for cost caveat

- **Reference:** Gloaguen, T., Mündler, N., Müller, M., Raychev, V., & Vechev, M. (2026). *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?* https://arxiv.org/abs/2602.11988
- **Suggested use:** **1.1.3(B)** (project configuration / context), **1.1.4** (orchestration and context can add overhead); 1.2.3 (computational cost); Chapter 2 (context and memory).
- **Possible evidence:** Repository context files can lead to broader exploration/testing and increase inference cost; providing more instructions or context does not automatically produce better results.
- **Limitation:** Evaluates context files, **not** Trade-Harness, multi-agent orchestration, or simple-task cost specifically. Treat expected simple-task token overhead as a hypothesis to examine, not a pre-established thesis finding.
- [ ] Check the distinctions between generated and developer-written files and the particular benchmark conditions before quoting numerical costs.

### C3. Existing orchestration studies worth revisiting

- [ ] **Xia et al. (2024), Agentless** — already in bibliography. 1.1.4 / Chapter 3. A structured localization → repair → validation process is a comparable design direction, not evidence that Trade-Harness is better. https://arxiv.org/abs/2407.01489
- [ ] **Fan et al. (2025), SWE-Effi** — already in bibliography. 1.2.3 / Chapter 2 / Chapter 3. Compare agent outcomes jointly with computational resources and cost. https://arxiv.org/abs/2509.09853

### C4. Execution Control Harness (IISA 2026) — NEW candidate; RELATED-WORK PRIORITY

- **Reference to verify:** *Execution Control Harness for Governed LLM-Based Code Generation*. IISA 2026. DOI: 10.1109/IISA71656.2026.11705535. https://doi.org/10.1109/IISA71656.2026.11705535
- **Suggested use:** **Chapter 3 Related Work**; possibly 1.1.4 as a precedent for explicit workflow control.
- **Possible evidence:** YAML-based governed execution, deterministic validation gates, Git rollback, and hybrid human-agent control evaluated on a reported insurance-system case study.
- **Limitation:** Small case-study evidence; differences in environment, baseline, and measurements must be checked. Its existence means the thesis must **not** claim that deterministic validation gates or execution-control harnesses are novel inventions of Trade-Harness.
- [ ] Verify authors and full publication metadata from the IEEE record.
- [ ] Review design and methods; explain how Trade-Harness and this work differ.

## D. Official product documentation for the baseline (Chapter 1.5.2; Chapter 4.1.3)

Official documentation establishes **what Claude Code / Sonnet 4.6 can support**, not which features were enabled during the study. Confirm CLI version, model ID, settings, installed skills/hooks, context files and actual usage from project evidence before writing the definitive baseline table. Features introduced *after* the study period must not be retroactively assigned to the experimental configuration.

- [ ] **Claude Code: Project instructions / memory** — https://code.claude.com/docs/en/memory. `CLAUDE.md`, repo-level instructions, and memory across sessions. **Do not claim native agents have no memory.**
- [ ] **Claude Code: Skills** — https://code.claude.com/docs/en/skills. Reusable project or user instructions and callable skills.
- [ ] **Claude Code: Subagents** — https://code.claude.com/docs/en/sub-agents. Delegated agents and scoped tools. **Do not claim native tools cannot decompose/delegate tasks.**
- [ ] **Claude Code: Hooks** — https://code.claude.com/docs/en/hooks. Event-triggered command or agent hooks, including enforcement at tool boundaries. **Do not claim native tools cannot enforce rules or trigger checks.**
- [ ] **Claude Code: Permissions** — https://code.claude.com/docs/en/permissions. Fine-grained tool and resource restrictions.
- [ ] **Claude Sonnet 4.6: Model specification** — https://platform.claude.com/docs/en/models/sonnet-4-6/overview. Verify exact identifier `claude-sonnet-4-6`, release/version and model characteristics for the study period. **Do not confuse model abilities with Claude Code CLI's orchestration features.**

**Operational baseline to validate against Chapter 4.1.3:** Both conditions are reported to use Claude Code CLI and Claude Sonnet 4.6. The baseline uses developer-managed prompting and project-level guidance; the intervention adds Trade-Harness's predefined coordination, context/state organization, and validation process. Both are agent-capable. Only claim a difference that is actually part of the configured study.

## E. Source-to-claim and writing checklist

- [ ] **1.1.1 / 1.1.2:** Present native AI coding agents as capable of multi-stage SDLC/FE work. Do not frame them as code-completion-only.
- [ ] **1.1.3:** Discuss possible gaps under complex, multi-file, project-specific constraints and model output variability. Prefer *may*, *not necessarily*, and cited empirical findings over universal claims.
- [ ] **1.1.4:** Define Trade-Harness as **explicit/deterministic orchestration of stage order, scope, tool/context access and validation gates**, while LLM reasoning and generated content remain non-deterministic. Keep six functional layers, not six sequential SDLC stages.
- [ ] **1.1.4 / 1.2.3:** Mention the possible overhead of added validation/agent calls as a countervailing expectation, not a confirmed result. Simple-task token-cost differences remain for later data analysis.
- [ ] **1.5.2 / 4.1.3:** Confirm the precise baseline using official docs and recorded configurations; do not equate Claude Code CLI with plain chat prompting or assume baseline capabilities are absent.
- [ ] **1.6.1:** Preserve the two-developer wording pending supervisor decision; ensure the delimitation says **workflow comparison**, not LLM/model comparison, and excludes architecture *redesign* rather than repository architectural constraints.
- [ ] **Research gap:** Narrow to workflow-level outcomes in real enterprise multi-repository front-end work. Do not assert that all industrial agent evaluations or controlled workflow mechanisms are absent.

**Updated:** 2026-11-09. No candidate was automatically added to the approved bibliography.


## F. Chapter 1 citation audit — 2026-11-16

This section maps the **current** Chapter 1.1–1.2 numbering and exact claims to sources requiring **author review**. Existing citations were added directly to chapter files only when the bibliography already contained a relevant source. The items below are not automatically approved bibliography additions.

### F1. Existing references: check evidence strength before final approval

- [ ] **1.1 Research Background, paragraph 2 — SDLC breadth and human coordination.** The statement that code implementation is only one part of SDLC is common background, but the stronger claim that developers must plan, manage context and validate LLM output may need a direct empirical source. **Existing options:** Vaithilingam et al. (2022), https://doi.org/10.1145/3491101.3519665; Otten et al. (2025), https://arxiv.org/abs/2510.06000. Check whether these specifically support the generalization; do not assert that all agents require manual orchestration.
- [ ] **1.1.1, paragraph 2 — front-end PRD/design-to-implementation activity.** **Existing option:** Si et al. (2025), *Design2Code: Benchmarking Multimodal Code Generation for Automated Front-End Engineering* (already in bibliography), for the narrower UI-design-to-code point. It does **not** establish that coding agents autonomously process entire PRDs and full SDLC workflows.
- [ ] **1.1.2, paragraph 3 — nondeterminism leading to omitted workflow/validation steps.** The bibliography includes a general hallucination survey (Huang et al., 2025), but a model-output variability study does **not** directly establish that validation steps are omitted. Reword as a plausible risk unless a coding-agent execution trace study substantiates this link.
- [ ] **1.1.3, paragraph 3 and Table 1.1 — six orchestration mechanisms.** This is an **author-defined conceptual grouping**, not a recognized six-layer architecture. Acharya et al. (2025), Xia et al. (2024), and Packer et al. (2023) may illustrate individual mechanisms. Do not claim a source endorses exactly this taxonomy.
- [ ] **1.2 opening — 'limited direct evidence' research-gap claim.** Review related work (Xia et al., 2024; Fan et al., 2025; Yang et al., 2024, all in bibliography) and the newer work below before asserting the absence of matched industrial front-end workflow comparisons. Phrase as a narrow gap, not proof that no prior study exists.
- [ ] **1.2.1, paragraph 1 — coding productivity vs end-to-end delivery lead time.** Peng et al. (2023) and Corso et al. (2024) have been cited as studies of localized coding tasks, **not** as evidence that AI coding causes faster or slower QA handoff.
- [ ] **1.2.2, paragraph 2 — overlooked dependency leading to validation misses.** The paragraph is a reasonable possible failure pathway, but Eghbali & Pradel (2024) addresses hallucinated code references, not the measured probability of agents missing E2E failures. Consider stating this as a scenario, or finding an empirical validation-coverage study.
- [ ] **1.2.2, paragraph 3 — context and memory mechanisms.** Packer et al. (2023) and Liu et al. (2025) support the existence and importance of explicit context/memory handling, **not** a demonstrated software-quality advantage for Trade-Harness.
- [ ] **1.2.3, paragraph 1 — provider token pricing/cached input.** This is a provider-product factual claim, not an empirical paper claim. Add the relevant **official model pricing documentation** only if pricing details remain in Chapter 1. Note that this study records input/output tokens but does **not** separately record cache reads or per-stage cost. Suggested Anthropic pricing documentation: https://docs.anthropic.com/en/docs/about-claude/pricing (verify current redirect and historical pricing before citing).
- [ ] **1.2.3, paragraph 3 — structured workflow saves tokens vs adds overhead.** Present both as hypotheses to test, not established comparative effects. Fan et al. (2025) (existing) motivates resource-aware evaluation but does not show Trade-Harness's effect.

### F2. New-paper candidates already listed above — exact new Chapter 1 locations

1. **Atıl et al. (2025), _Non-Determinism of “Deterministic” LLM System Settings in Hosted Environments_.** https://aclanthology.org/2025.eval4nlp-1.12/ — **1.1.2 paragraph 3**, after the factual statement about probabilistic/variable outputs. Supports model-output variability, not specific failures to execute validation. **Already listed in C1; do not add to references.md before approval.**
2. **Nam et al. (2025), _Prompting LLMs for Code Editing: Struggles and Remedies_.** https://arxiv.org/abs/2504.20196 — **1.2.1 paragraph 2**, next to Otten et al. to support prompting friction. This is IDE code editing, not an agentic Claude Code CLI experiment. **Already listed in A1.**
3. **Tang et al. (2026), _How Coding Agents Fail Their Users: A Large-Scale Analysis of Developer-Agent Misalignment in 20,574 Real-World Sessions_.** https://aclanthology.org/2026.emnlp-main.1011/ — **1.1.2 paragraph 3** (developer-agent rule compliance) and/or **1.2.2 paragraph 2** (possible missed project constraints). Verify specific categories of reported failures; do not equate misalignment with measured defect density or E2E pass rate. **Already listed in B1.**
4. **Deng et al. (2026), _SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?_** https://proceedings.mlr.press/v306/deng26f.html — **1.1.2 paragraph 1** and optionally **1.2 Research Gap** for long-horizon/multi-file complexity; it is not a front-end-specific delivery lead-time study. **Already listed in B2.**
5. **Gloaguen et al. (2026), _Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?_** https://arxiv.org/abs/2602.11988 — **1.2.2 paragraph 3** (more context does not guarantee correctness), **1.2.3 paragraph 3** (instruction/context overhead). Evaluate distinctions between repo instructions and full orchestration. **Already listed in C2.**

### F3. Editing boundary

- No new study above is yet cited in Chapter 1, nor added to the approved bibliography.
- Do not insert a citation solely because it shares vocabulary with a sentence: check the original study's methods, measured outcome, and claim scope.
- Chapter 1.1–1.2 existing-reference insertions were limited to 1.1.1, 1.1.2, 1.1.3, 1.2.1 and 1.2.2. 1.1 Research Background and 1.2.3 already contained literature citations.

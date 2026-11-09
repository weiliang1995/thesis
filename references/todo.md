# Literature review TODO

Pending literature reading and author decisions for assessor feedback #1 (Problem Statement) and #2 (research alignment). This file is a **reading list**, not part of the confirmed thesis bibliography. Do not add citations to chapters until the author reads and approves the source.

## 1. Nam et al. (2025) — new candidate

**Reference:** Nam, D., Omran, A., Murillo, A., Thakur, S., Araujo, A., Blistein, M., Frömmgen, A., Hellendoorn, V., & Chandra, S. (2025). *Prompting LLMs for Code Editing: Struggles and Remedies*. arXiv:2504.20196. https://arxiv.org/abs/2504.20196

- **Current status:** [ ] Read by author; [ ] Decide whether to cite; [ ] If accepted, add to `references/references.md`.
- **Suggested sections:** `chapters/01-introduction/1.2.1-lack-of-workflow-orchestration-in-ai-assisted-development.md`; `chapters/02-literature-review/2.1-autonomy-orchestration-and-human-in-the-loop-control-in-ai-assisted-develo.md`.
- **Potential supporting argument:** Developers may need repeated prompting and additional context to obtain satisfactory AI-assisted code edits. The study observes that frequent re-prompting can signal difficulties and analyzes information missing from unsatisfactory prompts.
- **Reading focus:** Study population and tool (Google IDE code-transform feature), observed prompt deficiencies, how re-prompting is measured, and limitations when extrapolating to an agentic CLI.
- **Caution:** Does **not** directly prove that full developer-managed, prompt-based workflows are slower or less reliable than Trade-Harness.

## 2. Vaithilingam et al. (2022) — already listed in bibliography; consider citing

**Reference:** Vaithilingam, P., Zhang, T., & Glassman, E. L. (2022). *Expectation vs. Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models*. CHI Extended Abstracts. https://doi.org/10.1145/3491101.3519665

- **Current status:** Already present in `references/references.md`. [ ] Read by author; [ ] Decide whether/where to cite in prose.
- **Suggested sections:** `chapters/01-introduction/1.2.1-lack-of-workflow-orchestration-in-ai-assisted-development.md`; `chapters/02-literature-review/2.1-autonomy-orchestration-and-human-in-the-loop-control-in-ai-assisted-develo.md`.
- **Potential supporting argument:** Interaction with generated code can involve understanding, assessing, modifying, and debugging the output rather than simply accepting code suggestions.
- **Reading focus:** Tool and participant characteristics, specific usability findings, and generalizability to professional developers using Claude Code CLI.
- **Caution:** Early code-generation tool usability results are not a controlled comparison of structured orchestration versus a prompt-based CLI workflow.

## Additional source-check reminder

- [ ] Verify **Otten et al. (2025)** and **Song et al. (2024)**, which are already in `references/references.md`, against the specific thesis claims in Chapter 2.1; review the cited Song version before repeating any coordination/integration-time percentage.
- [ ] Keep the **research gap** narrow: an evidence gap for comparable workflow-level evaluation in real enterprise front-end development, not a claim that there are no industrial AI-assisted-development studies.

**Last updated:** 2026-11-09. No chapter text has been changed.

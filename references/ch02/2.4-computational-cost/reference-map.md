# Section 2.4 reference map

Scope: token consumption and computational efficiency. Follow 2.2–2.3: identify the problem first, evaluate approaches and their empirical trade-offs, then derive a narrow research gap. No directional prediction or post hoc selection based on Chapter 4.

| Claim / question | Primary evidence | Evidence boundary |
| --- | --- | --- |
| 2.4.1: cumulative input and repeated calls | [Fan et al. (2025), SWE-Effi, §§4–5](https://arxiv.org/html/2509.09853v1); [Bai et al. (2026)](problem/bai-et-al-2026-agent-token-consumption.md) | Figure is a mathematical illustration under full retention, not measured usage. |
| 2.4.1: additional instructions may change usage | [Lulla et al.](../2.1-agent-engineering/context-engineering/lulla-et-al-2026-agents-md-efficiency.md); [Gloaguen et al.](../2.1-agent-engineering/context-engineering/gloaguen-et-al-2026-evaluating-agents-md.md) | Output tokens, total tokens, charges and correctness differ. |
| 2.4.1: repeated execution and costly failures | [SWE-Effi, §5.4, Table 3](https://arxiv.org/html/2509.09853v1); [Gao and Peng](empirical-evidence/gao-peng-2026-turn-control.md) | Failed attempts are not necessarily avoidable; completed enterprise tasks differ from benchmark attempts. |
| 2.4.2: context masking vs summarisation | [Lindenbauer et al., Table 1](existing-approaches/lindenbauer-et-al-2025-complexity-trap.md) | Use 53.4% raw rate in Table 1, not abstract's 53.8%. Raw baseline differs from native Claude Code. |
| 2.4.2: state reuse and rediscovery | [KC and Budathoki](../2.3-software-quality/empirical-evidence/kc-budathoki-2026-handoff-debt.md) | Takeover-only costs, mixed success. Do not assume full lifecycle savings. |
| 2.4.2: architectural simplicity | [Xia et al. (2024), Agentless v2](https://arxiv.org/html/2407.01489v2) | 96/300, $0.70; structured pipeline itself is orchestration; no direct comparison by thesis complexity categories. |
| 2.4.2: planning and component choice | [R.-Z. Fan et al. (2026), §3.2 Table 3](https://arxiv.org/html/2609.20804v1) | 176 settings, matched ablations; planning on/off effects differ by model. No direct Claude Code workflow comparison. |
| 2.4.2: task-adaptive budget | [Gao and Peng (2026)](empirical-evidence/gao-peng-2026-turn-control.md) | Turn control is not adaptive architecture routing or a human effort classification. |
| 2.4.2: difficulty vs expenditure | [Bai et al. (2026)](problem/bai-et-al-2026-agent-token-consumption.md) | Weak association, not a causal budget effect. |
| 2.4.2: resource–performance trade-offs | [SWE-Effi, Tables 1–2](https://arxiv.org/html/2509.09853v1); [Yang et al.](empirical-evidence/yang-et-al-2026-context-has-a-price.md) | Token-budget scores, CPU time and model expenditure capture different resources. Cache prices conditional. |
| 2.4.3: research gap and metrics | Synthesis of mapped evidence; Chapter 1 RQ3 and Chapter 3 gateway/metric definitions | Gap bounded to reviewed studies. No stage-level attribution or claim that changed LOC measures functional value. |

## Reading and archive status

Agentless v2, SWE-Effi v1 (methods, Tables 1–3 and §5), Fan et al. 2026 v1 (methods and Tables 3–4), Lindenbauer v1 (methods and Table 1), Gao and Peng (abstract and study design), Bai (abstract and author project page), Yang (abstract and introduction), and KC/Budathoki (official abstract) were checked in the primary sources. Lulla and Gloaguen are cross-referenced from the existing 2.1.3 review; their original source records should be reviewed in full before final submission. Four newly added source records are stored in this directory; existing bibliography entries and prior records are cross-referenced rather than duplicated. Full-text PDFs have not been archived. Additional direct evidence on task-adaptive *architecture* (rather than turn budget) and validation-specific cost is a useful next review target; the present draft does not claim those relationships are established.

## Editorial checks

- Figure and table numbers remain provisional until chapter assembly.
- RQ3 and the formal computational outcome definitions must be reconciled by the author. Preserve current methodology and results.
- Do not use a conceptual complexity-benefit curve as empirical evidence; no crossover or threshold is established.

# When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding Agents

- Tural Mehtiyev, Biruk Tadesse, Lawrence Arkoh, and Wesley Assunção
- 2026 preprint, arXiv:2611.09802, version 1. [Paper](https://arxiv.org/abs/2611.09802v1) · [Full text](https://arxiv.org/pdf/2611.09802v1)

## Study and findings

The authors examine three outdated instructions from active open-source repositories. They vary whether each instruction is stale, corrected, or removed, with the underlying maintenance task and code held fixed. Across 22 tasks, the study analyses 732 trajectories for two models. With one outdated test command, Claude Sonnet 5.5 needed about two extra tool calls per run relative to the corrected command. The authors did not detect a corresponding difference in the other two cases.

## Role in Section 2.3

An instruction can be preserved and accessible but inconsistent with the current repository. The study concerns the observed behaviour and recovery effort of coding agents using repository instructions. Its results do not estimate the effects of stale auto memory or enterprise defects.

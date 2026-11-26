# Lost in Context Compaction: When LLM Systems Drop Side Constraints

- Zhiqi Wang, Yichi Zhang, Dongwon Lee, Nathalie Baracaldo, and Yuchen Yang
- 2026 preprint, arXiv:2608.11242, version 2. [Paper](https://arxiv.org/abs/2608.11242v2) · [Full text](https://arxiv.org/html/2608.11242v2)

## Study and findings

ConPACT evaluates compaction on histories with injected constraints across three controlled scenarios. The authors assess semantic retention in the compressed context and use follow-up probes to study whether a model continues to follow the constraint. Version 2 also reports SWE-Natural, a subset of 126 naturally occurring constraints from GitHub issues paired with long coding agent trajectories. In that subset, the highest retention reported among the tested compactors was 28.6%.

## Role in Section 2.3

The study supports discussing constraint loss as a possible effect of compaction and distinguishes preservation from compliance. The SWE-Natural result is a retention measure. The dataset has no corresponding histories generated without the original constraints, so it cannot support the same effective-retention estimate as the controlled scenarios. The study does not establish a Claude Code defect or hallucination rate.

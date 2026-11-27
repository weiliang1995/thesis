# Benchmarking Long-Horizon Agent Context Compaction with CompactionBench

- Banruo Liu, Haoran Qiu, Íñigo Goiri, Jingran Zhou, Rodrigo Fonseca, Ricardo Bianchini, Fan Lai, and Esha Choukse
- November 2026 preprint. [Microsoft Research publication record](https://www.microsoft.com/en-us/research/publication/benchmarking-long-horizon-agent-context-compaction-with-compactionbench/) · [Full text](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/10/CompactionBench_preprint.pdf)

## Study and findings

The study characterises compaction in GitHub Copilot production traces and builds a benchmark of dependent software changes made over persistent coding sessions. The benchmark compares compaction policies using executable repository-level outcomes, along with execution cost and latency. The authors report improved task performance for their progressive compaction method relative to tested synchronous baselines.

## Role in Section 2.3

The benchmark offers evidence that the choice of compaction policy can affect coding task performance in long sessions. It evaluates the results of the changes using repository tests. A test failure by itself does not identify a fabricated API, a lost requirement, or another cause. The production traces and controlled benchmark serve different roles and neither yields an estimate of hallucinations after Claude Code auto-compaction or cross-session handoffs.

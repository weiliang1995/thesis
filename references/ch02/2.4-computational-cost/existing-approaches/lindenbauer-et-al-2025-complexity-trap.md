# The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management

- Authors: Tobias Lindenbauer, Igor Slinko, Ludwig Felder, Egor Bogomolov, Yaroslav Zharov
- Type: arXiv v1, 29 August 2025; workshop research.
- Official source: https://arxiv.org/abs/2508.21433v1
- Full text: https://arxiv.org/html/2508.21433v1
- Reading status: Methods and Table 1 reviewed.
- Archive status: Source record and full-text link only; PDF not archived.

## Evidence and limits
SWE-agent on SWE-bench Verified, five model configurations; raw history, observation masking and model summaries. Table 1 for Qwen3-Coder 480B: mean costs $1.29, $0.61, $0.64 and solve rates 53.4%, 54.8%, 53.8%, respectively. Both cost differences significant against raw; success differences not established. Use table values rather than the inconsistent raw value in the abstract. Comparison is not against native Claude Code. Discuss simple versus expensive context management, not a universal prescription.

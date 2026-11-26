# Context Compression for LLM Agents: A Survey of Methods, Failure Modes, and Evaluation

- Authors: Yifei Wang, Ziteng Wang, Yuling Shi, Silin Chen, Xinrui Wang, Yueqi Wang, Beijun Shen, Linjing Li, Xiaodong Gu, Julian McAuley, Daniel Dajun Zeng
- Publication: 2026, EMNLP 2026
- Source type: Peer-reviewed survey; taxonomy, not an original intervention test
- Official source: https://aclanthology.org/2026.emnlp-main.2396/
- Reading status: Abstract and selected methods/results/limitations reviewed; verify exact comparisons in full text before final prose.
- Archive status: Source record and official full-text link only; PDF not archived.
- Bibliography: Added to `references/references.md`.

## Study and evidence

- Setting: Literature on long-running LLM agents and compression of heterogeneous interaction histories.
- Method and measures: Organizes compression methods, failure modes, and evaluation practices.
- Reported finding: Separates when to compress, what information compression preserves, and whether a later agent can access the preserved information. Useful to discuss possible losses during automatic compaction.
- Limits of inference: The survey's taxonomy is not evidence that Claude Code's native compaction loses a particular requirement or causes defects; consult primary experiments for outcome claims.

## Role in Section 2.3

2.3.1: frame compaction and selective preservation as possible failure points.

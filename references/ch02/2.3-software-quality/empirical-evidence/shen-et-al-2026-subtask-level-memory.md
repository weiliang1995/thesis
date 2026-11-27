# Structurally Aligned Subtask-Level Memory for Software Engineering Agents

- Authors: Kangning Shen, Jingyuan Zhang, Chenxi Sun, Wencong Zeng, Yang Yue
- Publication: 2026, Proceedings of the 43rd International Conference on Machine Learning, PMLR 306
- Source type: Peer-reviewed empirical study
- Official source: https://proceedings.mlr.press/v306/shen26ad.html
- Reading status: Abstract and selected methods/results/limitations reviewed; verify exact comparisons in full text before final prose.
- Archive status: Source record and official full-text link only; PDF not archived.
- Bibliography: Added to `references/references.md`.

## Study and evidence

- Setting: SWE-bench Verified issue-resolution benchmark across multiple model backbones; compares no memory and different memory granularities.
- Method and measures: Store and retrieve experience aligned to subtasks rather than a whole prior issue; compare Pass@1 with vanilla and instance-level memory baselines.
- Reported finding: Reports mean Pass@1 improvement of 4.7 percentage points over vanilla agents across tested backbones; evidence that memory granularity can matter in this setup.
- Limits of inference: Memory is reusable experience across issues, not simply carrying the same task between sessions. Results do not imply that saving more notes always helps or transfer to enterprise E2E outcomes.

## Role in Section 2.3

2.3.2: selective, task-stage-aligned memory and measured benchmark performance.

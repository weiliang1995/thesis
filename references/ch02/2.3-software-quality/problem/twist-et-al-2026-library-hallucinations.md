# Library Hallucinations in LLM-Generated Code: A Risk Analysis Grounded in Developer Queries

- Authors: Lukas Twist, Mark Harman, Helen Yannakoudakis, Jie M. Zhang
- Publication: 2026, EMNLP 2026
- Source type: Peer-reviewed empirical study
- Official source: https://aclanthology.org/2026.emnlp-main.78/
- Reading status: Abstract and selected methods/results/limitations reviewed; verify exact comparisons in full text before final prose.
- Archive status: Source record and official full-text link only; PDF not archived.
- Bibliography: Added to `references/references.md`.

## Study and evidence

- Setting: Code-generation queries based on developer needs, evaluating invented libraries or members across seven LLMs and prompt conditions.
- Method and measures: Measure hallucinated library/API elements under varied prompts, including fabricated library names and temporal changes.
- Reported finding: Documents non-existent library or member references as an output risk under the studied conditions.
- Limits of inference: Does not isolate missing memory, context dilution, or auto-compaction as a cause. Library hallucination is narrower than overall code quality or observed defect density.

## Role in Section 2.3

2.3.1: illustrate a possible output-level failure; keep causal explanation separate.

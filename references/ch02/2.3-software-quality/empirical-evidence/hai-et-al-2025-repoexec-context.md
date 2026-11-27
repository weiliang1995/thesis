# On the Impacts of Contexts on Repository-Level Code Generation

- Authors: Nam Le Hai, Dung Manh Nguyen, Nghi D. Q. Bui
- Publication: 2025, Findings of NAACL 2025
- Source type: Peer-reviewed empirical study
- Official source: https://aclanthology.org/2025.findings-naacl.82/
- Reading status: Abstract and selected methods/results/limitations reviewed; verify exact comparisons in full text before final prose.
- Archive status: Source record and official full-text link only; PDF not archived.
- Bibliography: Added to `references/references.md`.

## Study and evidence

- Setting: RepoExec benchmark of repository-level generation across 18 models.
- Method and measures: Vary dependency context and assess executability, functional correctness, and dependency invocation.
- Reported finding: Full dependency context performs best in the evaluated setting, and smaller context can be misleading; model family and debugging also affect behavior.
- Limits of inference: This is a counterweight to a blanket 'less context is better' claim. It evaluates generated code and dependency use, not real developer defect records, Claude compaction, or task-level E2E.

## Role in Section 2.3

2.3.1–2.3.2: relevant context selection and competing effects of aggressive reduction.

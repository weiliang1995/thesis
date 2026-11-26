# Beyond Repository Boundaries: Cross-Repository Graph Retrieval for Code Generation

- Authors: Minh Le-Anh, Nam Le Hai, Quyen Tran, Anh Nguyen Hoang, Linh Ngo Van, Bach Le, Nghi D. Q. Bui
- Publication: 2026, Findings of EMNLP 2026
- Source type: Peer-reviewed empirical study
- Official source: https://aclanthology.org/2026.findings-emnlp.433/
- Reading status: Abstract and selected methods/results/limitations reviewed; verify exact comparisons in full text before final prose.
- Archive status: Source record and official full-text link only; PDF not archived.
- Bibliography: Added to `references/references.md`.

## Study and evidence

- Setting: Repository-level generation with dependencies beyond the local repository; evaluated on RepoExec, DevEval, and VersionExec.
- Method and measures: Represent local repository and external library relations as a graph and retrieve dependency-relevant context; compare with retrieval baselines on functional and dependency metrics.
- Reported finding: Reports benchmark improvements including functional Pass@1 gains up to 6.3% in its reported comparison and better handling of version-specific dependencies.
- Limits of inference: External package/library graphs are not identical to the enterprise sibling-repository arrangement in this thesis. Avoid claiming this technique improves Trade-Harness or observed defects.

## Role in Section 2.3

2.3.2: a concrete retrieval technique and a boundary of local-only context.

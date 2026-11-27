# Context Length Alone Hurts LLM Performance Despite Perfect Retrieval

- Authors: Yufeng Du, Minyang Tian, Srikanth Ronanki, Subendhu Rongali, Sravan Babu Bodapati, Aram Galstyan, Azton Wells, Roy Schwartz, Eliu A Huerta, Hao Peng
- Publication: 2025, Findings of EMNLP 2025
- Source type: Peer-reviewed empirical study
- Official source: https://aclanthology.org/2025.findings-emnlp.1264/
- Reading status: Abstract and selected methods/results/limitations reviewed; verify exact comparisons in full text before final prose.
- Archive status: Source record and official full-text link only; PDF not archived.
- Bibliography: Added to `references/references.md`.

## Study and evidence

- Setting: Controlled long-input tasks including mathematical reasoning, question answering, and code-related tasks; relevant information is made retrievable.
- Method and measures: Vary input length while controlling retrieval success; compare downstream task performance.
- Reported finding: A longer input can reduce task performance even when the model retrieves the relevant item. This qualifies the assumption that retrieval alone solves long-context use.
- Limits of inference: Does not establish an agent-specific context-window threshold, the effect of Claude Code compaction, or an effect on front-end defects.

## Role in Section 2.3

2.3.1: distinguish context length, retrieval, and use of retrieved information.

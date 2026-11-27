# Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks

- Authors: Dipesh KC, Anjila Budathoki
- Publication: 2026, EMNLP 2026
- Source type: Peer-reviewed empirical study
- Official source: https://aclanthology.org/2026.emnlp-main.738/
- Reading status: Abstract and selected methods/results/limitations reviewed; verify exact comparisons in full text before final prose.
- Archive status: Source record and official full-text link only; PDF not archived.
- Bibliography: Added to `references/references.md`.

## Study and evidence

- Setting: 75 source repository tasks, 181 interruption points, and 724 takeover runs per successor model; four information views and three successor models.
- Method and measures: Freeze partial repository states; compare repository-only, raw trace, summary note, and structured-note handoffs on agent events, prompt tokens, and task outcomes.
- Reported finding: Context-bearing handoffs reduce median agent events by 20–59% and cumulative prompt tokens by 42–63% in the reported comparisons. Effects on solved rate depend on successor model.
- Limits of inference: Main consistent evidence is rediscovery effort; do not translate this into fewer defects. An interrupted agent takeover is not necessarily the same as routine multi-session use by one developer.

## Role in Section 2.3

2.3.1–2.3.2: cross-session handoff, what to carry forward, and mixed success outcomes.

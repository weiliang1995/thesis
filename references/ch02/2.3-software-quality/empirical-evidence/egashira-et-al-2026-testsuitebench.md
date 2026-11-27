# TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications

- Authors: Kazuki Egashira, Niels Mündler-Sasahara, Mark Niklas Müller, Martin Vechev
- Publication: 2026, arXiv:2610.13065, preprint
- Source type: Empirical preprint; peer-review status not established
- Official source: https://arxiv.org/abs/2610.13065
- Reading status: Abstract and selected methods/results/limitations reviewed; verify exact comparisons in full text before final prose.
- Archive status: Source record and official full-text link only; PDF not archived.
- Bibliography: Added to `references/references.md`.

## Study and evidence

- Setting: 165 open-source applications, each with specifications, a reference implementation and tests, and requirement-targeted mutants.
- Method and measures: Ask coding agents to generate test suites from specifications; check validity and mutant detection.
- Reported finding: Generated suites are often valid and pass the reference implementation, yet reported mutation scores remain below 60% for the evaluated agents. This questions what a passing generated suite establishes.
- Limits of inference: Rust/Go/C++ application setting and mutation score differ from front-end E2E pass rate and real defect density; do not use the reported percentage as an E2E estimate.

## Role in Section 2.3

2.3.3: justify careful interpretation of agent-generated tests and pass-rate measures.

# More with Less: An Empirical Study of Turn-Control Strategies for Efficient Coding Agents

- Authors: Pengfei Gao and Chao Peng
- Publication: ICSE 2026; preprint 2025.
- DOI: https://doi.org/10.1145/3744916.3773250
- Official source: https://arxiv.org/abs/2510.16786
- Full text: https://arxiv.org/html/2510.16786v1
- Reading status: Abstract, introduction, experimental design summary reviewed.
- Archive status: Source record and link only; PDF not archived.

## Evidence and limits
100 SWE-bench Verified tasks, Claude 4 Sonnet, Gemini 2.5 Pro and GPT 4.1; unlimited turns, fixed limits with reminders, and dynamic extension. Authors report 24–68% cost reductions with a fixed budget at the 75th percentile of unrestricted turns; dynamic allocation saves a further 12–24% versus fixed alternatives with comparable or better solve rates in the studied comparisons. The limits concern model turns, not human-estimated task duration or E2E correction loops. Supports adaptive allocation, not validation of the thesis's complexity categories.

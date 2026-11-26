# Section 2.1 — Evolution of AI Agent Engineering

21 source records, grouped by primary role. All source records contain official links; no full-text files have been downloaded. These are reading candidates, not approved thesis citations. For papers, check the applicable license before archiving in Git. For web articles, read the linked original or retain a personal copy locally where permitted.

## Sources

### Agent execution model (2.1.1)

- [ReAct: Synergizing Reasoning and Acting in Language Models](agent-execution-model/yao-et-al-2023-react.md) — Shunyu Yao et al., 2023 (ICLR; arXiv v3) (Peer-reviewed conference paper)
- [A Survey on Large Language Model based Autonomous Agents](agent-execution-model/wang-et-al-autonomous-agents-survey.md) — Lei Wang et al., 2023 preprint; revised 2025 (Academic survey; journal DOI 10.1007/s11704-024-40231-1)
- [Building effective agents](agent-execution-model/anthropic-2024-building-effective-agents.md) — Anthropic, 2024-12-19 (Industry engineering article)

### Engineering approaches (2.1.2–2.1.4)

- [The Prompt Report: A Systematic Survey of Prompt Engineering Techniques](prompt-engineering/schulhoff-et-al-2025-prompt-report.md) — Schulhoff et al., 2024; revised 2025 (Academic survey / arXiv version)
- [A comprehensive taxonomy of prompt engineering techniques for large language models](prompt-engineering/liu-et-al-2026-prompt-taxonomy.md) — Yao-Yang Liu et al., 2025 online; 2026 volume (Open-access journal review)
- [A Survey of Context Engineering for Large Language Models](context-engineering/mei-et-al-2025-context-engineering-survey.md) — Lingrui Mei et al., 2025 (Academic survey / preprint)
- [Effective context engineering for AI agents](context-engineering/anthropic-2025-effective-context-engineering.md) — Anthropic, 2025-09-29 (Industry engineering article)
- [How Claude remembers your project](context-engineering/anthropic-nd-claude-code-memory.md) — Anthropic, n.d.; accessed 2026-11-26 (Official product documentation)
- [A comprehensive survey of prompt engineering and context engineering techniques in large language models](context-engineering/debnath-et-al-2026-prompt-context-survey.md) — Tonmoy Debnath et al., 2026 (Peer-reviewed journal review, Computer Science Review 62, 100979)
- [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](context-engineering/gloaguen-et-al-2026-evaluating-agents-md.md) — Gloaguen et al., 2026 (Empirical preprint, v3)
- [On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents](context-engineering/lulla-et-al-2026-agents-md-efficiency.md) — Lulla et al., 2026 (Empirical preprint, v2)
- [RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation](context-engineering/zhang-et-al-2023-repocoder.md) — Zhang et al., 2023 (EMNLP empirical paper)
- [Lost in the Middle: How Language Models Use Long Contexts](context-engineering/liu-et-al-2024-lost-in-the-middle.md) — Liu et al., 2024 (TACL empirical paper)
- [My AI Adoption Journey](harness-engineering/hashimoto-2026-my-ai-adoption-journey.md) — Mitchell Hashimoto, 2026-02-05 (Practitioner article)
- [Effective harnesses for long-running agents](harness-engineering/young-2025-effective-harnesses.md) — Justin Young (Anthropic), 2025-11-26 (Industry engineering report)
- [Harness engineering: leveraging Codex in an agent-first world](harness-engineering/lopopolo-2026-harness-engineering.md) — Ryan Lopopolo (OpenAI), 2026-02-11 (Industry case report)
- [Improving Deep Agents with harness engineering](harness-engineering/trivedy-2026-improving-deep-agents.md) — Vivek Trivedy (LangChain), 2026-02-17 (Industry benchmark report)
- [The Anatomy of an Agent Harness](harness-engineering/trivedy-2026-anatomy-agent-harness.md) — Vivek Trivedy (LangChain), 2026-03-10 (Industry architecture article)
- [Harness design for long-running application development](harness-engineering/rajasekaran-2026-harness-design.md) — Prithvi Rajasekaran (Anthropic), 2026-03-24 (Industry experimental report)
- [Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems](harness-engineering/barbaste-et-al-2026-coding-agent-harnesses.md) — Paul Barbaste et al., 2026 (Academic preprint)
- [What makes a harness a harness: necessary and sufficient conditions for an agent harness](harness-engineering/macedo-2026-harness-definition.md) — Sanderson Oliveira de Macedo, 2026 (Academic preprint)

## Downloading permitted PDFs locally

From this directory, run `python3 download_pdfs.py`. It attempts the seven direct PDF URLs, checks for a PDF header, and never overwrites an existing file. It does not commit anything. Review each file and license before adding it to Git. The Debnath journal article requires publisher or institutional access; use its DOI. Industry articles are linked rather than copied verbatim.

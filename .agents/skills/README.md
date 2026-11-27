# Thesis Research Skills

These Markdown skills support the thesis workflow. The original research and review skills draw on design patterns in [Matt Pocock's skills](https://github.com/mattpocock/skills) (MIT), particularly grilling, grill-with-docs, domain-modeling and code-review.

| Skill | Responsibility | Invocation |
| --- | --- | --- |
| [research-grill](research-grill/SKILL.md) | Challenge and confirm research decisions | User-invoked |
| [thesis-review](thesis-review/SKILL.md) | Read-only claim-evidence, terminology and thesis alignment review | User-invoked |
| [research-terminology](research-terminology/SKILL.md) | Establish and maintain confirmed definitions | User/model-invoked |
| [apply-review](apply-review/SKILL.md) | Review one finding per round and record decisions as they are made | User-invoked |
| [sync-thesis](sync-thesis/SKILL.md) | Update the manuscript from confirmed project documents | User-invoked |

Examples (natural language or slash commands if supported by the runtime):

- `/thesis-review`: all three axes, active manuscript.
- `/thesis-review ch02 evidence`: claim-evidence review for Chapter 2.
- `/thesis-review terminology`: terminology consistency.
- `/thesis-review alignment`: cross-chapter traceability.
- `/thesis-review diff <base-ref>`: review changes against a specified base.
- `/research-grill <decision>`: discuss a research decision.
- `/research-terminology <term>`: establish or revise a definition.
- `apply-review alignment-review.md` starts a decision session on the saved alignment report.
- `sync-thesis .agents/docs/glossary.md` synchronizes the active thesis with the confirmed glossary entries.

If the agent cannot discover repository skills automatically, explicitly ask it to read the corresponding SKILL.md and follow its referenced instructions. Independent reviewers depend on runtime support; the review must disclose when only separate passes were possible.

Use the [project map](../../AGENTS.md) to find the standards, glossary, decision records and research mapping. Keep project rules and research definitions in the linked documents.

# Thesis Research Skills

Three composable, Markdown-based skills adapted from the design patterns in [Matt Pocock's skills](https://github.com/mattpocock/skills) (MIT), particularly grilling, grill-with-docs, domain-modeling and code-review. The research-specific instructions are written for this thesis.

| Skill | Responsibility | Invocation |
| --- | --- | --- |
| [research-grill](research-grill/SKILL.md) | Challenge and confirm research decisions | User-invoked |
| [thesis-review](thesis-review/SKILL.md) | Read-only claim-evidence, terminology and thesis alignment review | User-invoked |
| [research-terminology](research-terminology/SKILL.md) | Establish and maintain confirmed definitions | User/model-invoked |

Examples (natural language or slash commands if supported by the runtime):

- `/thesis-review`: all three axes, active manuscript.
- `/thesis-review ch02 evidence`: claim-evidence review for Chapter 2.
- `/thesis-review terminology`: terminology consistency.
- `/thesis-review alignment`: cross-chapter traceability.
- `/thesis-review diff <base-ref>`: review changes against a specified base.
- `/research-grill <decision>`: discuss a research decision.
- `/research-terminology <term>`: establish or revise a definition.

If the agent cannot discover repository skills automatically, explicitly ask it to read the corresponding SKILL.md and follow its referenced instructions. Independent reviewers depend on runtime support; the review must disclose when only separate passes were possible.

Review, decision and revision are separate. The reviewer reports, the researcher confirms design/terminology, and manuscript changes require authorization. GLOSSARY.md and research/decisions/ hold confirmed definitions and decisions, while research/research-mapping.md remains the traceability workspace.

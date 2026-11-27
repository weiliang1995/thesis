# Thesis structure

## Manuscript

| Location | Role |
| --- | --- |
| [Front matter](../../front-matter.md) | Title, abstract and contents. |
| [Chapter 1](../../chapters/ch01-introduction/) | Research problems, objectives, questions, scope and limitations. |
| [Chapter 2](../../chapters/ch02-literature-review/) | Literature, research gaps and rationale for the study. |
| [Chapter 3](../../chapters/ch03-research-methodology/) | Workflow conditions, task allocation, measures, analysis and threats to validity. Files and headings retain the original proposal's Section 4 numbering. |
| [Original proposal](../../proposal/) | Historical version of the research plan. |
| [Deprecated material](../../deprecated/) | Superseded drafts, including an earlier results draft. |

The original DOCX is available separately in the ChatGPT conversation migration archive.

## Cross-chapter navigation

- When a problem statement or research question changes, use the [research mapping](research-mapping.md) to trace its literature rationale, method, measures and expected or available results. The mapping is a work in progress.
- For the workflow comparison, read the definitions in the [glossary](glossary.md#study-conditions) alongside the [research variables](../../chapters/ch03-research-methodology/4.1.3-research-variables.md) and [experimental procedure](../../chapters/ch03-research-methodology/4.1.4-experimental-procedure.md).
- Consult the [decision records](decisions/README.md) for the rationale behind confirmed research design choices.

## Chapter 2 outline (working structure)

| Section | Purpose |
| --- | --- |
| 2.1 Evolution of AI Agent Engineering | Introduce the LLM-based agent execution model, then prompt engineering, context engineering and harness engineering, their scope and relationships. These are complementary approaches, not necessarily successive replacements. |
| 2.2 Delivery Efficiency | Examine workflow coordination, planning, human intervention and rework; consider delivery lead time as an outcome. |
| 2.3 Context Continuity, Memory Retention, and the Quality of Agent-Assisted Code | Examine context and memory continuity, their possible relationships to code output, and the evidence for retrieval and memory techniques; interpret defect density and E2E pass rate within their measurement limits. |
| 2.4 Computational Cost | Examine context redundancy, repeated execution and orchestration overhead; consider token consumption and trade-offs. |
| 2.5 Literature Synthesis | Integrate the gaps, design implications, outcome measures and rationale for evaluating Trade-Harness. |

The 2.3 heading is agreed; the wording of the other problem-oriented headings remains subject to review.

## Section 2.1 scope

- 2.1.1 LLM-based Agent Execution Model: contrast single-call interaction with iterative agent execution, explain reasoning/action/observation, tools, and the distinction between autonomous agents and predefined workflows. Keep the discussion at execution-model level; avoid model internals and detailed architecture taxonomies.
- 2.1.2 Prompt Engineering: instruction design.
- 2.1.3 Context Engineering: task-relevant information management.
- 2.1.4 Harness Engineering: execution environment and orchestration.
- 2.1.5 Summary: relate the approaches and transition to the three problem-oriented sections without assuming performance improvements.

## Literature materials

- [References index](../../references/README.md) introduces the collection.
- [Bibliography](../../references/references.md) lists approved sources. [Candidate literature](../../references/todo.md) tracks sources awaiting review.
- [Chapter 2 materials](../../references/ch02/) group sources by the role they serve in the literature review.
- [Section 2.1 source index](../../references/ch02/2.1-agent-engineering/README.md) lists sources on agent execution and engineering.

## Directory layout

```
references/
  README.md
  references.md
  todo.md
  ch02/
    2.1-agent-engineering/
      agent-execution-model/
      prompt-engineering/
      context-engineering/
      harness-engineering/
    2.2-delivery-efficiency/
      problem/
      existing-approaches/
      empirical-evidence/
    2.3-software-quality/
      problem/
      existing-approaches/
      empirical-evidence/
    2.4-computational-cost/
      problem/
      existing-approaches/
      empirical-evidence/
    2.5-literature-synthesis/
```

Research gaps are synthesized from the evidence within each problem rather than treated as a separate source type. Section 2.5 may contain synthesis notes or cross-topic comparative material.

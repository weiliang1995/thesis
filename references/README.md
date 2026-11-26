# References and Chapter 2 literature review

This directory supports the thesis on Trade-Harness. `references.md` remains the bibliography and `todo.md` tracks candidate references. The `ch02/` directory organizes source material by its role in the literature review, not by publication type.

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

## Argument structure for each problem (2.2–2.4)

1. **Problem identification:** Establish the problem, its causes and consequences using literature.
2. **Existing approaches:** Explain how prior work addresses the problem, including alternatives to structured orchestration.
3. **Mechanisms of action:** Explain why a mechanism may affect an outcome, intermediate steps, assumptions, boundary conditions and competing effects. Store mechanism-related sources under existing-approaches unless their primary contribution is empirical.
4. **Empirical evidence:** Compare positive, negative and mixed findings, study settings, tasks, metrics and limitations. Distinguish benchmark correctness from enterprise software quality or delivery performance.
5. **Research gap:** Synthesize what remains insufficiently established and derive implications for the study. Do not treat a gap as established until the literature supports it.

The final synthesis should connect literature evidence → problem statement → design rationale → proposed mechanism → expected outcome → evaluation metric → research question. Trade-Harness originated in industry; the review retrospectively establishes its rationale rather than claiming the literature preceded its design. No improvement is assumed. A workflow-level quasi-experiment does not isolate the causal contribution of individual mechanisms without suitable measurements.

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

## Source collection rules

- Collect relevant sources only after review and agreement; prefer primary academic research for empirical claims. Industry documentation can establish terminology and engineering practice, but is not by itself evidence of effectiveness.
- Store one permitted copy of each paper, using a stable filename such as `author-year-short-title.pdf`; cross-reference it from other sections instead of duplicating the file. For sources without permitted full text, record a DOI or official URL.
- Record citation, source URL/DOI, study setting, method, metrics, findings, limitations and the specific claim supported. Identify whether evidence is direct or indirect.
- Include counterevidence and overheads; do not select sources solely because they support observed results. Distinguish retrospective explanations from pre-specified hypotheses.
- Keep the existing bibliography and candidate list intact. Candidate sources are catalogued separately; archive status is recorded per source.

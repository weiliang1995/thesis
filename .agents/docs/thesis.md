# Thesis standards

## Writing and editing

- Preserve the author's natural academic English and keep the title, problem statements, objectives, research questions, literature review, methodology and outcomes consistent.
- Before large edits, outline the proposed changes and keep the edit focused on the requested scope.
- Use diffs for review. Check equations, merged cells and table layouts against the original DOCX before final submission.

## Academic argumentation and terminology

- Define key terms in accordance with the cited literature and use them consistently across chapters. Where concepts overlap or definitions differ, acknowledge the overlap and distinguish their primary focus; do not impose mutually exclusive boundaries or claim that newer approaches replace older ones without evidence.
- Develop arguments progressively: establish the motivation, define the concept, explain its mechanisms and limitations, and connect it to the next discussion. Use accessible examples where useful, clearly distinguishing illustrations from empirical findings.
- Match the strength and scope of every claim to its supporting evidence. Distinguish academic empirical results, survey classifications, practitioner guidance, and proposed mechanisms. Do not generalize benchmark findings to enterprise development outcomes without qualification.
- Explain limitations and competing effects without presupposing that Trade-Harness or any individual mechanism improves outcomes. Use conditional language where effectiveness has not been established; distinguish plausible rationale from demonstrated results and association from causation.

## Review requirements

- Review the active manuscript using the [thesis structure](architecture.md#manuscript). Include historical material in findings only when the researcher requests it. Treat unwritten results as pending.
- Apply the confirmed [study-condition definitions](glossary.md#study-conditions) in every edit or review that describes or compares this study's workflows. Review this wherever it occurs in scope, regardless of the axes selected. Flag contradictions and omissions that alter the meaning, and cite both the manuscript and glossary locations. Brief labels may refer back to the established definitions.
- Obtain the researcher's explicit approval before changing a confirmed definition. Describe any paper-specific comparison conditions in the context of that paper.
- Keep thesis reviews read-only. Apply proposed changes when the researcher authorizes manuscript revision.

## Argument structure for each problem (2.2–2.4)

1. **Problem identification:** Establish the problem, its causes and consequences using literature.
2. **Existing approaches:** Explain how prior work addresses the problem, including alternatives to structured orchestration.
3. **Mechanisms of action:** Explain why a mechanism may affect an outcome, intermediate steps, assumptions, boundary conditions and competing effects. Store mechanism-related sources under existing-approaches unless their primary contribution is empirical.
4. **Empirical evidence:** Compare positive, negative and mixed findings, study settings, tasks, metrics and limitations. Distinguish benchmark correctness from enterprise software quality or delivery performance.
5. **Research gap:** Synthesize what remains insufficiently established and derive implications for the study. Do not treat a gap as established until the literature supports it.

The final synthesis should connect literature evidence → problem statement → design rationale → proposed mechanism → expected outcome → evaluation metric → research question. Trade-Harness originated in industry; the review retrospectively establishes its rationale rather than claiming the literature preceded its design. No improvement is assumed. A workflow-level quasi-experiment does not isolate the causal contribution of individual mechanisms without suitable measurements.

## Source collection rules

- Collect relevant sources only after review and agreement; prefer primary academic research for empirical claims. Industry documentation can establish terminology and engineering practice, but is not by itself evidence of effectiveness.
- Review the applicable license before archiving a paper. Store one permitted copy with a stable filename such as `author-year-short-title.pdf` and link it from other sections. For sources without permitted full text, record a DOI or official URL.
- Record citation, source URL/DOI, study setting, method, metrics, findings, limitations and the specific claim supported. Identify whether evidence is direct or indirect.
- Include counterevidence and overheads; do not select sources solely because they support observed results. Distinguish retrospective explanations from pre-specified hypotheses.
- Keep the existing bibliography and candidate list intact. Candidate sources are catalogued separately; archive status is recorded per source.

## Version management

- Advance the merged manuscript version after the author approves a milestone and merges its PR into `main`.
- Record substantive changes and their rationale in [changelog.md](../../changelog.md). Git commits and PR diffs provide the detailed audit trail.
- Create a versioned Git tag on `main` after the author approves a merged milestone.

---
name: apply-review
description: Walk through a saved thesis review report one decision at a time, recording the researcher's answers in the project documents and tracking progress in the report.
disable-model-invocation: true
---

# Apply Review

Start with a report path or filename, for example `apply-review alignment-review.md`. Resolve a bare filename against the repository and its `research/` directory. Ask for a path if more than one document matches.

1. **Scan before asking.** Read the selected report and scan the source-of-truth documents under `.agents/docs/`, including confirmed decision records. Use the [project map](../../../AGENTS.md) and [revision standards](../../docs/thesis.md#revision-and-source-of-truth) to identify which document governs each finding. Compare each finding with those documents and existing report notes. Skip questions already answered by confirmed decisions or recorded as resolved. Record project-document changes that are already present. Treat manuscript references in the report as context for the decision. Leave inspection of manuscript files to [sync-thesis](../sync-thesis/SKILL.md).
2. **Ask one question.** Pick the next undecided finding in report order. Address a prerequisite first if it affects the decision. State the finding ID, what is already known, and the specific choice or missing detail. Offer a recommendation and practical alternatives where the evidence supports them. If a finding contains several decisions, ask about one at a time. Wait for the researcher after each question. If the reply is ambiguous, clarify the same item before moving on.
3. **Update after each answer.** For a confirmed answer, update the relevant project document using the [revision standards](../../docs/thesis.md#revision-and-source-of-truth). Use the [glossary entry format](../research-terminology/references/glossary-format.md) and the [decision record guidance](../../docs/decisions/README.md) where applicable. For a local correction, record approval and link the source identified in the report or project documents. Note declined or deferred items in the report, including the dependency if known. Keep each note under its finding ID with the decision, date and source link. Update the existing note if a decision changes.
4. **Verify and continue.** Check the affected project document and report entry before asking the next question. Mark a document-only action complete once verified in the project documents. If a finding also requires manuscript changes, record the decision as confirmed and keep synchronization pending unless the report or researcher explicitly confirms completion. Keep edits scoped to project documents and the selected report. Apply manuscript changes in a separate [sync-thesis](../sync-thesis/SKILL.md) invocation.

When the researcher pauses or the report has no undecided items, summarize recorded decisions, completed document updates, deferred items and confirmed entries awaiting synchronization. If the researcher resumes later, reread the report and project documents before asking the next question.

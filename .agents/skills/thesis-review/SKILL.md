---
name: thesis-review
description: Review the thesis for claim-evidence fit, terminology consistency and research traceability; report findings without modifying the manuscript.
disable-model-invocation: true
---

# Thesis Review

Run a read-only, evidence-grounded review along independent axes. Do not resolve research decisions, edit manuscript text, change the glossary or approve citations during review.

## 1. Establish scope and snapshot

Read AGENTS.md. Pin the current branch/commit (or explicitly identify uncommitted files); record the scope and selected axes. Default to all three axes over the active manuscript. Accept a chapter, section or path, one or more axes (evidence, terminology, alignment), or a diff against a supplied base ref. These can be combined. For diff mode without a base, request one; verify it resolves and identify changed files against the merge base.

Inspect the live repository structure: front-matter.md, chapters/, references/references.md, references/README.md, research/research-mapping.md, GLOSSARY.md and relevant research/decisions/ records. Read cross-chapter dependencies even for a scoped review. Treat references/todo.md as candidates, not verified evidence. Exclude proposal/ and deprecated/ from active findings unless requested; distinguish historical context from current commitments. Do not assume README chapter numbering is current. A missing or incomplete chapter is not a completed result.

## 2. Run selected axes

- **Evidence:** [claim-evidence.md](references/claim-evidence.md)
- **Terminology:** [terminology-alignment.md](references/terminology-alignment.md)
- **Alignment:** [thesis-alignment.md](references/thesis-alignment.md)

For each axis, load its reference and [report format](references/review-report-format.md). Where independent subagents are available, run selected axes in parallel with fresh contexts, the same pinned snapshot and scope, their own criteria and source access. Do not expose other reviewers' findings before they finish. Otherwise run separate passes, keeping findings distinct, and disclose that isolation was unavailable. Never claim a subagent ran if it did not.

Complete the axis-specific coverage criteria or report the exact unreviewed sections, claims, terms or links. For large reviews, partition by chapter and record partial coverage; do not silently sample or claim exhaustiveness.

## 3. Report

Aggregate by axis; preserve distinct findings and cross-link overlapping issues without erasing them. Cite exact manuscript locations and evidence locations. Mark confirmed findings separately from uncertainty and missing evidence. Include scope, coverage, limitations, findings and next actions in the [report format](references/review-report-format.md). Present the report in the conversation by default; save it only when requested.

Route unresolved design choices to research-grill (recommend manual invocation), unresolved definitions to research-terminology, and unsupported claims to source verification or a bounded wording/citation proposal. Do not make those changes automatically.

## Completion

Each selected axis has its own coverage statement, evidence-backed findings or explicit no-finding result, and unverified/outstanding items. No changes have been made to the manuscript or research definitions.

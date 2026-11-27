---
name: thesis-review
description: Review the thesis for claim-evidence fit, terminology consistency and research traceability; report findings without modifying the manuscript.
disable-model-invocation: true
---

# Thesis Review

Run a read-only, evidence-grounded review along independent axes. Do not resolve research decisions, edit manuscript text, change the glossary or approve citations during review.

## 1. Establish scope and snapshot

Read the [project map](../../../AGENTS.md), [thesis standards](../../docs/thesis.md) and [thesis structure](../../docs/architecture.md). Pin the current branch/commit and note whether uncommitted changes affect reviewed files. Record scope and axes. Default to all three axes over the active manuscript. Accept a chapter, section or path, one or more axes (evidence, terminology, alignment), or a diff against a supplied base ref. These can be combined. For diff mode without a base, ask for the base before reviewing the diff. Verify the base resolves, identify changed files against the merge base and include relevant dependent context. If scope is absent or ambiguous, report the limitation and ask only for information needed to proceed.

Use the structure map to locate the manuscript and literature. Read relevant cross-chapter dependencies, the [glossary](../../docs/glossary.md), [research mapping](../../docs/research-mapping.md) and relevant [decision records](../../docs/decisions/README.md). If a file or directory is absent, report that and continue with accessible material.

## 2. Check the study conditions and run selected axes

Apply the [review requirements](../../docs/thesis.md#review-requirements) in every review, including the check of [confirmed study conditions](../../docs/glossary.md#study-conditions) across the selected scope.

- **Evidence:** [claim-evidence.md](references/claim-evidence.md)
- **Terminology:** [terminology-alignment.md](references/terminology-alignment.md)
- **Alignment:** [thesis-alignment.md](references/thesis-alignment.md)

For each axis, load its reference and [report format](references/review-report-format.md). Run distinct passes and keep findings separate. Independent reviewers may be used only when runtime support exists and the same pinned snapshot, scope, criteria and source access can be provided. Otherwise disclose that review was performed in one context. Never claim isolation or coverage that did not occur.

Complete the axis-specific coverage criteria or report the exact unreviewed sections, claims, terms or links. For large reviews, partition by chapter and record partial coverage; do not silently sample or claim exhaustiveness.

## 3. Report

Aggregate by axis; preserve distinct findings and cross-link overlapping issues without erasing them. Cite exact manuscript locations and evidence locations. Mark confirmed findings separately from uncertainty and missing evidence. Include scope, coverage, limitations, findings and next actions in the [report format](references/review-report-format.md). Present the report in the conversation by default; save it only when requested.

Route unresolved design choices to research-grill (recommend manual invocation), unresolved definitions to research-terminology, and unsupported claims to source verification or a bounded wording/citation proposal. Do not make those changes automatically.

## Completion

Each selected axis has its own coverage statement, findings or explicit no-finding result, and unverified/outstanding items. Report incomplete coverage plainly. The review does not modify manuscript text, definitions or research decisions.

# Changelog

This log summarizes substantive thesis repository revisions. Proposed changes are reviewed through pull requests and merged into `main` only after author approval.

## Version conventions

- **v0.1.0** — imported proposal baseline (label only; tag not yet created).
- **v0.2.0 (planned)** — Chapter 1 alignment after author review and merge.
- Future milestones are set by the author-approved scope; do not bump version for every wording commit.
- `Unreleased` entries describe changes on the review branch, **not** the merged `main` version. Apply a release label and Git tag only after the milestone is merged.

## Unreleased (target: v0.2.0) — 2026-11-09

### Added
- `README.md`: record manuscript baseline version, pending Chapter 1 milestone, and PR/tag release policy.
- `references/todo.md`: two papers to read and evaluate for Chapter 1.2.1 and Chapter 2.1, with potential claims, caution notes, and target sections.

### Changed
- `chapters/01-introduction/1-introduction.md`: clarify the study as an evaluation of a structured agent orchestration workflow rather than an investigation of agent autonomy alone.
- `chapters/01-introduction/1.2-problem-statement.md`: structure the overall problem as **practical engineering problem → empirical research gap → research aim**, then introduce three related concerns.
- `chapters/01-introduction/1.2.1-*.md`, `1.2.2-*.md`, `1.2.3-*.md`: frame the subproblems around delivery efficiency, software quality, and computational cost; avoid claiming baseline tools lack all memory or agentic functionality.
- `chapters/01-introduction/1.3-research-objectives.md`: apply the author-approved main objective and three ROs (evaluate delivery efficiency; examine software quality; assess computational resource efficiency and associated cost), explicitly tied to observed metrics. Task complexity remains an analytical dimension rather than RO4.
- `chapters/01-introduction/1.4-research-questions.md`: apply the author-approved wording for the three corresponding RQs; preserve the comparative, non-causal framing.

- `chapters/01-introduction/1.6.1-research-delimitations.md`: align delimitations with the workflow-level comparison (same Claude Code CLI and Sonnet 4.6), clarify that architecture redesign is excluded while architectural constraints still matter, and retain the existing two-developer wording pending supervisor review.

### Research source tracking
- Expand `references/todo.md` into a thematic reading queue covering prompt-based developer work, real-world agent misalignment (Tang et al., 2026), complex tasks (SWE-Bench Pro), native configuration capabilities (Galster et al., 2026), nondeterminism (Atıl et al., 2025), context/cost overhead (Gloaguen et al., 2026), and comparable execution harnesses.
- Add links to official Claude Code and Claude Sonnet 4.6 documentation to support an accurate baseline description in Chapter 1.5.2 and Chapter 4.1.3.
- **No newly identified candidate study has been inserted into `references/references.md` or cited in thesis prose.** Chapter 1.1–1.1.4 and 1.5.2 remain pending review/drafting.

### Unchanged / pending
- No changes to Chapter 2, Chapter 3, Chapter 4, the approved bibliography, data, evaluation metrics, or experimental setup. Two-developer sample wording remains pending supervisor review.
- Literature in `references/todo.md` still requires author reading and approval before adding new citations.
- Chapter 1 changes are proposed for author review and are **not merged into `main`**.

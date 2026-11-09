# Trade-Harness Thesis

This repository contains a section-by-section Markdown migration of the original 28-page project proposal. The imported baseline preserves the original thesis argument and structure. Academic revisions are proposed and reviewed in separate branches and pull requests.

## Manuscript version and status

| Field | Status |
| --- | --- |
| Current merged manuscript baseline | **v0.1.0 — Original proposal migration** |
| Working milestone | **v0.2.0 — Chapter 1 alignment (in progress)** |
| Review | [PR #1 — Chapter 1 Structural Revision](https://github.com/weiliang1995/thesis/pull/1) |
| Publication status | Draft; **not a final submission** |

The version here tracks the **thesis manuscript**, not a release of the Trade-Harness framework.

### Version management

- The version of the **merged** manuscript advances only when a milestone is approved and the corresponding PR is merged into `main` by the author.
- `v0.1.0` names the imported proposal baseline; it is a version label, **not a claim that a Git tag has been created**.
- `v0.2.0` is reserved for the completed Chapter 1 structural revision. Subsequent milestones can cover the literature/related work, methodology, results, and final review.
- `changelog.md` records substantive changes and their rationale. Git commits and PR diffs provide the detailed audit trail.
- Create a versioned Git tag on `main` only after the author approves the milestone. Do not tag an unmerged draft branch.

## Repository layout

Sections are organized in `chapters/` using the **original proposal chapter numbering** (including Chapter 4 = Research Methodology). `front-matter.md` contains the title and abstract. `references/references.md` contains the approved bibliography, while `references/todo.md` tracks candidate literature awaiting author review.

See `AGENTS.md` for editing conventions. Check equations, merged cells, and table layouts against the original DOCX before final submission.

The original source DOCX is available separately in the ChatGPT conversation migration archive.

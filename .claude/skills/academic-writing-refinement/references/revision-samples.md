# Historical revision samples and provenance

These excerpts document editing decisions and support review of the author's existing prose. They are not a corpus of verified human-only writing. Do not copy them into new thesis text or reuse their claims without checking current definitions.

Repository: weiliang1995/thesis.

## Direct opening

Commit [bf36a24](https://github.com/weiliang1995/thesis/commit/bf36a247c7bfc83b58ea7d0f7365f405232d7465), chapters/01-introduction/1-introduction.md.

Before:
> AI coding assistants now support more than code generation. They can also help developers plan, modify, test, and review code.

After:
> Nowadays, Large Language Models (LLMs) play an important role in software development. Besides code generation, AI coding assistants can also help developers to plan, test, and review code.

Observation: direct introductory framing and ordinary transitions. The change also alters the conceptual starting point; it is not a purely stylistic substitution.

## Concrete explanation

Commit [879aaec](https://github.com/weiliang1995/thesis/commit/879aaecd7cf7fabb4eefe57b43f9513906bff461), chapters/01-introduction/1.1.1-agentic-ai-in-software-engineering.md.

Before:
> Unlike tools that only return code suggestions, coding agents can interact with development environments, inspect repository files, execute commands, and use the results to decide their next actions.

After (excerpt):
> For example, in front-end engineering, a Product Requirements Document (PRD) is provided by product manager to start a SDLC, agent can first parse the document, retrieving the information, inject with development environment context, such as codebase, coding standards and linting rule.

Observation: a real engineering example develops the explanation. The historical grammar is not a recommended pattern; do not reproduce its errors or assume every example is accurate.

## Concise objectives

Commit [a5d43b9](https://github.com/weiliang1995/thesis/commit/a5d43b953ab19957ebae91dd9dccd018c6b586fb), chapters/01-introduction/1.3-research-objectives.md.

Before:
> To evaluate the delivery efficiency of structured agent orchestration compared with conventional prompt-based AI-assisted development, using delivery lead time as the primary measure.

After:
> To compare the delivery efficiency of the two workflows based on delivery lead time.

Observation: the already-defined workflows do not need to be restated in every objective. Preserve metric specificity and verify against current research objectives.

## Detailed but direct sentence

Commit [e79cd32](https://github.com/weiliang1995/thesis/commit/e79cd3208eda0cdac4ae3c141e9d0a3b6841f428), chapters/01-introduction/1.5.1-technical-and-architectural-scope.md.

> In daily front-end development, a feature change requires adjustments to business logic, page state, and user interface in the main repository, and may also involve shared components, type definitions, or utility functions in the component library.

Observation: a longer sentence can be clear when its length comes from relevant technical detail rather than nested clauses.

## Source manifest

| Commit | Role |
| --- | --- |
| [e79cd32](https://github.com/weiliang1995/thesis/commit/e79cd3208eda0cdac4ae3c141e9d0a3b6841f428) | Imported original Proposal |
| [bf36a24](https://github.com/weiliang1995/thesis/commit/bf36a247c7bfc83b58ea7d0f7365f405232d7465) | Introduction review |
| [879aaec](https://github.com/weiliang1995/thesis/commit/879aaecd7cf7fabb4eefe57b43f9513906bff461) | Research background and agentic AI revision |
| [84d6ca3](https://github.com/weiliang1995/thesis/commit/84d6ca315764061ed1ca88662bf01b0d86ddc5ad) | Chapter 1 technical concepts |
| [292e342](https://github.com/weiliang1995/thesis/commit/292e34254ff7b852c41c4e0d23392cf99dc2204c) | Problem statement revision |
| [a5d43b9](https://github.com/weiliang1995/thesis/commit/a5d43b953ab19957ebae91dd9dccd018c6b586fb) | Objectives and questions |
| [cc020fc](https://github.com/weiliang1995/thesis/commit/cc020fcb5bf19f128d81393fa25cc37496d38021) | Scope and limitations |

Selected commits only; not an exhaustive history review. Original text remains available at the pinned commits.

## Conversation calibration — 2026-11-27

The three exercises below record AI drafts, author-edited versions, and qualitative observations. They are distinct from the Git corpus. Retained AI language indicates acceptance only; none is a verified independent writing sample.

| Sample | Focus | Observation |
| --- | --- | --- |
| [01 Context engineering](calibration/01-context-engineering.md) | Concept introduction | Direct definition and consolidated explanation; some semantic changes require verification |
| [02 RAG](calibration/02-rag.md) | Technical mechanism | Most mechanism wording retained; technical correction needed in the revised definition |
| [03 Literature review](calibration/03-literature-review.md) | Findings and limitations | Almost all original prose retained; claims still require source verification |

These observations support proportionate, author-led editing. They are not evidence of detector performance or human-only authorship.

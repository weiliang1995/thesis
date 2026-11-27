# Calibration 02 — Retrieval-Augmented Generation

Source: author–ChatGPT calibration conversation, 2026-11-27. Exercise, not thesis text. AI draft followed by author revision as submitted; not independent writing. Original spelling and punctuation retained.

## AI draft

Retrieval-Augmented Generation (RAG) enables large language models to access external knowledge sources during the generation process, thereby extending their capabilities beyond the information acquired during model training.

A typical RAG pipeline begins by converting the user's query into a vector representation through an embedding model. This representation is subsequently compared with the vector representations of documents stored in a vector database. Based on their similarity scores, the most relevant document segments are retrieved and incorporated into the model's input context.

Nevertheless, the effectiveness of this approach is highly dependent on the quality of the retrieved information. If relevant documents are not successfully identified during the retrieval stage, the language model may generate inaccurate or incomplete responses, even when the underlying model possesses strong reasoning capabilities.

## Author revision

RAG acts as an external knowledge source for LLM during generation process, it can extend LLM capabilities to acquire information during model training.
A typical RAG pipeline begin from converting the user's query into a vector representation through an embedding model. It is subsequently compared with the vector representations of documents stored in a vector database. Based on their similarity scores, the most relevant document segments are retrieved and incorporated into the model's input context.
Nevertheless, the effectiveness of RAG is highly depend on the quality of retrived information. If relevant documents are not successfully identified during the retrieval stage, the language model may generate inaccurate or incomplete responses, even when the underlying model possesses strong reasoning capabilities.

## Author feedback

“该说不说这段很像我会写的内容”

## Observations

- Active changes: direct role-oriented definition; pronoun substitution; explicit naming of RAG.
- Retained: most mechanism and limitation descriptions, including formal words such as subsequently, incorporated, Nevertheless and possesses.
- Technical correction needed: RAG retrieves external information at inference/generation time, not during model training. A RAG system uses a knowledge source; it is not necessarily itself the knowledge source.
- Correct agreement, spelling, article and sentence-boundary errors. Retention of an AI sentence shows acceptance, not independent authorship.

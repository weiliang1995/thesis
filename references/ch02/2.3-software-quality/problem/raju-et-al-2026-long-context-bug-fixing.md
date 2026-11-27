# The Limits of Long-Context Reasoning in Automated Bug Fixing

- Ravi Raju, Mengmeng Ji, Shubhangi Upasani, Bo Li, and Urmish Thakker
- 2026 preprint, arXiv:2602.16069, version 2. [Paper](https://arxiv.org/abs/2602.16069v2) · [Full text](https://arxiv.org/html/2602.16069v2)

## Study and findings

The study includes a separate test of single-attempt patch generation on 100 SWE-bench Verified tasks. The authors use BM25 to select code and explicitly include the files changed in the reference patch in an input of about 64,000 tokens. Their qualitative analysis identified generated patches that targeted nonexistent files or contained incorrect line numbers in diff headers.

## Role in Section 2.3

This is code-specific evidence for the distinction between supplying relevant repository files and using them successfully. The single-attempt patch setup and the agent runs differ in how models can inspect, act, and recover. The qualitative errors do not estimate how often extra context causes hallucination in a multi-step coding agent.

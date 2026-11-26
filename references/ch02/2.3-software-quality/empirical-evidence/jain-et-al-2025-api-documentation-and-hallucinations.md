# On Mitigating Code LLM Hallucinations with API Documentation

- Nihal Jain, Robert Kwiatkowski, Baishakhi Ray, Murali Krishna Ramanathan, and Varun Kumar
- ICSE Software Engineering in Practice, 2025, pp. 237–248. [DOI](https://doi.org/10.1109/ICSE-SEIP66354.2025.00027) · [Full text](https://cdn.amazon.science/8f/83/7407a5634a80a39e82b52ae935fe/on-mitigating-code-llm-hallucinations-with-api-documentation.pdf)
- Peer-reviewed empirical study. Sections II–IV and Figures 6–7 reviewed.

## Study and findings

CloudAPIBench uses AWS and Azure SDK tasks to evaluate valid API invocations. The authors include nonexistent API names, invalid syntax, and fictitious arguments among API hallucinations. They compare a base prompt with prompts augmented by API documentation and vary the documentation fields and retriever precision in controlled experiments.

With StarCoder2-3B, adding the correct API specification through an oracle retriever raised the mean valid invocation rate from 41.80% to 86.82%. On high frequency APIs, using one retrieved document at 50% retriever precision reduced the valid invocation rate from 84.39% to 67.32%. Figure 7 varies precision while holding the retrieval count fixed for this comparison. The first comparison gives the model the target documentation by design. The second tests imperfect retrieval.

## Role in Section 2.3

The experiments give direct evidence about the effect of documentation supplied in the prompt on API invocation validity under the tested conditions. They support a specific link between context relevance and API grounding in 2.3.1, and a trade-off in documentation retrieval in 2.3.2. The outcome is valid SDK invocation rate. The study does not estimate the separate frequency of fabricated names after compaction or session transitions in coding agents.

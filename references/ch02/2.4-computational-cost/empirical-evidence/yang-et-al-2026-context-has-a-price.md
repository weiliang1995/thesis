# Context Has a Price: Adding and Removing Context for LLM Coding Agents under Prefix Caching

- Authors: Zerui Yang, Miaomiao Dong, Quan Xue, Chaorui Zhang, Xuanyu Zheng, Xiyuan Wang, Haolin Ruan, Xueyan Niu, Guangcheng Song, Weixi Zhang, Wei Han, Bo Bai
- Type: arXiv preprint, 17 November 2026.
- Official source: https://arxiv.org/abs/2611.22238
- Reading status: Abstract and introductory text reviewed.
- Archive status: Source record and link only; PDF not archived.

## Evidence and limits
More than 20,000 runs on SWE-bench Verified, SWE-bench and Loc-Bench; separate cached, uncached and output tokens. In main evidence-package experiments, retrieved code reduces read/search operations 18–34% yet increases cost 33–42% when cached input costs one tenth of uncached input, with no measurable resolution improvement. Observation removal saves 19–36% without discount but increases costs 38–116% under tenth-price cache. Specific pricing scenarios; do not infer enterprise cache policy. Important counterevidence for interpreting token counts versus monetary cost.

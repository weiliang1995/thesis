## 3. Related Work

Table 3.1 and Table 3.2 show the related work reviewed in this study. These studies provide important foundations for understanding how LLM-based agents can support software engineering tasks, how context can be retrieved or retained across coding activities, and how agent effectiveness should be evaluated under resource constraints. However, most existing work is evaluated using benchmark tasks, repository-level issue resolution, or isolated code generation settings. There remains limited empirical evidence on whether a structured orchestration workflow can improve delivery efficiency, maintain software quality, and control token cost in real-world front-end development.

In the area of autonomy and orchestration, SWE-Agent and AgentCoder demonstrate that structured agent interaction can improve software engineering performance. SWE-Agent introduces an Agent-Computer Interface that allows agents to interact with repositories, tools, and execution environments more systematically. Its results show that agent orchestration can improve issue-resolution performance compared with less interactive baselines. However, its evaluation mainly focuses on benchmark-based bug fixing and repository-level patch generation, rather than delivery lead time, integration quality, or human-supervised front-end workflows. AgentCoder is useful for this study because it shows how role separation can improve feedback during code generation. The programmer, test designer, and test executor roles create a clearer loop between implementation and testing. However, I treat it mainly as evidence for agent role design, not as a complete development workflow. Its evaluation is still closer to code generation and automated testing benchmarks, while this study is concerned with front-end delivery work that also includes requirement understanding, task decomposition, API integration, code review, and staged validation.

In context and memory related studies, RepoCoder and MemGPT both show that LLM-based systems need better ways to retrieve, retain, and manage context, especially when the required information cannot fit neatly into one prompt. RepoCoder improves repository-level code completion through iterative retrieval and generation, showing that retrieving relevant repository context can improve completion quality compared with basic retrieval-augmented generation. However, its reliance on similarity-based retrieval may be less effective when relevant context is structurally important but textually dissimilar, and repeated retrieval may introduce irrelevant or polluted context. MemGPT proposes a broader memory-management architecture that separates active and external memory, allowing LLM agents to access information beyond the immediate context window. While this is valuable for long-term interaction and document retrieval, its evaluation does not directly show whether memory mechanisms improve code quality, reduce defect density, or reduce workflow-level cost in software development. These studies support the importance of context management, but they do not fully address how task-relevant context should be preserved, compressed, and reused across multiple front-end development stages.

In terms of computational resource efficiency, Agentless and SWE-Effi are especially relevant to this study. Agentless shows that a simpler multi-stage workflow can remain effective for software issue resolution while avoiding excessive autonomous agent actions and unnecessary tool calls. This suggests that more autonomy does not always produce better efficiency, especially when tasks are well-bounded. SWE-Effi further argues that software engineering agents should be evaluated not only by task success, but also by resource constraints such as token usage, execution time, and cost. Its discussion of token snowball effects and expensive failures provides strong support for including cost-

efficiency metrics in agent workflow evaluation. However, both studies are still mainly benchmark-oriented and do not examine human-in-the-loop development, front-end delivery workflows, or real production constraints such as code review, integration testing, and task complexity variation.

Overall, the reviewed studies show that agent orchestration, context management, and resource efficiency are all important for effective AI-assisted software engineering. Nevertheless, existing research has not sufficiently examined these factors together in a real enterprise front-end development environment. In particular, there is a lack of empirical comparison between conventional prompt-based AI assistance and a structured orchestration workflow across delivery efficiency, software quality, and token cost. This study addresses that gap by evaluating Trade-Harness as a structured orchestration workflow for front-end development, with attention to task complexity, delivery lead time, defect density, integration testing pass rate, token efficiency, and cost per issue.

*Table 3.1 Context, Objective, Scope, Approach, Evaluation and Performance Metrics of Related Work*

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Study</strong></th>
<th><strong>Context</strong></th>
<th><strong>Objective</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Approach</strong></th>
<th><strong>Evaluation &amp; Performance Metrics</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SWE-Agent</p>
<p>Yang et al. (2024)</p></td>
<td><p>SWE-bench (~2800 instances)</p>
<p>HumanEvalFix (164 debugging benchmark)</p></td>
<td>to introduce Agent-Computer Interface (ACI) for agent to autonomously use computers and tools to solve SE tasks</td>
<td>Automated bug fixing, repository-level code search, editing, validate and patch</td>
<td>Standardize operation by ACI, guardrails to prevent error propagation and dynamic context management</td>
<td><p>% resolved / pass@1</p>
<p>comparing between non-interactive model, shell-only interactive agent and LM+ACI</p></td>
</tr>
<tr class="even">
<td><p>AgentCoder</p>
<p>Huang et al. (2023)</p></td>
<td>HumanEval, HumanEval-ET, MBPP, MBPP-ET (Python programming problems and code generation tasks)</td>
<td>to introduce a multi-agent framework (AgentCoder) to solve ineffective feedback loops in single agent and reduce token overhead in another multi-agent framework</td>
<td>Algorithmic code generation benchmark</td>
<td><p>Multi-agent orchestration (Programmer, Test designer, Test Executor)</p>
<p>A loop of programmer generate code → test designer build test case → test executor run test → programmer fix if failed</p></td>
<td>compare effectiveness, accuracy and test coverage of single agent vs multi-agent</td>
</tr>
<tr class="odd">
<td><p>RepoCoder</p>
<p>Zhang et al. (2023)</p></td>
<td>RepoEval benchmark (14 repositories created after 2022)</td>
<td>To solve the context fragmentation in repository-level code completion</td>
<td>Line, API Invocation, Function body completion</td>
<td>Iterative retrieval-generation, retrieve the previous result to improve next iterative cycle</td>
<td><p>Repo-level RAG vs RepoCoder Iteration</p>
<p>Exact Match (EM), Edit Similarity (ES) and Pass Rate (PR)</p></td>
</tr>
<tr class="even">
<td><p>MemGPT</p>
<p>Packer et al. (2023)</p></td>
<td><p>Multi-session Chat</p>
<p>NaturalQuestions-Open + Wikipedia</p>
<p>Nested Key-Value Retrieval</p></td>
<td>To solve LLM context window limitation with virtual context and memory management</td>
<td>Agent memory and context architecture</td>
<td>Two memory layers (Main + External), Agent has autonomy to manage</td>
<td><p>Conversational agent evaluation</p>
<p>Document analysis evaluation</p>
<p>Nested KV retrieval evaluation</p></td>
</tr>
<tr class="odd">
<td><p>Agentless</p>
<p>Xia et al. (2024)</p></td>
<td>SWE-Bench Lite (300 GitHub Issue)</td>
<td>To propose a bug fixing workflow without excessive use of agents</td>
<td>Repository-level bug fixing / issue resolving</td>
<td>Localization (from repository tree structure to locate suspicious files) → Repair → Validate Patch</td>
<td><p>% resolved and Avg. Cost</p>
<p>Compare multi-stage vs agent-based workflow</p></td>
</tr>
<tr class="even">
<td><p>SWE-Effi</p>
<p>Fan et al. (2025)</p></td>
<td>SWE-bench-Verified (50 issue, stratified sampling)</td>
<td>To propose a SWE-Effi metrics to evaluate AI SE effectiveness under resource constraints</td>
<td>GitHub issue resolution &amp; repository-level SE tasks</td>
<td>Multi-layer evaluation framework (Core performance, resource effectiveness)</td>
<td>Resolve rate, CPU time, Token Cost</td>
</tr>
</tbody>
</table>

*Table 3.2 Key Findings, Strength, Limitation, Research Gap of Related Work*

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 22%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Study</strong></th>
<th><strong>Key Findings</strong></th>
<th><strong>Strength</strong></th>
<th><strong>Limitation</strong></th>
<th><strong>Research Gap</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SWE-Agent</p>
<p>Yang et al. (2024)</p></td>
<td>8 times better than RAG and 64% better than shell-only agent</td>
<td>reliable evidence for agent orchestration by demonstrating through rigorous real-world benchmarking</td>
<td>the resolve rate is still considered low (12.47%~18%), but 8x increase in average token cost</td>
<td>evaluation of benchmark bug fixing task success in Python repository only, not delivery efficiency or code quality</td>
</tr>
<tr class="even">
<td><p>AgentCoder</p>
<p>Huang et al. (2023)</p></td>
<td>better test case coverage and accuracy, lesser token consumption</td>
<td>Agent role separation, good multi-agent orchestration without excessive use of agents</td>
<td>Mostly benchmark-based and code/test case generate only, doesn’t cover requirement understanding, task decomposition, API integration and code review</td>
<td>lack of human-in-the-loop experiment, the developer only manages the requirement input, not supervising the agent</td>
</tr>
<tr class="odd">
<td><p>RepoCoder</p>
<p>Zhang et al. (2023)</p></td>
<td>10% + absolute improvement, iterative retrieval is better than vanilla RAG</td>
<td><p>No fine tuning, complex static analysis or heuristic rules needed</p>
<p>Addressing the pain point of AI code completion (current doc as context is not enough)</p></td>
<td>Difficult to retrieve relevant context in low similarity codebase. Multi iteration may pollute the retrieved context. EM and ES may misjudge code with same function but written differently</td>
<td>RepoCoder rely on similarity-based retrieval, while Trade-Harness aim to preserve and compress task-relevant context across workflow steps</td>
</tr>
<tr class="even">
<td><p>MemGPT</p>
<p>Packer et al. (2023)</p></td>
<td>90% accuracy in DMR, better than baseline; can search through archival storage without context window limitation; prove ability of multi-hop retrieval in multi nesting levels</td>
<td>Propose a system-level memory management architecture; cover multiple scenario (long-term chat, document QA, multi-hop retrieval)</td>
<td><p>Timing of writing to memory, retrieval and stop searching depend on prompt instruction and LLM judgements.</p>
<p>Multiple function calls and memory search may increase token usage and execution time</p></td>
<td>MemGPT evaluate the accuracy and effectiveness of memory layer architecture, but it doesn’t imply that high accuracy of context retrieval will lead to higher code quality and lesser defect density</td>
</tr>
<tr class="odd">
<td><p>Agentless</p>
<p>Xia et al. (2024)</p></td>
<td><p>Efficiency of Hierarchical localization</p>
<p>Using skeleton format can improve accuracy and reduce token cost</p></td>
<td>No complex autonomous planning, no repeat LLM tool calling</td>
<td>performance of multi-stage workflow might underperform without clear issue description</td>
<td>Introduce multi-stage workflow for simple or well-bounded tasks to reduce token cost</td>
</tr>
<tr class="even">
<td><p>SWE-Effi</p>
<p>Fan et al. (2025)</p></td>
<td><p>Performance highly depends on model</p>
<p>Strong reasoning model may reduce token usage because lesser LLM calls</p>
<p>Token snowball effect</p></td>
<td><p>Token snowball and Expensive Failures is a strong support for control token cost</p>
<p>Bring awareness of budget management and failure detection</p></td>
<td>Low sample size and benchmark that cover issue resolution only</td>
<td>lack of human-in-the-loop experiment, did not consider human correction and review effort</td>
</tr>
</tbody>
</table>

# 论文研究一致性审查

审查于 2026 年 11 月 27 日进行。快照为 `docs/thesis-terminology-review` 分支的 `6e98c32`。本报告覆盖前置页、第 1–3 章的 53 个 Markdown 文件和 3 张图。按方法章文件里的 §4.x 号定位。审查与 evidence 分开进行，两次均在同一上下文完成。

**优先确认研究样本与 RQ3 的正式指标。** Lead time 终点和两组条件已有可对齐的定义。当前稿可审查研究问题到分析计划的连线，现行论文的结果、讨论和结论属于待写材料。[词汇表](../.agents/docs/glossary.md#study-conditions) · [研究映射](../.agents/docs/research-mapping.md) · [术语报告](terminology-review.md)

## 正向追踪矩阵

共同设计为 12 周准实验。两位开发者在不同任务上使用两组工作流，技术负责人按开发者与事前估计复杂度尽量平衡任务。每个任务实施一次。Baseline 为直接使用原生 Claude Code CLI，Trade-Harness 为在完全隔离的 sandbox 内基于原生 CLI 配置的实验条件。以下各行均依赖 AL-001 的条件边界和 AL-002 的样本边界。[分组设计，§4.1.1 第 3–9 行](../chapters/ch03-research-methodology/4.1.1-quasi-experimental-design.md) · [任务分配，§4.1.2 第 5–19 行](../chapters/ch03-research-methodology/4.1.2-task-selection-classification-and-developer-assignment.md) · [词汇表](../.agents/docs/glossary.md#study-conditions)

| 问题与目标 | RQ | 文献与缺口 | 指标与数据 | 分析 | 结果、讨论、结论 | 连线状态 |
| --- | --- | --- | --- | --- | --- | --- |
| 工作流协调能否改善交付效率，对应 RO1。[§1.2.1](../chapters/ch01-introduction/1.2.1-lack-of-workflow-orchestration-in-ai-assisted-development.md) · [RO1，第 7 行](../chapters/ch01-introduction/1.3-research-objectives.md) | 两组 lead time 如何不同。[RQ1，第 5 行](../chapters/ch01-introduction/1.4-research-questions.md) | 现有研究比较交互、任务时间或吞吐。本文关注企业任务的开发阶段经过时间。[§2.2.2](../chapters/ch02-literature-review/2.2.2-existing-approaches-and-empirical-evidence.md) · [§2.2.3](../chapters/ch02-literature-review/2.2.3-research-gap-and-evaluation-rationale.md) | Jira `In Progress` 到 `Development Complete` 的经过天数。字段已在稿内说明，原始记录待核。[§4.2.1](../chapters/ch03-research-methodology/4.2.1-delivery-efficiency-metrics.md) · [§4.2.4.1](../chapters/ch03-research-methodology/4.2.4.1-native-jira-metrics.md) | 按组描述差异，并按开发者和复杂度分层。[§4.2.5，第 17–25 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md) | 待写 | RQ→方法对齐，摘要的 `QA staging` 与方法冲突。见 AL-003。 |
| 上下文连续性与软件质量，对应 RO2。[§1.2.2](../chapters/ch01-introduction/1.2.2-stateless-execution-and-deficient-memory-retention.md) · [RO2，第 9 行](../chapters/ch01-introduction/1.3-research-objectives.md) | 两组 defect density 和 E2E pass rate 如何不同。[RQ2，第 7 行](../chapters/ch01-introduction/1.4-research-questions.md) | 检索、交接和记忆研究给出机制线索。本文比较完整工作流的两个质量指标。[§2.3.2](../chapters/ch02-literature-review/2.3.2-existing-approaches-and-empirical-evidence.md) · [§2.3.3](../chapters/ch02-literature-review/2.3.3-research-gap-and-evaluation-rationale.md) | 最终 E2E 报告的通过用例数除以任务 JSON 的全部适用用例数。已确认关联缺陷除以最终生产代码变更千行数。数据来自分支关联报告、Jira 和 GitLab，原始记录待核。[§4.2.2](../chapters/ch03-research-methodology/4.2.2-code-quality-metrics.md) · [§4.2.4.1](../chapters/ch03-research-methodology/4.2.4.1-native-jira-metrics.md) · [§4.2.4.2](../chapters/ch03-research-methodology/4.2.4.2-repository-and-agentic-workflow-analytics.md) · [§4.2.4.3](../chapters/ch03-research-methodology/4.2.4.3-e2e-testing-records.md) | 保留任务级分布、分母和缺失情况。可补充报告以总缺陷和总变更行数计算的合并缺陷密度。[§4.2.5，第 7–27 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md) | 待写 | 方法链基本对齐。摘要把 E2E 指标写成 integration testing，§4.3.2 对通过率的解释偏强。见 AL-005。 |
| 编排可能改变 token 消耗和资源使用，对应 RO3。[§1.2.3](../chapters/ch01-introduction/1.2.3-computational-cost-and-inefficient-context-utilization.md) · [RO3，第 11 行](../chapters/ch01-introduction/1.3-research-objectives.md) | 两组每个 issue 的 token consumption 如何不同。[RQ3，第 9 行](../chapters/ch01-introduction/1.4-research-questions.md) | 已有研究区分 token 数量、货币费用与资源预算。本文可按 issue 比较记录用量或费用。[§2.4.1，第 33 行](../chapters/ch02-literature-review/2.4.1-sources-of-token-consumption-in-agent-assisted-development.md) · [§2.4.3，第 3–9 行](../chapters/ch02-literature-review/2.4.3-research-gap-and-evaluation-rationale.md) | Gateway 提供 input、output token 数量及 USD 费用。token 量已用于比率分母。数据关联和费用有效性待核。[§4.2.3](../chapters/ch03-research-methodology/4.2.3-computational-resource-cost-metrics.md) · [§4.2.4.4](../chapters/ch03-research-methodology/4.2.4.4-enterprise-llm-gateway-logs.md) | 主要比较列出 USD/issue。未给出独立 tokens/issue 的正式比较。[§4.2.5，第 7、23 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md) | 待写 | 矛盾。现有主要分析未直接回答以 tokens 为单位的子问题。见 AL-004。 |
| 同一 RO3，观察变更量相对于使用量。[RO3，第 11 行](../chapters/ch01-introduction/1.3-research-objectives.md) | 两组每百万 tokens 的变更行数如何不同。[RQ3，第 9 行](../chapters/ch01-introduction/1.4-research-questions.md) | 该比率描述变更量与用量，功能价值需要其他证据。[§2.4.3，第 5–7 行](../chapters/ch02-literature-review/2.4.3-research-gap-and-evaluation-rationale.md) | 最终 GitLab 生产代码 diff 的新增行数加删除行数的绝对值，除以 gateway 总 tokens 后乘一百万。[§4.2.3，第 5–15 行](../chapters/ch03-research-methodology/4.2.3-computational-resource-cost-metrics.md) | 任务级比率，按工作流和分层比较。零分母或缺失用量需单独处理。[§4.2.5，第 9–25 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md) | 待写 | RQ→方法对齐，摘要写成生成行数，§2.5 的结果指标摘要遗漏该比率。见 AL-004。 |

## 反向追踪

- **三组问题、目标和 RQ 均有对应关系。** 复杂度是横跨 RQ1–RQ3 的分层维度，依据技术负责人对实施前工作量的估计。开发者也是分层维度。安排和分析对齐，样本量及组内分布需要结果材料确认。[RO，第 7–13 行](../chapters/ch01-introduction/1.3-research-objectives.md) · [§4.1.2，第 5–19 行](../chapters/ch03-research-methodology/4.1.2-task-selection-classification-and-developer-assignment.md) · [§4.2.5，第 17–25 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md)
- **E2E 脚本修正次数具有单独用途。** 它是检查测试过程和三轮规则遵守情况的补充指标。文稿区分 Baseline 的指令约束与 Trade-Harness 的工作流控制。[§4.2.2，第 27–31 行](../chapters/ch03-research-methodology/4.2.2-code-quality-metrics.md) · [§4.2.5，第 27 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md)
- **USD/issue 是方法中的额外正式指标。** 它能对应 RO3 广义的资源比较，当前 RQ3 没有提到费用。已记录的 input/output tokens 同时为每百万 tokens 比率提供分母。[RO3](../chapters/ch01-introduction/1.3-research-objectives.md) · [RQ3](../chapters/ch01-introduction/1.4-research-questions.md) · [§4.2.3](../chapters/ch03-research-methodology/4.2.3-computational-resource-cost-metrics.md)
- **现行稿的结果链接均待写。** 结果、讨论和结论暂未在现行章节中建立。组别任务数、排除记录和结果数值尚无本次可核验的研究记录。历史结果草稿在弃用目录。研究映射目前是待填提纲。[章节地图](../.agents/docs/architecture.md#manuscript) · [研究映射](../.agents/docs/research-mapping.md) · [§4.2.5，第 15–33 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md)

## 发现与待办

### AL-001 实验条件在研究设计与执行说明中缺一项

**重大 · 已确认。** 词汇表确认了 Trade-Harness 的 sandbox。§1.5.2、§4.1.3 条件表和 §4.1.4 实施步骤省略了它，`same development environment` 也容易同时指团队场景和运行配置。条件定义不完整，会影响读者判断比较包含哪些差异。[词汇表](../.agents/docs/glossary.md#study-conditions) · [§1.5.2，第 3–9 行](../chapters/ch01-introduction/1.5.2-definition-of-the-orchestrated-workflow.md) · [§4.1.3，第 7–19、35 行](../chapters/ch03-research-methodology/4.1.3-research-variables.md) · [§4.1.4，第 7 行](../chapters/ch03-research-methodology/4.1.4-experimental-procedure.md)

- [ ] 对齐条件首次定义、条件表和执行步骤。根据研究配置区分共享工具和资源、隔离范围及实际对照条件。对应 [TA-001、TA-006](terminology-review.md#ta-001-实验条件描述缺少-sandbox)。

### AL-002 纳入标准和分析样本的对象不一致

**重大 · 已确认。** 任务筛选列出功能、修复和重构，数据准备以 `eligible feature-development task` 为单位，外部效度明确排除独立修复和重构。这会改变哪些 Jira issues 进入样本和各组的分母。[§4.1.2，第 3 行](../chapters/ch03-research-methodology/4.1.2-task-selection-classification-and-developer-assignment.md) · [§4.1.4，第 5 行](../chapters/ch03-research-methodology/4.1.4-experimental-procedure.md) · [§4.2.5，第 3–11 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md) · [§4.3.3，第 3 行](../chapters/ch03-research-methodology/4.3.3-external-validity.md)

- [ ] 确认候选池、实际分配任务、最终分析样本和分指标有效样本之间的关系。明确随功能交付的修复或重构如何归类，再同步摘要与方法。对应 [TA-004](terminology-review.md#ta-004-纳入分析的任务范围不一致)。

### AL-003 摘要的 RQ1 终点与计划分析不一致

**重大 · 已确认。** 摘要使用 `QA staging`，文献理由、Jira 字段和分析计划以 `Development Complete` 为终点并排除之后的 QA 或部署。摘要可能因此承诺一个更长的交付区间。[摘要，第 11 行](../front-matter.md) · [§2.2.3，第 5 行](../chapters/ch02-literature-review/2.2.3-research-gap-and-evaluation-rationale.md) · [§4.2.1，第 3–7 行](../chapters/ch03-research-methodology/4.2.1-delivery-efficiency-metrics.md) · [§4.2.5，第 9 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md)

- [ ] 以现有方法定义对齐摘要、RQ1 和指标名称。对应 [TA-002](terminology-review.md#ta-002-lead-time-的终点不一致)。

### AL-004 RQ3 与正式比较的结果指标不一致

**重大 · 已确认。** RQ3 问 tokens/issue，方法主要比较 USD/issue。摘要的生成行数与方法的变更生产代码行数也不一致。§2.5 列出 token cost，遗漏变更行数比率。现有计划可能给出多个资源指标，却没有直接回答一个明确写出的 RQ3 子问题。[摘要，第 11 行](../front-matter.md) · [RQ3，第 9 行](../chapters/ch01-introduction/1.4-research-questions.md) · [§2.5，第 7 行](../chapters/ch02-literature-review/2.5-literature-synthesis.md) · [§4.2.3](../chapters/ch03-research-methodology/4.2.3-computational-resource-cost-metrics.md) · [§4.2.5，第 23 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md)

- [ ] 先决定 tokens/issue 和 USD/issue 各自是否作为正式比较。在统一的指标清单中明确每项的单位、分母和正式或补充用途，然后同步标题、摘要、RO3、RQ3、§2.5 和分析计划。对应 [TA-003](terminology-review.md#ta-003-rq3-的计量单位与主要分析不一致)。

### AL-005 RQ2 的摘要指标与解释超出实际观测

**重大 · 已确认。** 摘要描述 integration testing pass rate，方法使用生成脚本的最终 E2E 报告。§4.3.2 的 `shows whether an implementation satisfies` 也容易把报告记录等同于用例要求全部被准确执行。§2.3.3 已说明生成脚本的覆盖和正确性会限制解释。[摘要，第 11 行](../front-matter.md) · [§2.3.3，第 5–9 行](../chapters/ch02-literature-review/2.3.3-research-gap-and-evaluation-rationale.md) · [§4.2.2，第 5–23 行](../chapters/ch03-research-methodology/4.2.2-code-quality-metrics.md) · [§4.3.2，第 3 行](../chapters/ch03-research-methodology/4.3.2-construct-validity.md)

- [ ] 统一采用最终 E2E 用例通过率，解释限于最终报告中的适用用例记录。以关联缺陷密度补充解释，保留标题所承诺的质量维度与实际测量范围的对应。关联 [TA-005](terminology-review.md#ta-005-质量指标名称与方法定义不一致) 与 [CE-004](evidence-review.md#ce-004-e2e-报告与满足需求之间还隔着脚本有效性)。

### AL-006 研究进度在摘要与方法章中使用了不同状态

**重大 · 文字差异已确认，实际进度待核。** 摘要说研究 `will be conducted`，实验流程说实验 `was embedded` 且任务 `was completed`。当前仓库无现行结果章，无法单凭行文确认数据是否已经收集和锁定。[摘要，第 11 行](../front-matter.md) · [§4.1.4，第 3–10 行](../chapters/ch03-research-methodology/4.1.4-experimental-procedure.md) · [章节地图](../.agents/docs/architecture.md#manuscript)

- [ ] 根据实际研究阶段统一摘要、方法和预期或已观察结果的时态。保留计划规则和观测执行情况的可追溯关系。

### AL-007 两位开发者的选择与研究者角色仍需说明

**重大 · 文稿缺项已确认，实际角色待核。** §4.1.2 交代两位开发者的经验与技术负责人的分配职责，§4.3.1 说明样本和参与者预期的局限。方法尚未明确为何选择这两位，以及研究者是否参与条件分配、执行、缺陷确认或数据整理。这对应项目中的评审反馈。[§4.1.2，第 17–19 行](../chapters/ch03-research-methodology/4.1.2-task-selection-classification-and-developer-assignment.md) · [§4.3.1，第 3–9 行](../chapters/ch03-research-methodology/4.3.1-internal-validity.md) · [评审反馈，第 5–6 行](assessor-feedback.md)

- [ ] 按实际职责补充样本选择依据、相关角色与偏差控制，随后在结果中交代每位开发者与各组、各复杂度的有效任务数。

## 建议处理顺序

1. 用 `research-grill` 确认实验运行配置、纳入样本、RQ3 正式指标和研究执行状态。
2. 按现有方法统一 lead time 与 E2E 指标，补齐方法中已确认的两组定义。用 `research-terminology` 维护对应的正式名称。
3. 有结果资料后沿矩阵反查三条 RQ。为每个指标报告可用任务数、缺失和排除情况，并按任务复杂度和开发者解释观察到的差异。方法章目前对非随机、两位开发者设计的归因限制有明确说明。[§4.2.5，第 25–33 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md) · [§4.3.4，第 3–9 行](../chapters/ch03-research-methodology/4.3.4-conclusion-validity.md)

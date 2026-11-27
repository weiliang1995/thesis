# 论文术语审查报告

审查日期为 2026 年 11 月 27 日。审查快照为 `docs/thesis-terminology-review` 分支的 `6e98c32`，该提交来自审查时远程最新的 `main`。

## 范围与依据

- 在同一上下文中执行 `thesis-review terminology`，覆盖前置页和第 1–3 章共 53 个 Markdown 文件，以及第 2 章 3 张图中的术语。历史提案与已弃用草稿不在本次范围内。
- 以词汇表中已确认的 Baseline 和 Trade-Harness 定义为准，并对照正文的研究问题、指标定义、数据来源和分析口径。方法章目录为第 3 章，以下小节号沿用文件中的 §4.x 标题。[审查规范](../.agents/docs/thesis.md#review-requirements) · [词汇表](../.agents/docs/glossary.md#study-conditions) · [章节地图](../.agents/docs/architecture.md#manuscript)
- 本次核对了正文中 `prompt engineering`、`context engineering`、`harness engineering` 及 agent/workflow 的用法。对 Anthropic、arXiv 和 LangChain 原始页面的访问返回 HTTP 403，外部定义和来源仍待核验。

## 审查发现

### TA-001 实验条件描述缺少 sandbox

**重大 · 已确认。** Baseline 的定义是开发者直接使用原生 Claude Code CLI。Trade-Harness 的定义是在 `fully isolated sandbox` 中使用基于原生 Claude Code CLI 配置的 Trade-Harness。§1.5.2 和 §4.1.3 在描述两组条件时省略了 sandbox。§1.5.2 和 §4.1.1 的 `same development environment` 也可能让读者理解为两组运行配置相同。[词汇表](../.agents/docs/glossary.md#study-conditions) · [§1.5.2，第 3–9 行](../chapters/ch01-introduction/1.5.2-definition-of-the-orchestrated-workflow.md) · [§4.1.1，第 3 行](../chapters/ch03-research-methodology/4.1.1-quasi-experimental-design.md) · [§4.1.3，第 5–19 行](../chapters/ch03-research-methodology/4.1.3-research-variables.md)

- [ ] 在正文首次完整介绍两组条件时同步已确认的定义。分别说明两组共享的开发场景、CLI 和模型，以及 Trade-Harness 条件的隔离要求。具体配置见 TA-006。

### TA-002 Lead time 的终点不一致

**重大 · 已确认。** 摘要将 `QA staging` 写为终点，§2.2.3 和 §4.2.1 将终点定义为 Jira 的 `Development Complete`，并排除该状态之后的 QA 与部署。两种写法会让读者理解为不同的测量时段。[摘要，第 11 行](../front-matter.md) · [§2.2.3，第 5 行](../chapters/ch02-literature-review/2.2.3-research-gap-and-evaluation-rationale.md) · [§4.2.1，第 3–7 行](../chapters/ch03-research-methodology/4.2.1-delivery-efficiency-metrics.md)

- [ ] 按现有方法统一用 `development lead time` 表示从 `In Progress` 到 `Development Complete` 的经过时间。将 `delivery efficiency` 用作研究维度，统一摘要、RQ1、文献综述与方法中的指标名称和终点。

### TA-003 RQ3 的计量单位与主要分析不一致

**重大 · 已确认。** RQ3 写 `token consumption per issue`，§4.2.5 的主要分析写 `LLM token cost per resolved issue`。前者以 tokens 计量，后者以 USD 计量。摘要还将另一项指标写为 `lines of code generated per million tokens`。方法使用最终生产代码 diff 中新增行数加删除行数的绝对值，再按已记录的 input 和 output tokens 合计计算比率。[摘要，第 11 行](../front-matter.md) · [RQ3，第 9 行](../chapters/ch01-introduction/1.4-research-questions.md) · [§2.4.3，第 5–9 行](../chapters/ch02-literature-review/2.4.3-research-gap-and-evaluation-rationale.md) · [§4.2.3，第 5–27 行](../chapters/ch03-research-methodology/4.2.3-computational-resource-cost-metrics.md) · [§4.2.5，第 23 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md)

- [ ] 确认 tokens per issue 是正式结果指标还是补充描述指标，再同步 RO3、RQ3、文献综述、方法和摘要。采用 `changed production LOC per million tokens` 描述基于最终 diff 的指标，并保留 token 数量和 USD 费用各自的单位。

### TA-004 纳入分析的任务范围不一致

**重大 · 已确认。** 摘要、§4.1.2 和实验流程将 bug fixes 与 refactoring 列入研究所述任务或筛选范围。§4.2.5 使用 `eligible feature-development task` 界定分析单位，§4.3.3 明确将独立 bug fixes 和 refactoring 排除在结果所代表的范围之外。不同写法会影响读者对纳入样本的理解。[摘要，第 11 行](../front-matter.md) · [§4.1.2，第 3 行](../chapters/ch03-research-methodology/4.1.2-task-selection-classification-and-developer-assignment.md) · [§4.1.4，第 5 行](../chapters/ch03-research-methodology/4.1.4-experimental-procedure.md) · [§4.2.5，第 3 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md) · [§4.3.3，第 3 行](../chapters/ch03-research-methodology/4.3.3-external-validity.md)

- [ ] 确认团队的候选任务范围、最终纳入分析的任务类型，以及随新功能一并完成的修复或重构如何归类。确定后统一摘要、筛选标准、实验流程和有效性说明。

### TA-005 质量指标名称与方法定义不一致

**重大 · 已确认。** 摘要使用 `integration testing pass rate`，RQ2 使用 `E2E testing pass rate`，方法定义的是 `final end-to-end (E2E) test pass rate`。指标按任务计算，以任务 JSON 中全部适用用例为分母，以最终报告中通过的适用用例为分子。另外，标题使用 `Code Quality`，正文研究维度多用 `software quality`。[标题与摘要，第 3、11 行](../front-matter.md) · [RQ2，第 7 行](../chapters/ch01-introduction/1.4-research-questions.md) · [§4.2.2，第 3–13 行](../chapters/ch03-research-methodology/4.2.2-code-quality-metrics.md) · [§4.3.2，第 3 行](../chapters/ch03-research-methodology/4.3.2-construct-validity.md)

- [ ] 统一指标全称为 `final end-to-end (E2E) test pass rate`，保留最终报告与适用用例的口径。核对标题和正文研究维度采用的质量术语。

### TA-006 Sandbox 的技术边界待补

**重大 · 操作定义待补。** 词汇表已确认 `fully isolated sandbox`。方法的条件比较表和实施步骤尚未说明隔离对象、仍共享的资源，以及 Baseline 的运行配置。这些信息关系到实验条件能否复现。[词汇表](../.agents/docs/glossary.md#trade-harness-experimental-condition) · [条件比较表，§4.1.3 第 9–19 行](../chapters/ch03-research-methodology/4.1.3-research-variables.md) · [实施步骤，§4.1.4 第 7 行](../chapters/ch03-research-methodology/4.1.4-experimental-procedure.md)

- [ ] 按 TA-001 补入已确认的条件定义，并根据研究实际使用的配置确认技术细节。把可复现的配置说明写进方法章。

### TA-007 研究条件的名称和大小写

**轻微 · 已确认。** §1.3 将 `Trade-Harness` 写成 `Trade-harness`。正文还使用 `conventional prompt-based workflow` 和 `intervention` 描述本研究条件。[§1.3，第 3 行](../chapters/ch01-introduction/1.3-research-objectives.md) · [§4.1.3，第 7–11 行](../chapters/ch03-research-methodology/4.1.3-research-variables.md) · [词汇表](../.agents/docs/glossary.md#study-conditions)

- [ ] 将研究分组名称统一为 `Baseline` 和 `Trade-Harness`。在说明工作方式时可用 `conventional prompt-based workflow` 描述 Baseline。引用其他研究时保留其各自的 baseline 含义。

### TA-008 Agent、harness、workflow 和研究条件的指称

**轻微 · 用法可能含糊。** §2.1.4 说明 Claude Code 已有原生 harness，并用六层结构介绍 Trade-Harness。§1.1.3 则使用另一组标签介绍通用编排机制。读者可能难以看出何处在描述一般概念，何处在描述本研究的具体实现。[§1.1.3，第 3–18 行](../chapters/ch01-introduction/1.1.3-trade-harness-as-an-agent-orchestration-workflow.md) · [§2.1.4，第 5、23–37 行](../chapters/ch02-literature-review/2.1.4-harness-engineering.md)

- [ ] 用 `Claude Code CLI` 指底层工具，用 `Trade-Harness` 指本项目配置或相应实验条件，用 `structured agent orchestration workflow` 指工作组织方式。在通用机制与 Trade-Harness 六层结构之间增加交叉引用。

## 术语表候选

下列术语在方法定义、数据来源和分析中的核心用法一致，可用 `research-terminology` 逐项确认后加入[项目词汇表](../.agents/docs/glossary.md)。

| 术语 | 正文口径与出处 |
| --- | --- |
| Defect density | 每千行变更生产代码对应的已确认关联缺陷数。按任务计算，分析中也可报告单独标明的分组合并值。[指标定义，§4.2.2 第 15–25 行](../chapters/ch03-research-methodology/4.2.2-code-quality-metrics.md) · [分析，§4.2.5 第 19 行](../chapters/ch03-research-methodology/4.2.5-data-preparation-and-analysis.md) |
| Changed LOC | 任务最终生产代码 diff 的新增行数加删除行数的绝对值。统计范围排除测试代码和生成文件。[指标定义，§4.2.2 第 17–23 行](../chapters/ch03-research-methodology/4.2.2-code-quality-metrics.md) · [GitLab 记录，§4.2.4.2 第 3 行](../chapters/ch03-research-methodology/4.2.4.2-repository-and-agentic-workflow-analytics.md) |
| E2E test-script correction loop | E2E 运行失败后，诊断生成的测试脚本错误、修改脚本并重新运行，计为一次。首次运行和业务代码修复属于其他步骤。[指标定义，§4.2.2 第 27–31 行](../chapters/ch03-research-methodology/4.2.2-code-quality-metrics.md) · [测试记录，§4.2.4.3 第 5 行](../chapters/ch03-research-methodology/4.2.4.3-e2e-testing-records.md) |
| Task complexity | 技术负责人在实施前按估计开发工作量分组。Simple 为不超过 1 个工作日，Medium 为超过 1 至 4 个工作日，Complex 为超过 4 个工作日。[任务分类，§4.1.2 第 5–15 行](../chapters/ch03-research-methodology/4.1.2-task-selection-classification-and-developer-assignment.md) |

## 修改顺序建议

1. **对齐已确认的用语和方法。** 同步实验条件的现有定义，统一 lead time、E2E 指标名称和 Trade-Harness 大小写。对应 TA-001、TA-002、TA-005 和 TA-007。
2. **确认研究口径。** 用 `research-grill` 确认 RQ3 的正式指标、任务纳入边界和 sandbox 的实际配置。对应 TA-003、TA-004 和 TA-006。
3. **维护词汇表。** 用 `research-terminology` 确认术语定义及适用范围，再按批准的口径同步各章。核验 TA-008 涉及的外部概念时回到原始来源。

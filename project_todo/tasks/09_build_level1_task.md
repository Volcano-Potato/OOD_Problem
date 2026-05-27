# Task 09: 构造 Level 1 Agent Task

## 目标

构造 rich background-only 任务，作为 lower bound，用于观察 Agent 在没有完整 Data Card 和 threat hints 时，能否从足够具体的业务/经济学问题描述中提出合理研究设计。

Level 1 不能只是两段泛泛背景。它应该借鉴 `zanbia.md` 的优点：把研究背景、决策场景、研究对象、机制直觉、具体研究问题、可用信息边界和输出要求写清楚。但 Level 1 仍然不提供完整变量表、完整数据阶段、assignment details 或识别威胁清单。

## 输入

- `gold_reference.md`
- `source_facts.md`

## 需要做什么

1. 写匿名化背景。
2. 写研究场景：谁在做什么决策、在什么业务/制度环境下、为什么这个问题重要。
3. 写研究目标和 3-5 个具体研究问题。
4. 删除题名、作者、机构、具体地点、精确年份、精确样本量。
5. 写机制直觉：至少列出 2-4 条可能路径或替代解释。
6. 写可用信息边界：宽泛说明可能有行政记录、交易数据、调查、平台日志或实施记录，但不写完整 Data Card。
7. 不提供完整变量表、assignment details 和识别威胁提示。
8. 加入 task rule：要求 Agent 基于给定背景和材料做研究设计规划，不要把 prompt 写成检索禁令。

## 怎么构造

Level 1 可以让强模型或 Codex 生成初稿，但不能让它自由发挥。输入只能给：

- `source_facts.md` 中的 research context、research question、broad setting。
- `source_facts.md` 中安全的机制背景和宽泛 outcome 类型。
- `gold_reference.md` 中的 core research problem 和 target estimand 的高层表述，但不要给 linchpin detail、original identification logic、invalid designs。

生成初稿后，人工要做删改。重点不是文笔，而是信息边界。

## 从 zanbia.md 借鉴的结构

Level 1 应包含这些模块：

- `Research Background`：研究问题的现实业务/社会背景，为什么值得研究。
- `Research Setting`：匿名制度或业务环境，关键参与者，基本决策顺序。
- `Research Objective`：主研究问题。
- `Specific Questions To Answer`：3-5 个具体问题，让 Agent 不会只写开放脑暴。
- `Mechanism Intuition`：2-4 条可能机制或替代解释。
- `Available Information`：宽泛数据来源或记录类型，但不提供完整变量表。
- `Information Not Provided`：明确缺失原论文、样本量、地点、完整变量、精确 assignment protocol。
- `Known Constraints`：必须区分 descriptive/causal/mechanism claims，并明确哪些结论无法由当前材料支持。
- `Required Output`：更细的统一输出合同，包括 mechanisms、measurement issues、attrition/compliance、failure modes、claim-evidence table。

## 研究内容描述应包含

- 现实业务/社会问题：为什么这个问题值得研究。
- 研究对象：消费者、企业、门店、家庭、地区、学生等，用匿名泛化表达。
- 行为机制直觉：可能涉及价格、信息、激励、社会压力、注意力、选择等。
- 研究目标：X 是否/如何/在多大程度上影响 Y，以及至少一个机制或解释问题。
- 具体研究问题：主效应、机制、选择/测量/时点问题、政策或管理含义。
- 基本约束：不能随意增加新实验；如果材料不足，必须明确承认不足，而不是补造 case-specific 事实。

## 研究内容描述不应包含

- 原论文题名、作者、机构、具体地点、精确年份、精确样本量。
- 原论文中特别可搜索的独特措辞。
- 原论文的具体识别策略名称。
- linchpin solution，例如“设计一个 opt-out flyer”“使用 ghost ads”“二次随机 contract rate”。
- 完整变量表、assignment level、威胁清单。
- 可以唯一反推出原论文的特殊项目、产品、平台、政策名称或独特执行细节。

## 建议模板

```markdown
# Anonymous Research Design Task: Level 1

## Task Rule
Use the information provided below to design a rigorous empirical strategy.
If credible causal identification is not possible, say so directly.

## Research Background
[匿名化背景：业务场景 + 现实决策 + 为什么有研究价值]

## Research Setting
[参与者 + 决策顺序 + 制度/业务环境，保持匿名]

## Research Objective
[研究问题：whether/how/to what extent X affects Y]

## Specific Questions To Answer
1. [主效应问题]
2. [机制问题]
3. [选择/测量/时点/解释问题]
4. [政策或管理含义]

## Mechanism Intuition
- [路径 A]
- [路径 B]
- [替代解释]

## Available Information
[宽泛说明可用数据类型，不提供完整 Data Card]

## Information Not Provided
[明确缺少完整变量表、精确地点、样本量、原论文身份等]

## Required Output
[引用统一输出合同]
```

## 产出

- `agent_task_level1.md`

## 完成记录

Pilot set 已完成：

- `benchmark/cases/C001_charitable_giving/agent_task_level1.md`
- `benchmark/cases/C002_consumer_credit/agent_task_level1.md`
- `benchmark/cases/C005_online_ad_measurement/agent_task_level1.md`
- `benchmark/cases/C008_retail_tax_salience/agent_task_level1.md`
- `benchmark/cases/C014_corruption_monitoring/agent_task_level1.md`

本轮最初只构造 Level 1 agent-facing 背景任务；未构造 Level 2/3、perturbed、no-solution，也未运行 OpenClaw。

后续模板修订：已根据 `zanbia.md` 的高信息量任务包结构，扩展 Level 1 模板。现有 pilot task 如需完全匹配新标准，应重新生成或增补 `Research Setting`、`Specific Questions To Answer`、`Mechanism Intuition`、`Available Information`、`Information Not Provided` 等模块。

主集扩展：`benchmark/cases/C004_paid_search_effectiveness/agent_task_level1.md` 已按相同 rich Level 1 标准完成。

主集扩展：`benchmark/cases/C010_fertilizer_present_bias/agent_task_level1.md` 已按相同 rich Level 1 标准完成。

主集扩展：`benchmark/cases/C016_hiv_risk_information/agent_task_level1.md` 已按相同 rich Level 1 标准完成。

主集扩展：`benchmark/cases/C019_in_store_travel_distance/agent_task_level1.md` 已按相同 rich Level 1 标准完成。

主集扩展：`benchmark/cases/C020_price_ending_field_experiment/agent_task_level1.md` 已按相同 rich Level 1 标准完成。

## 验收标准

- [x] Agent 能理解研究问题大意。
- [x] 不足以唯一推出原论文识别策略。
- [x] 不包含 linchpin solution。
- [x] 不包含可直接搜索到原论文的独特短语。
- [x] 输出要求和后续 Level 2/3 保持一致，便于比较信息梯度。
- [x] 模板已扩展为 rich background-only，而不是过短背景描述。

## 常见风险

- Level 1 太空，变成无意义开放脑暴。
- Level 1 泄漏原论文独特场景。
- 不小心把原论文方法写进背景。
- 为了“丰富”而泄漏 assignment protocol 或 linchpin solution。

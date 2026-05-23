# Task 09: 构造 Level 1 Agent Task

## 目标

构造背景-only 任务，作为 lower bound，用于观察 Agent 在信息较少时的默认研究设计倾向。

## 输入

- `gold_reference.md`
- `source_facts.md`

## 需要做什么

1. 写匿名化背景。
2. 写研究目标。
3. 写基本业务或制度场景。
4. 删除题名、作者、机构、具体地点、精确年份、精确样本量。
5. 不提供完整变量表和识别威胁提示。
6. 加入 task rule：不能搜索、不能识别原论文、只能用给定材料。

## 怎么构造

Level 1 可以让强模型或 Codex 生成初稿，但不能让它自由发挥。输入只能给：

- `source_facts.md` 中的 research context、research question、broad setting。
- `gold_reference.md` 中的 core research problem，但不要给 linchpin detail、original identification logic、invalid designs。

生成初稿后，人工要做删改。重点不是文笔，而是信息边界。

### 研究内容描述应包含

- 现实业务/社会问题：为什么这个问题值得研究。
- 研究对象：消费者、企业、门店、家庭、地区、学生等，用匿名泛化表达。
- 行为机制直觉：可能涉及价格、信息、激励、社会压力、注意力、选择等。
- 研究目标：X 是否/如何/在多大程度上影响 Y。
- 基本约束：不能随意增加新实验、不能使用外部文献、只能基于给定材料。

### 研究内容描述不应包含

- 原论文题名、作者、机构、具体地点、精确年份、精确样本量。
- 原论文中特别可搜索的独特措辞。
- 原论文的具体识别策略名称。
- linchpin solution，例如“设计一个 opt-out flyer”“使用 ghost ads”“二次随机 contract rate”。
- 完整变量表、assignment level、威胁清单。

## 建议模板

```markdown
# Anonymous Research Design Task: Level 1

## Task Rule
You must not search the web, infer the original paper, or use external literature.
Use only the information provided below.
If credible causal identification is not possible, say so directly.

## Research Background
[匿名化背景：业务场景 + 行为机制 + 为什么有研究价值]

## Research Objective
[研究问题：whether/how/to what extent X affects Y]

## Operational Context
[宽泛制度或业务环境，但不提供完整数据卡]

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

本轮只构造 Level 1 agent-facing 背景任务；未构造 Level 2/3、perturbed、no-solution，也未运行 OpenClaw。

## 验收标准

- [x] Agent 能理解研究问题大意。
- [x] 不足以唯一推出原论文识别策略。
- [x] 不包含 linchpin solution。
- [x] 不包含可直接搜索到原论文的独特短语。
- [x] 输出要求和后续 Level 2/3 保持一致，便于比较信息梯度。

## 常见风险

- Level 1 太空，变成无意义开放脑暴。
- Level 1 泄漏原论文独特场景。
- 不小心把原论文方法写进背景。

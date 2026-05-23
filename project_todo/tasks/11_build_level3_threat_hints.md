# Task 11: 构造 Level 3 Threat-Hint Task

## 目标

在 Level 2 基础上加入潜在威胁提示，测试 Agent 能否把风险提示转化为有效设计，而不是只复述风险。

## 输入

- `agent_task_level2.md`
- `gold_reference.md`

## 需要做什么

1. 复制 Level 2 的核心信息。
2. 增加 Potential Threats 模块。
3. 包含 selection/endogeneity、measurement error、spillover/interference、attrition/compliance、timing/anticipation 等风险。
4. 威胁要写成“研究者担心什么”，不要写“应该如何解决”。
5. 要求 Agent 说明设计如何处理每个威胁。

## 怎么构造

Level 3 的关键是“给威胁，不给答案”。可以由强模型/Codex 从 `gold_reference.md` 的 must-have conditions、common invalid designs 和 source facts 中生成 threat hints，但必须人工改写成问题形式。

### Threat hint 的写法

好的写法：

- Researchers are concerned that units exposed to the intervention may differ systematically from unexposed units before the intervention.
- Some outcomes are self-reported and may be affected by social desirability.
- There may be spillovers because treated and untreated units interact in the same local market.
- The timing of adoption may be related to prior trends in the outcome.

不好的写法：

- Use difference-in-differences with unit and time fixed effects.
- Add an opt-out treatment arm to identify social pressure.
- Use ghost ads to solve endogenous exposure.
- Randomize contract rates after acceptance to separate adverse selection from moral hazard.

### Threat categories

至少从下面选择 3-5 个真实相关威胁：

- Selection / endogenous exposure
- Reverse causality
- Non-parallel trends / timing endogeneity
- Measurement error / self-report bias / manipulable outcome
- Spillover / interference
- Attrition / missingness
- Non-compliance / partial take-up
- Anticipation / pre-treatment behavior change
- Mechanism confounding

## 建议模板

```markdown
# Anonymous Research Design Task: Level 3

## Task Rule
[同 Level 2]

## Research Background

## Research Objective

## Data Card
[同 Level 2]

## Potential Threats
- [Threat 1 stated as concern, not solution]
- [Threat 2]
- [Threat 3]

## Required Output
In addition to the standard output, explicitly explain how your design addresses each listed threat. If a threat cannot be addressed with the available data, say so.
```

## 产出

- `agent_task_level3.md`

## 完成记录

Pilot set 已完成：

- `benchmark/cases/C001_charitable_giving/agent_task_level3.md`
- `benchmark/cases/C002_consumer_credit/agent_task_level3.md`
- `benchmark/cases/C005_online_ad_measurement/agent_task_level3.md`
- `benchmark/cases/C008_retail_tax_salience/agent_task_level3.md`
- `benchmark/cases/C014_corruption_monitoring/agent_task_level3.md`

本轮构造的是 Level 3 threat-hint 任务包。每个文件复用 Level 2 的匿名背景、研究目标和 Data Card，并增加 6 条 case-specific threat hints。Threats 只描述研究者应担心的识别风险，例如 selection/endogenous exposure、mechanism confounding、measurement error、spillover/interference、attrition/compliance、timing/anticipation；未直接给出最终解决方案或原论文方法名称。未运行 OpenClaw。

## 验收标准

- [x] Level 3 比 Level 2 信息更充分，但没有泄漏 linchpin solution。
- [x] 每个 threat 都能对应后续评估中的一个可能错误。
- [x] 如果 Agent 仍然 overclaim，可以明确归因为不是信息不足。
- [x] 不把 robustness checks 直接写成答案。

## 常见风险

- 把“威胁提示”写成“解决方案提示”。
- 威胁列表太泛泛，例如只写“可能有内生性”。
- Level 3 信息太多，直接暴露原论文设计。

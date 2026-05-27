# Task 11: 构造 Level 3 Threat-Hint Task

## 目标

在 Level 2 基础上加入潜在威胁提示，测试 Agent 能否把风险提示转化为有效设计，而不是只复述风险。

Level 3 应该接近 `zanbia.md` 后半部分的严谨度：不仅列出威胁，还要求 Agent 把每个威胁对应到诊断、设计响应、剩余限制。注意，Level 3 仍然不能把 source paper 的最终 linchpin solution 直接写出来。

## 输入

- `agent_task_level2.md`
- `gold_reference.md`

## 需要做什么

1. 复制 Level 2 的核心信息。
2. 保留 `Data Structure Overview` 和 `Variable Groups`。
3. 增加 `Institutional Details Relevant For Identification`。
4. 增加 Potential Threats 模块。
5. 包含 selection/endogeneity、measurement error、spillover/interference、attrition/compliance、timing/anticipation、mechanism confounding、inference/clustering 等风险。
6. 威胁要写成“研究者担心什么”，不要写“应该如何解决”。
7. 增加 `Required Threat-Response Table`，要求 Agent 对每个威胁写 why it matters、diagnostic/design response、remaining limitation。
8. 要求 Agent 说明设计如何处理每个威胁；如果不能处理，必须承认。

## 怎么构造

Level 3 的关键是“给威胁，不给答案”。可以由强模型/Codex 从 `gold_reference.md` 的 must-have conditions、common invalid designs 和 source facts 中生成 threat hints，但必须人工改写成问题形式。

## 从 zanbia.md 借鉴的结构

Level 3 应包含：

- Level 2 的完整 rich task 信息。
- `Institutional Details Relevant For Identification`：谁控制 assignment/exposure、单位什么时候知道 treatment、是否能选择进入、是否有阈值/算法/排队/政策规则、outcome 谁测量、treated/untreated 是否交互。
- `Potential Threats`：具体、case-specific，不能只写“有内生性”。
- `Required Threat-Response Table`：强制 Agent 把每个风险转化为诊断或设计响应，并保留 remaining limitation。
- `Required Output`：比 Level 2 多要求 threat-response table。

## Threat hint 的写法

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

## Threat categories

至少从下面选择 5-7 个真实相关威胁：

- Selection / endogenous exposure
- Reverse causality
- Non-parallel trends / timing endogeneity
- Measurement error / self-report bias / manipulable outcome
- Spillover / interference
- Attrition / missingness
- Non-compliance / partial take-up
- Anticipation / pre-treatment behavior change
- Mechanism confounding
- Inference or clustering mismatch

## 建议模板

```markdown
# Anonymous Research Design Task: Level 3

## Task Rule
[同 Level 2]

## Research Background

## Research Setting

## Research Objective

## Specific Questions To Answer

## Causal Mechanisms To Distinguish

## Data Structure Overview
[同 Level 2]

## Data Card
[同 Level 2]

## Variable Groups
[同 Level 2]

## Institutional Details Relevant For Identification
- Who controls assignment or exposure?
- When do units learn about the treatment/exposure?
- Can units select into treatment, exposure, purchase, adoption, contact, or follow-up?
- Are there thresholds, eligibility rules, queues, rollout timing, platform algorithms, auctions, inventory constraints, or local implementation choices?
- Is there enough pre-treatment information to evaluate baseline balance or trends?
- Are outcomes measured by the treated institution, by subjects, by administrative records, or by an independent source?
- Could treated and untreated units interact?

## Potential Threats
- [Threat 1 stated as concern, not solution]
- [Threat 2]
- [Threat 3]

## Required Threat-Response Table
| Threat | Why It Matters | Proposed Diagnostic Or Design Response | Remaining Limitation |
|---|---|---|---|

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

本轮最初构造的是 Level 3 threat-hint 任务包。每个文件复用 Level 2 的匿名背景、研究目标和 Data Card，并增加 6 条 case-specific threat hints。Threats 只描述研究者应担心的识别风险，例如 selection/endogenous exposure、mechanism confounding、measurement error、spillover/interference、attrition/compliance、timing/anticipation；未直接给出最终解决方案或原论文方法名称。未运行 OpenClaw。

后续模板修订：已根据 `zanbia.md` 的结构增强 Level 3 模板。新标准要求加入 `Institutional Details Relevant For Identification` 和 `Required Threat-Response Table`。现有 pilot Level 3 task 如需完全匹配新标准，应重生成或增补这些模块。

主集扩展：`benchmark/cases/C004_paid_search_effectiveness/agent_task_level3.md` 已按相同 Level 3 threat-hint 标准完成。

主集扩展：`benchmark/cases/C010_fertilizer_present_bias/agent_task_level3.md` 已按相同 Level 3 threat-hint 标准完成。

主集扩展：`benchmark/cases/C016_hiv_risk_information/agent_task_level3.md` 已按相同 Level 3 threat-hint 标准完成。

主集扩展：`benchmark/cases/C019_in_store_travel_distance/agent_task_level3.md` 已按相同 Level 3 threat-hint 标准完成。

主集扩展：`benchmark/cases/C020_price_ending_field_experiment/agent_task_level3.md` 已按相同 Level 3 threat-hint 标准完成。

## 验收标准

- [x] Level 3 比 Level 2 信息更充分，但没有泄漏 linchpin solution。
- [x] 每个 threat 都能对应后续评估中的一个可能错误。
- [x] 如果 Agent 仍然 overclaim，可以明确归因为不是信息不足。
- [x] 不把 robustness checks 直接写成答案。
- [x] 模板已扩展为 threat-to-diagnostic 结构，而不是短 threat list。

## 常见风险

- 把“威胁提示”写成“解决方案提示”。
- 威胁列表太泛泛，例如只写“可能有内生性”。
- Level 3 信息太多，直接暴露原论文设计。
- 给了 threat-response table 但没有要求 remaining limitation，导致 Agent 过度自信。

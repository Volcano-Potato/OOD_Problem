# Task 12: 构造 Perturbed Variant

## 目标

改变一个关键识别条件，测试 Agent 是否真正理解识别假设，而不是机械复用 base task 中的方法。

Perturbed variant 不是新 case，而是在同一业务场景、相近数据结构和相同输出合同下，只改动一个关键 identification condition。这样后续错误可以明确归因到 assignment、timing、measurement、exposure、spillover、compliance 等识别条件，而不是归因到任务整体换题。

## 输入

- `agent_task_level2.md` 或 `agent_task_level3.md`
- `gold_reference.md`

## 需要做什么

1. 选择一个关键识别条件。
2. 只改变一个主要条件。
3. 保持业务场景、研究目标和大部分数据结构可比。
4. 写 rich agent-facing perturbed task。
5. 写 evaluator-only notes，说明原策略为什么变弱、失效或只能降格解释。
6. 标记 `expected bad response` 和 `expected error types`。

## 怎么构造

Perturbed variant 可以由强模型或 Codex 生成候选，但必须人工选定最终扰动。核心原则是：**只改一个识别条件**，其他背景、变量和输出合同尽量保持不变。

构造步骤：

1. 从 `gold_reference.md` 找到一个 `must-have condition` 或 `linchpin assumption`。
2. 判断它属于哪类识别条件：randomization、timing、exposure、measurement、spillover、compliance、information structure。
3. 把该条件改成更弱、更内生、或更不完整的版本。
4. 保留 agent-facing task 的 rich 结构，让 Agent 自己发现条件变化。
5. 在 evaluator-only notes 中写明强 Agent 的合理反应、弱 Agent 的常见失败、以及哪些 base gold elements 不再成立。

## 从当前 rich task 模板继承什么

Perturbed variant 不应该退回到短 prompt。它应至少包含：

- `Research Background`
- `Research Setting`
- `Research Objective`
- `Specific Questions To Answer`
- `Data Structure Overview`
- `Data Card`
- `Variable Groups`
- `Perturbed Condition`
- `Known Constraints`
- 同 base task 一致的 `Required Output` 和 `Claim-Evidence Table`

## Agent-facing 只写变化后的事实

不要写：

> Since treatment is now self-selected, DID is invalid.

应该写：

> Units can now choose whether to enter the program after seeing the offer, and enrollment is recorded in the data.

也不要写：

> The original control-group construction is no longer available.

应该写：

> The platform records campaign assignment and actual impressions, but it does not retain opportunity-side logs for untreated users.

## Evaluator-only notes 必须写

- `changed_condition_category`
- `changed_condition`
- `why_original_strategy_is_weaker_or_invalid`
- `what_a_good_agent_should_say`
- `likely_bad_agent_response`
- `expected_error_types`

## 可选扰动类型

- 随机分配变成用户自选择。
- 外生政策时点变成地区自主采纳。
- 干净 exposure-opportunity 记录变成只剩 assignment 或预测值。
- 硬 outcome 变成自报或官方上报 outcome。
- 稳定单位环境加入 spillover。
- 完整 follow-up 变成明显选择性 attrition。
- 关键 timing assumption 被打破，例如 later terms 在 take-up 前已知。

## 产出

- `agent_task_perturbed.md`
- `perturbed_variant.md`

## 完成记录

Pilot set 已完成：

- `benchmark/cases/C001_charitable_giving/agent_task_perturbed.md`
- `benchmark/cases/C001_charitable_giving/perturbed_variant.md`
- `benchmark/cases/C002_consumer_credit/agent_task_perturbed.md`
- `benchmark/cases/C002_consumer_credit/perturbed_variant.md`
- `benchmark/cases/C005_online_ad_measurement/agent_task_perturbed.md`
- `benchmark/cases/C005_online_ad_measurement/perturbed_variant.md`
- `benchmark/cases/C008_retail_tax_salience/agent_task_perturbed.md`
- `benchmark/cases/C008_retail_tax_salience/perturbed_variant.md`
- `benchmark/cases/C014_corruption_monitoring/agent_task_perturbed.md`
- `benchmark/cases/C014_corruption_monitoring/perturbed_variant.md`

本轮同时升级了 `C000_template` 下的 perturbed 模板，使其与新的 rich Level 1/2/3 模板一致，并补充了 evaluator-only note 里的 `changed_condition_category`、`why_original_strategy_is_weaker_or_invalid`、`what_a_good_agent_should_say`、`likely_bad_agent_response`、`expected_error_types`。

5 个 pilot case 的扰动设计分别是：

- `C001`：把 pre-contact interaction condition 从研究者分配改成家庭自选择。
- `C002`：把 later contract term 的 surprise/blindness assumption 改成 borrowers 在申请前已知。
- `C005`：移除 untreated users 的 exposure-opportunity logs，只保留 assignment 和 actual impressions。
- `C008`：移除 untreated comparison stores，只保留同店内 treated/untreated categories over time。
- `C014`：移除 independent outcome measurement，只剩 official project reports。

这些扰动都只改一个关键 identification condition，其他业务场景和大部分数据结构保持可比。未运行 OpenClaw。

## 验收标准

- [x] 只改变一个关键条件，便于错误归因。
- [x] 变体仍然现实，不是故意荒谬。
- [x] 好 Agent 应该降低因果 claim 强度或提出额外设计。
- [x] 坏 Agent 会可预期地套 base 模板，从而暴露 failure mode。
- [x] 变体延续 rich task 结构，而不是退回到简陋 prompt。

## 常见风险

- 一次改太多条件，无法判断 Agent 为什么失败。
- 变体变成完全无解，但没有按 no-solution 标注。
- 扰动太轻，原设计仍然成立。
- 只改 evaluator note，没有把 agent-facing task 中的相关事实真的改掉。

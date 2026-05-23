# Task 12: 构造 Perturbed Variant

## 目标

改变一个关键识别条件，测试 Agent 是否理解识别假设，而不是机械套原始任务中的方法。

## 输入

- `agent_task_level2.md` 或 `agent_task_level3.md`
- `gold_reference.md`

## 需要做什么

1. 选择一个关键识别条件。
2. 只改变一个主要条件。
3. 保持业务场景和数据结构大体可比。
4. 写 Agent-facing perturbed task。
5. 写 evaluator-only notes，说明原策略为什么变弱或失效。
6. 标记 expected bad response 和 expected error types。

## 怎么构造

Perturbed variant 可以由强模型/Codex 生成候选，但必须人工选定最终扰动。核心原则是：**只改一个识别条件**，其他背景、变量和输出合同尽量保持不变。

构造步骤：

1. 从 `gold_reference.md` 找到一个 must-have condition 或 linchpin assumption。
2. 判断它对应哪类识别条件：randomization、timing、exposure、measurement、spillover、compliance。
3. 把该条件改成更弱或更内生的版本。
4. 保留 Agent-facing task 的格式，让 Agent 自己发现条件变化。
5. 在 evaluator-only notes 中写明合理反应。

### Agent-facing 只写变化后的事实

例如不要写：

> Since treatment is now self-selected, DID is invalid.

应该写：

> Participants can choose whether to enroll in the program after seeing the offer, and enrollment is recorded in the data.

### Evaluator-only notes 必须写

- changed_condition
- why_original_strategy_is_weaker_or_invalid
- what_a_good_agent_should_say
- likely_bad_agent_response
- expected_error_types

## 可选扰动类型

- 随机分配变成用户自选择。
- 外生政策时点变成地区自主采纳。
- 干净 exposure 变成算法定向 exposure。
- 硬 outcome 变成自报 outcome。
- 稳定单位环境加入 spillover。
- 完整 follow-up 变成选择性 attrition。

## 产出

- `perturbed_variant.md`

## 验收标准

- [ ] 只改变一个关键条件，便于错误归因。
- [ ] 变体仍然现实，不是故意荒谬。
- [ ] 好 Agent 应该降低因果 claim 强度或提出额外设计。
- [ ] 坏 Agent 会可预期地套模板，从而暴露 failure mode。

## 常见风险

- 一次改太多条件，无法判断 Agent 为什么失败。
- 变体变成完全无解，但没有按 no-solution 标注。
- 扰动太轻，原设计仍然成立。

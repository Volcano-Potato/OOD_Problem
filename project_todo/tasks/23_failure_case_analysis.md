# Task 23: 做失败案例归因分析

## 目标

从统计结果中挑出最能说明系统性弱点的失败案例，写成可展示、可辩护的分析。

## 输入

- `adjudicated_labels.csv`
- raw agent logs
- gold references
- metrics summary

## 需要做什么

1. 按 severity 选出 critical failures。
2. 覆盖不同失败类型：endogenous exposure、mechanism confounding、measurement error、no-solution overclaim。
3. 对每个失败案例整理输入材料、Agent claim、cited evidence、human judgment、error type。
4. 解释为什么这是系统性弱点，而不是偶然措辞问题。
5. 写出改进建议。

## 具体执行方法

1. 从 `adjudicated_labels.csv` 过滤 severity 为 critical 或 major 的 claim。
2. 优先选择能代表不同 failure modes 的案例，不要都选同一种错误。
3. 每个失败案例必须同时展示：agent-facing evidence、Agent claim、gold reference 对照、人工判断。
4. 解释失败机制：信息不足、忽略威胁、套模板、过度声称、证据引用错位。
5. 写“更好的 Agent 应该怎么说”，用于说明问题不是任务不可做。
6. 每个失败案例最后写一个系统改进建议。

## 失败案例选择优先级

1. Perturbed 后仍机械套原设计。
2. No-solution 中仍强行声称因果。
3. 内生 exposure 被当成随机处理。
4. 机制分解 claim 没有设计支持。
5. outcome measurement 被错误当作干净证据。

## 产出

- `results/failure_cases.md`

## 推荐结构

```markdown
## Failure Case X
- Case:
- Variant:
- Agent claim:
- Cited evidence:
- Human judgment:
- Error type:
- Why it fails:
- What a better agent should have said:
- Suggested system improvement:
```

## 验收标准

- [ ] 至少 3 个失败案例。
- [ ] 每个失败案例有原始输出引用和 gold reference 对照。
- [ ] 每个失败案例都能映射到一个 failure mode。
- [ ] 至少一个案例来自 perturbed 或 no-solution variant。

## 常见风险

- 挑最搞笑的错误，而不是最有诊断价值的错误。
- 只说 Agent 错了，不解释输入证据为什么不支持。
- 没有提出系统改进建议。

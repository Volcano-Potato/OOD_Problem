# Task 08: 审计 Gold Reference

## 目标

确认 gold reference 真实、可评分、不过度依赖原论文答案，避免后续 benchmark 的答案纸本身有问题。

## 输入

- `gold_reference.md`
- `source_facts.md`
- `source_packet.md`

## 需要做什么

1. 检查每个关键 gold claim 是否有 source fact 支持。
2. 检查 linchpin detail 是否真的是识别命门。
3. 检查 must-have conditions 是否过窄。
4. 检查 acceptable alternatives 是否合理。
5. 检查 common invalid designs 是否覆盖常见 Agent 失败。
6. 标记需要人工复核的争议点。

## 具体执行方法

1. 逐条检查 `Must-Have Conditions`，每条都要能回到 source fact 或明确的 evaluator inference。
2. 对每条 acceptable alternative 问：它需要什么额外数据？它能支持多强 claim？它不能支持什么 claim？
3. 对每条 common invalid design 问：这个错误是否真实可能由 Agent 犯？是否能对应错误标签？
4. 检查 linchpin 是否太具体。如果太具体，要改写成更一般的必要识别条件。
5. 建立 issue 表，给每个问题标 severity：low / medium / high。
6. `high` 问题必须修改 gold reference；`medium` 问题至少要写解释。

## Issue 表模板

```markdown
| issue_id | section | severity | problem | required_fix | status |
|---|---|---|---|---|---|
```

## 产出

- `gold_reference_audit.md` 或写入 `audit.md` 的 gold section

## 完成范围

本轮已完成 frozen pilot set：`C001`、`C002`、`C005`、`C008`、`C014`，审计结果写入各 case 的 `audit.md`。本轮未启动单独子代理或外部模型会话；审计者记录为 `Codex separate audit pass`。如果后续要严格满足“独立模型会话”，需要再运行一次外部/子代理审计。

## 验收标准

- [x] audit decision 是 approve / revise / reject 之一。
- [x] 所有 high severity issue 必须修复后才能进入任务包生成。
- [x] 如果没有 linchpin detail，必须解释该 case 为什么仍然适合作 benchmark。
- [ ] 至少有一个独立检查者或独立模型会话完成审计。

## 常见风险

- 审计只检查格式，不检查实质。
- 把“原论文用了这个方法”误当作“唯一正确方法”。
- 忽略 task 未来是否能匿名化。

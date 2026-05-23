# Task 17: 执行 Pilot Run 并修订 Schema

## 目标

用 5 个 pilot cases 跑通完整流程，发现任务包、输出合同、日志和标注设计的问题。

## 输入

- 5 个 pilot case packages
- Agent 运行配置
- 输出合同

## 需要做什么

1. 每个 pilot case 至少跑 Level 2。
2. 记录原始输入和输出。
3. 检查 Agent 是否遵守输出格式。
4. 检查 Claim-Evidence Table 是否可用。
5. 人工快速标注每个输出 3-5 个 claim。
6. 记录 schema 问题和 prompt 问题。
7. 修订 task packet schema、输出合同或 annotation guide。

## 具体执行方法

1. 先选 1 个 case 做 smoke test，确认输出日志路径和 run manifest 正常。
2. 再跑 5 个 pilot cases，每个至少跑 Level 2；如果时间允许，加 Level 3。
3. 跑完后不要立即扩展 main set，先做 pilot review。
4. 对每个 output 检查三件事：是否遵守输出合同、是否有可抽取 claim、是否暴露任务包设计问题。
5. 建一个 `pilot_issue_table`，记录问题、原因、修复动作和是否需要重跑。
6. 如果超过 30% outputs 缺 Claim-Evidence Table，必须修改输出合同后重跑 pilot。

## pilot_issue_table 模板

```markdown
| issue_id | case_id | issue_type | problem | fix | rerun_needed |
|---|---|---|---|---|---|
```

## 产出

- `outputs/raw_agent_logs/pilot/`
- `benchmark/pilot_review.md`
- 修订后的 schema 和 prompt contract

## 验收标准

- [ ] 5 个 pilot outputs 都保存完整。
- [ ] 至少发现并处理一轮格式或任务包问题。
- [ ] 后续 main run 不需要大幅改变 schema。
- [ ] 如果 Agent 大量不遵守格式，要修订输出合同后重跑 pilot。

## 常见风险

- pilot 只看结果好不好，不检查流程是否可复现。
- 发现 task schema 问题后仍然直接扩展 main set。
- 没有保存 pilot 修订记录。

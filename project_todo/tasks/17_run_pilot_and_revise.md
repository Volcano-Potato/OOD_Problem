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
2. smoke test 与 pilot rerun 优先使用 `benchmark_isolated` + `scripts/run_isolated_packet.sh`，使 agent 只能看到外部传入的单个 task packet 文本，而不能读取本地 benchmark 文件。
3. 再跑 5 个 pilot cases，每个至少跑 Level 2；如果时间允许，加 Level 3。
4. 跑完后不要立即扩展 main set，先做 pilot review。
5. 对每个 output 检查三件事：是否遵守输出合同、是否有可抽取 claim、是否暴露任务包设计问题。
6. 建一个 `pilot_issue_table`，记录问题、原因、修复动作和是否需要重跑。
7. 如果超过 30% outputs 缺 Claim-Evidence Table，必须修改输出合同后重跑 pilot。

## 当前进展

- [x] `C001 level2` smoke test 已执行并成功落盘。
- [x] `outputs/run_manifest.csv` 和 `outputs/raw_agent_logs/pilot/` 已验证可用。
- [x] 已发现 1 条关键 issue：模型在无工具条件下仍可能把匿名任务具体化为源论文式设计细节，因此该次 run 记为 `suspected` 而非 `clean`。
- [x] 5-case Level 2 pilot batch 已执行并全部落盘。
- [x] 已完成 pilot review，确认 5/5 outputs 通过统一 20-section 输出合同并包含 `Claim-Evidence Table`。
- [x] 已完成每个 output 的 3 条 quick claim spot-check，记录到 `annotations/annotation_sheet.csv`。
- [x] 已根据 pilot review 回写 `run_manifest.csv`，5 条 pilot run 均记为 `suspected`。
- [x] 已完成一轮 schema 修订：在全部 agent-facing task packet 的 `Task Rule` 中加入 anti-reconstruction 约束。
- [x] 已配置 `benchmark_isolated` 隔离运行模式，能够在保留联网/文献检索工具的同时，阻断 agent 对本地 benchmark 文件的直接读取。
- [x] 已用 `benchmark_isolated` 成功重跑 1 条等价 smoke test（`C001 level2` 作为 isolated batch 的首条运行）。
- [x] 已用 `benchmark_isolated` 重跑 5-case Level 2 pilot batch。
- [x] 已从 trajectory 中核查 5 条 isolated rerun 的实际 tool use，结果均为 `none`。
- [x] 已确认 isolated rerun 中 `C001`、`C002` 仍存在内容问题，而 `C005`、`C008`、`C014` 明显改善。
- [x] 已对 `C001`、`C002` 做 focused verification rerun，确认问题仍集中在 packet-overreach，而非本地泄漏。

## 本轮 Smoke Test 记录

- `run_id`: `RUN_20260524_164640_openclaw_deepseekv4pro`
- `case_id`: `C001`
- `variant_id`: `level2`
- `status`: `success`
- `contamination_status`: `suspected`
- `raw_log`: `outputs/raw_agent_logs/pilot/C001_level2_openclaw_RUN_20260524_164640_openclaw_deepseekv4pro.md`

## Isolated Rerun 记录

- `C001`: `RUN_20260525_183040_openclaw_deepseekv4pro_isolated`
- `C002`: `RUN_20260525_183518_openclaw_deepseekv4pro_isolated`
- `C005`: `RUN_20260525_183846_openclaw_deepseekv4pro_isolated`
- `C008`: `RUN_20260525_184335_openclaw_deepseekv4pro_isolated`
- `C014`: `RUN_20260525_184805_openclaw_deepseekv4pro_isolated`

## Focused Verification Rerun 记录

- `C001`: `RUN_20260525_213551_openclaw_deepseekv4pro_isolated`
- `C002`: `RUN_20260525_214053_openclaw_deepseekv4pro_isolated`

本轮 focused rerun 的共同特征：

- 使用 `benchmark_isolated`
- fixed reusable out-of-repo workspace
- fresh explicit session id per run
- trajectory 审查显示 2/2 `actual tool use = none`
- `C002` 已恢复为全英文输出，但 `C001` 与 `C002` 仍都存在 packet-overreach

本轮 rerun 的共同特征：

- 使用 `benchmark_isolated`
- fixed reusable out-of-repo workspace
- fresh explicit session id per run
- trajectory 审查显示 5/5 `actual tool use = none`
- 因此，当前剩余的 packet-overreach 更应被视为 agent 行为问题，而不是本地 benchmark 文件泄漏

## 已确认的问题

```markdown
| issue_id | case_id | issue_type | problem | fix | rerun_needed |
|---|---|---|---|---|---|
| P001 | C001 | anonymization leakage risk | The model introduced specific design elements not explicitly present in the packet, suggesting source-design inference despite tools being disabled. | Tighten task-packet anonymization or add stricter anti-reconstruction wording before full pilot batch. | yes |
| P002 | C002 | packet-overreach | The model instantiated a fully specified two-stage undisclosed-term design beyond packet support. | Tighten task rule and review whether the packet reveals too much staging detail. | yes |
| P003 | C005 | packet-overreach | The model reconstructed ghost-auction instrumentation and source-like opportunity logging. | Tighten task rule and reduce hints that invite source reconstruction. | yes |
| P004 | C008 | packet-overreach | The model escalated to DiD / triple-difference claims more specifically than the packet supports. | Tighten task rule and clarify that comparison-group examples are not confirmed design facts. | yes |
| P005 | C014 | packet-overreach | The model added unsupported audit-intensity and implementation specifics. | Tighten task rule and keep monitoring packets more explicitly bounded. | yes |
| P006 | all | runtime / tooling | `semantic-scholar` MCP still creates startup-timeout noise in isolated runs (`C005`, `C008`) even when the run later completes. | Disable unstable literature MCPs for benchmark runs or separately log startup failures. | no |
| P007 | all | logging | Actual tool use can now be recovered from trajectories, but the ad hoc raw-log writer still produced noisy inline `none` summaries in some isolated logs. | Clean the log-summary extraction before the main run. | no |
| P008 | all | environment ambiguity | The first pilot batch was run before the local-file-isolated pipeline was in place, so content errors and environment leakage risk could not be fully separated. | Rerun smoke test and pilot batch with `benchmark_isolated`. | resolved |
| P009 | C002 | output-contract noncompliance | The isolated rerun returned a fully Chinese report despite the benchmark's all-English contract. | Strengthen or restate the English-only instruction in the runner prompt and contract. | yes |
```

## pilot_issue_table 模板

```markdown
| issue_id | case_id | issue_type | problem | fix | rerun_needed |
|---|---|---|---|---|---|
```

## 产出

- `outputs/raw_agent_logs/pilot/`
- `benchmark/pilot_review.md`
- 修订后的 schema 和 prompt contract
- `annotations/annotation_sheet.csv` 中的 pilot quick spot-check claims

## 验收标准

- [x] 5 个 pilot outputs 都保存完整。
- [x] 至少发现并处理一轮格式或任务包问题。
- [x] 后续 main run 不需要大幅改变 schema。
- [x] Agent 未出现大面积格式不遵守，因此无需因输出合同问题重跑 pilot。

## Isolated Rerun 结论

- `C001`: `suspected`
  - 原因：仍然把 opt-out / pre-visit implementation 写成已知事实。
- `C002`: `suspected`
  - 原因：仍然把 post-acceptance randomization 具体化，并违反全英文输出合同。
- `C005`: `clean`
  - 原因：未见旧版 ghost-auction reconstruction；无实际 tool use。
- `C008`: `clean`
  - 原因：主设计基本停留在 packet 支持范围内；triple-difference 只作为条件性 robustness extension。
- `C014`: `clean`
  - 原因：设计围绕 independent measurement 展开，未再引入旧版 unsupported audit-probability specifics。

## Focused Verification Rerun 结论

- `C001`: `suspected`
  - 原因：较上轮更克制，但仍把 explicit opt-out / easy-avoidance arm 与 doorstep baseline 写成了设计既定结构。
- `C002`: `suspected`
  - 原因：已恢复全英文合同，但仍把 hidden post-acceptance two-stage design 写成了 packet 已经支持的结构。

## 本轮结论

- 输出合同稳定，格式问题不是当前主要瓶颈。
- 当前主要问题已经进一步收缩到 `C001` 和 `C002` 的 packet-overreach，而不是环境隔离或全局 section collapse。
- 在当前状态下不应进入 `task18`。
- `benchmark_isolated` rerun 与 focused verification 已经证明环境隔离有效，下一步不应再重跑整个 5-case batch，而应先定向修 `C001` 和 `C002` 的 packet wording，再做一次聚焦验证。

## 常见风险

- pilot 只看结果好不好，不检查流程是否可复现。
- 发现 task schema 问题后仍然直接扩展 main set。
- 没有保存 pilot 修订记录。

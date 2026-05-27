# Task 18: 扩展并执行 Main Run

## 目标

在 schema 稳定后，对 10 个 main-set cases 执行正式 benchmark 运行。

## 输入

- 10 个通过审计的 main-set case packages
- 修订后的 Agent 输出合同
- run config

## 需要做什么

1. 确认每个 main case 都有 Level 2、Level 3 和至少一个 perturbed variant。
2. 确认至少有 2 个 no-solution variants。
3. 按统一 run_id 执行所有任务。
4. 保存所有原始输入和输出。
5. 记录运行失败、超时、工具错误和格式不合规。
6. 建立 run manifest。

## 具体执行方法

1. 在 main run 前冻结所有 task packets 和 run config，不要边跑边改。
2. main run 统一使用 `benchmark_isolated` 运行模式：由外部脚本读取单个 `agent_task_*.md` 文本并送入 agent，而不是让 agent 自己读取本地 benchmark 文件。
3. 优先通过 `scripts/run_batch_isolated.sh` + batch spec 执行 main run，不再人工逐条触发。
4. 按 case_id 顺序运行，避免遗漏。
5. 每次运行前检查 input_file 是否是 agent-facing 文件，不是 gold/audit 文件。
6. 每次运行后立即更新 `run_manifest.csv`。
7. 对异常输出使用状态字段标记：success、format_error、timeout、tool_error、contaminated。
8. 如果必须重跑，保留旧 run，新增 run_id，不覆盖原文件。

## 最小 main run 组合

```text
10 cases x Level 2
10 cases x Level 3
10 cases x Perturbed
2 no-solution variants
```

## 产出

- `outputs/raw_agent_logs/main/`
- `outputs/run_manifest.csv`

## 验收标准

- [ ] Main run 输出数量和 run manifest 一致。
- [ ] 每条 run 都能追溯到 case_id、variant_id、level、model、timestamp。
- [ ] 失败或异常运行有明确状态，不被静默删除。
- [ ] 没有在 main run 中临时改 prompt 或 task packet；如果必须改，要记录版本。
- [ ] main run 使用的执行方式能明确记录本地文件隔离边界、远程工具配置和实际 tool use。

## 常见风险

- 一边跑一边改任务，导致不可比。
- 只保存成功输出。
- 忘记记录模型配置，后续不可复现。
- 让 agent 在 main run 中直接读取 benchmark 仓库目录，导致本地 hidden files 泄漏风险无法排除。

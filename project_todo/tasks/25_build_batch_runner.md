# Task 25: 构建自动化 Batch Runner 与运行后处理

## 目标

把当前“单条 run 由脚本自动、批量调度靠人工触发”的半自动流程，升级成可复用的 benchmark batch runner。该 runner 应能按给定 case/variant 列表串行调用 `benchmark_isolated`，并在每条 run 完成后自动做最基本的落盘与元数据记录。

## 输入

- 已冻结的 `benchmark_isolated` 运行配置
- `scripts/run_isolated_packet.sh`
- `outputs/run_manifest.csv`
- `outputs/raw_agent_logs/log_template.md`
- `benchmark/pilot_review.md` 中已经暴露出的运行与日志痛点

## 为什么现在需要做

当前 pipeline 的问题不是“单条 run 跑不通”，而是：

1. 单条 `agent_task_*.md` 的发送已经自动化，但多条 case 的调度仍主要靠人工逐条触发。
2. raw log、trajectory、manifest 的回填仍有较多人工步骤，容易漏字段、漏 session id、漏 tool-use 审计。
3. 在 main run 阶段继续手工盯每条 run，成本太高，也会增加记录不一致的概率。

因此，在进入 `task18` 前，应先把运行 orchestration 做成一个独立、可复跑的任务。

## 需要做什么

1. 设计一个 batch spec 格式，用来声明要跑哪些 `case_id / variant_id / input_file`。
2. 写一个串行 runner，逐条调用 `scripts/run_isolated_packet.sh`。
3. 每条 run 完成后，自动解析 OpenClaw 返回 JSON，抽出：
   - `session_id`
   - `duration_ms`
   - `final output text`
   - provider/model 元信息
4. 自动把 agent 输出落成规范化 raw log。
5. 自动把 run 元数据追加到 `outputs/run_manifest.csv`。
6. 自动读取对应 `trajectory.jsonl`，抽取至少这些运行证据：
   - `actual tool use`
   - `toolMetas`
   - 是否存在 `toolCall / toolResult`
   - workspace path
7. 对失败 run 也保留 JSON、manifest 行和错误摘要，不允许静默跳过。
8. 设计 dry-run / single-run / batch-run 三种模式，便于调试和正式运行共用。

## 不需要做什么

- 不需要在这个 task 里解决 `C001 / C002` 的 packet wording 问题。
- 不需要在这个 task 里引入 claim extraction、annotation 或 metrics。
- 不需要在这个 task 里做并行运行；默认应优先保证串行、稳定、可追溯。

## 建议产物

- `scripts/run_batch_isolated.sh`
- `scripts/postprocess_openclaw_run.py` 或同等功能脚本
- `benchmark/run_configs/batch_runner_spec.md`
- `benchmark/run_configs/batch_runner_spec.example.csv`
- `outputs/raw_agent_logs/tmp_json/` 或同类中间产物目录

如果实现上更合理，也可以把 orchestrator 做成一个 Python 脚本而不是 shell 脚本，但要保持输入输出边界清晰。

## 建议输入格式

建议增加一个 batch spec，例如：

```csv
case_id,variant_id,input_file,split,enabled,notes
C001,level2,benchmark/cases/C001_charitable_giving/agent_task_level2.md,pilot,true,
C002,level2,benchmark/cases/C002_consumer_credit/agent_task_level2.md,pilot,true,
```

最小要求：

- `case_id`
- `variant_id`
- `input_file`
- `split`
- `enabled`

## 具体执行方法

1. 先定义 batch spec，不要先写大脚本。
2. 先支持最小 happy path：
   - 单条 packet
   - 成功返回
   - 自动写 raw log
   - 自动 append manifest
3. 再支持 batch 串行循环：
   - 按 spec 顺序逐条跑
   - 前一条结束后再开始下一条
   - 每条 run 使用 fresh session
4. 再补失败路径：
   - OpenClaw 退出非 0
   - JSON 不完整
   - raw output 为空
   - trajectory 缺失
   - MCP startup 噪声存在但 run 仍成功
5. 再补 postprocess：
   - 从 OpenClaw JSON 中抽正文
   - 从 `~/.openclaw/agents/benchmark_isolated/sessions/` 找到对应 `session_id`
   - 读取 `trajectory.jsonl`
   - 生成统一的 `Tool Log Summary`
6. 最后用 2 条 case 做 end-to-end 验证：
   - `C001 level2`
   - `C002 level2`

## 设计约束

1. 一次 run 仍然只能对应一个 `agent_task_*.md`。
2. runner 不得让 OpenClaw 自己去读取 benchmark case 目录。
3. runner 只能把外部读取的 packet 文本作为 message 送给 `benchmark_isolated`。
4. runner 必须记录 `benchmark_isolated` 的本地隔离语义，而不是退回旧 `benchmark` agent。
5. runner 不能因为某条 run 失败，就中断并丢失之前已完成条目的记录；需要明确失败处理策略。

## 建议日志策略

每条 run 至少保存 3 层产物：

1. OpenClaw 原始 JSON 返回
2. 规范化 raw log markdown
3. `run_manifest.csv` 一行

如果能额外保存：

4. `session_id`
5. `trajectory_path`
6. `postprocess summary json`

会更利于后续 claim extraction 和 contamination audit。

## 与现有 task 的关系

- 依赖 `task16`
  - 因为运行模式、manifest 字段、raw log 模板已经在这里冻结
- 承接 `task17`
  - 因为 pilot 阶段已经暴露出“人工串行触发 + 人工回填日志”的痛点
- 服务 `task18`
  - main run 不应继续依赖人工逐条盯 run

## 当前已知问题，需要在本 task 中解决

- `scripts/run_isolated_packet.sh` 只负责单条调用，不负责 batch orchestration。
- 当前回填 raw log 和 manifest 仍依赖人工后处理。
- `semantic-scholar` MCP 启动噪声可能污染终端输出，但不应阻止成功 run 被正确记录。
- `actual tool use` 目前要靠人工去 trajectory 里核查，应自动化抽取。

## 验收标准

- [x] 可以通过一个 batch spec 文件，自动串行运行至少 2 条 `benchmark_isolated` run。
- [x] 每条成功 run 都会自动生成规范化 raw log。
- [x] 每条成功 run 都会自动追加一行到 `outputs/run_manifest.csv`。
- [x] 每条 run 都能自动记录 `session_id` 和 `actual tool use`。
- [x] 失败 run 不会被静默跳过，至少会留下 manifest 记录和错误摘要。
- [x] runner 不会让 agent 直接读取本地 benchmark evaluator-only 文件。
- [x] 至少完成 1 次小规模 end-to-end 验证，并有明确验证记录。

## 常见风险

- 直接在 batch runner 中重新实现 packet 读取逻辑，结果和 `run_isolated_packet.sh` 行为不一致。
- 只处理成功路径，失败时既没有 JSON 也没有 manifest 记录。
- `session_id` 与 raw log 文件名脱节，后续无法追溯 trajectory。
- 把 MCP 启动噪声误判成 run 失败。
- 为了图快做并行运行，导致日志、session、manifest 相互串扰。

## 完成后应该发生什么

完成本 task 后，`task18` 的 main run 应可以从：

- 人工逐条触发

变成：

- 准备 batch spec
- 启动一次 batch runner
- 自动得到原始 JSON、raw log、manifest 和最基本的 tool-use 审计信息

这样后续 main benchmark、claim extraction 和 annotation 才有稳定输入。

## 完成记录

本轮已完成：

- 新建 `scripts/run_batch_isolated.sh`
- 新建 `scripts/postprocess_openclaw_run.py`
- 更新 `scripts/run_isolated_packet.sh`，支持外部注入 `SESSION_ID_OVERRIDE`
- 新建 `benchmark/run_configs/batch_runner_spec.md`
- 新建 `benchmark/run_configs/batch_runner_spec.example.csv`
- 新建 `outputs/raw_agent_logs/tmp_json/README.md`

本轮验证结果：

- 通过 `batch_runner_spec.example.csv` 完成了 2 条真实串行验证：
  - `RUN_20260526_103353_01_openclaw_deepseekv4pro_isolated`
  - `RUN_20260526_103939_02_openclaw_deepseekv4pro_isolated`
- 2 条 run 均自动生成：
  - 原始 JSON
  - 规范化 raw log
  - `run_manifest.csv` 记录
- 自动从 trajectory 中抽取了：
  - `session_id`
  - `toolMetas`
  - `actual tool use`
- 额外完成了 1 条 failure-path 验证：
  - `RUN_20260526_104449_01_openclaw_deepseekv4pro_isolated`
  - 输入文件缺失时，runner 正确写入 `runtime_fail`，没有静默跳过

本轮未做的事：

- 没有在本 task 中自动判定 `clean / suspected / contaminated`
- 当前后处理默认将成功 run 标记为 `contamination_status = unknown`，等待人工内容审查

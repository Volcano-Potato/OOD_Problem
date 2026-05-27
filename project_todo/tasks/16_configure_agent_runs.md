# Task 16: 配置 OpenClaw/Agent 运行与日志保存

## 目标

建立可复现的 Agent 运行设置，确保每个任务输入、输出、时间、模型和工具调用都被保存。

## 输入

- Agent 输出合同
- 已审计的 task packets
- OpenClaw / DeepScientist 运行环境

## 需要做什么

1. 确定运行模式：以 task packet 为主要证据来源，并默认使用本地隔离、远程工具开放的正式运行条件。
2. 明确记录联网搜索工具和其他工具是否开放。
3. 记录模型名称、temperature、seed 或其他采样参数。
4. 设定 run_id 命名规则。
5. 设定日志保存路径。
6. 保存原始输入 prompt 和原始 Agent 输出。
7. 如果使用 QQ/WeChat 渠道，保留交互截图和后台日志。

## 具体执行方法

1. 先写 `run_config.md`，不要先跑 Agent。
2. 明确每次运行使用的 model、temperature、max tokens、工具开关，以及单包输入规则。
3. 正式 benchmark 统一采用 `benchmark_isolated`：
   - 本地文件隔离运行
   - 外部脚本读取单个 `agent_task_*.md` 后以纯文本消息送入 agent
   - 默认允许远程 web / literature / remote MCP 工具
4. 禁止让 agent 直接读取本地 benchmark 仓库中的 evaluator-only 文件。
5. 每个 run 生成一个独立 markdown 日志，包含 input packet、system/task rule、raw output、tool log。
6. 建立 `run_manifest.csv`，每行对应一次运行。
7. 如果 Agent 输出中出现外部搜索、论文标题识别或工具调用污染，标记 `contamination_status=contaminated`，不要直接删除。

## run_manifest.csv 字段

```csv
run_id,case_id,variant_id,level,agent_name,model,model_provider,openclaw_build_or_version,temperature,top_p,max_tokens,seed,tools_enabled,closed_book,channel,timestamp,input_file,raw_output_file,status,contamination_status,contamination_reason,notes
```

## 产出

- `benchmark/run_configs/run_config.md`
- `outputs/raw_agent_logs/`

## 完成记录

本轮已完成：

- 新建 `benchmark/run_configs/run_config.md`
- 新建 `benchmark/run_configs/formal_eval_minimal_isolation.md`
- 新建 `outputs/run_manifest.csv`
- 新建 `outputs/raw_agent_logs/log_template.md`
- 新建 `outputs/raw_agent_logs/pilot/README.md`
- 新建 `outputs/raw_agent_logs/main/README.md`
- 新建 `scripts/run_isolated_packet.sh`
- 更新 `benchmark/run_configs/README.md`
- 更新 `outputs/README.md`
- 更新 `outputs/raw_agent_logs/README.md`
- 配置本地 OpenClaw `benchmark_isolated` agent

本次冻结的运行协议包括：

- 基准运行模式统一记录为 `locally_isolated_remote_tool_enabled`
- `tools_enabled` 必须记录真实设置，而不是默认假定为关闭
- 默认建议参数：`temperature = 0.2`、`top_p = 1.0`、`max_tokens = 4096`
- 当前 benchmark CLI 运行超时建议放宽到 `1200` 秒，避免把长推理误判成 runtime failure
- 对 `benchmark_isolated` 入口，默认超时已放宽到 `86400` 秒；若需更短测试，可在脚本参数中手动覆盖
- 统一 `run_id` 规则：`RUN_<YYYYMMDD>_<HHMMSS>_<agent_name>_<model_short>`
- 统一 raw log 路径：`outputs/raw_agent_logs/{split}/{case_id}_{variant_id}_{agent_name}_{run_id}.md`
- 统一 `run_manifest.csv` 字段，保留失败和污染运行
- 明确 `clean / suspected / contaminated / unknown` 四档污染状态
- 明确 QQ / WeChat 渠道运行也必须记录 channel 和附加上下文风险
- 新增隔离运行模式：
  - 固定 workspace：`/Users/jiangcanxiang/OpenClawBenchmarkIsolated`
  - 不暴露本地文件读写工具
  - 通过外部脚本读取单个 `agent_task_*.md` 后作为纯文本 `--message` 送入 agent
  - 每次运行生成 fresh session id
  - 默认保留联网与文献检索工具，并允许未来新增的非本地文件型远程 MCP

推荐 smoke test：

- `case_id = C001`
- `variant_id = level2`
- `input_file = benchmark/cases/C001_charitable_giving/agent_task_level2.md`

本轮未实际运行 OpenClaw，只冻结了运行配置与日志协议。

## 建议命名

```text
<case_id>_<variant_id>_<agent_name>_<run_id>.md
```

## 验收标准

- [x] 任意一个输出都能追溯到具体输入 task packet。
- [x] 日志中包含模型、时间、运行配置和工具可用性。
- [x] 运行环境和工具设置记录清楚，便于区分本地隔离边界、远程工具可用性和实际 tool use。
- [x] 失败运行也要保存日志，不要只保存成功输出。
- [x] 已提供一个可复用的本地文件隔离运行入口。

## 常见风险

- 只复制最终回答，不保存原始 prompt。
- 工具调用没有记录，无法判断是否污染。
- run_id 命名混乱，后续 annotation 对不上。
- 让 agent 自己读取 benchmark 仓库中的 case 文件，导致本地 evaluator-only 文件泄漏风险上升。

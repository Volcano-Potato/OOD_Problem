# Task 16: 配置 OpenClaw/Agent 运行与日志保存

## 目标

建立可复现的 Agent 运行设置，确保每个任务输入、输出、时间、模型和工具调用都被保存。

## 输入

- Agent 输出合同
- 已审计的 task packets
- OpenClaw / DeepScientist 运行环境

## 需要做什么

1. 确定运行模式：closed-book 为主。
2. 禁用或记录联网搜索工具。
3. 记录模型名称、temperature、seed 或其他采样参数。
4. 设定 run_id 命名规则。
5. 设定日志保存路径。
6. 保存原始输入 prompt 和原始 Agent 输出。
7. 如果使用 QQ/WeChat 渠道，保留交互截图和后台日志。

## 具体执行方法

1. 先写 `run_config.md`，不要先跑 Agent。
2. 明确每次运行使用的 model、temperature、max tokens、工具开关、closed-book 规则。
3. 每个 run 生成一个独立 markdown 日志，包含 input packet、system/task rule、raw output、tool log。
4. 建立 `run_manifest.csv`，每行对应一次运行。
5. 如果 Agent 输出中出现外部搜索、论文标题识别或工具调用污染，标记 `contamination_status=contaminated`，不要直接删除。

## run_manifest.csv 字段

```csv
run_id,case_id,variant_id,level,model,temperature,tools_enabled,closed_book,timestamp,input_file,output_file,status,contamination_status,notes
```

## 产出

- `benchmark/run_configs/run_config.md`
- `outputs/raw_agent_logs/`

## 建议命名

```text
<case_id>_<variant_id>_<level>_<run_id>.md
```

## 验收标准

- [ ] 任意一个输出都能追溯到具体输入 task packet。
- [ ] 日志中包含模型、时间、运行配置和工具可用性。
- [ ] closed-book 设置清楚，避免检索污染。
- [ ] 失败运行也要保存日志，不要只保存成功输出。

## 常见风险

- 只复制最终回答，不保存原始 prompt。
- 工具调用没有记录，无法判断是否污染。
- run_id 命名混乱，后续 annotation 对不上。

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

## Frozen Main-Run Matrix

The current main run freezes the 10-case main set and uses one canonical batch spec.

### Case List

- `C001_charitable_giving`
- `C002_consumer_credit`
- `C004_paid_search_effectiveness`
- `C005_online_ad_measurement`
- `C008_retail_tax_salience`
- `C010_fertilizer_present_bias`
- `C014_corruption_monitoring`
- `C016_hiv_risk_information`
- `C019_in_store_travel_distance`
- `C020_price_ending_field_experiment`

### Variant Policy

- Run `level2` for all 10 cases.
- Run `level3` for all 10 cases.
- Run `perturbed` for all 10 cases.
- Run `no_solution` for 4 cases chosen to cover different failure modes:
  - `C001`
  - `C005`
  - `C016`
  - `C020`

### `no_solution` Selection Rationale

The main run does not use `no_solution` for all 10 cases. Instead, it uses a smaller set chosen to maximize failure-mode coverage while keeping total runtime and later annotation burden manageable.

- `C001`
  - covers contact, engagement, and mechanism-separation failure under endogenous participation
- `C005`
  - covers digital-advertising attribution, intent selection, and missing exogenous exposure variation
- `C016`
  - covers information-treatment interpretation when credible assignment is removed but outcome structure still looks rich
- `C020`
  - covers endogenous pricing, mechanism confounding, and the temptation to overclaim from rich product-level historical data

This 4-case subset is intended to test whether the agent can refuse unsupported causal claims across distinct business-research settings, not to duplicate the full `level2/level3/perturbed` matrix.

### Total Planned Runs

```text
10 level2
10 level3
10 perturbed
4 no_solution
= 34 total runs
```

## Canonical Batch Spec

- spec file: `benchmark/run_configs/main_run_batch_spec.csv`
- split: `main`
- agent: `benchmark_isolated`
- timeout_seconds: `1800`
- thinking level: `high`

## Exact Execution Checklist

1. Confirm all 10 case directories contain approved `agent_task_level2.md`, `agent_task_level3.md`, and `agent_task_perturbed.md`.
2. Confirm the 4 selected no-solution cases contain approved `agent_task_no_solution.md`.
3. Freeze the batch spec and do not edit any task packet during the run.
4. Launch the batch runner in the background so that the full 34-run job can continue without holding an interactive shell.
5. Write stdout and stderr to a dedicated operator log.
6. Let `scripts/postprocess_openclaw_run.py` append each completed run to `outputs/run_manifest.csv`.
7. If the job stops unexpectedly, resume by creating a fresh batch spec with already-completed rows set to `enabled=false`.

## Canonical Launch Command

```bash
mkdir -p outputs
nohup ./scripts/run_batch_isolated.sh benchmark/run_configs/main_run_batch_spec.csv 1800 \
  > outputs/main_run_batch.log 2>&1 &
echo $!
```

## Current Execution Status

- [x] Main case list frozen.
- [x] Variant policy frozen.
- [x] Batch spec path frozen.
- [x] Background launch command frozen.
- [x] Batch job launched.
- [x] Batch job finished.
- [x] Manifest row count matches completed main outputs.

## Operator Launch Record

- launch_date: `2026-05-27`
- launch_mode: detached background process
- batch_pid: `98725`
- batch_log: `outputs/main_run_batch.log`
- batch_spec: `benchmark/run_configs/main_run_batch_spec.csv`
- timeout_seconds: `1800`
- first_run_observed: `C001 level2`

## Aborted-Run Rerun Record

- rerun_date: `2026-05-28`
- rerun_spec: `benchmark/run_configs/main_run_rerun_aborted_spec.csv`
- rerun_targets:
  - `C001 perturbed`
  - `C001 no_solution`
- rerun_outcome:
  - both reruns completed with `status=success`
  - original aborted runs were retained in the manifest and raw-log directory

## Final Main-Run Tally

- original frozen matrix size: `34`
- original main batch result:
  - `32 success`
  - `2 aborted`
- post-rerun main total recorded in manifest:
  - `36 rows`
  - `34 success`
  - `2 aborted retained as historical records`

## 产出

- `outputs/raw_agent_logs/main/`
- `outputs/run_manifest.csv`

## 验收标准

- [x] Main run 输出数量和 run manifest 一致。
- [x] 每条 run 都能追溯到 case_id、variant_id、level、model、timestamp。
- [x] 失败或异常运行有明确状态，不被静默删除。
- [x] 没有在 main run 中临时改 prompt 或 task packet；如果必须改，要记录版本。
- [x] main run 使用的执行方式能明确记录本地文件隔离边界、远程工具配置和实际 tool use。

## 常见风险

- 一边跑一边改任务，导致不可比。
- 只保存成功输出。
- 忘记记录模型配置，后续不可复现。
- 让 agent 在 main run 中直接读取 benchmark 仓库目录，导致本地 hidden files 泄漏风险无法排除。

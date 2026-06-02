# Task 34: 执行 v2 Retrieval-Augmented Perturbed Batch

## 目标

在 `task33` 固定 retrieval stage 和 search gate 后，正式运行 `research_agent_v2_search` 的 `10` 条 `perturbed` batch，并把结果桥接进正式评测链。

本 task 的重点是：

- 跑通 `10` 条 `perturbed`
- 保证 retrieval 行为被记录
- 把最终 Stage 5 输出写回正式 main raw log 和 manifest

本 task **不**负责最终效果解释和跨版本结论。

## 为什么现在需要做

`task33` 只会给出 infrastructure 和 smoke proof。
要回答“retrieval 是否进一步改善 v1 的表现”，必须先拿到完整的 `10` 条 `perturbed` 正式 batch。

因此，本 task 的职责是把 v2 从可运行原型推进到：

- 有完整 raw artifacts
- 有正式 manifest rows
- 有下游 extraction / annotation / metrics 入口

## 输入

- `task33` 的全部产物
- `benchmark/cases/*/agent_task_perturbed.md`
- `benchmark/run_configs/perturbed_intervention_batch_spec.csv`
- `outputs/run_manifest.csv`
- `scripts/extract_agent_claims.py`
- `scripts/build_first_pass_annotations.py`
- `scripts/build_second_labels_and_adjudication.py`
- `scripts/compute_benchmark_metrics.py`

## 需要做什么

1. 冻结 v2 的 `10` case `perturbed` batch spec。
2. 运行全部 `10` 条 `research_agent_v2_search` batch。
3. 保存 multi-stage raw artifacts。
4. 将每条 Stage 5 final memo bridge 进正式 main raw log。
5. 在 `run_manifest.csv` 中登记 `research_agent_v2_search` 行。
6. 跑 extraction / annotation / adjudication / metrics。
7. 单独生成 v2 arm 的 metrics summary 文件。

## 具体执行方法

### Step 1. 冻结 case list

保持与 v1 完全一致的 `10` case：

- `C001`
- `C002`
- `C004`
- `C005`
- `C008`
- `C010`
- `C014`
- `C016`
- `C019`
- `C020`

不要在这一轮增删 case，否则 v1/v2 对比失去可解释性。

### Step 2. 冻结运行参数

建议固定：

- `agent_variant = research_agent_v2_search`
- 同一 timeout
- 同一 `perturbed` packet 集
- 同一 postprocess 和 formal-bridge 规则

### Step 3. 正式 batch 运行

要求：

- 每个 case fresh session
- 保留 `stage2_retrieval/`
- 保留 `stage3_candidates/`
- 保留 `stage4_critique/`
- 保留 `stage5_final/`

对失败 case：

- 不覆盖旧目录
- 新增 rerun 目录和新 `run_id`
- 明确保留失败原因

### Step 4. formal bridge

每条成功 run 应写入：

- `outputs/raw_agent_logs/main/*__research_agent_v2_search__*.md`
- `outputs/run_manifest.csv`

并确保 manifest 里能追踪：

- `case_id`
- `variant_id`
- `agent_variant`
- `retrieval_attempted`
- `retrieval_successful`

### Step 5. downstream 处理

沿用 v1 的链路：

1. claim extraction
2. annotation
3. adjudication
4. metrics recomputation

但保持 baseline canonical outputs 不被覆盖。

## 建议产物

- `benchmark/run_configs/perturbed_retrieval_v2_batch_spec.csv`
- `scripts/run_research_agent_v2_batch.sh`
- `outputs/raw_agent_logs/research_agent_v2/`
- `outputs/raw_agent_logs/main/*__research_agent_v2_search__*.md`
- `results/metrics_summary_research_agent_v2_search.csv`
- `results/metrics_summary_research_agent_v2_search.md`

## 验收标准

- [x] `10` 条 `perturbed` case 的 v2 batch spec 已冻结。
- [x] `10` 条正式 v2 batch 已运行完成并落盘。
- [x] 每条成功 run 都已 bridge 进正式 main raw log。
- [x] `run_manifest.csv` 已记录 `research_agent_v2_search` rows。
- [x] 每条 run 的 retrieval metadata 可追踪。
- [x] v2 arm 已进入 extraction / annotation / adjudication / metrics 链。
- [x] arm-specific metrics summary 已生成。
- [x] 所有新增或更新文件通过 `git diff --check`。

## 常见风险

- 跑了 multi-stage artifacts，但没 bridge 回正式 main chain。
- retrieval metadata 只在中间目录里，manifest 没透传，后续没法统计。
- batch 过程中改 prompt 或 search gate，导致 v2 内部不可比。
- v2 arm 的 downstream 输出覆盖 baseline canonical 结果。

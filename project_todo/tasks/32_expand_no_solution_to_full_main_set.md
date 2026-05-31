# Task 32: 将 no-solution 从 4 条扩到主集全覆盖

## 目标

把当前 `4/4 tested no-solution runs` 扩展成更完整的主集结果，避免 `No-solution Honesty Rate` 长期停留在一个小样本观察上。

本 task 的核心问题是：

> 当 no-solution cases 从 4 个扩到更多主集 case 时，agent 还能否保持当前的 honesty / downgrade behavior？

## 为什么这是最后做的扩展

当前 `4/4` 的结果本身是有价值的，但样本量有限。
如果项目时间允许，再做这一步能让：

- honesty rate 更稳
- `no_solution` 不再只是一个补充性观察

但它不应优先于：

- framing rewrite
- Bottleneck crosswalk
- pairwise design evaluation

因为那些对项目整体故事的增益更大。

## 输入

- 所有 main-set cases 的 `agent_task_no_solution.md`
- 当前 `4` 条 no-solution main outputs
- `scripts/run_batch_isolated.sh`
- `scripts/extract_agent_claims.py`
- annotation / adjudication / metrics scripts

## 需要做什么

1. 为尚未进入主矩阵的 no-solution cases 生成 batch spec。
2. 跑完新增 no-solution runs。
3. 对新增 runs 完成：
   - claim extraction
   - annotation
   - second-label sample extension if needed
   - adjudication
4. 重算：
   - `No-solution Honesty Rate`
   - related grouped metrics
5. 更新 README / report 中的 no-solution 表述。

## 具体执行方法

1. 先冻结新增 no-solution case list，不边跑边挑。
2. 运行后先检查是否有：
   - `aborted`
   - empty outputs
   - format failures
3. 只对新增 no-solution claims 追加标注，不重做旧 claims。
4. 重算指标时，必须保留：
   - 原 `4/4` tested runs 的历史可追溯性
   - 新总体样本量
5. 如果扩完后 honesty rate 明显下降，应把这解释为：
   - earlier no-solution set may have been easier / more transparent

## 建议产物

- `benchmark/run_configs/no_solution_extension_batch_spec.csv`
- 更新后的：
  - `outputs/run_manifest.csv`
  - `outputs/raw_agent_logs/main/`
  - `outputs/parsed_claims/claims_to_annotate.csv`
  - `annotations/annotation_sheet.csv`
  - `annotations/second_labels.csv`
  - `annotations/adjudicated_labels.csv`
  - `results/metrics_summary.csv`
  - `results/metrics_summary.md`
  - `results/grouped_metrics.csv`

## 验收标准

- [ ] 已冻结新增 no-solution 扩展列表。
- [ ] 新增 no-solution runs 已全部落盘。
- [ ] 新增 no-solution claims 已进入 annotation / adjudication。
- [ ] `No-solution Honesty Rate` 已重算并更新样本量。
- [ ] 报告和 README 的相关措辞已同步更新。
- [ ] 所有修改通过 `git diff --check`。

## 常见风险

- 扩了运行，但没接回 annotation 与 metrics 链路。
- 把 `4/4 tested runs` 和扩展后总体样本混写，导致口径不清。
- honesty rate 下降后没有解释样本难度变化。

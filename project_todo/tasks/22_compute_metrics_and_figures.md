# Task 22: 计算指标与生成图表

## 目标

把人工标注转成可报告的错误率、能力分数和图表。

## 输入

- `annotations/adjudicated_labels.csv`
- case metadata

## 需要做什么

1. 计算 Design-Evidence Inconsistency Rate。
2. 计算 Unsupported Design Claim Rate。
3. 计算 Critical Design Omission Rate。
4. 计算 Mechanism Confounding Rate。
5. 计算 No-solution Honesty Rate。
6. 按 Level 1/2/3 比较信息梯度。
7. 按 domain、design_family、failure_mode 分组统计。
8. 生成图表。

## 具体执行方法

1. 先定义分母：claim-level 指标用 claim 数，case-level 指标用 case 数，run-level 指标用 run 数。
2. 所有指标只读取 `adjudicated_labels.csv`。
3. 合并 case metadata，用于分组统计。
4. 对缺失输出、format_error、contaminated run 单独计数，不混入正常错误率。
5. 每张图保存源数据 CSV 和图片文件。
6. 在 `metrics_summary.md` 中写每个指标的公式。

## 指标公式示例

```text
Design-Evidence Inconsistency Rate
= count(error_type in {Unsupported Claim, Overclaim, Mis-citation, Contradiction}) / total_claims

No-solution Honesty Rate
= count(no_solution runs where agent refuses strong causal claim) / total_no_solution_runs
```

## 产出

- `results/metrics_summary.csv`
- `results/error_type_counts.csv`
- `results/case_level_scores.csv`
- `results/figures/`

## 推荐图表

- Level 1/2/3 平均设计分。
- 错误类型分布柱状图。
- case x linchpin omission 热力图。
- perturbed variant 前后 design downgrade 比较。

## 验收标准

- [x] 指标公式在脚本或文档中明确。
- [x] 所有图表能追溯到 `adjudicated_labels.csv`。
- [x] 总体指标和分组指标都输出。
- [x] 缺失值和无输出 run 有处理规则。

## 完成记录

- 新增可复跑脚本：
  - `scripts/compute_benchmark_metrics.py`
- 生成总体指标：
  - `results/metrics_summary.csv`
  - `results/metrics_summary.md`
- 生成明细表：
  - `results/error_type_counts.csv`
  - `results/case_level_scores.csv`
  - `results/run_level_scores.csv`
  - `results/grouped_metrics.csv`
- 生成图表及其源数据：
  - `results/figures/information_gradient_scores.csv`
  - `results/figures/information_gradient_scores.svg`
  - `results/figures/error_type_distribution.csv`
  - `results/figures/error_type_distribution.svg`
  - `results/figures/case_error_heatmap.csv`
  - `results/figures/case_error_heatmap.svg`
  - `results/figures/perturbed_downgrade.csv`
  - `results/figures/perturbed_downgrade.svg`

## 本轮关键指标

- `Mean Claim Score`: `0.8193`
- `Design-Evidence Inconsistency Rate`: `0.2526`
- `Unsupported Design Claim Rate`: `0.0842`
- `Contradiction Rate`: `0.0246`
- `Overclaim Rate`: `0.1439`
- `Critical Design Omission Rate (proxy)`: `0.0421`
- `Mechanism Confounding Rate (proxy)`: `0.2564`
- `No-solution Honesty Rate`: `1.0000`
- `Level 2 Mean Run Score`: `0.8213`
- `Level 3 Mean Run Score`: `0.8350`
- `Perturbed Mean Run Score`: `0.7380`

## 说明

- 本轮主矩阵未包含 `level1`，因此信息梯度图实际比较的是 `level2` 与 `level3`。
- `Critical Design Omission Rate` 与 `Mechanism Confounding Rate` 目前是 proxy 指标；原因是当前 adjudication schema 没有 omission-only 或 mechanism-only 的显式标签。
- `run_manifest.csv` 没有单独的 `split=main` 列；脚本通过 `raw_output_file` 位于 `outputs/raw_agent_logs/main/` 来识别主运行。

## 常见风险

- 只报总体错误率，无法解释失败在哪里。
- 指标分母不清楚。
- 图表无法复现。

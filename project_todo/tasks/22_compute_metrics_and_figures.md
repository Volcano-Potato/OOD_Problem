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

- [ ] 指标公式在脚本或文档中明确。
- [ ] 所有图表能追溯到 `adjudicated_labels.csv`。
- [ ] 总体指标和分组指标都输出。
- [ ] 缺失值和无输出 run 有处理规则。

## 常见风险

- 只报总体错误率，无法解释失败在哪里。
- 指标分母不清楚。
- 图表无法复现。

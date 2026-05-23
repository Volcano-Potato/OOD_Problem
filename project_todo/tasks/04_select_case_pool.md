# Task 04: 选择 Pilot Set 与 Main Set

## 目标

从候选论文中选出 5 个 pilot cases 和 10 个 main-set cases，覆盖不同领域、设计家族和失败模式。

## 输入

- `deepscientist_econ_business_experiment_papers.md`
- `downloads/deepscientist_econ_business_experiment_papers/`
- Task 02 的 taxonomy

## 需要做什么

1. 从候选池中列出 15-20 个可用 case。
2. 为每个候选 case 填写 domain、design_family、key_failure_mode、difficulty。
3. 标记 5 个 pilot cases。
4. 标记 10 个 main-set cases。
5. 说明每个入选 case 的诊断价值。
6. 标记可能有预训练记忆污染风险的经典论文。

## 具体执行方法

1. 先列 15-20 个候选，不要一开始就定 5 个。
2. 对每个候选写一句 `diagnostic_value`：这个 case 最能暴露哪种弱点。
3. 用 metadata 表检查覆盖度：domain、design_family、key_failure_mode 不能过于集中。
4. 标记 `memorization_risk`，经典论文可以保留，但不要让 main set 全是高记忆风险论文。
5. Pilot set 优先选“识别命门清楚、PDF 信息充足、容易匿名化”的 case。
6. Main set 再加入更难的机制分解、内生 exposure、measurement error 和 no-solution 场景。

## 选择表模板

```markdown
| case_id | paper_key | domain | design_family | key_failure_mode | diagnostic_value | memorization_risk | selected_for |
|---|---|---|---|---|---|---|---|
```

## 产出

- 更新后的 `benchmark/case_registry.csv`
- `benchmark/case_selection_notes.md`

## 推荐 pilot set

- Consumer credit information asymmetry
- Charitable giving social pressure
- Online advertising endogenous exposure
- Tax salience
- Fertilizer timing / present bias

## 验收标准

- [x] Pilot set 至少覆盖 4 种 failure modes。
- [x] Main set 至少覆盖 5 个 domains 或 subdomains。
- [x] 至少包含 2 个营销/平台广告相关 case。
- [x] 至少包含 2 个机制分解类 case。
- [x] 至少包含 1 个 measurement error 或 manipulable outcome case。
- [x] 每个入选 case 都有本地 PDF 或可靠来源说明。

## 常见风险

- 全选最著名论文，Agent 可能靠记忆答题。
- 全是 RCT，无法测试 DID/RDD/IV/event study 的边界。
- case 过于相似，最后只能得出很窄的结论。

# Task 02: 设计 Case Taxonomy 与 Metadata Schema

## 目标

定义每个 case 的分类字段，使后续能按领域、设计类型、失败模式和难度统计 Agent 表现。

## 输入

- Task 01 的 `benchmark/scope.md`
- `data_idea.md` 中的 Quality-control metadata
- `deepscientist_econ_business_experiment_papers.md`

## 需要做什么

1. 定义 case metadata 字段。
2. 定义 domain 枚举值。
3. 定义 design_family 枚举值。
4. 定义 key_failure_mode 枚举值。
5. 定义 variant_type 枚举值。
6. 定义 difficulty 标准。
7. 写一个空白 case registry 表头。

## 具体执行方法

1. 先从候选论文清单中选 5 篇不同类型论文试填 metadata，字段能填清楚再冻结 schema。
2. `domain` 只写应用领域，不写识别方法，例如 marketing、labor、public_econ。
3. `design_family` 只写合理答案可能涉及的设计族，例如 RCT、DID、RDD、IV、audit。
4. `key_failure_mode` 写这个 case 最想暴露的 Agent 弱点，例如 endogenous_exposure、mechanism_confounding。
5. `difficulty` 按匿名任务中的识别条件隐蔽程度定，不按原论文发表级别定。
6. `variant_plan` 明确该 case 后续做哪些版本：level1、level2、level3、perturbed、no_solution。

## case_registry.csv 模板

```csv
case_id,paper_key,short_name,domain,design_family,key_failure_mode,difficulty,variant_plan,source_pdf,selected_for_pilot,selected_for_main,leakage_risk,notes
C001,,,,,,,,,,,,
```

## 产出

- `benchmark/case_taxonomy.md`
- `benchmark/case_registry.csv`

## 推荐字段

```csv
case_id,paper_key,domain,design_family,key_failure_mode,difficulty,variant_plan,source_pdf,selected_for_pilot,selected_for_main,notes
```

## 推荐枚举

- `domain`: marketing, labor, public_econ, behavioral, development, education, health, platform_economics
- `design_family`: RCT, field_experiment, audit, DID, RDD, IV, event_study, mechanism_experiment, no_solution
- `key_failure_mode`: endogenous_exposure, selection, mechanism_confounding, measurement_error, spillover, attrition, weak_identification, overclaim
- `difficulty`: easy, medium, hard
- `variant_type`: original_like, level1, level2, level3, perturbed, no_solution

## 验收标准

- [x] 每个字段都有定义，不只是字段名。
- [x] 枚举值足够覆盖已有候选论文。
- [x] `case_registry.csv` 可以直接被后续脚本读取。
- [x] 能支持后续按 domain、design_family、failure_mode 分组统计。

## 常见风险

- metadata 太少，后续只能报总体错误率。
- design_family 和 key_failure_mode 混在一起。
- 难度等级没有标准，变成人工主观印象。

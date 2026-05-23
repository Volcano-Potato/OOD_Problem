# OOD-CausalDesignBench Todo List

本文件夹把 `OOD_CausalDesignBench_pipeline_plan.md` 和 `data_idea.md` 转成可执行任务清单。目标是先完成一个研究优先的 benchmark pipeline，再根据需要裁剪成展示或课程材料。

## 总原则

- 不把任务做成一次性 prompt demo，而是做成可复查、可复跑、可标注的 benchmark。
- 每个 case 都区分 agent-facing task packet、evaluator-only gold reference 和 quality-control metadata。
- 先跑 pilot set，再扩展 main set；不要在 schema 未稳定时批量生产所有 case。
- 生成可以用强模型辅助，但所有关键评测依据必须经过人工审计。
- 所有 Agent 输出都必须保留原始日志，所有人工判断都必须落到 annotation 表。

## 阶段总览

| 阶段 | 任务 | 目标产物 |
|---|---|---|
| A. Benchmark 设计冻结 | 01-04 | case taxonomy、目录结构、case registry、schema |
| B. 单 case 构建流水线 | 05-14 | source facts、gold reference、Level 1/2/3、variants、audit |
| C. Agent 运行 | 15-17 | 统一任务合同、OpenClaw 运行配置、pilot logs |
| D. Main run 与标注 | 18-21 | main outputs、claim table、annotation guide、adjudicated labels |
| E. 统计与分析 | 22-23 | metrics、失败案例、图表 |
| F. 报告与交付 | 24 | research report、reproducibility package、展示材料 |

## 任务清单

| ID | 任务 | 依赖 | 详细文件 |
|---|---|---|---|
| 01 | 冻结 benchmark scope 与研究问题 | 无 | [01_freeze_benchmark_scope.md](tasks/01_freeze_benchmark_scope.md) |
| 02 | 设计 case taxonomy 与 metadata schema | 01 | [02_case_taxonomy_metadata.md](tasks/02_case_taxonomy_metadata.md) |
| 03 | 建立目录结构与文件模板 | 01-02 | [03_repository_structure_templates.md](tasks/03_repository_structure_templates.md) |
| 04 | 选择 pilot set 与 main set | 02 | [04_select_case_pool.md](tasks/04_select_case_pool.md) |
| 05 | 为单篇论文准备 source packet | 04 | [05_prepare_source_packet.md](tasks/05_prepare_source_packet.md) |
| 06 | 抽取 source facts | 05 | [06_extract_source_facts.md](tasks/06_extract_source_facts.md) |
| 07 | 编写 hidden gold reference | 06 | [07_draft_gold_reference.md](tasks/07_draft_gold_reference.md) |
| 08 | 审计 gold reference | 07 | [08_audit_gold_reference.md](tasks/08_audit_gold_reference.md) |
| 09 | 构造 Level 1 agent task | 08 | [09_build_level1_task.md](tasks/09_build_level1_task.md) |
| 10 | 构造 Level 2 Data Card task | 08-09 | [10_build_level2_data_card.md](tasks/10_build_level2_data_card.md) |
| 11 | 构造 Level 3 threat-hint task | 10 | [11_build_level3_threat_hints.md](tasks/11_build_level3_threat_hints.md) |
| 12 | 构造 perturbed variant | 10-11 | [12_build_perturbed_variant.md](tasks/12_build_perturbed_variant.md) |
| 13 | 构造 no-solution variant | 10-11 | [13_build_no_solution_variant.md](tasks/13_build_no_solution_variant.md) |
| 14 | 做匿名化、泄漏与有效性审计 | 09-13 | [14_leakage_validity_audit.md](tasks/14_leakage_validity_audit.md) |
| 15 | 冻结 Agent 统一输出合同 | 09-14 | [15_freeze_agent_output_contract.md](tasks/15_freeze_agent_output_contract.md) |
| 16 | 配置 OpenClaw/Agent 运行与日志保存 | 15 | [16_configure_agent_runs.md](tasks/16_configure_agent_runs.md) |
| 17 | 执行 pilot run 并修订 schema | 04,14-16 | [17_run_pilot_and_revise.md](tasks/17_run_pilot_and_revise.md) |
| 18 | 扩展并执行 main run | 17 | [18_run_main_benchmark.md](tasks/18_run_main_benchmark.md) |
| 19 | 从 Agent 输出抽取 claim | 18 | [19_extract_agent_claims.md](tasks/19_extract_agent_claims.md) |
| 20 | 制定 annotation guide 与人工标注 | 19 | [20_annotation_guide_and_labeling.md](tasks/20_annotation_guide_and_labeling.md) |
| 21 | 复标、分歧裁决与标签冻结 | 20 | [21_adjudicate_annotations.md](tasks/21_adjudicate_annotations.md) |
| 22 | 计算指标与生成图表 | 21 | [22_compute_metrics_and_figures.md](tasks/22_compute_metrics_and_figures.md) |
| 23 | 做失败案例归因分析 | 21-22 | [23_failure_case_analysis.md](tasks/23_failure_case_analysis.md) |
| 24 | 写研究报告与复现说明 | 22-23 | [24_report_and_reproducibility_package.md](tasks/24_report_and_reproducibility_package.md) |

## 推荐执行顺序

1. 先完成 01-04，冻结 benchmark 的边界、case 分类和目录结构。
2. 用 1 个 case 完整走通 05-17，确认 schema、匿名化和输出合同可用。
3. 用 pilot set 跑 5 个 case，修正任务包和标注规范。
4. 扩展 main set 到 10 个 case，执行 18-21。
5. 最后做 22-24，形成结果、失败案例和报告。

## 完成定义

整个 todo 完成时，应至少具备：

- 10 个 main-set case 的完整 task packet 和 hidden gold reference。
- 每个 case 至少包含 Level 2、Level 3 和一个 perturbed variant。
- 至少 2 个 no-solution variants。
- 完整 Agent 原始输出日志。
- claim-level annotation 表和 adjudicated labels。
- metrics summary、错误类型分布、信息梯度图、case x linchpin 热力图。
- 研究报告和复现说明。


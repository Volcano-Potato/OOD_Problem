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
| C. Agent 运行 | 15-17,25 | 统一任务合同、OpenClaw 运行配置、pilot logs、batch runner |
| D. Main run 与标注 | 18-21 | main outputs、claim table、annotation guide、adjudicated labels |
| E. 统计与分析 | 22-23 | metrics、失败案例、图表 |
| F. 报告与交付 | 24 | research report、reproducibility package、展示材料 |
| G. 结果补强、Agent 干预与外部对齐 | 25-38 | batch runner、信息梯度补强、Bottleneck/APE 对齐、agent loop ablation、可选扩展 |

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
| 25 | 构建自动化 batch runner 与运行后处理 | 16-17 | [25_build_batch_runner.md](tasks/25_build_batch_runner.md) |
| 26 | 补强信息梯度、扰动复用证据与结果措辞 | 18-24 | [26_strengthen_information_gradient_and_perturbation_evidence.md](tasks/26_strengthen_information_gradient_and_perturbation_evidence.md) |
| 27 | 用 Bottleneck 重写项目定位与主叙事 | 24,26 | [27_reframe_project_with_bottleneck.md](tasks/27_reframe_project_with_bottleneck.md) |
| 28 | 构建 Bottleneck execution-dimension crosswalk | 24,26,27 | [28_build_bottleneck_execution_crosswalk.md](tasks/28_build_bottleneck_execution_crosswalk.md) |
| 29 | 增加 APE-style pairwise design-memo evaluation | 24,26-28 | [29_run_pairwise_design_memo_evaluation.md](tasks/29_run_pairwise_design_memo_evaluation.md) |
| 30 | 在 perturbed cases 上测试 design-critic intervention | 26 | [30_test_design_critic_intervention_on_perturbed.md](tasks/30_test_design_critic_intervention_on_perturbed.md) |
| 31 | 为 RQ1 增加 threat-recognition 量化 | 24,26 | [31_quantify_threat_recognition_for_rq1.md](tasks/31_quantify_threat_recognition_for_rq1.md) |
| 32 | 将 no-solution 从 4 条扩到主集全覆盖 | 18-26 | [32_expand_no_solution_to_full_main_set.md](tasks/32_expand_no_solution_to_full_main_set.md) |
| 33 | 构建 v2 的 retrieval stage 与 search gate | 30 | [33_build_v2_retrieval_stage_and_search_gate.md](tasks/33_build_v2_retrieval_stage_and_search_gate.md) |
| 34 | 执行 v2 retrieval-augmented perturbed batch | 33 | [34_run_v2_retrieval_augmented_perturbed_batch.md](tasks/34_run_v2_retrieval_augmented_perturbed_batch.md) |
| 35 | 分析 v2 相对 v1 的 retrieval effect | 34 | [35_analyze_v2_vs_v1_retrieval_effect.md](tasks/35_analyze_v2_vs_v1_retrieval_effect.md) |
| 36 | 构建 v3 的 planner 与 debate loop | 35 | [36_build_v3_planner_and_debate_loop.md](tasks/36_build_v3_planner_and_debate_loop.md) |
| 37 | 执行 v3 planner-debate perturbed batch | 36 | [37_run_v3_planner_debate_perturbed_batch.md](tasks/37_run_v3_planner_debate_perturbed_batch.md) |
| 38 | 汇总 v3 与 v1/v2 的 ablation 对比 | 37 | [38_analyze_v3_vs_v1_v2_ablation.md](tasks/38_analyze_v3_vs_v1_v2_ablation.md) |
| 39 | 用单一外部 LLM Judge 做双轴最终报告质量评测 | 30,32,35,38 | [39_run_llm_judge_report_quality_eval.md](tasks/39_run_llm_judge_report_quality_eval.md) |

## 推荐执行顺序

1. 先完成 01-04，冻结 benchmark 的边界、case 分类和目录结构。
2. 用 1 个 case 完整走通 05-17，确认 schema、匿名化和输出合同可用。
3. 用 pilot set 跑 5 个 case，修正任务包和标注规范。
4. 在 main set 扩展前完成 25，确保 batch orchestration、raw log 和 manifest 回填自动化。
5. 扩展 main set 到 10 个 case，执行 18-21。
6. 最后做 22-24，形成结果、失败案例和报告。
7. 若答辩前需要补强主结果，执行 26，优先补 `level1`、`perturbed` 配对计数与结果措辞收口。
8. 若希望把项目进一步对齐 Bottleneck / APE 的研究姿态，按 27 → 28 → 29 的顺序做补强。
9. `task27-29` 已完成；若继续推进扩展实验，先执行 `task30`，再做 `task31-32`。
10. 若继续把 `research_agent_redesign_plan.md` 落到 v2 / v3，按 `33 -> 34 -> 35 -> 36 -> 37 -> 38` 执行，保持 clean ablation。

## 当前执行状态

- 主线 benchmark：已完成到 `task26`
- 扩展对齐：
  - `task27` complete
  - `task28` complete
  - `task29` complete as exploratory extension
- intervention 扩展：
  - `task30` complete as first intervention study
    - `research_agent_v1` 已完成 `10` 条 `perturbed` batch rerun
    - paired audit headline: `9/10 -> 2/10`
  - `task31` complete
    - baseline `level2` threat-recognition audit headline: `19/20`
    - `9/10` cases scored `2/2`
  - `task32` complete
  - `task33` complete
    - v2 retrieval stage/search gate implemented
    - `C001_perturbed` smoke passed end-to-end
    - session-based tool accounting fixed
  - `task34` complete
    - `10`-case `research_agent_v2_search` perturbed batch completed
    - formal main rows and retrieval metadata recorded in `outputs/run_manifest.csv`
    - downstream extraction / annotation / adjudication / metrics chain completed
    - `results/metrics_summary_research_agent_v2_search.csv` and `.md` generated
  - `task35` complete
    - v2 paired audit headline: `0/10` mechanical reuse
    - v1 vs v2 delta: `2/10 -> 0/10`
    - retrieval attempt / success: `10/10`, with `0/10` zero-tool-use runs
    - retrieval usefulness audit generated, with `helpful 6 / neutral 3 / noisy 1 / failed 0`
    - recommendation: `go to v3`, but only as an optional ablation rather than a rescue step
  - `task36` complete
    - smoke-only `research_agent_v3_planner_debate` runner implemented
    - single-case `C005_perturbed` smoke passed end-to-end
    - `Stage 0 planner`, `Stage 3b response`, and `Stage 4b critique` artifacts now land under `outputs/raw_agent_logs/research_agent_v3/`
    - planner/debate stop rule fixed at one debate round for smoke validation
    - no formal bridge executed; `outputs/run_manifest.csv` remains unchanged for `v3`
  - `task37` complete
    - clean full rerun of `research_agent_v3_planner_debate` `10`-case `perturbed` batch completed
    - formal main rows and planner/retrieval/debate metadata recorded in `outputs/run_manifest.csv`
    - downstream extraction / annotation / adjudication / metrics chain completed
    - `results/metrics_summary_research_agent_v3_planner_debate.csv` and `.md` generated
    - current claim-level headline metrics remain provisional; the main `v3 vs v1/v2` interpretation is deferred to `task38`
  - `task38` complete
    - `v3` paired audit headline: `0/10`
    - unified baseline / `v1` / `v2` / `v3` ablation table generated
    - recommendation: stop at `research_agent_v2_search` as the default intervention arm
    - `research_agent_v3_planner_debate` retained as a diagnostic / ablation arm rather than a default upgrade
  - `task39` not started
    - protocol target: single fixed non-DeepSeek web chatbot
    - scope: report-level quality evaluation for baseline / `v1` / `v2` / `v3`
    - output layers: absolute rubric score + within-case ranking

当前最合理的后续顺序是：

1. 若要收尾，优先做：
   - 中文汇报版裁剪
   - 英文论文叙事统一
   - 仓库状态冻结与归档
2. 若要补一层外部 report-level evaluation，执行 `task39`
3. 如有需要，再补 `research_agent_v1` 的 run-specific annotation overrides，使其 claim-level headline metrics 也达到可稳定引用状态
5. 如有需要，再把 `task31` 的轻量 audit 扩到 intervention arm，做 baseline vs `research_agent_v1` 的 threat-recognition appendix

## 完成定义

整个 todo 完成时，应至少具备：

- 10 个 main-set case 的完整 task packet 和 hidden gold reference。
- 每个 case 至少包含 Level 2、Level 3 和一个 perturbed variant。
- 至少 2 个 no-solution variants。
- 完整 Agent 原始输出日志。
- claim-level annotation 表和 adjudicated labels。
- metrics summary、错误类型分布、信息梯度图、case x linchpin 热力图。
- 研究报告和复现说明。

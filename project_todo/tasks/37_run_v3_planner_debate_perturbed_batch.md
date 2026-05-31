# Task 37: 执行 v3 Planner-Debate Perturbed Batch

## 目标

在 `task36` 固定 v3 loop 后，正式运行 `research_agent_v3_planner_debate` 的 `10` 条 `perturbed` batch，并将结果桥接进正式评测链。

本 task 的重点是：

- 跑通 v3 的正式 batch
- 记录 planner / retrieval / debate 的全过程
- 生成可用于和 v1/v2 做 clean ablation 的正式输出

## 为什么现在需要做

没有完整 batch，就无法判断：

- planner 是否真的改善后续搜索和候选生成
- debate 是否真的进一步压低 residual reuse
- v3 的额外复杂度是否值得

因此，这一步是把 v3 从 smoke-test pipeline 推到正式实验条件。

## 输入

- `task36` 的全部产物
- 与 v1 / v2 完全一致的 `10` 条 `perturbed` packets
- `outputs/run_manifest.csv`
- 现有 extraction / annotation / adjudication / metrics 链

## 需要做什么

1. 冻结 v3 的 `10` case `perturbed` batch spec。
2. 正式运行 v3 batch。
3. 保存 planner / retrieval / debate / final 的全部 artifacts。
4. 将 Stage 5 final memo bridge 进正式 main raw log。
5. 在 manifest 中登记 `research_agent_v3_planner_debate` rows。
6. 跑 extraction / annotation / adjudication / metrics。

## 具体执行方法

### Step 1. 保持 case set 不变

仍使用 v1 / v2 同一组 `10` 个 `perturbed` cases。

### Step 2. 冻结 v3 运行参数

建议固定：

- `agent_variant = research_agent_v3_planner_debate`
- 最大 debate 轮数
- planner schema 版本
- retrieval policy 版本
- timeout

### Step 3. 批量运行

每条成功 run 应留下：

- `stage0_planner/`
- `stage2_retrieval/`
- `stage3_candidates/`
- `stage4_critique/`
- `debate_round_1/`
- `debate_round_2/`（如有）
- `stage5_final/`

### Step 4. formal bridge 与 downstream

与 v1/v2 一样：

- 写入 `outputs/raw_agent_logs/main/`
- 追加 `outputs/run_manifest.csv`
- 跑 extraction / annotation / adjudication / metrics

## 建议产物

- `benchmark/run_configs/perturbed_planner_debate_v3_batch_spec.csv`
- `scripts/run_research_agent_v3_batch.sh`
- `outputs/raw_agent_logs/research_agent_v3/`
- `outputs/raw_agent_logs/main/*__research_agent_v3_planner_debate__*.md`
- `results/metrics_summary_research_agent_v3_planner_debate.csv`
- `results/metrics_summary_research_agent_v3_planner_debate.md`

## 验收标准

- [ ] v3 的 `10` 条 `perturbed` batch spec 已冻结。
- [ ] `10` 条正式 v3 batch 已运行完成并落盘。
- [ ] planner / retrieval / debate / final artifacts 均已保留。
- [ ] 每条成功 run 都已 bridge 进正式 main raw log。
- [ ] manifest 中已登记 `research_agent_v3_planner_debate` rows。
- [ ] v3 arm 已进入 extraction / annotation / adjudication / metrics 链。
- [ ] arm-specific metrics summary 已生成。
- [ ] 所有新增或更新文件通过 `git diff --check`。

## 常见风险

- v3 比 v2 更复杂，但仍沿用过弱的日志结构，导致 debate 过程不可审。
- debate 轮数太多，成本失控。
- v3 batch 中途调整 planner / debate prompt，导致内部不可比。
- 没有把 planner / debate metadata 透传到最终分析层。


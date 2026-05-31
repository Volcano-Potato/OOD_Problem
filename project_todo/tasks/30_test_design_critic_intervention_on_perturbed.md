# Task 30: 在 perturbed cases 上测试 design-critic intervention

## 目标

把当前项目从 “诊断 agent 弱点” 推进一步到 “验证一个小型可操作修复是否有效”。

本 task 的核心问题是：

> 如果在 final answer 前强制加入一层 reviewer-style design critic，自检关键 identifying condition 是否失效，能否降低 `perturbed` 上的 `mechanical reuse`？

## 为什么现在值得做

当前最强的 failure finding 之一已经很清楚：

- `9/10` perturbed cases show mechanical reuse

这说明问题不只是“分数低了”，而是 agent 在关键条件变坏后仍沿用 base logic。
因此，最自然的下一步不是扩 case，而是做一个 **最小 intervention**：

- 不改 benchmark
- 不改标注体系
- 只改 agent 在输出前的自检逻辑

如果这个 intervention 能降低 reuse，它会让项目从：

- diagnosis only

变成：

- diagnosis + targeted repair

## 输入

- `benchmark/cases/*/agent_task_perturbed.md`
- `results/perturbed_mechanical_reuse.csv`
- `results/perturbed_pair_audit.md`
- 现有 `benchmark_isolated` 运行 pipeline
- `outputs/raw_agent_logs/main/*perturbed*.md`

## 需要做什么

1. 设计一个固定的 `design critic checklist`。
2. 选定 intervention 运行方式：
   - prompt prepend
   - two-stage self-critique
   - explicit critique block before final answer
3. 仅在 10 个 `perturbed` cases 上 rerun。
4. 对 intervention outputs 重新做：
   - claim extraction if needed
   - 或至少 mechanical reuse audit
5. 比较：
   - baseline `mechanical reuse`
   - intervention `mechanical reuse`
6. 报告是否有改善，以及改善集中在哪类 case。

## 具体执行方法

### Step 1. 设计 checklist

建议 checklist 至少包含：

1. What is the causal estimand?
2. What exact variation identifies it?
3. Which assumption or condition is critical?
4. Has the packet removed or weakened that condition?
5. If yes, what weaker claim remains defensible?

### Step 2. 固定 intervention 方式

推荐只选一种，不要同时做多个变体：

- **prompt prepend**
  - 最省事
- **forced critique block before final answer**
  - 最容易审查 agent 是否真的经过该步骤

### Step 3. 限定运行集

只跑：

- 10 个 `perturbed` cases

不要一开始扩到 level2 / no-solution / full matrix。

### Step 4. 定义改善指标

至少要看：

- `mechanical reuse: X/10 -> Y/10`

可选再看：

- `unsupported claims`
- `overclaim`
- `contradicted claims`

## 建议产物

- `benchmark/prompts/design_critic_checklist.md`
- `benchmark/prompts/perturbed_intervention_prompt.md`
- `benchmark/run_configs/perturbed_intervention_batch_spec.csv`
- `results/perturbed_intervention_eval.csv`
- `results/perturbed_intervention_eval.md`

## 验收标准

- [x] intervention checklist 已固定成单独文件。
- [x] intervention 运行方式已固定。
- [x] 10 个 perturbed cases 已 rerun。
- [x] 已产出 intervention 结果表。
- [x] 已比较 baseline 与 intervention 的 `mechanical reuse`。
- [x] 已说明哪些 case 改善，哪些没有改善。
- [x] 报告中没有把单次 intervention 写成普遍解决方案。
- [x] 所有修改通过 `git diff --check`。

## 常见风险

- 一次同时测试多个 intervention，导致结论混乱。
- 把 claim-level 全链路重做得过大，拖慢项目。
- 看到少量改善就过度宣称“方法有效”。
- intervention prompt 泄漏了过多 gold logic，反而污染 benchmark。

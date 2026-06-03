# Task 38: 汇总 v3 与 v1/v2 的 Ablation 对比

## 目标

在 `task37` 完成后，对三条 intervention 线做统一结论：

- `v1`: critic-and-reconcile
- `v2`: critic + retrieval
- `v3`: planner + retrieval + debate

本 task 的重点是回答：

> 复杂度的增加是否带来了额外、可 defend 的收益？

## 为什么现在需要做

如果没有这一层统一对比，你最终只会得到三批实验，而不是一个清楚的 agent-design 结论。

你真正需要的是：

- 哪个机制有效
- 哪个机制只是更贵
- 未来如果继续扩展，应该保留哪一层

## 输入

- `results/research_agent_v1_vs_baseline.md`
- `task35` 产物
- `task37` 的全部产物
- v3 的 paired audit、tool-use、planner/debate metadata

## 需要做什么

1. 对 v3 做 paired manual audit。
2. 生成 v3 的 `mechanical_reuse` headline。
3. 统计：
   - planner usage
   - retrieval success
   - debate rounds actually used
4. 构造 v1 / v2 / v3 的统一对比表。
5. 回答复杂度是否值得。
6. 给出最终推荐配置。

## 具体执行方法

### Step 1. 完成 v3 paired audit

沿用与 v1 / v2 完全一致的 `mechanical_reuse` 判定口径。

建议产物：

- `results/perturbed_mechanical_reuse_v3.csv`
- `results/perturbed_pair_audit_v3.md`

### Step 2. 汇总三组 headline

至少放在一张表里：

- baseline
- v1
- v2
- v3

字段至少包括：

- `mechanical_reuse_yes_count`
- `mechanical_reuse_rate`
- `tool_use_rate`
- `retrieval_success_rate`
- `mean_debate_rounds`
- `pipeline_complexity_note`

### Step 3. 做 mechanism-level interpretation

至少明确区分：

- critic 本身的贡献
- retrieval 的增量贡献
- planner / debate 的增量贡献

如果没有显著额外收益，要明确写出来。

### Step 4. 给出最终 recommendation

必须给出一个明确建议：

- 保留 `v1`
- 升级到 `v2`
- 升级到 `v3`
- 或停在某个更简单版本

不要只给表，不给判断。

## 建议产物

- `results/perturbed_mechanical_reuse_v3.csv`
- `results/perturbed_pair_audit_v3.md`
- `results/research_agent_v3_vs_v1_v2.md`
- `results/research_agent_ablation_summary.csv`
- `results/research_agent_ablation_summary.md`

## 验收标准

- [x] v3 的 paired manual audit 已完成。
- [x] v3 的 `mechanical_reuse` headline 已给出。
- [x] planner / retrieval / debate metadata 已完成汇总。
- [x] 已产出统一的 v1 / v2 / v3 对比表。
- [x] 已明确写出复杂度是否值得。
- [x] 已给出最终推荐配置。
- [x] 所有新增或更新文件通过 `git diff --check`。

## 完成说明

- 已生成：
  - `results/perturbed_mechanical_reuse_v3.csv`
  - `results/perturbed_pair_audit_v3.md`
  - `results/research_agent_v3_vs_v1_v2.md`
  - `results/research_agent_ablation_summary.csv`
  - `results/research_agent_ablation_summary.md`
- `v3` paired manual audit headline：
  - `0/10` `mechanical_reuse`
- 三组 headline 对比：
  - baseline: `9/10`
  - `v1`: `2/10`
  - `v2`: `0/10`
  - `v3`: `0/10`
- `v3` metadata summary：
  - planner present `10/10`
  - retrieval success `10/10`
  - mean debate rounds `1.0`
  - mean retrieval tool calls `19.7`
  - mean pipeline duration `899.7s`
- 最终推荐配置：
  - 默认保留 `research_agent_v2_search`
  - `research_agent_v3_planner_debate` 保留为诊断 / ablation arm，而不是默认升级配置
- 解释边界：
  - `v3` 的 claim-level headline metrics 仍应视为 provisional
  - `task38` 的主结论基于 paired `mechanical_reuse` audit 与运行元数据，而不是基于 `Mean Claim Score = 1.0`

## 常见风险

- 只比较最终分数，不比较不同机制到底做了什么。
- debate 轮数很多，但没有实际增益，却仍把 v3 写成更优。
- planner / retrieval / debate 三层同时变化，却不给出解释框架。
- 只给结果表，不给最终推荐，导致后续路线仍然模糊。

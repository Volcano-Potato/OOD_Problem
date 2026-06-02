# Task 35: 分析 v2 相对 v1 的 Retrieval Effect

## 目标

在 `task34` 完成后，回答一个干净的 ablation 问题：

> 在 critic-intervention 已经存在的前提下，显式 retrieval stage 是否进一步改善 `perturbed` 下的 design behavior？

本 task 的重点不是再建新 pipeline，而是把 v2 的效果讲清楚：

- 是否进一步降低 mechanical reuse
- 是否真的产生了工具使用
- retrieval 到底是 helpful、neutral 还是 noisy

## 为什么现在需要做

如果只跑完 `task34` 而不单独分析，你最多只能说：

- “又多跑了一组实验”

但你真正需要的是一个可 defend 的 ablation 结论：

- v2 比 v1 更好、没更好、还是只是更贵

## 输入

- `results/perturbed_mechanical_reuse_v1.csv`
- v2 的 paired audit 结果
- `results/research_agent_v1_vs_baseline.md`
- `results/metrics_summary_research_agent_v2_search.csv`
- `outputs/raw_agent_logs/research_agent_v2/`
- `outputs/raw_agent_logs/main/*__research_agent_v2_search__*.md`
- `run_manifest.csv`

## 需要做什么

1. 对 v2 的 `10` 条 `perturbed` run 做 paired manual audit。
2. 生成 v2 的 `mechanical_reuse` headline。
3. 统计 v2 的 retrieval usage：
   - attempted
   - successful
   - failed
4. 对每个 case 评估 retrieval 的作用：
   - helpful
   - neutral
   - noisy
   - failed
5. 汇总 v1 vs v2 的差异。
6. 给出是否继续进入 v3 的明确判断。

## 具体执行方法

### Step 1. 手审 paired audit

沿用 v1 的 paired narrative 口径，不改定义：

- `yes`：broken condition 后仍保留 base estimand / base identification logic
- `no`：明确降格、换 estimand、或承认因果识别不成立

新建：

- `results/perturbed_mechanical_reuse_v2.csv`
- `results/perturbed_pair_audit_v2.md`

### Step 2. 统计 retrieval 行为

不要只看“工具开着没”，要看：

- 是否真的尝试
- 是否真的成功
- 成功后是否被 Stage 5 用上

最少报告：

- `retrieval_attempt_rate`
- `retrieval_success_rate`
- `cases_with_zero_actual_tool_use`

### Step 3. 做 retrieval usefulness audit

建议每个 case 额外打一个标签：

- `helpful`
- `neutral`
- `noisy`
- `failed`

判定标准应写进方法说明中，不要边看边改。

### Step 4. 生成对比写作

至少回答这四件事：

1. v2 是否比 v1 进一步降低 `mechanical_reuse`
2. 如果有改善，改善集中在哪类 case
3. retrieval 是否真实被使用
4. retrieval 是否值得进入后续 v3 基线

### Step 5. 给出 go / no-go 判断

在本 task 末尾要有一个明确结论：

- `go to v3`
- `stop at v2`
- `revise v2 first`

不要把 v3 默认当成必做。

## 建议产物

- `results/perturbed_mechanical_reuse_v2.csv`
- `results/perturbed_pair_audit_v2.md`
- `results/research_agent_v2_vs_v1.md`
- `results/retrieval_usefulness_audit.csv`
- `results/retrieval_usefulness_summary.md`

## 验收标准

- [x] v2 的 paired manual audit 已完成。
- [x] v2 的 `mechanical_reuse` headline 已给出。
- [x] v2 的 retrieval attempt / success / failure 已统计。
- [x] 每个 case 的 retrieval usefulness 已分类。
- [x] 已写出 v1 vs v2 的结果对比说明。
- [x] 已给出是否继续进入 v3 的明确建议。
- [x] 所有新增或更新文件通过 `git diff --check`。

## 常见风险

- 只看自动 metrics，不做人审 paired audit。
- 把“发生了工具调用”误当作“retrieval 有帮助”。
- retrieval rate 很高，但最终 memo 没变化，却仍夸大 v2 的价值。
- 没有给出 go / no-go 结论，导致 v3 变成惯性扩展。

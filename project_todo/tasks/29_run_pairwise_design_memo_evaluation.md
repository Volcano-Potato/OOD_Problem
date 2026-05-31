# Task 29: 增加 APE-style pairwise design-memo evaluation

## 目标

借鉴 Project APE 的 `head-to-head` 评估逻辑，为本项目增加一层更容易解释的相对比较结果：

- published paper design logic
- vs
- OpenClaw agent design logic

但比较对象不是 full paper，而是 **matched design memos**。

本 task 的目标是生成一个结果，回答：

> 在匿名化、统一格式、固定 judge 的条件下，agent 的设计方案在多少个 case 上整体上仍不如真实论文的设计逻辑？

## 为什么现在需要做

当前项目已经有：

- claim-level metrics
- adjudication
- failure taxonomy

这些足以说明 agent “错在哪”。
但还缺一个更直观的对外结果：

- “整体上它的设计方案是否输给真实论文方案？”

APE 最值得借的点正是这一层：

- fixed judge
- pairwise comparison
- relative evaluation instead of only absolute scoring

如果做得干净，这会是最强的额外 headline 之一。

## 输入

- `benchmark/cases/*/gold_reference.md`
- `benchmark/cases/*/agent_task_level2.md`
- `outputs/raw_agent_logs/main/*level2*.md`
- `report/bottleneck_ape_leverage_plan.md`
- APE methodology notes

## 需要做什么

1. 选定 pairwise 评估子集。
2. 为每个 case 生成两份 matched design memo：
   - published-design memo
   - agent-design memo
3. 固定一个 judge model 和一个 judge prompt。
4. 对每个 case 随机化 A/B 顺序。
5. 让 judge 在固定标准下做 pairwise choice。
6. 汇总：
   - win/loss/tie
   - optional subtype breakdown
7. 写结果说明与局限性。

## 为什么比较 design memo 而不是 full paper

本项目当前真正想比较的是：

- causal-design reasoning quality

而不是：

- full paper writing
- figure quality
- exposition

因此，若直接比较 full paper，会把太多无关噪声带进来，也会让本项目看起来像在拙劣复刻 APE。

## 具体执行方法

### Step 1. 选子集

推荐优先：

- 10 个 `level2` main cases

因为：

- `level2` 最适合作为“主要设计能力”比较层
- `level3` 受额外 hints 影响
- `perturbed` / `no_solution` 更像挑战集，可留作第二阶段

### Step 2. 构造 matched design memo

每个 case 生成两份 结构对齐、长度接近 的设计 memo：

- research question
- treatment / exposure
- outcome
- identification source
- key assumptions
- main limitation

其中：

- published-design memo 从 `gold_reference` 和 source materials 抽取
- agent-design memo 从 `level2` 原始输出抽取

禁止在 memo 中泄漏论文标题、作者、年份、地理位置等 source identity。

### Step 3. 固定 judge protocol

必须固定：

- judge model
- prompt
- temperature
- output format

推荐输出：

- winner: `A/B/tie`
- reason
- scores on:
  - identification credibility
  - mechanism adequacy
  - defensibility under available evidence

### Step 4. 随机化顺序

每个 case 至少记录：

- which memo is A
- which memo is B
- randomized order seed or deterministic rule

如时间允许，可做 swapped-order double judgment；如时间有限，至少要保存随机化规则。

### Step 5. 汇总结果

至少报告：

- `agent loses X/Y`
- `agent wins X/Y`
- `ties`

可选再分：

- by domain
- by failure-heavy versus cleaner cases

## 建议产物

- `benchmark/prompts/pairwise_design_judge_prompt.md`
- `outputs/pairwise_design_memos/`
- `results/pairwise_design_memo_eval.csv`
- `results/pairwise_design_memo_eval.md`
- 如脚本化：
  - `scripts/build_pairwise_design_memos.py`
  - `scripts/run_pairwise_design_eval.py`

## 验收标准

- [x] 已选定固定 pairwise 评估子集。
- [x] 每个 case 已生成 published-design memo 与 agent-design memo。
- [x] judge model、prompt 和输出格式已固定。
- [x] A/B 顺序随机化规则已记录。
- [x] 已生成结构化 pairwise 结果表。
- [x] 已给出总体结果与谨慎解释。
- [x] 已明确说明该层评估比较的是 design memo，而不是 full paper。
- [x] 所有修改通过 `git diff --check`。

## 常见风险

- 直接拿 full paper 比 full paper，偏离本项目焦点。
- judge prompt 不固定，导致结果不可解释。
- design memo 长度和信息密度差太大，比较不公平。
- published-design memo 写成“标准答案”，而不是“同格式设计摘要”。

## 完成记录

- 已新增 judge prompt：
  - `benchmark/prompts/pairwise_design_judge_prompt.md`
- 已新增 memo 构建脚本：
  - `scripts/build_pairwise_design_memos.py`
- 已新增 pairwise 运行脚本：
  - `scripts/run_pairwise_design_eval.py`
- 已生成 memo 对：
  - `outputs/pairwise_design_memos/`
- 已生成结构化结果：
  - `results/pairwise_design_memo_eval.csv`
  - `results/pairwise_design_memo_eval.md`

## 本轮 protocol 设置

- subset: 全部 `10` 个 main-set `level2` cases
- unit of comparison: matched anonymized design memos
- fixed judge model: `deepseek-v4-pro`
- A/B order: deterministic per-case randomization from hashed `case_id`

## 本轮结果摘要

- agent loses to published design memo: `0/10`
- agent wins: `10/10`
- ties: `0/10`

维度级结果：

- identification winner = published memo in `0/10`
- mechanism winner = published memo in `1/10`
- defensibility winner = pulished memo in `0/10`

## 结果解释

这一结果与主 benchmark 的 claim-level adjudication 和 failure-case analysis 不一致，因此本 task 的结论不是“agent 真的整体上优于 published design logic”，而是：

- APE-style pairwise design-memo layer 已成功落地为一个可复跑 extension
- 但在当前 protocol 下，它明显受到 memo compression 与 same-family judge 的影响
- 因此该层结果应视为 exploratory artifact，而不是主 headline

当前最合理的解释是：

- agent memo 往往更显式地写出 assumptions、bounds 和 caution
- published memo 是从 evaluator materials 压缩出来的 matched summary
- fixed judge 会奖励“显式 defensibility”，从而高估 agent memo 的相对表现
- 最后一次重跑从 `9/10 + 1 tie` 进一步漂移到 `10/10`，说明这一层对 memo construction 和 fixed-judge protocol 很敏感

## 当前使用建议

- 可保留此层作为方法扩展示例
- 不建议把 `9/10 agent wins` 写成主结论
- 如果未来要继续推进这一层，应优先改进：
  - cross-family judge
  - stronger published-memo construction
  - possibly swapped-order double judgment

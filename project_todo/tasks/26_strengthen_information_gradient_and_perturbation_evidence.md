# Task 26: 补强信息梯度、扰动复用证据与结果措辞

## 目标

在不扩 benchmark 范围、不新增 case family、不重做标注体系的前提下，补齐当前主结果里最容易在答辩中被追问的三个缺口：

1. 补跑 `level1`，把信息梯度从 `level2 -> level3` 扩成 `level1 -> level2 -> level3`。
2. 给 `perturbed` 增加逐 case 配对审计，产出 `X/10 mechanical reuse`。
3. 收掉 README、report 和 metrics summary 中与 benchmark 主题相冲突的 overclaim 措辞。

本 task 的定位是 “主结果补强补丁”，不是新一轮 benchmark 扩容。

## 为什么现在需要做

当前主结果已经完整，但还有三个结构性短板：

1. **信息梯度缺一层。**
   现在正式矩阵没有 `level1`，因此无法严肃回答“从弱信息到强信息，额外信息究竟有没有帮助”。
2. **`perturbed` 只有均值下降，没有配对行为证据。**
   目前只能说 “变差了”，但还不能把 RQ5 直接写成 “在多少个 case 上机械复用了 base design”。
3. **部分对外表述仍然过强。**
   尤其是 `No-solution Honesty Rate = 1.0000` 和对 `level3 > level2` 的暗示，如果不收口，会与 benchmark 自己批评的 overclaim 问题冲突。

因此，这个 task 的任务不是继续扩 benchmark，而是把已有结果变得更可 defended。

## 不需要做什么

- 不新增 case，不扩到 11 篇或更多。
- 不重做 `task20-21` 的整套标注规则。
- 不做第三轮标注。
- 不换 agent，也不加 cross-model 对比。
- 不默认把 `no_solution` 从 4 个扩到 10 个；这可作为时间富余时的可选 extension。

## 输入

- 当前 10-case main set
- 已完成的 `task18-24` 产物
- `benchmark_isolated` 运行 pipeline
- `outputs/run_manifest.csv`
- `outputs/raw_agent_logs/main/`
- `outputs/parsed_claims/claims_to_annotate.csv`
- `annotations/annotation_sheet.csv`
- `annotations/second_labels.csv`
- `annotations/adjudicated_labels.csv`
- `results/metrics_summary.*`
- `report/research_report.md`
- `README.md`

## 需要做什么

### Part A. 把 `level1` 补进正式主矩阵

1. 为 10 个 main-set cases 新建一个 `level1` main-run batch spec。
2. 用现有 `benchmark_isolated` + batch runner 跑完 10 条 `level1` run。
3. 把新增 run 追加到：
   - `outputs/raw_agent_logs/main/`
   - `outputs/run_manifest.csv`
4. 对新增 `level1` 输出重复主链路：
   - claim extraction
   - first-pass annotation
   - second labeling sample extension if needed
   - adjudication
   - metrics recomputation
5. 重画信息梯度图，使其显式比较：
   - `level1`
   - `level2`
   - `level3`

### Part B. 给 `perturbed` 增加逐 case 配对审计

1. 对 10 个 main-set cases，逐对比较：
   - `level2` 输出
   - `perturbed` 输出
2. 对每个 case 记录：
   - key identifying condition broken in `perturbed`
   - agent 是否明确重算 estimand / design
   - agent 是否继续沿用 base-case logic
   - `mechanical_reuse = yes/no`
3. 输出至少一个结构化产物：
   - `results/perturbed_mechanical_reuse.csv`
   - 和/或 `results/perturbed_pair_audit.md`
4. 最终汇总一个 headline 数：
   - `X/10 perturbed cases show mechanical reuse under broken identification`

### Part C. 收口过强措辞

1. 在 `README.md` 中改写：
   - `No-solution Honesty Rate`
   - `level3 vs level2` 的结论措辞
2. 在 `report/research_report.md` 中同步改写。
3. 在 `results/metrics_summary.md` 中补上样本量和谨慎解释。

## 建议产物

- `benchmark/run_configs/main_run_level1_batch_spec.csv`
- `results/perturbed_mechanical_reuse.csv`
- `results/perturbed_pair_audit.md`
- 更新后的：
  - `outputs/run_manifest.csv`
  - `outputs/parsed_claims/claims_to_annotate.csv`
  - `annotations/annotation_sheet.csv`
  - `annotations/second_labels.csv`
  - `annotations/adjudicated_labels.csv`
  - `results/metrics_summary.csv`
  - `results/metrics_summary.md`
  - `results/grouped_metrics.csv`
  - `results/figures/information_gradient_scores.csv`
  - `results/figures/information_gradient_scores.svg`
  - `README.md`
  - `report/research_report.md`

## 具体执行方法

### A. `level1` 补跑与重算

1. 先冻结 `level1` main-run case list，不边跑边改。
2. 生成单独 batch spec，不直接覆写原 `main_run_batch_spec.csv`。
3. 跑完 10 条后，先检查：
   - 是否全部落盘
   - 是否有 `aborted`
   - 是否需要补跑
4. 只对新增 `level1` runs 抽 claims。
5. 只对新增 `level1` claims 做 first-pass 标注。
6. 将 second-label sample 扩展到包含 `level1`，但不必重做全部旧 claim。
7. 重生成 adjudicated labels。
8. 再重算 metrics 和 figure。

### B. `perturbed` 配对审计

1. 先定义固定判定规则，不要边看边改。
2. 每个 case 只回答一个核心问题：
   - `perturbed` 的关键条件失效后，agent 有没有真正重新设计？
3. 推荐二元规则：
   - `yes`：仍沿用 base estimand、base identification logic、或只做表面 threat 复述
   - `no`：明确降格、改 estimand、或改识别设计以适应 broken condition
4. 配对审计结果应能被后续引用到：
   - `README`
   - `report`
   - `failure_cases`

### C. 措辞修订

1. 不删除指标本身，只收紧它的解释。
2. `No-solution Honesty Rate` 至少要显式写出：
   - tested cases count
   - heuristic boundary
3. `level3 vs level2` 不得再被表述为“更好”，除非重算后差异明显且有充分支持。

## 判定规则建议

### `mechanical_reuse`

- `yes`
  - `perturbed` note 已说明关键 identifying condition 被拿掉或改坏
  - agent 仍直接保留 base estimand / base identifying contrast / base causal claim
- `no`
  - agent 明确缩小 claim
  - 改成更弱 estimand
  - 或承认因果识别不再成立，只保留 descriptive / reduced-form 解释

### `information_gradient`

补跑 `level1` 后，只允许三类解释：

1. `level1 < level2 ≈ level3`
   - 说明结构化数据信息有帮助，但显式 threat hints 帮助有限
2. `level1 ≈ level2 ≈ level3`
   - 说明额外信息总体没有带来实质提升，更像能力天花板或模板化推理
3. `level1 < level2 < level3`
   - 说明更详细威胁提示确实帮助 agent 生成更稳健设计

不要提前假定结果一定支持其中某一个。

## 与现有 task 的关系

- 依赖 `task18-24`
  - 因为这不是新 benchmark，而是对既有主结果的补强
- 部分复用 `task18-22`
  - 重新运行 `level1`
  - 重新走 extraction / annotation / adjudication / metrics
- 可回写 `task24`
  - 因为最终对外叙事需要同步更新

## 验收标准

- [x] 10 个 main-set cases 的 `level1` 均已正式运行并落盘。
- [x] 新增 `level1` runs 已完成 claim extraction。
- [x] 新增 `level1` claims 已纳入 annotation、second-label sample 和 adjudication。
- [x] 信息梯度图已更新为 `level1 -> level2 -> level3`。
- [x] 已产出 `perturbed` 的逐 case 配对审计结果。
- [x] 已给出明确 headline 数：`X/10 mechanical reuse`。
- [x] `README.md`、`report/research_report.md`、`results/metrics_summary.md` 中的相关 overclaim 措辞已收口。
- [x] 所有新增或更新文件通过 `git diff --check`。

## 可选 extension

以下内容不属于本 task 的必须范围，但如果时间富余可继续做：

- `RQ1` 的威胁识别命中率量化
- 将 `no_solution` 从 4 条扩到 10 条
- 对更隐蔽的 `no_solution` 再做一次 stress test

## 常见风险

- 只跑了 `level1`，但没把它接入 annotation 和 metrics，导致信息梯度仍不可比。
- `perturbed` 配对审计只写文字，没有给出统一计数规则。
- 把 `mechanical_reuse` 和 “单纯分数下降” 混为一谈。
- README 改了，但 report 和 metrics summary 没同步，导致口径分裂。
- 看到 `level1` 结果后临时修改解释规则，造成 post hoc 叙事。

## 完成后应该发生什么

完成本 task 后，这个 benchmark 的对外主张应变成：

1. 信息梯度是完整的，而不是缺 `level1` 的半截结论。
2. `perturbed` 不再只是“均值下降”，而是能回答“多少 case 出现机械复用”。
3. 仓库首页、研究报告和结果摘要中的措辞，与 benchmark 自己对 overclaim 的标准保持一致。

## 完成记录

本轮已完成：

- 新建 `benchmark/run_configs/main_run_level1_batch_spec.csv`
- 用 `benchmark_isolated` 跑完 10 条 `level1` main runs，全部 `success`
- 新建 `results/perturbed_mechanical_reuse.csv`
- 新建 `results/perturbed_pair_audit.md`
- 更新 `scripts/build_second_labels_and_adjudication.py`，确保 second-pass sample 覆盖 `level1`
- 更新 `scripts/compute_benchmark_metrics.py`，将 `level1` 与 `perturbed` 配对审计接入指标层
- 更新 `README.md`
- 更新 `report/research_report.md`

本轮结果摘要：

- `level1` success runs: `10/10`
- successful annotated main runs: `44`
- total adjudicated claims: `370`
- `level1` mean run score: `0.6902`
- `level2` mean run score: `0.8363`
- `level3` mean run score: `0.8421`
- `perturbed` mechanical reuse: `9/10`
- `no_solution` honesty应读作 `4/4 tested runs`，而不是无条件总体结论

# Task 28: 构建 Bottleneck execution-dimension crosswalk

## 目标

把 Bottleneck 里的 execution dimensions 和本项目已有 benchmark 证据建立一个清晰的映射表，让读者能够直接看懂：

- Bottleneck 讲的 execution gap
- 在这个 benchmark 中分别落成了哪些可测 failure channels

本 task 的任务是 **建立理论映射与解释表**，不是新增实验。

## 为什么现在需要做

当前项目已经有很多指标：

- `Mean Claim Score`
- `Design-Evidence Inconsistency Rate`
- `Overclaim Rate`
- `Mechanism Confounding Rate`
- `Perturbed Mechanical Reuse Rate`
- `Level 1/2/3 Mean Run Score`

但这些指标目前主要是 benchmark 内部语言。
如果不和 Bottleneck 的 execution 维度对齐，读者很难快速理解：

- 哪些指标对应 identification
- 哪些指标对应 mechanism
- 哪些指标只是辅助项
- 为什么 robustness/writing 不是你的主发现

因此，需要一个 crosswalk，把 “你测了什么” 重新翻译成 “它对应 execution 的哪一部分”。

## 输入

- `The Ideation Bottleneck.pdf`
- `report/research_report.md`
- `results/metrics_summary.md`
- `results/failure_cases.md`
- `report/bottleneck_ape_leverage_plan.md`

## 需要做什么

1. 提炼 Bottleneck 的 execution dimensions。
2. 为每个 dimension 找到本项目中最直接的 observable evidence。
3. 标记哪些是：
   - core evidence
   - partial proxy
   - out of scope
4. 写一段解释，说明为什么本项目重点聚焦：
   - identification
   - mechanism
   - anti-anchoring / claim calibration
5. 将 crosswalk 融入报告或 results summary。

## 具体执行方法

1. 用一个 3 列或 4 列表格完成映射：
   - Bottleneck dimension
   - benchmark observable
   - representative metric / artifact
   - interpretation note
2. 明确区分：
   - direct measurement
   - proxy measurement
3. 不要试图硬凑每个 dimension 都有同等强度证据。
4. 对 `Robustness` 和 `Writing`，如果在本项目中只属次要内容，应明确标成 secondary / out of scope。
5. 在报告正文中用一句话解释：
   - 这个 benchmark intentionally prioritizes the dimensions where execution failures are most consequential for causal credibility.

## 建议产物

- 新增：
  - `results/bottleneck_crosswalk.md`
- 更新：
  - `report/research_report.md`
  - `results/metrics_summary.md`

## 建议表格结构

| Bottleneck execution dimension | Benchmark evidence | Representative metric / artifact | Scope note |
|---|---|---|---|
| Identification | Level comparison, perturbed, no-solution | `Level 1/2/3 scores`, `mechanical reuse` | core |
| Econometrics | unsupported/contradicted design claims | claim-level labels | partial |
| Mechanism | mechanism confounding, overclaim | `Mechanism Confounding Rate`, failure cases | core |
| Data quality | misuse of dirty outcomes / missing untreated benchmarks | selected failure cases | partial |
| Robustness | limited direct focus | selected claims only | secondary |
| Writing | contract adherence only | format compliance | out of scope |

## 验收标准

- [x] 已生成一份明确的 crosswalk 文档。
- [x] 每个 Bottleneck execution dimension 都有对应说明。
- [x] 已区分 direct evidence 与 proxy evidence。
- [x] 报告或结果摘要中已引用该 crosswalk。
- [x] 没有把本项目没有真正测到的维度写成强结论。
- [x] 所有修改通过 `git diff --check`。

## 常见风险

- 只是把两个体系并列摆放，没有解释映射逻辑。
- 为了“对齐完整”，把弱 proxy 写成强 measurement。
- 忘记说明本 benchmark 的核心焦点是 identification 和 mechanism，而不是六维平均覆盖。

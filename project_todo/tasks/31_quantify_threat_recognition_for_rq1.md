# Task 31: 为 RQ1 增加 threat-recognition 量化

## 目标

把当前对 RQ1 的回答从：

- 主要依赖 failure family 的定性解释

补强为：

- 一个轻量但可报告的 threat-recognition quantitative audit

核心问题是：

> 对每个 case 的核心 causal threats，agent 在 `level2` 输出里识别到了几个？

## 为什么这是加分项

目前项目对 RQ1 的回答主要是：

- 从失败案例和错误率反推 agent 识别 threat 的能力

这不是错，但还不够直接。
最省成本的量化补强就是：

- 每个 case 预定义 2 个核心 threats
- 看 agent 是否在 `level2` 里明确点中

这样就能多一个很直观的结果：

- `0/2`
- `1/2`
- `2/2`

## 输入

- `benchmark/cases/*/gold_reference.md`
- `outputs/raw_agent_logs/main/*level2*.md`
- `results/failure_cases.md`
- `annotations/adjudicated_labels.csv`

## 需要做什么

1. 为每个 main-set case 选定 2 个核心 threats。
2. 固定“点中”的判定规则。
3. 对 10 个 `level2` outputs 做人工审计。
4. 记录每个 case 的：
   - `0/2`
   - `1/2`
   - `2/2`
5. 汇总总体 threat-recognition performance。

## 具体执行方法

1. threats 应来自 `gold_reference` 的核心识别命门，而不是临时发明。
2. “点中”要求：
   - agent 明确识别该 threat 的存在
   - 并在设计或限制部分有实际回应
3. 只做 `level2`，不要把 `level3` 混进来，因为 `level3` 已有显式 threat hints。
4. 汇总时至少报告：
   - average threat hits per case
   - number of `2/2`
   - number of `0/2`

## 建议产物

- `results/threat_recognition_audit.csv`
- `results/threat_recognition_summary.md`

## 验收标准

- [x] 10 个 main-set cases 都已定义 2 个核心 threats。
- [x] “点中”判定规则已写明。
- [x] 已完成 10 个 `level2` outputs 的 threat-recognition audit。
- [x] 已产出总体 summary。
- [x] 已明确说明这是一层轻量量化，而非完整新标注体系。
- [x] 所有修改通过 `git diff --check`。

## 常见风险

- threat 定义过宽，导致几乎所有输出都算“点中”。
- 只看 agent 有没有提 threat，不看它是否做了 design response。
- 把 `level3` 混入，污染 “自主 threat recognition” 的解释。

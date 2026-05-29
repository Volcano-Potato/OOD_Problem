# Task 21: 复标、分歧裁决与标签冻结

## 目标

提高人工标注可信度，避免结果完全依赖单人主观判断。

## 输入

- `annotation_sheet.csv`
- `annotation_guide.md`
- gold references

## 需要做什么

1. 抽样 20%-30% claims 给第二标注人复标。
2. 计算 simple agreement。
3. 列出 disagreement cases。
4. 对分歧进行裁决。
5. 更新最终标签。
6. 冻结 `adjudicated_labels.csv`。

## 具体执行方法

1. 用固定随机种子或按 case 分层抽样，选 20%-30% claims 复标。
2. 第二标注人只能看 agent-facing task、Agent 输出、gold reference 和 annotation guide，不能看第一标注人的 explanation。
3. 计算 simple agreement：相同 human_judgment 的比例、相同 error_type 的比例。
4. 对 disagreement 建表，不要口头解决。
5. 裁决时写明最终选择哪个标签以及理由。
6. 冻结后所有统计只使用 `adjudicated_labels.csv`。

## disagreement 表模板

```csv
claim_id,labeler1_judgment,labeler2_judgment,final_judgment,reason
```

## 产出

- `annotations/second_labels.csv`
- `annotations/adjudication_notes.md`
- `annotations/adjudicated_labels.csv`

## 验收标准

- [x] 至少 20% claims 有第二标注。
- [x] 报告 simple agreement。
- [x] 所有 high-severity disagreement 都有裁决说明。
- [x] `adjudicated_labels.csv` 是后续统计唯一数据源。

## 完成记录

- 第二标注样本由固定种子 `20260528` 抽取，并分层覆盖全部 10 个 case。
- 第二标注样本规模为 `78 / 370 = 21.1%`。
- 样本分布：
  - `level1`: `24`
  - `level2`: `19`
  - `level3`: `16`
  - `perturbed`: `15`
  - `no_solution`: `4`
- simple agreement：
  - `human_judgment`: `97.4%`
  - `error_type`: `97.4%`
- 共识别 `2` 条需要显式裁决的 disagreement。
- 最终冻结文件：
  - `annotations/second_labels.csv`
  - `annotations/adjudication_notes.md`
  - `annotations/adjudicated_labels.csv`
- `annotations/adjudicated_labels.csv` 已完整覆盖 `370` 条 main-run claims，后续 `task22-24` 与 `task26` 收尾都只应使用该文件。

## 常见风险

- 复标只做形式，没有真正比较分歧。
- 裁决时改标签但不记录原因。
- 统计脚本使用了未裁决版本。

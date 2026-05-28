# Task 19: 从 Agent 输出抽取 Claim

## 目标

把长篇 Agent 输出转成 claim-level 标注表，减少人工标注负担。

## 输入

- `outputs/raw_agent_logs/main/`
- Agent 的 Claim-Evidence Table

## 需要做什么

1. 为每个 run 抽取关键 claim。
2. 拆分复合 claim。
3. 保留 Agent 原文片段。
4. 记录 cited evidence。
5. 标记 claim_type。
6. 输出待标注 CSV。

## 具体执行方法

1. 优先使用 Agent 自己输出的 Claim-Evidence Table。
2. 如果表格缺失，人工或强模型从正文中抽取 claim，但必须保留原文 quote。
3. 一个 claim 只能表达一个判断；复合句要拆开。
4. 因果、机制、识别、假设、模型、robustness、限制性表述都要抽。
5. 不要在本任务判断对错；只做结构化抽取。
6. 每个 claim_id 使用稳定格式：`<run_id>_CL001`。

## 拆分示例

原句：

```text
Because treatment is random, OLS with controls identifies the causal effect and can test the mechanism.
```

拆成：

```text
CL001: Treatment is random.
CL002: OLS with controls identifies the causal effect.
CL003: The design can test the mechanism.
```

## 产出

- `outputs/parsed_claims/claims_to_annotate.csv`
- `outputs/parsed_claims/claim_extraction_skipped.csv`
- `outputs/parsed_claims/claim_extraction_summary.md`
- `scripts/extract_agent_claims.py`

## 推荐字段

```csv
case_id,variant_id,level,run_id,claim_id,claim_type,agent_claim,cited_evidence,verbatim_quote,notes
```

## Claim types

- research_question
- treatment_outcome_unit
- identification_strategy
- assumption
- statistical_model
- robustness_check
- mechanism
- limitation
- additional_data

## 验收标准

- [x] 每个 run 至少抽取 5 个关键 claim，除非输出极短且说明原因。
- [x] 所有因果识别和机制 claim 必须被抽取。
- [x] claim_id 唯一且稳定。
- [x] 不在本任务判断 claim 对错，只抽取。

## 常见风险

- 只抽取 conclusion，漏掉 assumptions 和 model claims。
- 一个 claim 包含多个判断，导致后续无法标注。
- 没有保留原文，人工复查困难。

## 完成记录

### 本轮实现

- 新增 `scripts/extract_agent_claims.py`，从 `outputs/run_manifest.csv` 中筛选 `status=success` 且 `raw_output_file` 位于 `outputs/raw_agent_logs/main/` 的正式 main runs。
- 抽取逻辑优先使用 Agent 输出中的 `Claim-Evidence Table`，支持两种表头变体：
  - `| # | Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |`
  - `| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |`
- 为每条 claim 生成稳定 `claim_id`：`<run_id>_CL001`。
- 额外保留了：
  - `confidence`
  - `what_would_falsify_this_claim`
  - `raw_output_file`
  - `source_section`
  便于 Task 20 和 Task 23 复查。

### 本轮结果

- 成功 main runs processed: `34`
- runs with extracted claim tables: `34`
- skipped runs: `0`
- total extracted claims: `285`
- min claims per run: `6`
- max claims per run: `11`

### 说明

- 历史上 `C001 perturbed` 和 `C001 no_solution` 的两条 aborted records 没有进入本轮 claim extraction；Task 18 中的成功补跑版本已覆盖这两个 case-variant。
- 本任务只做结构化抽取，不在 CSV 中写 judgment、error_type 或 severity；这些留给 Task 20。

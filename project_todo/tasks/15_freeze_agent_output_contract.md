# Task 15: 冻结 Agent 统一输出合同

## 目标

统一所有 case 的 Agent 输出格式，降低后续 claim extraction 和人工标注成本。

## 输入

- `data_idea.md` 中的 Required Output
- Level 1/2/3 task drafts

## 需要做什么

1. 写统一 task rule。
2. 写统一 Required Output。
3. 强制输出 Research Question、Estimand、Treatment、Outcome、Design、Assumptions、Model、Checks、Failure Modes、What Cannot Be Claimed。
4. 强制输出 Claim-Evidence Table。
5. 加入 no-solution 约束：不能强因果识别时必须承认。
6. 决定输出语言：建议英文，方便表格和后续自动抽取；报告可翻译中文。

## 具体执行方法

1. 从 `data_idea.md` 的任务模板复制 Required Output，但压缩成 Agent 能稳定遵守的版本。
2. 把 Task Rule 写成固定块，所有 Level 和 variant 都复用。
3. Claim-Evidence Table 必须固定列名，后续 claim extraction 依赖这些列。
4. 加入强约束：如果不能因果识别，不得编造识别策略。
5. 在一个 pilot task 上测试输出合同是否太长；如果 Agent 经常漏表格，缩短说明但保留表格。

## 输出合同必须包含

```markdown
## Required Output
1. Research question
2. Estimand
3. Treatment and outcome
4. Main identification challenge
5. Proposed empirical design
6. Why the design is valid
7. Required assumptions
8. Statistical model
9. Robustness/placebo checks
10. Heterogeneity analysis
11. Failure modes
12. What cannot be claimed
13. Additional data needed
14. Claim-evidence table
```

## Claim-Evidence Table 固定列

```markdown
| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
```

## 产出

- `benchmark/prompts/closed_book_design_prompt.md`
- `benchmark/prompts/evidence_aware_output_contract.md`

## 验收标准

- [ ] 所有 case 使用同一输出合同。
- [ ] Claim-Evidence Table 有固定列。
- [ ] 明确禁止联网、搜索原论文、使用外部文献。
- [ ] 明确要求区分 causal claims 和 descriptive claims。

## 常见风险

- 输出合同太长，Agent 忽略核心任务。
- 每个 case 的 prompt 格式不同，导致结果不可比。
- 没有要求 evidence id，后续标注困难。

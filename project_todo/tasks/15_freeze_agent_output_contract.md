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
1. Executive summary
2. Research question
3. Target estimand or strongest defensible estimand
4. Treatment or exposure and main outcomes
5. Data structure summary
6. Relevant causal mechanisms
7. Main identification challenge
8. Whether credible causal identification is possible
9. Proposed empirical design or strongest defensible descriptive analysis
10. Why the design is valid or why causal identification is not credible
11. Required assumptions
12. Statistical model or analysis equation
13. Robustness, placebo, falsification checks, or diagnostic tests
14. Heterogeneity analysis if supportable
15. Measurement, compliance, missingness, spillover, or implementation limits
16. Failure modes and alternative explanations
17. What cannot be claimed
18. Additional data needed
19. Threat-response table if explicitly requested by the task packet
20. Claim-evidence table
```

## Claim-Evidence Table 固定列

```markdown
| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
```

## 产出

- `benchmark/prompts/closed_book_design_prompt.md`
- `benchmark/prompts/evidence_aware_output_contract.md`

## 完成记录

本轮已完成：

- 新建 `benchmark/prompts/closed_book_design_prompt.md`
- 新建 `benchmark/prompts/evidence_aware_output_contract.md`
- 更新 `benchmark/prompts/README.md`

冻结决定如下：

- 所有 agent-facing benchmark output contract 统一使用英文。
- 所有 variant 统一共享同一套 packet-grounded `Task Rule`。
- 所有 variant 统一共享同一套 evidence-aware `Required Output`。
- `no_solution` 不再使用单独的缩短版输出结构，而是在统一合同下明确回答 “Whether credible causal identification is possible”。
- `Claim-Evidence Table` 固定列名不变：`Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim`。
- `Evidence Used` 必须优先引用 task packet 内部证据来源，并与一般方法论推理区分开。

本轮还将现有 `agent_task_*.md` 的 `Required Output` 对齐到统一合同，避免 pilot run 前出现不同 level / variant 之间的格式漂移。

## 验收标准

- [x] 所有 case 使用同一输出合同。
- [x] Claim-Evidence Table 有固定列。
- [x] 明确要求以 task packet 为主要证据来源，而不是把外部信息混入成未说明的 case 事实。
- [x] 明确要求区分 causal claims 和 descriptive claims。

## 常见风险

- 输出合同太长，Agent 忽略核心任务。
- 每个 case 的 prompt 格式不同，导致结果不可比。
- 没有要求 evidence id，后续标注困难。

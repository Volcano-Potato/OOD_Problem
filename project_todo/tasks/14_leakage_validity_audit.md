# Task 14: 匿名化、泄漏与有效性审计

## 目标

确保 agent-facing task 不泄漏原论文身份、不暗含答案，同时仍然有足够信息支撑研究设计评估。

## 输入

- `agent_task_level1.md`
- `agent_task_level2.md`
- `agent_task_level3.md`
- `perturbed_variant.md`
- `no_solution_variant.md`
- `gold_reference.md`

## 需要做什么

1. 检查题名、作者、机构、地点、年份、样本量是否已删除或模糊化。
2. 检查是否保留原文独特短语。
3. 检查 Level 2 是否有足够数据结构但不泄漏方法答案。
4. 检查 Level 3 是否提示威胁但不泄漏解法。
5. 检查 perturbed variant 是否只改一个条件。
6. 检查 no-solution 是否真的没有隐藏强识别来源。
7. 给出 approve / revise / reject。

## 怎么构造审计

审计可以由强模型/Codex 辅助，但建议使用和生成任务包不同的会话，避免同一个模型为自己生成的内容辩护。人工最后只需要看审计结论和 high-risk 项。

## 审计清单

### 1. Identity leakage

- 是否出现原论文题名、作者、机构、真实地名、真实项目名？
- 是否保留原文独特短语？
- 是否保留精确样本量、年份和地点组合，导致可搜索？
- 是否场景太独特，模型可能靠记忆识别论文？

### 2. Solution leakage

- Level 2 是否直接说出了原论文识别方法？
- Level 3 是否把威胁的解决方式写出来了？
- 任务文本是否暗示“应该使用某特定方法”？
- Institutional Details 是否直接包含 linchpin solution？

### 3. Validity

- Level 1 是否还能理解研究问题？
- Level 2 是否足以判断可行识别方向？
- Level 3 是否只是增加威胁提示，而不是答案？
- Perturbed variant 是否只改一个主要条件？
- No-solution variant 是否真的没有强因果识别来源？

## 审计输出模板

```markdown
# Audit

## Identity Leakage
- risk_level:
- issues:
- fixes:

## Solution Leakage
- risk_level:
- issues:
- fixes:

## Validity
- level1_status:
- level2_status:
- level3_status:
- perturbed_status:
- no_solution_status:

## Final Decision
approve / revise / reject
```

## 产出

- `audit.md`
- 更新 `metadata.yaml` 中的 `leakage_risk` 和 `audit_decision`

## 完成记录

Pilot set 已完成：

- `benchmark/cases/C001_charitable_giving/audit.md`
- `benchmark/cases/C001_charitable_giving/metadata.yaml`
- `benchmark/cases/C002_consumer_credit/audit.md`
- `benchmark/cases/C002_consumer_credit/metadata.yaml`
- `benchmark/cases/C005_online_ad_measurement/audit.md`
- `benchmark/cases/C005_online_ad_measurement/metadata.yaml`
- `benchmark/cases/C008_retail_tax_salience/audit.md`
- `benchmark/cases/C008_retail_tax_salience/metadata.yaml`
- `benchmark/cases/C014_corruption_monitoring/audit.md`
- `benchmark/cases/C014_corruption_monitoring/metadata.yaml`

本轮同时升级了 `C000_template/audit.md`，让后续 case 可以直接复用 `Identity Leakage / Solution Leakage / Validity / File Checklist / Final Decision` 结构，而不是只保留早期的 gold-reference 审计框架。

本次审计覆盖：

1. `agent_task_level1.md`
2. `agent_task_level2.md`
3. `agent_task_level3.md`
4. `agent_task_perturbed.md`
5. `agent_task_no_solution.md`
6. `perturbed_variant.md`
7. `no_solution_variant.md`
8. `gold_reference.md`

审计结论：

- 5 个 pilot case 的 agent-facing 文件均未发现高严重度 identity leakage。
- 5 个 pilot case 的 Level 2/Level 3 均未直接泄漏原论文题名、作者、地点、年份、样本量组合或 source-specific 方法名。
- 5 个 perturbed variant 都只改动一个关键 identification condition。
- 5 个 no-solution variant 都已显式移除可信强识别来源，同时仍保留现实研究价值和“诱导错误回归”的数据外观。
- `metadata.yaml` 已同步更新 `taxonomy.leakage_risk`、`audit.audit_decision`、各 variant 状态、以及审计完成时间。

未运行 OpenClaw。

## 验收标准

- [x] 所有 agent-facing 文件的 leakage risk 为 low 或有明确修订计划。
- [x] audit 中 high severity issue 必须修复。
- [x] 每个 variant 都有 evaluator-only expected response。
- [x] 审计者不需要读原论文全文，也能判断任务是否可评测。

## 常见风险

- 只做身份泄漏检查，不做 solution leakage 检查。
- 为了匿名化删掉太多结构信息，使 Level 2 不可做。
- 没有记录修订历史。

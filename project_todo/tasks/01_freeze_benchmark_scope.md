# Task 01: 冻结 Benchmark Scope 与研究问题

## 目标

明确 OOD-CausalDesignBench 到底评估什么、不评估什么，防止后续 case 构建、prompt 设计和结果解释不断漂移。

## 输入

- `OOD_CausalDesignBench_pipeline_plan.md`
- `data_idea.md`
- `Bench_idea.md`

## 需要做什么

1. 写出 benchmark 的一句话定义。
2. 明确被测对象：OpenClaw / DeepScientist 搭建的科研 Agent。
3. 明确 OOD 场景：泛商科、经济学、营销学因果研究设计。
4. 明确被测能力：问题结构化、因果威胁识别、识别策略设计、证据边界意识。
5. 明确不测什么：不测原论文记忆、不测 literature review、不测写作流畅度、不测自由联网检索能力。
6. 定义核心失败：unsupported causal design claims。

## 具体执行方法

1. 从 `OOD_CausalDesignBench_pipeline_plan.md` 提取 benchmark 的核心对象：科研 Agent、商科/经济学 OOD、因果研究设计。
2. 用固定句式写一句话定义：`OOD-CausalDesignBench evaluates whether [agent] can [capability] in [OOD setting] without producing [failure].`
3. 把研究问题写成可被后续指标回答的问题，例如“Level 3 信息更充分时错误率是否下降？”。
4. 对每个 evaluated capability 写 operational definition，必须能对应后续标注或指标。
5. 对每个 out-of-scope 项写原因，防止后续讨论跑偏。
6. 最后检查：如果别人问“为什么这不是让 Agent 猜论文？”，`scope.md` 里应该已经有答案。

## 具体字段建议

```markdown
## One-sentence Definition

## Research Questions
- RQ1:
- RQ2:
- RQ3:

## Evaluated Capabilities
| capability | operational definition | later evidence |

## Out-of-Scope Capabilities
| excluded item | reason |

## Main Failure Modes
| failure mode | definition | example |
```

## 产出

- `benchmark/scope.md`

## 建议内容结构

```markdown
# Benchmark Scope

## One-sentence Definition

## Research Questions

## Evaluated Capabilities

## Out-of-Scope Capabilities

## Main Failure Modes

## Unit of Evaluation
```

## 验收标准

- [ ] 能用 1-2 句话解释 benchmark 的研究对象和研究问题。
- [ ] 明确写出至少 4 个 evaluated capabilities。
- [ ] 明确写出至少 4 个 out-of-scope 项，避免后续被质疑“为什么不测检索/写作/复现原论文”。
- [ ] 核心失败类型必须和后续标注体系一致：Unsupported Claim、Overclaim、Mis-citation、Contradiction。

## 常见风险

- 把 benchmark 写成“看 Agent 能不能猜中原论文方法”。
- 把任务范围扩大到所有商科研究能力，导致不可执行。
- 忘记声明 task packet、本地隔离边界与远程工具配置，导致后续无法解释 run 到底测的是哪种研究能力。

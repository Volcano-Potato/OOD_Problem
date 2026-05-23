# Task 06: 抽取 Source Facts

## 目标

把 source packet 转成结构化事实表，减少后续 gold reference 里混入模型臆测。

## 输入

- `source_packet.md`

## 需要做什么

1. 抽取研究背景。
2. 抽取研究问题。
3. 抽取数据结构。
4. 抽取 treatment / exposure / variation source。
5. 抽取 outcome 和 measurement method。
6. 抽取原论文识别策略。
7. 抽取 linchpin design details。
8. 抽取 robustness / placebo / mechanism checks。
9. 标记不确定或证据不足的点。

## 具体执行方法

1. 只从 `source_packet.md` 抽事实，不用论文名记忆或外部搜索补细节。
2. 每条 fact 只表达一个事实，避免一行里混合数据、方法和结论。
3. 每条 fact 都必须有 `evidence_id`，例如 `[P003]`。
4. 如果是评审者推断，放进 `Evaluator Inference`，不要混进 source fact。
5. Data structure 必须拆出 observation unit、assignment level、time structure、outcome measurement level。
6. Linchpin detail 必须写 `why_it_matters` 和 `what_fails_without_it`。
7. 不确定的信息写进 `Uncertainties`，后续 gold reference 不能把它当硬事实。

## Fact 表模板

```markdown
| fact_id | category | fact | evidence_id | confidence |
|---|---|---|---|---|
| F001 | data_structure | ... | P003 | high |
```

## 产出

- `source_facts.md`

## 完成范围

本轮已完成 frozen pilot set：`C001`、`C002`、`C005`、`C008`、`C014`。Main set 其余 case 可在 pilot 流程验证后按同一模板扩展。

## 建议结构

```markdown
# Source Facts

## Research Context
| fact_id | fact | evidence_id |

## Data Structure
| fact_id | observation_unit | time_span | variables | evidence_id |

## Treatment / Variation

## Outcomes

## Identification Logic

## Linchpin Details

## Uncertainties
```

## 验收标准

- [x] 每条 source fact 都有 evidence id。
- [x] 明确区分“论文明确说了”和“评审者推断”。
- [x] 至少识别 1 个 linchpin detail 或明确说明为什么没有。
- [x] 至少列出 2 个 naive design 可能失败的原因。

## 常见风险

- 把论文结论当作任务输入事实。
- 忽略 outcome measurement risk。
- 没有抽出 assignment mechanism，导致后续任务包不可评测。

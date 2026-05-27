# Task 07: 编写 Hidden Gold Reference

## 目标

为每个 case 写 evaluator-only 的隐藏答案，用于后续评分和错误归因。

## 输入

- `source_facts.md`
- `source_packet.md`

## 需要做什么

1. 写核心研究问题。
2. 写 treatment / exposure、outcome、unit、estimand。
3. 写数据结构和 assignment / variation source。
4. 写原论文识别逻辑。
5. 写 linchpin detail 及其作用。
6. 写可接受替代设计。
7. 写不可接受设计。
8. 写 scoring notes。

## 具体执行方法

1. 从 `source_facts.md` 复制必要事实，不要重新凭记忆概括论文。
2. `Original Identification Logic` 可以写原论文方法，但必须标记 evaluator-only。
3. `Must-Have Conditions` 写成“有效答案必须处理的问题”，不要写成“必须复现原论文方法”。
4. `Acceptable Alternative Designs` 至少写 2 个，并说明需要额外什么数据或干预。
5. `Common Invalid Designs` 模拟弱 Agent 可能输出的具体错误说法。
6. `Scoring Notes` 明确 critical omission、partial credit、automatic failure。

## Must-Have 写法示例

好的写法：

```markdown
- The design must address non-random exposure because exposure is related to prior purchase intent.
```

不好的写法：

```markdown
- The agent must use the exact original ghost ads method.
```

## 产出

- `gold_reference.md`

## 完成范围

本轮已完成 frozen pilot set：`C001`、`C002`、`C005`、`C008`、`C014`，并已新增完成 `C004`、`C010`、`C016`、`C019` 与 `C020`。Main set 其余 case 可在 pilot 流程验证后按同一模板扩展。

## 必须包含

- `Core Research Problem`
- `Data Structure`
- `Original Identification Logic`
- `Linchpin Detail`
- `Must-Have Conditions`
- `Acceptable Alternative Designs`
- `Common Invalid Designs`
- `Scoring Notes`

## 验收标准

- [x] 不要求 Agent 复现原论文，但明确有效答案必须满足哪些必要识别条件。
- [x] 至少列出 3 个 common invalid designs。
- [x] linchpin detail 写清楚“遗漏后会错在哪里”。
- [x] 可接受替代设计说明能支持什么 claim、不能支持什么 claim。

## 常见风险

- gold reference 写得太像原论文复述。
- 没有写可接受替代方案，评分会过于死板。
- 没有写 invalid designs，后续错误分类会随意。

# Task 10: 构造 Level 2 Data Card Task

## 目标

构造主测试层级：给 Agent 足够数据结构信息，让它有条件提出可辩护识别策略，但不直接告诉答案。

## 输入

- `gold_reference.md`
- `source_facts.md`
- `agent_task_level1.md`

## 需要做什么

1. 保留 Level 1 背景和研究目标。
2. 增加 Data Card。
3. 明确 observation unit、time span、sample construction。
4. 明确 treatment/exposure、outcome、covariates。
5. 明确 panel/repeated structure。
6. 明确 assignment or variation source，但不要命名为最终识别策略。
7. 增加 assignment level、outcome measurement level、clustering level。
8. 增加 compliance、missingness、spillover 信息。

## 怎么构造

Level 2 是主测试层级。可以让强模型/Codex 基于 `source_facts.md` 和 `gold_reference.md` 生成初稿，但必须人工检查。这里不是写“故事”，而是写清楚 Agent 判断识别策略所需的最小充分信息。

输入可以包含：

- `source_facts.md` 的 data structure、treatment/variation、outcomes、measurement risk。
- `gold_reference.md` 的 data structure 和 must-have conditions。

输入不应包含：

- original identification logic 的最终方法名称。
- linchpin detail 的解决方案表述。
- common invalid designs。

## Data Card 应写到什么粒度

| 模块 | 应该写什么 | 不应该写什么 |
|---|---|---|
| Unit of observation | individual / household / firm / store / product / region / time-period | 原论文真实样本名 |
| Time span | 前后几期、周度/月度/年度、是否有 pre-period | 精确年份如会泄漏论文 |
| Sample construction | 样本来自交易记录、调查、平台日志、政策数据等 | 独特机构名或地点名 |
| Treatment/exposure | X 是什么，如何被观察或分配 | “这是 RCT/DID/RDD 的处理” |
| Outcome | Y 是什么，如何测量 | 原论文独特变量名 |
| Covariates | 可用控制变量类别 | 过细导致可搜索的信息 |
| Panel/repeated structure | 是否重复观测、是否可用固定效应 | 直接告诉应使用哪种模型 |
| Assignment or variation source | 随机/准随机/政策/算法/自选择/市场结果 | 最终识别策略答案 |
| Assignment level | 处理在哪个层级分配 | 模糊到无法判断聚类 |
| Clustering/inference level | 合理推断层级 | 把个体样本量当独立观测 |
| Compliance/take-up | 是否 partial compliance | 忽略处理未达成 |
| Missingness/attrition | 是否有缺失或退出 | 只写“数据完整”但无依据 |
| Spillover/interference | 是否可能有外溢 | 无根据排除外溢 |

## 建议模板

```markdown
# Anonymous Research Design Task: Level 2

## Task Rule
[同 Level 1]

## Research Background
[继承 Level 1，可略微压缩]

## Research Objective

## Data Card
- Unit of observation:
- Time span:
- Sample construction:
- Treatment/exposure variable:
- Outcome variable:
- Covariates:
- Panel/repeated structure:
- Assignment or variation source:
- Assignment level:
- Outcome measurement level:
- Recommended clustering/inference level:
- Repeated exposure:
- Compliance/take-up:
- Missingness/attrition:
- Potential spillover/interference:

## Constraints

## Required Output
[统一输出合同 + Claim-Evidence Table]
```

## 产出

- `agent_task_level2.md`

## 完成记录

Pilot set 已完成：

- `benchmark/cases/C001_charitable_giving/agent_task_level2.md`
- `benchmark/cases/C002_consumer_credit/agent_task_level2.md`
- `benchmark/cases/C005_online_ad_measurement/agent_task_level2.md`
- `benchmark/cases/C008_retail_tax_salience/agent_task_level2.md`
- `benchmark/cases/C014_corruption_monitoring/agent_task_level2.md`

本轮构造的是 Level 2 Data Card 主测试任务包。每个文件保留 Level 1 的匿名研究背景和研究目标，并补充 16 个 Data Card 字段：observation unit、time span、sample construction、treatment/exposure、outcome、covariates、panel/repeated structure、assignment/variation source、assignment level、outcome measurement level、clustering/inference level、repeated exposure、compliance/take-up、missingness/attrition、spillover/interference 等。未运行 OpenClaw。

## 验收标准

- [x] 一个懂基本计量/实验设计的人读完后能提出至少一个合理方向。
- [x] 信息足以判断是否能做 RCT/DID/RDD/IV/event study 或只能描述性分析。
- [x] 没有直接提示“应该使用某某方法”。
- [x] Data Card 字段完整，不用读原论文也能理解数据结构。

## 常见风险

- 只给变量名，不给 assignment details。
- 给了 treatment 是随机的，但没说随机化层级。
- 忘记 outcome measurement risk，导致 Agent 过度相信 outcome。

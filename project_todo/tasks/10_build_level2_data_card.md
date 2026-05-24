# Task 10: 构造 Level 2 Data Card Task

## 目标

构造主测试层级：给 Agent 足够数据结构和变量组信息，让它有条件提出可辩护识别策略，但不直接告诉答案。

Level 2 应该接近 `zanbia.md` 中“数据结构 + 变量定义 + 研究目标”的清晰度。它不应只是一个短 Data Card，而应该让 Agent 明白数据如何产生、样本如何流转、哪些变量对应 treatment、selection、outcome、controls、design variables。

## 输入

- `gold_reference.md`
- `source_facts.md`
- `agent_task_level1.md`

## 需要做什么

1. 保留 Level 1 背景和研究目标。
2. 增加 `Research Setting`、`Specific Questions To Answer`、`Causal Mechanisms To Distinguish`。
3. 增加 `Data Structure Overview`，用 Stage 1/2/3/4 写清楚数据生成和样本流转。
4. 增加 Data Card。
5. 明确 observation unit、time span、sample construction。
6. 明确 treatment/exposure、outcome、secondary outcomes、covariates、baseline variables。
7. 明确 panel/repeated structure。
8. 明确 assignment or variation source，但不要命名为最终识别策略。
9. 增加 assignment level、outcome measurement level、clustering level。
10. 增加 compliance、missingness、spillover 信息。
11. 增加 `Variable Groups`，按 treatment、selection/sample-flow、main outcomes、secondary outcomes、baseline controls、design variables 组织。

## 怎么构造

Level 2 是主测试层级。可以让强模型/Codex 基于 `source_facts.md` 和 `gold_reference.md` 生成初稿，但必须人工检查。这里不是写“故事”，而是写清楚 Agent 判断识别策略所需的最小充分信息。

输入可以包含：

- `source_facts.md` 的 data structure、treatment/variation、outcomes、measurement risk。
- `source_facts.md` 的安全 sample-flow、time structure、assignment level、outcome measurement level。
- `gold_reference.md` 的 data structure 和 must-have conditions。

输入不应包含：

- original identification logic 的最终方法名称。
- linchpin detail 的解决方案表述。
- common invalid designs。
- 原论文独特术语或精确执行细节。

## 从 zanbia.md 借鉴的结构

Level 2 应包含：

- `Research Background`：继承 Level 1，保持任务自洽。
- `Research Setting`：参与者、决策顺序、业务/制度约束。
- `Research Objective`：主问题。
- `Specific Questions To Answer`：主效应、机制、选择/测量/政策解释。
- `Causal Mechanisms To Distinguish`：列出必须区分的机制路径。
- `Data Structure Overview`：用阶段叙事写清数据如何产生。例如 baseline/pre-period、intervention/exposure、short-run outcome、long-run/supplementary measurement。
- `Data Card`：结构化字段。
- `Variable Groups`：treatment/exposure、selection/sample-flow、main outcomes、secondary outcomes、baseline controls/design variables。
- `Known Constraints` 和 `Required Output`：强制 Agent 说明 identification logic、assumptions、sample restrictions、failure modes。

## Data Card 应写到什么粒度

| 模块 | 应该写什么 | 不应该写什么 |
|---|---|---|
| Unit of observation | individual / household / firm / store / product / region / time-period | 原论文真实样本名 |
| Time span | 前后几期、周度/月度/年度、是否有 pre-period | 精确年份如会泄漏论文 |
| Sample construction | 样本来自交易记录、调查、平台日志、政策数据等 | 独特机构名或地点名 |
| Treatment/exposure | X 是什么，如何被观察或分配 | “这是 RCT/DID/RDD 的处理” |
| Outcome | Y 是什么，如何测量 | 原论文独特变量名 |
| Secondary outcomes | 机制、中间结果、替代 outcome | 把机制 outcome 写成最终结论 |
| Covariates | 可用控制变量类别 | 过细导致可搜索的信息 |
| Baseline variables | pre-treatment 状态、历史行为、基线 outcome | post-treatment controls |
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

## Research Setting

## Research Objective

## Specific Questions To Answer

## Causal Mechanisms To Distinguish

## Data Structure Overview
- Stage 1:
- Stage 2:
- Stage 3:
- Stage 4:

## Data Card
- Unit of observation:
- Time span:
- Sample construction:
- Treatment/exposure variable:
- Outcome variable:
- Secondary outcomes:
- Covariates:
- Baseline or pre-treatment variables:
- Panel/repeated structure:
- Assignment or variation source:
- Assignment level:
- Outcome measurement level:
- Recommended clustering/inference level:
- Repeated exposure:
- Compliance/take-up:
- Missingness/attrition:
- Potential spillover/interference:

## Variable Groups
### Treatment Or Exposure Variables
### Selection Or Sample-Flow Variables
### Main Outcome Variables
### Secondary Outcome Variables
### Baseline Controls And Design Variables

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

本轮最初构造的是 Level 2 Data Card 主测试任务包。每个文件保留 Level 1 的匿名研究背景和研究目标，并补充 16 个 Data Card 字段：observation unit、time span、sample construction、treatment/exposure、outcome、covariates、panel/repeated structure、assignment/variation source、assignment level、outcome measurement level、clustering/inference level、repeated exposure、compliance/take-up、missingness/attrition、spillover/interference 等。未运行 OpenClaw。

后续模板修订：已根据 `zanbia.md` 的结构增强 Level 2 模板。新标准要求额外包含 `Data Structure Overview`、`Variable Groups`、`secondary outcomes`、`baseline/pre-treatment variables`。现有 pilot Level 2 task 如需完全匹配新标准，应重生成或增补这些模块。

## 验收标准

- [x] 一个懂基本计量/实验设计的人读完后能提出至少一个合理方向。
- [x] 信息足以判断是否能做 RCT/DID/RDD/IV/event study 或只能描述性分析。
- [x] 没有直接提示“应该使用某某方法”。
- [x] Data Card 字段完整，不用读原论文也能理解数据结构。
- [x] 模板已扩展为 staged data + variable groups，而不是单张短 Data Card。

## 常见风险

- 只给变量名，不给 assignment details。
- 给了 treatment 是随机的，但没说随机化层级。
- 忘记 outcome measurement risk，导致 Agent 过度相信 outcome。
- 把 Data Structure Overview 写成原论文复述，泄漏地点、年份、机构或独特执行方式。

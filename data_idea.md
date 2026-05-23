我建议：**不要只给“不同粒度的研究描述”**。那样还是容易被质疑成 prompt engineering。更稳的是给 OpenClaw 一个标准化的 **Research Case Packet**，也就是“研究设计任务包”。OpenClaw 本身更像一个可通过 QQ/WeChat 等渠道接入、能调工具和处理任务的 agent gateway，所以你的关键不是让它自由聊天，而是把输入、输出、日志和评测协议全部控制住。OpenClaw 官方页面也强调它支持 WeChat、QQ 等多渠道，并可以作为本地 gateway 管理 sessions、channels、tools 和 events。([GitHub][1])

你应该准备两类信息：**给 agent 看的信息**，以及**不给 agent 看的隐藏评测答案**。

## 1. 给 OpenClaw / agent 看的信息

我建议每个 case 都给它 5 个模块。

### A. 任务边界说明

先明确告诉它：

> 你不是在写 literature review，也不是在搜索原论文。你的任务是基于下列匿名化研究背景和数据描述，设计一个可辩护的实证/实验方案。请不要尝试识别原论文、作者、标题或在网上搜索相似论文。请只使用给定材料。

这一点很重要。否则 OpenClaw 一旦能联网或调用搜索工具，它可能反查到原论文，整个测试就污染了。

### B. 匿名化研究背景

这里不是越文学化越好，而是要服务于实验设计。包括：

研究场景是什么、现实问题是什么、研究对象是谁、行为机制可能是什么、为什么这个问题值得因果识别、目前直觉上可能有哪些混杂因素。

但不要给它原论文标题、作者、地区中特别可搜索的专有表达、原文里的独特句子。

### C. Data Card：数据说明卡

这个比背景更重要。你要像给数据集写 datasheet 一样写清楚：

| 项目                      | 应该给 agent 的内容                                                          |
| ----------------------- | ---------------------------------------------------------------------- |
| 观测单位                    | individual / household / firm / store / product / region / time-period |
| 时间跨度                    | 例如周度、月度、实验前后几期                                                         |
| 地理范围                    | 可以模糊化，比如“多个地区/多个门店”，不要给可反查具体名                                          |
| 样本来源                    | 调查、交易记录、平台日志、政策数据、实验记录                                                 |
| treatment / exposure    | 什么变量可能构成干预或处理                                                          |
| outcome                 | 要解释的核心结果变量                                                             |
| covariates              | 控制变量有哪些                                                                |
| panel structure         | 是否有重复观测、是否能做个体/时间固定效应                                                  |
| assignment details      | treatment 是随机、准随机、政策分配、自选择、还是市场结果                                      |
| assignment level        | treatment 是在 individual / household / firm / store / product / region 哪一层分配的         |
| outcome measurement level | outcome 是在哪一层测量的，是否和 treatment 分配层级一致                                      |
| clustering level        | 如果做统计推断，标准误应该按什么层级 cluster                                                |
| repeated exposure       | 同一对象是否会多次暴露于 treatment / exposure                                             |
| compliance              | 是否存在未接受分配处理、处理强度不一致、non-compliance 或 partial take-up                     |
| missingness / attrition | 是否有缺失、退出、样本选择问题                                                        |
| possible spillover      | 是否可能存在干扰或外溢                                                            |

你给它的数据描述不能只写“我们有消费者购买数据”。要写到它能判断：能不能 DID？能不能 RDD？是否有 panel FE？是否有内生性？是否需要 IV？

这里尤其要注意 **assignment level / outcome level / clustering level**。很多科研 agent 会写出看似正确的回归式，但忽略 treatment 实际是在门店、地区、学校或平台实验桶层面分配的，最后把个体层面的样本量当成独立观测，导致推断过度自信。

### D. Institutional Details：制度/机制细节

这是社会科学实验设计的灵魂。很多 agent 会失败，不是因为不会写模型，而是它抓不住“外生变化从哪里来”。

你应该给它这些原料，但不要直接说“这就是识别策略”：

比如：

促销/价格/政策/规则变化是由谁决定的？发生在什么时候？是否提前公布？是否所有对象同时受到影响？有没有阈值规则？有没有排队、抽签、地理边界、资格线、库存冲击、算法推荐规则、门店距离、平台曝光机制？

这个模块决定了它能不能自己发现 RCT、DID、RDD、IV、event study 或 matching 的可能性。

这里建议额外明确三个时间和操纵相关问题：

| 机制问题 | 为什么重要 |
| --- | --- |
| treatment 是否提前公布 | 如果提前公布，可能存在 anticipation effect |
| treatment 前是否有足够 pre-period | 决定能不能检查 pre-trend 或做 event study |
| 对象是否能操纵进入 treatment | 决定 RDD、资格线、补贴领取、广告曝光等设计是否可信 |

如果这些细节不给清楚，agent 可能会机械套 DID / RDD / IV，但无法判断关键假设是否成立。

### E. 输出格式要求

这个一定要强约束。不要让它自由写一大段“看似专业”的方案。你可以要求它必须输出：

1. **Research Question**：核心问题是什么
2. **Estimand**：想估计的因果量是什么，例如 ATE / ATT / elasticity / policy effect
3. **Treatment and Outcome**：处理变量和结果变量
4. **Main Identification Challenge**：最关键的内生性/选择偏差是什么
5. **Proposed Design**：主识别策略
6. **Why This Design Works**：为什么这个设计能支撑因果解释
7. **Required Assumptions**：关键假设
8. **Statistical Model**：模型形式，是否需要 FE、clustered SE、event-study terms
9. **Robustness / Placebo Checks**：至少 3 个
10. **Failure Modes**：什么时候这个设计会失效
11. **What Cannot Be Claimed**：哪些结论不能说
12. **Additional Data Needed**：如果数据不够，还需要什么

还应该强制它输出一个 **Claim-Evidence Table**，方便后续人工标注：

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
| --- | --- | --- | --- | --- |
| Agent 的关键结论 | 引用了哪些输入材料 | 因果 / 机制 / 模型 / 假设 / 局限 | high / medium / low | 什么证据会推翻它 |

同时要加一句硬约束：

> If credible causal identification is not possible, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

这一步很关键，因为你的课程要求本来就强调要有测试样例、人工判断、错误分类、日志和可复现性，而不是只展示一个漂亮输出。

## 2. 不给 agent 看的隐藏评测信息

这个是你的“答案纸”，不能放进 OpenClaw prompt。

每个 case 背后你要保存：

| 隐藏材料     | 用途                                                       |
| -------- | -------------------------------------------------------- |
| 原论文真实设计  | 不是要求完全复现，而是作为 gold reference                             |
| 关键识别逻辑   | 例如随机化、政策冲击、阈值、工具变量、自然实验                                  |
| 必须识别出的威胁 | 例如 selection、reverse causality、parallel trends、spillover |
| 可接受替代方案  | 防止评分过于死板                                                 |
| 不可接受方案   | 例如只做 OLS 相关性却声称因果                                        |
| 反事实变体答案  | 修改关键条件后，合理设计应该如何变化                                       |
| rubric   | 每项几分，错误如何归类                                              |

这会让你的展示更硬：你不是事后挑毛病，而是事前定义了评分标准。

此外，每个 case 还应该有一个 **Quality-control metadata**，用于后续统计和审计：

| 字段 | 用途 |
| --- | --- |
| case_id | 唯一编号，方便追踪输入、输出和标注 |
| domain | marketing / labor / public econ / behavioral / development 等 |
| design_family | RCT / DID / RDD / IV / audit / field experiment / no-solution |
| key_failure_mode | endogenous exposure / selection / mechanism confounding / measurement error / spillover |
| difficulty | easy / medium / hard |
| variant_type | original-like / perturbed / no-solution |
| leakage_risk | low / medium / high |
| audit_decision | approve / revise / reject |

这些 metadata 可以让你后面不只是展示几个例子，而是回答更强的问题：agent 到底在哪类商科任务上最容易失败？是广告 exposure、机制分解、测量误差，还是没有强识别时的 overclaim？

## 3. 我建议你给 OpenClaw 的材料分 3 个版本

你之前说“不同粒度的研究描述”，这个可以保留，但要成为整体设计的一部分。

| 版本      | 给 agent 什么                     | 测什么              |
| ------- | ------------------------------ | ---------------- |
| Level 1 | 背景 + 研究问题                      | 能否形成基本研究设计方向     |
| Level 2 | 背景 + Data Card + 变量结构          | 能否根据数据结构选择识别策略   |
| Level 3 | 背景 + Data Card + 制度细节 + 潜在威胁提示 | 在信息较充分时是否仍然犯低级错误 |

展示时你就可以说：
**如果 Level 1 做不好，不代表 agent 差；但如果 Level 2/3 仍然只给泛泛 OLS、忽略自选择、把相关性写成因果，那就是科研设计能力缺陷。**

这比“只给一个研究背景”稳太多。

## 4. 最漂亮的是再加两个特殊 case

### 一个反事实扰动 case

比如原始版本里 treatment 近似随机，扰动版本里 treatment 变成用户自选择。

你看它是否还机械套 RCT/DID。如果它不调整设计，就说明它没有理解识别条件，只是在套模板。

### 一个无解 case

故意给一个只能做相关性、无法做强因果识别的数据包。正确 agent 应该说：

> 当前数据不足以支持因果结论，只能做描述性分析或相关性分析；若要识别因果，需要补充外生冲击、随机化、工具变量或更细粒度 panel data。

这类 case 很适合展示科研 agent 的 overclaim 问题。DeepScientist 官方 README 也强调其可以辅助 planning、implementation、experiment orchestration、analysis、writing，但最终判断、claim 和真实实验结果仍由人类负责，这正好支持你把项目定位成“能力边界诊断”，而不是“证明 agent 自动科研成功”。([GitHub][2])

## 5. 一个可以直接塞给 OpenClaw 的任务模板

你可以每个 case 都用这个结构：

```markdown
# Anonymous Research Design Task

## Task Rule
You must not search the web, infer the original paper, or use external literature.
You must only use the information provided below.
Your goal is to design a rigorous empirical strategy, not to write a literature review.

## Research Background
[匿名化背景]

## Research Objective
[研究问题：是否/如何/在多大程度上 X 影响 Y]

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

## Institutional Details
[制度、政策、市场机制、干预过程、时间规则、分配规则等]
- Was the treatment announced in advance?
- Is there enough pre-treatment data?
- Can units manipulate entry into treatment?
- Are there thresholds, lotteries, queues, geographic boundaries, eligibility rules, inventory shocks, platform algorithms, or exposure rules?

## Constraints
- You cannot collect new data unless you explicitly state why existing data is insufficient.
- You must distinguish causal claims from descriptive claims.
- If causal identification is not credible, say so directly.
- If credible causal identification is not possible, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

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

## Claim-Evidence Table
| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
```

## 6. Case Packet Schema

每个 benchmark case 最终应该拆成三个层次的文件。这样可以把“给 agent 的任务”“不给 agent 的答案”和“构建质量控制”分开，避免后面数据污染或评分混乱。

### 6.1 Agent-facing task packet

这是唯一可以进入 OpenClaw / agent 上下文的文件：

- Task rule
- Anonymous research background
- Research objective
- Data Card
- Institutional Details
- Constraints
- Required Output
- Claim-Evidence Table 要求

### 6.2 Evaluator-only gold reference

这是隐藏评测答案，不能进入 agent 上下文：

- Original paper source
- True research question
- Data structure
- Identification logic
- Linchpin detail
- Acceptable alternative designs
- Invalid designs
- Perturbed variant answer
- No-solution answer
- Rubric

### 6.3 Quality-control metadata

这是任务包构建过程中的审计信息：

- case_id
- domain
- design_family
- key_failure_mode
- difficulty
- variant_type
- leakage_risk
- audit_decision

### 6.4 Leakage Control

匿名任务包需要单独做泄漏检查。建议每个 case 都记录：

| 字段 | 检查内容 |
| --- | --- |
| removed_identifiers | 是否删除了题名、作者、机构、具体地点、精确年份、精确样本量 |
| remaining_searchable_phrases | 是否还保留原文中特别可搜索的短语 |
| unique_context_risk | 场景是否过于独特，导致 agent 可能反推出原论文 |
| method_leakage_risk | Level 2 / Level 3 是否直接暗示了原论文的识别策略 |
| final_decision | approve / revise / reject |

泄漏控制的目标不是把任务变得空泛，而是避免 agent 通过记忆或搜索命中原论文。一个合格任务包应该保留研究设计所需的结构信息，但去掉可反查身份的信息。

## 我的建议结论

所以答案是：**不是仅仅给不同粒度的研究描述，而是给“背景 + 数据卡 + 制度机制 + 约束条件 + 输出合同”的标准化任务包。**

你最终要展示的不是“OpenClaw 能不能猜中原论文”，而是：

> 在信息逐步充分的情况下，科研 agent 是否能把研究问题、数据结构和制度细节转化成合理识别策略；如果不能，它具体失败在因果威胁识别、模型选择、假设诊断，还是过度声称因果。

这个 framing 很稳，而且和你课程 project 的“功能扩展或缺陷诊断”“真实交互、日志、测试样例、失败案例、可复现性”的要求完全对齐。

[1]: https://github.com/openclaw/openclaw?utm_source=chatgpt.com "OpenClaw — Personal AI Assistant"
[2]: https://github.com/ResearAI/DeepScientist?utm_source=chatgpt.com "ResearAI/DeepScientist: Now, Stronger AI Pushes ..."

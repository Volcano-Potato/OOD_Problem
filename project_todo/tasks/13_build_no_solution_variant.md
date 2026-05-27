# Task 13: 构造 No-Solution Variant

## 目标

构造“信息很多但现有数据无法支持强因果识别”的任务，测试 Agent 是否具备科研诚实性。

No-solution variant 不是“信息太少”的 Level 1，也不是“只改一个条件”的 perturbed variant。它应该保留研究问题的重要性、可观测 outcome、丰富 covariates、看起来像可分析的数据结构，但故意不提供可信的外生 variation。正确答案应当是：不能做强因果识别，只能做描述性、预测性或相关性分析，并明确还缺什么设计。

## 输入

- `gold_reference.md`
- `agent_task_level2.md`

## 需要做什么

1. 移除或削弱关键外生 variation source。
2. 保留现实重要性和看似有用的数据。
3. 明确数据最多只能支持描述性、预测性或相关性分析。
4. 不保留隐藏随机化、阈值、外生冲击、有效工具变量或自然实验。
5. 写 rich agent-facing no-solution task。
6. 写 evaluator-only notes，说明最大可支持 claim 和需要补什么设计。

## 怎么构造

No-solution variant 可以让强模型或 Codex 生成候选，但人工必须检查没有隐藏可用的强识别条件。

构造步骤：

1. 保留研究问题的重要性和业务或政策价值。
2. 保留一些“诱惑性”变量，例如 outcome、covariates、历史记录、自报信息、大样本横截面、treated and untreated 都可观察。
3. 移除随机化、阈值、外生政策冲击、有效工具变量、干净 exposure-opportunity、可信 untreated market、独立硬 outcome、可用 pre-period 外生 timing 等。
4. 让 treatment/exposure 变成自选择、风险定价、算法分配、管理者自主决策、横截面差异、或市场结果。
5. 明确最大可支持结论：描述性关系、预测、相关性、机制假说，而不是 causal effect。
6. 明确要支持因果 claim 还需要什么：随机化、自然实验、panel、独立 outcome、工具变量、外生 adoption timing 等。

## 从 rich task 模板继承什么

No-solution variant 不应该退回到简陋 prompt。它应至少包含：

- `Research Background`
- `Research Setting`
- `Research Objective`
- `Specific Questions To Answer`
- `Data Structure Overview`
- `Available Data`
- `Variable Groups`
- `Identification Limitations`
- `Known Constraints`
- `Required Output`
- `Claim-Evidence Table`

## Agent-facing 应该看起来“有诱惑力”

可以包含：

- 很多协变量。
- 大样本横截面或运营数据。
- 处理组和对照组都可观察。
- outcome 清楚。
- 业务问题重要。

但不能包含：

- 可用 pre-period + 明确外生 staggered adoption。
- 明确随机分配。
- 清晰资格阈值。
- 明显有效工具变量。
- 可以让人直接做 RDD、DID、IV 的制度规则。
- 独立 outcome 加外生 assignment 的组合。

## evaluator-only notes 必须写

- `missing_identification_category`
- `core_reason`
- `main_unobserved_confounder_or_alternative_explanation`
- `strongest_supported_claim`
- `likely_bad_agent_response`
- `expected_error_types`

## 产出

- `agent_task_no_solution.md`
- `no_solution_variant.md`

## 完成记录

Pilot set 已完成：

- `benchmark/cases/C001_charitable_giving/agent_task_no_solution.md`
- `benchmark/cases/C001_charitable_giving/no_solution_variant.md`
- `benchmark/cases/C002_consumer_credit/agent_task_no_solution.md`
- `benchmark/cases/C002_consumer_credit/no_solution_variant.md`
- `benchmark/cases/C005_online_ad_measurement/agent_task_no_solution.md`
- `benchmark/cases/C005_online_ad_measurement/no_solution_variant.md`
- `benchmark/cases/C008_retail_tax_salience/agent_task_no_solution.md`
- `benchmark/cases/C008_retail_tax_salience/no_solution_variant.md`
- `benchmark/cases/C014_corruption_monitoring/agent_task_no_solution.md`
- `benchmark/cases/C014_corruption_monitoring/no_solution_variant.md`

本轮同时升级了 `C000_template` 下的 no-solution 模板，使其与新的 rich task 结构一致，并补充了 evaluator-only note 里的 `missing_identification_category`、`core_reason`、`main_unobserved_confounder_or_alternative_explanation`、`strongest_supported_claim`、`likely_bad_agent_response`、`expected_error_types`。

5 个 pilot case 的 no-solution 设计分别是：

- `C001`：fundraising outreach 和 pre-contact communication 完全由运营判断决定，没有随机化或机制分离设计。
- `C002`：consumer credit pricing 由 underwriting risk model 和 staff discretion 决定，没有 exogenous pricing variation。
- `C005`：digital ad exposure 完全由 targeting、bidding、optimization 决定，没有 holdout 或机会集对照。
- `C008`：retail visible-pricing adoption 由 store managers 自主决定，没有 exogenous rollout timing。
- `C014`：monitoring assignment 和 official outcomes 都是内生的，而且没有 independent outcome measurement。

这些 no-solution task 都保留了真实研究价值、清晰 outcome、丰富 covariates 和“很像能跑回归”的结构，但不保留可信强识别来源。未运行 OpenClaw。

主集扩展：`C004` 已新增完成 `benchmark/cases/C004_paid_search_effectiveness/agent_task_no_solution.md` 和 `benchmark/cases/C004_paid_search_effectiveness/no_solution_variant.md`。该 no-solution 版本保留 rich marketing logs、market-time sales 和 segment covariates，但移除了任何可信的外生 ad-availability variation。

主集扩展：`C010` 已新增完成 `benchmark/cases/C010_fertilizer_present_bias/agent_task_no_solution.md` 和 `benchmark/cases/C010_fertilizer_present_bias/no_solution_variant.md`。该 no-solution 版本保留 seasonal panel、price variation、intentions 和 adoption outcomes，但移除了任何可信的 randomized timing variation。

主集扩展：`C016` 已新增完成 `benchmark/cases/C016_hiv_risk_information/agent_task_no_solution.md` 和 `benchmark/cases/C016_hiv_risk_information/no_solution_variant.md`。该 no-solution 版本保留 school-level program exposure、objective and survey outcomes、以及丰富 school/community covariates，但移除了任何可信的 exogenous information-content assignment。

主集扩展：`C019` 已新增完成 `benchmark/cases/C019_in_store_travel_distance/agent_task_no_solution.md` 和 `benchmark/cases/C019_in_store_travel_distance/no_solution_variant.md`。该 no-solution 版本保留 rich route logs、checkout baskets、display exposure 和 shopper covariates，但移除了任何可信的 exogenous route variation。

主集扩展：`C020` 已新增完成 `benchmark/cases/C020_price_ending_field_experiment/agent_task_no_solution.md` 和 `benchmark/cases/C020_price_ending_field_experiment/no_solution_variant.md`。该 no-solution 版本保留 rich item-level price histories、promotion labels、item history 和 sales outcomes，但移除了任何可信的 exogenous ending-format variation。

## 验收标准

- [x] 正确答案应是“不能做强因果识别”。
- [x] 任务仍然有研究价值，而不是明显无意义。
- [x] 至少包含 2-3 个会诱导弱 Agent 误用回归、matching、伪 DID 或机制解释的变量。
- [x] evaluator notes 明确 maximum defensible claim 和 additional data or intervention needed。
- [x] 变体延续 rich task 结构，而不是退回到简陋 prompt。

## 常见风险

- 不小心留下可用的强识别来源。
- 任务太明显，Agent 很容易机械回答“不能做因果”而不必认真判断。
- 没有定义最大可支持的描述性结论。
- 看起来是 no-solution，但其实还能靠 panel、timing、threshold 或独立 measurement 做强识别。

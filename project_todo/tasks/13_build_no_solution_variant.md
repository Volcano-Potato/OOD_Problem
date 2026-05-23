# Task 13: 构造 No-Solution Variant

## 目标

构造现有数据无法支持强因果识别的任务，测试 Agent 是否具备科研诚实性。

## 输入

- `gold_reference.md`
- `agent_task_level2.md`

## 需要做什么

1. 移除或削弱关键外生 variation source。
2. 保留现实重要性和看似有用的数据。
3. 明确数据只能支持描述性或相关性分析。
4. 不藏随机化、阈值、外生冲击、有效工具变量或自然实验。
5. 写 Agent-facing no-solution task。
6. 写 evaluator-only notes，说明最大可支持 claim。

## 怎么构造

No-solution variant 不是“信息很少”的 Level 1，而是“信息看似很多，但没有强识别来源”。可以让强模型/Codex 根据原 case 生成候选，但人工必须检查没有隐藏可用的强识别条件。

构造步骤：

1. 保留研究问题的重要性。
2. 保留一些可用变量，例如 outcome、covariates、历史记录、自报信息。
3. 移除随机化、阈值、外生政策冲击、有效工具变量或干净时间变化。
4. 让 treatment/exposure 变成自选择、市场结果、算法分配或只在横截面中观测。
5. 明确最大可支持结论：描述性关系、预测、相关性或机制假说。
6. 明确要支持因果 claim 还需要什么：随机化、自然实验、panel、独立 outcome、工具变量等。

## Agent-facing 应该看起来“有诱惑力”

可以包含：

- 很多协变量。
- 大样本横截面。
- 处理组和对照组都可观察。
- outcome 清楚。
- 业务问题重要。

但不能包含：

- 可用 pre-period + 明确外生 staggered adoption。
- 明确随机分配。
- 清晰资格阈值。
- 明显有效工具变量。
- 可以让人直接做 RDD/DID/IV 的制度规则。

## 产出

- `no_solution_variant.md`

## 验收标准

- [ ] 正确答案应是“不能做强因果识别”。
- [ ] 任务仍然有研究价值，而不是明显无意义。
- [ ] 至少包含 2-3 个会诱导弱 Agent 误用回归/matching/DID 的变量。
- [ ] evaluator notes 明确 additional data or intervention needed。

## 常见风险

- 不小心留下可用的强识别来源。
- 任务太明显，Agent 很容易说不能做因果。
- 没有定义最大可支持的描述性结论。

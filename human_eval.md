# C001 baseline report 人工审计
## level 1

| 编号 | 不能怪匿名信息的瑕疵 | 为什么算它自己的问题 |
| -- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | 把主识别放在 T1 in-person vs T3 flyer-only | 它自己也承认 T1–T3 混合了 pressure、attention、information、salience，却还把这个说成“core pressure contrast”。更好的主轴应是 advance notice / opt-out 如何改变人们是否愿意 engage。匿名 packet 已经明确要求回答“是否 engage with fundraiser”和“如何区分不愿拒绝的压力” |
| 2 | treatment 简化成“pressure level”排序| 它把 T1，T2，T3分别对应高中低三种压力等级。但更严谨地说，T2/T4主要改变的是能否提前回避/选择接触，不是简单改变面对面时的压力强度。论文核心也是让人可以 seek or avoid solicitor |
| 3 | 缺少两阶段行为模型 | 它没有清楚建模“先决定是否开门/接触，再决定是否捐、捐多少” |
| 4 | 把 T3 flyer-only giving 当 genuine demand lower bound 太脆弱| flyer-only 给得少可能是没看到 flyer、远程捐款麻烦、信息弱、没有即时支付方式，而不一定是 genuine demand 少。agent 自己在 failure modes 里承认这个问题，却仍把它放在核心 estimand |
| 5 | 金额模型太模板化：Tobit / two-part 不够贴合问题 | 捐款金额通常是大量 0、小额离散、可能有 $5/$10 bunching。Tobit 的 latent normal censoring是连续的；更关键应看 unconditional amount、giving probability、金额分布、小额/大额捐款的 treatment effect |
| 6 | 没有把小额 vs 大额捐款作为核心机制检验 | 即便不知道论文结果，也应该想到：压力型捐款更可能集中在小额打发式捐款，而 genuine demand 更可能体现在较大额或持续捐款 |


## level 2

| 编号 | 不能怪匿名信息的瑕疵 | 为什么算report自己的问题 |
| -- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | 把提前通知但无 opt-out的 B 组说成不能便宜地回避，并把 A vs B 解释成压力大致不变、主要测 awareness/scheduling | 匿名包已经说处理可以改变visit 如何被沟通以及接触前回避是否容易，原论文的核心逻辑也是 flyer 让住户可以 seek or avoid solicitor。也就是说，普通 flyer 本身就改变回避机会，不是只改变日程/知情。report 这里把 B 组机制窄化了，会低估 A vs B 对压力/回避的识别价值 |
| 2 | 把conditional on contact 的 giving 差异写成一个average causal effect | contact 是处理后的变量，report 自己后面也承认 contacted sample 是内生选择；所以不能在 target estimand 处先把它命名为因果效应。匿名包明确要求区分描述、因果和机制 claims，这不是信息缺失，而是概念前后不一致 |
| 3 | 把未接触家庭的 giving/amount 说成unobserved/missing | 对上门募捐中的实际 in-person contribution来说，没接触通常应是结构性 0；未观察到的是如果接触了会不会捐的反事实偏好，不是实际捐款结果本身。匿名包的数据卡已经把单位定义为 planned contact opportunity，并把是否贡献、金额列为机会层面的 outcome；report 把实际 outcome 和潜在 outcome 混在一起了 |
| 4 | Lee bounds / principal-strata 部分过度包装成“net of selection 的 pressure effect” | Lee bounds 最多在单调选择等假设下给选择调整后的条件捐赠差异范围；它不能自动把这个差异解释成 social pressure，因为 B vs C 同时改变 opt-out 话语、预期、心理信号和样本组成。report 甚至自己承认 opt-out 可能传递尊重/组织质量信号，却仍说 bounds 排除 0 就是 pressure effect net of selection，机制 claim 跳得太快 |
| 5 | 小额捐赠分析没有把无条件分布放在核心位置 | report 虽然提到 contribution-size distribution，但模型部分更偏向 conditional giving 和 multinomial/ordered logit。问题是小额捐减少是否支持压力，最好看 planned opportunity 层面的无条件小额/大额捐概率变化；若只在 contacted 样本里看，很容易又被选择进入 contact 的组成变化污染。匿名包已经列出 contribution size bins 和 small vs large categories，这个分析层级可以从已给信息推出 |

## level 3


| 编号 | 不能怪匿名信息的瑕疵 | 为什么算 report 自己的问题 |
| -- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | Principal stratification / Lee bounds 的表述有硬伤：说 always-contacted households 在 B 和 C 下的捐赠都能观察到 | 这是随机分组的横截面设计，同一个 household 不会同时处在 B 和 C。即使在 B vs. C 单调性下，C 组被接触者可以被解释为 always-contacted，但 B 组被接触者仍是 always-contacted 与 avoiders 的混合；不能说我们观察到 always-contacted 在两个处理下的捐赠 |
| 2 | 单调性假设写得过宽，尤其把 advance notice 也说成不太可能让本来不接触的人变成接触 | 论文和匿名任务的核心机制之一恰恰是：真心想捐的人可能因为提前通知而 seek the solicitor / 增加在家开门概率；原论文也明确说如果 altruism 是主导，flyer 应提高 presence 和 giving。单调性最多可对在已有通知下额外给 easy opt-out这一比较更有说服力，不能笼统套到所有 notice 比较上 |
| 3 | 把 A vs. B 中 contact 下降直接解释成households are sorting away | 匿名任务已经提醒：提前沟通可能改变 scheduling/awareness，即使没有 pressure。A vs. B 的 contact 下降最多说明 notice 改变了接触概率，不能单独判定是主动躲避 solicitor；更强的 avoidance 证据应来自 B vs. C 的 opt-out/easy avoidance 比较。 |
| 4 | 把pressure gap说成 B vs. C unconditional giving 的差，或要求 giving 下降超过 contact-rate change 能解释的部分。 | 社会压力机制完全可能主要通过 sorting-out 发生：容易躲避后，原本会在压力下给小钱的人不再开门，因此 unconditional giving 下降，但 contacted 样本的 conditional giving 未必显著下降。原论文的关键 reduced-form 证据是 opt-out 降低开门和捐赠，且降幅集中在小额捐赠,并不是必须观察到 always-contacted 的行为变化。report 这里把选择进入/退出接触与接触后行为变化混得太紧 |
| 5 | Contribution-size 分析过度放在among contacted households / conditional distribution上 | 匿名任务强调 contribution size 要和 contact、giving 联合分析；原论文的命题也是看 unconditional probability of small/large donations，因为 conditional-on-contact 的金额分布本身会被选择进门的人群改变。report 建议对 contacted 样本做 KS test / conditional distribution shift，容易把样本选择后的分布变化误读成机制证据 |


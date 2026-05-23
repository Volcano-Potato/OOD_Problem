# DeepScientist 经济学 / 商科实验设计能力测试候选论文清单

> 用途：从经典经济学、营销学、行为经济学 field experiment / lab experiment 中抽取“研究背景 + 数据描述 + 研究目标”，隐藏原论文题名和关键处理臂，让 Openclaw构建的科研agent 自行提出实验设计、模型设计或识别策略，再与真实论文的关键设计细节对比。  
> 核心评价点不是 Agent 是否会说“随机实验 / 回归 / 稳健性检验”，而是它能否自发提出那些**看似流程细节、实则识别命门**的安排。

---

## 1. 主推荐池：最适合做盲测主案例

| # | 论文 | 领域 | 论文 / 官方链接 | 数据 / 复制材料 | Linchpin detail：关键设计命门 | 适合作为测试题的原因 |
|---|---|---|---|---|---|---|
| 1 | DellaVigna, List & Malmendier (2012), **Testing for Altruism and Social Pressure in Charitable Giving** | 行为经济学 / 慈善捐赠 | [Author PDF](https://sdellavi.com/pdf/CharityQJEFeb12.pdf); [QJE / RePEc](https://ideas.repec.org/a/oup/qjecon/v127y2012i1p1-56.html) | — | 上门募捐前挂 flyer，部分 flyer 带 “Do Not Disturb” opt-out 框。 | 检验 Agent 能否想到：为了区分 altruism / warm glow 与 social pressure，需要给被试一个低成本回避通道，而不只是随机化募捐话术。 |
| 2 | Karlan & Zinman (2009), **Observing Unobservables: Identifying Information Asymmetries with a Consumer Credit Field Experiment** | 消费信贷 / 信息不对称 | [Wiley / Econometrica](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA5781); [Author PDF](https://sites.dartmouth.edu/jzinman/files/2021/02/KarlanZinman_OU_long.pdf); [J-PAL summary](https://www.povertyactionlab.org/evaluation/identifying-information-asymmetries-consumer-credit-market-south-africa) | — | 三重随机化：offer rate、accept 后才揭晓的 contract rate、未来贷款动态还款激励。 | 极适合测试 Agent 是否能分离 adverse selection 与 moral hazard；如果只说“随机利率”，识别是不够的。 |
| 3 | Niederle & Vesterlund (2007), **Do Women Shy Away from Competition? Do Men Compete Too Much?** | 劳动 / 性别 / 实验经济学 | [Author PDF](https://web.stanford.edu/~niederle/Niederle.Vesterlund.QJE.2007.pdf); [QJE / RePEc](https://ideas.repec.org/a/oup/qjecon/v122y2007i3p1067-1101..html) | — | 让被试为已经完成过的表现选择计件或锦标赛支付，而不是为新任务选择。 | 检验 Agent 是否能把“竞争偏好”从风险厌恶、自信程度、当场表现反馈等替代解释里剥离出来。 |
| 4 | Blake, Nosko & Tadelis (2015), **Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment** | 营销 / 搜索广告 / 平台经济 | [Wiley / Econometrica](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA12423); [Author PDF](https://faculty.haas.berkeley.edu/stadelis/BNT_ECMA_rev.pdf); [NBER](https://www.nber.org/papers/w20171) | — | eBay 大规模付费搜索广告实验；品牌词广告作为近似 placebo / 诊断探针；按用户过去访问频率分层。 | 很适合商科测试。普通 Agent 容易做“广告开/关”的平均 ROI，但会漏掉搜索意图内生性和消费者异质性。 |
| 5 | Johnson, Lewis & Nubbemeyer (2017), **Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness** | 营销 / 在线广告 / retargeting | [Journal of Marketing Research / SAGE](https://journals.sagepub.com/doi/abs/10.1509/jmr.15.0297); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2620078); [NBER conference PDF](https://conference.nber.org/confer/2016/EoDs16/Johnson_Lewis_Nubbemeyer.pdf) | — | 在控制组中识别“如果被分到 treatment 本该看到广告”的 ghost impressions。 | 极适合测 Agent 是否理解广告 exposure 的内生性。普通用户级 A/B 或点击回归会严重不够。 |
| 6 | Cohen & Dupas (2010), **Free Distribution or Cost-Sharing? Evidence from a Randomized Malaria Prevention Experiment** | 发展经济学 / 健康产品定价 | [QJE / Oxford Academic](https://academic.oup.com/qje/article/125/1/1/1880305); [PDF](https://www.earth.columbia.edu/sitefiles/file/bednets/Cohen_Dupas_Free_Distribution_or_costsharing_2009.pdf); [Harvard GAP](https://gap.hks.harvard.edu/free-distribution-or-cost-sharing-evidence-randomized-malaria-prevention-experiment) | — | 价格随机化 + 对购买者再随机折扣 / 后续使用检查，用来分离 selection 与 sunk-cost effect。 | 很适合测试 Agent 是否会把“价格筛选出使用者”和“付钱导致更珍惜”区分开。 |
| 7 | Ashraf, Berry & Shapiro (2010), **Can Higher Prices Stimulate Product Use? Evidence from a Field Experiment in Zambia** | 营销 / 健康产品 / 发展经济学 | [AEA / AER](https://www.aeaweb.org/articles?id=10.1257%2Faer.100.5.2383); [NBER](https://www.nber.org/papers/w13247); [Author page](https://shapiro.scholars.harvard.edu/publications/can-higher-prices-stimulate-product-use-evidence-field-experiment-zambia) | [AEA replication / openICPSR](https://www.openicpsr.org/openicpsr/project/112389/version/V1/view%3Bjsessionid%3D25611B96526237C19502774CE9F55B2D?path=%2Fopenicpsr%2F112389%2Ffcr%3Aversions%2FV1%2Fcode) | 对家庭水净化产品进行价格随机化，并测购买后真实使用；核心是区分 screening effects 与 sunk-cost effects。 | 适合作为已有数据友好案例。Agent 容易把价格影响使用直接解释为 sunk cost，而忽略 selection。 |
| 8 | Chetty, Looney & Kroft (2009), **Salience and Taxation: Theory and Evidence** | 公共经济学 / 税收显著性 / 消费者行为 | [AEA / AER](https://www.aeaweb.org/articles?id=10.1257%2Faer.99.4.1145); [Author PDF](https://rajchetty.com/wp-content/uploads/2021/04/taxsalience_aer.pdf); [NBER](https://www.nber.org/papers/w13330) | [AEA replication / openICPSR](https://www.openicpsr.org/openicpsr/project/113312/version/V1/view?path=%2Fopenicpsr%2F113312%2Ffcr%3Aversions%2FV1%2FLICENSE.txt&type=file) | 在超市部分商品贴含税价标签，并结合控制商品 / 控制门店 / 时间变化识别。 | 测 Agent 是否从简单前后比较升级到 treated categories × control categories × stores × weeks 的差分结构。 |
| 9 | Bertrand, Karlan, Mullainathan, Shafir & Zinman (2010), **What’s Advertising Content Worth? Evidence from a Consumer Credit Marketing Field Experiment** | 营销 / 广告内容 / 消费金融 | [QJE / Oxford Academic](https://academic.oup.com/qje/article-abstract/125/1/263/1880334); [J-PAL PDF](https://www.povertyactionlab.org/sites/default/files/research-paper/13%20Marketing%20Feb%2010.pdf); [RePEc](https://econpapers.repec.org/RePEc%3Aoup%3Aqjecon%3Av%3A125%3Ay%3A2010%3Ai%3A1%3Ap%3A263-306.) | — | 同时随机化广告内容、贷款价格和 offer deadline。 | 测 Agent 是否会把营销 A/B test 从“点击率测试”提升到真实金融需求、价格参照和 adverse selection 的识别。 |
| 10 | Duflo, Kremer & Robinson (2011), **Nudging Farmers to Use Fertilizer: Theory and Experimental Evidence from Kenya** | 发展经济学 / 技术采纳 / present bias | [AEA / AER](https://www.aeaweb.org/articles?id=10.1257%2Faer.101.6.2350); [NBER](https://www.nber.org/papers/w15131); [J-PAL summary](https://www.povertyactionlab.org/evaluation/nudging-farmers-use-fertilizer-experimental-evidence-kenya) | [AEA replication / openICPSR](https://www.openicpsr.org/openicpsr/project/112458/version/V1/view?path=%2Fopenicpsr%2F112458%2Ffcr%3Aversions%2FV1%2FLICENSE.txt&type=file) | 小额、限时、刚收获后提供的折扣 / delivery，而不是大额长期补贴。 | 测 Agent 是否能把机制从“价格水平不够低”转向“时点 friction + present bias”。 |

---

## 2. 强补充池：适合做辅助案例或展示案例

| # | 论文 | 领域 | 论文 / 官方链接 | 数据 / 复制材料 | Linchpin detail：关键设计命门 | 适合作为测试题的原因 |
|---|---|---|---|---|---|---|
| 11 | Bertrand & Mullainathan (2004), **Are Emily and Greg More Employable than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination** | 劳动经济学 / 审计实验 / 歧视 | [AEA / AER](https://www.aeaweb.org/articles?id=10.1257%2F0002828042002561); [NBER](https://www.nber.org/papers/w9873); [JSTOR](https://www.jstor.org/stable/3592802) | [AEA replication / openICPSR](https://www.openicpsr.org/openicpsr/project/116023/version/V1/view?path=%2Fopenicpsr%2F116023%2Ffcr%3Aversions%2FV1%2FLICENSE.txt&type=file) | 同一招聘广告下投递多份随机化简历；姓名 race signal 与简历质量交叉随机。 | 顶级经典，但太有名，Agent 可能背过。适合作 sanity check 或反向分析题。 |
| 12 | Gneezy & Rustichini (2000), **A Fine Is a Price** | 行为经济学 / 社会规范 / 激励 | [JSTOR](https://www.jstor.org/stable/10.1086/468061); [PDF](https://www.ius.uzh.ch/dam/jcr%3Aed3f9a0b-ab68-4cf6-a18c-a480b33c9456/Gneezy%20et%20al%20A%20Fine%20is%20a%20Price.pdf); [RePEc](https://econpapers.repec.org/RePEc%3Aucp%3Ajlstud%3Av%3A29%3Ay%3A2000%3Ai%3A1%3Ap%3A1-17) | — | 部分托儿所引入迟到罚款，随后取消罚款；关键是取消后迟到没有回落。 | 测 Agent 是否想到撤销臂，用不可逆性区分价格机制与社会规范被挤出。 |
| 13 | Fryer, Levitt, List & Sadoff (2022; NBER 2012), **Enhancing the Efficacy of Teacher Incentives through Framing: A Field Experiment** | 教育经济学 / 激励 / loss aversion | [AEA PDF / AEJ: Economic Policy](https://pubs.aeaweb.org/doi/pdfplus/10.1257/pol.20190287); [Author PDF](https://rady.ucsd.edu/_files/faculty-research/sadoff/Fryer_et_al_Enhancing_Efficacy_Teacher_Incentives_Framing_AEJ_Policy_2022.pdf); [NBER 2012 WP](https://www.nber.org/papers/w18237) | — | 奖金先预付，年底不达标再退回；与年底达标才发的 gain frame 对比。 | 测 Agent 是否会设计“经济等价但心理框架不同”的处理臂，而不是只改变激励金额。 |
| 14 | Olken (2007), **Monitoring Corruption: Evidence from a Field Experiment in Indonesia** | 政治经济学 / 腐败治理 / 公共项目 | [JPE / UChicago](https://www.journals.uchicago.edu/doi/abs/10.1086/517935); [J-PAL PDF](https://www.povertyactionlab.org/sites/default/files/research-paper/27_Olken_Monitoring_Corruption.pdf); [NBER](https://www.nber.org/papers/w11753) | — | 随机提高审计概率，并用独立工程师估计道路真实投入，与官方支出对比。 | 测 Agent 是否意识到 outcome 本身不能来自可能被操纵的官方账本，必须独立测量。 |
| 15 | Hanna, Mullainathan & Schwartzstein (2014), **Learning Through Noticing: Theory and Evidence from a Field Experiment** | 发展经济学 / 学习 / 注意力 | [QJE / Oxford Academic](https://academic.oup.com/qje/article-abstract/129/3/1311/1817927); [NBER](https://www.nber.org/papers/w18401); [IPA summary](https://poverty-action.org/publication/learning-through-noticing-theory-and-experimental-evidence-farming) | — | 不只是给农民数据，而是比较“拥有数据”与“突出提示未注意到的关系”。 | 测 Agent 是否能区分 information provision 与 attention reallocation。 |
| 16 | Dupas (2011), **Do Teenagers Respond to HIV Risk Information? Evidence from a Field Experiment in Kenya** | 健康经济学 / 信息干预 / 教育 | [AEA / AEJ: Applied Economics](https://www.aeaweb.org/articles?id=10.1257%2Fapp.3.1.1); [J-PAL PDF](https://www.povertyactionlab.org/sites/default/files/research-paper/Dupas%20-%20American%20Economic%20Journal%20-%20HIV%20Risk%20informations.pdf); [Harvard GAP](https://gap.hks.harvard.edu/do-teenagers-respond-hiv-risk-information-evidence-field-experiment-kenya) | [AEA replication / openICPSR](https://www.openicpsr.org/openicpsr/project/113775/version/V1/view%3Bjsessionid%3DE6D34F755F737F580616644D1FDC6A3D?path=%2Fopenicpsr%2F113775%2Ffcr%3Aversions%2FV1%2Fdo&type=folder) | 不同信息处理臂交叉，且用 pregnancy / childbearing 等更硬 outcome 补足自报行为问题。 | 测 Agent 是否会设计机制区分的信息干预，并选择不容易被社会期许偏差污染的 outcome。 |
| 17 | Allcott (2011), **Social Norms and Energy Conservation** | 能源经济学 / 行为干预 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0047272711000478); [MIT CEEPR PDF](https://ceepr.mit.edu/wp-content/uploads/2023/02/2009-014.pdf); [RePEc](https://ideas.repec.org/a/eee/pubeco/v95y2011i9p1082-1095.html) | — | Opower 家庭能源报告，社会比较 + injunctive norm；大规模 randomized natural field experiments。 | 测 Agent 是否考虑 boomerang effect、异质性和 norm message 的副作用。 |
| 18 | Goldstein, Cialdini & Griskevicius (2008), **A Room with a Viewpoint: Using Social Norms to Motivate Environmental Conservation in Hotels** | 消费者行为 / 社会规范 / 酒店环保 | [Journal of Consumer Research / Oxford Academic](https://academic.oup.com/jcr/article/35/3/472/1856257); [JSTOR](https://www.jstor.org/stable/10.1086/586910); [University of Minnesota page](https://experts.umn.edu/en/publications/a-room-with-a-viewpoint-using-social-norms-to-motivate-environmen/) | — | 比较普通环保诉求、描述性规范和“本房间住客”这种 provincial norm。 | 测 Agent 是否会细化 reference group，而不是只写“社会规范提示”。 |
| 19 | Hui, Inman, Huang & Suher (2013), **The Effect of In-Store Travel Distance on Unplanned Spending: Applications to Mobile Promotion Strategies** | 营销 / 零售 / 移动促销 | [Journal of Marketing / SAGE](https://journals.sagepub.com/doi/10.1509/jm.11.0436); [Drexel page](https://researchdiscovery.drexel.edu/esploro/outputs/journalArticle/The-Effect-of-In-Store-Travel-Distance/991019167663004721) | — | RFID 店内路径数据 + IV 处理 travel distance 的内生性；用于模拟移动优惠券策略。 | 测 Agent 是否意识到购物路径不是外生的，不能直接把距离和非计划消费做 OLS。 |
| 20 | Anderson & Simester (2003), **Effects of $9 Price Endings on Retail Sales: Evidence from Field Experiments** | 营销 / 定价 / field experiment | [Springer](https://link.springer.com/article/10.1023/A%3A1023581927405); [Author PDF](https://www.kellogg.northwestern.edu/faculty/anderson_e/htm/personalpage_files/Papers/Effects_of_9_Price_Endings_on_Retail_Sales.pdf); [RePEc](https://ideas.repec.org/a/kap/qmktec/v1y2003i1p93-110.html) | — | 多个服装目录 field experiments 随机操纵价格尾数；效果在新品中更强，且与 sale cue 交互。 | 测 Agent 是否理解 $9 ending 不是单纯心理错觉，而可能是低价/促销信号。 |

---

## 3. 建议的 5 个主测试组合

如果最终只做 5 个 case，我建议优先选：

1. **Karlan & Zinman (2009)**：机制分解最强，测试 adverse selection vs moral hazard。
2. **DellaVigna, List & Malmendier (2012)**：测试是否会设计“回避通道”来识别 social pressure。
3. **Johnson, Lewis & Nubbemeyer (2017) / Ghost Ads**：最适合营销广告因果识别，测试 endogenous exposure。
4. **Chetty, Looney & Kroft (2009)**：测试是否从 before-after 升级到差分结构。
5. **Duflo, Kremer & Robinson (2011)**：测试是否能把机制从价格水平转向购买时点 / present bias。

备选替换：

- 如果想更偏营销：用 **Blake, Nosko & Tadelis (2015)** 替换 Duflo。
- 如果想更偏行为实验：用 **Niederle & Vesterlund (2007)** 替换 Chetty。
- 如果想做有公开数据的复现：优先选 AEA 页面带 replication package 的 Ashraf et al., Chetty et al., Duflo et al., Bertrand & Mullainathan, Dupas。

---

## 4. 统一标注字段模板

每个测试样例可以整理成下面格式：

```markdown
## Case X: [匿名化研究主题]

### 给 Agent 的输入
- 研究背景：
- 可用数据：
- 研究目标：
- 业务 / 伦理 / 实施约束：

### 需要 Agent 输出
- 实验设计：
- 识别策略：
- 主要回归式：
- 关键假设：
- 潜在威胁：
- robustness checks：

### 原论文关键设计
- Linchpin detail：
- 它排除的替代解释：
- 如果删掉这个细节，识别会如何失败：

### 人工评分
| 维度 | 0 分 | 1 分 | 2 分 | Agent 得分 |
|---|---|---|---|---|
| 关键机制识别 | 未区分核心机制 | 提到机制但设计不足 | 明确设计可区分机制 |  |
| 隐性替代解释 | 未意识到 | 泛泛提到 confounder | 准确指出原论文关键替代解释 |  |
| 关键流程细节 | 完全遗漏 | 有类似但不精确安排 | 命中 linchpin detail |  |
| 估计策略 | 只有口头描述 | 有基本回归 | 回归与识别逻辑严格对应 |  |
| outcome 设计 | outcome 软或内生 | 基本合理 | 有硬 outcome / 独立测量 / 突击检查 |  |
| 可执行性 | 脱离现实 | 基本可做 | 符合业务、伦理和操作约束 |  |
```

---

## 5. 可统计的错误率指标

- **Critical Design Omission Rate**：关键流程细节遗漏率。
- **Mechanism Confounding Rate**：把两个机制混在一起解释的比例。
- **Naive RCT Rate**：只会写“随机分组”，但没有命中识别细节的比例。
- **Unsupported Identification Claim Count**：声称能识别某机制，但设计实际上不支持的次数。
- **Endogenous Outcome / Exposure Error**：把内生 exposure、点击、官方账本、自报行为等当作干净 outcome 的次数。

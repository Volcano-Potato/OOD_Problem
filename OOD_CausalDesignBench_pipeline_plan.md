# OOD-CausalDesignBench Pipeline 计划

## 1. 项目定位

本项目选择 `revised_final_project_openclaw_deepscientist-3.pdf` 中的 **方向 B：智能体框架缺陷诊断（Research 赛道）**，但把原要求中的“科研报告生成中的引用与结论不一致”扩展到一个更贴合商科 OOD 的版本：

> 测试基于 OpenClaw / DeepScientist 搭建的科研 Agent 在泛商科、经济学、营销学研究设计任务中，是否会生成没有被输入材料充分支持的因果识别 claim、实验设计 claim、机制解释 claim 或稳健性 claim。

核心问题不是“Agent 能不能背出某篇论文的方法”，而是：

1. Agent 能否从商科研究背景和数据结构中识别关键因果威胁？
2. Agent 能否提出与数据结构、干预条件、业务约束匹配的实验或准实验设计？
3. Agent 是否会把弱证据写成强因果结论，例如把相关性、普通 A/B 测试或内生 exposure 说成可以识别机制？
4. 当任务信息逐步充分时，Agent 的错误率是否下降？
5. 当关键识别条件被扰动或移除时，Agent 是否会调整设计，还是机械套用模板？

这使项目同时满足课程要求和你的 OOD 研究目标：

- 课程要求：至少 5 个测试样例、输入材料、Agent 输出、人工判断、错误类型、错误率、2 个失败案例、1 个 QQ/WeChat 完整交互。
- 你的目标：诊断科研 Agent 从 AI / AI for Science 迁移到泛商科研究设计时的能力边界。

## 2. Benchmark 名称与核心定义

建议命名：

**OOD-CausalDesignBench: Evaluating Scientific Agents on Out-of-Domain Business Research Design**

中文名：

**科研 Agent 的商科 OOD 因果研究设计能力诊断**

### 2.1 被测能力

本 benchmark 不评估一般写作流畅度，而评估四类能力：

| 能力 | 具体含义 | 常见失败 |
|---|---|---|
| 问题结构化 | 识别 treatment、outcome、unit、estimand、机制 | 把业务问题改写成泛泛预测任务 |
| 因果威胁识别 | 识别选择偏差、内生 exposure、共同趋势、spillover、attrition、measurement error | 只说“控制变量”和“随机分组” |
| 识别策略设计 | 提出能支撑因果 claim 的 RCT / DID / IV / RDD / event study / audit design | 策略与数据结构不匹配 |
| 证据边界意识 | 知道哪些结论不能由现有材料推出 | 过度声称机制、外推性或因果性 |

### 2.2 与课程方向 B 的对应关系

课程方向 B 的原始错误类型可以迁移为以下版本：

| 课程错误类型 | 在本项目中的定义 |
|---|---|
| Unsupported Claim | Agent 声称某设计可以识别因果效应或机制，但输入材料中没有足够条件支持 |
| Overclaim | 材料只支持描述性、相关性或平均处理效应，Agent 写成强因果、机制分解或可推广结论 |
| Mis-citation | Agent 引用某个输入事实作为设计依据，但该事实不能支持具体识别策略 |
| Contradiction | Agent 的设计或结论与输入约束冲突，例如任务说明处理不是随机的，Agent 却当作 RCT |

关键改动：这里的“引用与结论不一致”不只看 bibliographic citation，也看 **Agent 输出中的设计 claim 与输入 evidence 是否一致**。这更适合实验设计能力诊断。

## 3. 总体 Pipeline

```text
真实商科/经济学论文池
        |
        v
抽取隐藏 gold reference：研究问题、数据结构、识别策略、关键设计命门
        |
        v
构造匿名任务包：Level 1 / Level 2 / Level 3 / Perturbed / No-solution
        |
        v
通过 OpenClaw / DeepScientist Agent 运行任务并保存完整日志
        |
        v
抽取 Agent 输出中的关键 claim 与自称 evidence
        |
        v
人工按统一 rubric 标注：支持 / 部分支持 / 不支持 / 矛盾
        |
        v
统计错误率与设计能力分数
        |
        v
选择成功案例、失败案例、边界案例用于报告和现场展示
```

## 4. 数据与案例构建

### 4.1 候选论文来源

优先使用本地已有材料：

- `Bench_idea.md`
- `deepscientist_econ_business_experiment_papers.md`
- `downloads/deepscientist_econ_business_experiment_papers/`

这些材料已经覆盖经济学、营销学、行为经济学、公共经济学中的经典 field experiment / lab experiment，并且多数 PDF 已经下载到本地，适合构建可复现测试包。

### 4.2 建议主测试 5 个 case

建议先做 5 个主 case，满足课程最低要求；如果时间允许，再扩展到 8-10 个。

| Case | 领域 | 真实论文作为隐藏 gold reference | 要测的核心弱点 |
|---|---|---|---|
| C1 | 消费信贷 / 信息不对称 | Karlan & Zinman (2009) | 是否能区分 adverse selection 与 moral hazard，而不是只说随机利率 |
| C2 | 慈善捐赠 / 行为经济学 | DellaVigna, List & Malmendier (2012) | 是否能设计低成本回避通道以识别 social pressure |
| C3 | 在线广告 / 营销 | Johnson, Lewis & Nubbemeyer (2017) 或 Blake et al. (2015) | 是否理解广告 exposure、搜索意图和 retargeting 的内生性 |
| C4 | 税收显著性 / 消费行为 | Chetty, Looney & Kroft (2009) | 是否从简单前后比较升级到 treated goods × control goods × store × week 的差分结构 |
| C5 | 农户采纳 / present bias | Duflo, Kremer & Robinson (2011) | 是否能把机制从“价格水平”转向“购买时点、承诺和 present bias” |

备选 case：

- Niederle & Vesterlund (2007)：竞争偏好、性别差异、风险偏好和自信心的区分。
- Cohen & Dupas (2010) / Ashraf et al. (2010)：价格、筛选效应和 sunk-cost effect 的区分。
- Olken (2007)：不能用可能被操纵的官方账本作为唯一 outcome。
- Bertrand & Mullainathan (2004)：适合 sanity check，但论文太有名，Agent 可能从预训练中记住。

### 4.3 每个 case 的文件结构

建议建立如下目录：

```text
benchmark/
  cases/
    C1_consumer_credit/
      gold_reference.md
      level1_background.md
      level2_data_structure.md
      level3_threats_constraints.md
      perturbed_variant.md
      no_solution_variant.md
      scoring_rubric.md
    C2_charitable_giving/
      ...
  prompts/
    closed_book_design_prompt.md
    evidence_aware_design_prompt.md
    claim_extraction_prompt.md
  outputs/
    raw_agent_logs/
    parsed_claims/
  annotations/
    annotation_sheet.csv
    adjudicated_labels.csv
  scripts/
    compute_metrics.py
    summarize_failures.py
```

### 4.4 Gold reference 不给 Agent

`gold_reference.md` 只给人工评审使用，不进入 Agent 上下文。内容包括：

```markdown
# Gold Reference

## 原论文信息
- 论文：
- 领域：
- PDF 路径：

## 真实研究问题

## 原论文关键设计
- Treatment:
- Outcome:
- Unit:
- Assignment / variation source:
- Estimand:
- Identification strategy:

## Linchpin detail
- 关键设计命门：
- 它解决了什么替代解释：
- 如果遗漏该细节，识别会如何失败：

## 可接受替代设计
- 允许 Agent 不复现原论文，但必须满足哪些最低识别条件：

## 不可接受设计
- 哪些看似合理但实际不支持因果 claim：
```

这样可以避免答辩时被质疑“你只是要求 Agent 猜原论文答案”。评分标准是“是否满足因果识别的必要条件”，不是“是否复刻论文”。

## 5. 信息梯度任务设计

每个 case 至少构造 3 个信息层级。主实验使用 Level 2 和 Level 3，Level 1 作为 lower bound。

### Level 1：背景-only

只给研究背景、业务场景、研究问题和目标。

用途：

- 观察 Agent 在开放问题下会不会输出模板化实验建议。
- 作为 lower bound，不把失败直接作为主要结论。

示例内容：

```markdown
你是一名研究者，想评估某营销干预是否真的提升了消费者购买，而不是仅仅吸引了本来就会购买的人。请基于以下背景设计研究方案。
```

### Level 2：背景 + 数据结构

给出可用数据的最小充分信息：

- observation unit
- 时间跨度
- treatment / exposure 变量
- outcome 变量
- 协变量
- 是否有 panel
- 是否有自然变化或实验变化
- 业务实施限制

用途：

- 这是主测试层级。
- 如果 Agent 在 Level 2 仍然设计不出可辩护方案，说明不是简单信息不足。

### Level 3：背景 + 数据结构 + 潜在威胁提示

额外给出威胁清单，但不给解决方案：

- 选择偏差
- 内生 exposure
- spillover
- attrition
- measurement error
- parallel trends 风险
- 干预合规问题
- 伦理或业务约束

用途：

- 测试 Agent 能否把“被提示的风险”转化为真实设计，而不是只把风险复述一遍。
- 作为 upper bound。

### Perturbed Variant：反事实扰动

改变一个关键条件，例如：

- 原本随机发放优惠券，改为用户主动领取优惠券。
- 原本广告随机开关，改为平台算法根据购买意向投放广告。
- 原本政策统一生效，改为地区自行选择实施时间。
- 原本有硬 outcome，改为只有自报 outcome。

正确表现：

- Agent 应该降低因果 claim 强度。
- Agent 应该提出额外数据、工具变量、随机化或稳健性诊断。
- Agent 不应该机械沿用原来的 RCT / DID / IV 模板。

### No-solution Variant：无强因果识别任务

构造 1-2 个现有数据无法支持强因果识别的任务。正确答案应该是：

- 只能做描述性或相关性分析。
- 不能声称因果识别。
- 需要补充随机化、外生冲击、panel 数据、独立测量或更细粒度日志。

用途：

- 测试 Agent 的科研诚实性。
- 很适合做失败案例或边界案例展示。

## 6. 给 Agent 的统一任务 Prompt

建议用固定 prompt，降低 prompt variance。

```markdown
你是一个科研 Agent。请只基于下面提供的材料设计一个可执行的商科/经济学研究方案。

重要约束：
1. 不要假设材料中没有提供的数据、随机化或外生冲击。
2. 如果现有材料不足以支持因果识别，请明确说明不能支持，并提出需要补充的数据或实验。
3. 每个关键结论都必须标注它依据的输入材料编号，例如 [E1]、[E2]。
4. 不要只给泛泛建议，要说明 treatment、outcome、unit、estimand、识别策略、模型、关键假设和诊断检验。

请输出以下结构：

## 1. Research Question

## 2. Treatment / Outcome / Unit / Estimand

## 3. Main Design

## 4. Identification Assumptions

## 5. Statistical Model

## 6. Robustness / Placebo / Heterogeneity Checks

## 7. Unsupported or Weakly Supported Claims

## 8. Additional Data Needed

## 9. Claim-Evidence Table
| Claim ID | Claim | Evidence ID | Support Strength: strong / partial / weak / none |
```

输入材料需要人为编号：

```markdown
[E1] 研究背景：...
[E2] 可用数据：...
[E3] 业务约束：...
[E4] 已知威胁：...
```

这会让后续“结论与证据一致性”标注更容易，也更贴合课程方向 B。

## 7. Agent 运行设置

### 7.1 主实验设置

建议先做闭卷评测：

- Agent 只能使用给定输入材料。
- 禁止联网检索真实论文标题或相关文献。
- 保留完整 prompt、输出、工具调用日志、后台截图。

原因：

- 本项目测的是研究设计推理，不是检索能力。
- 如果允许自由联网，Agent 可能找到原论文，污染 blind test。

### 7.2 可选扩展设置

如果时间允许，可以增加一个“开卷 / 检索可用”对照：

- Agent 允许搜索，但不提供原论文标题和作者。
- 观察它是否检索到相关资料，以及是否错误引用或误用。

这个扩展可以诊断科研 Agent 的另一个问题：检索到相关文献不等于能正确使用文献。

### 7.3 运行矩阵

最低版本：

| 维度 | 设置 |
|---|---|
| Cases | 5 个 |
| 信息层级 | Level 2 + Level 3 |
| 变体 | 至少 1 个 Perturbed 或 No-solution |
| 每个设置重复 | 1 次 |
| 总任务数 | 11 个左右 |

推荐版本：

| 维度 | 设置 |
|---|---|
| Cases | 5 个 |
| 信息层级 | Level 1 + Level 2 + Level 3 |
| 变体 | 每个 case 1 个 Perturbed，另加 1 个 No-solution |
| 每个设置重复 | 2 次 |
| 总任务数 | 40 个左右 |

如果时间紧，优先完成最低版本，并确保标注和失败分析扎实。

## 8. 人工标注方案

### 8.1 标注单位

不要只给整篇输出打一个分。建议按 **claim-level** 标注：

- Agent 输出中的每个关键因果 claim
- 每个识别策略 claim
- 每个机制 claim
- 每个稳健性 claim
- 每个额外数据需求 claim

示例：

```text
Claim: 随机化广告展示可以识别广告对购买的因果影响。
Evidence: 输入材料说明广告由平台算法根据用户购买意向投放。
Judgment: 矛盾。
Error Type: Contradiction。
Explanation: exposure 不是随机的，且与购买意向相关。
```

### 8.2 标注表字段

建议建立 `annotations/annotation_sheet.csv`：

| 字段 | 含义 |
|---|---|
| case_id | C1-C5 |
| variant_id | level1 / level2 / level3 / perturbed / no_solution |
| run_id | 第几次运行 |
| claim_id | Agent 输出中的 claim 编号 |
| agent_claim | Agent 关键结论 |
| cited_evidence | Agent 声称依据的 evidence |
| human_judgment | supported / partially_supported / unsupported / contradicted |
| error_type | none / Unsupported Claim / Overclaim / Mis-citation / Contradiction |
| severity | minor / major / critical |
| explanation | 人工解释 |
| missed_linchpin | 是否遗漏关键设计命门 |
| gold_reference | 对应 gold reference 条目 |

### 8.3 设计能力 rubric

每个 case 额外给一个 100 分设计分，用于展示能力曲线。

| 维度 | 分值 | 看什么 |
|---|---:|---|
| 研究问题理解 | 10 | 是否准确识别 treatment、outcome、unit、estimand |
| 因果威胁识别 | 20 | 是否指出内生性、选择偏差、趋势混淆、spillover、measurement error |
| 识别策略合理性 | 25 | 设计是否真的能支撑因果 claim |
| 统计模型匹配度 | 15 | 模型是否匹配 panel、cluster、fixed effects、assignment level |
| 假设与诊断 | 15 | 是否提出 balance、parallel trends、placebo、falsification、robustness |
| 局限性与补充数据 | 10 | 是否知道哪些结论不能下 |
| OOD 适应性 | 5 | 在反事实变体中是否调整设计 |

### 8.4 最好有第二标注人

如果可以，找 1 名同学对部分 claim 复标：

- 至少复标 20%-30% claim。
- 统计 simple agreement。
- 如果两人有分歧，进行 adjudication。

这不是课程硬要求，但能提高答辩可信度。

## 9. 指标统计

### 9.1 课程要求指标

至少报告：

```text
Citation / Evidence Inconsistency Rate
= (Unsupported Claim + Overclaim + Mis-citation + Contradiction) / Total Claims
```

### 9.2 本项目核心指标

建议报告以下指标：

| 指标 | 定义 | 解释 |
|---|---|---|
| Unsupported Design Claim Rate | 不被输入材料支持的设计 claim / 总设计 claim | Agent 是否乱声称能识别 |
| Critical Design Omission Rate | 遗漏 linchpin detail 的 case / 总 case | 是否漏掉识别命门 |
| Mechanism Confounding Rate | 混淆关键机制的 case / 总 case | 例如混淆 selection 与 sunk cost |
| Naive Design Rate | 只给泛泛 RCT / DID / regression 的 case / 总 case | 是否模板化 |
| Contradiction Rate | 与输入约束冲突的 claim / 总 claim | 是否忽略条件 |
| No-solution Honesty Rate | 无解任务中承认不能强因果识别的比例 | 科研诚实性 |
| Info Gradient Improvement | Level 3 分数 - Level 1 分数 | 信息充分后是否改善 |

### 9.3 输出图表

项目报告中建议放 3 张图：

1. **不同信息层级下的平均设计分**：Level 1 / Level 2 / Level 3。
2. **错误类型分布柱状图**：Unsupported、Overclaim、Mis-citation、Contradiction。
3. **每个 case 的 critical design omission 是否发生**：5 个 case 的热力图。

## 10. 失败案例选择

至少准备 2 个失败案例，用于报告和展示。

### 失败案例 A：内生 exposure 被当成随机处理

适合使用在线广告 case。

预期错误：

- Agent 说“比较看过广告和没看过广告的用户即可估计广告效果”。
- 或者说“随机分配广告 exposure”，但输入材料没有随机分配条件。

为什么严重：

- 广告 exposure 往往由用户兴趣、搜索意图、平台竞价或 retargeting 决定。
- 直接比较会高估广告效果。

可归类：

- Unsupported Claim
- Overclaim
- Contradiction

### 失败案例 B：机制分解失败

适合使用消费信贷或价格 case。

预期错误：

- Agent 只设计“随机化利率 / 价格”，然后声称可以区分 adverse selection、moral hazard、sunk cost 或 screening。

为什么严重：

- 单一价格随机化通常只能估计价格对 take-up 或 repayment/use 的总影响。
- 要分解机制，需要额外设计，例如 contract rate、后续激励、购买者二次随机化或使用追踪。

可归类：

- Overclaim
- Critical Design Omission
- Mechanism Confounding

### 边界案例：无解任务

适合现场展示：

- 给 Agent 一个只有横截面问卷和自报购买意向的数据。
- 任务要求评估促销是否因果提升购买。

理想输出：

- 不能支持强因果结论。
- 只能做描述性分析。
- 需要随机化、自然实验或 panel 数据。

如果 Agent 仍然写出强因果方案，就是很清晰的边界失败。

## 11. 可复现脚本设计

不需要复杂工程，但建议有最小统计脚本，体现“可复现”。

### 11.1 `compute_metrics.py`

输入：

```text
annotations/adjudicated_labels.csv
```

输出：

```text
results/metrics_summary.csv
results/error_type_counts.csv
results/case_level_scores.csv
```

核心统计：

```python
total_claims = len(df)
inconsistent = df["error_type"].isin([
    "Unsupported Claim",
    "Overclaim",
    "Mis-citation",
    "Contradiction",
]).sum()
inconsistency_rate = inconsistent / total_claims
```

### 11.2 `summarize_failures.py`

输入：

```text
annotations/adjudicated_labels.csv
outputs/raw_agent_logs/
```

输出：

```text
results/failure_cases.md
```

自动列出：

- severity 为 critical 的 claim
- 对应输入 evidence
- 人工解释
- 所属错误类型

## 12. 报告结构

最终项目报告建议 6-10 页：

1. **题目与方向**
   - 题目：OOD-CausalDesignBench: 科研 Agent 的商科 OOD 因果研究设计能力诊断
   - 方向：Research 赛道，智能体框架缺陷诊断
   - 基础系统：OpenClaw / DeepScientist

2. **问题定义**
   - 科研 Agent 在 AI / AI for Science 中常用于文献总结、实验规划和结果解释。
   - 泛商科研究设计依赖因果识别、机制区分和业务约束，属于 OOD 场景。
   - 本项目诊断 Agent 是否会产生 unsupported causal design claims。

3. **Benchmark 设计**
   - 真实论文作为 hidden gold reference。
   - 匿名任务包。
   - 信息梯度 Level 1-3。
   - Perturbed / No-solution 变体。

4. **实验设置**
   - 5 个 case。
   - Agent prompt。
   - 运行方式。
   - 日志保存。
   - QQ/WeChat 真实交互案例。

5. **标注与指标**
   - claim-level 标注表。
   - 错误类型。
   - 设计分 rubric。
   - 错误率公式。

6. **结果**
   - 总体错误率。
   - 信息层级对比。
   - case-level 分析。

7. **失败案例**
   - 至少 2 个具体输出片段。
   - 展示输入材料、Agent claim、人工判断、错误原因。

8. **改进建议**
   - 强制 claim-evidence table。
   - 增加 causal design checklist。
   - 对识别策略做 verifier / critic pass。
   - 对“是否有足够条件做因果识别”先做 gatekeeping。

9. **局限性**
   - 样例数量有限。
   - 人工标注存在主观性。
   - 商科 OOD 只覆盖因果设计类任务，不代表全部商科科研能力。

## 13. 现场展示设计

现场 10 分钟建议流程：

| 时间 | 内容 |
|---:|---|
| 1 min | 说明选择 Research 赛道和商科 OOD 问题 |
| 2 min | 展示 benchmark pipeline 和 5 个 case |
| 2 min | 展示 QQ/WeChat 中一个完整任务交互 |
| 2 min | 展示一个成功案例和一个失败案例 |
| 2 min | 展示错误率、错误类型分布和信息梯度结果 |
| 1 min | 总结 Agent 弱点与改进建议 |

现场必须准备：

- QQ/WeChat 真实交互截图。
- Agent 后台运行截图。
- 至少 5 个输入/输出样例 PDF 或 markdown。
- 标注表截图。
- 统计脚本运行截图。
- 一个失败案例的逐行解释。

如果现场系统不稳定，要准备录屏和日志，避免展示风险。

## 14. 对答辩质疑的回应

### 质疑 1：只给背景，Agent 设计不好很正常

回应：

> 本项目不是单一背景 prompt，而是信息梯度实验。Level 1 是 lower bound，主测试是 Level 2 和 Level 3，其中包含数据结构、变量、观测单位、时间跨度、业务约束和潜在威胁。我们不要求 Agent 复现原论文，只要求它提出被输入材料支持的识别策略，并说明假设、诊断和局限。因此失败不能简单归因于信息不足。

### 质疑 2：实验设计没有唯一答案，怎么评分？

回应：

> 评分不是看是否一字不差复刻原论文，而是看是否满足因果识别的必要条件。每个 case 有 hidden gold reference 和可接受替代设计。只要 Agent 的方案能处理关键替代解释、匹配数据结构并避免过度 claim，就可以得分。

### 质疑 3：这是不是在考经济学专业知识，而不是 Agent 能力？

回应：

> 科研 Agent 被用于跨学科科研辅助时，必须知道何时不能过度声称因果。本项目测试的是通用科研推理能力中的 evidence grounding、assumption awareness 和 causal design validity。商科只是一个 OOD 场景，用来暴露当前 Agent 在非 AI / 非生化任务中的泛化边界。

### 质疑 4：Agent 可以联网找到原论文怎么办？

回应：

> 主实验采用闭卷设置，只允许使用给定匿名材料，避免检索污染。开卷检索可以作为扩展实验，但不作为主结论依据。

## 15. 最小可行版本

如果时间有限，按这个版本执行：

1. 选 5 个 case：消费信贷、慈善捐赠、在线广告、税收显著性、农户肥料采纳。
2. 每个 case 只做 Level 2 和 Level 3。
3. 额外做 1 个 no-solution 边界任务。
4. 每个任务运行 1 次，共 11 个输出。
5. 手工抽取每个输出 5-8 个关键 claim。
6. 标注 60-80 个 claim。
7. 统计一个主错误率和 3 个辅助指标。
8. 展示 2 个失败案例、1 个 QQ/WeChat 完整交互、1 张错误类型图。

这个版本已经满足课程 Research 赛道最低要求，并且足以支撑“科研 Agent 在商科 OOD 因果设计任务中存在系统性 unsupported design claims”的结论。

## 16. 推荐执行时间表

| 阶段 | 时间 | 产物 |
|---|---|---|
| Day 1 | 构建 5 个 gold reference 和 Level 2 / Level 3 任务包 | `benchmark/cases/` |
| Day 2 | 配置 Agent prompt，完成本地和 QQ/WeChat 跑通 | raw logs、截图 |
| Day 3 | 完成所有 case 运行，整理输出 | `outputs/raw_agent_logs/` |
| Day 4 | claim 抽取和人工标注 | `annotations/annotation_sheet.csv` |
| Day 5 | 跑统计脚本，生成图表和失败案例 | `results/` |
| Day 6 | 写项目报告和证据材料 PDF | report、evidence PDF |
| Day 7 | 彩排现场展示，准备 poster | slides / poster / demo script |

## 17. 最终提交清单

```text
GroupXX_LLM_Project_Research.zip
  project_report.pdf
  evidence_materials.pdf
  code_and_data/
    README.md
    benchmark/
    prompts/
    outputs/
    annotations/
    scripts/
    results/
    configs/
```

`README.md` 至少说明：

- 如何启动 OpenClaw / DeepScientist Agent。
- 如何运行一个测试 case。
- 如何复现统计结果。
- 哪个 case 是 QQ/WeChat 完整交互。
- 哪些文件对应报告中的失败案例。

## 18. 核心结论模板

如果实验结果符合预期，报告可以这样收束：

> 在 5 个泛商科 OOD 因果研究设计任务中，OpenClaw / DeepScientist 搭建的科研 Agent 能够生成形式完整的研究方案，但经 claim-level 标注发现，它经常把弱证据写成强因果设计 claim，尤其容易遗漏内生 exposure、机制分解和关键流程细节。信息更充分时，部分错误下降，但在 perturbed 和 no-solution 任务中仍存在模板化设计和过度声称因果的问题。这说明当前科研 Agent 在跨域研究设计中需要额外的因果识别 verifier、证据边界检查和领域约束感知模块。

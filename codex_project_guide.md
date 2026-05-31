# Codex 协作指南：科研 Agent 计量模型设计缺陷诊断 Project

> 本文件用于本地 Codex 在协助改进本课程 Project 时参阅。所有设计决策须遵循下述原则；如需偏离请显式说明理由。

---

## 0. 一句话定位（开场白 / single sentence pitch）

> *Bottleneck 论文把 AI 经济学论文质量分解为 idea 和 execution，发现 71%/29% 的 gap 分布。本 project 在**控制 idea**之后，把 execution 这 29% 进一步分解到具体的 **econometric design errors**，并通过 **trap-augmented sampling** 在小样本里放大可观察的 failure modes。*

写引言、做 poster、做现场答辩开场都从这句出发。**不与 ETH APE 或 Ideation Bottleneck 竞争 novelty，定位为 Bottleneck 的细颗粒度续集。**

---

## 1. 项目基本信息

- **课程**：《大语言模型：从原理到应用》期末 Project
- **方向**：方向 B（Research 赛道）—— 智能体框架缺陷诊断
- **基础系统**：OpenClaw 搭建的科研 Agent
- **任务调整**：原方向 B 模板针对的是"引用与结论不一致"问题；本 project 将其**重新映射**为"计量模型设计缺陷"，需要在报告中明确说明这一映射逻辑
- **交付要求摘要**：
  - 至少 5 个测试样例（建议做到 8–12 个）
  - 至少 1 个样例必须通过 QQ 或 WeChat 真实完成
  - 错误分类与统计
  - 至少 2 个失败案例
  - 可复现的评测材料、日志、配置
  - PDF 报告（6–10 页） + 代码工程目录 + 证据材料 PDF
  - 现场展示 10 分钟 + 问答 5 分钟 + Poster (120×80cm)

---

## 2. 理论参考与引用义务

本 project 的方法论扎根于以下两个工作，引用是**必须的**，不是装饰：

1. **Li Ning (2026). "The Ideation Bottleneck: Decomposing the Quality Gap Between AI-Generated and Human Economics Research."** Tsinghua University.
   - 核心发现：AI vs Human paper 的 quality gap 中，71% 来自 idea，29% 来自 execution
   - 关键观察：74% 的 AI papers 默认使用 DiD
   - Execution 六维度：Identification / Econometrics / Mechanism / Robustness / Data Quality / Writing
   - Execution 维度差距：Mechanism d=1.43，Data Quality d=1.05，Robustness d=0.08（无显著差异）

2. **ETH Social Catalyst Lab. Project APE (Autonomous Policy Evaluation).** https://ape.socialcatalystlab.org/
   - 912 篇 AI 生成的经济学论文 corpus
   - Tournament 形式的 head-to-head 评估
   - LLM judge: Gemini 3.1 Flash Lite

3. **辅助引用**（增强报告说服力）：
   - Angrist & Pischke (2010), "The Credibility Revolution in Empirical Economics"
   - Callaway & Sant'Anna (2021); de Chaisemartin & D'Haultfœuille (2020); Goodman-Bacon (2021) —— modern staggered DiD critiques
   - Abadie et al. (2023), clustering for inference

---

## 3. 从 Bottleneck + APE 提炼的 10 条操作准则

Codex 协助生成任何 prompt / 样例 / 评估脚本时，须遵循这些原则。

### 来自 Ideation Bottleneck

**P1. 匿名化是控制变量，不是省略信息。**
匿名化 checklist（每个样例须过一遍）：
- [ ] 去除所有估计量名称（DiD, RDD, IV, 2SLS, fixed effects 等）
- [ ] 去除 specification 形式（"log-linear", "interaction term"）
- [ ] 去除变量层级与 cluster 单位提示
- [ ] 去除 SE 类型提示（"clustered at firm level"）
- [ ] 去除 I.V. 暗示词（"exogenous shock", "natural experiment", "shift-share"）
- [ ] 去除 cutoff/threshold/discontinuity 等暴露 RDD 的关键词
- [ ] 去除 "quasi-experimental", "panel data 2010–2020" 等隐式 hint

输出格式遵循 Bottleneck 的 **120–150 词结构化段落**：phenomenon / gap / question / strategy（高层次）/ contribution。

**P2. LLM judge 不换模型、不换 prompt。**
- 选定一个 judge model（推荐：**与 OpenClaw 底层 LLM 不同源**的模型，避免同源偏差）
- 从第一个样例到最后一个样例使用同一个 model version + 同一套 scoring prompt
- 在报告中 disclose model version、prompt 全文、调用日期

**P3. 报 effect size，不只报 percentage。**
- 错误率须配 conditional comparison（trap vs non-trap 的对比，或不同领域的对比）
- 鼓励使用 Cohen's d 或胜率差

**P4. 把 Robustness 无差距当减法信号。**
- 不要把测评精力花在"Agent 会不会做 robustness checks"上（Bottleneck 已证明 d=0.08，无差）
- 聚焦：**Identification Strategy** 和 **Mechanism Analysis**（d=1.43 和 d=1.05，最大差距）

**P5. 寻找一个 quantifiable structural pattern 当 headline finding。**
候选 headline metric：
- "在 K 个该用 RDD 的 trap 里 Agent 选 DiD 的比例"
- "Agent 提到 Callaway-Sant'Anna 或 de Chaisemartin 的比例"
- "Agent 主动检验 parallel trend 的比例"
- "Agent 在 staggered treatment 场景下用 naive TWFE 的比例"

挑一个最 striking 的数字放 poster 标题位 + 报告 abstract 第一句。

**P6. 用 discriminant validity 验证错误分类。**
- 抽 20+ 个 case，由 2 人独立标注
- 计算 inter-rater agreement（Cohen's kappa）
- 若两类总被混标，合并

### 来自 APE

**P7. 全流程可复现归档。**
仓库目录结构（Codex 须遵循）：
```
project_root/
├── anonymized_descriptions/      # 匿名化后的研究描述
│   ├── case_001.md
│   └── ...
├── source_papers/                # 原始 paper 元信息（标题、DOI、真实方案摘要）
│   └── case_metadata.csv
├── agent_outputs/                # Agent 的原始输出
│   ├── case_001_raw.txt
│   └── case_001_log.json
├── judge_scorings/               # LLM judge 的评分
│   ├── case_001_judgment.json
│   └── judge_prompt.md
├── human_annotations/            # 人工标注
│   └── annotations.csv
├── analysis_scripts/             # 统计分析脚本
│   ├── compute_error_rates.py
│   └── make_radar_chart.py
├── prompts/                      # 所有 Agent / judge 用到的 prompt
├── results/                      # 最终图表
└── README.md                     # 安装、运行、复现说明
```

每个 case 用统一 ID（case_001 等）贯穿全程。

**P8. Head-to-head 优于 absolute scoring。**
核心评估须以 pairwise 形式进行：
- 同一研究问题
- 喂给 judge LLM 两个方案：(A) paper 真实方案 (B) Agent 方案
- judge 二选一（或六维度各选一次）
- **顺序随机化**：A/B 标签随机分配，避免 position bias
- 报告："Agent 方案在 X% 的 case 里被 judge 判为不如真实方案"

**P9. Paper 来源的 quality threshold。**
所有 source paper 限定：
- AER / AEJ:Applied / AEJ:Policy / QJE / JPE / REStud / Econometrica
- 发表年份：2019–2025（确保涉及 modern staggered DiD 讨论）
- 优先选 identification strategy 清晰、有明确 estimator 的 empirical papers

**P10. Scale 不必大，但要 > minimum。**
- N = 8–12 个 case
- 其中 3–4 个为 trap case
- 这是统计意义和工作量的平衡点

---

## 4. 错误分类系统（本 project 的核心贡献）

**不要使用原方向 B 模板的四分类**（Unsupported Claim / Overclaim / Mis-citation / Contradiction）—— 那是为 related work 任务设计的。

采用以下针对计量模型设计的分类（Codex 帮助标注时遵循）：

| 错误类型 | 定义 | 典型表现 |
|---------|------|---------|
| **E1. Identification Strategy Mismatch** | 大类策略选错 | 场景该用 RDD，Agent 选 DiD；该用 IV，Agent 直接 OLS |
| **E2. Identifying Assumption Violation** | 策略大类对，但 identifying assumption 不成立 | DiD 用于明显有 anticipation effect 或 pre-trend 违反的场景 |
| **E3. Specification Error** | fixed effects 层级、cluster、controls 错误 | 控制了 bad controls (post-treatment vars)；FE 层级错 |
| **E4. Inference Error** | 标准误、检验程序错误 | clustering level 错；忽视 multiple hypothesis testing |
| **E5. Modern Methods Ignorance** | 不 aware of post-2020 计量发展 | staggered treatment 用 naive TWFE，无视 Callaway-Sant'Anna 等 |
| **E6. Methodological Anchoring (DiD Default)** | 不分场合默认 DiD | 复现 Bottleneck 的 74% 发现 |

每个 case 可以打多个标签。

---

## 5. 样例设计：Trap-Augmented Sampling

### 5.1 普通样例（N ≈ 5）
- 从顶刊近 5 年文献随机取
- 涵盖多领域：labor / development / finance / health / public

### 5.2 Trap 样例（N ≈ 3–4，必须）

每个 trap 都是**故意构造的考察点**，提前预测 Agent 会犯哪类错误：

**Trap A：RDD 陷阱**
- 选政策按 cutoff（年龄、收入、考试分数）执行的真实 paper
- 描述时只说 phenomenon，不说 sharp/fuzzy threshold
- 预测：Agent default 选 DiD（→ E1, E6）

**Trap B：Parallel Trends Violation**
- 选 treated group 在政策前就有显著上升趋势的场景
- 描述中性，不暴露 pre-trend 问题
- 预测：Agent 选 DiD 且不检验平行趋势（→ E2）

**Trap C：Staggered Treatment**
- 选 treatment 在不同时间发生在不同单位的真实 paper
- 预测：Agent 用 naive TWFE，不提 Callaway-Sant'Anna / de Chaisemartin（→ E5）

**Trap D：IV 必要场景**
- 选明显有 self-selection / reverse causality 的研究问题
- 预测：Agent 直接 OLS 或简单 DiD 而不寻找 instrument（→ E1）

可选 **Trap E：Structural Necessity**
- 选 reduced form 无法回答（需要 welfare 计算）的福利评估问题
- 预测：Agent 不提 structural model

---

## 6. 评估流程（标准 pipeline）

```
Step 1: Source Paper Selection
   ↓
Step 2: Anonymization (P1 checklist)
   ↓
Step 3: Agent Prompt (统一模板，禁止 case 间变更)
   ↓
Step 4: Agent Output Collection (含完整日志)
   ↓
Step 5a: LLM Judge Scoring (六维度，P2 一致性)
Step 5b: Human Annotation (P6 双人标注)
Step 5c: Pairwise H2H (P8 Agent vs Paper 真实方案)
   ↓
Step 6: Error Classification (Section 4 体系)
   ↓
Step 7: Statistical Analysis (P3 effect size + headline metric)
   ↓
Step 8: Visualization (雷达图 + 错误热图 + DiD anchoring bar)
```

---

## 7. 工程实现要点（Codex 直接产出）

### 7.1 必备脚本
- `anonymize_check.py`：对照 P1 checklist 自动扫描描述文本是否泄漏关键词
- `agent_caller.py`：统一调用 OpenClaw 接口、记录完整日志
- `judge_runner.py`：统一调用 judge LLM、固定 prompt 和模型版本
- `pairwise_eval.py`：实现 P8，随机化 A/B 顺序
- `compute_metrics.py`：错误率、Cohen's d、胜率、conditional comparison
- `make_radar_chart.py`、`make_error_heatmap.py`：可视化

### 7.2 Prompt 模板规范
- Agent prompt：**保存为单独文件 `prompts/agent_design_prompt.md`**，所有 case 共用
- Judge prompt：**保存为单独文件 `prompts/judge_scoring_prompt.md`**
- 任何修改 prompt 须 commit，git log 须可追溯

### 7.3 Prompt Ablation（如时间允许，加分项）
对比三个版本的 Agent prompt：
1. **Naive**：只问 "Design the econometric model"
2. **Method-aware**：加 "Consider RDD / IV / Synthetic Control / structural alternatives before defaulting to DiD"
3. **Literature-aware**：加 modern DiD critiques 的简要 context

测错误率是否下降 → 把"诊断"升级为"诊断 + 可操作改进路径"。

---

## 8. 报告结构（6–10 页 PDF）

```
1. Introduction
   - 引 Ideation Bottleneck (71%/29% decomposition)
   - 引 APE
   - 定位本 project：控制 idea 后的 execution 精细诊断
   - 一句话 pitch（Section 0）

2. Related Work
   - Bottleneck / APE 简述
   - Modern DiD literature 简述
   - 与方向 B 标准模板的差异说明

3. Methodology
   - 匿名化协议（引 Bottleneck 的 120–150 词 protocol）
   - 错误分类系统（Section 4 表格放显眼位置）
   - Trap-augmented sampling 设计（Section 5）
   - 评估流程图（Section 6）

4. Results
   - Headline finding（P5 选定的 metric）
   - 雷达图：Agent 方案 vs Paper 真实方案
   - 错误类型分布（按领域 / 按 trap-vs-normal）
   - Pairwise H2H 胜率
   - （可选）Prompt ablation 结果

5. Failure Case Analyses (至少 2 个深度展开)
   - Trap A 失败案例完整复盘
   - 一个 normal case 的意外失败

6. Discussion
   - 与 Bottleneck 29% execution gap 的对话
   - 对 OpenClaw 的具体改进建议

7. Limitations
   - 样本量小（套用 Bottleneck 局限性章节句式）
   - LLM judge 偏差
   - 单一基础系统（OpenClaw）

8. Group Contribution Statement
```

---

## 9. 现场展示设计（30 分大头）

### 9.1 10 分钟流程
1. **Pitch**（1 min）：Section 0 那句话 + 一个 headline number
2. **方法快讲**（2 min）：匿名化协议 + 错误分类（用 poster 上的 figure 1）
3. **现场跑 1 个 trap**（3 min）：通过 QQ/WeChat，让 Agent 在现场设计 RDD 陷阱样例的方案
4. **结果展示**（2 min）：雷达图 + 错误率
5. **失败案例**（2 min）：Trap A 完整复盘

### 9.2 现场预案
- 至少彩排 1 次完整流程
- 准备录屏作为 fallback
- 准备 2 个 backup trap case，防止现场 Agent "突然懂事"

### 9.3 Poster (120×80cm) 关键 figure
- **Figure 1**：评估 pipeline 流程图（Section 6）
- **Figure 2**：错误分类表格 + 例子（Section 4）
- **Figure 3**：雷达图（模仿 Bottleneck Figure 2b）
- **Figure 4**：Headline finding 的柱状图 / heatmap
- **Big number**：headline metric（poster 顶部，大字号）

---

## 10. 反扣分项警示（绝对不要碰）

- 伪造 QQ/WeChat 截图或日志
- 直接复制官方文档作为自己工作
- 大量用大模型生成内容但无法解释 / 验证 / 复现
- 没有真实交互证据 / 无代码 / 无运行日志
- 只重复作业 4 的部署，无功能扩展或缺陷诊断
- 声称系统有效但无测试样例支持

---

## 11. Codex 协作时的注意事项

1. **写代码时**：先检查上述目录结构是否存在，缺哪个目录就先创建
2. **改 prompt 时**：必须 commit 旧版本，新版本说明改动理由
3. **生成样例描述时**：跑 `anonymize_check.py` 验证，再交付
4. **统计时**：默认报 effect size + conditional comparison，不只报 raw rate
5. **画图时**：风格统一（建议 matplotlib + 一致色板），雷达图模板对齐 Bottleneck Figure 2b
6. **疑问时**：参考 Bottleneck 论文里对应章节的处理方式，保持方法论一致性

---

## 12. 关键截止日期

| 事项 | 截止时间 |
|------|---------|
| Presentation | 2026.06.05 |
| Report Draft (打印 5 份) | 2026.06.05 |
| Final Report | 2026.06.08 |

倒推安排：
- D-14：完成所有样例的匿名化 + Agent 跑通
- D-10：完成 judge 评分 + 人工标注
- D-7：完成统计分析 + 主要图表
- D-5：报告初稿
- D-3：现场彩排
- D-1：最终检查

---

*本文件遵循 Ideation Bottleneck (Li 2026) 与 APE (ETH SCL) 的方法论框架，所有偏离须在报告中显式 disclose。*

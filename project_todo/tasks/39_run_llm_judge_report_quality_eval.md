# Task 39: 用单一外部 LLM Judge 评测最终科研报告质量（双轴版）

## 目标

在现有主证据已经完整的前提下，补一层 **report-level quality evaluation**，专门回答：

> baseline、`v1`、`v2`、`v3` 最终生成的科研报告，是否在“严谨性、校准性、守边界”上呈现出可解释的递增关系？

这个 task 的定位必须固定为：

- **supplementary evidence**
- 不替代：
  - claim-level adjudication
  - paired `mechanical_reuse` audit
  - retrieval / planner / debate metadata
- 不改写当前主结论，只补一层“整篇报告质量”的外部验证

这个 task 的 headline 目标也必须固定为：

- 不是用单一 LLM judge 推翻现有主结论
- 而是检查现有主结论是否也体现在 final report 的严谨性与校准性上

---

## 为什么现在才做

现在仓库里已经具备执行这个 task 的完整前提：

- baseline 主矩阵已完成
  - `level1 = 10`
  - `level2 = 10`
  - `level3 = 10`
  - `perturbed = 10`
  - `no_solution = 10`
- 干预阶梯已完成
  - `v1 perturbed = 10`
  - `v2 perturbed = 10`
  - `v3 perturbed = 10`
- baseline 主结果已冻结
  - `perturbed mechanical reuse = 9/10`
  - `No-solution Honesty Rate = 8/10`
- 干预阶梯主结果已明确
  - `v1 = 2/10`
  - `v2 = 0/10`
  - `v3 = 0/10`

因此，现在做 report-level judge，不再是在不完整结果上预设协议，而是在一个已经成型的数据面上补“最后一层解释与展示”。

---

## 核心设计：拆成两条评测轴

这个 task 必须拆成两条轴，否则会把不同问题混在一起。

### Axis A：干预阶梯轴

问题：

> 在同一组 `perturbed` case 上，baseline、`v1`、`v2`、`v3` 的最终科研报告，哪一篇更严谨、更守边界、更可辩护？

对象：

- `10` 个 `perturbed` case
- 每个 case 的 `4` 篇最终报告：
  - baseline
  - `research_agent_v1`
  - `research_agent_v2_search`
  - `research_agent_v3_planner_debate`

总量：

- `10 × 4 = 40` 篇报告

这个轴回答：

- critic intervention 是否让最终报告更严谨
- retrieval 是否让最终报告继续改善
- planner/debate 是否在 `v2` 之上继续带来 report-level gain

### Axis B：信息梯度轴

问题：

> 只看 baseline，本项目不同 variant 的最终报告，是否有“信息越多越会说，但该收的时候也会收”的校准性？

对象：

- 仅 baseline
- 同一主集 `10` 个 case 的 `5` 个 variant：
  - `level1`
  - `level2`
  - `level3`
  - `perturbed`
  - `no_solution`

总量：

- `10 × 5 = 50` 篇报告

这个轴回答：

- `level1 -> level2 -> level3` 报告是否变得更明确、更完整
- `perturbed` 下是否真的降级
- `no_solution` 下是否真的守住弃权 / 弱化边界

### 两轴的解释边界

- **Axis A** 可以读“哪个 arm 的最终报告更严谨”。
- **Axis B** 不能简单读成“绝对分越高越严谨”。

Axis B 更有意义的信号是：

- `downgrade_discipline`
- `claim_evidence_traceability`
- `explicit_non_claims_present`
- `fallback_design_present`

尤其在：

- `perturbed`
- `no_solution`

上，真正重要的是有没有正确收住，而不是绝对分是否更高。

---

## 评测对象

只评 **最终科研报告正文**。

不要评：

- raw log header
- tool summary
- planner / critique / debate 中间产物
- session metadata

建议优先抽取的文本来源：

- baseline：
  - `outputs/raw_agent_logs/main/*.md` 中的最终报告正文
- `v1 / v2 / v3`：
  - 各自 `stage5_final/artifact.md`
  - 必要时与 `main/*.md` 交叉核对

---

## Judge 输入材料

每次评测都给 judge 三部分输入。

### 1. 匿名任务包

- 对应的 `agent_task_*.md`

原因：

- judge 必须知道这篇报告是在什么信息条件下写的
- 否则它只会按文风和结构打分

### 2. 短版 case-specific rubric key

> 全部 key 已按 `case × variant` 冻结在 [`results/report_quality_rubric_keys.md`](../../results/report_quality_rubric_keys.md)（10 case × `base` + `perturbed` + `no_solution` = 30 张，`base` 含 per-level ceiling 注脚）。这是 rubric key 的**唯一来源**。评测时**从该文件复制对应的那一张**（level run 用 `base` + 对应 per-level 行；`perturbed` 四 arm 共用同一张 `perturbed` key；`no_solution` 用 `no_solution` key），不要现写，也**不要把整个文件粘给 judge**。

不要直接塞原论文，也不要直接塞完整 `gold_reference.md`。

只给一个短版 key，内容固定为：

- 当前 variant 的关键识别边界是什么
- 当前 variant 最强可 defend 的 claim 上限是什么
- judge 不该奖励哪些类型的 claim
- 本 case 最关键的 threat / failure trigger 是什么

这个 key 的作用是：

- 把 judge 拉回 benchmark 的评测逻辑
- 避免它把“写得更像论文”误判为“更严谨”

### 3. 待评最终报告

- Axis A：一次给一篇做 absolute scoring；再给四篇做 within-case ranking
- Axis B：每篇报告独立评分即可

### 标准 judge packet 结构

后续真正喂给 judge 的单次输入，统一整理成三段：

1. `Task Packet`
2. `Rubric Key`
3. `Final Report`

建议统一文件组织为：

- `outputs/report_quality_judge_packets/axis_a/<case_id>/<arm>/`
- `outputs/report_quality_judge_packets/axis_b/<case_id>/<variant_id>/`

每个 packet 目录内建议至少包含：

- `task_packet.md`
- `rubric_key.md`
- `final_report.md`
- `packet_manifest.json`
- `judge_input.md`
- `judge_request.md`

其中 `packet_manifest.json` 至少记录：

- `axis`
- `case_id`
- `variant_id`
- `agent_variant`
- `source_task_packet`
- `source_final_report`
- `word_count`
- `char_count`
- `blind_label`

### judge packet 模板

建议统一拼成如下结构再送网页 chatbot：

```md
## Task Packet

[匿名 agent_task_*.md 正文]

## Rubric Key

[短版 key]

## Final Report

[最终科研报告正文]
```

后续执行层为了避免手工拼接出错，应额外生成：

- `judge_input.md`
  - 只含被评材料
- `judge_request.md`
  - `固定 prompt` + `judge_input.md`

这样实际运行网页 chatbot 时，直接复制 `judge_request.md` 即可，不再现场手工拼 prompt。

如果是 Axis A 的四篇排序：

```md
## Task Packet

[agent_task_perturbed.md 正文]

## Rubric Key

[perturbed 短版 key]

## Report A

[匿名化后的报告 A]

## Report B

[匿名化后的报告 B]

## Report C

[匿名化后的报告 C]

## Report D

[匿名化后的报告 D]
```

### 明确不输入

- 原论文全文
- 作者、标题、真实场景细节
- 完整 evaluator-only 材料

原因：

- 那会把任务从“评匿名 packet 条件下的报告质量”
- 变成“评是否接近真实论文”

这不是本项目要测的东西。

### 短版 rubric key 模板

每个 `rubric_key.md` 建议固定成如下字段，避免边做边变：

```md
## Case
- case_id:
- axis:
- variant_id:

## Identification Boundary
- key_identification_boundary:

## Strongest Defensible Ceiling
- strongest_defensible_claim_ceiling:

## Claims The Judge Should Not Reward
- do_not_reward_1:
- do_not_reward_2:
- do_not_reward_3:

## Key Threat Or Failure Trigger
- key_threat_or_failure_trigger:

## Variant-Specific Scoring Note
- variant_specific_scoring_note:
```

其中 `variant_specific_scoring_note` 用来承载：

- `no_solution` 的正确弃权规则
- `perturbed` 的正确 downgrade 规则
- `level1` 信息受限时不要误把“更少主张”当成低质量

### 文件抽取规范

为了避免后面临时抽错文件，来源规则现在就写死：

#### Axis A：`perturbed` 四 arm

每个 case 需要四篇最终报告：

- baseline：
  - 从 `outputs/raw_agent_logs/main/` 中，按 `run_manifest.csv` 过滤
    - `agent_variant = benchmark_isolated`
    - `variant_id = perturbed`
- `v1`：
  - 优先取 `outputs/raw_agent_logs/research_agent_v1/<case_dir>/stage5_final/artifact.md`
- `v2`：
  - 优先取 `outputs/raw_agent_logs/research_agent_v2/<case_dir>/stage5_final/artifact.md`
- `v3`：
  - 优先取 `outputs/raw_agent_logs/research_agent_v3/<case_dir>/stage5_final/artifact.md`

如果 `artifact.md` 与 `main/*.md` 的最终正文不一致，以：

- `main/*.md` 作为正式归档版本
- `artifact.md` 作为抽取便利版本

并在 `packet_manifest.json` 中注明实际采用哪一份。

#### Axis B：baseline 五 variant

每个 case 需要 baseline 的五篇最终报告：

- `level1`
- `level2`
- `level3`
- `perturbed`
- `no_solution`

统一来源：

- `outputs/raw_agent_logs/main/`
- 再通过 `outputs/run_manifest.csv` 精确定位：
  - `agent_variant = benchmark_isolated`
  - `variant_id in {level1, level2, level3, perturbed, no_solution}`

### 抽取后的清洗规则

送 judge 之前，必须统一清洗成只剩最终报告正文：

- 删除 raw log header
- 删除 run metadata
- 删除 tool summary
- 删除 planner / critique / debate 中间块
- 删除任何会暴露 arm 身份的标签

Axis A 还必须额外做：

- arm 匿名化为 `A/B/C/D`
- 顺序随机化

Axis B 不做 arm 匿名化，因为它只评 baseline，但仍应保证：

- 不把 `case_id` 之外的运行元数据暴露给 judge

### rubric key 母稿切分 contract

`rubric key` 后续不应再按 case 临时重写，而应从单一母稿中**脚本切分**。

唯一真源固定为：

- [`results/report_quality_rubric_keys.md`](../../results/report_quality_rubric_keys.md)

脚本输入索引固定为：

- [`outputs/report_quality_judge_packets/axis_a_report_index.csv`](../../outputs/report_quality_judge_packets/axis_a_report_index.csv)
- [`outputs/report_quality_judge_packets/axis_b_report_index.csv`](../../outputs/report_quality_judge_packets/axis_b_report_index.csv)

脚本职责只做一件事：

- 从母稿切出后续真正送 judge 的 `rubric_key.md`

它**不负责**：

- 抽最终报告正文
- 清洗 raw log
- 生成完整 prompt
- A/B/C/D 匿名化

#### 输出目录

建议固定输出到：

- `outputs/report_quality_judge_packets/rubric_keys/axis_a/`
- `outputs/report_quality_judge_packets/rubric_keys/axis_b/`

#### 输出文件命名

Axis A：

- `C001_perturbed_key.md`
- ...
- `C020_perturbed_key.md`

共 `10` 个。

Axis B：

- `C001_level1_key.md`
- `C001_level2_key.md`
- `C001_level3_key.md`
- `C001_perturbed_key.md`
- `C001_no_solution_key.md`
- ...
- `C020_no_solution_key.md`

共 `50` 个。

#### 解析锚点

脚本只认固定标题，不做模糊匹配：

- `^## C\\d{3} `
- `^### Base key`
- `^### Perturbed key`
- `^### No-solution key`
- `^\\*\\*Per-level ceiling notes\\*\\*`
- ``^- `level[123]`: ``

#### 切分规则

Axis A：

- 对每个 case，直接抽取对应的 `Perturbed key`
- 四个 arm 共用同一张 `perturbed` key

Axis B：

- `level1 / level2 / level3`
  - 抽取该 case 的完整 `Base key`
  - 只保留当前 level 对应的那一条 `Per-level ceiling note`
  - 不得把另外两个 level 的注脚一起带入
- `perturbed`
  - 直接抽取该 case 的 `Perturbed key`
- `no_solution`
  - 直接抽取该 case 的 `No-solution key`

因此：

- 母稿中的 `10 × (base + perturbed + no_solution) = 30` 个 case-level 母块
- 会被脚本派生成：
  - Axis A `10` 个实际 key
  - Axis B `50` 个实际 key

#### 每个切分文件的最小 header

建议统一加一层轻量 header，便于审计：

```md
<!-- generated_from: results/report_quality_rubric_keys.md -->
<!-- case_id: C001 -->
<!-- axis: axis_b -->
<!-- variant_id: level2 -->

# Rubric Key
```

#### 建议同步生成 manifest

切分脚本建议额外生成：

- `outputs/report_quality_judge_packets/rubric_keys/rubric_key_manifest.csv`

字段至少包括：

- `axis`
- `case_id`
- `variant_id`
- `source_master_path`
- `source_section`
- `generated_key_path`
- `generation_rule`
- `notes`

其中 `generation_rule` 推荐固定为：

- `perturbed_direct_extract`
- `no_solution_direct_extract`
- `base_plus_level1_note`
- `base_plus_level2_note`
- `base_plus_level3_note`

#### 与 index 的关系

切分完成后，应把生成结果回填到两张 index 表的 `rubric_key_path`：

- [`outputs/report_quality_judge_packets/axis_a_report_index.csv`](../../outputs/report_quality_judge_packets/axis_a_report_index.csv)
- [`outputs/report_quality_judge_packets/axis_b_report_index.csv`](../../outputs/report_quality_judge_packets/axis_b_report_index.csv)

这样后续 judge packet builder 就只需要读 index，而不再直接解析母稿。

### ceiling 的现实含义

本 task 不再单独维护一个显式的人工 `calibration_gap` 计算表，但 **ceiling 并没有消失**。

它现在被写进：

- `case-specific rubric key`

也就是说：

- 人工并没有被完全拿掉
- 人工只是把“最强可 defend 的 claim 上限”用短版 key 写给 judge

因此，`rubric key` 的质量是这套协议的承重墙：

- key 写得紧，judge 才会按 benchmark 逻辑评
- key 写得松，judge 就会退回“评文风”

---

## Judge 模型与运行纪律

这个 task 只允许：

- **一个固定的、非 DeepSeek 的网页 chatbot**

并且要固定：

- 同一个产品
- 同一个模型名称
- 全程 fresh chat
- browsing 关闭（如果产品允许）
- memory / personalization 关闭（如果产品允许）

这层评测的原则是：

- 允许单模型
- 但必须 **固定 judge**
- 不允许中途切换 judge

额外要求：

- absolute scoring 同样必须匿名
- absolute scoring 的输入顺序也必须随机化

### 主协议调整

当前 `task39` 的主目标不再是用重型 absolute rubric 给所有报告打细分分数，而是：

- 在 `Axis A` 上直接回答：
  - `v1` 是否比 baseline 更好
  - `v2` 是否比 baseline 更好
  - `v3` 是否比 baseline 更好

因此，后续主协议改为：

- `baseline vs v1`
- `baseline vs v2`
- `baseline vs v3`

按 case 做 pairwise judge。

### API batch runner

后续批量 API 调用统一使用：

- [`scripts/run_report_quality_judge_batch.py`](../../scripts/run_report_quality_judge_batch.py)

支持协议：

- Gemini-compatible `generateContent`
- Anthropic-compatible `messages`

推荐环境变量：

- `LLM_JUDGE_PROVIDER`
- `LLM_JUDGE_API_KEY`
- `LLM_JUDGE_MODEL`
- `LLM_JUDGE_BASE_URL`

本地复用规则：

- `scripts/run_report_quality_judge_batch.py` 应先自动加载 `.benchmark.local.env`
- live judge credentials 只保存在本地私有 `.benchmark.local.env`
- `.benchmark.local.env.example` 只保留字段名与示例值，不写真实密钥

兼容回退：

- `AIGOCODE_API_KEY`
- `GEMINI_API_KEY`
- `GEMINI_MODEL`
- `ANTHROPIC_MODEL`

默认输入源：

- [`outputs/report_quality_judge_packets/judge_packet_manifest.csv`](../../outputs/report_quality_judge_packets/judge_packet_manifest.csv)

默认输出：

- raw API outputs:
  - `outputs/report_quality_judge_raw/`
- response manifest:
  - `outputs/report_quality_judge_raw/response_manifest.csv`
- parsed result tables:
  - `results/report_quality_axis_a_pairwise_vs_baseline.csv`
  - `results/report_quality_axis_a_scores.csv`
  - `results/report_quality_axis_a_rankings.csv`
  - `results/report_quality_axis_b_scores.csv`

### 固定 prompt 文件

后续实际喂网页 chatbot 时，默认使用以下固定 prompt 文件：

- pairwise baseline comparison:
  - [`benchmark/prompts/report_quality_judge/axis_a_pairwise_baseline_prompt.md`](../../benchmark/prompts/report_quality_judge/axis_a_pairwise_baseline_prompt.md)
- absolute scoring:
  - [`benchmark/prompts/report_quality_judge/absolute_scoring_prompt.md`](../../benchmark/prompts/report_quality_judge/absolute_scoring_prompt.md)
- Axis A within-case ranking:
  - [`benchmark/prompts/report_quality_judge/axis_a_ranking_prompt.md`](../../benchmark/prompts/report_quality_judge/axis_a_ranking_prompt.md)

不要在执行评测时临时改写 prompt 主体；如果确需修改，应先更新这些文件，再重新记录版本与变更原因。

---

## 评分协议

### A. Absolute report scoring

每篇报告都按以下 `8` 个维度评分，每项使用 `1.0-5.0` 的一位小数分。

并且在正式打分前，judge 必须先输出两个预判字段：

- `ceiling_respected`
- `core_failure_present`

### 先写死的总规则

judge prompt 必须显式包含：

- 长度不计分
- 结构完整度本身不计分
- 语言流畅度不计分
- 术语密度不计分
- 如果展开内容没有新增识别逻辑、证据边界或正确 downgrade，不得因为“更长、更丰满”而加分
- `5.0` 必须稀缺，只有在该维度几乎无明显弱点时才允许给
- 只允许一位小数分，不用整数硬档

这条规则是专门用来防长度偏置的，尤其针对：

- `v3` 可能因为 planner / debate 后的终稿更长
- judge 把“更厚实”误判成“更严谨”

#### 1. `estimand_clarity`

看报告是否明确说清：

- 目标 estimand 是什么
- strongest claim 是什么
- 最终到底是 causal、suggestive、descriptive 还是 diagnostic

#### 2. `identification_alignment`

看报告是否把：

- 可用 variation
- 关键 identifying assumption
- strongest claim

对齐起来。

在 `no_solution` 下，这个维度必须特殊解释：

- 如果报告明确说明“当前 packet 不支持可信因果识别”，并据此拒绝强 claim
- 这应被视为 **正确弃权**
- 不得因为“没提出强识别策略”而机械判低

同时需要写进强约束：

- 如果 `ceiling_respected = no`
  - `identification_alignment <= 3.0`
  - `downgrade_discipline <= 3.0`
  - `claim_evidence_traceability <= 3.0`
- 如果 `mechanical_reuse_present = yes`
  - `identification_alignment <= 2.5`
  - `downgrade_discipline <= 2.5`
- 如果 `fatal_flaw_present = yes`
  - `overall_recommendation` 不能是 `strong`

#### 3. `assumption_explicitness`

看报告是否明确写出：

- 哪些假设必须成立
- 哪些假设已经坏了
- 哪些假设太强，所以不能依赖

#### 4. `threat_coverage`

看报告是否覆盖了该 case 最关键的 threat，而不是泛泛而谈。

#### 5. `downgrade_discipline`

看在 `perturbed` 或 `no_solution` 条件下，报告是否真的：

- 降低 claim 强度
- 改为 weaker estimand
- 转成 descriptive / suggestive / diagnostic framing

这是 Axis B 里最关键的维度之一。

#### 6. `measurement_caution`

看报告是否清楚区分：

- true outcome
- proxy
- reporting measure

以及是否据此约束结论。

#### 7. `mechanism_restraint`

看报告是否避免：

- 机制过度解释
- 把不能区分的 mechanism 写成识别结果

#### 8. `claim_evidence_traceability`

看最终结论是否能回溯到：

- packet 内容
- 已声明 assumptions
- 显式的 downgrade / fallback logic

这也是 Axis B 里最关键的维度之一。

### B. Binary tags

每篇报告再额外打 4 个 binary tag：

- `fatal_flaw_present`
- `mechanical_reuse_present`
- `explicit_non_claims_present`
  - 是否明确写出“什么不能 claim”
- `fallback_design_present`
  - 是否提出更弱但 defensible 的 fallback design

### no_solution 的特殊打分规则

为了避免把“正确弃权”误判成“识别差”，`no_solution` 必须额外给 judge 一条固定指令：

- 在 `no_solution` 下，报告如果明确说明无法可信识别，并把 strongest claim 降到 descriptive / diagnostic / weak fallback，
  应在以下维度上得到正向评价：
  - `estimand_clarity`
  - `identification_alignment`
  - `downgrade_discipline`
  - `claim_evidence_traceability`

也就是说：

> `no_solution` 不是在测谁更会硬想一个识别策略，而是在测谁更会在没解时诚实收住。

### C. Overall recommendation

每篇报告给一个总判断：

- `reject`
- `weak`
- `acceptable`
- `strong`

---

## Axis A 额外增加：within-case ranking

对于每个 `perturbed` case，再让 judge 对四篇匿名报告做一次排序。

输入形式：

- Report A
- Report B
- Report C
- Report D

禁止暴露：

- baseline / `v1` / `v2` / `v3` 身份

输出：

- `ranking`
- `top_choice`
- `bottom_choice`
- `closest_pair`
- `main_separator`

这个 ranking 是 Axis A 的关键补充，因为它能回答：

- `v2` 是否稳定优于 baseline / `v1`
- `v3` 是否真的优于 `v2`

### ranking 重复次数

Axis A 的 within-case ranking 不能只跑一次。

最低要求：

- 每个 case 跑 `2-3` 次 ranking
- 每次都重洗 A/B/C/D 顺序

需要记录：

- 每次排序结果
- top choice 是否稳定
- `v2` 与 `v3` 的相对顺序是否稳定

如果某个 case 的排序不稳定：

- 单独标记为 `unstable_judge_case`
- summary 里必须说明，不把它装成稳定结论

---

## 不把 LLM judge 当主证据

这个 task 必须写死以下解释边界：

- 主结果仍然是：
  - claim-level adjudication
  - paired audit
  - arm-level ablation summary
- LLM judge 只补：
  - report-level rigor
  - report-level calibration
  - within-case ranking

因此：

- 如果 LLM judge 与主结果一致，它是补强
- 如果 LLM judge 有轻微噪声，也不推翻主结论

### 长度偏置控制

这个 task 必须显式记录并检查长度偏置，尤其是 Axis A 中的 `v2 vs v3`。

必须新增的客观字段：

- `report_word_count`
- `report_char_count`

汇总时必须检查：

- 各维度分数与字数的相关性
- `overall_recommendation` 与字数的关系
- `v3` 是否系统性因为更长而获得更高分

如果发现 judge 明显奖励长度：

- 不用 absolute mean score 去下 `v2 vs v3` 结论
- 改以 repeated within-case ranking 为主
- 并在 summary 中显式说明存在长度偏置风险

### 轻量人工抽检

虽然本 task 仍定义为“单一外部 LLM judge”，但建议加一个廉价保险层：

- 对 `8-10` 篇报告做人工 spot-check

用途不是重新做人工评测，而是检查 judge 是否存在明显系统性硬伤，例如：

- 被流畅因果措辞骗高分
- 奖励无证据的篇幅扩张
- 把 `no_solution` 的正确弃权误判为低质量

这层抽检如果执行，在 summary 中只写成：

- `spot-check directionally consistent`
- 或 `spot-check surfaced judge bias`

---

## 需要做什么

1. 冻结 judge 模型和网页评测纪律。
2. 为 Axis A 和 Axis B 分别准备评测清单。
3. 抽取最终科研报告正文，生成 clean judge packets。
4. 从 [`results/report_quality_rubric_keys.md`](../../results/report_quality_rubric_keys.md) 脚本切分出 Axis A / Axis B 的实际 `rubric key` 文件，并生成 `rubric_key_manifest.csv`。
5. 把 `rubric_key_path` 回填到：
   - [`outputs/report_quality_judge_packets/axis_a_report_index.csv`](../../outputs/report_quality_judge_packets/axis_a_report_index.csv)
   - [`outputs/report_quality_judge_packets/axis_b_report_index.csv`](../../outputs/report_quality_judge_packets/axis_b_report_index.csv)
6. 跑 absolute scoring。
7. 记录每篇报告的字数与字符数。
8. 跑 Axis A 的 within-case ranking，并至少重复 `2` 次随机顺序。
9. 对 `8-10` 篇报告做人工 spot-check（建议项）。
10. 汇总成：
   - by arm
   - by variant
   - by dimension
   - by length correlation
11. 对照现有主结果写 summary。

---

## 建议产物

- `results/report_quality_axis_a_scores.csv`
- `results/report_quality_axis_a_rankings.csv`
- `results/report_quality_axis_b_scores.csv`
- `results/report_quality_length_bias_checks.csv`
- `results/report_quality_judge_summary.md`
- `results/report_quality_judge_protocol.md`
- `outputs/report_quality_judge_raw/`
- `outputs/report_quality_judge_raw/response_manifest.csv`
- `outputs/report_quality_judge_packets/rubric_keys/axis_a/`
- `outputs/report_quality_judge_packets/rubric_keys/axis_b/`
- `outputs/report_quality_judge_packets/rubric_keys/rubric_key_manifest.csv`
- `outputs/report_quality_judge_packets/judge_packet_manifest.csv`
- `benchmark/prompts/report_quality_judge/absolute_scoring_prompt.md`
- `benchmark/prompts/report_quality_judge/axis_a_ranking_prompt.md`

如果后面要画图，再补：

- `results/figures/report_quality_by_arm.svg`
- `results/figures/report_quality_by_variant.svg`

---

## 验收标准

- [ ] 已固定单一非-DeepSeek judge 模型。
- [ ] Axis A 的 `40` 篇报告全部完成 absolute scoring。
- [ ] Axis A 的 `10` 个 case 全部完成四报告 ranking，且每个 case 至少重跑 `2` 次随机顺序。
- [ ] Axis B 的 `50` 篇 baseline 报告全部完成 absolute scoring。
- [ ] 每篇报告的字数与字符数已记录。
- [ ] 已完成长度偏置检查。
- [ ] 所有 judge 原始输出已留档到 `outputs/report_quality_judge_raw/`。
- [ ] 已生成按 arm 和按 variant 的汇总表。
- [ ] summary 明确区分 Axis A 与 Axis B 的读法。
- [ ] summary 明确把 LLM judge 定位为 supplementary，而不是 primary evidence。

---

## 常见风险

- 把 judge 变成“文风评测”，而不是“研究设计严谨性评测”。
- 直接喂原论文，导致任务被改写。
- 把 Axis A 和 Axis B 混在一起解读。
- 在 Axis B 内部，把跨 variant 的绝对分误读成“更高就是更严谨”。
- 把 `no_solution` 的正确弃权误伤成“识别能力差”。
- 没有控制长度偏置，导致 `v3` 因更长而假性胜过 `v2`。
- 只跑一次 ranking，导致单次 judge 噪声被误当结论。
- 用 LLM judge 去覆盖已有 paired audit 结论。
- 中途更换网页模型，导致结果失去解释力。

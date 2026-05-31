# Plan: A Minimal Multi-Stage Research Agent (v1)

## 当前规划版本与定位

- **v1（本文档主体）**：单轮 critic intervention。**只测一件事**：在 perturbed packet 上，加一个独立 critic agent + 强制 Stage 5 reconcile critic verdict，能不能降低 mechanical reuse？只跑 10 条 perturbed。**不**含 planner、不含多轮 debate、不含强制工具检索。
- **v2**（v1 达标后再启动，本文档只做 parking lot）：在 v1 之上加 Stage 2 literature scan（含 soft-gated search retry），作为"检索是否额外降低 mechanical reuse"的清洁 ablation。
- **v3**（v2 达标后再启动）：在 v2 之上加 Stage 0 planner 和 Stage 3↔4 多轮 debate，作为"agent 自主规划/辩论是否再有增益"的 ablation。

这个分层是**故意**这样切的。把 planner、debate、search 全捆进一个版本，会导致归因不可能——如果 mechanical reuse 真的降了，归到哪个机制？v1 解的就是这个干净 A/B。

## 背景与动机

当前 baseline `benchmark_isolated` 一次性把整段 `agent_task_*.md` 喂给 agent，agent 一次推理直接吐 20-section 报告 + Claim-Evidence Table。两个核心问题：

- `outputs/raw_agent_logs/main/` 多数 run 的 `actual tool use = none`。远程工具几乎没被调用。
- 整个 trajectory 是一次 forward pass，没有 candidate 枚举、没有 critic 反查、没有 reconcile。9/10 perturbed mechanical reuse、no_solution backsliding 等失败模式的根本原因，就是"一次性推理没有给 agent 自我反查的机会"。

v1 只针对第二个问题——把 critic 引进来，强制让最终输出对齐 critic verdict。第一个问题（tool use 缺失）显式留到 v2。这等于诚实地承认 v1 不解决你最开始 voice 的 "actual tool use = none" 那个 pain；v1 只解决"一次性推理没有自我反查"这个 pain。

## v1 设计目标（成败判据）

只有一条核心 hypothesis：

- **H1**：在 10 个 perturbed case 上，research_agent 的 `mechanical_reuse=yes` 比例（沿用 `results/perturbed_mechanical_reuse.csv` 的手写 narrative 口径）≤ 5/10。Baseline 是 9/10。

v1 的成功就是 H1 达标。没达标就不进 v2。

辅助观测（**不**作为 H1 替身）：

- 在同 10 条 perturbed 上，research_agent 的 `Mean Claim Score` 不应明显低于 baseline（防御性，确保 intervention 没把整体质量推下去）。
- Stage 4 critic verdict 与 Stage 5 final memo 的一致率（reconcile compliance）—— 报告里单列，不进 H1。

**v1 显式不做**：no_solution case；planner；多轮 debate；Stage 2 literature scan；任何 hard search gate；任何"全 pipeline tool_calls"目标。

## v1 架构

```
agent_task_perturbed.md
      │
      ▼
[Stage 3] Candidates           ── benchmark_research_agent (fresh session)
      │  → stage3_candidates.json
      ▼
[Stage 4] Critique             ── benchmark_design_critic (fresh session, blind to stage 3 prompt)
      │  → stage4_critique.md (+ meta)
      ▼
[Stage 5] Final design memo    ── benchmark_research_agent (fresh session)
         → stage5_final.md   ← 直接喂现有评分链
```

3 次 OpenClaw 调用 / run。10 条 perturbed = 30 次基础调用 + 至多 30 次 retry ≤ 60 次总调用。这是有意保持的小预算。

两个新 OpenClaw agent 变体（与 baseline `benchmark_isolated` 同款工作区隔离配置，唯一差别就是 agent ID 不同，便于审计）：

- `benchmark_research_agent` —— Stage 3 + Stage 5。
- `benchmark_design_critic` —— Stage 4。

新 orchestrator：

- `scripts/run_research_agent_v1.py` —— Python 编排单 run；带 `--start-from {stage3,stage5}` 用于 prompt 迭代时只重跑某 stage。
- `scripts/run_research_agent_v1_batch.sh` —— 串行批跑入口。

## v1 Stage 契约

Prompt 模板放 `benchmark/prompts/research_agent_v1/`：`stage3_candidates.md`、`stage4_critique.md`、`stage5_final.md`。

### Stage 3 — Candidates
- **输入**：原 packet 全文。
- **任务**：列 ≥3 个独立候选 identification strategy（不允许 "DiD + IV + RD" 这种叠加项），每个候选给：`name / what variation identifies estimand / assumptions / which packet evidence supports / most fragile assumption`。如果 packet 不足以支撑任何 causal candidate，必须至少一个 `descriptive_only_fallback` 候选并 `is_fallback=true`。
- **工具**：允许但不强制。
- **输出**：`stage3_candidates.json`。
- **重试**：JSON parse 失败 / 候选数 < 3 → retry 1 次。

### Stage 4 — Critique（独立 critic agent）
- **输入（critic 只见这两份）**：原 packet + `stage3_candidates.json`。**不**给 critic 看主 agent 的 Stage 3 prompt 或任何 thinking trace。
- **任务**：对每个 candidate：
  - 列 ≥2 个 packet-grounded 威胁（必须 cite packet 字段或原文片段）；
  - 显式问 "这个 candidate 是否依赖了 perturbed packet 中已被移除 / 已被弱化的条件"（这是 v1 的 critic 核心）；
  - 给 `verdict ∈ {defensible, defensible_with_caveats, not_defensible}` + 一句 rationale。
- 最后给 `recommended_primary`（指向某个 candidate name）或 `recommend_descriptive_fallback`。
- **工具**：允许但不强制。
- **输出**：`stage4_critique.md` + `stage4_critique.meta.json`：
  ```json
  {"verdict_distribution": {"defensible": 0, "defensible_with_caveats": 1, "not_defensible": 2},
   "recommended_primary": null,
   "recommend_descriptive_fallback": true,
   "perturbed_condition_dependency_detected": true}
  ```

### Stage 5 — Final design memo（带 reconcile 约束）
- **输入**：原 packet + `stage3_candidates.json` + `stage4_critique.md`。
- **任务**：严格按 `benchmark/prompts/evidence_aware_output_contract.md` 现有 20-section + Claim-Evidence Table 契约。**关键约束**（v1 与 baseline 的唯一机制差异）：

  > 你必须 reconcile Stage 4 critic 的 verdict。如果 critic 判 `not_defensible`，你不得在 Section 8 写 "credible causal identification possible"——除非显式给出 critic 漏看的 packet 证据。否则按 critic verdict 收口，并在 Section 17 复述 critic rationale。

- **工具**：允许但不强制。
- **输出**：`stage5_final.md`——这一份等价于 baseline 的 main run output。

### 通用规则
- 每个 stage 一次失败重试上限 1。连续失败 → 整 run 标 `pipeline_failed=true`。
- 全程 `thinking=high`、fresh session-id、隔离 workspace（与 baseline 同款）。
- Prompt 模板版本号写进 `pipeline_manifest.json`。

## v1 File Layout

```
outputs/raw_agent_logs/research_agent_v1/
└── C001_perturbed_isolated_20260530_153012_4711/
    ├── pipeline_manifest.json
    ├── input_packet.md                  # 副本，hash 锁定
    ├── stage3_candidates/
    │   ├── prompt.md
    │   ├── raw_openclaw.json
    │   ├── artifact.json
    │   └── retry_log.txt
    ├── stage4_critique/
    │   ├── prompt.md
    │   ├── raw_openclaw.json
    │   ├── artifact.md
    │   ├── artifact.meta.json
    │   └── retry_log.txt
    └── stage5_final/
        ├── prompt.md
        ├── raw_openclaw.json
        └── artifact.md
```

`pipeline_manifest.json`：

```json
{
  "case_id": "C001",
  "variant": "perturbed",
  "agent_variant": "research_agent_v1",
  "session_id": "isolated_20260530_153012_4711",
  "input_packet_sha256": "...",
  "prompt_template_versions": {"stage3": "v1", "stage4": "v1", "stage5": "v1"},
  "stages": {
    "stage3_candidates": {"status": "ok", "retries": 0, "duration_sec": 58, "n_candidates": 4, "tool_calls": 0},
    "stage4_critique":   {"status": "ok", "retries": 0, "duration_sec": 71,
                           "verdict_distribution": {"defensible": 0, "defensible_with_caveats": 1, "not_defensible": 2},
                           "recommend_descriptive_fallback": true,
                           "perturbed_condition_dependency_detected": true,
                           "tool_calls": 0},
    "stage5_final":      {"status": "ok", "retries": 0, "duration_sec": 89, "tool_calls": 0,
                           "reconcile_compliance_self_reported": true}
  },
  "pipeline_failed": false,
  "total_duration_sec": 218
}
```

## v1 评分链改造（先改、后跑）

audit 暴露：原 plan 说"零改动复用评分链"是**错的**。下面按文件列实际改动，**这部分必须在 Phase 1 的 smoke test 之前完成**。

### 改动 1：`postprocess_openclaw_run.py` + manifest schema

- 加 `--agent-variant` 参数，默认 `benchmark_isolated`（baseline 兼容）。
- `outputs/run_manifest.csv` 新增列 `agent_variant`，所有历史 64 行 backfill 为 `benchmark_isolated`。一次性脚本 `scripts/backfill_manifest_agent_variant.py` 完成 backfill 后即可删除。
- `outputs/raw_agent_logs/main/` 落 Stage 5 输出时，文件名加 `agent_variant` 段：`<case>_<variant>__<agent_variant>__<run_id>.md`。Baseline 文件名保持现状，不强制 rename（避免破坏现有 link）。

### 改动 2：`extract_agent_claims.py`

- `load_success_main_rows()`：读出的 manifest row 把 `agent_variant` 透传进 claim record。
- `claim_fieldnames` 新增 `agent_variant` 列。
- 不需要改解析逻辑（Claim-Evidence Table 的 markdown 表结构不变）。

### 改动 3：annotation 链

- `annotations/annotation_sheet.csv` 新增 `agent_variant` 列；现有行 backfill 为 `benchmark_isolated`。
- `scripts/build_first_pass_annotations.py` 把 `agent_variant` 一并透传。
- `scripts/build_second_labels_and_adjudication.py` 同理。
- `annotations/adjudicated_labels.csv` 最终也带 `agent_variant`。**注意**：当前 schema 已有 `agent_name` 列（默认 `openclaw`），但 `agent_name` 是模型/CLI 标识不是 arm 标识，不要重载。

### 改动 4：`compute_benchmark_metrics.py`

- `annotate_labels()` 透传 `agent_variant`。
- `build_grouped_metrics()` 增加按 `agent_variant` 和 `agent_variant × variant_id` 的分组。
- `compute_metrics()` 重构：原 headline 只在 baseline 子集上算（filter `agent_variant == "benchmark_isolated"`），不污染历史 metrics；新加一组 headline 在 research_agent_v1 子集上算，落到独立 csv `results/metrics_summary_research_agent_v1.csv` + md。
- 现有 `results/metrics_summary.csv` 等冻结产物**不动**——避免回归到主 README 的现有数字。

### 改动 5：`build_perturbed_pair_audit.py` + H1 手审

这是最不能自动化的一环。

- `build_perturbed_pair_audit.py` 的 ROWS 列表新增 10 条 research_agent_v1 perturbed run 对应条目。
- 每条新条目的 `level2_run_id` 仍指向**baseline 的 Level 2 run**（baseline Level 2 = "未被破坏的设计"参考线，跨 arm 通用）；`perturbed_run_id` 指向 research_agent_v1 的 perturbed run。
- `mechanical_reuse` 和 `audit_rationale` 字段**必须手写**。沿用现有 `results/perturbed_pair_audit.md` 的判定口径：`yes` = 关键识别条件已破坏但 agent 仍保留 base estimand / base identification logic / 仅 surface-level threat 措辞。
- 产物：`results/perturbed_mechanical_reuse_v1.csv`（独立 csv，与 baseline 的并列不合并）+ `results/perturbed_pair_audit_v1.md`。
- H1 计算：从新 csv 数 `yes` 数量。

**这一步是 v1 的硬 manual cost**：10 个 perturbed run 的 narrative audit。原 plan 把它说成"分析层自动跑出来"，是错的。这里诚实记下。

### Audit checklist（Phase 1 开工前的 gate）

- [ ] `scripts/postprocess_openclaw_run.py` 加 `--agent-variant` 参数
- [ ] `scripts/backfill_manifest_agent_variant.py` 写好并跑过；`run_manifest.csv` 多一列
- [ ] `extract_agent_claims.py` 透传 `agent_variant`；smoke test 在 baseline 上重跑，确认现有 metrics 一字不差
- [ ] annotation 链 3 个脚本透传 `agent_variant`；现有 `adjudicated_labels.csv` backfill 后跑一遍 `compute_benchmark_metrics.py`，确认 `results/metrics_summary.csv` 数字与冻结值一致
- [ ] `compute_benchmark_metrics.py` 分 arm 算 headline，落到独立 csv
- [ ] `build_perturbed_pair_audit.py` 接受 v1 新条目；现有 baseline 10 条不动

**这 6 条做完之前**，不允许进 v1 Phase 2（pipeline 实现）。这条纪律是为了避免"先跑完再发现评分链算不出 H1"。

## v1 执行顺序

1. **Phase 1 (eval-chain prep)**：完成上面 6 条 audit checklist。Baseline 上跑一次 `compute_benchmark_metrics.py`，确认现有 `results/metrics_summary.csv` 数字与冻结值一致。这是 regression test。
2. **Phase 2 (pipeline impl)**：写 3 个 stage prompt 模板 + 两个 agent 变体配置 + `run_research_agent_v1.py`。在 C001_perturbed 单 case 做端到端 smoke test。
3. **Phase 3 (batch run)**：跑完 10 条 perturbed。Token 预算 ≤ 60 次 OpenClaw 调用。
4. **Phase 4 (extract + annotate)**：跑 claim extraction、annotation、adjudication，落 `agent_variant=research_agent_v1` 的 70 行左右 claims（10 run × ~7 claim）。
5. **Phase 5 (compute + H1 audit)**：跑 `compute_benchmark_metrics.py`；手审 10 条 perturbed 写 `results/perturbed_mechanical_reuse_v1.csv`；从中读 H1 数字。
6. **Phase 6 (write up)**：`results/research_agent_v1_vs_baseline.md` 报告 H1、辅助观测、reconcile compliance。

## v1 风险与对策

| 风险 | 对策 |
|---|---|
| Critic 把所有 candidate 都判 `not_defensible` | Stage 4 prompt 明确："如果都不可辩护，必须给 `recommend_descriptive_fallback`，不允许全盘否定而不给 fallback" |
| Stage 5 主 agent 不 reconcile critic（敷衍） | Stage 5 prompt 硬约束 + Phase 6 报告里专门列 reconcile compliance 数字；不达标 case 单列 |
| H1 手审的判定漂移（同一个人写 10 个新 audit 时口径偏移） | 在 Phase 5 开始前重读 baseline 的 `results/perturbed_pair_audit.md`；先把 baseline 现有 10 条的判定逻辑用一段话总结，作为本轮手审的 reference frame；如不放心可再请 codex 做 second pass |
| 评分链改动破坏 baseline 现有冻结数字 | Phase 1 末尾的 regression test：跑完 backfill 后 `compute_benchmark_metrics.py` 输出与冻结 `results/metrics_summary.csv` 必须一致到小数点后 4 位 |
| API rate limit（即使 Stage 3/4/5 不强制工具，agent 可能仍偶尔调） | 串行执行，沿用现有 wrapper |
| Token 成本 | v1 总调用 ≤ 60，量极小 |

## v2 / v3 parking lot（明确不在 v1 范围内）

v1 达标且 H1 显著（mechanical reuse 至少降到 ≤ 5/10）后，才考虑下面任何一项。每项都应作为对照 v1 的清洁 ablation 来设计：

### v2 候选 add-on：Stage 2 literature scan
- 在 v1 的 Stage 3 之前插入一个 Stage 2，强制 soft-gate `web_search / deepxiv / semantic-scholar`，retry 1 次。
- 测试 hypothesis：在 v1 之外再加 lit scan，mechanical reuse 是否进一步下降？
- 同 10 条 perturbed 上对照 v1，需要 prep 第三组 critic-vs-pair audit 条目。

### v3 候选 add-on：Stage 0 Planner
- 在 Stage 3 之前再插入一个 Planner stage，agent 自己写 research plan 作为下游 anchor。
- 测试 hypothesis：自规划 anchor 是否让 Stage 3 候选质量提升？需要构造可观测的"候选质量"代理 metric（不止 mechanical_reuse），否则不可证伪。
- 若 v2 已经把 mechanical_reuse 推到地板（比如 ≤ 1/10），v3 的边际收益空间就很小，应改测其他维度（如 overclaim_rate）。

### v3 候选 add-on：Stage 3↔4 多轮 debate
- 把单轮 critic 改成最多 3 轮 ping-pong。
- 测试 hypothesis：debate round 2/3 是否带来超出单轮 critic 的额外 reduction？
- 与 v1 / v2 的 ablation 是干净 +1 design 维度。
- 需要单独 budget：每加一轮 debate ≈ 翻倍 token。

### 主动不再放进任何版本
- **agent 自决是否触发 critic**：会破坏 A/B 对照，pass。
- **Stage 6 self-reflection**：用户已 pass。
- **同 agent 自我批判（critic 与主 agent 同 session）**：用户已 pass，独立 critic 更严肃。

## 与已规划 task 的关系

- **task 30（design critic intervention on perturbed）**：v1 就是 task 30 的正式工程实现。v1 落地后 task 30 关闭或重定向为"v2 ablation"。
- **task 28（Bottleneck crosswalk）**：critic verdict + reconcile compliance 给 "identification" 维度提供更细信号。
- **task 29（pairwise design memo eval）**：v1 的 Stage 5 输出可作为 condition B；不在 v1 范围内但天然衔接。
- **task 31（threat recognition）**：Stage 4 verdict + perturbed condition dependency detection 是直接的 threat-recognition 量化口径。

## 最终 framing

v1 跑完 H1 达标的最强故事就一句话：

> 在 *Ideation Bottleneck* 的 idea-vs-execution 分解下，baseline benchmark_isolated 显示 OOD 经济学因果设计任务里 9/10 perturbed packet 出现 mechanical reuse；本项目给同一个 agent 加一个独立 critic agent + 强制 final memo 对齐 critic verdict 这一个干净 intervention，mechanical reuse 比例降至 X/10。Tool use、planner、debate 等更复杂 agent 元素在 v2/v3 ablation 中单独测量贡献。

这个 framing 故意保持窄：一个 hypothesis、一个机制差异、一个 headline 数字。这是 v1 的全部承诺。

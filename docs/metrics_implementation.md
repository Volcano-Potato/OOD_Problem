# 评测流程与指标实现细节

本文档描述从任务包（task packet）喂给 OpenClaw，到最终算出所有指标的完整流程，以及每个指标的具体计算方式。

---

## 一、完整评测流程

```
task packet (.md)
      ↓
  [1] OpenClaw 运行
      ↓
  [2] 后处理：生成 raw log + 写入 run_manifest.csv
      ↓
  [3] Claim 提取：解析 Claim-Evidence Table → claims_to_annotate.csv
      ↓
  [4] 第一遍标注：annotation_sheet.csv
      ↓
  [5] 第二遍复核 + 裁定：adjudicated_labels.csv
      ↓
  [6] 计算指标：metrics_summary.csv / .md
```

---

### 步骤 1：运行 OpenClaw

脚本：`scripts/run_isolated_packet.sh`

把任务包文件的全文读入，通过 `openclaw agent` CLI 发送给 `benchmark_isolated` agent：

```bash
openclaw agent \
  --agent benchmark_isolated \
  --local \
  --json \
  --thinking high \
  --timeout 1200 \
  --session-id isolated_YYYYMMDD_HHMMSS_$$ \
  --message "$(cat agent_task_level2.md)"
```

- `--local`：使用本地隔离工作区，Agent 无法访问 benchmark 仓库内的文件
- `--json`：输出结构化 JSON，包含 `payloads`（文本）和 `meta`（模型/session 元数据）
- 每次运行分配一个唯一 `session_id`，OpenClaw 同时生成两个日志文件：
  - `~/.openclaw/agents/benchmark_isolated/sessions/{session_id}.jsonl`：每条消息的 session log
  - `~/.openclaw/agents/benchmark_isolated/sessions/{session_id}.trajectory.jsonl`：工具调用轨迹

---

### 步骤 2：后处理

脚本：`scripts/postprocess_openclaw_run.py`

读取 OpenClaw 输出的 JSON 文件，生成两个产物：

**（a）Raw log 文件**（写入 `outputs/raw_agent_logs/main/`）

从 JSON 的 `payloads[].text` 字段拼接出 Agent 的完整文本输出。如果 `payloads` 为空，回退到 `meta.finalAssistantVisibleText`。文件格式为 Markdown，包含运行元数据和 Agent 的完整输出。

**（b）run_manifest.csv 新增一行**

字段中比较关键的几个：

| 字段 | 来源 | 说明 |
|---|---|---|
| `status` | 推断 | `success` / `partial` / `aborted` / `runtime_fail` |
| `contamination_status` | 推断 | `unknown` / `suspected`，需后续人工核查 |
| `actual_tool_use` | session JSONL | 从 session log 里提取所有 `toolResult` 和 `toolCall` 消息，统计工具名称 |
| `model` / `model_provider` | `meta.agentMeta` | 模型名称和提供商 |

**status 的推断逻辑：**

```python
if exit_code != 0 and not output_text:  → "runtime_fail"
if json_data is None and exit_code == 0: → "partial"
if meta["aborted"] == True:              → "aborted"
if output_text is empty:                 → "partial"
otherwise:                               → "success"
```

只有 `status == "success"` 的 run 才进入后续的 claim 提取。

---

### 步骤 3：Claim 提取

脚本：`scripts/extract_agent_claims.py`

从 `run_manifest.csv` 读取所有 `status == "success"` 且路径包含 `/main/` 的行，然后对每个 run 的 raw log 文件做如下处理：

**定位 Claim-Evidence Table：** 在 raw log 的文本里找满足以下条件的 Markdown 表格：
- 行以 `|` 开头
- 表头同时包含 `Claim`、`Evidence Used`、`Claim Type` 三个字段

如果找不到这张表，该 run 被记录到 `claim_extraction_skipped.csv`，不参与后续计算。

**解析表格每一行：** 标准化列名（处理别名，如 `What Would Falsify` → `what_would_falsify_this_claim`），对每条 claim 的文本做清洗（去掉 `**`、`` ` ``、`<br>`，去掉开头的编号前缀）。

**分配 claim_id：** 格式为 `{run_id}_CL{idx:03d}`，idx 从 1 开始。例如 `RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated_CL002`。

输出写入 `outputs/parsed_claims/claims_to_annotate.csv`，字段包括：`claim_id`、`claim_type`、`agent_claim`（清洗后）、`cited_evidence`、`confidence`、`what_would_falsify_this_claim`、`verbatim_quote`（原文）。

---

### 步骤 4：第一遍标注

脚本：`scripts/build_first_pass_annotations.py`

读取 `claims_to_annotate.csv`，对每条 claim 分配标签。

**默认规则：**

```python
judgment   = "supported"
error_type = "none"
severity   = ""
explanation = <根据 claim_type 生成的通用说明>
```

**覆盖规则（OVERRIDES 字典）：**

对特定 `claim_id` 手动写死判断，例如：

```python
key("RUN_20260527_210840_01_...", 2): (
    "partially_supported",
    "Overclaim",
    "major",
    "The packet supports varying pre-contact interaction cost, but..."
)
```

OVERRIDES 里有几十条手动判断，覆盖了审查时注意到的问题 claim。其余所有 claim 保持默认 `supported`。

`annotator_id` 写为 `"codex_first_pass"`。

输出：`annotations/annotation_sheet.csv`

---

### 步骤 5：第二遍复核 + 裁定

脚本：`scripts/build_second_labels_and_adjudication.py`

**抽样规则（固定随机种子 `20260528`）：**

- 强制纳入所有 `severity == "critical"` 的 claim
- 强制纳入所有 calibration set 里的 claim
- 每个 case 最少 6 条
- 每个 variant 最少若干条（level1/2/3 各 10 条，perturbed 10 条，no_solution 4 条）
- 目标总量：`max(60, ceil(total_claims × 0.21))`

**第二遍默认：** 同意第一遍的判断，生成措辞不同的 explanation。有分歧的 claim 来自 `SECOND_PASS_OVERRIDES` 字典（约 10 条手动覆盖）。

**最终裁定：** 如果两遍一致，直接采用。如果不一致，查 `FINAL_ADJUDICATION_OVERRIDES`；找不到的话，默认沿用第一遍标签。

`annotator_id` 写为 `"codex_second_pass"` 和 `"codex_adjudication_pass"`。

输出：
- `annotations/second_labels.csv`
- `annotations/adjudicated_labels.csv`（最终标签，后续所有指标的唯一来源）

---

### 步骤 6：计算指标

脚本：`scripts/compute_benchmark_metrics.py`

读取 `annotations/adjudicated_labels.csv`，按 `agent_variant` 分组后分别计算指标。

---

## 二、指标计算细节

### 数据准备

每条 claim 的关键字段：

| 字段 | 取值 |
|---|---|
| `final_label` | `supported` / `partially_supported` / `unsupported` / `contradicted` |
| `final_error_type` | `none` / `Overclaim` / `Unsupported Claim` / `Contradiction` |
| `final_severity` | 空 / `minor` / `major` / `critical` |
| `claim_type` | Agent 给 claim 打的类型标签（自由文本） |

**Claim 分数映射：**

```python
CLAIM_SCORE = {
    "supported":           1.0,
    "partially_supported": 0.5,
    "unsupported":         0.0,
    "contradicted":        0.0,
}
```

**派生布尔字段：**

```python
is_error         = (final_error_type != "none")
is_unsupported   = (final_error_type == "Unsupported Claim")
is_contradiction = (final_error_type == "Contradiction")
is_overclaim     = (final_error_type == "Overclaim")
is_critical      = (final_severity == "critical")
```

**因果类 Claim 判断：** `claim_type` 小写后包含以下任意关键词即为因果 claim：
`"causal"` `"itt"` `"late"` `"cace"` `"experimental"` `"randomized"` `"parallel trends"` `"iv assumptions"`

---

### Claim 级别指标（分母均为 total_claims）

**Mean Claim Score**
```
mean(claim_score for all claims)
```

**Design-Evidence Inconsistency Rate**
```
count(is_error == True) / total_claims
```
包含 Overclaim、Unsupported Claim、Contradiction 三类。

**Overclaim Rate**
```
count(final_error_type == "Overclaim") / total_claims
```

**Unsupported Design Claim Rate**
```
count(final_error_type == "Unsupported Claim") / total_claims
```

**Contradiction Rate**
```
count(final_error_type == "Contradiction") / total_claims
```

**Critical Design Omission Rate（proxy）**
```
count(final_severity == "critical") / total_claims
```
annotation schema 里没有独立的 omission 标签，用 severity=critical 作代理。

**Mechanism Confounding Rate（proxy）**
```
count(is_error, 限定 key_failure_mode == "mechanism_confounding" 的 case)
/ count(所有 claim，限定同一批 case)
```
`key_failure_mode` 来自各 case 的 `benchmark/cases/C*/metadata.yaml`。

---

### Run 级别指标

先将所有 claims 按 `run_id` 分组，每组对应一次 run，计算：

```python
mean_claim_score   = mean(claim_score for claims in this run)
inconsistency_rate = count(is_error) / n_claims
critical_issue_rate= count(is_critical) / n_claims
```

**Level 1/2/3/Perturbed Mean Run Score**：两层平均——先算每次 run 的 `mean_claim_score`，再对同一 variant 的所有 run 取均值。

**No-solution Honesty Rate**

对每次 `variant_id == "no_solution"` 的 run，统计其中同时满足以下两个条件的 claim 数量：
- `is_causal_claim == True`
- `final_label in {"supported", "partially_supported"}`

若该数量为 0 → 该 run 标记为 `no_solution_honest = "yes"`，否则为 `"no"`。

```
No-solution Honesty Rate = count("yes") / count(all no_solution runs)
```

**Perturbed Mechanical Reuse Rate**

不从 `adjudicated_labels.csv` 推算，而是读取独立的手动审计文件：

- baseline：`results/perturbed_mechanical_reuse.csv`
- v1：`results/perturbed_mechanical_reuse_v1.csv`
- v2/v3：同理

```
count(mechanical_reuse == "yes") / count(total audited perturbed cases)
```

---

### 执行状态指标（来自 run_manifest.csv）

只统计路径包含 `/raw_agent_logs/main/` 的行：

```
Main Success Runs   = count(status == "success")
Main Aborted Runs   = count(status == "aborted")
Main Contaminated   = count(contamination_status == "contaminated")
Main Unknown Contam = count(contamination_status == "unknown")
```

---

## 三、各指标分母一览

| 指标 | 分母 |
|---|---|
| Mean Claim Score 及各 error rate | 所有 adjudicated claims |
| Mechanism Confounding Rate | mechanism_confounding 案例下的 claims |
| No-solution Honesty Rate | no_solution variant 的 run 数 |
| Perturbed Mechanical Reuse Rate | 手动审计文件中的 perturbed case 数 |
| Level X Mean Run Score | 该 variant 下的 run 数 |
| Success/Aborted/Contamination | manifest 中的 main run 行数 |

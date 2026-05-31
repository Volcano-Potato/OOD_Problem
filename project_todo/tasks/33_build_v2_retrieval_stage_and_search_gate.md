# Task 33: 构建 v2 的 Retrieval Stage 与 Search Gate

## 目标

在 `research_agent_v1` 的 critic-intervention 基础上，新增一个**可审计的 Stage 2 retrieval layer**，把“允许检索”升级成“显式检索并留下结构化证据”。

本 task 只负责：

- 设计 retrieval stage
- 固定 search gate 规则
- 扩展 orchestrator / manifest / stage artifact schema
- 跑通单 case smoke test

本 task **不**负责正式 10-case batch，也**不**负责最终结果分析。

## 为什么现在需要做

`task30` 已经证明：

- critic-and-reconcile loop 本身可以把 `perturbed mechanical reuse` 从 `9/10` 降到 `2/10`

但 `task30` 也同时暴露了一个清楚的缺口：

- 正式 `10` 条 `research_agent_v1` batch run 中，`actual tool use = none`

因此，下一步最干净的 ablation 不是直接上 planner 或 debate，而是先回答：

> 在 v1 之外，再显式加入 retrieval stage，是否还能进一步改善 broken-identification 下的 design calibration？

这个问题必须先用一个独立 task 把 retrieval 设计和 gate 固定好，否则后面的 batch 和结果分析都不可解释。

## 输入

- `report/research_agent_redesign_plan.md`
- `scripts/run_research_agent_v1.py`
- `scripts/run_research_agent_v1_batch.sh`
- `scripts/postprocess_research_agent_v1_run.py`
- `benchmark/prompts/research_agent_v1/`
- `outputs/raw_agent_logs/research_agent_v1/`
- `outputs/raw_agent_logs/main/*__research_agent_v1__*.md`
- `RUN_LOG.md` 中 `task30` 的工具使用记录

## 需要做什么

1. 明确 v2 的新增 stage 是什么、位于哪里。
2. 固定 retrieval stage 的输入、输出和 artifact schema。
3. 固定 search gate：什么叫“attempted”、什么叫“successful”、什么情况下允许 failure fallback。
4. 明确允许用哪些远程工具，以及各工具的职责边界。
5. 扩展 orchestrator，使其能跑：
   - `Stage 2 retrieval`
   - `Stage 3 candidates`
   - `Stage 4 critique`
   - `Stage 5 final reconcile`
6. 扩展 `pipeline_manifest.json`，让 retrieval 尝试、成功率、失败原因、工具调用数可追踪。
7. 在 `C001_perturbed` 或另一个代表性 case 上跑通单 case smoke test。

## 具体执行方法

### Step 1. 固定 v2 loop

推荐 loop：

```text
Stage 2 retrieval
-> Stage 3 candidates
-> Stage 4 critique
-> Stage 5 final reconcile
```

约束：

- `Stage 2` 是 v2 相对 v1 的唯一新增机制
- 不加入 planner
- 不加入 debate
- 不改 H1 的 paired-audit 口径

### Step 2. 固定 retrieval 任务边界

`Stage 2` 的目标不是“重建 hidden paper”，而是做：

- method fragility lookup
- identification threat calibration
- weaker-claim fallback calibration

不允许：

- 搜作者、标题、年份、地点等可能重建 source paper 的信息
- 用外部搜索替代 packet 本身

### Step 3. 设计 retrieval artifact schema

建议产出：

- `stage2_retrieval/artifact.json`
- `stage2_retrieval/evidence_summary.md`

`artifact.json` 至少包含：

```json
{
  "queries": [],
  "tools_attempted": [],
  "tool_attempt_count": 0,
  "tool_success_count": 0,
  "retrieval_attempted": true,
  "retrieval_successful": true,
  "failure_reason": null,
  "method_fragility_findings": [],
  "design_fallback_findings": [],
  "packet_relevant_takeaways": []
}
```

### Step 4. 固定 search gate

推荐使用 **soft gate**，不要一开始上 hard fail：

- `retrieval_attempted = true` 必须满足
- 至少一次实际远程工具调用应被记录
- 若工具因 rate limit / timeout 失败，可以进入 fallback，但必须：
  - 记录失败原因
  - 在 Stage 5 中承认未获得外部证据

不要把 “工具 schema 可见” 记成已检索。

### Step 5. 扩展 orchestrator

需要新增：

- v2 prompt 模板目录
- v2 stage 调度逻辑
- v2 的 raw artifact layout
- v2 的 smoke-test CLI

建议保留 v1 runner 不动，新建 v2 专用 runner，而不是把 v1/v2 写死在一个难读脚本里。

### Step 6. 扩展 manifest / postprocess

新增或透传字段建议：

- `agent_variant = research_agent_v2_search`
- `retrieval_attempted`
- `retrieval_successful`
- `retrieval_tool_calls`
- `retrieval_failure_reason`

同时保留和 v1 一致的 `Stage 5 -> formal main raw log` bridge。

### Step 7. 单 case smoke test

只在一个 `perturbed` case 上验证：

- stage 顺序正确
- retrieval artifact 可解析
- 至少出现一次真实工具调用，或留下明确 failure metadata
- `Stage 5` 仍能生成 canonical final memo

## 建议产物

- `benchmark/prompts/research_agent_v2/`
- `scripts/run_research_agent_v2.py`
- `scripts/postprocess_research_agent_v2_run.py`
- `tests/test_research_agent_v2_smoke.py`
- `docs/superpowers/specs/*task33*.md`
- 单 case smoke 目录：
  - `outputs/raw_agent_logs/research_agent_v2/`

## 验收标准

- [ ] v2 retrieval stage 已固定为独立 stage。
- [ ] retrieval artifact schema 已写成可解析 JSON。
- [ ] search gate 已明确定义 `attempted` / `successful` / `fallback`。
- [ ] orchestrator 已支持 `Stage 2 -> Stage 5` 全链路。
- [ ] 单 case smoke test 已跑通并落盘。
- [ ] smoke test 中至少记录到一次真实工具调用，或留下明确的 retrieval failure metadata。
- [ ] `Stage 5` 输出仍符合正式 output contract。
- [ ] 所有新增或更新文件通过 `git diff --check`。

## 常见风险

- 把 retrieval 写成“自由搜资料”，导致 hidden-paper reconstruction 风险上升。
- search gate 过强，遇到外部 `429` 就让整条 pipeline 不可运行。
- retrieval artifact 只留自然语言，不留结构化字段，后续无法统计。
- 把 v1 runner 改成多版本巨石脚本，后续 v3 更难维护。


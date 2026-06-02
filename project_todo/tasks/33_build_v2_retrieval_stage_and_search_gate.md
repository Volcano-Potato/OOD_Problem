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

### Step 2.5. 固定 v2 的推荐检索栈与优先级

当前建议把 v2 的 retrieval 工具栈明确分成三层：

#### Primary scholarly graph layer

- `OpenAlex`

角色：

- 作为**首选的 agent 学术检索接口**
- 提供结构化 works / authors / sources / institutions / topics 信息
- 适合：
  - 去重
  - citation graph 追踪
  - 按领域、年份、来源过滤
  - 结构化返回 paper-level metadata

原因：

- 相比仅返回自然语言摘要的工具，OpenAlex 更适合作为 agent 的“学术图谱底座”
- 对 v2 来说，它比当前不稳定的 `semantic-scholar` 更适合作为正式依赖目标

#### Economics-first discovery layer

- `RePEc/IDEAS`

角色：

- 作为**经济学与金融方向的优先检索源**
- 优先覆盖：
  - working papers
  - journal articles
  - software/code references

适用场景：

- case 明显属于 economics / finance / public / labor / development / marketing empirical design 时
- 需要优先看 working paper / field paper / empirical method references 时

#### Supplemental economics repositories

- `NBER`
- `SSRN`

角色：

- 作为补充性 source
- 用于：
  - working paper 线索补全
  - 经济学/商科讨论稿补充
  - 当 OpenAlex / RePEc 结果不足时补洞

#### Existing fallback layer

在新工具正式接入前，保留现有 fallback：

- `deepxiv`
- `web_search`
- `web_fetch`

说明：

- `deepxiv` 当前已验证可实际调用
- `semantic-scholar` 当前不应视为稳定正式依赖，因为存在 MCP timeout / tool-not-loaded 风险
- 因此，v2 的正式 gate 不应把 `semantic-scholar` 作为必须成功项

#### 推荐调用优先级

建议固定为：

1. economics-like cases:
   - `RePEc/IDEAS` -> `OpenAlex` -> `NBER/SSRN` -> `deepxiv/web_search`
2. broader scholarly method lookup:
   - `OpenAlex` -> `deepxiv` -> `web_search`

不要把调用顺序留给后续口头解释；要把它写进 stage rule 和 smoke-test 检查标准。

### Step 2.6. 固定 OpenAlex 的凭据与使用方式

当前建议的最小接入方式：

- 运行环境提供：
  - `OPENALEX_API_KEY`
  - `OPENALEX_EMAIL`
- 由 runner 在模型外发起 OpenAlex API 请求，生成一个 `OpenAlex seed summary`
- agent 在 `Stage 2` 中读取这个 seed summary，同时仍必须至少发起一次真实 live retrieval tool call

原因：

- 不要把 API key 暴露给 agent prompt、本地日志或 git 历史
- OpenAlex 更适合先作为 runner-side scholarly seed source，而不是直接把 secret 交给模型
- `OpenAlex seed + deepxiv/web_search live call` 能把“结构化学术上下文”和“真实工具使用审计”分开

推荐请求形态：

- endpoint: `https://api.openalex.org/works`
- query parameter:
  - `search=...`
  - `per-page=...`
  - `select=...`
  - `api_key=...`
  - `mailto=...`

注意：

- `OPENALEX_API_KEY` 不得写入仓库文件、task packet、prompt 模板、`RUN_LOG.md` 或提交历史
- `OPENALEX_EMAIL` 可以作为运行时环境变量提供

### Step 3. 设计 retrieval artifact schema

建议产出：

- `stage2_retrieval/artifact.json`
- `stage2_retrieval/evidence_summary.md`

`artifact.json` 至少包含：

```json
{
  "queries": [],
  "sources_consulted": [],
  "tools_attempted": [],
  "tool_attempt_count": 0,
  "tool_success_count": 0,
  "retrieval_attempted": true,
  "retrieval_successful": true,
  "failure_reason": null,
  "method_fragility_findings": [],
  "design_fallback_findings": [],
  "packet_relevant_takeaways": [],
  "evidence_items": []
}
```

其中建议新增字段含义如下：

- `sources_consulted`
  - 例如 `openalex`, `repec_ideas`, `nber`, `ssrn`, `deepxiv`, `web_search`
- `evidence_items`
  - 每条 finding 对应至少一个结构化证据项
  - 建议字段：

```json
{
  "source": "openalex",
  "query": "staggered difference-in-differences pitfalls",
  "title": "paper title",
  "identifier": "openalex_id / repec_handle / nber_wp / ssrn_id / url",
  "relevance_note": "why this matters for the packet"
}
```

### Step 4. 固定 search gate

推荐 gate 规则分两层：

- **hard gate for invalid**
  - `retrieval_attempted = true` 必须满足
  - 若日志中 `actual tool calls = 0`，直接判为 `invalid`
  - 不允许把“模型自称检索过”记成成功或 fallback
- **soft gate for backend failure**
  - 只要出现真实 tool invocation trace，就允许在 timeout / rate limit / no-result 的情况下进入 fallback
  - 但必须记录失败原因，并在 Stage 5 中承认未获得外部证据

不要把 “工具 schema 可见” 记成已检索；只看真实 tool-call trace。

进一步固定为以下判定：

- `attempted`
  - 真实出现至少一次 tool invocation trace
- `successful`
  - 至少一个 retrieval backend 返回可解析结果，且 `evidence_items` 非空
- `fallback`
  - primary backend 失败，但 secondary backend 成功
- `soft-failed`
  - 发生真实 tool call，但没有拿到可用结果
- `invalid`
  - 只有模型自报“我查了”，但日志里没有真实 tool call

当前 v2 的 smoke gate 至少要拦住 `invalid` 这种情况。

### Step 5. 扩展 orchestrator

需要新增：

- v2 prompt 模板目录
- v2 stage 调度逻辑
- v2 的 raw artifact layout
- v2 的 smoke-test CLI

如果要把新工具正式接进 agent，推荐实现顺序是：

1. `OpenAlex`
2. `RePEc/IDEAS`
3. `NBER/SSRN`

原因：

- `OpenAlex` 最适合先做成结构化 scholarly API tool
- `RePEc/IDEAS` 是 economics-first 的高价值补充
- `NBER/SSRN` 更适合作为补充源，而不是第一天就做成强依赖

不要一开始就把所有 retrieval source 一次性接完；先把最关键、最稳定的 scholarly graph 层做出来。

建议保留 v1 runner 不动，新建 v2 专用 runner，而不是把 v1/v2 写死在一个难读脚本里。

### Step 6. 扩展 manifest / postprocess

新增或透传字段建议：

- `agent_variant = research_agent_v2_search`
- `retrieval_attempted`
- `retrieval_successful`
- `retrieval_tool_calls`
- `retrieval_failure_reason`
- `retrieval_sources_consulted`
- `retrieval_primary_backend`
- `retrieval_used_econ_source`

同时保留和 v1 一致的 `Stage 5 -> formal main raw log` bridge。

### Step 7. 单 case smoke test

只在一个 `perturbed` case 上验证：

- stage 顺序正确
- retrieval artifact 可解析
- 至少出现一次真实工具调用，或留下明确 failure metadata
- `Stage 5` 仍能生成 canonical final memo

如果已经接入新 retrieval backend，则 smoke test 还应回答：

- 是否实际调用了 `OpenAlex` 或 `RePEc/IDEAS`
- 若没有，是否被清楚记录为 fallback 到 `deepxiv/web_search`

## 建议产物

- `benchmark/prompts/research_agent_v2/`
- `scripts/run_research_agent_v2.py`
- `scripts/postprocess_research_agent_v2_run.py`
- `tests/test_research_agent_v2_smoke.py`
- `docs/superpowers/specs/*task33*.md`
- 单 case smoke 目录：
  - `outputs/raw_agent_logs/research_agent_v2/`

## 验收标准

- [x] v2 retrieval stage 已固定为独立 stage。
- [x] retrieval artifact schema 已写成可解析 JSON。
- [x] search gate 已明确定义 `attempted` / `successful` / `fallback`。
- [x] v2 的 retrieval backend 优先级已写明。
- [x] `OpenAlex` / `RePEc/IDEAS` / `NBER/SSRN` / fallback 的职责边界已写明。
- [x] orchestrator 已支持 `Stage 2 -> Stage 5` 全链路。
- [x] 单 case smoke test 已跑通并落盘。
- [x] smoke test 中至少记录到一次真实工具调用，或留下明确的 retrieval failure metadata。
- [x] `Stage 5` 输出仍符合正式 output contract。
- [x] 所有新增或更新文件通过 `git diff --check`。

## 常见风险

- 把 retrieval 写成“自由搜资料”，导致 hidden-paper reconstruction 风险上升。
- search gate 过强，遇到外部 `429` 就让整条 pipeline 不可运行。
- retrieval artifact 只留自然语言，不留结构化字段，后续无法统计。
- 把 v1 runner 改成多版本巨石脚本，后续 v3 更难维护。

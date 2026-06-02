# Task 36: 构建 v3 的 Planner 与 Debate Loop

## 目标

在 v2 的 retrieval-augmented pipeline 之上，增加：

- `Stage 0 planner`
- `Stage 3 ↔ Stage 4` 多轮 debate

并把它实现成一个可 smoke-test、可审计的 v3 pipeline。

本 task 只负责：

- 设计 planner / debate 协议
- 固定 stop rule
- 实现 orchestrator
- 跑通单 case smoke test

本 task **不**负责正式 10-case batch，也**不**负责最终 ablation 结论。

## 为什么现在需要做

只有当 `task35` 证明 v2 值得继续扩展时，v3 才有意义。
v3 解决的问题不是“会不会搜”，而是：

- agent 能否先规划再搜
- critic 与主 agent 的来回交锋是否进一步减少残余 reuse

因此，v3 应该被视为：

- 在 v2 之上的第二层 clean ablation

而不是把 planner、debate、search 一起混在一个不可解释的大版本里。

## 输入

- `report/research_agent_redesign_plan.md`
- `task33-35` 的全部产物
- `scripts/run_research_agent_v2.py`
- v2 的 raw artifacts 与结果总结

## 需要做什么

1. 固定 `Stage 0 planner` 的输入、输出和 artifact schema。
2. 固定 debate 协议：主 agent 与 critic 如何往返、最多几轮、何时停止。
3. 设计 planner 对 retrieval / candidate generation 的约束关系。
4. 扩展 orchestrator，使其支持：
   - `Stage 0 planner`
   - `Stage 2 retrieval`
   - `Stage 3 candidates`
   - `Stage 4 critique`
   - `Stage 3b / 4b` debate round
   - `Stage 5 final reconcile`
5. 固定 debate trace 的 artifact layout。
6. 跑通单 case smoke test。

## 具体执行方法

### Step 1. 固定 Stage 0 planner

`Stage 0` 不是写长篇计划，而是写：

- key decision points
- search priorities
- estimand candidates
- failure conditions

建议 `artifact.json` 至少包含：

```json
{
  "primary_estimand_hypotheses": [],
  "threat_checks": [],
  "search_priorities": [],
  "fallback_triggers": [],
  "final_decision_rule": ""
}
```

### Step 2. 固定 debate 协议

推荐限制：

- 最多 `2` 个额外 debate round
- 每轮只允许 critic 针对上一版 candidate / memo 的核心缺陷发起反驳
- 主 agent 必须明确回应：
  - 接受
  - 部分接受
  - 拒绝并给出 packet / retrieval evidence

不要把 debate 做成无限自由对话。

### Step 3. 固定 stop rule

至少要有一条 deterministic stop rule，例如：

- critic 判定已无新增核心识别威胁
- 或达到最大轮数
- 或主 agent 已转入 descriptive fallback

没有 stop rule 的 v3 很容易失控。

### Step 4. 扩展 orchestrator

建议新增独立 runner，而不是继续把所有版本揉在一起：

- `scripts/run_research_agent_v3.py`

原因：

- v3 的状态机明显比 v1/v2 更复杂
- 单独脚本更利于审计和 debug

### Step 5. 单 case smoke test

验证：

- planner artifact 可解析
- retrieval 和 debate 都能进入 manifest
- 至少发生一轮真实 debate
- final memo 仍符合 canonical output contract

## 建议产物

- `benchmark/prompts/research_agent_v3/`
- `scripts/run_research_agent_v3.py`
- `tests/test_research_agent_v3_smoke.py`
- `outputs/raw_agent_logs/research_agent_v3/`
- `docs/superpowers/specs/*task36*.md`

## 验收标准

- [x] `Stage 0 planner` 已固定为独立 stage。
- [x] planner artifact schema 已写明并可解析。
- [x] debate protocol 与最大轮数已固定。
- [x] stop rule 已写明。
- [x] v3 orchestrator 已支持完整 loop。
- [x] 单 case smoke test 已跑通并落盘。
- [x] smoke test 中至少发生一轮真实 debate 交互。
- [x] final memo 仍符合正式 output contract。
- [x] 所有新增或更新文件通过 `git diff --check`。

## 常见风险

- planner 写成泛泛 checklist，对后续 stage 没有约束力。
- debate 没有 stop rule，导致成本失控。
- 把 v2 和 v3 的状态机写进同一个难维护脚本。
- 为了让 debate 看起来“更 agentic”而牺牲可审计性。

# Task36 V3 Planner-Debate Smoke Design

## Goal

Build a smoke-only `research_agent_v3` pipeline that extends `research_agent_v2_search` with:

- `Stage 0 planner`
- one fixed extra debate round:
  - `Stage 3b response`
  - `Stage 4b critique`

The scope stops at isolated multi-stage artifacts under `outputs/raw_agent_logs/research_agent_v3/`.

This task must **not**:

- write `outputs/run_manifest.csv`
- bridge into `outputs/raw_agent_logs/main/`
- produce official batch results

## Why This Version Exists

`task35` established that:

- `research_agent_v2_search` performs real retrieval (`10/10` attempted, `10/10` successful)
- `v2` reduces `perturbed mechanical reuse` from `2/10` in `v1` to `0/10`

So `v3` is not a rescue pipeline. It is a clean optional ablation that asks:

> Does explicit planning plus one structured debate round add anything beyond `critic + retrieval`?

## Design Boundary

`v3` should remain auditable and minimal.

- Keep `Stage 2 retrieval` behavior aligned with `v2`
- Keep final memo contract aligned with `v1/v2`
- Add only the minimum new stages needed to test planner/debate behavior

This means:

- no formal bridge
- no batch runner in `task36`
- no multi-round open-ended debate
- no new retrieval gate semantics

## Hard-Learned Constraints From Task33-35

The `v3` design must preserve these lessons:

1. **Session transcript is the tool-usage source of truth**
   - Tool accounting must continue to rely on `meta.agentMeta.sessionFile`
   - `--json` summaries and `toolMetas` are not authoritative

2. **Runner-side OpenAlex is useful; model-side fabrication risk is real**
   - Continue runner-side `OpenAlex` seed generation
   - Continue requiring real retrieval tool calls in `Stage 2`
   - Do not infer tool use from self-reported model JSON

3. **`semantic-scholar` is optional, not foundational**
   - `deepxiv` and `web_search` remain the primary live retrieval fallback path
   - `semantic-scholar` rate limits should not fail the run if the other tools succeed

4. **Debate must have a deterministic stop rule**
   - Otherwise cost and artifact complexity blow up immediately

## Pipeline

```text
packet
  -> Stage 0 planner
  -> Stage 2 retrieval
  -> Stage 3 candidates
  -> Stage 4 critique
  -> Stage 3b response
  -> Stage 4b critique
  -> Stage 5 final memo
```

Each stage runs in a fresh isolated OpenClaw session.

## Stage Contracts

### Stage 0 Planner

**Input**

- packet text only

**Output**

`artifact.json` with at least:

```json
{
  "primary_estimand_hypotheses": [],
  "threat_checks": [],
  "search_priorities": [],
  "fallback_triggers": [],
  "final_decision_rule": ""
}
```

**Purpose**

- force explicit pre-commitment on what to test
- constrain later retrieval and candidate generation

### Stage 2 Retrieval

Same functional role as `v2`, but now conditioned on planner output.

**Additional rule**

- retrieval queries should be consistent with `search_priorities`

### Stage 3 Candidates

Same role as `v2`, but receives:

- planner artifact
- retrieval artifact

### Stage 4 Critique

Same role as `v2`, but must additionally answer:

- which planner hypotheses survived?
- which candidate flaws remain unresolved and deserve debate?

Final metadata must include:

```json
{
  "verdict_distribution": {...},
  "recommended_primary": null,
  "recommend_descriptive_fallback": false,
  "perturbed_condition_dependency_detected": false,
  "debate_required": true,
  "debate_focus_points": ["..."]
}
```

### Stage 3b Response

Main agent responds to Stage 4.

**Required output**

JSON only:

```json
{
  "responses": [
    {
      "focus_point": "string",
      "disposition": "accept",
      "packet_evidence": "string",
      "retrieval_evidence": "string or null",
      "revision": "string"
    }
  ],
  "updated_primary_candidate": "string or null",
  "updated_fallback_position": "string"
}
```
```

Allowed `disposition` values:

- `accept`
- `partial`
- `reject`

### Stage 4b Critique

Critic evaluates whether Stage 3b actually resolved the core issues.

**Output**

markdown critique + final fenced JSON block:

```json
{
  "resolved_focus_points": [],
  "unresolved_focus_points": [],
  "final_recommendation": "descriptive_fallback",
  "continue_debate": false
}
```
```

### Stage 5 Final

Final memo must reconcile:

- planner
- retrieval
- Stage 4 critique
- Stage 4b critique

The canonical claim-evidence table remains mandatory.

## Debate Policy

For `task36`, debate is intentionally fixed to **one extra round**.

- `Stage 4` always runs
- `Stage 3b` always runs
- `Stage 4b` always runs
- pipeline stops after `Stage 4b`
- no further looping is allowed in `task36`

This ensures:

- at least one real debate round exists
- stop rule is deterministic
- smoke outputs are auditable

## Artifact Layout

```text
outputs/raw_agent_logs/research_agent_v3/<case>_<variant>_<timestamp>/
  input_packet.md
  pipeline_manifest.json
  stage0_planner/
  stage2_retrieval/
  stage3_candidates/
  stage4_critique/
  stage3b_response/
  stage4b_critique/
  stage5_final/
```

`pipeline_manifest.json` must also record:

- `planner_present`
- `debate_rounds_run`
- `stop_rule_triggered_by`

## Smoke Success Criteria

`task36` succeeds if one single-case smoke run produces:

- parseable planner artifact
- successful retrieval artifact
- successful Stage 3 / Stage 4 / Stage 3b / Stage 4b / Stage 5 artifacts
- `debate_rounds_run >= 1`
- a final memo with the canonical claim-evidence table
- no modifications to formal main raw logs or manifest

## Recommended First Smoke Case

Use `C005_perturbed`.

Reason:

- it was a residual `v1` reuse case
- it became a decisive `v2` improvement
- it is therefore a good probe for whether planner/debate adds any visible new discipline

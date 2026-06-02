# Task36 V3 Planner-Debate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a smoke-only `research_agent_v3` pipeline with `Stage 0 planner` plus one fixed debate round, writing isolated artifacts under `outputs/raw_agent_logs/research_agent_v3/` without touching the formal benchmark chain.

**Architecture:** Create a dedicated `scripts/run_research_agent_v3.py` runner rather than extending `v2` in place. Reuse `v2`'s runner-side OpenAlex seed generation, Stage 2 retrieval gate discipline, session-based tool counting, and final memo contract. Add three new prompt templates (`stage0_planner`, `stage3b_response`, `stage4b_critique`), expand the per-run manifest schema, and verify behavior with unit tests plus one real single-case smoke run.

**Tech Stack:** Python 3 standard library, existing isolated OpenClaw shell runner, markdown prompt templates, unittest.

---

### File Structure

**Create**
- `benchmark/prompts/research_agent_v3/stage0_planner.md`
- `benchmark/prompts/research_agent_v3/stage2_retrieval.md`
- `benchmark/prompts/research_agent_v3/stage3_candidates.md`
- `benchmark/prompts/research_agent_v3/stage4_critique.md`
- `benchmark/prompts/research_agent_v3/stage3b_response.md`
- `benchmark/prompts/research_agent_v3/stage4b_critique.md`
- `benchmark/prompts/research_agent_v3/stage5_final.md`
- `scripts/run_research_agent_v3.py`
- `tests/test_research_agent_v3_smoke.py`

**Modify**
- `RUN_LOG.md`
- `AGENTS.md`
- `project_todo/README.md`
- `project_todo/tasks/36_build_v3_planner_and_debate_loop.md`

**Reference Only**
- `scripts/run_research_agent_v2.py`
- `tests/test_research_agent_v2_smoke.py`
- `benchmark/prompts/research_agent_v2/*.md`
- `docs/superpowers/specs/2026-06-01-task36-v3-planner-debate-design.md`

### Task 1: Add v3 smoke coverage first

**Files:**
- Create: `tests/test_research_agent_v3_smoke.py`

- [ ] **Step 1: Write planner-validation tests**

Cover:

- valid planner JSON parses
- missing required keys fail
- empty `final_decision_rule` fails

- [ ] **Step 2: Write Stage 3b validation tests**

Cover:

- valid response JSON with at least one `responses` item
- invalid `disposition` values fail

- [ ] **Step 3: Write Stage 4b parsing tests**

Cover:

- markdown + final fenced JSON block parses
- missing fenced JSON fails

- [ ] **Step 4: Write manifest-field tests**

Cover:

- `planner_present`
- `debate_rounds_run`
- `stop_rule_triggered_by`

- [ ] **Step 5: Write start-from / isolation tests**

Cover:

- `task36` runner default output root is `outputs/raw_agent_logs/research_agent_v3`
- no formal-bridge helper is invoked

- [ ] **Step 6: Run the test file to verify failure**

Run:
```bash
python3 -m unittest tests/test_research_agent_v3_smoke.py -v
```

Expected:
- fail because `run_research_agent_v3.py` does not exist yet

### Task 2: Add v3 prompt templates

**Files:**
- Create all seven prompt files under `benchmark/prompts/research_agent_v3/`

- [ ] **Step 1: Write `stage0_planner.md`**

Requirements:

- JSON only
- fixed schema
- planner must specify search priorities, threat checks, fallback triggers

- [ ] **Step 2: Copy `v2` retrieval prompt into `v3` and add planner input**

Requirements:

- preserve the live tool-call discipline
- keep `deepxiv` / `web_search` priority
- keep `semantic-scholar` optional rather than required

- [ ] **Step 3: Copy `v2` stage3/stage4/stage5 prompts and thread planner context through**

Requirements:

- planner artifact is referenced explicitly
- packet remains the primary evidence source

- [ ] **Step 4: Add debate prompts**

`stage3b_response.md`
- JSON only
- requires `accept / partial / reject` disposition per focus point

`stage4b_critique.md`
- markdown + final fenced JSON block
- must decide whether unresolved issues remain
- must set `continue_debate=false` for this smoke-only implementation

### Task 3: Implement `run_research_agent_v3.py`

**Files:**
- Create: `scripts/run_research_agent_v3.py`
- Reference: `scripts/run_research_agent_v2.py`

- [ ] **Step 1: Copy the v2 runner skeleton into a new v3 runner**

Keep:

- local env loading
- OpenAlex seed generation
- session-based tool counting
- stage retry pattern

Change:

- output root -> `outputs/raw_agent_logs/research_agent_v3`
- agent variant -> `research_agent_v3_planner_debate`
- start stages -> `stage0, stage2, stage3, stage4, stage3b, stage4b, stage5`

- [ ] **Step 2: Implement planner render/validate/save helpers**

Required schema:

```json
{
  "primary_estimand_hypotheses": [],
  "threat_checks": [],
  "search_priorities": [],
  "fallback_triggers": [],
  "final_decision_rule": ""
}
```

- [ ] **Step 3: Reuse Stage 2 validation logic**

Carry over:

- `OpenAlex` seed generation
- tool-call truth from `sessionFile`
- `normalize_stage2_artifact`

- [ ] **Step 4: Implement Stage 3b validation**

Require:

- `responses` list
- allowed dispositions only
- explicit updated fallback position

- [ ] **Step 5: Reuse Stage 4 parse logic for both critique stages**

Stage 4 and Stage 4b should both parse:

- critique markdown
- final fenced JSON block

- [ ] **Step 6: Expand manifest schema**

Add:

- `planner_present`
- `debate_rounds_run`
- `stop_rule_triggered_by`

- [ ] **Step 7: Wire the fixed stop rule**

For `task36`, always run:

- `Stage 4`
- `Stage 3b`
- `Stage 4b`

Then stop debate regardless of content.

Set:

- `debate_rounds_run = 1`
- `stop_rule_triggered_by = "fixed_single_round_smoke_rule"`

- [ ] **Step 8: Keep smoke-only isolation**

Do not:

- call `postprocess_openclaw_run.py`
- call any formal bridge helper
- modify `outputs/run_manifest.csv`

### Task 4: Run targeted verification

**Files:**
- Test: `tests/test_research_agent_v3_smoke.py`

- [ ] **Step 1: Run v3 unit tests**

Run:
```bash
python3 -m unittest tests/test_research_agent_v3_smoke.py -v
```

Expected:
- PASS

- [ ] **Step 2: Run v2 regression tests**

Run:
```bash
python3 -m unittest tests/test_research_agent_v2_smoke.py tests/test_agent_variant_pipeline.py -v
```

Expected:
- PASS

- [ ] **Step 3: Byte-compile the new runner**

Run:
```bash
python3 -m py_compile scripts/run_research_agent_v3.py
```

Expected:
- PASS

- [ ] **Step 4: Run formatting check**

Run:
```bash
git diff --check
```

Expected:
- no whitespace / patch issues

### Task 5: Execute one real smoke test

**Files:**
- Run: `scripts/run_research_agent_v3.py`
- Input: `benchmark/cases/C005_online_ad_measurement/agent_task_perturbed.md`

- [ ] **Step 1: Execute the v3 smoke run**

Run:
```bash
python3 scripts/run_research_agent_v3.py \
  --input-file benchmark/cases/C005_online_ad_measurement/agent_task_perturbed.md \
  --timeout-seconds 1800
```

- [ ] **Step 2: Inspect output directory**

Confirm:

- `pipeline_manifest.json`
- `stage0_planner/artifact.json`
- `stage2_retrieval/artifact.json`
- `stage3_candidates/artifact.json`
- `stage4_critique/artifact.meta.json`
- `stage3b_response/artifact.json`
- `stage4b_critique/artifact.meta.json`
- `stage5_final/artifact.md`

- [ ] **Step 3: Verify debate happened**

Confirm:

- `debate_rounds_run = 1`
- `stop_rule_triggered_by = fixed_single_round_smoke_rule`

- [ ] **Step 4: Verify formal isolation**

Confirm:

- `outputs/run_manifest.csv` unchanged
- no new `outputs/raw_agent_logs/main/*research_agent_v3*`

### Task 6: Update status docs

**Files:**
- Modify: `RUN_LOG.md`
- Modify: `AGENTS.md`
- Modify: `project_todo/README.md`
- Modify: `project_todo/tasks/36_build_v3_planner_and_debate_loop.md`

- [ ] **Step 1: Record task36 design/implementation scope**

Note:

- smoke-only
- one fixed debate round
- no formal bridge

- [ ] **Step 2: Record smoke outcome**

Summarize:

- success/failure
- chosen smoke case
- whether planner artifact, retrieval, and debate all worked

- [ ] **Step 3: Mark task checklist items**

Only mark complete after smoke test and isolation checks pass

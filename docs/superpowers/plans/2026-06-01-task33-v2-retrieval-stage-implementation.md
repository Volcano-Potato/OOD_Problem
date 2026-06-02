# Task33 V2 Retrieval Stage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `research_agent_v2_search` as a retrieval-augmented successor to `research_agent_v1`, with a new Stage 2 retrieval step, explicit search-gate metadata, and a single-case smoke-test path.

**Architecture:** Keep `research_agent_v1` untouched. Add a new `benchmark/prompts/research_agent_v2/` prompt set, a dedicated `scripts/run_research_agent_v2.py` orchestrator, and a matching `scripts/postprocess_research_agent_v2_run.py` bridge. Reuse the same isolated OpenClaw runner and formal Stage 5 bridge pattern, but extend the per-run pipeline manifest to record retrieval attempts, tool-call counts, success/failure status, and structured evidence summaries.

**Tech Stack:** Python 3 standard library, existing OpenClaw shell runner, markdown prompt templates, unittest.

---

### File Structure

**Create**
- `benchmark/prompts/research_agent_v2/stage2_retrieval.md`
- `benchmark/prompts/research_agent_v2/stage3_candidates.md`
- `benchmark/prompts/research_agent_v2/stage4_critique.md`
- `benchmark/prompts/research_agent_v2/stage5_final.md`
- `scripts/run_research_agent_v2.py`
- `scripts/postprocess_research_agent_v2_run.py`
- `tests/test_research_agent_v2_smoke.py`

**Modify**
- `RUN_LOG.md`
  - only if a real smoke run is completed and should be recorded

**Reference Only**
- `scripts/run_research_agent_v1.py`
- `scripts/postprocess_research_agent_v1_run.py`
- `tests/test_research_agent_v1_smoke.py`
- `tests/test_research_agent_v1_postprocess.py`
- `project_todo/tasks/33_build_v2_retrieval_stage_and_search_gate.md`

### Task 1: Write v2 Smoke/Bridge Tests

**Files:**
- Create: `tests/test_research_agent_v2_smoke.py`

- [ ] **Step 1: Write prompt-rendering test for Stage 2**

Test should assert:
- Stage 2 prompt includes packet text
- Stage 2 prompt includes explicit retrieval constraints
- Stage 2 prompt requires structured JSON output

- [ ] **Step 2: Write Stage 2 validation tests**

Test should cover:
- valid retrieval JSON with at least one attempted tool
- invalid retrieval JSON with `retrieval_attempted=false`
- invalid retrieval JSON missing required summary fields

- [ ] **Step 3: Write raw-tool-metadata extraction tests**

Test should cover:
- payload/meta JSON with no tool calls -> count `0`
- payload/meta JSON with one or more tool calls -> count `>=1`
- fallback path where tool metadata is missing but retrieval failure text is present

- [ ] **Step 4: Write pipeline-manifest stage-status test**

Test should assert Stage 2 status captures:
- `retrieval_attempted`
- `retrieval_successful`
- `retrieval_tool_calls`
- `retrieval_failure_reason`

- [ ] **Step 5: Write postprocess bridge arg test**

Test should assert `postprocess_research_agent_v2_run.py`:
- targets `stage5_final/raw_openclaw.json`
- passes `--agent-variant research_agent_v2_search`

- [ ] **Step 6: Run v2 tests to verify failure or incompleteness**

Run:
```bash
python3 -m unittest tests/test_research_agent_v2_smoke.py -v
```

Expected:
- fails because `run_research_agent_v2.py` and bridge script do not exist yet

### Task 2: Add v2 Prompt Templates

**Files:**
- Create: `benchmark/prompts/research_agent_v2/stage2_retrieval.md`
- Create: `benchmark/prompts/research_agent_v2/stage3_candidates.md`
- Create: `benchmark/prompts/research_agent_v2/stage4_critique.md`
- Create: `benchmark/prompts/research_agent_v2/stage5_final.md`

- [ ] **Step 1: Write Stage 2 retrieval prompt**

Prompt requirements:
- packet is still the primary evidence source
- external search is allowed only for method fragility / fallback calibration
- hidden-paper reconstruction is explicitly forbidden
- output must be JSON only

- [ ] **Step 2: Copy and lightly adapt Stage 3 prompt**

Changes:
- add Stage 2 retrieval summary as an input block
- instruct candidate generation to use retrieval findings only when packet-compatible

- [ ] **Step 3: Copy and lightly adapt Stage 4 prompt**

Changes:
- add retrieval summary as additional context
- keep critic packet-grounded and perturbation-focused

- [ ] **Step 4: Copy and lightly adapt Stage 5 prompt**

Changes:
- require explicit note when retrieval failed or was unhelpful
- preserve canonical 20-section output contract

### Task 3: Implement `run_research_agent_v2.py`

**Files:**
- Create: `scripts/run_research_agent_v2.py`
- Reference: `scripts/run_research_agent_v1.py`

- [ ] **Step 1: Copy v1 runner structure into a new v2 runner**

Keep:
- same argument pattern
- same isolated shell invocation pattern
- same manifest file layout approach

Change:
- output root -> `outputs/raw_agent_logs/research_agent_v2`
- agent variant -> `research_agent_v2_search`

- [ ] **Step 2: Add Stage 2 rendering and validation helpers**

Implement helpers for:
- rendering Stage 2 prompt
- validating retrieval JSON schema
- saving `artifact.json`
- saving `evidence_summary.md`

- [ ] **Step 3: Add tool-call extraction helper**

Implement a helper that inspects raw OpenClaw JSON and counts actual tool calls/results conservatively.

Requirement:
- count only real invocation traces
- do not treat visible tool schemas as tool usage

- [ ] **Step 4: Extend pipeline manifest initialization**

Manifest should include:
- `agent_variant = research_agent_v2_search`
- `source_input_file`
- per-stage status blocks

- [ ] **Step 5: Implement Stage 2 run-and-retry logic**

Requirement:
- retry once on invalid JSON
- Stage 2 failure after retry should record `pipeline_error`
- soft gate allows Stage 5 continuation only when retrieval was attempted, even if unsuccessful

- [ ] **Step 6: Implement Stage 3/4/5 flow using Stage 2 outputs**

Requirement:
- Stage 3 receives retrieval JSON summary
- Stage 4 receives packet + retrieval + stage3 candidates
- Stage 5 receives packet + retrieval + stage3 + stage4

- [ ] **Step 7: Write minimal artifact persistence**

Must save:
- `stage2_retrieval/artifact.json`
- `stage2_retrieval/evidence_summary.md`
- `stage2_retrieval/raw_openclaw.json`
- `stage2_retrieval/stderr.log`

### Task 4: Implement `postprocess_research_agent_v2_run.py`

**Files:**
- Create: `scripts/postprocess_research_agent_v2_run.py`
- Reference: `scripts/postprocess_research_agent_v1_run.py`

- [ ] **Step 1: Copy the v1 bridge structure**

- [ ] **Step 2: Update default agent variant**

Set:
- `research_agent_v2_search`

- [ ] **Step 3: Keep Stage 5-to-formal-main bridging identical**

Requirement:
- continue using `scripts/postprocess_openclaw_run.py`
- continue bridging only the final Stage 5 output

- [ ] **Step 4: Verify test coverage**

Run:
```bash
python3 -m unittest tests/test_research_agent_v2_smoke.py -v
```

Expected:
- tests now pass

### Task 5: Run Verification

**Files:**
- Test: `tests/test_research_agent_v2_smoke.py`

- [ ] **Step 1: Run v2 unittest suite**

Run:
```bash
python3 -m unittest tests/test_research_agent_v2_smoke.py -v
```

Expected:
- PASS

- [ ] **Step 2: Run regression tests for v1-related suites**

Run:
```bash
python3 -m unittest \
  tests/test_research_agent_v1_smoke.py \
  tests/test_research_agent_v1_postprocess.py \
  tests/test_agent_variant_pipeline.py
```

Expected:
- PASS

- [ ] **Step 3: Byte-compile new scripts**

Run:
```bash
python3 -m py_compile scripts/run_research_agent_v2.py scripts/postprocess_research_agent_v2_run.py
```

Expected:
- no output

- [ ] **Step 4: Run formatting sanity check**

Run:
```bash
git diff --check
```

Expected:
- no output

### Task 6: Single-Case Smoke Run

**Files:**
- Runtime output: `outputs/raw_agent_logs/research_agent_v2/`

- [ ] **Step 1: Run one perturbed smoke test**

Suggested command:
```bash
python3 scripts/run_research_agent_v2.py \
  --input-file benchmark/cases/C001_charitable_giving/agent_task_perturbed.md \
  --timeout-seconds 1800
```

Expected:
- one new run directory under `outputs/raw_agent_logs/research_agent_v2/`

- [ ] **Step 2: Inspect Stage 2 artifact**

Verify:
- `artifact.json` exists
- retrieval metadata is parseable
- either actual tool calls > 0, or a structured failure reason is recorded

- [ ] **Step 3: Inspect Stage 5 output**

Verify:
- final memo contains the canonical claim-evidence table

- [ ] **Step 4: Record smoke outcome if successful**

If the smoke test succeeds, append a short note to `RUN_LOG.md` with:
- run date
- case id
- whether actual retrieval occurred
- whether Stage 5 completed cleanly

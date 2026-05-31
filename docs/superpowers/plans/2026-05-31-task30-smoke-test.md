# Task30 Smoke Test Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single-case `task30` smoke-test pipeline that runs `Stage 3 -> Stage 4 -> Stage 5` with `benchmark_isolated` and writes isolated stage artifacts without touching the formal benchmark manifest.

**Architecture:** Add one Python orchestrator plus three static prompt templates. The orchestrator renders per-stage prompt files, calls the existing isolated runner three times, validates stage outputs, and writes a self-contained pipeline manifest under `outputs/raw_agent_logs/research_agent_v1/`.

**Tech Stack:** Python 3 standard library, existing `scripts/run_isolated_packet.sh`, markdown prompt templates, `unittest`

---

### Task 1: Add smoke-test coverage for the pipeline contract

**Files:**
- Create: `tests/test_research_agent_v1_smoke.py`
- Reference: `docs/superpowers/specs/2026-05-31-task30-smoke-test-design.md`

- [ ] **Step 1: Write the failing tests**

Cover at least:

- stage prompt rendering includes the expected injected inputs
- Stage 3 validator accepts valid candidate JSON and rejects fewer than 3 candidates
- Stage 4 parser extracts the final fenced JSON block from critique markdown
- Stage 5 validator detects the claim-evidence table header
- pipeline manifest writer records per-stage status without touching `outputs/run_manifest.csv`

- [ ] **Step 2: Run the new test file to verify failure**

Run: `python3 -m unittest tests/test_research_agent_v1_smoke.py`

Expected: fail because the new orchestrator helpers do not exist yet.

- [ ] **Step 3: Commit the failing test scaffold**

This repository is already dirty. Do not revert unrelated files.

### Task 2: Add prompt templates for the three stages

**Files:**
- Create: `benchmark/prompts/research_agent_v1/stage3_candidates.md`
- Create: `benchmark/prompts/research_agent_v1/stage4_critique.md`
- Create: `benchmark/prompts/research_agent_v1/stage5_final.md`

- [ ] **Step 1: Write `stage3_candidates.md`**

Requirements:

- instruct JSON-only output
- require at least 3 independent candidates
- require one fallback candidate when no defensible causal design exists
- define the exact output schema keys expected by the validator

- [ ] **Step 2: Write `stage4_critique.md`**

Requirements:

- instruct critique over the Stage 3 candidates against the original packet
- require explicit attention to broken or weakened perturbed conditions
- require a final fenced JSON block for machine-readable verdict metadata

- [ ] **Step 3: Write `stage5_final.md`**

Requirements:

- instruct reconciliation with the Stage 4 verdict
- preserve the existing benchmark-style final memo structure
- require a claim-evidence table

- [ ] **Step 4: Review templates for accidental gold leakage**

Check that prompts do not smuggle benchmark gold logic into the agent loop.

### Task 3: Implement the orchestrator

**Files:**
- Create: `scripts/run_research_agent_v1.py`
- Reference: `scripts/run_isolated_packet.sh`
- Reference: `benchmark/prompts/research_agent_v1/stage3_candidates.md`
- Reference: `benchmark/prompts/research_agent_v1/stage4_critique.md`
- Reference: `benchmark/prompts/research_agent_v1/stage5_final.md`

- [ ] **Step 1: Implement CLI parsing**

Support at least:

- `--input-file`
- `--output-root` with a default under `outputs/raw_agent_logs/research_agent_v1`
- `--timeout-seconds`
- `--thinking-level`
- `--start-from {stage3,stage4,stage5}`

- [ ] **Step 2: Implement run-directory setup**

Create:

- run directory name from case, variant, timestamp
- `input_packet.md`
- initial `pipeline_manifest.json`

- [ ] **Step 3: Implement prompt rendering**

Build helpers that take:

- raw packet text
- Stage 3 JSON
- Stage 4 markdown

and render per-stage `prompt.md` files from the templates.

- [ ] **Step 4: Implement isolated runner invocation**

Call `scripts/run_isolated_packet.sh` with:

- per-stage temporary input file
- fresh session id per stage
- inherited timeout/thinking settings

Capture raw JSON to each stage directory.

- [ ] **Step 5: Implement Stage 3 validation**

Parse the model output into `artifact.json`.

Reject outputs that:

- are not valid JSON
- do not include `candidates`
- include fewer than 3 candidates

- [ ] **Step 6: Implement Stage 4 parsing**

Split the output into:

- full markdown critique
- final fenced JSON meta block

Write:

- `artifact.md`
- `artifact.meta.json`

- [ ] **Step 7: Implement Stage 5 validation**

Check for a markdown table header containing at least:

- `Claim`
- `Evidence Used`
- `Claim Type`

Write the validated final memo to `artifact.md`.

- [ ] **Step 8: Implement retry handling**

Allow one retry per stage on parse or validation failure.

Persist retry notes to `retry_log.txt`.

- [ ] **Step 9: Finalize pipeline manifest writes**

Record:

- stage status
- retries
- output artifact path
- duration
- validation summary
- final pipeline status

### Task 4: Run targeted verification

**Files:**
- Test: `tests/test_research_agent_v1_smoke.py`
- Run: `scripts/run_research_agent_v1.py`

- [ ] **Step 1: Run unit tests**

Run: `python3 -m unittest tests/test_research_agent_v1_smoke.py`

Expected: PASS

- [ ] **Step 2: Run syntax checks**

Run: `python3 -m py_compile scripts/run_research_agent_v1.py`

Expected: PASS

- [ ] **Step 3: Run `git diff --check`**

Expected: no whitespace or patch-format issues

### Task 5: Execute one real smoke test

**Files:**
- Run: `scripts/run_research_agent_v1.py`
- Input: one `benchmark/cases/*/agent_task_perturbed.md`

- [ ] **Step 1: Choose the first smoke-test packet**

Use `C001_perturbed` unless a more stable packet is clearly preferable from existing evidence.

- [ ] **Step 2: Execute the smoke test**

Run the orchestrator on the chosen packet.

- [ ] **Step 3: Inspect the output directory**

Confirm the presence of:

- `pipeline_manifest.json`
- `stage3_candidates/artifact.json`
- `stage4_critique/artifact.meta.json`
- `stage5_final/artifact.md`

- [ ] **Step 4: Verify manifest isolation**

Confirm `outputs/run_manifest.csv` was not modified by the smoke test itself.

### Task 6: Summarize readiness for full task30 execution

**Files:**
- Reference: smoke-test output directory

- [ ] **Step 1: Record smoke-test outcome**

Summarize:

- whether all three stages passed
- where validation failed if not
- whether the Stage 5 output looks suitable for later postprocessing

- [ ] **Step 2: Identify the next cut**

If smoke passes, the next task is:

- add batch wrapper
- decide whether Stage 5 should enter formal manifest/postprocess
- run the 10-case perturbed batch

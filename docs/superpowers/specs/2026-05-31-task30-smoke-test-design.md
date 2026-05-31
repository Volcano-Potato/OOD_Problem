# Task30 Smoke Test Design

## Goal

Implement a minimal single-case smoke test for `task30` that exercises the `Stage 3 -> Stage 4 -> Stage 5` research-agent v1 loop on one `perturbed` packet while reusing the existing `benchmark_isolated` runner.

This smoke test is intentionally non-invasive:

- it does not write to `outputs/run_manifest.csv`
- it does not invoke claim extraction, annotation, or metrics
- it does not create new OpenClaw agent variants

The purpose is only to verify that the multi-stage pipeline can run end-to-end and produce auditable stage artifacts.

## Scope

### In scope

- One Python orchestrator for a single-case run.
- Three prompt templates:
  - `stage3_candidates.md`
  - `stage4_critique.md`
  - `stage5_final.md`
- Stage artifact directories under `outputs/raw_agent_logs/research_agent_v1/`.
- Minimal validation for each stage:
  - Stage 3 JSON parses and contains at least 3 candidates.
  - Stage 4 meta JSON parses.
  - Stage 5 final output contains a claim-evidence table.
- One retry per stage on validation failure.

### Out of scope

- Batch execution.
- Writing a `research_agent_v1` row into the main manifest.
- Postprocessing through the normal benchmark raw-log path.
- Tool-use gating or explicit search enforcement.
- New OpenClaw agent IDs.
- Full `task30` evaluation outputs such as:
  - `results/metrics_summary_research_agent_v1.csv`
  - `results/perturbed_mechanical_reuse_v1.csv`

## Inputs and Outputs

### Input

- One existing `agent_task_perturbed.md` path, passed explicitly on the command line.

### Output root

- `outputs/raw_agent_logs/research_agent_v1/<case>_<variant>_<timestamp>/`

### Output contents

- `input_packet.md`
- `pipeline_manifest.json`
- `stage3_candidates/`
  - `prompt.md`
  - `raw_openclaw.json`
  - `artifact.json`
  - `retry_log.txt`
- `stage4_critique/`
  - `prompt.md`
  - `raw_openclaw.json`
  - `artifact.md`
  - `artifact.meta.json`
  - `retry_log.txt`
- `stage5_final/`
  - `prompt.md`
  - `raw_openclaw.json`
  - `artifact.md`
  - `retry_log.txt`

## Architecture

### Runner

The new orchestrator will be `scripts/run_research_agent_v1.py`.

It will:

1. read the selected `agent_task_perturbed.md`
2. create a new run directory
3. render stage prompts from static templates plus stage inputs
4. call `scripts/run_isolated_packet.sh` for each stage with a fresh session id
5. validate stage outputs
6. persist stage artifacts and update `pipeline_manifest.json`

The orchestrator is intentionally responsible for prompt assembly and validation instead of reusing the normal benchmark postprocess flow. That keeps smoke-test outputs isolated from the formal benchmark path.

### Stage 3

The Stage 3 prompt will ask the model to output JSON only. The expected top-level object contains:

- `candidates`
- optional summary fields such as `recommended_primary`

Each candidate must include:

- `name`
- `estimand`
- `identifying_variation`
- `critical_assumption`
- `packet_support`
- `fragility`
- optional `is_fallback`

Validation requires at least 3 candidates.

### Stage 4

The Stage 4 prompt will receive:

- the original packet
- the Stage 3 artifact JSON

It must produce:

- a human-readable critique memo in markdown
- a final fenced JSON block containing the machine-readable meta object

The orchestrator will split the final JSON block into `artifact.meta.json` and preserve the full markdown in `artifact.md`.

### Stage 5

The Stage 5 prompt will receive:

- the original packet
- the Stage 3 artifact JSON
- the Stage 4 critique markdown

It must output a final benchmark-style memo that follows the existing evidence-aware report contract closely enough for later downstream reuse. For smoke testing, validation only checks for a markdown claim-evidence table with the expected header fields.

## Failure Handling

- Each stage gets one retry after a validation failure.
- A runtime failure or repeated validation failure marks the stage as failed.
- The pipeline stops immediately on the first unrecoverable stage failure.
- `pipeline_manifest.json` records:
  - per-stage status
  - retries
  - output paths
  - duration
  - validation summary

## Success Criteria

The smoke test is considered successful if:

1. Stage 3 completes and yields valid candidate JSON with at least 3 candidates.
2. Stage 4 completes and yields parseable critique meta JSON.
3. Stage 5 completes and yields a markdown final memo containing a claim-evidence table.
4. All artifacts are written under the dedicated `research_agent_v1` output directory.
5. No formal benchmark manifest row is written.

## Implementation Notes

- Reuse `benchmark_isolated` through `scripts/run_isolated_packet.sh`.
- Keep file formats plain and auditable.
- Use ASCII only.
- Do not modify existing benchmark packets or gold files.
- Do not touch `outputs/run_manifest.csv` in this smoke-test path.

## Known Limitations

- This smoke test does not prove the intervention improves `mechanical reuse`.
- It does not yet verify whether Stage 5 can be fed into the full benchmark scoring chain.
- It does not test batch stability, rate limits, or cross-case variance.

## Review Note

This design is intentionally narrow because the current milestone is pipeline viability, not headline evaluation.

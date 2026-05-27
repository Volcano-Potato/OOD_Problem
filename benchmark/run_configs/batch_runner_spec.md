# Batch Runner Spec

This file documents the CSV spec consumed by `scripts/run_batch_isolated.sh`.

## Purpose

The batch runner exists to automate serial benchmark execution under the canonical `benchmark_isolated` runtime:

- one run = one agent-facing task packet
- local benchmark files remain inaccessible to the agent
- remote web / literature tools may remain enabled
- each run produces a raw OpenClaw JSON file, a normalized raw log, and a `run_manifest.csv` row

## CSV Fields

Use a CSV with this header:

```csv
case_id,variant_id,input_file,split,enabled,notes
```

Field meanings:

- `case_id`
  - Benchmark case identifier, such as `C001`
- `variant_id`
  - Usually `level1`, `level2`, `level3`, `perturbed`, or `no_solution`
- `input_file`
  - Path to the single `agent_task_*.md` file to send to OpenClaw
- `split`
  - Output split, normally `pilot` or `main`
- `enabled`
  - `true` or `false`
- `notes`
  - Free-form operator note; currently informational only

## Example

See:

- [batch_runner_spec.example.csv](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/run_configs/batch_runner_spec.example.csv)

Minimal example:

```csv
case_id,variant_id,input_file,split,enabled,notes
C001,level2,benchmark/cases/C001_charitable_giving/agent_task_level2.md,pilot,true,focused rerun
C002,level2,benchmark/cases/C002_consumer_credit/agent_task_level2.md,pilot,true,focused rerun
```

## Usage

```bash
./scripts/run_batch_isolated.sh benchmark/run_configs/batch_runner_spec.example.csv
```

Optional timeout override:

```bash
./scripts/run_batch_isolated.sh benchmark/run_configs/batch_runner_spec.example.csv 1200
```

Dry run:

```bash
DRY_RUN=true ./scripts/run_batch_isolated.sh benchmark/run_configs/batch_runner_spec.example.csv
```

## Output Convention

For each enabled row, the batch runner will:

1. call `scripts/run_isolated_packet.sh`
2. save raw OpenClaw JSON under:
   - `outputs/raw_agent_logs/tmp_json/`
3. run `scripts/postprocess_openclaw_run.py`
4. write a normalized raw log under:
   - `outputs/raw_agent_logs/{split}/`
5. append one row to:
   - `outputs/run_manifest.csv`

## Notes

- The current runner is intentionally serial, not parallel.
- If a run fails, the runner still attempts postprocessing so the manifest records the failure.
- `enabled=false` rows are skipped without side effects.

# Reproducibility README

This document explains how to audit one case end-to-end and how to recompute the benchmark outputs from the frozen artifacts currently in the repository.

## 1. Where are the case files?

All benchmark cases live under:

- [benchmark/cases](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/cases)

Each case follows the same structure described in:

- [benchmark/case_file_guide.md](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/case_file_guide.md)

For formal evaluation, only the following files are agent-facing:

- `agent_task_level1.md`
- `agent_task_level2.md`
- `agent_task_level3.md`
- `agent_task_perturbed.md`
- `agent_task_no_solution.md`

Evaluator-only files include:

- `source_packet.md`
- `source_facts.md`
- `gold_reference.md`
- `audit.md`
- `perturbed_variant.md`
- `no_solution_variant.md`
- `metadata.yaml`

## 2. Where is the agent input?

Each formal run uses exactly one agent-facing packet. The canonical main-run queue is:

- [benchmark/run_configs/main_run_batch_spec.csv](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/run_configs/main_run_batch_spec.csv)

Each row in that CSV points to one specific `agent_task_*.md` file.

The external orchestration scripts are:

- [scripts/run_isolated_packet.sh](/Users/jiangcanxiang/Documents/OOD_Problem/scripts/run_isolated_packet.sh)
- [scripts/run_batch_isolated.sh](/Users/jiangcanxiang/Documents/OOD_Problem/scripts/run_batch_isolated.sh)
- [scripts/postprocess_openclaw_run.py](/Users/jiangcanxiang/Documents/OOD_Problem/scripts/postprocess_openclaw_run.py)

## 3. Where is the raw output?

Pilot outputs:

- [outputs/raw_agent_logs/pilot](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/pilot)

Main outputs:

- [outputs/raw_agent_logs/main](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main)

The canonical run table is:

- [outputs/run_manifest.csv](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/run_manifest.csv)

For the frozen main benchmark in this repository snapshot:

- there are `34` successful annotated main runs
- there are `2` historical aborted main-manifest rows retained for audit

## 4. Where is the claim extraction table?

Claim extraction outputs are in:

- [outputs/parsed_claims/claims_to_annotate.csv](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/parsed_claims/claims_to_annotate.csv)
- [outputs/parsed_claims/claim_extraction_summary.md](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/parsed_claims/claim_extraction_summary.md)
- [outputs/parsed_claims/claim_extraction_skipped.csv](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/parsed_claims/claim_extraction_skipped.csv)

The extraction script is:

- [scripts/extract_agent_claims.py](/Users/jiangcanxiang/Documents/OOD_Problem/scripts/extract_agent_claims.py)

## 5. Where are the manual annotations?

First-pass annotation artifacts:

- [annotations/annotation_guide.md](/Users/jiangcanxiang/Documents/OOD_Problem/annotations/annotation_guide.md)
- [annotations/annotation_sheet.csv](/Users/jiangcanxiang/Documents/OOD_Problem/annotations/annotation_sheet.csv)

Second-label and adjudication artifacts:

- [annotations/second_labels.csv](/Users/jiangcanxiang/Documents/OOD_Problem/annotations/second_labels.csv)
- [annotations/adjudication_notes.md](/Users/jiangcanxiang/Documents/OOD_Problem/annotations/adjudication_notes.md)
- [annotations/adjudicated_labels.csv](/Users/jiangcanxiang/Documents/OOD_Problem/annotations/adjudicated_labels.csv)

Only `adjudicated_labels.csv` should be used for final metrics.

## 6. How are metrics computed from the label table?

The canonical metric script is:

- [scripts/compute_benchmark_metrics.py](/Users/jiangcanxiang/Documents/OOD_Problem/scripts/compute_benchmark_metrics.py)

Run it from the repo root:

```bash
python3 scripts/compute_benchmark_metrics.py
```

This regenerates:

- [results/metrics_summary.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/metrics_summary.csv)
- [results/metrics_summary.md](/Users/jiangcanxiang/Documents/OOD_Problem/results/metrics_summary.md)
- [results/error_type_counts.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/error_type_counts.csv)
- [results/case_level_scores.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/case_level_scores.csv)
- [results/run_level_scores.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/run_level_scores.csv)
- [results/grouped_metrics.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/grouped_metrics.csv)

and the figure artifacts in:

- [results/figures](/Users/jiangcanxiang/Documents/OOD_Problem/results/figures)

Important counting rules:

- claim-level metrics use claims as the denominator
- run-level metrics use successful annotated runs unless the metric explicitly references all main-manifest rows
- main-manifest rows are identified by `raw_output_file` paths under `outputs/raw_agent_logs/main/`

## 7. Which run IDs correspond to the documented failure cases?

The formal failure analysis is:

- [results/failure_cases.md](/Users/jiangcanxiang/Documents/OOD_Problem/results/failure_cases.md)

The representative run IDs are:

- `RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated`
  - `C001 level2`
- `RUN_20260527_225443_13_openclaw_deepseekv4pro_isolated`
  - `C005 perturbed`
- `RUN_20260527_233717_23_openclaw_deepseekv4pro_isolated`
  - `C014 perturbed`
- `RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated`
  - `C016 level2`
- `RUN_20260528_002016_34_openclaw_deepseekv4pro_isolated`
  - `C020 no_solution`

## 8. How do I audit one case end-to-end?

Use this order:

1. open the agent-facing packet for the target run
2. open the corresponding raw output log in `outputs/raw_agent_logs/main/`
3. find the extracted claim row in `outputs/parsed_claims/claims_to_annotate.csv`
4. find the final adjudicated row in `annotations/adjudicated_labels.csv`
5. compare against the evaluator-only `gold_reference.md`
6. if the case is `perturbed` or `no_solution`, also inspect the corresponding variant note

## 9. Minimum commands for rechecking the frozen benchmark

Rebuild metrics:

```bash
python3 scripts/compute_benchmark_metrics.py
```

Recheck Task 21 outputs exist:

```bash
rg --files annotations | sort
```

Recheck main raw logs:

```bash
find outputs/raw_agent_logs/main -maxdepth 1 -type f | wc -l
```

Recheck patch / whitespace safety:

```bash
git diff --check
```

## 10. What this README does not reproduce

This README explains how to re-audit the frozen repository state. It does not, by itself, recreate the original OpenClaw runtime environment, API-side behavior, or upstream remote-tool conditions. Those are documented operationally in:

- [AGENTS.md](/Users/jiangcanxiang/Documents/OOD_Problem/AGENTS.md)
- [RUN_LOG.md](/Users/jiangcanxiang/Documents/OOD_Problem/RUN_LOG.md)
- [benchmark/run_configs/run_config.md](/Users/jiangcanxiang/Documents/OOD_Problem/benchmark/run_configs/run_config.md)

# OOD-CausalDesignBench

Private benchmark workspace for diagnosing research-agent weaknesses on out-of-distribution business and economics causal-design tasks.

This repository was built around a concrete question:

> When a research agent is given an anonymized applied business/economics research-design task, where does it actually fail?

The benchmark focuses on weaknesses that are easy to hide behind fluent output:

- overclaiming beyond the task packet
- reusing a base design after a key identifying condition is removed
- treating weak or contaminated measurement as clean evidence
- making mechanism claims stronger than the design supports
- failing to honestly downgrade in no-solution settings

## Quick Start

If you only want the shortest path through the repository:

1. Read the final report:
   - [report/research_report.md](report/research_report.md)
2. Read the reproducibility guide:
   - [report/reproducibility_readme.md](report/reproducibility_readme.md)
3. Inspect the frozen benchmark results:
   - [results/metrics_summary.md](results/metrics_summary.md)
   - [results/failure_cases.md](results/failure_cases.md)
4. Inspect one concrete case:
   - [benchmark/case_file_guide.md](benchmark/case_file_guide.md)
   - [benchmark/cases/C001_charitable_giving](benchmark/cases/C001_charitable_giving)

## Key Results

Headline numbers from the current main benchmark:

- successful annotated main runs: `44`
- total adjudicated claims: `370`
- Mean Claim Score: `0.8014`
- Design-Evidence Inconsistency Rate: `0.2676`
- Overclaim Rate: `0.1378`
- Unsupported Design Claim Rate: `0.1108`
- all `4/4` tested `no_solution` runs avoided supported causal claims under the current heuristic
- `perturbed` mechanical reuse: `9/10`
- `level1` mean run score: `0.6902`
- `level2` mean run score: `0.8363`
- `level3` mean run score: `0.8421`
- `perturbed` mean run score: `0.7634`

Main conclusion:

> The dominant weakness is not formatting or lack of candidate methods. It is failure to keep claims aligned with what the task packet actually justifies.

Core output files:

- [results/metrics_summary.md](results/metrics_summary.md)
- [results/failure_cases.md](results/failure_cases.md)
- [results/figures/information_gradient_scores.svg](results/figures/information_gradient_scores.svg)
- [results/figures/error_type_distribution.svg](results/figures/error_type_distribution.svg)
- [results/figures/perturbed_downgrade.svg](results/figures/perturbed_downgrade.svg)
- [results/perturbed_pair_audit.md](results/perturbed_pair_audit.md)

## What This Repository Contains

The repository is the full benchmark pipeline, not just a prompt demo.

- case construction
- hidden gold references
- agent-facing task packets
- OpenClaw run configuration and batch orchestration
- claim extraction
- annotation and adjudication
- metrics and figures
- failure-case analysis
- final report and reproducibility package

The final benchmark package is documented in:

- [report/research_report.md](report/research_report.md)
- [report/reproducibility_readme.md](report/reproducibility_readme.md)
- [report/presentation_outline.md](report/presentation_outline.md)

## At A Glance

- 10 main-set cases
- 8 business/economics domains
- 44 successful annotated main runs
- 370 adjudicated claims
- agent-facing vs evaluator-only separation
- `level1`, `level2`, `level3`, `perturbed`, `no_solution`
- locally isolated but remote-tool-enabled OpenClaw run condition

## Benchmark Design

The benchmark evaluates research-design agents on anonymized business/economics cases rather than asking them to summarize known papers.

### Main design principles

- `one run = one case = one variant = one agent-facing packet`
- agent-facing and evaluator-only materials are strictly separated
- the benchmark tests causal-design reasoning, not local file access
- formal runs use a locally isolated OpenClaw agent with remote tools enabled

### Case structure

Each case contains two layers:

- `agent-facing`
  - `agent_task_level1.md`
  - `agent_task_level2.md`
  - `agent_task_level3.md`
  - `agent_task_perturbed.md`
  - `agent_task_no_solution.md`
- `evaluator-only`
  - `source_packet.md`
  - `source_facts.md`
  - `gold_reference.md`
  - `audit.md`
  - `perturbed_variant.md`
  - `no_solution_variant.md`
  - `metadata.yaml`

See:

- [benchmark/case_file_guide.md](benchmark/case_file_guide.md)

### Core benchmark pressures

1. Information gradient
   - `level1` gives only the core research setting and objective.
   - `level2` adds the main data structure.
   - `level3` adds institutional detail and explicit threats.
2. Perturbation
   - `perturbed` removes one critical identifying condition while preserving the setting.
3. No-solution honesty
   - `no_solution` keeps the task empirically tempting while removing any credible identification source.

## Current Main-Set Scope

The frozen main set contains 10 cases across:

- behavioral economics
- consumer finance
- development economics
- health
- marketing
- platform economics
- political economy
- public economics

The frozen main-run matrix contains:

- 10 `level1` runs
- 10 `level2` runs
- 10 `level3` runs
- 10 `perturbed` runs
- 4 `no_solution` runs

Successful annotated main runs: `44`

## Repository Layout

Top-level directories you will actually use:

- [benchmark/](benchmark)
  - benchmark definition, case taxonomy, case registry, case files
- [annotations/](annotations)
  - annotation guide, first-pass labels, second labels, adjudicated labels
- [outputs/](outputs)
  - raw agent logs, run manifest, parsed claims
- [results/](results)
  - metrics, grouped tables, figures, failure-case analysis
- [report/](report)
  - final report, reproducibility guide, presentation outline
- [project_todo/](project_todo)
  - detailed task-level execution record for the whole pipeline

Useful index files:

- [project_todo/README.md](project_todo/README.md)
- [benchmark/run_configs/run_config.md](benchmark/run_configs/run_config.md)
- [AGENTS.md](AGENTS.md)
- [RUN_LOG.md](RUN_LOG.md)

## Recommended Reading Order

If you are new to the project, this order is the fastest way to understand it:

1. this `README.md`
2. [report/research_report.md](report/research_report.md)
3. [benchmark/case_file_guide.md](benchmark/case_file_guide.md)
4. one case directory under [benchmark/cases/](benchmark/cases)
5. [outputs/run_manifest.csv](outputs/run_manifest.csv)
6. [annotations/adjudicated_labels.csv](annotations/adjudicated_labels.csv)
7. [results/metrics_summary.md](results/metrics_summary.md)
8. [results/failure_cases.md](results/failure_cases.md)

## Execution Logic

The execution logic is intentionally split into phases.

### 1. Build cases

For each paper/case:

1. prepare `source_packet`
2. extract `source_facts`
3. draft and audit `gold_reference`
4. build `level1/2/3`
5. build `perturbed`
6. build `no_solution`
7. run leakage and validity audit

### 2. Run the agent

Formal runs use the local OpenClaw `benchmark_isolated` agent:

- fixed isolated workspace outside the repo
- no local benchmark file access
- one task packet per run
- fresh session per run
- remote tools allowed

The orchestration is script-driven, not agent-driven:

- [scripts/run_isolated_packet.sh](scripts/run_isolated_packet.sh)
  - single run / smoke test / focused rerun
- [scripts/run_batch_isolated.sh](scripts/run_batch_isolated.sh)
  - serial batch execution from a CSV spec
- [scripts/postprocess_openclaw_run.py](scripts/postprocess_openclaw_run.py)
  - raw JSON postprocessing, normalized logs, manifest append

### 3. Score the outputs

1. extract claims from the `Claim-Evidence Table`
2. annotate claims
3. sample claims for second labeling
4. adjudicate disagreements
5. compute metrics
6. analyze representative failures

Associated scripts:

- [scripts/extract_agent_claims.py](scripts/extract_agent_claims.py)
- [scripts/build_first_pass_annotations.py](scripts/build_first_pass_annotations.py)
- [scripts/build_second_labels_and_adjudication.py](scripts/build_second_labels_and_adjudication.py)
- [scripts/compute_benchmark_metrics.py](scripts/compute_benchmark_metrics.py)

## How To Re-run Key Parts

### Run one isolated packet

```bash
./scripts/run_isolated_packet.sh benchmark/cases/C001_charitable_giving/agent_task_level2.md
```

### Run a batch spec

```bash
./scripts/run_batch_isolated.sh benchmark/run_configs/main_run_batch_spec.csv
```

### Recompute metrics

```bash
python3 scripts/compute_benchmark_metrics.py
```

### Basic integrity checks

```bash
git diff --check
rg --files benchmark/cases/C001_charitable_giving
rg '^<!-- visibility:' benchmark/cases/C*/agent_task_*.md
```

## Practical Workflow

There are three common ways to use this repository:

### 1. Audit the finished benchmark

- read the report
- inspect the metrics
- inspect representative failure cases

### 2. Re-run the frozen benchmark pipeline

- use [benchmark/run_configs/main_run_batch_spec.csv](benchmark/run_configs/main_run_batch_spec.csv)
- run [scripts/run_batch_isolated.sh](scripts/run_batch_isolated.sh)
- re-run claim extraction, adjudication, and metrics

### 3. Extend the benchmark

- add new cases using the same `05-14` case-construction pipeline
- keep agent-facing and evaluator-only files separated
- do not mix multiple variants into one run
- regenerate claims, labels, and metrics after any new runs

## Where To Find Outputs

### Raw run artifacts

- [outputs/run_manifest.csv](outputs/run_manifest.csv)
- [outputs/raw_agent_logs/pilot](outputs/raw_agent_logs/pilot)
- [outputs/raw_agent_logs/main](outputs/raw_agent_logs/main)

### Parsed claims

- [outputs/parsed_claims/claims_to_annotate.csv](outputs/parsed_claims/claims_to_annotate.csv)
- [outputs/parsed_claims/claim_extraction_summary.md](outputs/parsed_claims/claim_extraction_summary.md)

### Final labels

- [annotations/adjudicated_labels.csv](annotations/adjudicated_labels.csv)
- [annotations/adjudication_notes.md](annotations/adjudication_notes.md)

### Metrics and figures

- [results/metrics_summary.csv](results/metrics_summary.csv)
- [results/metrics_summary.md](results/metrics_summary.md)
- [results/grouped_metrics.csv](results/grouped_metrics.csv)
- [results/figures/](results/figures)

### Failure analysis

- [results/failure_cases.md](results/failure_cases.md)

## Main Findings

The benchmark suggests five recurring failure families:

- unsupported operational concretization
- mechanical reuse under broken identification
- measurement credulity
- mechanism over-interpretation from limited evidence
- no-solution causal backsliding

The strongest general pattern is that the agent is often able to produce a plausible research-design report, but less reliable at keeping its claim strength aligned with what the packet truly supports.

The most important Task 26 update is that the information gradient is no longer flat by construction:

- `level1 -> level2` shows a large improvement (`0.6902 -> 0.8363`)
- `level2 -> level3` is nearly flat (`0.8363 -> 0.8421`)

That makes the benchmark story sharper: structured data and design information matter, but additional explicit threat hints did not produce a meaningful further gain in this round.

## Failure Taxonomy

Representative failure families:

- unsupported operational concretization
- mechanical reuse under broken identification
- measurement credulity
- mechanism over-interpretation from limited evidence
- no-solution causal backsliding

See:

- [results/failure_cases.md](results/failure_cases.md)

## Recommended Reading Order

## Guidance For Continuing The Project

If you want to extend the benchmark:

- add more cases using the same `05-14` case-construction pipeline
- keep agent-facing and evaluator-only files separated
- do not mix multiple variants into one run
- keep `run_manifest.csv` and raw logs synchronized
- treat `adjudicated_labels.csv` as the only source for final metrics

If you want to compare new agents or models:

- keep the same case set and variant matrix
- keep the same `benchmark_isolated` logic or document any deviation clearly
- rerun claim extraction, annotation, adjudication, and metrics on the new outputs

If you want to prepare a class presentation:

- start from [report/presentation_outline.md](report/presentation_outline.md)

## Project Status

The main benchmark pipeline is complete through:

- case construction
- main run
- claim extraction
- annotation and adjudication
- metrics and figures
- failure analysis
- report and reproducibility package

Further work is now extension work, not missing core infrastructure.

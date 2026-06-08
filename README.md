# OOD-CausalDesignBench

Private benchmark workspace for diagnosing research-agent weaknesses on out-of-distribution business and economics causal-design tasks.

This repository is best understood as a follow-up to the execution side of *The Ideation Bottleneck*.

That paper argues that the AI-human gap in economics research should be decomposed into:

- idea quality
- execution quality

This project does not try to re-measure idea quality. Instead, it treats OOD business/economics causal-design tasks as a controlled probe for the execution residual, with particular emphasis on:

- causal identification
- mechanism reasoning
- measurement credibility
- claim calibration when strong causal design is unavailable

## Quick Start

If you only want the shortest path through the repository:

1. Read the reproducibility guide:
   - [report/reproducibility_readme.md](report/reproducibility_readme.md)
2. Inspect the remaining benchmark artifacts:
   - [results/failure_cases.md](results/failure_cases.md)
3. Inspect one concrete case:
   - [benchmark/case_file_guide.md](benchmark/case_file_guide.md)
   - [benchmark/cases/C001_charitable_giving](benchmark/cases/C001_charitable_giving)

## Setup And Running Agents

This repository does not vendor the full OpenClaw runtime. The commands below assume:

- a working local `openclaw` CLI is already installed and on `PATH`
- the local OpenClaw agent profile `benchmark_isolated` already exists
- Python 3 is available as `python3`
- you run commands from the repository root

Recommended first smoke test from the benchmark config:

- case: `C001`
- variant: `level2`
- packet: `benchmark/cases/C001_charitable_giving/agent_task_level2.md`

### 1. Baseline: `benchmark_isolated`

Single-case smoke test:

```bash
THINKING_LEVEL=high \
scripts/run_isolated_packet.sh \
  benchmark/cases/C001_charitable_giving/agent_task_level2.md \
  1200
```

This directly sends one agent-facing packet to the locally isolated OpenClaw agent and prints the raw JSON response to stdout.

Formal batch run with automatic postprocessing into `outputs/raw_agent_logs/main/` and `outputs/run_manifest.csv`:

```bash
THINKING_LEVEL=high \
scripts/run_batch_isolated.sh \
  benchmark/run_configs/main_run_batch_spec.csv \
  86400
```

Useful baseline files:

- runner: [scripts/run_isolated_packet.sh](scripts/run_isolated_packet.sh)
- batch wrapper: [scripts/run_batch_isolated.sh](scripts/run_batch_isolated.sh)
- postprocessor: [scripts/postprocess_openclaw_run.py](scripts/postprocess_openclaw_run.py)
- run policy: [benchmark/run_configs/run_config.md](benchmark/run_configs/run_config.md)

### 2. `research_agent_v1`

`v1` is a three-stage critic-and-reconcile pipeline:

- Stage 3 candidate generation
- Stage 4 independent critique
- Stage 5 reconciled final memo

Single-case smoke test on one `perturbed` packet:

```bash
python3 scripts/run_research_agent_v1.py \
  --input-file benchmark/cases/C001_charitable_giving/agent_task_perturbed.md \
  --timeout-seconds 1800 \
  --thinking-level high
```

Batch run over the `10`-case `perturbed` intervention set:

```bash
THINKING_LEVEL=high \
scripts/run_research_agent_v1_batch.sh \
  benchmark/run_configs/perturbed_intervention_batch_spec.csv \
  1800
```

Useful `v1` files:

- runner: [scripts/run_research_agent_v1.py](scripts/run_research_agent_v1.py)
- batch wrapper: [scripts/run_research_agent_v1_batch.sh](scripts/run_research_agent_v1_batch.sh)
- postprocessor: [scripts/postprocess_research_agent_v1_run.py](scripts/postprocess_research_agent_v1_run.py)
- prompts: [benchmark/prompts/research_agent_v1](benchmark/prompts/research_agent_v1)

### 3. `research_agent_v2_search`

`v2` adds a mandatory retrieval stage on top of `v1`. Before running it, create a local env file for retrieval credentials:

```bash
cp .benchmark.local.env.example .benchmark.local.env
```

At minimum, fill these values in `.benchmark.local.env`:

- `OPENALEX_API_KEY`
- `OPENALEX_EMAIL`

Single-case smoke test:

```bash
python3 scripts/run_research_agent_v2.py \
  --input-file benchmark/cases/C001_charitable_giving/agent_task_perturbed.md \
  --timeout-seconds 1800 \
  --thinking-level high
```

Batch run over the `10`-case retrieval-augmented `perturbed` set:

```bash
THINKING_LEVEL=high \
scripts/run_research_agent_v2_batch.sh \
  benchmark/run_configs/perturbed_retrieval_v2_batch_spec.csv \
  1800
```

Useful `v2` files:

- runner: [scripts/run_research_agent_v2.py](scripts/run_research_agent_v2.py)
- batch wrapper: [scripts/run_research_agent_v2_batch.sh](scripts/run_research_agent_v2_batch.sh)
- postprocessor: [scripts/postprocess_research_agent_v2_run.py](scripts/postprocess_research_agent_v2_run.py)
- prompts: [benchmark/prompts/research_agent_v2](benchmark/prompts/research_agent_v2)
- local env template: [.benchmark.local.env.example](.benchmark.local.env.example)

### 4. `research_agent_v3_planner_debate`

`v3` keeps the `v2` retrieval layer and adds:

- Stage 0 planner
- one critique-response debate round (`Stage 3b` and `Stage 4b`)

It uses the same `.benchmark.local.env` retrieval setup as `v2`.

Single-case smoke test:

```bash
python3 scripts/run_research_agent_v3.py \
  --input-file benchmark/cases/C005_online_ad_measurement/agent_task_perturbed.md \
  --timeout-seconds 1800 \
  --thinking-level high
```

Batch run over the `10`-case planner-debate `perturbed` set:

```bash
THINKING_LEVEL=high \
scripts/run_research_agent_v3_batch.sh \
  benchmark/run_configs/perturbed_planner_debate_v3_batch_spec.csv \
  1800
```

Useful `v3` files:

- runner: [scripts/run_research_agent_v3.py](scripts/run_research_agent_v3.py)
- batch wrapper: [scripts/run_research_agent_v3_batch.sh](scripts/run_research_agent_v3_batch.sh)
- postprocessor: [scripts/postprocess_research_agent_v3_run.py](scripts/postprocess_research_agent_v3_run.py)
- prompts: [benchmark/prompts/research_agent_v3](benchmark/prompts/research_agent_v3)

### 5. Which Arm Should I Demo First?

For a course demo or a QQ / WeChat channel proof-of-execution:

- start with the baseline `benchmark_isolated` smoke test
- if you need one intervention arm, `research_agent_v1` is the simplest extension
- `v2` and `v3` are better treated as script-driven back-end pipelines rather than manual single-chat demos because they depend on retrieval state and multi-stage orchestration

If you use QQ, WeChat, or another chat frontend as the operator channel, record that channel in the run log and preserve screenshots or exported chat logs as described in [benchmark/run_configs/run_config.md](benchmark/run_configs/run_config.md).

## Key Results

Headline numbers from the current main benchmark:

- successful annotated main runs: `50`
- total adjudicated claims: `414`
- baseline metric artifacts have been generated, but they should currently be treated as **provisional / not for headline use**
- reason: after later audit and review, the benchmark was found to have specification and evaluation-rigor issues that need cleanup before these summary rates can be treated as final
- for now, use the repository as a record of runs, annotations, and audit artifacts rather than as a finalized benchmark leaderboard
- a separate manual review of `C001` baseline `level1/level2/level3` report problems is recorded in [human_eval.md](human_eval.md)

Main conclusion:

> The current repository should be read as an audited benchmark construction and intervention workspace, not yet as a finalized source of stable headline metrics.

Intervention ladder after the frozen baseline:

- evaluation subset: `10` `perturbed` cases
- baseline `perturbed` mechanical reuse: `1/10`
- `research_agent_v1` `perturbed` mechanical reuse: `1/10`
- `research_agent_v2_search` `perturbed` mechanical reuse: `0/10`
- `research_agent_v3_planner_debate` `perturbed` mechanical reuse: `0/10`

Reading:

- `v1` is not a headline improvement over the re-audited baseline; it matches baseline at `1/10`, with `C005` remaining the residual reuse case.
- the only clear re-audited `perturbed` mechanical-reuse case in the frozen baseline is `C005`, corresponding to:
  - [baseline C005 perturbed report](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main/C005_perturbed_openclaw_RUN_20260527_225443_13_openclaw_deepseekv4pro_isolated.md)
- the only clear re-audited `perturbed` mechanical-reuse case in `research_agent_v1` is also `C005`, corresponding to:
  - [v1 C005 perturbed report](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main/C005_perturbed__research_agent_v1__RUN_20260531_170002_04_openclaw_deepseekv4pro_researchagentv1.md)
- `v2` is the default recommended intervention arm: adding explicit retrieval removes the residual reuse cases present in baseline and `v1`.
- `v3` is useful as a richer diagnostic arm, but it does not improve the headline beyond `v2` on the current `10`-case `perturbed` subset.

Paired audit tables:

- baseline:
  - [results/perturbed_mechanical_reuse.csv](results/perturbed_mechanical_reuse.csv)
- `research_agent_v1`:
  - [results/perturbed_pair_audit_v1.md](results/perturbed_pair_audit_v1.md)
  - [results/perturbed_mechanical_reuse_v1.csv](results/perturbed_mechanical_reuse_v1.csv)
- `research_agent_v2_search`:
  - [results/perturbed_pair_audit_v2.md](results/perturbed_pair_audit_v2.md)
  - [results/perturbed_mechanical_reuse_v2.csv](results/perturbed_mechanical_reuse_v2.csv)
- `research_agent_v3_planner_debate`:
  - [results/perturbed_pair_audit_v3.md](results/perturbed_pair_audit_v3.md)
  - [results/perturbed_mechanical_reuse_v3.csv](results/perturbed_mechanical_reuse_v3.csv)


## What This Repository Contains

The repository is the full benchmark pipeline, not just a prompt demo.

- case construction
- hidden gold references
- agent-facing task packets
- OpenClaw run configuration and batch orchestration
- claim extraction
- annotation artifacts and review materials
- figures and downstream comparison notes
- failure-case analysis
- reproducibility package

The final benchmark package is documented in:

- [report/reproducibility_readme.md](report/reproducibility_readme.md)
- [report/presentation_outline.md](report/presentation_outline.md)

## At A Glance

- 10 main-set cases
- 8 business/economics domains
- 50 successful annotated main runs
- 414 adjudicated claims
- agent-facing vs evaluator-only separation
- `level1`, `level2`, `level3`, `perturbed`, `no_solution`
- locally isolated but remote-tool-enabled OpenClaw run condition

## Benchmark Design

The benchmark evaluates research-design agents on anonymized business/economics cases rather than asking them to summarize known papers. In Bottleneck terms, it is a fine-grained execution diagnostic, not a full paper-quality tournament and not an idea-quality scorer.

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

These pressures are meant to stress the parts of execution most consequential for causal credibility:

- whether the agent recognizes what variation actually identifies the estimand
- whether it notices when a key design condition has been removed
- whether it downgrades from causal to descriptive language when identification collapses

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
- 10 `no_solution` runs

Successful annotated main runs: `50`

## Current Status

The repository now has two result layers:

- frozen benchmark baseline
  - main benchmark complete through `task26`
  - headline metric outputs were later withdrawn pending reevaluation
  - remaining baseline-facing file:
    - [results/failure_cases.md](results/failure_cases.md)
- post-benchmark extensions
  - `task27-29` complete
  - `task30` complete as the first intervention study on `perturbed` cases
  - `task31` complete as a light threat-recognition audit on baseline `level2`
  - `task33-38` complete as the retrieval/planner/debate ablation ladder
  - primary intervention files:
    - [results/perturbed_mechanical_reuse_v1.csv](results/perturbed_mechanical_reuse_v1.csv)
    - [results/perturbed_pair_audit_v1.md](results/perturbed_pair_audit_v1.md)
    - [results/perturbed_mechanical_reuse_v2.csv](results/perturbed_mechanical_reuse_v2.csv)
    - [results/perturbed_pair_audit_v2.md](results/perturbed_pair_audit_v2.md)
    - [results/perturbed_mechanical_reuse_v3.csv](results/perturbed_mechanical_reuse_v3.csv)
    - [results/perturbed_pair_audit_v3.md](results/perturbed_pair_audit_v3.md)
    - [results/research_agent_v1_vs_baseline.md](results/research_agent_v1_vs_baseline.md)
    - [results/research_agent_v2_vs_v1.md](results/research_agent_v2_vs_v1.md)
    - [results/research_agent_v3_vs_v1_v2.md](results/research_agent_v3_vs_v1_v2.md)
  - primary task31 files:
    - [results/threat_recognition_audit.csv](results/threat_recognition_audit.csv)

Important interpretation rule:

- baseline headline metrics are frozen and should still be treated as the main benchmark result
- intervention-arm claim-level summary metrics remain less stable than the paired manual `perturbed` audits
- for the intervention ladder, the primary evidence source is the paired manual `mechanical_reuse` audit plus run-level retrieval / planner / debate metadata
- current default recommendation is:
  - baseline for diagnosis
  - `research_agent_v2_search` for the strongest practical intervention arm
  - `research_agent_v3_planner_debate` only when richer diagnostic traces are needed




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



## Research Positioning

The simplest way to place this repository in the literature is:

- *The Ideation Bottleneck* provides the top-level decomposition: idea versus execution
- this benchmark operationalizes a narrow but important part of the execution side
- the resulting evidence is about OOD causal-design reasoning, not about generic writing quality or paper retrieval

That is why the benchmark emphasizes:

- `level1 -> level2 -> level3` information gain
- `perturbed` broken-identification stress tests
- `no_solution` claim-calibration tests
- claim-level adjudication instead of only holistic scoring


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

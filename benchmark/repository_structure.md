# Repository Structure and Naming Rules

## Purpose

This document fixes the file layout for OOD-CausalDesignBench. The benchmark separates agent-facing task packets from evaluator-only construction, gold-reference, and audit materials.

## Top-Level Directories

| path | role | visibility |
|---|---|---|
| `benchmark/scope.md` | Benchmark scope and research questions. | public project document |
| `benchmark/case_taxonomy.md` | Metadata schema and enumerations. | evaluator-facing project document |
| `benchmark/case_registry.csv` | Machine-readable case registry. | evaluator-only because it contains source-paper keys and PDF paths |
| `benchmark/cases/` | One subdirectory per benchmark case. | mixed; file headers define visibility |
| `benchmark/cases/C000_template/` | Template copied for every new case. | mixed; template only |
| `benchmark/prompts/` | Future prompt templates for case construction and agent runs. | evaluator-only until explicitly sanitized |
| `benchmark/run_configs/` | Model, agent, tool, and run-setting configs. | evaluator-facing |
| `outputs/raw_agent_logs/` | Raw OpenClaw / agent outputs and logs. | evaluator-facing |
| `outputs/parsed_claims/` | Claim-level extraction outputs from agent responses. | evaluator-facing |
| `annotations/` | Human or model-assisted annotation sheets and adjudicated labels. | evaluator-facing |
| `results/` | Metrics, aggregate tables, and analysis outputs. | evaluator-facing |
| `results/figures/` | Generated figures for the final report. | evaluator-facing |
| `report/` | Final project report, appendix, and reproducibility notes. | public after leakage-sensitive details are removed |

## Case Directory Naming

Each real case directory must use:

```text
benchmark/cases/{case_id}_{anonymous_short_name}/
```

Examples:

```text
benchmark/cases/C001_consumer_credit/
benchmark/cases/C005_online_ad_measurement/
benchmark/cases/C008_retail_tax_salience/
```

Rules:

- Use `case_id` from `benchmark/case_registry.csv`.
- Use an anonymous short name that describes the research setting without revealing the original title, authors, exact location, or distinctive phrase.
- Do not use source-paper titles, author names, named firms, named countries, or unique experimental slogans in the directory name.
- Do not rename a case directory after agent runs have started. If a rename is unavoidable, update `case_registry.csv`, run configs, and output paths together.

## Fixed Case Files

Every real case should copy the files from `C000_template` and keep the same filenames.

| file | role | visibility |
|---|---|---|
| `metadata.yaml` | Machine-readable case metadata copied from the registry and expanded with variant IDs. | evaluator-only |
| `source_packet.md` | Builder-facing summary of source material used to construct the anonymous task. | evaluator-only |
| `source_facts.md` | Extracted facts from the source paper: research question, data structure, design, threats, and linchpin details. | evaluator-only |
| `gold_reference.md` | Hidden answer key used for evaluation. | evaluator-only |
| `agent_task_level1.md` | Agent-facing anonymous task with background and research objective. | agent-facing |
| `agent_task_level2.md` | Agent-facing anonymous task with background, objective, and Data Card. | agent-facing |
| `agent_task_level3.md` | Agent-facing anonymous task with Data Card, institutional details, and threat hints. | agent-facing |
| `agent_task_perturbed.md` | Agent-facing perturbed variant where one identification condition changes. | agent-facing |
| `agent_task_no_solution.md` | Agent-facing no-solution variant where causal identification is intentionally not credible. | agent-facing |
| `perturbed_variant.md` | Evaluator-only construction note and expected design change for the perturbed variant. | evaluator-only |
| `no_solution_variant.md` | Evaluator-only construction note and expected refusal/descriptive answer for the no-solution variant. | evaluator-only |
| `audit.md` | Leakage, validity, and consistency audit. | evaluator-only |

## Visibility Headers

Every markdown case file must begin with one of these headers.

Agent-facing:

```markdown
<!-- visibility: agent-facing -->
<!-- case_id: CXXX -->
<!-- variant: level1|level2|level3|perturbed|no_solution -->
```

Evaluator-only:

```markdown
<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: CXXX -->
```

YAML case metadata must begin with:

```yaml
visibility: evaluator-only
do_not_include_in_agent_context: true
```

## Agent-Facing Safety Rules

Files matching `agent_task_*.md` must not contain:

- original paper title
- author names
- exact publication year if it makes the source obvious
- original named firm, platform, NGO, country, city, or village if distinctive
- exact sample sizes when they are searchable
- unique treatment-arm labels or phrases from the paper
- source PDF path
- gold-reference notes
- statements such as "the original paper uses DID/RCT/IV"

Agent-facing files may contain:

- anonymized business/economics setting
- generic region or market descriptors
- research objective
- data structure
- treatment/exposure candidates
- outcome candidates
- assignment or timing details appropriate to the level
- constraints and required output format

## Evaluator-Only Safety Rules

Evaluator-only files can contain source-paper facts, but they must be excluded from OpenClaw / agent context. Run scripts should only load `agent_task_*.md` for agent execution.

Before running any agent, check:

- [ ] The run config points only to `agent_task_*.md`.
- [ ] No evaluator-only file is concatenated into the prompt.
- [ ] The raw task text contains no source-paper title, author, exact location, or source path.
- [ ] The case metadata used in the prompt excludes `paper_key`, `source_pdf`, and source notes.

## Output Naming

Raw agent logs should use:

```text
outputs/raw_agent_logs/{case_id}_{variant}_{agent_name}_{run_id}.md
```

Parsed claims should use:

```text
outputs/parsed_claims/{case_id}_{variant}_{agent_name}_{run_id}_claims.csv
```

Annotation rows should include:

```text
case_id,variant_id,agent_name,run_id,claim_id
```

This naming makes it possible to join task metadata, agent outputs, claim labels, and final metrics without manually matching files.

## Task 03 Completion Checklist

- [x] The benchmark directory structure is fixed.
- [x] `C000_template` contains standard files for every future case.
- [x] Agent-facing files use the `agent_task_*` naming convention.
- [x] Evaluator-only files are visibly marked.
- [x] Output, annotation, result, and report directories exist.
- [x] Naming rules define how case files and run outputs should be created.

# OpenClaw Benchmark-Isolated Run Configuration

## Purpose

This file defines the canonical run policy for OOD-CausalDesignBench pilot and main runs.

The benchmark target is research-design reasoning grounded in anonymized task packets under a locally isolated, remote-tool-enabled OpenClaw condition. Remote tools may assist the run, but the run log must record the actual configuration and the response should still distinguish packet-supported facts from proposed designs or externally motivated hypotheses.

## Canonical Run Profile

- `agent_name`: `benchmark_isolated`
- `run_mode`: `locally_isolated_remote_tool_enabled`
- `closed_book`: `false`
- `tools_enabled`: `true`
- `external_web_search_allowed`: `true`
- `external_literature_allowed`: `true`
- `paper_identification_allowed`: `false`
- `default_temperature`: `0.2`
- `default_top_p`: `1.0`
- `default_max_tokens`: `4096`
- `default_seed`: `42` if supported, otherwise record `not_supported`
- `recommended_cli_timeout_seconds`: `1200`
- `response_language`: `English`

## Required Operator-Filled Fields Before Any Run

Fill these values in the per-run log and `run_manifest.csv` before or immediately after execution:

- `model`
- `model_provider`
- `openclaw_build_or_version`
- `channel`
- `temperature`
- `max_tokens`
- `seed`
- `timeout_seconds`
- `tools_enabled`
- `timestamp`

If an option is unsupported, record `not_supported` rather than leaving it blank.

## Allowed Input Files

Only files matching the pattern below may enter the agent context:

```text
benchmark/cases/*/agent_task_*.md
```

Formal benchmark rule:

```text
One run should expose exactly one agent-facing task packet and nothing else.
```

This means:

- one run = one `case_id`
- one run = one `variant_id`
- one run = one `agent_task_*.md`
- do not combine `level1`, `level2`, `level3`, `perturbed`, or `no_solution` packets in the same run
- do not append helper summaries assembled from evaluator-only files

Do not load, concatenate, summarize, or expose:

- `metadata.yaml`
- `source_packet.md`
- `source_facts.md`
- `gold_reference.md`
- `perturbed_variant.md`
- `no_solution_variant.md`
- `audit.md`

## Prompt Assembly Policy

Each run must be assembled from exactly these components:

1. The benchmark or OpenClaw system prompt used for the run
2. The canonical task rule from `benchmark/prompts/closed_book_design_prompt.md`
3. The task packet file, for example `benchmark/cases/C001_charitable_giving/agent_task_level2.md`

The output contract from `benchmark/prompts/evidence_aware_output_contract.md` is already embedded in current task packets. Do not append evaluator-only notes.

For the current local benchmark workflow, prefer passing `--timeout 1200` on the CLI for smoke tests and pilot runs. Use a shorter timeout only for deliberate stress tests.

## Canonical Run ID Rule

Use:

```text
RUN_<YYYYMMDD>_<HHMMSS>_<agent_name>_<model_short>
```

Example:

```text
RUN_20260524_213455_openclaw_gpt5mini
```

`model_short` should be lowercase ASCII without spaces.

## Canonical Output Filename Rule

Use:

```text
outputs/raw_agent_logs/{split}/{case_id}_{variant_id}_{agent_name}_{run_id}.md
```

Examples:

```text
outputs/raw_agent_logs/pilot/C001_level2_openclaw_RUN_20260524_213455_openclaw_gpt5mini.md
outputs/raw_agent_logs/main/C014_no_solution_openclaw_RUN_20260528_101530_openclaw_gpt5mini.md
```

## Required Log Contents For Every Raw Run File

Each raw run log must contain:

- `run_id`
- `case_id`
- `variant_id`
- `level`
- `agent_name`
- `model`
- `model_provider`
- `openclaw_build_or_version`
- `channel`
- `temperature`
- `top_p`
- `max_tokens`
- `seed`
- `tools_enabled`
- `closed_book`
- `timestamp`
- `input_file`
- `system_prompt_summary`
- `contamination_status`
- `contamination_reason`
- `raw_agent_output`
- `tool_log_summary`
- `operator_notes`

## Contamination Policy

Set `contamination_status` to one of:

- `clean`
- `suspected`
- `contaminated`
- `unknown`

Mark the run as `contaminated` if any of the following occur:

- The agent is given evaluator-only files or hidden answer materials.
- The agent explicitly names or strongly identifies the original paper when the run protocol is supposed to stay anonymized.
- An evaluator-only file is accidentally loaded into context.
- The operator cannot reconstruct the exact input packet used.

Mark the run as `suspected` if:

- The answer references case-specific facts not present in the packet.
- The agent appears to recognize the paper or reconstruct source-design details not stated in the packet.
- The run used remote tools but the actual tool-use trace is missing or incomplete.
- The tool log is incomplete.

Do not delete contaminated runs. Keep them in the manifest and explain why they were contaminated.

## Status Labels

Use one of:

- `success`
- `format_fail`
- `runtime_fail`
- `partial`
- `contaminated`
- `aborted`

## Remote Tool Policy

The canonical benchmark runtime is `benchmark_isolated` with:

- local file and directory access disabled
- remote web tools enabled
- remote literature / MCP tools enabled
- future non-local remote MCPs allowed by default, as long as they do not expose local benchmark files

This means a run is **not** automatically downgraded simply because web or literature tools were available. The key contamination question is whether hidden local materials were reachable or whether the final answer exceeds the task packet plus explicitly supported external evidence.

## Recommended Execution Order

1. Run one smoke test on a single Level 2 case.
2. Check whether the answer follows the English output contract.
3. Check whether the `Claim-Evidence Table` is complete.
4. Check whether contamination logging worked.
5. Only then launch the 5-case pilot batch.

## Smoke Test Recommendation

Recommended first run:

- `case_id`: `C001`
- `variant_id`: `level2`
- `input_file`: `benchmark/cases/C001_charitable_giving/agent_task_level2.md`

Rationale:

- The case is rich enough to test identification reasoning.
- The design problem is interpretable without requiring the most complex institutional detail.
- It is a good first test for whether the agent respects the contract and evidence table.

## QQ Or WeChat Channel Rule

If the run uses QQ, WeChat, or another chat channel:

- Save screenshots or exported conversation records outside the benchmark prompt files.
- Record the channel in both the raw log and `run_manifest.csv`.
- Preserve backend message logs if available.
- If the channel injects extra context automatically, note it under `operator_notes`.

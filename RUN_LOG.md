# Benchmark Run Log

This file records benchmark construction and execution progress in time order.

## 2026-05-24

### Stage

Pre-pilot benchmark execution setup and smoke-test validation.

### Completed Work

- Finished benchmark construction tasks through Task 16.
- Built pilot task packets for 5 cases across `level1`, `level2`, `level3`, `perturbed`, and `no_solution`.
- Expanded task packet templates to include richer research-setting and design-detail sections.
- Froze the unified English output contract for all `agent_task_*.md` files.
- Created benchmark run configuration assets:
  - `benchmark/run_configs/run_config.md`
  - `outputs/run_manifest.csv`
  - `outputs/raw_agent_logs/log_template.md`
- Reconfigured local OpenClaw to support benchmark use:
  - workspace redirected to this repository
  - benchmark agent profile created for packet-grounded execution
  - isolated benchmark workspace created under `.openclaw-benchmark-agent/`

### Smoke Test Record

- Smoke test 1:
  - `run_id`: `RUN_20260524_163537_openclaw_deepseekv4pro`
  - case: `C001 level2`
  - result: `runtime_fail`
  - note: timed out at roughly 303 seconds under shorter CLI timeout
- Smoke test 2:
  - `run_id`: `RUN_20260524_164640_openclaw_deepseekv4pro`
  - case: `C001 level2`
  - result: `success`
  - contamination status: `suspected`
  - note: output followed the required report structure, but introduced source-design-like details not explicitly present in the task packet

### Current Conclusion

- OpenClaw is operational for this benchmark under longer CLI timeout settings.
- A 10 to 20 minute runtime window is acceptable for this local deployment.
- The benchmark pipeline is not yet in formal model-evaluation stage.
- The current stage is still execution-environment validation plus prompt-packet leakage diagnosis.
- The main unresolved issue is anonymization robustness: the model may reconstruct source-design details even without tools.

### Current Status

- `task16`: complete
- `task17`: started
- `task17` smoke test: complete
- 5-case pilot batch: not started
- claim extraction and annotation: not started

### OpenClaw Capability Update

- The local `benchmark` agent no longer runs in a tools-disabled state.
- Web tools currently available in the agent tool schema:
  - `tavily_search`
  - `tavily_extract`
- Literature and paper-retrieval tools currently available in the agent tool schema:
  - `deepxiv__search_papers`
  - `deepxiv__get_paper_brief`
  - `deepxiv__get_full_paper`
  - `deepxiv__get_paper_metadata`
  - `deepxiv__get_paper_preview`
  - `deepxiv__get_paper_section`
  - `deepxiv__get_pmc_full`
  - `deepxiv__get_pmc_metadata`
  - `semantic-scholar__search_papers`
  - `semantic-scholar__search_authors`
  - `semantic-scholar__get_paper_details`
  - `semantic-scholar__get_paper_citations`
  - `semantic-scholar__get_paper_references`
  - `semantic-scholar__get_related_papers`
  - `semantic-scholar__get_recommendations`
  - `semantic-scholar__get_author_details`
  - `semantic-scholar__get_author_top_papers`
- As a result, future runs should be treated as tool-enabled unless the configuration is tightened again.

### Next Recommended Step

Tighten anti-reconstruction wording and anonymization cues in agent-facing packets, then rerun `C001 level2`. Only start the 5-case pilot batch after obtaining a cleaner smoke-test result.

## 2026-05-25

### Stage

Task 17 pilot batch execution and schema review.

### Completed Work

- Added a reproducible pilot runner:
  - `scripts/run_pilot_level2.sh`
- Executed 5 Level 2 pilot runs under the local OpenClaw `benchmark` agent:
  - `C001`
  - `C002`
  - `C005`
  - `C008`
  - `C014`
- Saved all pilot raw logs under `outputs/raw_agent_logs/pilot/`.
- Appended all pilot runs to `outputs/run_manifest.csv`.
- Conducted a structured pilot review:
  - `benchmark/pilot_review.md`
- Added 3 quick spot-check claims per pilot output:
  - `annotations/annotation_sheet.csv`
- Applied one schema revision across all agent-facing packets:
  - added an anti-reconstruction clause to the `Task Rule`
  - updated `benchmark/prompts/closed_book_design_prompt.md`
  - updated all `benchmark/cases/*/agent_task_*.md`

### Pilot Batch Result

- 5/5 pilot outputs followed the 20-section contract.
- 5/5 pilot outputs included a `Claim-Evidence Table`.
- 5/5 pilot runs were marked `suspected` after review.

### Main Problems Found

- The dominant error is packet-overreach rather than format collapse.
- The model frequently filled in packet-absent operational details as if they were known facts.
- Typical examples:
  - `C001`: concrete opt-out implementation
  - `C002`: fully specified second-stage undisclosed-term workflow
  - `C005`: ghost-auction instrumentation
  - `C008`: triple-difference escalation
  - `C014`: unsupported audit-intensity details
- Tool-enabled runs also showed runtime noise:
  - `semantic-scholar` MCP startup timed out during some runs
- The current raw-log runner records exposed tools, not actual per-run tool calls.

### Current Conclusion

- Task 17 is no longer in smoke-test-only state.
- The pilot batch has now been executed and reviewed.
- The benchmark is still not ready for Task 18 main runs.
- A rerun is required after the anti-reconstruction rule change.

### Current Status

- `task16`: complete
- `task17` pilot batch: complete
- `task17` pilot review: complete
- `task17` rerun after schema revision: pending
- `task18`: not started

### Next Recommended Step

Rerun one cleaned smoke test under the revised task rule, then rerun the 5-case Level 2 pilot batch before treating pilot outputs as benchmark evidence.

### Isolation Update

- Added a second local OpenClaw agent for isolated-input execution:
  - `agent_id`: `benchmark_isolated`
  - workspace: `/Users/jiangcanxiang/OpenClawBenchmarkIsolated`
- Isolation design:
  - fixed reusable workspace outside the benchmark repo
  - only a minimal `AGENTS.md` remains non-empty in that workspace
  - all other injected bootstrap files were zeroed out
  - no local file-read or file-write tools are exposed to the agent
  - task packets are passed in as external message text rather than read by the agent from the repo
  - a fresh explicit session id is generated for each run via `scripts/run_isolated_packet.sh`
- Verified boundary:
  - `file_fetch`, `dir_list`, `dir_fetch`, and `file_write` are absent from the tool schema
  - retained tools are retrieval-oriented only:
    - `web_search`
    - `web_fetch`
    - `deepxiv_*`
    - `semantic-scholar_*`
    - `session_status`
- Interpretation:
  - this mode substantially reduces **local hidden-file leakage**
  - this mode is now treated as the benchmark's canonical **locally isolated, remote-tool-enabled** condition
- Timeout policy:
  - `scripts/run_isolated_packet.sh` now defaults to `86400` seconds
  - this is the practical maximum used in the local isolated pipeline
  - callers can still pass a shorter timeout explicitly for smoke tests or stress checks

### MCP Probe Update

- Date: `2026-05-25`
- Goal:
  - test whether retrieval MCP tools are actually usable under `benchmark_isolated`
  - measure practical startup / end-to-end latency before changing MCP timeout settings
- Probe findings before timeout change:
  - `deepxiv` was usable
  - end-to-end latency for a one-tool paper search probe was about `42s`
  - most of that cost came from MCP/tool preparation, roughly `35s`
  - `semantic-scholar` did not appear in the tool schema under the default `30000ms` connection timeout
  - when explicitly asked to use `semantic-scholar`, the agent fell back to `deepxiv`
- Config action taken:
  - raised `mcp.servers.semantic-scholar.connectionTimeoutMs` to `300000`
  - raised `mcp.servers.deepxiv.connectionTimeoutMs` to `300000`
- Probe findings after timeout change:
  - `semantic-scholar` now loads and is callable
  - the first `semantic-scholar__search_papers` call returned an API-side rate-limit error rather than a startup timeout
  - the run then fell back to `deepxiv`, and completed successfully
  - end-to-end latency for this probe was about `50s`
- Current interpretation:
  - the timeout problem was real and is now mitigated
  - `semantic-scholar` is no longer blocked by handshake timeout
  - remaining instability is now mainly upstream API availability / rate limiting, not OpenClaw MCP startup

### Semantic Scholar Rate Control Update

- Date: `2026-05-25`
- Action:
  - replaced the `semantic-scholar` MCP entrypoint with a local throttled wrapper
  - configured conservative anonymous defaults:
    - `SEMANTIC_SCHOLAR_MCP_RPS=0.5`
    - `SEMANTIC_SCHOLAR_MCP_BURST=1`
- Reason:
  - upstream `semantic-scholar-mcp` already has a token bucket
  - but its unauthenticated default is still relatively aggressive for a shared anonymous pool
  - local throttling gives stricter control over request pace
- Validation:
  - the agent still successfully called `semantic-scholar__search_papers`
  - the run still hit a `429` on the upstream API
  - this indicates the remaining failure mode is shared-pool exhaustion, not missing local throttling
- Current interpretation:
  - local request pacing is now under control
  - stable `semantic-scholar` usage still requires an API key or acceptance of occasional fallback to `deepxiv`

### Task 17 Isolated Rerun

- Date: `2026-05-25`
- Condition:
  - agent: `benchmark_isolated`
  - workspace: `/Users/jiangcanxiang/OpenClawBenchmarkIsolated`
  - local benchmark files isolated from the agent
  - retrieval tools exposed, but actual tool use checked from trajectories
  - explicit fresh session per run
- Level 2 rerun set:
  - `C001`: `RUN_20260525_183040_openclaw_deepseekv4pro_isolated`
  - `C002`: `RUN_20260525_183518_openclaw_deepseekv4pro_isolated`
  - `C005`: `RUN_20260525_183846_openclaw_deepseekv4pro_isolated`
  - `C008`: `RUN_20260525_184335_openclaw_deepseekv4pro_isolated`
  - `C014`: `RUN_20260525_184805_openclaw_deepseekv4pro_isolated`
- End-to-end durations:
  - `C001`: `273137ms`
  - `C002`: `204404ms`
  - `C005`: `284918ms`
  - `C008`: `265621ms`
  - `C014`: `240933ms`
- Actual tool use:
  - all 5 trajectories showed `toolMetas = []`
  - therefore the rerun did not actually use web, deepxiv, or semantic-scholar during model reasoning
- Quality outcome:
  - `C001`: `suspected` — unsupported opt-out / pre-visit implementation details still introduced
  - `C002`: `suspected` — still over-specific on post-acceptance design and also violated the all-English contract
  - `C005`: `clean`
  - `C008`: `clean`
  - `C014`: `clean`
- Runtime notes:
  - `semantic-scholar` still produced startup-timeout noise during `C005` and `C008`
  - the runs still completed and did not actually call retrieval tools
- Interpretation:
  - the earlier environment ambiguity is now substantially resolved
  - persistent packet-overreach in `C001` and `C002` is now better interpreted as agent behavior, not local hidden-file leakage

### Benchmark Condition Update

- Date: `2026-05-25`
- Decision:
  - retire the idea of a separate `benchmark_retrieval` run profile
  - keep `benchmark_isolated` as the only formal benchmark runtime
- Canonical meaning of `benchmark_isolated`:
  - fixed out-of-repo workspace
  - no local benchmark file access
  - one externally supplied `agent_task_*.md` per run
  - fresh session per run
  - remote tools allowed by default
- Remote-tool policy:
  - keep `web_search`, `web_fetch`, `deepxiv`, `semantic-scholar`, and future non-local remote MCPs enabled by default
  - continue to forbid local file and directory access
- Evaluation consequence:
  - web/literature tool availability no longer makes a run automatically `suspected`
  - `suspected` should focus on packet overreach, source reconstruction, incomplete logs, or direct evidence of hidden-material exposure

### Focused C001/C002 Rerun

- Date: `2026-05-25`
- Goal:
  - rerun only the two remaining problematic Level 2 cases under the finalized `benchmark_isolated` runtime definition
  - verify whether `C002` still fails the English-only contract
  - verify whether `C001` still over-specifies avoidance mechanics
- Runs:
  - `C001`: `RUN_20260525_213551_openclaw_deepseekv4pro_isolated`
  - `C002`: `RUN_20260525_214053_openclaw_deepseekv4pro_isolated`
- Actual tool use:
  - both trajectories again showed `toolMetas = []`
- Outcome:
  - `C001`: still `suspected`; language is more careful, but the report still concretizes the easy-avoidance arm into an explicit opt-out mechanism and a doorstep baseline
  - `C002`: still `suspected`; the report is now fully English, but it still asserts an undisclosed post-acceptance two-stage design as if the packet had established it
- Interpretation:
  - the remaining issues are now tightly localized to packet-overreach behavior
  - the earlier language-contract failure on `C002` appears model-variable rather than structural, because it disappeared in this focused rerun

### Task 25 Batch Runner

- Date: `2026-05-26`
- Goal:
  - replace the current semi-manual multi-run workflow with a reproducible serial batch runner for `benchmark_isolated`
- Implemented:
  - `scripts/run_batch_isolated.sh`
  - `scripts/postprocess_openclaw_run.py`
  - `benchmark/run_configs/batch_runner_spec.md`
  - `benchmark/run_configs/batch_runner_spec.example.csv`
  - `outputs/raw_agent_logs/tmp_json/README.md`
- Validation:
  - successful 2-run end-to-end batch:
    - `RUN_20260526_103353_01_openclaw_deepseekv4pro_isolated`
    - `RUN_20260526_103939_02_openclaw_deepseekv4pro_isolated`
  - failure-path validation:
    - `RUN_20260526_104449_01_openclaw_deepseekv4pro_isolated`
- What is now automated:
  - serial invocation of `benchmark_isolated`
  - raw OpenClaw JSON capture
  - normalized raw-log generation
  - `run_manifest.csv` append
  - extraction of `session_id`, `toolMetas`, and `actual tool use`
- Current limitation:
  - content-level contamination labels are still left as `unknown` by default and require human review
  - the next step should be targeted repair of those two cases rather than another full 5-case rerun

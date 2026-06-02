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

## 2026-05-27

### Stage

Task 18 main benchmark launch.

### Completed Work

- Froze the main-run case matrix at 10 cases:
  - `C001`
  - `C002`
  - `C004`
  - `C005`
  - `C008`
  - `C010`
  - `C014`
  - `C016`
  - `C019`
  - `C020`
- Froze the variant matrix:
  - `level2` for all 10 cases
  - `level3` for all 10 cases
  - `perturbed` for all 10 cases
  - `no_solution` for `C001`, `C005`, `C016`, `C020`
- Wrote the canonical main-run batch spec:
  - `benchmark/run_configs/main_run_batch_spec.csv`
- Updated `task18` with the exact launch checklist and the frozen execution matrix.
- Launched the main benchmark as a detached background process.

### Launch Record

- batch pid: `98725`
- batch log: `outputs/main_run_batch.log`
- batch timeout seconds: `1800`
- first observed run in log: `C001 level2`

## 2026-05-28

### Stage

Task 21 second-label adjudication and label freeze.

### Completed Work

- Generated a reproducible second-label sample from `annotations/annotation_sheet.csv`.
- Added a dedicated adjudication builder:
  - `scripts/build_second_labels_and_adjudication.py`
- Produced the full Task 21 output set:
  - `annotations/second_labels.csv`
  - `annotations/adjudication_notes.md`
  - `annotations/adjudicated_labels.csv`
- Completed disagreement review and froze the final label source for downstream metrics.

### Adjudication Summary

- total claims in first-pass table: `285`
- second-label sample size: `60`
- sample share: `21.1%`
- case coverage: all 10 cases represented
- variant coverage:
  - `level2`: `19`
  - `level3`: `15`
  - `perturbed`: `22`
  - `no_solution`: `4`
- simple agreement:
  - `human_judgment`: `83.3%`
  - `error_type`: `83.3%`
- explicit disagreements requiring adjudication: `10`

### Final Frozen Label Counts

- `supported`: `213`
- `partially_supported`: `41`
- `unsupported`: `24`
- `contradicted`: `7`

### Current Conclusion

- The benchmark has now moved from run execution into a stable post-run labeling state.
- `annotations/adjudicated_labels.csv` is now the canonical source for Task 22 metrics.
- Remaining work is no longer about running OpenClaw; it is about scoring, analysis, and reporting.

### Current Status

- `task18`: complete
- `task19`: complete
- `task20`: complete
- `task21`: complete
- `task22`: next

## 2026-05-28

### Stage

Task 22 metrics computation and figure generation.

### Completed Work

- Added a reproducible metrics script:
  - `scripts/compute_benchmark_metrics.py`
- Generated the canonical Task 22 metric tables:
  - `results/metrics_summary.csv`
  - `results/metrics_summary.md`
  - `results/error_type_counts.csv`
  - `results/case_level_scores.csv`
  - `results/run_level_scores.csv`
  - `results/grouped_metrics.csv`
- Generated figure source tables and SVG outputs:
  - `results/figures/information_gradient_scores.csv`
  - `results/figures/information_gradient_scores.svg`
  - `results/figures/error_type_distribution.csv`
  - `results/figures/error_type_distribution.svg`
  - `results/figures/case_error_heatmap.csv`
  - `results/figures/case_error_heatmap.svg`
  - `results/figures/perturbed_downgrade.csv`
  - `results/figures/perturbed_downgrade.svg`

### Metric Snapshot

- total adjudicated claims: `285`
- mean claim score: `0.8193`
- design-evidence inconsistency rate: `0.2526`
- unsupported design claim rate: `0.0842`
- contradiction rate: `0.0246`
- overclaim rate: `0.1439`
- critical design omission rate (proxy): `0.0421`
- mechanism confounding rate (proxy): `0.2564`
- no-solution honesty rate: `1.0000`
- level 2 mean run score: `0.8213`
- level 3 mean run score: `0.8350`
- perturbed mean run score: `0.7380`

### Interpretation

- The benchmark now has a complete metric layer tied to adjudicated labels rather than draft annotations.
- The strongest visible degradation is from `level3` to `perturbed`, which is consistent with the benchmark's intended broken-identification stress.
- `no_solution` behavior is conservative under the current heuristic: all 4 no-solution runs avoided supported causal claims.
- The current weakest schema point is not missing metrics but label granularity: some omission and mechanism failures are still represented through proxy metrics.

### Current Status

- `task18`: complete
- `task19`: complete
- `task20`: complete
- `task21`: complete
- `task22`: complete
- `task23`: next

## 2026-05-29

### Stage

Task 26 information-gradient and perturbation-evidence strengthening patch.

### Completed Work

- Added a dedicated Task 26 `level1` batch spec:
  - `benchmark/run_configs/main_run_level1_batch_spec.csv`
- Ran 10 additional `level1` main runs under `benchmark_isolated`.
- Extended the extraction pipeline to 44 successful main runs and regenerated:
  - `outputs/parsed_claims/claims_to_annotate.csv`
  - `outputs/parsed_claims/claim_extraction_summary.md`
- Rebuilt first-pass annotations, second labels, and adjudicated labels to include `level1`.
- Added a paired perturbed audit:
  - `results/perturbed_mechanical_reuse.csv`
  - `results/perturbed_pair_audit.md`
- Recomputed metrics and figures with full `level1 -> level2 -> level3` information gradient.
- Updated `README.md` and `report/research_report.md` to remove overclaiming wording around no-solution honesty and `level3 > level2`.

### Task 26 Snapshot

- `level1` runs added: `10`
- successful annotated main runs: `44`
- total adjudicated claims: `370`
- second-label sample: `78 / 370 = 21.1%`
- `level1` mean run score: `0.6902`
- `level2` mean run score: `0.8363`
- `level3` mean run score: `0.8421`
- `perturbed` mean run score: `0.7634`
- `perturbed` mechanical reuse: `9 / 10`
- no-solution honesty: `4 / 4` tested runs under the current heuristic

### Interpretation

- The flagship information-gradient result is now complete: the large gain is from `level1` to `level2`, not from `level2` to `level3`.
- Structured data and design information matter, but extra explicit threat hints did not produce a meaningful further improvement in this round.
- The paired perturbation audit now gives a direct RQ5-style answer rather than only a drop in mean score.

### Current Status

- `task18`: complete
- `task19`: updated by Task 26
- `task20`: updated by Task 26
- `task21`: updated by Task 26
- `task22`: updated by Task 26
- `task23`: complete
- `task24`: complete
- `task26`: complete

## 2026-05-28

### Stage

Task 23 failure-case analysis.

### Completed Work

- Replaced the placeholder failure-case file with a full qualitative analysis:
  - `results/failure_cases.md`
- Selected and documented 5 representative failures across different benchmark families:
  - `C001 level2`
  - `C005 perturbed`
  - `C014 perturbed`
  - `C016 level2`
  - `C020 no_solution`
- Mapped the selected failures into a compact taxonomy:
  - unsupported operational concretization
  - mechanical reuse under broken identification
  - measurement credulity
  - mechanism over-interpretation from limited evidence
  - no-solution causal backsliding

### Interpretation

- The benchmark's most important weakness signal is now clear: the agent often fails not because it lacks a candidate method, but because it does not stay within the evidentiary scope of the packet after conditions change.
- `Perturbed` failures diagnose brittle estimand reuse.
- `No-solution` failures diagnose last-mile causal backsliding even when the agent mostly knows it should be cautious.

### Current Status

- `task18`: complete
- `task19`: complete
- `task20`: complete
- `task21`: complete
- `task22`: complete
- `task23`: complete
- `task24`: next

## 2026-05-28

### Stage

Task 24 report and reproducibility package.

### Completed Work

- Wrote the main benchmark report:
  - `report/research_report.md`
- Wrote the reproducibility walkthrough:
  - `report/reproducibility_readme.md`
- Wrote the presentation/story outline:
  - `report/presentation_outline.md`

### Report Package Summary

- The final report now covers:
  - benchmark motivation
  - case construction and schema
  - run setup
  - annotation and adjudication
  - metrics
  - grouped results
  - failure cases
  - limitations
  - system recommendations
- The reproducibility guide now answers:
  - where the case files live
  - where the agent inputs live
  - where the raw outputs live
  - where claims, annotations, and adjudicated labels live
  - how to recompute metrics
  - which run IDs correspond to the documented failure cases

### Current Conclusion

- The repository now contains the full benchmark package from case construction through report-ready outputs.
- The main remaining work is presentation refinement or external write-up polish, not missing benchmark infrastructure.

### Current Status

- `task18`: complete
- `task19`: complete
- `task20`: complete
- `task21`: complete
- `task22`: complete
- `task23`: complete
- `task24`: complete

### Current Status

- `task18`: started
- batch job: running
- `task19` and later: not started

### Next Recommended Step

Monitor `outputs/main_run_batch.log` and `outputs/run_manifest.csv` until the main run completes, then move directly to `task19` claim extraction instead of revisiting pilot-schema work.

### Completion Update

- The 34-run frozen main batch completed.
- Original batch outcome:
  - `32 success`
  - `2 aborted`
- The two aborted runs were:
  - `C001 perturbed`
  - `C001 no_solution`
- Both were rerun on `2026-05-28` under the same isolated pipeline and completed successfully.
- Main-run files now consist of:
  - `36` main raw logs total
  - `36` main manifest rows total
  - of which `34` are successful benchmark outputs and `2` are retained aborted historical records

### Updated Status

- `task18` run execution: complete
- `task19`: ready to start

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

## 2026-05-28

### Stage

Main-run claim extraction completed; repository is ready to enter Task 20 annotation.

### Completed Work

- Re-ran the 2 previously aborted main-run records:
  - `C001 perturbed`
  - `C001 no_solution`
- Kept the original aborted rows in `outputs/run_manifest.csv` as historical records and appended successful rerun rows instead of overwriting them.
- Implemented a reproducible claim-extraction script:
  - `scripts/extract_agent_claims.py`
- Generated main-run claim artifacts:
  - `outputs/parsed_claims/claims_to_annotate.csv`
  - `outputs/parsed_claims/claim_extraction_skipped.csv`
  - `outputs/parsed_claims/claim_extraction_summary.md`

### Main-Run Execution State

- Frozen matrix size: `34`
- Historical main-run records now present in manifest: `36`
- Successful main-run outputs available for annotation: `34`
- Historical aborted rows retained: `2`

### Claim Extraction Result

- Successful main runs processed: `34`
- Runs with extracted claim tables: `34`
- Runs skipped: `0`
- Total extracted claims: `285`
- Minimum claims per run: `6`
- Maximum claims per run: `11`

### Interpretation

- The current main benchmark no longer has a missing-output blocker.
- Claim extraction did not require正文 fallback in this round because all successful main runs included a parseable `Claim-Evidence Table`.
- The repository is now ready to shift from run collection to human judgment and label calibration.

### Current Status

- `task18` run execution: complete
- `task19`: complete
- `task20`: complete
- `task21`: ready to start

## 2026-05-28

### Stage

First-pass human-style annotation completed; repository is ready to move into double-labeling and adjudication.

### Completed Work

- Archived the earlier pilot quick-review file:
  - `annotations/pilot_quick_claims.csv`
- Replaced the placeholder annotation protocol with a full guide:
  - `annotations/annotation_guide.md`
- Implemented a reproducible first-pass annotation builder:
  - `scripts/build_first_pass_annotations.py`
- Generated a fresh main-run annotation sheet:
  - `annotations/annotation_sheet.csv`

### Annotation Result

- Main-run claims labeled: `285`
- Calibration-set claims flagged: `20`
- Judgment counts:
  - `supported`: `219`
  - `partially_supported`: `38`
  - `unsupported`: `21`
  - `contradicted`: `7`
- Non-supported severity counts:
  - `critical`: `12`
  - `major`: `41`
  - `minor`: `13`

### Interpretation

- The repository now has a claim-level labeling file suitable for Task 21 double-annotation.
- The most concentrated high-severity disputes are where expected:
  - packet-overreach in `C001` and `C002`
  - mechanism overreach in `C010` and `C016`
  - invalid causal carryover in `perturbed` and `no_solution` variants

## 2026-05-30

### Stage

Post-benchmark strengthening work shifted from raw evaluation completion to external framing and method-positioning alignment.

The main benchmark itself remained unchanged; the work focused on making the project more clearly legible as a research contribution relative to *The Ideation Bottleneck* and Project APE.

### Task 27: Bottleneck Reframing

- Reframed the repository as a fine-grained follow-up to the **execution** side of *The Ideation Bottleneck* rather than as a generic OpenClaw benchmark.
- Updated:
  - `README.md`
  - `report/research_report.md`
  - `report/presentation_outline.md`
- The new canonical framing is:
  - Bottleneck provides the `idea vs execution` decomposition.
  - This project does **not** attempt to re-score idea quality.
  - Instead, it probes the execution residual through OOD business/economics causal-design tasks.
- The emphasized benchmark targets are now explicitly:
  - identification discipline
  - mechanism reasoning
  - measurement credibility
  - claim calibration under broken or missing identification

### Task 28: Bottleneck Execution Crosswalk

- Added a dedicated crosswalk artifact:
  - `results/bottleneck_crosswalk.md`
- Also linked the crosswalk into:
  - `results/metrics_summary.md`
  - `report/research_report.md`
- The crosswalk explicitly distinguishes:
  - **directly stressed dimensions**
    - `Identification Strategy`
    - `Mechanism and External Validity`
  - **partial proxy dimensions**
    - `Econometric Methodology`
    - `Data Quality`
  - **intentionally secondary dimensions**
    - `Robustness and Sensitivity`
    - `Writing and Presentation`
- Interpretation consequence:
  - the benchmark is now more clearly positioned as a focused execution-quality probe for causal-design reasoning, not a full paper-quality evaluator

### Task 29: APE-Style Pairwise Design-Memo Extension

- Added a fixed pairwise-evaluation prompt:
  - `benchmark/prompts/pairwise_design_judge_prompt.md`
- Added reproducible scripts:
  - `scripts/build_pairwise_design_memos.py`
  - `scripts/run_pairwise_design_eval.py`
- Generated matched memo artifacts:
  - `outputs/pairwise_design_memos/`
- Generated pairwise outputs:
  - `results/pairwise_design_memo_eval.csv`
  - `results/pairwise_design_memo_eval.md`

### Pairwise Protocol

- subset: all `10` main-set `level2` cases
- comparison unit: matched anonymized **design memos**, not full papers
- fixed judge model: `deepseek-v4-pro`
- A/B order: deterministic per-case randomization from hashed `case_id`

### Pairwise Outcome

- final pairwise result:
  - agent loses to published design memo: `0/10`
  - agent wins: `10/10`
  - ties: `0/10`
- dimension-level counts:
  - identification winner = published memo in `0/10`
  - mechanism winner = published memo in `1/10`
  - defensibility winner = published memo in `0/10`

### Interpretation Of Pairwise Outcome

- This result conflicts sharply with the benchmark's main claim-level adjudication and failure-case analysis.
- Therefore the pairwise layer should **not** be treated as headline evidence.
- The most plausible explanation is protocol sensitivity:
  - memo compression changes the informational balance between published-design summaries and agent outputs
  - the fixed judge appears to reward explicit assumptions, bounds, and caution language in the agent memo
  - the current pairwise layer also uses a same-family judge relative to the benchmarked model family
- The repository therefore retains this layer as an **exploratory extension artifact**, not as a primary benchmark result.

### Additional Planning Work

- Added follow-on strengthening tasks to `project_todo/tasks/`:
  - `27_reframe_project_with_bottleneck.md`
  - `28_build_bottleneck_execution_crosswalk.md`
  - `29_run_pairwise_design_memo_evaluation.md`
  - `30_test_design_critic_intervention_on_perturbed.md`
  - `31_quantify_threat_recognition_for_rq1.md`
  - `32_expand_no_solution_to_full_main_set.md`
- Updated `project_todo/README.md` so that post-main-run strengthening work now has a dedicated phase.

### Current Status

- `task27`: complete
- `task28`: complete
- `task29`: complete as an exploratory extension
- Historical status as of this entry: `task30-32` not started

### Current Recommendation

- Treat the benchmark's main evidence as:
  - adjudicated claim-level metrics
  - information gradient
  - paired perturbed audit
  - failure-case analysis
- Treat the pairwise design-memo layer as:
  - a successfully implemented APE-style extension
  - but currently too protocol-sensitive to serve as a main result without further judge diversification or memo redesign

## 2026-05-31

### Stage

Work moved from post-benchmark framing extensions into the first actual intervention experiment.

The goal was to turn `task30` from a planning document into a runnable and auditable perturbation-repair study, while keeping the frozen baseline benchmark intact.

### Task 30: research_agent_v1 Intervention Infrastructure

- Added a new external-orchestration intervention arm:
  - `research_agent_v1`
- This arm reuses the existing `benchmark_isolated` single-packet runner, but inserts a 3-stage loop:
  - `Stage 3`: candidate design generation
  - `Stage 4`: independent critique
  - `Stage 5`: final reconcile memo

### New Prompt And Runner Assets

- Added prompt templates:
  - `benchmark/prompts/research_agent_v1/stage3_candidates.md`
  - `benchmark/prompts/research_agent_v1/stage4_critique.md`
  - `benchmark/prompts/research_agent_v1/stage5_final.md`
- Added orchestration and bridge scripts:
  - `scripts/run_research_agent_v1.py`
  - `scripts/postprocess_research_agent_v1_run.py`
  - `scripts/run_research_agent_v1_batch.sh`
- Added batch spec:
  - `benchmark/run_configs/perturbed_intervention_batch_spec.csv`

### Evaluation-Chain Prep And Schema Extension

- Extended the postprocessing and scoring pipeline to carry an explicit `agent_variant` field end-to-end.
- Updated:
  - `scripts/postprocess_openclaw_run.py`
  - `scripts/extract_agent_claims.py`
  - `scripts/build_first_pass_annotations.py`
  - `scripts/build_second_labels_and_adjudication.py`
  - `scripts/compute_benchmark_metrics.py`
  - `scripts/build_perturbed_pair_audit.py`
- Added one-off manifest backfill utility:
  - `scripts/backfill_manifest_agent_variant.py`
- Result:
  - baseline rows remain `benchmark_isolated`
  - intervention rows can now be tracked as `research_agent_v1`
  - arm-specific metrics can be emitted without overwriting canonical benchmark outputs

### Smoke Test And Formal Batch

- Completed a successful single-case smoke test on:
  - `C001_perturbed`
- Then ran the full `10`-case perturbed intervention batch for:
  - `C001`
  - `C002`
  - `C004`
  - `C005`
  - `C008`
  - `C010`
  - `C014`
  - `C016`
  - `C019`
  - `C020`
- The formal manifest now contains:
  - `10` successful `research_agent_v1` main rows
- The provisional smoke-only bridged `C001` row was removed before final downstream analysis to avoid duplicate counting.

### New Task 30 Artifacts

- Multi-stage raw runs:
  - `outputs/raw_agent_logs/research_agent_v1/`
- Formal bridged main raw logs:
  - `outputs/raw_agent_logs/main/*__research_agent_v1__*.md`
- New intervention-specific results:
  - `results/perturbed_mechanical_reuse_v1.csv`
  - `results/perturbed_pair_audit_v1.md`
  - `results/metrics_summary_research_agent_v1.csv`
  - `results/metrics_summary_research_agent_v1.md`
  - `results/research_agent_v1_vs_baseline.md`

### H1 Outcome

- Baseline paired perturbed audit:
  - mechanical reuse = `9/10`
- `research_agent_v1` paired perturbed audit:
  - mechanical reuse = `2/10`
- Case-level transition:
  - improved from `yes -> no` on `C001`, `C002`, `C004`, `C010`, `C014`, `C016`, `C020`
  - remained `yes` on `C005`, `C008`
  - remained `no` on `C019`

### Interpretation Of Task 30 Result

- The critic-and-reconcile loop substantially reduced broken-identification mechanical reuse on the perturbed subset.
- The intervention appears to work mainly by forcing explicit downgrade to:
  - descriptive analyses
  - bounded claims
  - retargeted weaker estimands
- Residual failures are concentrated where the final memo still preserves a secondary causal candidate from the base design:
  - `C005`: supplementary actual-exposure `IV/LATE`
  - `C008`: secondary within-store `DiD` plus salience-gradient logic

### Plan-vs-Implementation Note

- `research_agent_v1` should be read as the implemented `v1` arm from `report/research_agent_redesign_plan.md`, not as a verbatim reproduction of every engineering detail in that document.
- What matched the plan:
  - the `10`-case `perturbed`-only scope
  - the `Stage 3 -> Stage 4 -> Stage 5` candidate / critique / reconcile loop
  - the H1 evaluation logic centered on paired `mechanical reuse`
- What was simplified in implementation:
  - the run reused the existing `benchmark_isolated` OpenClaw configuration rather than creating separate `benchmark_research_agent` and `benchmark_design_critic` base agents
  - role separation was implemented through stage-specific prompts plus an external orchestrator, not through two distinct underlying agent configs
- What was explicitly not part of this run:
  - `v2` literature-scan retrieval
  - `v3` planner or multi-round debate
- Actual tool use remained `none` across the official `10`-case batch, so the result should be interpreted as a critic-augmented packet-grounded intervention, not as a retrieval-heavy research-agent result.

### Annotation And Metrics Caveat

- The intervention arm now cleanly enters the shared extraction / annotation / adjudication / metrics chain.
- However, the existing claim-level override system was originally calibrated to frozen baseline run IDs.
- Therefore:
  - the manual paired perturbed audit is the primary evidence source for `task30`
  - `results/metrics_summary_research_agent_v1.csv` is structurally correct and its `Perturbed Mechanical Reuse Rate = 0.2` is usable
  - other intervention claim-level headline values should still be treated as provisional until run-specific override coverage is expanded for `research_agent_v1`

### Bug Fix During Task 30

- A real regression surfaced during downstream processing:
  - adding a new arm caused `build_second_labels_and_adjudication.py` to resample and rewrite frozen baseline second-pass / adjudication outputs
- Fixed by preserving existing variant-level adjudication artifacts when the claim set for that variant is unchanged.
- This restored the frozen baseline canonical metrics:
  - `Mean Claim Score = 0.8014`
  - `Design-Evidence Inconsistency Rate = 0.2676`
  - `Overclaim Rate = 0.1378`
  - `Unsupported Design Claim Rate = 0.1108`
  - `Perturbed Mechanical Reuse Rate = 0.9`

### Validation

- Added and passed regression coverage for the new arm-aware pipeline:
  - `tests/test_agent_variant_pipeline.py`
  - `tests/test_research_agent_v1_smoke.py`
  - `tests/test_research_agent_v1_postprocess.py`
- Verified:
  - `python3 -m unittest tests/test_agent_variant_pipeline.py tests/test_research_agent_v1_smoke.py tests/test_research_agent_v1_postprocess.py`
  - `git diff --check`

### Task 31: Threat-Recognition Audit For RQ1

- Implemented a lightweight quantitative threat-recognition audit on the frozen baseline `level2` outputs only.
- Scope:
  - `10` main-set `level2` runs
  - `2` pre-defined threats per case
  - no `level3` runs
  - no `research_agent_v1` intervention rows in this pass
- Added:
  - `scripts/build_threat_recognition_audit.py`
  - `results/threat_recognition_audit.csv`
  - `results/threat_recognition_summary.md`
  - `docs/superpowers/specs/2026-05-31-task31-threat-recognition-design.md`
  - `tests/test_threat_recognition_audit.py`

### Threat-Recognition Counting Rule

- A threat counts as a hit only if:
  - the `level2` output explicitly identifies the threat
  - and the output gives a concrete design response, assumption, limitation, or non-claim that addresses it
- Mere generic caution language does not count.

### Threat-Recognition Outcome

- average threat hits per case: `1.9/2`
- overall threat hit rate: `19/20 = 95.0%`
- case distribution:
  - `9/10` cases scored `2/2`
  - `1/10` case scored `1/2`
  - `0/10` cases scored `0/2`
- the single partial-recognition miss is:
  - `C005`
    - the output correctly recognizes endogenous actual exposure
    - but does not recover the benchmark's narrower requirement of a comparable exposure-opportunity control group

### Interpretation Of Task 31 Result

- On baseline `level2`, the agent usually recognizes the benchmark's core threats.
- This means the project's main weakness is not simple threat blindness at `level2`.
- Instead, the dominant residual problems are more often:
  - packet overreach
  - overclaiming
  - mechanism over-interpretation
  - failure to keep later claims aligned with already-recognized threat structure
- This also helps interpret `task30`:
  - the critic intervention improves downstream design discipline under perturbation
  - but the baseline already recognized many `level2` threats before that intervention

### Current Status

- `task30`: intervention infrastructure complete
- `task30`: 10-case perturbed batch complete
- `task30`: H1 paired audit complete
- `task30`: write-up artifact complete
- `task31`: complete
- `task32`: not started
- `task33-38`: planned as the next `research_agent_redesign_plan.md` execution branch

### Next-Phase Task Scaffolding

- Added a new fine-grained v2 / v3 task breakdown under `project_todo/tasks/`:
  - `task33`: build v2 retrieval stage and search gate
  - `task34`: run v2 retrieval-augmented `10`-case `perturbed` batch
  - `task35`: analyze v2 vs v1 retrieval effect
  - `task36`: build v3 planner and debate loop
  - `task37`: run v3 planner-debate `10`-case `perturbed` batch
  - `task38`: summarize v3 vs v1/v2 ablation
- Updated `project_todo/README.md` so the execution order now treats:
  - `task33 -> 34 -> 35` as the v2 branch
  - `task36 -> 37 -> 38` as the v3 branch
- `task32` remains a separate `no_solution` coverage extension and is intentionally not bundled into the v2 / v3 ablation path.

### Task 33: OpenAlex-First Retrieval Gate Work Started

- Began `task33` implementation for `research_agent_v2`.
- Added:
  - `scripts/run_research_agent_v2.py`
  - `scripts/postprocess_research_agent_v2_run.py`
  - `benchmark/prompts/research_agent_v2/`
  - `tests/test_research_agent_v2_smoke.py`
  - `docs/superpowers/plans/2026-06-01-task33-v2-retrieval-stage-implementation.md`
- Fixed the v2 runner so that:
  - OpenAlex is queried runner-side via `OPENALEX_API_KEY` and `OPENALEX_EMAIL`
  - the resulting `openalex_seed.json` is saved under `stage2_retrieval/`
  - `Stage 2` is marked `invalid` when `actual tool calls = 0`
  - invalid runs still preserve `artifact.json`, `evidence_summary.md`, `raw_openclaw.json`, and `stderr.log` for audit
- Updated `task33` spec to reflect the intended retrieval stack:
  - primary scholarly graph: `OpenAlex`
  - economics-first layer: `RePEc/IDEAS`
  - supplemental layer: `NBER/SSRN`
  - current live fallback: `deepxiv` and `web_search`
- Added local credential persistence for runner-side OpenAlex access:
  - `.benchmark.local.env` is now the default local credential file
  - `.benchmark.local.env.example` documents the expected format
  - `run_research_agent_v2.py` auto-loads this file on each run if `OPENALEX_API_KEY` / `OPENALEX_EMAIL` are not already present in the shell environment
  - `.benchmark.local.env` is git-ignored and should remain local-only

### Task 33 Smoke Outcome So Far

- Verified runner-side OpenAlex access works:
  - `openalex_seed.json` is generated successfully for `C001_perturbed`
  - current query shape still needs refinement, but the API path is live
- Verified `deepxiv` is available in the OpenClaw tool stack during the smoke run
- Ran two early `C001_perturbed` v2 smoke tests before the counter fix.
- Both runs failed at the same gate:
  - `Stage 2 is invalid: no actual retrieval tool call was recorded.`
- In both runs:
  - `toolMetas = null`
  - `messages = []`
  - `tool_calls = 0`
  - `tool_results = 0`
- The model still fabricated retrieval artifacts claiming use of:
  - `deepxiv`
  - `semantic-scholar`
  - `web_search`
  despite leaving no actual tool-call trace

### Interpretation Of Current Task 33 State

- The OpenAlex integration path is now working at the runner layer.
- The remaining failure is no longer about unavailable scholarly context.
- The remaining blocker is agent behavior:
  - even with a mandatory first-query instruction and an explicit real-tool-call requirement, the current OpenClaw trajectory still chooses to emit a fabricated retrieval summary instead of executing a live tool call
- Therefore `task33` is **in progress**, not complete.
- The next likely repair direction is to add a stronger execution constraint than prompt-only gating, such as:
  - a tool-preflight step outside the model
  - or a stricter no-answer-before-tool-call protocol if the platform supports it

## 2026-06-01

### Stage

OpenClaw "cannot call tools" investigation. Root-caused the Task 33 search-gate failure and corrected the prior misdiagnosis.

### Trigger

- Reported symptom: OpenClaw in this project "keeps failing to call tools".
- The `2026-05-31` Task 33 entry concluded the blocker was **agent behavior** (the model allegedly fabricating retrieval instead of calling tools).
- This conclusion was **wrong** and is corrected below.

### Root Cause

- The failure was a parser bug in `scripts/run_research_agent_v2.py`, not OpenClaw and not model behavior.
- `extract_tool_call_counts()` read tool activity from `data["messages"]` and `meta["toolMetas"]`.
- Current OpenClaw (`2026.5.5`) `openclaw agent --local --json` output contains neither:
  - top-level keys are only `payloads` and `meta`
  - there is no `messages` array
  - `meta.toolMetas` is empty even when tools were called
- Actual tool calls are recorded only in the session transcript at `meta.agentMeta.sessionFile`:
  - assistant messages carry `content` blocks of `type: "toolCall"`
  - tool outputs are separate messages with `role: "toolResult"`
- Therefore `extract_tool_call_counts()` always returned `0`, which made the gate (`tool_calls == 0`) mark `Stage 2` invalid and made `normalize_stage2_artifact()` overwrite the model's truthful `retrieval_successful` to `False` with `failure_reason="no_actual_tool_use_recorded"`.

### Evidence

- The initial real `C001_perturbed` run recorded `retrieval_tool_calls: 0` in its manifest even though the session transcript showed live tool use.
- Its session transcript actually contained `20` tool calls:
  - `web_search` x15, `web_fetch` x3, `semantic-scholar__search_papers` x1, `semantic-scholar__get_paper_details` x1
- The stage artifact even self-reported `tool_attempt_count: 12`, `tool_success_count: 10`.
- `systemPromptReport.tools.entries` confirmed all tools (`web_search`, `web_fetch`, `deepxiv__*`, `semantic-scholar__*`) were registered and sent as native function schemas (`schemaChars: 6359`).
- Two isolated control probes (`--thinking off` and `--thinking high`, identical forcing prompt) both produced real `toolCall` blocks, ruling out a thinking-level or capability cause.

### Fix — What Was Changed

- File: `scripts/run_research_agent_v2.py`
- Function: `extract_tool_call_counts()` (only this function changed; added one helper).

**Why it was wrong:** the old version counted from `data["messages"]` and `meta["toolMetas"]`, neither of which exists/populates in OpenClaw `2026.5.5` `--json` output, so it always returned `0`.

Before (broken — reads fields the `--json` payload does not contain):

```python
def extract_tool_call_counts(data: dict) -> dict[str, int]:
    tool_calls = 0
    tool_results = 0
    for entry in data.get("messages") or []:          # <- no "messages" key in --json
        ...
    tool_metas = (data.get("meta") or {}).get("toolMetas") or []   # <- always empty
    if tool_calls == 0 and tool_metas:
        tool_calls = len(tool_metas)
    return {"tool_calls": tool_calls, "tool_results": tool_results}
```

After (fixed — counts from the session transcript, which is the source of truth):

```python
def count_tool_calls_from_session(session_file: Path) -> dict[str, int]:
    # assistant messages carry content blocks of type "toolCall";
    # tool outputs are separate messages with role "toolResult".
    ...

def extract_tool_call_counts(data: dict) -> dict[str, int]:
    meta = data.get("meta") or {}
    session_file = (meta.get("agentMeta") or {}).get("sessionFile")
    if session_file and Path(session_file).exists():
        return count_tool_calls_from_session(Path(session_file))   # <- new primary path
    # ... old messages/toolMetas logic retained only as fallback ...
```

- Net effect: tool calls are now read from `meta.agentMeta.sessionFile` (`toolCall` blocks + `toolResult` messages); the old logic stays only as a fallback for other `--json` schemas.
- No other pipeline stage, prompt, or schema was modified.

### Fix Verification (replay, no new API call)

- Re-ran the patched counter against the original pre-fix `C001_perturbed` run:
  - `extract_tool_call_counts -> {'tool_calls': 20, 'tool_results': 19}`
  - the gate no longer fails (`tool_calls == 0` is now `False`)
  - on fresh model values, `normalize_stage2_artifact` keeps `retrieval_successful=True` and `failure_reason=None`
- `python3 -m py_compile scripts/run_research_agent_v2.py` passed.

### Re-run Verification (fresh C001 perturbed run)

- Re-ran the full pipeline on `benchmark/cases/C001_charitable_giving/agent_task_perturbed.md`.
- A fresh post-fix validation run then passed the Stage 2 gate and completed the full pipeline.
- `stage2_retrieval` now passes the gate:
  - `status: ok`
  - `retrieval_attempted: true`
  - `retrieval_successful: true`
  - `retrieval_tool_calls: 12`
  - no `no_actual_tool_use_recorded` failure_reason
- Actual tool use in the new stage 2 session (`12` calls / `12` results):
  - `web_search` x6 (live web search)
  - `deepxiv__search_papers` x5 (literature retrieval MCP)
  - `web_fetch` x1
- Full pipeline completed: `pipeline_failed: false`, all four stages `ok`, `stage5_final` recorded `retrieval_successful=True`, `recommend_descriptive_fallback=False`.
- Conclusion: with the counter fixed, the same case that previously hard-failed at the gate now correctly registers live tool use and web search, and the pipeline runs to completion.

### Secondary Findings (not the main blocker)

- `web_fetch` to `news.ycombinator.com` hit the 30s SSRF-guard timeout in the isolated probes; when a tool fails, `deepseek-v4-pro` tends to fabricate a plausible result instead of reporting the failure. This is a benchmark-integrity risk to watch.
- Non-fatal config warnings: `bundle-mcp` is an invalid allowlist entry; `plugins.allow` is empty so `qqbot`/`openclaw-weixin` auto-load; skills symlink-escape warnings for `.orchestra`/`.codex` paths.
- `~/.openclaw/openclaw.json` stores secrets (tavily key, gateway token, qqbot clientSecret) in plaintext; do not share or commit that file.

### Corrected Interpretation Of Task 33

- The earlier "agent fabricates retrieval instead of calling tools" reading was an artifact of the broken counter.
- The model does perform live retrieval; the pipeline simply failed to see it.
- `task33` should be re-evaluated with the fixed gate before adding any heavier no-answer-before-tool-call constraint.

### Task 33 Completion After Counter Fix

- Re-ran the full `C001_perturbed` v2 smoke test after the counter repair.
- Final outcome:
  - all four stages `ok`
  - `pipeline_failed: false`
  - `stage2_retrieval.retrieval_tool_calls = 15`
  - `stage2_retrieval.retrieval_successful = true`
- This confirms the original `invalid` outcome was a false negative produced by the broken tool counter.

### Postprocess Chain Correction

- Fixed `scripts/postprocess_openclaw_run.py` so that:
  - `sessionFile` is the primary truth source for both tool counts and tool names
  - trajectory `toolMetas` is now only a fallback
- Fixed `scripts/postprocess_research_agent_v2_run.py` so that:
  - formal v2 raw logs summarize **pipeline-level** tool use, not just the `stage5_final` session
- Re-bridged the successful smoke run:
  - run id: `RUN_20260601_TASK33_SMOKE_FIX`
  - raw log: `outputs/raw_agent_logs/main/C001_perturbed__research_agent_v2_search__RUN_20260601_TASK33_SMOKE_FIX.md`
- Correct formal tool summary now records:
  - `actual_tool_use = deepxiv__search_papers,web_search,deepxiv__get_paper_brief`
  - contamination note also reflects the same pipeline-level tool use

### Task 33 Status

- `task33` is now complete.
- The next executable step in the redesign branch is:
  - `task34`: run the v2 retrieval-augmented 10-case `perturbed` batch

## 2026-06-01 - Task 34 v2 Batch Completion

### Batch Completion

- Completed the formal `research_agent_v2_search` `10`-case `perturbed` batch with the same case set as `research_agent_v1`:
  - `C001`, `C002`, `C004`, `C005`, `C008`, `C010`, `C014`, `C016`, `C019`, `C020`
- Batch spec:
  - `benchmark/run_configs/perturbed_retrieval_v2_batch_spec.csv`
- Batch runner:
  - `scripts/run_research_agent_v2_batch.sh`
- Multi-stage artifacts:
  - `outputs/raw_agent_logs/research_agent_v2/`
- Formal bridged outputs:
  - `outputs/raw_agent_logs/main/*__research_agent_v2_search__*.md`

### Manifest / Retrieval Metadata

- `outputs/run_manifest.csv` now contains `10` success rows for `research_agent_v2_search`.
- All `10` rows record retrieval metadata:
  - `retrieval_attempted = true`
  - `retrieval_successful = true`
  - `retrieval_tool_calls > 0`
- Recorded retrieval tool-call counts across the `10` runs:
  - `10, 15, 17, 19, 24, 14, 19, 17, 18, 14`
- Non-fatal retrieval notes remain in `retrieval_failure_reason` for some rows where `semantic-scholar` hit rate limits but `deepxiv` / `web_search` still provided enough coverage.

### Downstream Chain

- Re-ran the v2 downstream chain after the batch:
  - `scripts/extract_agent_claims.py`
  - `scripts/build_first_pass_annotations.py`
  - `scripts/build_second_labels_and_adjudication.py`
  - `scripts/compute_benchmark_metrics.py`
- v2 is now present in:
  - `outputs/parsed_claims/claims_to_annotate.csv`
  - `annotations/annotation_sheet.csv`
  - `annotations/second_labels.csv`
  - `annotations/adjudicated_labels.csv`
- Generated arm-specific metrics outputs:
  - `results/metrics_summary_research_agent_v2_search.csv`
  - `results/metrics_summary_research_agent_v2_search.md`

### Downstream Debug Note

- A transient false failure appeared while re-running downstream because `build_first_pass_annotations.py` and `build_second_labels_and_adjudication.py` were accidentally launched in parallel during a quick verification pass.
- Symptom:
  - `second_labels.csv` and `adjudicated_labels.csv` temporarily collapsed to a truncated `52`-row baseline-only state.
- Root cause:
  - `build_second_labels_and_adjudication.py` read `annotations/annotation_sheet.csv` while `build_first_pass_annotations.py` was still rewriting it.
- Resolution:
  - Re-ran the downstream chain in the correct sequential order.
- Final state is now consistent.

### Interpretation Boundary

- `task34` proves that the v2 retrieval-augmented arm now runs end-to-end at batch scale and writes retrieval-aware formal outputs into the benchmark chain.
- `task34` does **not** by itself establish that retrieval improved performance relative to `v1`.
- That comparison belongs to `task35`.

## 2026-06-01 - Task 35 v2 vs v1 Retrieval Effect

### Paired Audit Completion

- Completed the paired manual `perturbed` audit for `research_agent_v2_search`.
- Generated:
  - `results/perturbed_mechanical_reuse_v2.csv`
  - `results/perturbed_pair_audit_v2.md`
- Headline:
  - `research_agent_v1` mechanical reuse: `2/10`
  - `research_agent_v2_search` mechanical reuse: `0/10`
- Interpretation:
  - adding the explicit retrieval stage removed the last two residual reuse cases left in `v1`

### Where v2 Actually Improves

- The incremental gain is concentrated in:
  - `C005`
    - `v1` still preserved a supplementary exposure-level `LATE`
    - `v2` rejects exposure-level identification and keeps only assignment-level `ITT` plus predictive `PIE`
  - `C008`
    - `v1` still preserved a secondary within-store comparison / salience-gradient rescue
    - `v2` drops that rescue entirely and keeps only descriptive demand-reallocation analysis
- Other cases mostly preserve the same broad downgrade direction as `v1`, but often with stronger methodological backing.

### Retrieval Usefulness Audit

- Generated:
  - `results/retrieval_usefulness_audit.csv`
  - `results/retrieval_usefulness_summary.md`
- Retrieval behavior:
  - attempted: `10/10`
  - successful: `10/10`
  - zero-tool-use runs: `0/10`
  - mean recorded retrieval tool calls: `16.7`
- Usefulness labels:
  - `helpful`: `6/10`
  - `neutral`: `3/10`
  - `noisy`: `1/10`
  - `failed`: `0/10`
- The most clearly helpful retrieval cases are:
  - `C002`
  - `C004`
  - `C005`
  - `C008`
  - `C014`
  - `C016`
- `C020` is the clearest noisy case:
  - retrieval still lands on the right bundle-only estimand
  - but one rate-limit event and one off-target deepxiv result added search noise

### Comparison Write-up

- Generated:
  - `results/research_agent_v2_vs_v1.md`
- Main reading:
  - `v2` is not just `v1` plus tool exposure
  - it produces real retrieval and removes the last residual `mechanical_reuse` failures on the `perturbed` subset
  - however, the benefit is concentrated rather than uniform

### Metrics Caveat

- Re-ran `scripts/compute_benchmark_metrics.py` after wiring `research_agent_v2_search` to the correct paired-audit file.
- `results/metrics_summary_research_agent_v2_search.csv` now carries the correct `Perturbed Mechanical Reuse Rate = 0/10`.
- The broader claim-level headline metrics for `v2` remain provisional, just as for `v1`; do not use `Mean Claim Score = 1.0` as the primary intervention result.

### Task 35 Conclusion

- Recommendation: `go to v3`, but only as a clean optional ablation.
- Reason:
  - `v2` already fixes the `perturbed mechanical reuse` problem on this subset
  - the rationale for `v3` is now "test whether planner/debate adds anything beyond critic + retrieval"
  - the rationale is **not** "v2 is still broken and needs rescue"

## 2026-06-01 - Task 36 v3 Planner/Debate Smoke

### Implementation Scope

- Implemented `task36` strictly as a smoke-only `v3` build:
  - no formal bridge
  - no `outputs/run_manifest.csv` writes
  - no `outputs/raw_agent_logs/main/` writes
- Added:
  - `benchmark/prompts/research_agent_v3/stage0_planner.md`
  - `benchmark/prompts/research_agent_v3/stage2_retrieval.md`
  - `benchmark/prompts/research_agent_v3/stage3_candidates.md`
  - `benchmark/prompts/research_agent_v3/stage4_critique.md`
  - `benchmark/prompts/research_agent_v3/stage3b_response.md`
  - `benchmark/prompts/research_agent_v3/stage4b_critique.md`
  - `benchmark/prompts/research_agent_v3/stage5_final.md`
  - `scripts/run_research_agent_v3.py`
  - `tests/test_research_agent_v3_smoke.py`
- `run_research_agent_v3.py` is intentionally a thin wrapper around the `v2` runner utilities rather than a forked copy of the retrieval/tool-count stack.

### Tool-Use And Retrieval Lessons Preserved

- Reused the corrected `sessionFile`-based tool accounting from `task33`.
- Kept `OpenAlex` as runner-side seed generation rather than as a live OpenClaw tool dependency.
- Kept `deepxiv` / `web_search` as the preferred live retrieval path.
- Kept `semantic-scholar` optional rather than required, because stable `v2` behavior already showed that `deepxiv` is the reliable scholarly retrieval layer.

### Smoke Result

- Ran a real single-case smoke on:
  - `benchmark/cases/C005_online_ad_measurement/agent_task_perturbed.md`
- Output directory:
  - `outputs/raw_agent_logs/research_agent_v3/C005_perturbed_20260601_173508`
- Manifest summary:
  - `planner_present = true`
  - `retrieval_attempted = true`
  - `retrieval_successful = true`
  - `retrieval_tool_calls = 21`
  - `debate_rounds_run = 1`
  - `stop_rule_triggered_by = fixed_single_round_smoke_rule`
  - all stages `ok`
- New debate artifacts were produced and parsed successfully:
  - `stage3b_response/artifact.json`
  - `stage4b_critique/artifact.md`
  - `stage4b_critique/artifact.meta.json`
- `stage5_final/artifact.md` passed the canonical claim-evidence table check.

### Interpretation Boundary

- `task36` proves that the planner/debate state machine is now operational and auditable under the smoke-only boundary.
- `task36` does **not** establish that `v3` improves over `v2`.
- That comparison belongs to `task37-38`.

## 2026-06-02 - Task 37 v3 Planner/Debate Formal Batch

### Batch Completion

- Completed a clean full rerun of `research_agent_v3_planner_debate` on the shared `10`-case `perturbed` set.
- Formal `v3` rows in `outputs/run_manifest.csv` now total `10`, all `success`.
- Formal raw logs now total `10` under:
  - `outputs/raw_agent_logs/main/*__research_agent_v3_planner_debate__*.md`
- Pipeline directories now total `10` under:
  - `outputs/raw_agent_logs/research_agent_v3/`

### Retrieval Metadata

- All `10` formal `v3` rows record:
  - `retrieval_attempted = true`
  - `retrieval_successful = true`
  - `retrieval_tool_calls > 0`
- Retrieval tool-call counts by case:
  - `C001 = 14`
  - `C002 = 24`
  - `C004 = 9`
  - `C005 = 21`
  - `C008 = 19`
  - `C010 = 20`
  - `C014 = 17`
  - `C016 = 18`
  - `C019 = 19`
  - `C020 = 36`

### Downstream Chain

- Re-ran the downstream chain sequentially to avoid CSV read/write races:
  - `scripts/extract_agent_claims.py`
  - `scripts/build_first_pass_annotations.py`
  - `scripts/build_second_labels_and_adjudication.py`
  - `scripts/compute_benchmark_metrics.py`
- `research_agent_v3_planner_debate` is now present in:
  - `outputs/parsed_claims/claims_to_annotate.csv`
  - `annotations/annotation_sheet.csv`
  - `annotations/adjudicated_labels.csv`
- Current row counts for `research_agent_v3_planner_debate`:
  - claims-to-annotate: `79`
  - annotation-sheet: `79`
  - adjudicated-labels: `79`
- Generated arm-specific metrics summary:
  - `results/metrics_summary_research_agent_v3_planner_debate.csv`
  - `results/metrics_summary_research_agent_v3_planner_debate.md`

### Interpretation Boundary

- `task37` establishes that the `v3` planner/debate arm is now a formal, repeatable benchmark condition rather than a smoke-only pipeline.
- `task37` does **not** yet establish that `v3` improves over `v2`.
- As with `v1` and `v2`, the current claim-level headline metrics for `v3` should be treated as provisional.
- The main `v3 vs v1/v2` interpretation should remain scoped to `task38`.

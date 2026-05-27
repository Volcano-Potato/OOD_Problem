# Pilot Review

## Scope

This review records the isolated rerun of the 5 Level 2 pilot cases executed on `2026-05-25` under the local OpenClaw `benchmark_isolated` agent with `thinking=high`, `timeout=86400`, reusable out-of-repo workspace isolation, and explicit fresh sessions. The first, older pilot batch remains useful as a precursor, but the current benchmark judgment should rely on this isolated rerun.

## Run Summary

| case_id | run_id | output contract | claim-evidence table | actual tool use | contamination status | quick judgment |
|---|---|---|---|---|---|---|
| C001 | `RUN_20260525_183040_openclaw_deepseekv4pro_isolated` | pass | pass | none | suspected | still reconstructs a specific opt-out / pre-visit implementation not stated in the packet |
| C002 | `RUN_20260525_183518_openclaw_deepseekv4pro_isolated` | fail | pass | none | suspected | still instantiates a highly specific two-stage design and also violates the full-English output contract |
| C005 | `RUN_20260525_183846_openclaw_deepseekv4pro_isolated` | pass | pass | none | clean | substantially improved; no ghost-auction reconstruction, no actual retrieval use |
| C008 | `RUN_20260525_184335_openclaw_deepseekv4pro_isolated` | pass | pass | none | clean | substantially improved; primary design stays within packet support, triple-difference only appears as conditional robustness |
| C014 | `RUN_20260525_184805_openclaw_deepseekv4pro_isolated` | pass | pass | none | clean | substantially improved; identification remains grounded in independent outcome measurement rather than source reconstruction |

## High-Level Findings

1. The local-file-isolated rerun removed the main environment ambiguity from the first pilot batch. All 5 reruns completed successfully, and the session trajectories show `toolMetas = []` for every run.
2. Packet-overreach did not disappear under isolation. `C001` and `C002` still over-specified packet-absent design details even though no tools were actually used. This is now much stronger evidence that the failure mode is agent behavior rather than local hidden-file leakage.
3. The anti-reconstruction wording helped materially on `C005`, `C008`, and `C014`. Those three cases are now provisionally usable as `clean` pilot evidence under the current Level 2 schema.
4. Output-contract obedience is still not fully stable. `C002` returned a fully Chinese response, including Chinese section titles and a Chinese claim-evidence table, despite the benchmark's all-English requirement.
5. Runtime noise remains. During `C005` and `C008`, `semantic-scholar` MCP again produced startup-timeout noise during bundle-tool preparation, although the runs still completed and did not actually call retrieval tools.

## Pilot Issue Table

| issue_id | case_id | issue_type | problem | fix | rerun_needed |
|---|---|---|---|---|---|
| P001 | C001 | packet-overreach | The report still introduced concrete opt-out and pre-visit implementation details not stated in the packet. | Further harden C001 packet wording around pre-contact communication and avoidance-cost manipulation. | yes |
| P002 | C002 | packet-overreach + output-contract failure | The report still instantiated a highly specific post-acceptance randomization design and also violated the all-English output contract. | Tighten C002 packet wording around later-term variation and strengthen the English-only instruction in the output contract or runner prompt. | yes |
| P006 | all | runtime / tooling | `semantic-scholar` MCP still creates startup-timeout noise in isolated runs. | Disable `semantic-scholar` for benchmark execution or treat it as optional non-benchmark tooling. | no |
| P007 | all | logging hygiene | Actual tool use can now be recovered cleanly from trajectories, but the ad hoc raw-log writer still produced noisy inline `none` summaries in some files. | Clean the log-summary extraction in the runner before a larger main run. | no |

## Resolved Relative to the First Pilot Batch

- `P003 / C005`: resolved enough for pilot purposes. The rerun no longer reconstructed ghost-auction machinery or other source-like delivery instrumentation.
- `P004 / C008`: largely resolved. The rerun still uses modern panel-event-study language, but triple-difference appears only as a conditional robustness extension rather than as an unsupported primary design fact.
- `P005 / C014`: largely resolved. The rerun no longer inserts unsupported audit-probability magnitudes and keeps the design centered on independent measurement.
- `P008 / all`: resolved. The isolated rerun removed the earlier ambiguity between content failures and local-file leakage risk.

## Quick Rerun Spot-Check

- `C001`: still unsupported on operational specificity. The packet supports varying interaction cost before contact, not a specific opt-out solicitation implementation.
- `C002`: still unsupported on the exact post-acceptance randomization design, and now also fails a benchmark-level format rule by returning Chinese rather than English.
- `C005`: now mostly packet-grounded. The strongest defensible estimand is campaign-assignment ITT, with actual-exposure LATE clearly marked as secondary and assumption-dependent.
- `C008`: now much closer to acceptable. The core salience design is grounded in repeated treated/control category comparisons with explicit price controls.
- `C014`: now much closer to acceptable. The design correctly treats independent post-completion measurement as part of identification, not just better measurement.

Detailed quick-claim rows for the isolated rerun were appended to `annotations/annotation_sheet.csv`.

## Decision

Do **not** proceed to Task 18 yet.

The isolated rerun resolved the biggest environment-validity concern and showed that 3 of the 5 Level 2 pilot cases are now in reasonable shape. But `C001` and `C002` still need targeted revision before the benchmark should be treated as schema-stable. The next step is not another full-batch rerun; it is a narrow repair pass on those two cases, followed by one focused verification rerun.

## Focused Verification Rerun

After freezing `benchmark_isolated` as the canonical locally isolated, remote-tool-enabled runtime, both remaining problematic cases were rerun again under the same single-packet pipeline.

| case_id | run_id | actual tool use | contamination status | quick judgment |
|---|---|---|---|---|
| C001 | `RUN_20260525_213551_openclaw_deepseekv4pro_isolated` | none | suspected | improved wording, but still hard-codes an explicit opt-out/easy-avoidance arm and a doorstep baseline beyond packet support |
| C002 | `RUN_20260525_214053_openclaw_deepseekv4pro_isolated` | none | suspected | English-only contract is now satisfied, but the report still asserts a hidden post-acceptance two-stage design as if it were established by the packet |

Focused rerun takeaways:

- `C001` improved from "source-like direct reconstruction" to "still too concrete in its illustrative arm definitions," but it is not yet safely `clean`.
- `C002` no longer fails the language contract, so the remaining problem is now concentrated on packet overreach rather than formatting.
- Both reruns again showed `toolMetas = []`, so the residual issue is still best interpreted as agent behavior under the packet, not local hidden-file leakage.

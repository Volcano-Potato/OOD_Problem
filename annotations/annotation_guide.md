# Annotation Guide

## Purpose

This guide defines the first-pass human labeling protocol for claim-level evaluation in the OOD Causal Design Benchmark. The goal is to judge whether each extracted claim is warranted by:

1. the agent-facing task packet,
2. the case-specific `gold_reference.md`, and
3. the relevant variant note when the run is `perturbed` or `no_solution`.

The annotation target is not prose quality. It is whether the agent's design claim is evidence-consistent and strength-calibrated.

## Inputs Required Per Claim

For each claim, the annotator should read:

- the row in `outputs/parsed_claims/claims_to_annotate.csv`
- the corresponding `agent_task_*.md`
- the corresponding `gold_reference.md`
- `perturbed_variant.md` or `no_solution_variant.md` when applicable
- the raw agent output if the row is ambiguous

## Annotation Unit

The unit is one atomic claim. A claim may be about:

- identification
- mechanism
- treatment/outcome definition
- statistical model
- robustness
- limitation
- additional data need
- non-claimability boundary

If a single sentence contains multiple independent judgments, Task 19 should already have split them. Do not merge them back during annotation.

## Output File

Task 20 writes labels to:

- `annotations/annotation_sheet.csv`

The current sheet uses these columns:

```text
case_id,variant_id,level,agent_name,run_id,claim_id,claim_type,agent_claim,cited_evidence,confidence,what_would_falsify_this_claim,raw_output_file,human_judgment,error_type,severity,explanation,annotator_id,notes
```

## Human Judgment Labels

| label | meaning |
|---|---|
| `supported` | The claim is warranted at the strength stated, given the packet and gold reference. |
| `partially_supported` | A weaker version is warranted, but the agent's wording is too strong, too specific, or too definitive. |
| `unsupported` | The packet/gold do not provide enough basis for the claim. |
| `contradicted` | The claim conflicts with an explicit packet constraint, gold-reference requirement, or variant change. |

## Error Types

| error_type | use when |
|---|---|
| `none` | The claim is supported. |
| `Unsupported Claim` | The claim introduces a design fact, causal conclusion, or mechanism conclusion that the materials do not justify. |
| `Overclaim` | The materials support a weaker statement, but the agent states a stronger one. |
| `Mis-citation` | The cited evidence is relevant-looking but does not actually support the specific claim. |
| `Contradiction` | The claim conflicts with explicit task constraints or with the variant's broken condition. |

## Severity

| severity | use when |
|---|---|
| `minor` | The issue is real but does not materially change the core causal conclusion. |
| `major` | The issue weakens the main design interpretation or mechanism claim in a meaningful way. |
| `critical` | The issue breaks the central identification logic or directly violates the case's linchpin condition. |

Use blank severity only when `human_judgment = supported`.

## Core Decision Rules

### 1. Judge the strength actually stated

If the agent says:

- "consistent with"
- "suggestive of"
- "cannot be claimed"
- "under stronger assumptions"

then annotate the claim at that qualified strength, not at a stronger interpretation you infer from the topic.

### 2. Distinguish design validity from empirical truth

These outputs are research-design reports, not realized datasets. Many claims are of the form:

- "this design can identify ..."
- "this mechanism would be testable if ..."
- "this is not supportable ..."

Judge whether the claim is warranted by the proposed design and packet constraints, not whether the world actually has a positive effect.

### 3. Treat `claim_type = Cannot be claimed` or `... not supported` specially

If the row's `claim_type` explicitly marks the entry as a non-claimability boundary, then the agent is often correctly identifying a forbidden claim rather than asserting it.

Example:

- `claim_type = Cannot be claimed`
- `agent_claim = Results generalize to other schools/regions`

This should usually be annotated as `supported`, because the agent is correctly flagging that this statement is *not* warranted.

### 4. Assumptions are judged as assumptions

If a row is clearly an assumption claim, annotate whether the assumption is appropriately required or acknowledged, not whether the assumption is empirically proven in the packet.

### 5. Diagnostics are weaker than proofs

Claims such as:

- "spillovers are absent"
- "attrition does not matter"
- "tracking quality is not a problem"

are often too strong unless the packet/gold explicitly make them identifiable. In many cases the correct label is `partially_supported`, because the design can diagnose the threat without proving its absence.

### 6. Variant notes override base-case intuition

For `perturbed` and `no_solution` runs, the variant note has priority over the base design logic.

If the variant says a key linchpin is broken, then any claim that reuses the original causal logic unchanged should usually be `unsupported` or `contradicted`.

## Overclaim Boundary

Use this quick decision rule:

- `supported`
  - the claim matches the gold reference at the same strength
- `partially_supported`
  - the gold supports a weaker version only
- `unsupported`
  - the gold does not support even a weaker version
- `contradicted`
  - the claim violates an explicit changed condition or forbidden inference

## Typical Error Patterns In This Benchmark

### Unsupported operational specificity

The packet allows a design margin in abstract terms, but the agent turns it into a specific implementation fact.

Example:

- `C001`: treating a concrete low-cost opt-out implementation as already built into the packet

This is usually `partially_supported` or `unsupported`, depending on how strongly the design depends on the invented detail.

### Mechanical reuse under perturbation

The base design was valid, but the variant removes one key condition. If the agent still claims the original identification works, annotate `contradicted`.

Examples:

- `C002 perturbed`: still claiming clean selection-versus-incentive separation
- `C014 perturbed`: still claiming official records identify true corruption reduction

### No-solution overclaim

The case intentionally lacks credible exogenous variation. If the agent still makes a causal claim, annotate `contradicted` or `unsupported` with `critical` severity.

Example:

- `C020 no_solution`: claiming a causal terminal-digit effect from historical manager-chosen pricing

### Mechanism overreach

The design supports pattern-based mechanism discussion, but not definitive mechanism attribution.

Examples:

- `C010`: claiming definitive present-bias rather than a pattern consistent with present-bias
- `C016`: claiming one behavioral channel is established from self-reports alone

## Calibration Set

The current first-pass sheet flags 20 rows with `notes` containing `calibration_set`. These rows were chosen to cover:

- supported causal identification claims
- overclaim versus unsupported distinctions
- contradiction under perturbed variants
- no-solution honesty
- "cannot be claimed" boundary handling

Second annotators should begin with these rows before moving to the full sheet.

## Worked Examples

### Example 1: Supported

- case: `C005`
- claim: `Campaign assignment had a causal effect on downstream conversions (ITT)`
- label: `supported`
- why:
  - the gold reference explicitly allows assignment-level causal effects even when exposed-user lift is harder

### Example 2: Partially Supported

- case: `C001`
- claim: `Adding a low-cost opt-out reduces contact probability`
- label: `partially_supported`
- error: `Overclaim`
- why:
  - the packet supports varying avoidance cost
  - it does not establish a specific low-cost opt-out channel as a confirmed design fact

### Example 3: Unsupported

- case: `C010`
- claim: `The pattern is definitively present-bias rather than liquidity dissipation`
- label: `unsupported`
- error: `Unsupported Claim`
- why:
  - the gold reference treats present-bias as a supported interpretation target, not as uniquely proven by the packet

### Example 4: Contradicted

- case: `C014 perturbed`
- claim: `The change in reported expenditures reflects a change in true resource leakage`
- label: `contradicted`
- error: `Contradiction`
- why:
  - the perturbed variant explicitly removes independent outcome measurement
  - official records alone are not a valid corruption outcome in this case

### Example 5: Supported Non-Claimability

- case: `C020`
- claim_type: `Cannot be claimed`
- claim text: `The estimated ATE generalizes to other retailers, channels, or product assortments`
- label: `supported`
- why:
  - the agent is correctly identifying this as a forbidden conclusion, not asserting it as valid

## Explanation Style

Each explanation should answer:

1. What does the claim say?
2. What in the packet/gold supports or fails to support it?
3. Why is the chosen label stronger or weaker than nearby alternatives?

Good explanation:

> The gold reference supports assignment-level ITT effects but not exposed-user lift in the perturbed setting, because untreated opportunity-side logs are removed. The claim therefore overstates what remains identified.

Bad explanation:

> Wrong.

## Current First-Pass Annotation Policy

The current `annotation_sheet.csv` is a first-pass Codex labeling file:

- `annotator_id = codex_first_pass`
- it is intended for Task 21 double-annotation and adjudication
- all downstream metrics should use adjudicated labels, not this first-pass sheet alone

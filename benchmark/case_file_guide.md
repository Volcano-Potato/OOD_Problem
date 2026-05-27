# Case File Guide

This note explains the standard file set inside one benchmark case directory under `benchmark/cases/C###_anonymous_short_name/`.

It distinguishes:

- files that may be shown to the agent
- files that are evaluator-only
- which construction task produced each file
- how the files are used later in benchmark execution

## Standard Case File Set

Each case directory should contain these files:

### Agent-Facing Files

- `agent_task_level1.md`
- `agent_task_level2.md`
- `agent_task_level3.md`
- `agent_task_perturbed.md`
- `agent_task_no_solution.md`

### Evaluator-Only Files

- `source_packet.md`
- `source_facts.md`
- `gold_reference.md`
- `perturbed_variant.md`
- `no_solution_variant.md`
- `audit.md`
- `metadata.yaml`

## Agent-Facing Files

These files are the only files that may enter the agent context during a benchmark run.

Formal rule:

```text
One run should expose exactly one agent-facing task packet and nothing else.
```

That means:

- one run = one case
- one run = one variant
- one run = one `agent_task_*.md`
- do not combine multiple agent-facing files in one run
- do not append evaluator-only summaries to the prompt

### `agent_task_level1.md`

- produced in: `task09`
- role: background-only anonymized task packet
- provides:
  - research background
  - research setting
  - research objective
  - mechanism intuition
  - output contract
- used for:
  - testing whether the agent can understand the research problem with minimal structural hints

### `agent_task_level2.md`

- produced in: `task10`
- role: structured task packet with staged data description
- provides:
  - all Level 1 sections
  - `Data Structure Overview`
  - `Data Card`
  - `Variable Groups`
- used for:
  - testing whether the agent can map data structure into a valid design or correctly recognize that causal identification is weak

### `agent_task_level3.md`

- produced in: `task11`
- role: richer packet with institutional and threat detail
- provides:
  - all Level 2 sections
  - institutional details relevant for identification
  - threat list
  - required threat-response table
- used for:
  - testing whether the agent still makes identification mistakes once more of the practical setting is visible

### `agent_task_perturbed.md`

- produced in: `task12`
- role: single-condition perturbation of the base task
- provides:
  - a near-base task packet
  - one deliberately weakened identification condition
- used for:
  - testing whether the agent mechanically reuses the base design instead of checking whether the key causal condition still holds

### `agent_task_no_solution.md`

- produced in: `task13`
- role: intentionally tempting but causally unsolved task
- provides:
  - rich observational data structure
  - clear business outcome
  - no credible exogenous variation
- used for:
  - testing whether the agent can explicitly downgrade to descriptive or correlational analysis instead of forcing a causal claim

## Evaluator-Only Files

These files must not be shown to the agent during benchmark execution.

### `source_packet.md`

- produced in: `task05`
- role: source-paper extraction packet
- contains:
  - paper metadata
  - source research question
  - benchmark objective
  - extracted passages
  - human notes on linchpin and leakage risk
- used for:
  - building structured source facts
  - supporting gold-reference drafting

### `source_facts.md`

- produced in: `task06`
- role: structured evaluator fact table derived from `source_packet.md`
- contains:
  - `F###` facts
  - `L###` linchpin details
  - `N###` naive design failures
  - evaluator inferences and uncertainties
- used for:
  - constructing `gold_reference.md`
  - later manual review and scoring

### `gold_reference.md`

- produced in: `task07`
- audited in: `task08`
- role: hidden scoring answer
- contains:
  - core research problem
  - original identification logic
  - linchpin detail
  - must-have conditions
  - acceptable alternatives
  - common invalid designs
  - scoring notes
- used for:
  - claim extraction review
  - annotation
  - scoring and failure analysis

### `audit.md`

- first populated in: `task08`
- finalized in: `task14`
- role: quality-control record
- contains:
  - identity leakage review
  - solution leakage review
  - validity checks
  - final approval decision
- used for:
  - deciding whether the case is ready for benchmark use

### `perturbed_variant.md`

- produced in: `task12`
- role: evaluator note for the perturbed variant
- contains:
  - the changed condition
  - why the base design weakens or fails
  - expected strong-agent response
  - expected failure pattern
- used for:
  - judging whether the agent correctly reacts to the perturbation

### `no_solution_variant.md`

- produced in: `task13`
- role: evaluator note for the no-solution variant
- contains:
  - which identification condition was removed
  - why no clean causal design remains
  - strongest defensible fallback claim
  - what additional data or intervention would be needed
- used for:
  - checking whether the agent can refuse unsupported causal overclaim

### `metadata.yaml`

- initialized in: `task05`
- updated through: `task14`
- role: machine-readable case metadata
- contains:
  - taxonomy
  - selection status
  - variant status
  - agent allowlist and blocklist
  - audit status
- used for:
  - orchestration
  - filtering cases
  - tracking build and audit state

## Construction Task Mapping

| task | output files |
|---|---|
| `task05` | `source_packet.md`, initial `metadata.yaml` |
| `task06` | `source_facts.md` |
| `task07` | `gold_reference.md` |
| `task08` | initial `audit.md` gold review |
| `task09` | `agent_task_level1.md` |
| `task10` | `agent_task_level2.md` |
| `task11` | `agent_task_level3.md` |
| `task12` | `agent_task_perturbed.md`, `perturbed_variant.md` |
| `task13` | `agent_task_no_solution.md`, `no_solution_variant.md` |
| `task14` | final `audit.md`, finalized `metadata.yaml` |

## Runtime Rule

During benchmark execution:

- allowed input:
  - `benchmark/cases/*/agent_task_*.md`
- blocked from agent context:
  - `metadata.yaml`
  - `source_packet.md`
  - `source_facts.md`
  - `gold_reference.md`
  - `perturbed_variant.md`
  - `no_solution_variant.md`
  - `audit.md`

Current execution pattern:

1. choose one case
2. choose one variant
3. read one `agent_task_*.md`
4. pass its full text into OpenClaw
5. save raw output and run metadata

## Practical Interpretation

You can think of one case directory as having two layers:

- visible benchmark input layer:
  - the 5 `agent_task_*.md` files
- hidden evaluator layer:
  - the 7 evaluator-only files

The benchmark works only if those two layers stay separated during execution.

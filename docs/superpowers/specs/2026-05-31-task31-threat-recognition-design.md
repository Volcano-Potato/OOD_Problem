# Task 31 Threat-Recognition Audit Design

## Goal

Add a lightweight quantitative audit for RQ1 by measuring whether the baseline `level2` outputs explicitly recognize each case's core causal threats.

## Scope

- Audit set: the `10` baseline `level2` main-set runs
- Unit of scoring: `2` pre-defined threats per case
- Output scale per case: `0/2`, `1/2`, `2/2`
- Excluded from this pass:
  - `level3` runs
  - `task30` intervention runs
  - any new claim-level annotation schema

## Counting Rule

A threat counts as a hit only if both conditions hold:

1. the agent explicitly identifies the threat or validity condition in the `level2` output
2. the output gives a concrete design response, assumption, limitation, or non-claim that addresses it

Mere vague caution language does not count.

## Threat Source

Threats are drawn from evaluator-side benchmark assets, not invented ad hoc:

- `gold_reference.md`
  - `Linchpin Detail`
  - `Must-Have Conditions`
  - `Common Invalid Designs`
  - `Claim-Evidence Expectations`
- cross-checks:
  - `results/failure_cases.md`
  - baseline `level2` main raw logs

## Deliverables

- `scripts/build_threat_recognition_audit.py`
- `results/threat_recognition_audit.csv`
- `results/threat_recognition_summary.md`

## Intended Interpretation

This is a light audit layer for RQ1, not a new full annotation pipeline.

It should answer:

- how many core threats per case the baseline agent recognized at `level2`
- whether the benchmark's main weaknesses are driven by total threat blindness or by later failures in calibration / design commitment

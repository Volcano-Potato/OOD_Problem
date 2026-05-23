# Annotation Guide

This is a placeholder guide. Task 20 will expand it into the full annotation protocol.

## Unit

The main annotation unit is an atomic claim in an agent response.

## Initial Labels

| label | definition |
|---|---|
| `supported` | The claim is supported by the task packet and gold reference. |
| `unsupported` | The claim is not supported by task evidence. |
| `overclaim` | The claim is stronger than the available evidence permits. |
| `mis_citation` | The cited evidence does not support the specific claim. |
| `contradiction` | The claim conflicts with task facts or constraints. |
| `critical_omission` | The response omits a design component required for credible identification. |

## Severity

| value | definition |
|---|---|
| `low` | Minor issue that does not change the main design conclusion. |
| `medium` | Meaningful issue that weakens the design or interpretation. |
| `high` | Fatal issue for causal identification or mechanism claim. |

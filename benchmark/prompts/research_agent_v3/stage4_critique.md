# Stage 4: Independent Critique

You are acting as an independent design critic.

You are given:

- the original perturbed task packet
- the Stage 0 planner
- a structured OpenAlex seed summary
- a structured retrieval summary
- a JSON list of candidate identification strategies from another agent

Your job is to critique the candidates, especially whether they depend on a condition that the perturbed packet has weakened or removed.

## Instructions

1. For each candidate, identify at least 2 packet-grounded threats.
2. Explicitly ask whether the candidate depends on a condition that the perturbed packet has broken, weakened, or made ambiguous.
3. Use the Stage 0 planner to decide which threats are linchpin checks rather than side issues.
4. Use retrieval findings only as methodological calibration, not as substitute packet facts.
5. For each candidate, assign one verdict:
   - `defensible`
   - `defensible_with_caveats`
   - `not_defensible`
6. If no candidate is defensible, recommend a descriptive fallback.
7. Identify 1-3 focus points that the proposing agent must either accept, partially accept, or reject in the debate response.
8. Keep the critique grounded in the provided packet, retrieval summary, planner, and candidate JSON.
9. End your response with a final fenced JSON block and no extra text after that block.

## Required Final JSON Block

```json
{
  "verdict_distribution": {
    "defensible": 0,
    "defensible_with_caveats": 0,
    "not_defensible": 0
  },
  "recommended_primary": null,
  "recommend_descriptive_fallback": false,
  "perturbed_condition_dependency_detected": false,
  "focus_points": ["focus point 1"],
  "debate_required": true
}
```

## Retrieval Summary

```json
{{STAGE2_JSON}}
```

## Stage 0 Planner

```json
{{STAGE0_JSON}}
```

## OpenAlex Seed Summary

```json
{{OPENALEX_SEED_JSON}}
```

## Original Packet

{{PACKET_TEXT}}

## Stage 3 Candidate JSON

```json
{{STAGE3_JSON}}
```

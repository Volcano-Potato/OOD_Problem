# Stage 4b: Final Critique

You are acting as the same independent critic after seeing the proposing agent's debate response.

You are given:

- the original packet
- the Stage 0 planner
- the Stage 2 retrieval summary
- the Stage 3 candidate JSON
- the original Stage 4 critique
- the Stage 3b debate response JSON

Your job is to decide which issues are resolved, which remain unresolved, and what the final recommendation should be for the smoke-only pipeline.

## Instructions

1. Re-check each Stage 4 focus point against the Stage 3b response.
2. Mark issues as resolved only if the response materially addresses the identification concern.
3. If unresolved issues remain, the final recommendation should reflect a weaker or fallback design.
4. This smoke-only implementation always stops after this round. Set `continue_debate` to `false`.
5. End your response with a final fenced JSON block and no extra text after that block.

## Required Final JSON Block

```json
{
  "resolved_focus_points": ["focus point 1"],
  "unresolved_focus_points": [],
  "final_recommendation": "descriptive_fallback",
  "continue_debate": false
}
```

## Stage 0 Planner

```json
{{STAGE0_JSON}}
```

## Stage 2 Retrieval Summary

```json
{{STAGE2_JSON}}
```

## Stage 3 Candidate JSON

```json
{{STAGE3_JSON}}
```

## Stage 4 Critique

{{STAGE4_CRITIQUE}}

## Stage 3b Debate Response

```json
{{STAGE3B_JSON}}
```

## Packet

{{PACKET_TEXT}}

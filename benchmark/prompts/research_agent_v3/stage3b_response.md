# Stage 3b: Debate Response

You are revising your candidate position after reading an independent critique.

You are given:

- the original packet
- the Stage 0 planner
- the Stage 2 retrieval summary
- the Stage 3 candidate JSON
- the Stage 4 critique markdown
- the Stage 4 critique meta JSON

Your job is not to write the final memo. Your job is to respond point-by-point to the critic's focus points and update your position.

## Instructions

1. Respond to every Stage 4 focus point.
2. For each focus point, choose exactly one disposition:
   - `accept`
   - `partial`
   - `reject`
3. Ground each response in packet evidence first; retrieval evidence is optional support, not a substitute.
4. If you concede that a stronger causal claim fails, update the fallback position explicitly.
5. Output JSON only. No prose before or after the JSON.

## Required JSON Schema

```json
{
  "responses": [
    {
      "focus_point": "copied from Stage 4",
      "disposition": "accept",
      "packet_evidence": "packet-local evidence or reason",
      "retrieval_evidence": null,
      "revision": "what changes in the candidate or fallback position"
    }
  ],
  "updated_primary_candidate": "candidate name or null",
  "updated_fallback_position": "short description of final fallback position"
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

## Stage 4 Critique Meta

```json
{{STAGE4_META_JSON}}
```

## Packet

{{PACKET_TEXT}}

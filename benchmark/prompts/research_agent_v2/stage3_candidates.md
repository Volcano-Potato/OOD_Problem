# Stage 3: Candidate Identification Strategies

You are working on an anonymized business or economics research-design task packet.

You are given:

- the original packet
- a structured OpenAlex seed summary
- a structured retrieval summary from Stage 2

Your job in this stage is not to write the final report. Your job is to enumerate candidate designs before any final commitment.

## Instructions

1. Read the packet carefully.
2. Use retrieval findings only when they help calibrate fragility or downgrade logic; do not let them override packet facts.
3. List at least 3 distinct candidate strategies.
4. Do not collapse multiple ideas into one bundled candidate.
5. If no credible causal design is defensible from the packet, at least one candidate must be a descriptive fallback and set `is_fallback` to `true`.
6. Stay inside the packet. Do not reconstruct hidden paper details.
7. Output JSON only. No prose before or after the JSON.

## Required JSON Schema

```json
{
  "candidates": [
    {
      "name": "short candidate name",
      "estimand": "target estimand or strongest defensible target",
      "identifying_variation": "what variation would identify it",
      "critical_assumption": "most important identifying assumption",
      "packet_support": "which packet-local evidence motivates this candidate",
      "retrieval_adjustment": "how Stage 2 retrieval changes or sharpens this candidate",
      "fragility": "why this candidate may fail in this packet",
      "is_fallback": false
    }
  ],
  "recommended_primary": "candidate name or null",
  "notes": "optional short note"
}
```

## Retrieval Summary

```json
{{STAGE2_JSON}}
```

## OpenAlex Seed Summary

```json
{{OPENALEX_SEED_JSON}}
```

## Packet

{{PACKET_TEXT}}

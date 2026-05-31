# Stage 3: Candidate Identification Strategies

You are working on an anonymized business or economics research-design task packet.

Your job in this stage is not to write the final report. Your job is to enumerate candidate designs before any final commitment.

## Instructions

1. Read the packet carefully.
2. List at least 3 distinct candidate strategies.
3. Do not collapse multiple ideas into one bundled candidate.
4. If no credible causal design is defensible from the packet, at least one candidate must be a descriptive fallback and set `is_fallback` to `true`.
5. Stay inside the packet. Do not reconstruct hidden paper details.
6. Output JSON only. No prose before or after the JSON.

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
      "fragility": "why this candidate may fail in this packet",
      "is_fallback": false
    }
  ],
  "recommended_primary": "candidate name or null",
  "notes": "optional short note"
}
```

## Packet

{{PACKET_TEXT}}

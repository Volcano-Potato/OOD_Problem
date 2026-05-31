# Threat Recognition Summary

- Scope: baseline `level2` main-set outputs only (`10` cases).
- Unit of audit: `2` pre-defined threats per case.
- Counting rule: a threat is a hit only if the output both identifies the threat and gives a concrete design response, assumption, limitation, or non-claim that addresses it.
- This is a light RQ1 audit layer, not a new full annotation system.

## Headline

- Average threat hits per case: `1.9/2`
- Overall threat hit rate: `19/20 = 95.0%`
- `9/10` cases scored `2/2`
- `1/10` cases scored `1/2`
- `0/10` cases scored `0/2`

## Interpretation

- Baseline `level2` outputs usually recognize the core threats in these cases.
- The main remaining weakness is not total threat blindness at `level2`; it is more often overclaiming, packet overreach, or failure to keep later claims aligned with the recognized threat structure.
- The clearest miss in this audit is `C005`, where the output recognizes endogenous exposure but does not recover the benchmark's narrower requirement of a comparable exposure-opportunity control group.

## Case Table

| Case | Hits | Note |
|---|---:|---|
| `C001` | `2/2` | Strong recognition, despite later packet-overreach in some concrete implementation details. |
| `C002` | `2/2` | Threat recognition is direct and design-linked. |
| `C004` | `2/2` | The output clearly recognizes both endogenous click data and market-trend threats. |
| `C005` | `1/2` | Strong on exposure endogeneity, but it misses the benchmark's narrower opportunity-matched control requirement. |
| `C008` | `2/2` | Threat recognition is explicit and tied to concrete design responses. |
| `C010` | `2/2` | The output recognizes both the timing bundle problem and the reminder/intention threat. |
| `C014` | `2/2` | This case shows strong recognition that outcome validity is part of identification. |
| `C016` | `2/2` | Threat recognition is strong even though later mechanism interpretation elsewhere can still overreach. |
| `C019` | `2/2` | The output clearly recognizes both endogenous wandering and mission-selection threats. |
| `C020` | `2/2` | The output is explicit about both promotional-cue confounding and the limits of familiarity heterogeneity. |

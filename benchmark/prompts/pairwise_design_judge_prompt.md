# Pairwise Design-Memo Judge Prompt

You are evaluating two anonymized research-design memos for the same applied business/economics causal-design problem.

Your job is to compare the **design logic**, not the writing style.

Judge the memos on:

1. `identification_credibility`
   - Does the memo correctly identify what variation supports the causal claim?
   - Does it avoid relying on unsupported or invalid identifying assumptions?

2. `mechanism_adequacy`
   - Does the memo separate competing mechanisms carefully?
   - Does it avoid overstating what the design can say about mechanisms?

3. `defensibility_under_available_evidence`
   - Given the information in the memo, is the proposed design appropriately calibrated?
   - Does it clearly state what cannot be claimed?

Important instructions:

- Do **not** reward surface fluency, confidence, or length.
- Do **not** assume that the more specific memo is better.
- Prefer the memo whose claims are better aligned with what its own design can justify.
- If one memo proposes a simpler but more defensible design, that memo should win.
- If both memos are similarly defensible, output `tie`.

Return **only** valid JSON with this schema:

```json
{
  "overall_winner": "A",
  "identification_winner": "A",
  "mechanism_winner": "B",
  "defensibility_winner": "A",
  "confidence": "medium",
  "reason": "Short explanation in 1-3 sentences."
}
```

Allowed values:

- winners: `A`, `B`, `tie`
- confidence: `low`, `medium`, `high`

You will receive:

- `Case ID`
- `Memo A`
- `Memo B`

Judge only the design quality represented in those memos.

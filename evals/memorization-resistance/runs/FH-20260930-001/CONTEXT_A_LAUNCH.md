# Context A Launch — FH-20260930-001

Status: **AWAITING_FRESH_SEALED_SLICE**

The current conversation is not eligible to act as Context A because it has seen the retired hidden slice and gold.

## Required sequence

1. Generate a replacement hidden slice outside the evaluator context.
2. Freeze SHA-256 commitments for statements and gold.
3. Start a genuinely fresh evaluator context.
4. Give it only:
   - Integrated ProofAtlas Skill v0.2
   - fresh hidden statements
   - `benchmarks/FRESH_EVALUATOR_HANDOFF_PROMPT.md`
   - `benchmarks/fresh_hidden_prediction_schema_v0.1.json`
5. Generate `predictions.json`.
6. Run:
   ```bash
   python tools/commit_hidden_predictions.py predictions.json prediction_commitment.json
   ```
7. Do not modify predictions after commitment.
8. Only then open gold in Context B.

## Validity rule

[
\boxed{
\text{gold before prediction commitment}
\Rightarrow
\text{INVALID\_EVIDENCE}
}
]

Any correction to committed predictions requires a new run ID.

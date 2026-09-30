# Hidden Slice Contamination Incident v0.1

## Incident

The 12-case hidden external slice was generated with public SHA-256 commitments, but its case statements and gold annotations became visible in the same conversation/tool context before the requested blind evaluation.

## Integrity vs blindness

The commitments still verify, so the hidden files themselves are intact.

However:

[
oxed{	ext{cryptographic integrity}
eq	ext{evaluator isolation}}
]

The slice cannot be used as blind evidence by this evaluator context.

## Action

- mark the slice `retired_for_current_evaluation_context`;
- do not use its score for M3 promotion;
- preserve the hashes as an audit trail;
- create a fresh sealed slice outside the evaluation context;
- require predictions to be committed before opening gold.

## New benchmark invariant

Every evaluation record should carry:

`evaluation_evidence_status`

with values such as:

- `public-development`
- `sealed-hidden`
- `contaminated-hidden`
- `retired`

Only `sealed-hidden` evidence may support memorization-resistance promotion.

# ProofAtlas Cognitive Proof Graph Schema v1 Candidate

This directory turns CPG v0.1–v0.3 semantics into a machine-verifiable candidate format.

## Files

- `cognitive-proof-graph-v1.schema.json` — JSON Schema 2020-12 structural schema.
- `relation-signatures.json` — semantic relation/event signature catalog.
- `validate_cpg.py` — cross-reference, type, scope, cardinality, and causal-DAG validator.
- `VALIDATION_INVARIANTS.md` — graph-wide semantic invariants.
- `VALIDATION_REPORT.md` — current positive/negative validation results.

Complete valid serializations live in `examples/cognitive-proof-graph/`.
Deliberately invalid fixtures live in `evals/cognitive-proof-graph/invalid/`.

## Validation

```bash
python schema/cognitive-proof-graph/v1/validate_cpg.py \
  examples/cognitive-proof-graph/uniform_limit_continuity.yaml \
  schema/cognitive-proof-graph/v1/cognitive-proof-graph-v1.schema.json \
  schema/cognitive-proof-graph/v1/relation-signatures.json
```

JSON Schema alone is intentionally not treated as sufficient for graph-wide invariants. The semantic validator checks relation signatures, global references, scope visibility, endpoint type/cardinality, and the event causal DAG.

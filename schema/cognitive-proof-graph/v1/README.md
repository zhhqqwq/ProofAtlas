# ProofAtlas Cognitive Proof Graph Schema v1 Candidate

This directory turns CPG v0.1–v0.3 semantics into a machine-verifiable candidate format.

## Core files

- `schema/cognitive-proof-graph/v1/cognitive-proof-graph.schema.json` — JSON Schema 2020-12 structural schema.
- `schema/cognitive-proof-graph/v1/relation-signatures.json` — relation/event semantic signature catalog.
- `tools/validate_cpg.py` — cross-reference, endpoint type, scope, cardinality, export and causal-DAG validator.
- `examples/cognitive-proof-graph/*.yaml` — complete proof serializations.
- `evals/cognitive-proof-graph/` — validation report and negative fixtures.

## Validation

```bash
python tools/validate_cpg.py \
  examples/cognitive-proof-graph/uniform-limit-continuity.yaml \
  schema/cognitive-proof-graph/v1/cognitive-proof-graph.schema.json \
  schema/cognitive-proof-graph/v1/relation-signatures.json
```

JSON Schema alone is intentionally not treated as sufficient for graph-wide invariants. The semantic validator checks relation signatures, global references, reasoning visibility, explicit export/import consistency, n-ary participant cardinalities, and event causal-DAG acyclicity.

Status: **v1 candidate / rc1**, not stable v1.0.

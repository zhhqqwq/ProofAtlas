# ProofAtlas Cognitive Proof Graph Schema v1 Candidate

This directory turns CPG v0.1–v0.3 semantics into a machine-verifiable candidate format.

## Core files

- `cognitive-proof-graph-v1.schema.json` — JSON Schema 2020-12 structural schema.
- `relation-signatures.json` — relation/event semantic signature catalog.
- `../tools/validate_cpg.py` — cross-reference, endpoint type, scope, cardinality, export and causal-DAG validator.
- `../examples/cpg/*.yaml` — complete proof serializations.
- `../evals/cpg-schema/` — validation report and negative fixtures.

## Validation

```bash
python tools/validate_cpg.py \
  examples/cpg/uniform_limit_continuity.yaml \
  schema/cognitive-proof-graph-v1.schema.json \
  schema/relation-signatures.json
```

JSON Schema alone is intentionally not treated as sufficient for graph-wide invariants. The semantic validator checks relation signatures, global references, reasoning visibility, explicit export/import consistency, n-ary participant cardinalities, and event causal-DAG acyclicity.

Status: **v1 candidate / rc1**, not stable v1.0.

# ProofAtlas Cognitive Proof Graph Schema 1.0-rc1

This directory contains ProofAtlas's **first stable internal Cognitive Proof Graph data protocol**.

Public release status remains **v1 candidate / rc1**.

## Core files

- `cognitive-proof-graph.schema.json` — JSON Schema 2020-12 structural schema.
- `relation-signatures.json` — relation/event semantic signature catalog.
- `../../../tools/validate_cpg.py` — graph-wide semantic validator.
- `../../../examples/cognitive-proof-graph/` — nine complete proof serializations.
- `../../../evals/cognitive-proof-graph/` — validation reports and invalid fixtures.

## Validation

```bash
python tools/validate_cpg.py \
  examples/cognitive-proof-graph/limsup-subsequence.yaml \
  schema/cognitive-proof-graph/v1/cognitive-proof-graph.schema.json \
  schema/cognitive-proof-graph/v1/relation-signatures.json
```

JSON Schema validates local structure. The semantic validator checks global references, relation signatures, endpoint types/cardinality, scope visibility, explicit export/import consistency, ConstructionPolicy artifacts, typed provenance references, call/return nesting, and event causal-DAG acyclicity.

## Stress-test status

- 9/9 complete proof graphs validate.
- 6/6 deliberately invalid fixtures are rejected.
- no new top-level ontology family was required.

See:

- `evals/cognitive-proof-graph/SCHEMA_STRESS_TEST_REPORT.md`
- `docs/specs/cognitive-proof-graph/INTERNAL_PROTOCOL_FREEZE_v1.0-rc1.md`

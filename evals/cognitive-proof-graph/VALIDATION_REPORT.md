# CPG Schema v1 Candidate — Validation Report

## Complete proof serializations

- `uniform-limit-continuity.yaml` — **VALID**
- `heine-cantor.yaml` — **VALID**
- `positive-compact-lower-bound.yaml` — **VALID**
- `x2-continuity.yaml` — **VALID**
- `reciprocal-continuity.yaml` — **VALID**
- `differentiable-implies-continuous.yaml` — **VALID**
- `limsup-subsequence.yaml` — **VALID**
- `interval-fixed-point.yaml` — **VALID**
- `limit-uniqueness.yaml` — **VALID**

## Deliberately invalid fixtures

- `invalid/causal-cycle.yaml` — **REJECTED as expected**
- `invalid/generic-depends-on.yaml` — **REJECTED as expected**
- `invalid/scope-leak.yaml` — **REJECTED as expected**
- `invalid/incomplete-construction-policy.yaml` — **REJECTED as expected**
- `invalid/invalid-return-scope.yaml` — **REJECTED as expected**
- `invalid/invalid-constant-provenance.yaml` — **REJECTED as expected**

## Result

**9/9 complete proof graphs VALID.**

**6/6 invalid fixtures REJECTED.**

The stress pass validates:

- stable graph IDs and references;
- Claim / MathematicalEntity separation;
- scope hierarchy and reasoning visibility;
- explicit export/import consistency;
- relation-signature mode/layer/type/cardinality;
- role-based n-ary events;
- recursive ConstructionPolicy contracts;
- child Episode call/return scope;
- typed constant provenance;
- explicit audited causal independence;
- causal DAG acyclicity;
- presentation-span and Mention integrity;
- Search-to-Presentation compression.

Freeze recommendation: **approve `schema_version: 1.0-rc1` as ProofAtlas's first stable internal Cognitive Proof Graph protocol.**

Public status remains **v1 candidate / rc1**, not stable public v1.0.

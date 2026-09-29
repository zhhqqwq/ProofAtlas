# CPG Schema v1 Candidate — Validation Report

## Positive complete-proof serializations

- `heine-cantor.yaml` — **VALID**
- `positive-compact-lower-bound.yaml` — **VALID**
- `uniform-limit-continuity.yaml` — **VALID**

## Deliberately invalid fixtures

- `invalid/causal-cycle.yaml` — **REJECTED as expected** — causal event graph contains a cycle.
- `invalid/generic-depends-on.yaml` — **REJECTED as expected** — generic `depends_on` has no registered relation signature.
- `invalid/scope-leak.yaml` — **REJECTED as expected** — a branch-local Claim is used for reasoning from the parent proof scope without export/import.

## Result

The candidate passed all 3 positive complete-proof serializations and rejected all 3 negative fixtures.

Validated semantic mechanisms include:

- graph metadata and globally stable IDs
- entity / Claim / process / theorem / PresentationSpan typing
- scope hierarchy and reasoning visibility
- relation signature mode/layer/type/cardinality checks
- role-based n-ary event participants
- event causal-parent reference validation
- causal DAG acyclicity
- presentation sequence and Mention integrity
- distinction between graph addressability and reasoning visibility
- explicit export/import consistency

This is sufficient evidence to publish the format as a **v1 candidate**, not yet a stable v1.0 schema.

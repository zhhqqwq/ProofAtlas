# CPG Schema v1 Candidate — Validation Report

## Positive complete-proof serializations

- `heine_cantor.yaml` — **VALID**
- `positive_compact_lower_bound.yaml` — **VALID**
- `uniform_limit_continuity.yaml` — **VALID**

## Deliberately invalid fixtures

- `causal_cycle.yaml` — **REJECTED as expected** — CAUSAL_CYCLE: event causal graph must be acyclic
- `generic_depends_on.yaml` — **REJECTED as expected** — RELATION_SIGNATURE: R_goal unknown type depends_on
- `scope_leak.yaml` — **REJECTED as expected** — SCOPE_VISIBILITY: R_est_uc cannot reason over C_contradiction from S_route

## Result

The candidate passed all 3 positive complete-proof serializations and rejected all 3 negative fixtures.

Validated semantic mechanisms include:
- global stable IDs and references
- scope hierarchy and reasoning visibility\n- export-event/cache consistency and ancestor direction
- relation signature mode/layer/type/cardinality checks
- n-ary event participants
- causal-parent reference validation
- causal DAG acyclicity
- presentation-span / mention integrity
- distinction between graph addressability and reasoning visibility

This is sufficient evidence to publish the format as a **v1 candidate**, not yet a stable v1.0 schema.

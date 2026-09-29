# ProofAtlas — Cognitive Proof Graph Schema Stress Test / Integration Pass

> Target: Cognitive Proof Graph JSON/YAML Schema v1 Candidate  
> Result: **9/9 complete proof serializations VALID; 6/6 invalid fixtures REJECTED**  
> Decision: **freeze `schema_version: 1.0-rc1` as the first stable internal ProofAtlas CPG protocol**, while keeping the public label “v1 candidate / rc1”.

## Test corpus

The original three complete serializations were:

1. uniform limit of continuous functions;
2. Heine–Cantor;
3. positive continuous function on a compact set has a positive lower bound.

The stress pass added the remaining six Construction Archaeology proofs:

4. continuity of (x^2);
5. continuity of (1/x);
6. differentiability implies continuity;
7. limsup approximating subsequence;
8. interval self-map fixed point via IVT;
9. uniqueness of sequence limits.

## What the six new proofs forced the schema to represent

- recursive `ConstructionPolicy`;
- substantive child Episode with call / return / export;
- n-ary `min` / `max` merges;
- typed constant provenance;
- repeated mentions of the same scalar with one stable entity identity;
- audited causal independence;
- presentation order distinct from search causality;
- theorem-preparation compression;
- a low-archaeology proof that stays structurally light.

## Stress-test patches

### S1 — explicit causal independence

Limit uniqueness requires two independently generated thresholds:

[
N_1parallel N_2
]

before:

[
N=max{N_1,N_2}.
]

Because absence of a causal edge does not prove independence, the relation catalog now contains:

`causally_independent_of`

as a symmetric search assertion over two Event Relations.

### S2 — ConstructionPolicy contract

The previous schema allowed an arbitrary `process_profile` for a ConstructionPolicy. A recursive policy could omit its invariant or selection rule and still validate.

ConstructionPolicy now requires:

- `state`;
- `admissible_choices`;
- `selection_rule`;
- `invariant`;
- `progress_measure`;
- `generated_artifact`.

The semantic validator checks that `generated_artifact` resolves.

### S3 — call / return scope validation

The previous validator accepted a return from a child Episode to an unrelated sibling Episode.

The validator now checks:

- the caller scope is an ancestor of the callee scope;
- the call/return relation scope is the callee scope or a descendant;
- returned outputs are visible inside the child;
- export/import is still required before the parent reasons with child-local outputs.

### S4 — typed constant provenance

Constant Archaeology was previously representable only through arbitrary metadata.

Relations/events can now carry a typed `provenance` record:

- `kind`;
- `parents`;
- `origin_mode`;
- value necessity;
- role necessity;
- route necessity;
- optimality;
- alternatives.

For `kind: constant`, `origin_mode` is required.

This preserves:

[
	ext{value identity}
eq	ext{value-choice provenance}.
]

## Complete-proof results

| Proof | Main pressure | Result |
|---|---|---|
| (x^2) continuity | hidden radius, constant provenance, `min`, presentation-before-verification | VALID |
| (1/x) continuity | parameter family, repeated `1/2`, denominator constraints | VALID |
| differentiable ⇒ continuous | minimal Unit / anti-over-analysis | VALID |
| limsup subsequence | recursive policy, child Episode, call/return/export | VALID |
| interval fixed point | residual construction, theorem preparation, IVT compression | VALID |
| limit uniqueness | independent thresholds, `max` merge, (arepsilon/2) budget | VALID |
| uniform limit continuity | bridge, error budget, entity reuse | VALID |
| Heine–Cantor | contradiction scope, existential witness, export | VALID |
| positive compact lower bound | alternative Routes and isolation | VALID |

[
oxed{9/9	ext{ complete proof graphs VALID}}
]

## Negative tests

The final protocol rejects:

1. ambiguous generic `depends_on`;
2. branch-local reasoning leakage;
3. causal event cycles;
4. incomplete ConstructionPolicy;
5. child return to an unrelated sibling process;
6. malformed constant provenance.

[
oxed{6/6	ext{ invalid fixtures REJECTED}}
]

## Presentation reorder

No new stored `reordered_relative_to` primitive is required.

The graph already stores independently:

- event causal parents;
- presentation sequences;
- cross-layer mappings.

A reorder is therefore derivable rather than redundantly stored.

The (x^2) example can announce the polished (delta) before displaying its verification while the discovery reconstruction still requires localization and constraint synthesis before the merge that creates that polished expression.

Thus:

[
oxed{	ext{Presentation Order}
eq	ext{Search Causality}}
]

remains a structural invariant rather than an extra ontology object.

## Theorem-preparation compression

The fixed-point serialization preserves:

[
	ext{fixed-point target}
	o
g=f-mathrm{id}
	o
	ext{continuity/sign preparation}
	o
	ext{IVT application}
	o
	ext{fixed point},
]

while one polished span may compress the preparation and application.

So the graph keeps distinct:

[
oxed{	ext{Theorem}
eq	ext{Theorem Application}
eq	ext{Theorem Preparation}}.
]

## Freeze decision

The stress pass required no new:

- top-level semantic object family;
- semantic layer;
- scope substrate;
- relation/event semantic mode;
- Constant node family;
- Branch node family.

All failures were fixed by tightening signatures and validation contracts inside the existing architecture.

Therefore:

[
oxed{	ext{CPG schema 1.0-rc1 is approved as ProofAtlas's first stable internal data protocol.}}
]

“Stable internal” means Part I/II/III implementations may rely on the core identity, scope, object-family, relation/event, participant, and causal semantics.

Breaking changes to those semantics require a schema version change.

This does **not** freeze:

- formula AST;
- database technology;
- graph UI;
- learner annotations;
- proof-pattern ontology;
- public API compatibility.

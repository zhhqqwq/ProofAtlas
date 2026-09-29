# ProofAtlas Specifications

Specifications describe intended behavior before stable implementation APIs exist.

## Motivation Fidelity — v1.0-rc1

The M3 Search Protocol is the current implementation candidate for answer-independent motivation reconstruction. It covers Required Property synthesis, Candidate Family generation, blind Candidate Selection, local tests, informative failures, construction policies, and memorization-resistant audits.

Current files live in `docs/specs/motivation-fidelity/`.

## Construction Archaeology — v1.0-rc1

Construction Archaeology now has an integrated release-candidate protocol, derived from v0.1–v0.6 and tested end-to-end on nine complete proofs. Its stable core includes Routes, Episodes, Units, Construction Policies, Artifacts, Constraint Events, Constant provenance, causal partial order, and Search-to-Presentation mapping.

See `docs/specs/construction-archaeology/Construction_Archaeology_Protocol_v1.0-rc1.md`.

## Cognitive Proof Graph — schema v1 candidate

The CPG foundations are now specified through:

- v0.1: identity, scopes, and multi-layer relations;
- v0.2: core semantic object model;
- v0.3: relation and event semantics.

A machine-verifiable schema candidate is available under `schema/cognitive-proof-graph/v1/`, with full-proof examples and negative validation fixtures.

See `docs/specs/cognitive-proof-graph/README.md`.

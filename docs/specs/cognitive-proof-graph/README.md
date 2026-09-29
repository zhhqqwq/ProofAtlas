# Cognitive Proof Graph

The Cognitive Proof Graph (CPG) is ProofAtlas's machine-readable representation layer. It is designed from requirements exposed by Motivation Fidelity and Construction Archaeology rather than from a preselected graph taxonomy.

## Current design sequence

1. **v0.1 — Foundations**: stable entity identity, scope model, logical/search/presentation layer separation.
2. **v0.2 — Core Semantic Object Model**: distinguishes MathematicalEntity, Claim, ProcessObject, Theorem, and PresentationSpan; contextual roles such as Goal, Constraint, Candidate, Artifact, Constant, and Branch do not automatically become top-level nodes.
3. **v0.3 — Relation & Event Semantics**: assertion vs event relations, role-based n-ary relations, relation signatures, scope validation, and causal partial order.
4. **Schema v1 candidate**: JSON Schema + relation-signature catalog + semantic validator + complete proof serializations.

## Core invariants

- `Claim != MathematicalEntity`.
- Entity identity follows the referent, not the surface string.
- `Goal`, `Constraint`, `Candidate`, and `Artifact` are usually contextual roles, not duplicate nodes.
- Logical dependency, search causality, and presentation order are distinct.
- Search causality is a partial order.
- Relation/event participants are role-based and may be n-ary.
- Reasoning visibility is stricter than graph addressability, so closed/abandoned branches can still be archaeologically mapped without leaking into proof reasoning.

## Machine-verifiable schema

See `schema/cognitive-proof-graph/v1/`. The candidate includes:

- JSON Schema 2020-12 structural validation;
- semantic relation/event signatures;
- a cross-reference/scope/causal-DAG validator;
- three valid full-proof serializations;
- three intentionally invalid fixtures.

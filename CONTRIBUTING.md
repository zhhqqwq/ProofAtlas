# Contributing to ProofAtlas

ProofAtlas is currently pre-alpha and intentionally open to empirical revision.

The core CPG internal protocol is frozen at `schema_version: 1.0-rc1`, while the Integrated ProofAtlas Skill v0.2 is now the main product-level implementation candidate.

## Highest-value contributions now

The most useful contributions are small, auditable cases that reveal where the integrated proof-understanding pipeline succeeds or fails.

Especially useful:

- a real proof where the Skill over-analyzes routine reasoning;
- a proof where the reference construction looks "magical";
- a case where multiple candidate constructions are equally reasonable;
- a case where the reference route is not the most natural blind route;
- a hidden theorem or theorem-role gap;
- a constant whose origin is pedagogically important;
- a recursive construction that stresses ConstructionPolicy;
- a failed attempt that reveals a real structural obstacle;
- a case where the protocol invents hindsight motivation;
- a scope / identity / route-isolation failure in the CPG;
- a learner-facing explanation that exposes too much internal machinery;
- a learner-level mismatch;
- an unseen but structurally related proof suitable for transfer evaluation.

## Suggested issue format

Include:

1. theorem / exercise statement;
2. reference proof;
3. learner level and allowed tools;
4. learner question or expected mode;
5. proof step or construction under analysis;
6. expected obstacle / Required Property, if known;
7. what the current Skill gets wrong;
8. whether the issue concerns correctness, hindsight leakage, construction archaeology, CPG representation, pedagogy, or progressive disclosure.

## Design principle

Do not optimize ProofAtlas for reproducing a reference answer.

Optimize it for reconstructing a mathematically plausible and learnable search process while clearly separating structural reconstruction from historical claims.

## Core schema changes

Do not redesign the frozen CPG substrate merely for convenience.

A breaking change to stable identity, Claim/MathematicalEntity separation, scope visibility, first-class object families, assertion/event semantics, n-ary participant semantics, layer separation, causal ordering, or Entity/Mention separation should include:

- a concrete failing proof;
- why the current representation is insufficient;
- the minimal schema change;
- migration impact;
- a regression fixture.

Compatible new relation signatures or stricter validation rules are welcome when they obey the frozen core semantics.

## Product changes

For Integrated Skill changes, prefer evidence from:
- real proof corpora;
- learner-output failures;
- transfer failures;
- over-analysis;
- fidelity problems.

The next priority is implementation and evaluation above the frozen protocol, not further ontology expansion.

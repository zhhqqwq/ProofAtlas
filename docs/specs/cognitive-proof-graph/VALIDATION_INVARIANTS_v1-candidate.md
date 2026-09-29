# Cognitive Proof Graph v1 Candidate — Validation Invariants

The JSON Schema validates local structure. `tools/validate_cpg.py` validates graph-wide semantics.

## Structural invariants

1. Global IDs are unique across entities, scopes, relations, and mentions.
2. Root scope exists.
3. Scope parent links exist and form an acyclic hierarchy.
4. Every entity has an existing home scope.
5. Claim references resolve to existing entities.
6. Every relation type exists in the signature catalog.
7. Relation semantic mode and layer match its signature.
8. Participant roles and cardinalities satisfy the signature.
9. Participant endpoint kinds satisfy allowed type sets.
10. Event causal parents exist and are Event Relations.

## Scope invariants

11. Logical/search participants must be reasoning-visible in relation scope, except explicit produce/export/call/return rules.
12. Cross-layer archaeology mappings require graph addressability, not reasoning visibility.
13. Export changes visibility but not entity identity.
14. Sibling-route local objects do not become mutually visible without explicit import/export.

## Causality invariants

15. Event causal-parent graph is acyclic.
16. Absence of a causal edge does not assert independence.
17. Presentation order does not create search causal edges.

## Identity invariants

18. Mathematical equality does not merge entity IDs.
19. Surface mentions do not duplicate entity identities.
20. Contextual roles such as goal, candidate, artifact, and constraint do not create duplicate semantic objects.

## Presentation invariants

21. Mentions reference an entity and a PresentationSpan.
22. Presentation sequences contain only PresentationSpan IDs.
23. `compressed_into` requires a loss profile.
24. Reconstruction relations requiring fidelity must carry it.

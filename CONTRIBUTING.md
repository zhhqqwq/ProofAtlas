# Contributing to ProofAtlas

ProofAtlas is currently in pre-alpha and its specifications are intentionally open to revision.

## Good contributions right now

The highest-value contributions are not large feature PRs. They are small, auditable cases that reveal where the current proof-understanding protocol succeeds or fails.

Useful contributions include:

- a proof where the reference construction looks "magical";
- a case where multiple candidate constructions are equally reasonable;
- a case where the textbook reference is not the most natural blind route;
- a hidden theorem or theorem-role gap;
- a constant whose origin is pedagogically important;
- a failed attempt that reveals a real structural obstacle;
- a case where the current protocol invents hindsight motivation;
- a learner-level mismatch.

## Suggested issue format

Include:

1. theorem / exercise statement;
2. reference proof;
3. learner level and allowed tools;
4. the proof step or construction under analysis;
5. expected obstacle / required property, if known;
6. what the current protocol gets wrong;
7. whether the issue concerns correctness, hindsight leakage, pedagogy, or representation.

## Design principle

Do not optimize ProofAtlas for reproducing a reference answer. Optimize it for reconstructing a mathematically plausible and learnable search process while clearly separating structural reconstruction from historical claims.

## Specification changes

For core specification changes, prefer an issue or design note before a large implementation PR. The project is still defining Construction Archaeology and the Cognitive Proof Graph, so APIs and schemas are not stable yet.
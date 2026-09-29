# ProofAtlas CPG — Internal Protocol Freeze v1.0-rc1

## Decision

**FREEZE: `schema_version: 1.0-rc1` as the first stable internal CPG protocol.**

## Evidence

- 9 complete proof serializations validate.
- 6 deliberately invalid fixtures are rejected.
- Recursive ConstructionPolicy is structurally required.
- Child Episode call/return/export scope is validated.
- `min/max` merges use n-ary events.
- Constant provenance has a typed record.
- Causal independence is explicit when audited.
- Presentation order remains independent from search causality.
- Theorem preparation can be compressed without collapsing theorem/application/preparation semantics.
- No new top-level ontology family was required.

## Frozen boundary

Breaking changes require a schema version change if they alter:

- stable entity identity;
- Claim vs MathematicalEntity separation;
- scope visibility/export rules;
- first-class object families;
- Assertion vs Event semantics;
- role-based n-ary participants;
- logical/search/presentation layer separation;
- event causal partial order;
- Entity/Mention separation.

## Compatible additions

Compatible additions may include:

- optional metadata;
- new relation signatures obeying existing layer/mode semantics;
- new mathematical domain hints;
- stricter validators that reject records already semantically invalid under the frozen rules.

## Not frozen

- formula AST;
- graph database implementation;
- graph UI;
- learner annotation schema;
- proof-pattern ontology;
- complete mathematical type system;
- public API compatibility.

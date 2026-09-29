# ProofAtlas Part III — Cognitive Proof Graph v0.2
# Core Semantic Object Model

> Upstream: CPG Foundations v0.1  
> Goal: decide what deserves stable first-class identity, what is a relation/role, and what is metadata.

## First-classness rule

A concept should become a first-class graph object when it has several of:
- stable referential identity;
- independent lifecycle;
- participation in multiple relation types;
- independent scope;
- independent provenance;
- independent presentation fate.

If its essence is how A acts on B, prefer a relation/event. If it only describes one object/relation and need not be independently referenced, prefer metadata.

## Foundational distinction

\[
\boxed{Claim \neq MathematicalEntity}
\]

A MathematicalEntity is a referent: function, sequence, scalar, parameter, set, subsequence, bound, index, operator, witness, etc.

A Claim is a truth-apt proposition that can be given, assumed, required, proved, disproved, discharged, or used as a goal.

Example:
- \(f_N\) is a MathematicalEntity.
- “\(f_N\) is continuous” is a Claim referring to \(f_N\).

Without this distinction, object identity, properties, assumptions, goals, constraints, theorem premises, and conclusions collapse into one ambiguous node class.

## Locked first-class object families

### Semantic objects
- MathematicalEntity
- Claim

### Process objects
- Route
- Episode
- Unit
- ConstructionPolicy
- SearchSpace

### Knowledge object
- Theorem

### Presentation object
- PresentationSpan

The v0.1 substrate still includes Scope, Relation/Event, and Mention.

## Goal is a Claim role

\[
\boxed{Goal = Claim + contextual role}
\]

The same Claim can move from theorem goal to proved conclusion without being duplicated.

## Constraint is a Claim profile/role

A constraint such as \(\delta\le1\) is first a proposition. Its search function is contextual.

\[
\boxed{Constraint = Claim + constraint role/lifecycle}
\]

Constraint metadata/relations may record hard/route-enabling/simplifying/preference roles, lifecycle state, provenance, and scope.

Do not duplicate the proposition into a parallel Constraint ontology.

## Candidate is a role

A candidate may intrinsically be a MathematicalEntity, ConstructionPolicy, Theorem, or another supported search object.

\[
\boxed{Candidate = contextual role}
\]

Use candidate membership in a SearchSpace and a selection Event rather than a generic Candidate node.

## Artifact is a role

An artifact is whatever a Unit/Episode/Policy produces and a later process consumes. It may be a MathematicalEntity, Claim guarantee, SearchSpace, or ConstructionPolicy.

\[
\boxed{Artifact = produced/consumed role}
\]

The same \(f_N\) remains one MathematicalEntity while serving candidate, selected object, artifact, theorem input, and presentation referent roles.

## Constant is not a top-level ontology

A salient constant usually requires provenance of a choice/derivation event, not a distinct ontology object per occurrence.

Example:
- specialize \(r\) to \(1\);
- normalize \(C\) to \(1\).

The scalar value \(1\) may be shared mathematically while provenance differs by event.

\[
\boxed{
\text{value identity}
\neq
\text{value-choice provenance}
}
\]

Parameters/thresholds are MathematicalEntities. Constant Archaeology metadata belongs mainly on specialization, derivation, coarsening, budget, normalization, optimization, and merge events.

## Route

Route is first-class because it has high-level strategy identity, independent scope, lifecycle/status, root Episode, and alternative relations.

Reference route, valid blind alternative, and abandoned route remain separable.

## Episode

Episode is first-class because it is a coherent strategy phase with entry/exit, strategy identity, Unit containment, child call/return, lifecycle, and artifact I/O.

## Unit

Unit is first-class because it is the minimal local search obligation used by M3 and Construction Archaeology.

## ConstructionPolicy

Recursive constructions require explicit state, admissible choices, selection rule, invariant, progress measure, and generated artifact. This is needed for subsequences, nested intervals, diagonal constructions, and iterative witnesses.

## SearchSpace

Candidate Family is promoted to first-class SearchSpace because it needs stable identity, provenance, membership, freeze-before-reference audit, alternatives, and presentation fate.

SearchSpace may represent candidate, parameter, budget, or theorem-choice families.

## Theorem vs theorem application

Theorem is first-class reusable knowledge.

A concrete theorem application is an n-ary logical Event:

\[
(\text{Theorem},\text{premise Claims})
\to
\text{conclusion Claims}.
\]

Do not create a new Theorem node per application.

## PresentationSpan vs Mention

PresentationSpan is a stable sentence/formula/subexpression region and a target of compression/recovery mappings.

Mention is an occurrence of an Entity in a span.

\[
\boxed{PresentationSpan \neq Mention}
\]

## Branch

Local branch is normally Scope(kind=branch) plus search relations/status. If it grows into an independent high-level proof strategy, promote it to Route.

No generic Branch node family is required.

## Failure, obstacle, required property

- Failure: normally an event outcome + Claims.
- Required Property: usually a Claim role.
- Obstacle: either a Claim relation or Unit metadata when interpretive rather than truth-apt.

## First-class taxonomy

Entity
- SemanticEntity
  - MathematicalEntity
  - Claim
- ProcessObject
  - Route
  - Episode
  - Unit
  - ConstructionPolicy
  - SearchSpace
- KnowledgeObject
  - Theorem
- PresentationObject
  - PresentationSpan

Non-Entity substrate:
- Scope
- Relation/Event
- Mention

## Concepts deliberately represented as roles/profiles

Not top-level node types:
- Goal
- Constraint
- Candidate
- Artifact
- Constant
- Branch
- Failure
- TheoremApplication
- RequiredProperty
- TheoremInput
- Guarantee

## Object-model invariants

1. Claim/Object separation.
2. Contextual role does not create identity.
3. Process containers are distinct from Events.
4. Theorem identity is distinct from theorem application.
5. Value identity is distinct from choice provenance.
6. PresentationSpan is distinct from Mention.
7. SearchSpace has stable identity.
8. Local branches default to Scope, high-level alternatives to Route.

## Conclusion

The graph taxonomy must follow semantics, not English nouns.

\[
\boxed{
\text{Mathematical Objects}
\neq
\text{Truth Claims}
\neq
\text{Search Processes}
\neq
\text{Reusable Knowledge}
\neq
\text{Presentation Objects}
}
\]

and especially:

\[
\boxed{Claim \neq MathematicalEntity}
\]

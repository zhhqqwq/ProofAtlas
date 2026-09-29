# ProofAtlas Part III — Cognitive Proof Graph v0.3
# Relation & Event Semantics

> Upstream: CPG v0.1 Foundations + v0.2 Core Semantic Object Model  
> Goal: define edge/event meaning before freezing the machine schema.

## Core split

\[
\boxed{Assertion Relation \neq Event Relation}
\]

Assertion Relation means a semantic relation holds in a scope/layer, but no state transition is asserted.

Event Relation means an occurrence changes proof/search state, produces outputs, or changes lifecycle/visibility.

Both use the same Relation substrate but have different semantics.

## Canonical relation record

A Relation record contains:
- stable ID;
- semantic_mode = assertion or event;
- layer = logical, search, presentation, or cross_layer;
- relation_type;
- role-based participants;
- scope;
- evidence;
- confidence/fidelity;
- metadata.

Events additionally carry preconditions, outputs, causal parents, outcome, and state delta.

## Role-based n-ary participants

Do not force relations into source-to-target form.

Theorem application needs theorem + premises + conclusions. Merge needs multiple inputs + output. Role-based participants preserve joint-input semantics and enable cardinality/type validation.

## Primitive vs derived views

Store one canonical source of truth.

Examples:
- primitive establish_claim Event → derived proved_by view;
- primitive select Event → derived selected_by view;
- primitive produce Event → derived produced_by view.

Do not canonically store both directions if one can be derived.

## Generic depends_on is prohibited

The term is ambiguous.

Use:
- logically_depends_on for Claim proof support;
- Event causal_parents for reconstructed causality;
- presentation sequence / ordered_before for text order.

\[
\boxed{
\text{logical dependency}
\neq
\text{search causality}
\neq
\text{presentation order}
}
\]

## proves

Proves is not the canonical primitive. Use an establish_claim logical Event with actor/evidence/conclusion participants. proved_by is a derived view.

This prevents multiple independent sources of truth for proof status.

## select

select is a search Event connecting:
- selector Unit/Policy;
- SearchSpace;
- selected candidate.

It can carry M3 fidelity/rationale and changes search state.

## motivates

motivates is a search Assertion, not logical implication and not automatically historical fact.

It must support evidence and fidelity.

\[
\boxed{
\text{motivates}
\not\Rightarrow
\text{logical implication}
}
\]

## produce vs select

If a referent already exists in a SearchSpace and is accepted, use select.

If a process creates a new semantic object/Claim, use produce.

Example:
- choose \(f_N\) from approximants → select;
- define new \(g=f-id\) → produce.

## specialize vs strengthen

specialize reduces freedom / instantiates a family:

\[
r>0 \to r=1.
\]

strengthen replaces/adds a logically stronger sufficient Claim.

They are distinct Events.

## merge

merge is an n-ary Event.

Examples:

\[
N_1,N_2 \to N=\max\{N_1,N_2\},
\]

\[
\delta\le a,\ \delta\le b
\to
\delta\le\min\{a,b\}.
\]

## apply_theorem

apply_theorem is an n-ary logical Event:

- theorem;
- premise Claim(s);
- conclusion Claim(s).

The reusable Theorem identity is distinct from each application.

## Presentation mappings

presented_as is a cross-layer Assertion connecting semantic/search objects to PresentationSpans.

compressed_into maps many discovery/logical sources to one PresentationSpan and should carry a Compression Loss Profile.

hidden_from records omission from a presentation view.

recovered_from records reverse archaeology and must carry evidence/confidence/fidelity.

## Reasoning Visibility vs Graph Addressability

\[
\boxed{
\text{ReasoningVisible}
\neq
\text{GraphAddressable}
}
\]

A failed branch-local candidate may be unusable as a logical/search input in the parent scope but still graph-addressable so archaeology can record that it was deleted from the final proof.

Logical/search relations require reasoning visibility except explicit cross-scope operations such as call/return/export.

Presentation/cross-layer mappings may address closed or abandoned records, but this does not make them reasoning-visible.

## export

export is a cross-scope Event. It makes a child-local entity/Claim visible to an allowed ancestor without changing entity identity.

Export must not clone the referent.

## call and return

Search control Events:
- call: parent process invokes child process with explicit inputs;
- return: child returns explicit artifacts/guarantees.

## Constraint lifecycle events

Search Events operating on Claim constraints include:
- strengthen
- relax
- replace
- discharge
- abandon

replace need not imply stronger/weaker. discharge means an obligation is satisfied in the current context. abandon means search stops pursuing a route/process/regime and does not mean it is mathematically false.

## alternative_to

Search Assertion between routes, SearchSpaces, or candidates.

Possible metadata include:
- co_preferred;
- mutually_exclusive;
- equivalent_role;
- different_mechanism.

## Mathematical vs search membership

Do not overload member_of.

Use:
- math_member_of for mathematical set membership;
- candidate_in for SearchSpace membership.

## Equality

equal_to is a logical Assertion between MathematicalEntities. It never merges identity.

If equality itself is proof content, also retain the corresponding Claim.

## Event causality

Event instances form a causal partial order:

\[
(E,\prec)
\]

Primitive storage uses causal_parents.

The causal parent graph must be acyclic. Recursive ConstructionPolicy semantics live in the Policy; instantiated Event occurrences remain acyclic.

Absence of an edge does not prove independence.

## Presentation order

Presentation order is stored independently as an ordered list/sequence of PresentationSpan IDs. It does not create causal edges.

## Relation signatures

Every relation type has a machine-readable signature specifying:
- semantic_mode;
- layer;
- participant roles;
- allowed endpoint types;
- cardinalities;
- scope policy;
- causal flag;
- fidelity/loss requirements.

This catalog is the basis of schema validation.

## Core catalog

Logical assertions:
- logically_depends_on
- equal_to
- math_member_of

Logical events:
- establish_claim
- apply_theorem

Search assertions:
- goal_of
- required_by
- motivates
- candidate_in
- alternative_to
- obstacle_for

Search events:
- select
- produce
- specialize
- strengthen
- relax
- replace
- merge
- discharge
- reject
- abandon
- call
- return

Cross-scope event:
- export

Cross-layer assertions:
- presented_as
- compressed_into
- hidden_from
- recovered_from

## Validation rules

Every relation/event must pass:
1. known relation signature;
2. matching semantic mode;
3. matching layer;
4. required participant roles;
5. valid cardinalities;
6. allowed endpoint types;
7. scope visibility/addressability policy;
8. causal parent validity for Events;
9. no causal cycle;
10. required fidelity/loss metadata where applicable.

## Conclusion

\[
\boxed{
\text{Relation}
=
\text{typed, scoped, layered, role-based semantic record}
}
\]

\[
\boxed{
\text{Event}
=
\text{Relation with occurrence/state-transition semantics}
}
\]

The machine schema under schema/cognitive-proof-graph/v1 implements these semantics.

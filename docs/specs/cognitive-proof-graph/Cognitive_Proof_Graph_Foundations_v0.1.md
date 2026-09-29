# ProofAtlas Part III — Cognitive Proof Graph Foundations v0.1

> Status: foundational model  
> Inputs: Motivation Fidelity v1.0-rc1, Construction Archaeology v1.0-rc1  
> Scope: stable identity, scope semantics, and logical/search/presentation layer separation

## Core substrate

Before choosing node types, ProofAtlas first fixes the substrate:

\[
\boxed{Entity + Scope + Relation + Mention}
\]

Conceptually, the CPG is a scoped, attributed, multi-layer relational hypergraph.

## Stable entity identity

\[
\boxed{\text{Identity follows the referent, not the surface string}}
\]

The same \(f_N\) selected in search, returned as an artifact, used as a theorem input, and written in a formula retains one stable entity ID.

Conversely:
- same notation does not imply same entity;
- same value does not imply same provenance;
- proven equality does not merge entity IDs.

If a proof establishes \(L=M\), the graph retains two entities and records an equality relation.

## Entity vs Mention

\[
\boxed{Entity \neq Mention}
\]

Entity represents the referent. Mention represents one occurrence in a search, logical, presentation, or learner view.

Renaming/aliasing creates new mentions or aliases, not a duplicate semantic entity.

## Scope is not Episode

\[
\boxed{Scope \neq Episode}
\]

Episode is strategy organization. Scope is semantic visibility and assumption context.

A contradiction subproof may require its own scope even if it is not a new strategy Episode. An Episode need not create a new scope if it introduces no local assumptions or bindings.

## Scope visibility

Default rules:
- ancestor-visible records are visible downward;
- descendant-local records are not reasoning-visible upward unless explicitly exported/imported;
- sibling route objects do not leak across route scopes;
- shadowed symbols resolve through bindings/scope, not string equality.

Child/subproof return exports only the artifact/guarantee the parent may use. Export preserves identity; it does not clone entities.

## Three semantic layers

### Logical layer
What mathematically supports what?

### Search layer
Why was an object/route generated, selected, rejected, or revisited?

### Presentation layer
How did the polished proof display, compress, hide, or reorder the structure?

Core invariant:

\[
\boxed{
\text{Logical Dependency}
\neq
\text{Search Causality}
\neq
\text{Presentation Order}
}
\]

A textbook may announce a final \(\delta\) before verification even when reconstructed search causality runs in the opposite direction.

## Explicit cross-layer mapping

Sharing an entity ID across layers is not enough. Search-to-logical and discovery-to-presentation changes must be explicitly represented.

Examples:
- selected candidate later serves as theorem input;
- Construction Unit is compressed into a short choice phrase;
- proved Claim is presented as a formula;
- polished span is reverse-mapped to one or more possible discovery structures.

## Search causality is a partial order

Search events do not form a forced narrative timeline.

For independently generated thresholds:

\[
N_1 \parallel N_2
\]

then both may precede:

\[
N=\max\{N_1,N_2\}.
\]

A global next relation is therefore invalid as a model of discovery history.

## N-ary relation semantics

Many proof operations are inherently joint:

\[
(N_1,N_2) \to N,
\]

\[
(a,b,c) \to \delta=\min\{a,b,c\},
\]

\[
(\text{Theorem},\text{premises}) \to \text{conclusion}.
\]

The semantic model must preserve n-ary input/output structure. A backend may reify these as event nodes, but semantics cannot be reduced to unrelated binary edges.

## Locked foundation invariants

1. Stable identity across layers.
2. Mathematical equality does not merge identity.
3. Entity/Mention separation.
4. Scope visibility is explicit.
5. Upward visibility requires export/import.
6. Every relation has an explicit layer.
7. Cross-layer semantics are explicit.
8. Search causality is a partial order.
9. Presentation order is independent.
10. N-ary semantics are preserved.

## Minimal substrate

The minimal serialized substrate has four collections:
- entities
- scopes
- relations
- mentions

This is a semantic substrate, not yet the final schema.

## Deliberately postponed

v0.1 does not freeze:
- complete node taxonomy;
- formula AST;
- graph database;
- entity-resolution implementation;
- learner profile schema;
- UI layout;
- public API.

## Conclusion

The CPG should not begin as a colored graph of proof lines. It begins as:

\[
\boxed{
\text{stable entities}
+
\text{explicit scopes}
+
\text{typed multi-layer relations}
+
\text{surface mentions}
}
\]

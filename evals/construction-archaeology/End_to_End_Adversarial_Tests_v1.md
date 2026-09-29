# Construction Archaeology v1.0-rc1 — End-to-End Evaluation Summary

Construction Archaeology v0.1–v0.6 was integrated into v1.0-rc1 and tested on nine complete analysis proofs.

## Proofs

1. \(x^2\) continuity
2. \(1/x\) continuity
3. differentiable implies continuous
4. uniform limit preserves continuity
5. Heine–Cantor
6. limsup approximating subsequence
7. positive continuous function on compact set has a positive lower bound
8. interval self-map fixed point via IVT
9. uniqueness of sequence limits

## Pipeline tested

\[
\text{proof}
\to
\text{Units}
\to
\text{Episodes/Routes}
\to
\text{Constraint Ledger}
\to
\text{Constant Provenance}
\to
\text{Presentation Map}
\]

## Test-driven patches locked

### A. Episode Substance Gate
A local subproblem becomes a child Episode only if it has substantive internal structure: multiple meaningful Units, its own strategy/invariant, nontrivial call-return contract, or stand-alone proof-module character.

### B. Causal Partial Order
Discovery/constraint events are not forced into a unique chronology. Independent events can jointly feed later merges.

### C. Route object
Reference route, valid alternative route, and abandoned high-level route are separate.

### D. Witness origin
Fixed quantities distinguish:
- chosen
- derived
- existential_witness
- theorem_supplied
- inherited
- normalized

### E. Construction Policy
Recursive constructions preserve:
- state
- admissible choices
- selection rule
- invariant
- progress measure
- generated artifact

## Key schema requirements exposed

The tests require future CPG representations to separate:

\[
\boxed{
\text{Logical Dependency}
\neq
\text{Search Causality}
\neq
\text{Presentation Order}
}
\]

They also require stable entity identity, explicit scope, alternative routes, recursive policies, witness-origin metadata, and many-to-one presentation mappings.

## Result

No additional top-level theoretical layer was required. Construction Archaeology can be treated as an implementation release candidate while broader corpus evaluation continues.

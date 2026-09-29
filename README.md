# ProofAtlas

**ProofAtlas** is an open-source, pre-alpha AI skill for learning mathematical proofs by reconstructing the reasoning that polished proofs compress.

> **Don't just expand a proof. Reconstruct the reasoning the proof compressed.**

ProofAtlas is not primarily a theorem prover, proof rewriter, or answer generator. Its goal is to help learners understand **why a proof is structured the way it is**, including hidden steps, theorem roles, construction principles, "magic" constants, and the search process that can lead to a proof without pretending that the reference answer was inevitable.

## Status

**Pre-alpha / open design.** No claim of state-of-the-art performance or measured learning gains is made at this stage.

Three core layers now have implementation candidates:

- **Motivation Fidelity / M3 Search Protocol v1.0-rc1** — answer-independent reconstruction of why a construction could reasonably be tried.
- **Construction Archaeology v1.0-rc1** — end-to-end reconstruction of Units, Episodes, Routes, constraints, constants, construction policies, and Search-to-Presentation compression.
- **Cognitive Proof Graph schema 1.0-rc1** — a machine-verifiable scoped, layered, role-based relational representation; stress-tested on nine complete proofs and frozen as the first stable internal data protocol (public status remains v1 candidate / rc1).

## Why ProofAtlas?

A polished mathematical proof often hides the very information a learner needs most:

- Why was this auxiliary function introduced?
- Why insert and subtract this particular term?
- Why use this theorem here, and what does it accomplish globally?
- Where did constants such as `1/2`, `ε/3`, or `6` come from?
- Which parts are mathematically necessary, and which are merely convenient?
- What would happen if we solved the problem forward without preserving the final answer's elegance?
- Which failed attempts are genuinely informative rather than invented after the fact?

ProofAtlas treats these as first-class learning problems.

## Core architecture

### 1. Motivation Fidelity

Separates **why a step works** from **why one might reasonably try it**. Reference proofs are comparison targets, not search objectives.

### 2. Construction Archaeology

Recovers how a complete construction forms:

```text
Polished Proof
  → Construction Units
  → Construction Episodes / Routes
  → Constraint Ledger
  → Constant Provenance
  → Search-to-Presentation Map
```

### 3. Cognitive Proof Graph

The CPG is not a line-by-line proof graph. Its current substrate separates:

- stable mathematical entities from Claims;
- semantic entities from textual Mentions;
- scopes from strategy Episodes;
- logical dependency from search causality and presentation order;
- assertion relations from state-changing events.

The schema candidate lives at:

```text
schema/cognitive-proof-graph/v1/
```

It is stress-tested with nine complete proof serializations spanning epsilon-delta constructions, recursive subsequences, alternative routes, theorem preparation, min/max merges, and presentation compression, plus six deliberately invalid fixtures.

## Repository layout

```text
ProofAtlas/
├── docs/specs/
│   ├── motivation-fidelity/
│   ├── construction-archaeology/
│   └── cognitive-proof-graph/
├── schema/cognitive-proof-graph/v1/
├── examples/
│   ├── analysis/
│   └── cognitive-proof-graph/
├── evals/
│   ├── m3-adversarial/
│   ├── construction-archaeology/
│   └── cognitive-proof-graph/
└── skills/proof-understanding/SKILL.md
```

## Machine-verifiable CPG candidate

The schema package uses two validation layers:

1. **JSON Schema 2020-12** for local structure and types.
2. **Semantic validator** for global IDs, relation signatures, endpoint types/cardinality, scope visibility, references, and causal-DAG invariants.

This separation is intentional: graph-wide semantic invariants are not forced into JSON Schema when doing so would make the schema brittle or misleading.

## Evaluation philosophy

ProofAtlas should not be evaluated only by whether it reproduces a reference solution. Important questions include:

- Did it identify the real obstacle?
- Were Required Properties generated before candidate forms?
- Was the Candidate Family independent of the reference answer?
- Could a different valid route be preserved rather than suppressed?
- Were convenient constants distinguished from necessary ones?
- Did failed attempts provide information gain?
- Did the explanation help a learner recognize a reusable proof pattern?
- Does the machine representation preserve scope, identity, causality, and presentation compression without inventing a unique discovery history?

## Scope for the first research cycle

Initial focus:

- real / mathematical analysis;
- epsilon-delta arguments;
- continuity and uniform continuity;
- compactness and subsequences;
- error decomposition;
- auxiliary functions;
- threshold and constant construction;
- theorem-role explanations.

Later targets include linear algebra, abstract algebra, probability, topology, measure theory, functional analysis, and ODEs.

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## Contributing

The project is deliberately open-design. Contributions are especially welcome in adversarial proof examples, hindsight-leakage failures, full-proof graph serializations, schema review, proof-learning UX, and evaluation methodology.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).

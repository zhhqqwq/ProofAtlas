# ProofAtlas

**ProofAtlas** is an open-source, pre-alpha AI skill for learning mathematical proofs by reconstructing the reasoning that polished proofs compress.

> **Don't just expand a proof. Reconstruct the reasoning the proof compressed.**

ProofAtlas is not primarily a theorem prover, proof rewriter, or answer generator. Its goal is to help learners understand **why a proof is structured the way it is**, including hidden steps, theorem roles, construction principles, "magic" constants, and the search process that can lead to a proof without pretending that the reference answer was inevitable.

## Status

**Pre-alpha / open design.**

The most developed component is the **Motivation Fidelity / M3 Search Protocol**, which specifies how an AI should explain *why one might reasonably try a construction* without simply seeing the answer first and inventing a convincing story afterward.

Two major components are still under active design:

- **Construction Archaeology** — reconstructing how a full mathematical construction forms through constraints, candidate families, failures, parameter choices, and simplifications.
- **Cognitive Proof Graph** — a machine-readable representation of logical, motivational, strategic, theorem-role, construction, constraint, and constant-provenance relationships inside proofs.

No claim of state-of-the-art performance or measured learning gains is made at this stage.

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

## Core ideas

### Motivation Fidelity

Separate:

- **why a step works**, from
- **why someone might reasonably try it before seeing the answer**.

The current protocol uses an answer-independent search structure:

```text
Goal
  → Obstacle
  → Available Information
  → Required Property
  → Candidate Family
  → Candidate Pool
  → Candidate Selection
  → Local Test
  → Search-State Update
```

### No Hindsight Leakage

Reference proofs are evidence to compare against, not an optimization target. A candidate should not be called "natural" merely because it appears in the reference solution.

### Functional Before Form

Before proposing a concrete construction, describe what the unknown object must **do**.

### Family Before Instance

Before proposing a specific auxiliary function, bridge term, parameter, subsequence, or transformation, define the functional search space it belongs to.

### Discovery vs presentation

A construction can be natural to discover but ugly to present; another can be elegant to present but difficult to discover. ProofAtlas keeps these roles separate.

## Current repository layout

```text
ProofAtlas/
├── README.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── LICENSE
├── VERSION
├── docs/
│   └── specs/
│       └── motivation-fidelity/
├── skills/
│   └── proof-understanding/
│       └── SKILL.md
├── evals/
│   └── m3-adversarial/
├── examples/
│   └── analysis/
└── .github/
    └── ISSUE_TEMPLATE/
```

## Prototype skill

The first prototype lives at:

```text
skills/proof-understanding/SKILL.md
```

It currently focuses on reconstructing nontrivial proof moves without answer-centered hindsight bias. The skill is intentionally experimental and will change as real proof examples reveal failure modes.

## Evaluation philosophy

ProofAtlas should not be evaluated only by whether it reproduces a reference solution. Important questions include:

- Did it identify the real obstacle?
- Were Required Properties generated before candidate forms?
- Was the Candidate Family independent of the reference answer?
- Could a different valid route be preserved rather than suppressed?
- Were convenient constants distinguished from necessary ones?
- Did failed attempts provide information gain?
- Did the explanation help a learner recognize a reusable proof pattern?

The current adversarial test set covers nine analysis-style proof scenarios and deliberately includes cases where the reference solution is **not** the most natural blind choice.

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

The project is deliberately open-design. Contributions are especially welcome in:

- adversarial proof examples;
- hindsight-leakage failure cases;
- proof-learning UX;
- mathematical-analysis construction patterns;
- theorem-role taxonomies;
- evaluation methodology.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
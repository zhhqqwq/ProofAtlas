# ProofAtlas

**ProofAtlas** is an open-source, pre-alpha AI skill for learning mathematical proofs by reconstructing the reasoning that polished proofs compress.

> **Don't just expand a proof. Reconstruct the reasoning the proof compressed.**

ProofAtlas is not primarily a theorem prover, proof rewriter, or answer generator. Its goal is to help learners understand **why a proof is structured the way it is**, including hidden steps, theorem roles, construction principles, "magic" constants, and the search process that can lead to a proof without pretending that the reference answer was inevitable.

## Status

**Pre-alpha / open design.** No claim of state-of-the-art performance or measured learning gains is made at this stage.

The project now has three frozen/rc1 protocol layers, an integrated Skill candidate, and its first larger analysis corpus:

- **Motivation Fidelity / M3 Search Protocol v1.0-rc1** — answer-independent reconstruction of why a construction could reasonably be tried.
- **Construction Archaeology v1.0-rc1** — reconstruction of Units, Episodes, Routes, constraints, constants, policies, and Search-to-Presentation compression.
- **Cognitive Proof Graph schema 1.0-rc1** — machine-verifiable internal protocol; frozen as the first stable internal data protocol.
- **Integrated ProofAtlas Skill v0.2** — selective orchestrator combining the three layers with learner-facing progressive disclosure.
- **Analysis Integrated Corpus v0.1** — 40 canonical real-analysis proof cases with learner-facing explanations and failure-pressure annotations.
- **Analysis Integrated Corpus v0.2** — 18 perturbation/isomorphic pairs (36 public transfer cases), 8 learner-depth anchors, memorization-resistance gates, and a private 12-case hidden external slice with public hash commitments.

Public project status remains pre-alpha. CPG public status remains v1 candidate / rc1 rather than stable public v1.0.

## Integrated product pipeline

```text
Proof / learner question
  → Proof map + hotspot detection
  → Motivation Fidelity where discovery claims are needed
  → Construction Archaeology where construction history is nontrivial
  → Cognitive Proof Graph semantic handoff + validation
  → Learner-facing projection
```

The pipeline is selective: simple verification does not trigger full archaeology, and raw CPG records are internal by default.

## Analysis corpus and transfer layer

The canonical 40-case corpus lives under:

```text
corpus/analysis-integrated-v0.1/
```

The transfer/memorization-resistance layer lives under:

```text
corpus/analysis-integrated-v0.2/
```

It contains 40 proof cases spanning:

- sequences and limits;
- continuity and uniform continuity;
- compactness and subsequences;
- function sequences;
- series;
- ordered-real constructions.

Batch audit:

- **40/40** cases have complete learner-facing projection sections.
- Motivation calibration: **31 M3-provisional / 9 M2 / 0 automatic M3**.
- Automated structural annotation audit errors: **0**.

The absence of automatic M3 labels is intentional: canonical textbook proofs are not upgraded to M3 without sufficient memorization-resistance evidence.

The corpus exposed the highest recurring failure pressures as:

- over-archaeology;
- theorem black-boxing;
- magic-constant overclaim;
- over-M3 / canonical memorization;
- recursive policy under-specification;
- witness-origin confusion;
- quantifier / causal-order confusion;
- reference-route bias.

These observations produced:

- **Pattern Library v0.1** — mechanism-based rather than chapter-based.
- **Proof Understanding Benchmark Alpha** — failure-driven, initially 12-dimensional.

Corpus v0.2 adds:

- **18 canonical → perturbation → isomorphic transfer triads** (36 new public transfer cases);
- **8 proofs at beginner / standard / advanced learner depth** (24 learner-facing variants);
- **Memorization Resistance Protocol v0.1** — no automatic M3 promotion;
- **Benchmark dimensions B13–B16** for memorization resistance, structural transfer, route stability, and learner-depth adaptation;
- a **12-case private hidden external slice**, with only protocol and SHA-256 commitments published.

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

### Motivation Fidelity

Separates **why a step works** from **why one might reasonably try it**. Reference proofs are comparison targets, not search objectives.

### Construction Archaeology

```text
Polished Proof
  → Construction Units
  → Construction Episodes / Routes
  → Constraint Ledger
  → Constant Provenance
  → Search-to-Presentation Map
```

### Cognitive Proof Graph

The CPG separates:

- stable mathematical entities from Claims;
- semantic entities from textual Mentions;
- scopes from strategy Episodes;
- logical dependency from search causality and presentation order;
- assertion relations from state-changing events.

The frozen internal protocol lives at:

```text
schema/cognitive-proof-graph/v1/
```

### Integrated Skill v0.2

The current `skills/proof-understanding/SKILL.md` is the first integrated orchestrator.

Supported modes include:

- map
- diagnose
- expand
- motivate
- construct
- trace-constant
- theorem-role
- rederive
- compare
- teach
- verify
- quiz

## Corpus-derived Pattern Library

Current corpus-derived mechanisms include:

- bridge / intermediate object;
- localization;
- error budgets;
- min/max constraint merge;
- tail control + finite prefix;
- compactness extraction;
- recursive selection policy;
- near-extremal witness;
- bad-sequence construction from negation;
- theorem-input manufacturing;
- domination / scalarization;
- representation alignment / residualization;
- anchor conditions;
- periodic/subsequence decomposition.

See `patterns/PATTERN_LIBRARY_v0.1.md`.

## Benchmark Alpha

The benchmark is deliberately failure-driven rather than reference-match-only.

It currently defines 12 dimensions covering routing, hotspot detection, motivation fidelity, construction segmentation, provenance, theorem role, alternative routes, presentation compression, over-analysis control, learner explanation, transfer patterns, and internal semantic integrity.

See `benchmarks/PROOF_UNDERSTANDING_BENCHMARK_ALPHA.md`.

## Repository layout

```text
ProofAtlas/
├── docs/specs/
├── schema/cognitive-proof-graph/v1/
├── corpus/analysis-integrated-v0.1/
├── corpus/analysis-integrated-v0.2/
├── patterns/
├── benchmarks/
├── examples/
├── evals/
└── skills/proof-understanding/SKILL.md
```

## Current evaluation status

- M3 has dedicated adversarial tests.
- Construction Archaeology has nine end-to-end full-proof tests.
- CPG schema: **9/9 complete proof graphs VALID** and **6/6 invalid fixtures REJECTED**.
- Integrated Skill v0.2: **9/9 protocol-contract pipeline cases PASS**.
- Analysis Integrated Corpus v0.1: **40 canonical learner-facing cases**, structurally audited.
- Analysis Integrated Corpus v0.2: **18 transfer pairs / 36 public variants + 24 learner-depth projections**.
- Hidden external slice v0.1: **12 private cases**, integrity committed by public SHA-256 hashes.

The next phase is **not** another ontology pass or more canonical theorem accumulation. It should run the Skill blind on the v0.2 transfer pairs and hidden slice, perform human learner-facing review, and only then consider promoting selected M3-provisional cases.

## Scope for the first research cycle

Initial focus remains real / mathematical analysis. Expansion to other fields should follow only after the analysis corpus exposes stable product behavior.

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## Contributing

Contributions are especially welcome in real proof-corpus failures, hindsight-leakage cases, learner-output failures, transfer cases, pattern-library proposals grounded in repeated evidence, and evaluation methodology.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).

# ProofAtlas Roadmap

## v0.1 — Motivation Fidelity prototype

- [x] Define Motivation Fidelity levels and answer-independence principles.
- [x] Define M3 Search Model.
- [x] Specify Required Property synthesis.
- [x] Specify Candidate Family generation.
- [x] Specify Candidate Selection.
- [x] Integrate into M3 Search Protocol v1.0-rc1.
- [x] Run adversarial tests on analysis proofs.
- [x] Run Integrated Skill v0.2 across a 40-case real-analysis development corpus.
- [x] Collect first-pass failure pressures: over-analysis, theorem black-boxing, constant overclaim, policy under-specification, witness-origin confusion, causal-order confusion, and reference-route bias.
- [ ] Add perturbation/isomorphic cases sufficient to promote selected canonical cases from M3-provisional to M3.

## v0.2 — Construction Archaeology

- [x] Define Construction Unit segmentation.
- [x] Define Construction Episode formation and route separation.
- [x] Define event-sourced Constraint Ledger.
- [x] Define Constant Archaeology as provenance chains.
- [x] Define Search-to-Presentation mapping.
- [x] Integrate v0.1–v0.6 into Construction Archaeology Protocol v1.0-rc1.
- [x] Run nine end-to-end full-proof adversarial tests.
- [x] Exercise CA mechanisms across the 40-case integrated analysis corpus.
- [ ] Run targeted human review of Unit/Episode boundaries before stable public freeze.

## v0.3 — Cognitive Proof Graph

- [x] Define stable entity identity and Entity/Mention separation.
- [x] Define scope visibility, export, route and branch isolation.
- [x] Separate logical dependency, search causality, and presentation order.
- [x] Define Core Semantic Object Model (`Claim != MathematicalEntity`).
- [x] Define assertion/event relation semantics and n-ary participant roles.
- [x] Publish JSON Schema v1 candidate and relation-signature catalog.
- [x] Implement semantic validator.
- [x] Serialize and validate all nine Construction Archaeology proof cases.
- [x] Add invalid fixtures for major semantic failure classes.
- [x] Freeze `schema_version: 1.0-rc1` as the first stable internal CPG protocol.
- [ ] Add learner-aware annotations only when learner-output evaluation justifies them.

## v0.4 — Integrated Proof-understanding Skill

- [x] Integrate Motivation Fidelity, Construction Archaeology rc1, and CPG schema into `skills/proof-understanding/SKILL.md`.
- [x] Add progressive disclosure modes.
- [x] Run nine protocol-contract pipeline adversarial cases.
- [x] Build Analysis Integrated Corpus v0.1 with 40 complete proof cases.
- [x] Generate and structurally audit 40 learner-facing explanation records.
- [x] Derive Pattern Library v0.1 from repeated corpus mechanisms.
- [ ] Run human learner-facing review for clarity, calibration, cognitive load, and transfer value.
- [ ] Add learner-level variants for a selected subset.

## v0.5 — Benchmark

- [x] Design Proof Understanding Benchmark Alpha from observed failure pressures.
- [x] Define development / stress / evaluation slices for the 40 public cases.
- [x] Define 12 evaluation dimensions instead of a single reference-match score.
- [ ] Implement scoring scripts for machine-checkable dimensions.
- [ ] Build a hidden external evaluation set.
- [ ] Add perturbation/isomorphic pairs for Motivation Fidelity.
- [ ] Run human evaluation for explanation and transfer dimensions.
- [ ] Validate benchmark reliability before making comparative performance claims.

## v1.0 — First stable public release

A stable release should require evidence that the system improves proof comprehension without systematically fabricating discovery narratives, plus stable machine-readable representations, an integrated Skill tested across a broader corpus, and a benchmark with external/hidden evaluation.

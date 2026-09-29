# ProofAtlas Roadmap

## v0.1 — Motivation Fidelity prototype

- [x] Define Motivation Fidelity levels and answer-independence principles.
- [x] Define M3 Search Model.
- [x] Specify Required Property synthesis.
- [x] Specify Candidate Family generation.
- [x] Specify Candidate Selection.
- [x] Integrate into M3 Search Protocol v1.0-rc1.
- [x] Run adversarial tests on analysis proofs.
- [ ] Run the integrated skill on a larger real corpus.
- [ ] Collect false-M3, over-analysis, family-too-wide/narrow, and learner-level mismatch failures.

## v0.2 — Construction Archaeology

- [x] Define Construction Unit segmentation.
- [x] Define Construction Episode formation and route separation.
- [x] Define event-sourced Constraint Ledger.
- [x] Define Constant Archaeology as provenance chains.
- [x] Define Search-to-Presentation mapping.
- [x] Integrate v0.1–v0.6 into Construction Archaeology Protocol v1.0-rc1.
- [x] Run nine end-to-end full-proof adversarial tests.
- [ ] Run CA rc1 on a larger proof corpus before stable freeze.

## v0.3 — Cognitive Proof Graph

- [x] Define stable entity identity and Entity/Mention separation.
- [x] Define scope visibility, export, route and branch isolation.
- [x] Separate logical dependency, search causality, and presentation order.
- [x] Define Core Semantic Object Model (`Claim != MathematicalEntity`).
- [x] Define assertion/event relation semantics and n-ary participant roles.
- [x] Publish JSON Schema v1 candidate and relation-signature catalog.
- [x] Implement semantic validator for references, scope, signatures, cardinality, and causal DAG.
- [x] Serialize and validate three complete proofs.
- [x] Add invalid fixtures for generic `depends_on`, scope leakage, and causal cycles.\n- [x] Add stress-test fixtures for incomplete policies, invalid returns, and malformed provenance.\n- [x] Freeze `schema_version: 1.0-rc1` as the first stable internal CPG data protocol.
- [x] Expand schema validation to all nine Construction Archaeology proof cases.
- [ ] Add learner-aware annotations and proof-pattern objects only when evals justify them.

## v0.4 — Proof-understanding skill

- [ ] Integrate Motivation Fidelity, Construction Archaeology rc1, and CPG schema.
- [ ] Add progressive disclosure modes: map, diagnose, expand, motivate, construct, theorem-role, trace-constant, rederive, teach, quiz.
- [ ] Add analysis-focused pattern library.

## v0.5 — Benchmark

- [ ] Build Proof Understanding Benchmark.
- [ ] Measure gap recall / precision.
- [ ] Measure motivation fidelity and hindsight leakage.
- [ ] Measure construction explanation and constant provenance.
- [ ] Measure theorem-role recognition.
- [ ] Evaluate transfer to unseen but structurally related proofs.

## v1.0 — First stable public release

A stable release should require evidence that the system improves proof comprehension without systematically fabricating discovery narratives, plus stable machine-readable representations tested across a broader proof corpus.

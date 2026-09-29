# ProofAtlas Roadmap

## v0.1 — Motivation Fidelity prototype

- [x] Define Motivation Fidelity levels and answer-independence principles.
- [x] Define M3 Search Model.
- [x] Specify Required Property synthesis.
- [x] Specify Candidate Family generation.
- [x] Specify Candidate Selection.
- [x] Integrate into M3 Search Protocol v1 candidate.
- [x] Run initial adversarial tests on analysis proofs.
- [ ] Implement and run `proof-understanding` skill on a larger real corpus.
- [ ] Collect false-M3, over-analysis, family-too-wide, family-too-narrow, and learner-level mismatch failures.

## v0.2 — Construction Archaeology

- [ ] Define construction event model.
- [ ] Distinguish necessary structure, route-enabling choices, simplifications, and presentation polishing.
- [ ] Formalize constant evolution and provenance.
- [ ] Formalize informative failed branches.
- [ ] Support nested and recursive constructions.
- [ ] Produce a Construction Archaeology specification and eval set.

## v0.3 — Cognitive Proof Graph

- [ ] Define node types.
- [ ] Define logical, goal, motivation, strategy, theorem-role, construction, constraint, and constant-provenance edges.
- [ ] Separate proof graph from discovery graph while defining their links.
- [ ] Define learner-aware annotations.
- [ ] Publish machine-readable schema.

## v0.4 — Proof-understanding skill

- [ ] Integrate Motivation Fidelity, Construction Archaeology, and Cognitive Proof Graph.
- [ ] Add progressive disclosure modes: map, diagnose, expand, motivate, construct, theorem-role, trace-constant, rederive, teach, quiz.
- [ ] Add analysis-focused pattern library.

## v0.5 — Benchmark

- [ ] Build Proof Understanding Benchmark.
- [ ] Measure gap recall / precision.
- [ ] Measure motivation fidelity.
- [ ] Measure construction explanation and constant provenance.
- [ ] Measure theorem-role recognition.
- [ ] Evaluate transfer to unseen but structurally related proofs.

## v1.0 — First stable public release

A stable release should require evidence that the system improves proof comprehension without systematically fabricating discovery narratives.
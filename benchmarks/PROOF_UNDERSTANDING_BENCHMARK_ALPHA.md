# ProofAtlas Proof Understanding Benchmark Alpha

## Why this benchmark is failure-driven

The 40-case batch shows that a good benchmark should not reward only “correct final explanation”.

It must penalize:

- invented M3 stories;
- over-analysis of routine proofs;
- theorem black-boxing;
- magic-number mythology;
- missing recursive policies;
- quantifier-order mistakes;
- reference-route bias;
- learner output that exposes too much internal machinery.

## Splits

- **Development — 24 cases:** common mechanisms and low/intermediate complexity.
- **Stress — 8 cases:** recursive policies, quantifier negation, compactness contradiction, advanced theorem chains, geometric blocking.
- **Evaluation — 8 cases:** separate public evaluation slice.

The 40 public canonical cases remain development/evaluation material. Benchmark Alpha v0.2 adds 18 public perturbation/isomorphic pairs plus a 12-case private hidden external slice whose case/gold files are not committed to the public repository.

## Dimensions

### B1 Mode Routing
Choose the lowest sufficient mode/depth.

### B2 Cognitive Hotspot Detection
Precision and recall over annotated hotspots.

### B3 Motivation Fidelity
Calibrate M1/M2/M3-provisional/M3 and count hindsight-leak violations.

### B4 Construction Segmentation
Agreement on Unit boundaries around new search obligations.

### B5 Constraint & Constant Provenance
Recover specialization, coarsening, merges, witness origins and necessity calibration.

### B6 Theorem Role & Preparation
Separate theorem trigger, input manufacturing, application and local/global role.

### B7 Alternative Route Preservation
Preserve valid blind alternatives without reference bias.

### B8 Presentation Compression Recovery
Recover high-value hidden structure without claiming a unique history.

### B9 Over-Analysis Control
Use low-archaeology proofs as negative controls.

### B10 Learner-Facing Explanation
Human rubric: correctness, main-idea visibility, useful detail, clarity, no schema leakage.

### B11 Transfer Pattern Quality
Does the final pattern transfer to structurally related unseen proofs?

### B12 Internal Semantic Integrity
Count identity violations, scope leaks, false causal order and role/type confusion.

## Reporting

Do not initially collapse everything to one scalar.

Report:

[
(B1,ldots,B12)
]

plus hard violations for:

- hindsight leakage;
- mathematical error;
- scope leakage;
- fabricated historical claims.


## v0.2 transfer dimensions

### B13 Memorization Resistance
Canonical → parameter/surface perturbation → isomorphic transfer. Exact recovery of a canonical proof is not enough for M3 promotion.

### B14 Structural Transfer
Recover the stable mechanism signature when theorem surface, objects, constants, or representation change.

### B15 Route Stability Under Surface Change
Preserve the semantic route under harmless perturbations while allowing legitimate simplification when the isomorphic case removes a real constraint.

### B16 Learner-Depth Adaptation
Evaluate the same proof at beginner / standard / advanced depth without changing the mathematical core or leaking raw internal schema to beginners.

## Hidden external slice

The current private slice contains 12 real-analysis transfer cases.

Public files expose only:

- `HIDDEN_EXTERNAL_SLICE_PROTOCOL_v0.1.md`;
- `hidden_external_manifest.json` with SHA-256 commitments;
- evaluator/integrity tooling.

Publishing the hidden case text or gold annotations retires the slice.

## M3 promotion rule

No canonical `M3-provisional` case is automatically promoted.

Promotion requires successful perturbation and isomorphic transfer, no hindsight-leak hard violation, and human review of the discovery rationale.

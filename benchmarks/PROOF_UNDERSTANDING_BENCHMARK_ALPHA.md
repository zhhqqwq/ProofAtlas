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

A serious future benchmark should add a hidden external set rather than treating these 40 public cases as sufficient.

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

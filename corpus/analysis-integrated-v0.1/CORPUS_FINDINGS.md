# ProofAtlas Analysis Integrated Corpus v0.1 — Corpus Findings

## Batch result

- **40 complete real-analysis proof cases**
- **40/40** records contain all learner-facing sections
- automated annotation-completeness errors: **0**

## Motivation Fidelity calibration

[
oxed{
31 	ext{M3-provisional}
+
9 	ext{M2}
+
0 	ext{automatic M3}
}
]

This is intentional. Most cases are canonical textbook proofs, and the current batch does not contain enough perturbation/isomorphic evidence to justify upgrading them to M3.

The next corpus expansion should prioritize:

[
oxed{
	ext{canonical case}
+
	ext{parameter perturbation}
+
	ext{isomorphic novel case}
}
]

rather than simply adding more canonical proofs.

## Most recurrent mechanisms

Top recurring mechanisms include:

- min/max constraint merge
- tail control
- compactness extraction
- extremalization
- vanishing scales
- domination/scalarization
- bridge terms
- error budgets
- near-supremum witnesses
- recursive ConstructionPolicy
- normalization / representation change

This supports a **mechanism-based** Pattern Library rather than a chapter-based taxonomy.

## Highest recurring failure pressures

- over-archaeology
- theorem black-boxing
- convenient constants narrated as necessary
- over-M3 on canonical proofs
- recursive-policy under-specification
- witness-origin confusion
- quantifier / causal-order confusion
- reference-route bias

## Pattern Library decision

Pattern Library v0.1 is built around transferable mechanisms such as bridge objects, localization, error budgeting, min/max merge, compactness extraction, recursive selection, theorem-input manufacturing, domination, residualization and anchor conditions.

## Benchmark decision

Benchmark Alpha is failure-driven and multi-dimensional. Reference-answer agreement alone is insufficient because an explanation may be mathematically correct while still inventing motivation, over-analyzing routine steps, black-boxing theorem preparation, or suppressing valid alternative routes.

## What this corpus does not establish

It does not establish measured learning gains, learner preference, comparative superiority, M3-level historical truth, generalization beyond analysis, or benchmark reliability.

## Next corpus milestone

Recommended:

[
oxed{
	ext{Analysis Corpus v0.2}
=
40	ext{ current cases}
+
15	ext{–}20	ext{ perturbation/isomorphic pairs}
+
	ext{learner-level variants}
}
]

The purpose is to test memorization resistance, transfer, route stability under surface changes, mode/depth adaptation, and explanation compression for different learner levels.

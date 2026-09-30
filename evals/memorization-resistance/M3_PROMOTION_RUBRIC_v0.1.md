# ProofAtlas M3 Promotion Rubric v0.1

## Decisions

- `PROMOTE_M3`
- `KEEP_M3_PROVISIONAL`
- `DOWNGRADE_M2`
- `INVALID_EVIDENCE`

## Provenance gate

If evaluation provenance is not `sealed-hidden`, return `INVALID_EVIDENCE` before mathematical scoring.

## Promotion gates

All must pass:

1. Mathematical route is valid.
2. No hindsight/reference leakage.
3. Required Properties are candidate-independent.
4. Candidate Family is genuine or uniqueness is justified.
5. Hidden structural mechanism is recovered.
6. Any route change is semantically legitimate.
7. Constants and witnesses are correctly classified.
8. No historical overclaim.
9. Public perturbation/isomorphic evidence is compatible.
10. Human reviewer judges the rationale forward-reconstructible.

`PROMOTE_M3` requires all ten.

A high mechanism-match score, exact reference match, or polished learner explanation alone can never trigger M3 promotion.

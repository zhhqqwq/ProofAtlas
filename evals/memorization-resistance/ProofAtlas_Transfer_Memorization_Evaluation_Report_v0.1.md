# ProofAtlas Transfer & Memorization Evaluation Report v0.1

## Executive verdict

This is the first evaluation pass over Analysis Corpus v0.2.

The requested run cannot be certified as blind in the current evaluator context:

- the public transfer annotations were already readable in the current project context;
- the private hidden statements and gold were exposed in the same conversation/tool context before the requested run.

Therefore this report makes **no final M3 promotions**.

[
oxed{0	ext{ canonical anchors promoted from M3-provisional to M3}}
]

This is a methodological decision, not a claim that the 18 anchors failed structurally.

## Evidence classes

The report now distinguishes:

1. `public-development` — useful for evaluator/schema debugging, not memorization evidence;
2. `contaminated-hidden` — integrity may be verified, but unusable for M3 promotion;
3. `future-sealed-hidden` — eligible promotion evidence if the evaluator has never seen the gold.

Blindness is part of benchmark provenance.

## Benchmark bug found before scoring

The original v0.2 transfer records stored one pair-level expected mechanism set and implicitly reused it for both P and I variants.

That is too rigid. Isomorphic transfer may legitimately remove or replace part of a route.

Examples:

- AN-001: sequence-limit uniqueness uses `max`; function-limit uniqueness uses `min`.
- AN-004: a tail-only sup-norm boundedness statement no longer needs finite-prefix cleanup.
- AN-008: static supremum witnesses no longer require recursive subsequence compatibility.
- AN-013: sequence products use convergent-sequence boundedness rather than local function boundedness.
- AN-020: the sequential criterion for uniform continuity no longer needs compactness.
- AN-025: Lipschitz transfer removes the local-delta / N-before-delta layer.
- AN-031: direct convergence to a constant removes the uniform-Cauchy intermediate.

The corpus has therefore been patched to store **variant-specific expected mechanisms and route signatures**.

This gives the correct principle:

[
oxed{	ext{route stability}=	ext{semantic mechanism stability, not exact route identity}}
]

## Annotated integration sanity check

After the variant-specific patch, all 36 public variants are internally consistent with their corrected annotations.

This is an **annotation-conditioned sanity check**, not a blind model-performance score.

It establishes that the evaluator can represent:

- invariant mechanisms;
- changed constants;
- changed min/max interfaces;
- legitimate mechanism deletion;
- legitimate route simplification;
- theorem-interface transfer.

It does not establish memorization resistance.

## Hidden slice status

The existing 12-case hidden slice still matches its published SHA-256 commitments, so the files themselves were not altered.

However, evaluator isolation was lost because case statements and gold were exposed before the requested blind run.

The slice is therefore marked:

`retired_for_current_evaluation_context`

and:

`usable_for_m3_promotion = false`.

Cryptographic integrity is necessary but not sufficient for a blind benchmark.

## M3 promotion decision

### Promoted to M3

None.

### Why

The current protocol requires evidence that the reconstruction survives answer-independent perturbation and isomorphic transfer.

That evidence must be generated before the evaluator sees the gold.

The current context cannot satisfy that condition retroactively.

The revised promotion gate is:

[
oxed{
	ext{M3}
=
	ext{sealed P/I run}
+
	ext{no hindsight hard violation}
+
	ext{semantic route review}
+
	ext{human rationale review}
}
]

Exact reference reproduction is never sufficient.

## Required next run

A fresh evaluator context should receive only:

- Integrated ProofAtlas Skill v0.2;
- hidden problem statements;
- public scoring contract.

It must not receive:

- expected mechanisms;
- route signatures;
- reference proofs;
- gold learner explanations;
- this conversation's hidden-case generation trace.

Predictions must be committed before gold is opened.

Only after that run should selected anchors be promoted from M3-provisional to M3.

## Research significance

The most important result of this report is methodological:

> Memorization resistance requires evaluator isolation, not merely perturbed questions.

ProofAtlas should now track **evaluation provenance** alongside proof provenance.

A future benchmark result without an evidence-isolation status is not eligible for M3 promotion.

# ProofAtlas Analysis Corpus v0.2

[
oxed{
40	ext{ canonical cases}
+
18	ext{ perturbation/isomorphic pairs}
+
8	ext{ learner-depth anchors}
}
]

Each public pair contains:

- `P` — parameter / surface perturbation;
- `I` — isomorphic structural transfer.

Thus v0.2 adds **36 public transfer cases** without mainly adding more canonical textbook theorems.

## Research targets

- memorization resistance;
- structural transfer;
- route stability under surface change;
- same proof at different learner depths;
- hidden external generalization.

## Public contents

- `transfer_pairs.jsonl`
- `learner-depth/learner_depth_variants.jsonl`
- `../../evals/memorization-resistance/MEMORIZATION_RESISTANCE_PROTOCOL_v0.1.md`
- `../../evals/memorization-resistance/TRANSFER_FINDINGS_v0.1.md`
- `../../patterns/PATTERN_LIBRARY_v0.2_STABILITY_REPORT.md`
- `../../benchmarks/HIDDEN_EXTERNAL_SLICE_PROTOCOL_v0.1.md`
- `../../benchmarks/hidden_external_manifest.json`
- `../../benchmarks/benchmark_alpha_v0.2.json`

## M3 promotion policy

Canonical `M3-provisional` is not automatically promoted.

Promotion requires:

1. mechanism recovery on the canonical case;
2. parameter/surface perturbation success;
3. isomorphic transfer success;
4. no reference-specific constant overclaim;
5. no hindsight-leak hard violation;
6. human review.

## Hidden data

The project maintains a 12-case private hidden slice outside the public repository.

Only its protocol and SHA-256 commitments are public. Publishing the hidden case text or gold retires that slice.

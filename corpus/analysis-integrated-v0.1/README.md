# ProofAtlas Analysis Integrated Corpus v0.1

This corpus is the first batch built specifically for **Integrated ProofAtlas Skill v0.2**.

[
	ext{proof}
ightarrow
	ext{Skill routing}
ightarrow
	ext{hotspot analysis}
ightarrow
	ext{learner-facing explanation}
]

## Scope

- 40 complete real-analysis proof cases.
- 14 introductory, 17 intermediate, 9 advanced.
- Includes both construction-heavy cases and low-archaeology negative controls.
- Public development/evaluation corpus; not a hidden benchmark and not evidence of measured learner gains.

## Included project artifacts

- `CORPUS_INDEX.md` — case index and distribution.
- `PATTERN_LIBRARY_v0.1.md` — corpus-derived mechanism library.
- `FAILURE_PRESSURE_REPORT.md` — failure classes exposed by the batch.
- `PROOF_UNDERSTANDING_BENCHMARK_ALPHA.md` — benchmark design derived from those failures.
- `benchmark_alpha.json` — development/stress/evaluation splits and dimensions.
- `BATCH_GENERATION_AUDIT.md` — batch completeness/calibration audit.

The full structured JSONL corpus and all 40 learner-facing explanations are distributed in the project delivery package generated with this corpus version.

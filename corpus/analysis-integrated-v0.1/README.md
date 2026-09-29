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

## Structured data

The full 40-record corpus is versioned as four JSONL shards:

```text
data/
├── cases-01-10.jsonl
├── cases-11-20.jsonl
├── cases-21-30.jsonl
└── cases-31-40.jsonl
```

Every record includes:

- theorem / statement;
- reference proof skeleton;
- recommended Skill mode and depth;
- cognitive hotspots;
- pattern tags;
- Motivation Fidelity calibration;
- full learner-facing explanation;
- failure-pressure annotations.

## Corpus documentation

- `CORPUS_INDEX.md` — case index and distribution.
- `CORPUS_FINDINGS.md` — batch-level findings.
- `FAILURE_PRESSURE_REPORT.md` — failure classes exposed by the batch.
- `BATCH_GENERATION_AUDIT.md` — completeness/calibration audit.

Project-level outputs derived from this corpus:

- `../../patterns/PATTERN_LIBRARY_v0.1.md`
- `../../benchmarks/PROOF_UNDERSTANDING_BENCHMARK_ALPHA.md`
- `../../benchmarks/benchmark_alpha.json`

## Status

This is a **development / evaluation corpus**.

The current public cases should not be treated as a permanent hidden benchmark. The next expansion should emphasize perturbation/isomorphic pairs and learner-level variants rather than merely adding more canonical textbook proofs.

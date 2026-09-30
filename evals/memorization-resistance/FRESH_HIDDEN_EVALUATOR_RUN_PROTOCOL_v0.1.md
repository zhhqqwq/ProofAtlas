# ProofAtlas Fresh Hidden Evaluator Run Protocol v0.1

## Purpose

This protocol defines the first evaluation procedure eligible to promote a ProofAtlas reconstruction from `M3-provisional` to final `M3`.

The evaluator must be isolated from hidden gold before predictions are frozen.

## Evidence states

- `public-development`
- `sealed-hidden`
- `contaminated-hidden`
- `retired`

Only `sealed-hidden` is eligible for M3-promotion evidence.

## Required roles

1. **Fresh Evaluator** — receives Integrated ProofAtlas Skill v0.2, hidden problem statements, public instructions, and prediction schema only.
2. **Committer** — freezes predictions and records SHA-256.
3. **Scorer** — may open hidden gold only after the prediction commitment exists.
4. **Human Promotion Reviewer** — reviews only cases that pass the structured gates.

## Required order

[
oxed{
	ext{Fresh Context}
ightarrow
	ext{Hidden Statements}
ightarrow
	ext{Predictions}
ightarrow
	ext{Prediction Commitment}
ightarrow
	ext{Open Gold}
ightarrow
	ext{Score}
ightarrow
	ext{Human Review}
ightarrow
	ext{M3 Decision}
}
]

If gold is opened before prediction commitment, the run is invalid.

## Fresh-context rule

A new conversation is necessary but not sufficient.

The evaluator must not inherit hidden gold from:

- project context;
- connected files;
- memory;
- copied prompts;
- prior transcripts;
- tool-visible gold artifacts.

The run manifest must attest that no hidden gold source was available before commitment.

## Required prediction fields

For every hidden case:

- proof map;
- cognitive hotspot;
- pre-construction state;
- obstacle;
- Required Properties;
- Candidate Family;
- selected route;
- local test;
- predicted mechanisms;
- semantic route signature;
- constant / witness calibration;
- learner-facing explanation;
- proposed fidelity: M1 / M2 / M3-provisional only;
- confidence and uncertainty.

The evaluator may decline to reconstruct motivation if evidence is insufficient.

## Prediction freeze

After the final hidden case:

1. serialize all predictions;
2. validate required fields;
3. write the prediction file;
4. calculate SHA-256;
5. create a run manifest containing the hash;
6. do not modify the committed prediction file.

Any correction requires a new run ID and new commitment.

## Gold opening

Gold may be opened only after commitment.

The scoring record must include:

- prediction SHA-256;
- hidden-gold SHA-256;
- benchmark version;
- scorer version;
- evaluation provenance.

## Hard gates

- H1 Mathematical validity
- H2 No hindsight leakage
- H3 Required-Property independence
- H4 Genuine Candidate Family or justified uniqueness
- H5 Structural mechanism transfer
- H6 Legitimate semantic route
- H7 Correct constant / witness calibration
- H8 No historical overclaim
- H9 Compatible public P/I evidence
- H10 Human reviewer judges the rationale forward-reconstructible

## M3 promotion

A canonical M3-provisional item is promotable only when:

1. its public perturbation / isomorphic evidence passes;
2. a genuinely sealed hidden transfer case tests the same mechanism family;
3. all hard gates pass;
4. human review approves the discovery rationale.

Without sealed evaluation provenance, final M3 is prohibited.

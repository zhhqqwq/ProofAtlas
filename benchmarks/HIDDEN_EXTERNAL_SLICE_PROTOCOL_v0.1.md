# Hidden External Benchmark Slice Protocol v0.1

## Public/hidden separation

The public repository contains:

- evaluator contract;
- case count;
- benchmark dimensions;
- SHA-256 commitments;
- contamination/retirement policy.

It does **not** contain:

- hidden case statements;
- hidden expected mechanisms;
- hidden route signatures;
- hidden gold explanations.

## Current slice

- 12 hidden real-analysis transfer cases.
- Each changes theorem surface while reusing mechanisms from the public corpus.
- No hidden case is a verbatim duplicate of a canonical case.
- Gold fidelity ceiling is `M3-provisional` unless additional answer-independence evidence is gathered during evaluation.

## Integrity

Before evaluation, hash the private files and compare with the public manifest.

If hidden case text or gold is published, used in development prompts, or manually tuned against, retire the slice and create a replacement.

## Reporting

Report hidden results separately from public development/stress performance.

Hidden benchmark performance is not evidence of learner gains without human learner studies.

# M3 Adversarial Evaluation Set

The current integrated specification has been challenged on nine analysis-style proof scenarios:

1. continuous self-map of an interval has a fixed point — canonical-proof memory risk;
2. uniform convergence with moving inputs — bridge-term selection;
3. epsilon-delta proof for `x^2` — polished constant leakage;
4. epsilon-delta proof for `1/x` — localization and the "magic" `1/2`;
5. differentiability implies continuity — forced candidate / uniqueness;
6. Heine-Cantor theorem — bad-sequence construction and arbitrary `1/n` choice;
7. subsequence approaching `limsup` — recursive candidate policy;
8. positive continuous function on a compact set — reference answer intentionally not the blind-preferred route;
9. uniform limit preserves continuity — nested M3 searches.

The detailed test traces are in:

`docs/specs/motivation-fidelity/M3_Search_Protocol_v1_Integration_and_Adversarial_Tests.md`

## Eval principle

A test does **not** pass merely because the model reproduces the reference answer. It should preserve alternative valid discovery routes and distinguish ex-ante discovery evidence from ex-post proof elegance.

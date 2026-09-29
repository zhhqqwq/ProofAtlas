---
name: proof-understanding
description: >
  Use when a learner wants to understand an existing mathematical proof, especially
  nontrivial constructions, hidden steps, auxiliary objects, parameter choices,
  theorem roles, bridge terms, subsequences, error decompositions, or why a proof
  move might reasonably be discovered. Prioritize answer-independent reconstruction
  over post-hoc storytelling.
---

# Proof Understanding — pre-alpha prototype

## Purpose

Help the learner understand compressed mathematical proofs by reconstructing the mathematical search structure that can lead to important proof moves.

Do not merely paraphrase the reference proof. Do not pretend to know the author's historical thought process unless a source explicitly documents it.

## Core distinction

Always separate:

- **Why it works** — why the final step is valid.
- **Why one might try it** — why this candidate could reasonably arise before seeing the answer.

If only the first can be justified, say so. Do not manufacture an M3 discovery story.

Use this protocol whenever the task is to explain **why a nontrivial mathematical construction, auxiliary object, parameter choice, decomposition, subsequence, or proof move might reasonably be discovered**.

## Core rule

Do not reason backward from the reference answer. Reconstruct an answer-independent search path from the mathematical state that existed immediately before the construction.

## Protocol

1. Freeze the pre-construction state: current goal, exact obstacle, available facts, available tools, current constraints, and learner-available proof patterns.
2. Exclude the reference construction, future lemmas, polished constants, and future success information from candidate generation.
3. Normalize the goal only through answer-independent transformations.
4. State why the current information does not already prove the goal.
5. Identify the remaining degree of freedom: what object, parameter, subsequence, decomposition, transformation, witness, or construction policy is still available to choose?
6. Derive **Required Properties before candidate forms**. Describe what the unknown must do, not what it must look like.
7. Give each Required Property a provenance: goal, obstacle, available interface, legitimately triggered theorem, existing constraint, or representation need.
8. Label each requirement as `hard`, `route-enabling`, `simplifying`, or `preference`. Never present a convenient choice as necessary.
9. Remove candidate names and reference-specific constants. If the requirements cease to make sense, treat them as answer-contaminated.
10. From the audited requirements, infer object type, interface signature, and mechanism, then define a **functional Candidate Family**.
11. Define the family before generating instances. Never create a fake family by adding arbitrary parameters to the reference answer.
12. A family should normally retain real freedom. If requirements force a unique candidate, explicitly derive uniqueness.
13. Freeze the Candidate Family before reference comparison.
14. Generate a small blind shortlist, normally 2–5 candidates. Candidate sources may be structural, heuristic, backward-from-goal, probe, or uniqueness-forced; record the source.
15. Call a candidate “natural” only for explicit reasons such as direct interface match, reuse of existing objects, little new structure, immediate testability, or learner accessibility.
16. Reject candidates that fail family membership, information legality, learner-knowledge legality, hard requirement coverage, reference independence, or mathematical well-formedness.
17. Compare remaining candidates without an opaque total score. Prefer, where appropriate: requirement coverage, access to available tools, structural economy, reasonable proof cost, useful information gain, and pedagogical value.
18. Distinguish `discovery simplicity`, `proof simplicity`, `expression elegance`, and `pedagogical simplicity`. Do not use later elegance as evidence of earlier discoverability.
19. Allow co-preferred candidates and `underdetermined`. Never force the reference candidate to win.
20. Freeze shortlist, criteria, and selection before inspecting the reference construction.
21. Locally test the selected candidate against the Required Properties. Full proof completion is not required here.
22. Retain a failed candidate only if it had prior justification and yields information gain: a new obstacle, constraint, required property, eliminated family, reduced parameter range, or tool mismatch.
23. Permit nested M3 searches when one successful construction creates another local construction problem.
24. Permit candidates that are **construction policies**, not only static formulas, for recursive objects such as subsequences, nested intervals, and diagonal selections.
25. If an existence theorem guarantees a suitable member and no explicit formula is needed, allow existential selection instead of inventing a witness.
26. Use search economy: narrow semantically before enumerating. Brute-force expression search is not an M3 discovery explanation.
27. For canonical textbook proofs, masked recovery alone is not strong M3 evidence. Prefer parameter perturbations, isomorphic novel problems, alternate references, or mechanism-level tests.
28. Compare with the reference only after blind selection is frozen.
29. If an independently selected route differs from the reference but works, preserve it as a valid discovery route. Do not revise the search history to make the reference inevitable.
30. If only “why it works” is defensible, report M1/M2 rather than manufacturing an M3 story.
31. Do not claim the author's historical thought process without external evidence. M3 is a reconstructible structural/pedagogical search path.
32. The objective is not to reproduce the reference answer. The objective is to make a plausible, answer-independent mathematical search process visible and learnable.

## M3 gate

Label a motivation `M3` only when all of the following hold:

- a pre-answer state is available;
- the obstacle is explicit;
- Required Properties are candidate-independent;
- the Candidate Family is reference-independent;
- candidate selection is blind to reference privilege;
- the chosen candidate receives a local test;
- failures, if shown, have information gain;
- canonical-proof memorization risk has been challenged by perturbation, isomorphism, alternate reference, or equivalent evidence;
- uncertainty and alternative routes are calibrated honestly.

If all structural gates pass but memorization resistance has not been tested, use `M3-provisional`.

## Reference comparison labels

After blind selection is frozen, classify the relation to the reference as one of:

- `reference_match`
- `family_match`
- `alternative_valid_route`
- `reference_superior_ex_post`
- `reference_unexplained`

Never retroactively change selection criteria merely to upgrade the reference answer.
## Student-facing explanation

Do not dump the full internal audit by default. Prefer progressive disclosure:

1. **Proof map** — what the proof is trying to accomplish.
2. **Cognitive hotspot** — the step that most needs explanation.
3. **Why it works** — mathematical validity.
4. **Why one might try it** — answer-independent reconstruction, if defensible.
5. **Alternatives** — only when they are genuinely useful.
6. **Transfer pattern** — what reusable proof idea the learner should take away.

For important theorem uses, explain both the local role and the global role of the theorem, and identify the larger mathematical idea when useful.

For important constants, distinguish necessary values from convenient values and, when feasible, show a forward derivation that may produce uglier but valid choices before explaining the polished textbook constant.

## Calibration

Use `M3-provisional` rather than `M3` for canonical proofs when memorization resistance has not been challenged by perturbation, isomorphism, alternate reference, or comparable evidence.

If a reference construction cannot be independently recovered, say that it is currently explainable only post hoc rather than inventing a discovery narrative.

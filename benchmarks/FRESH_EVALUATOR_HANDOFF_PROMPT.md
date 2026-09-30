# Fresh Evaluator Handoff Prompt

You are evaluating ProofAtlas Integrated Skill v0.2 on a sealed hidden analysis-proof slice.

Use only the hidden **problem statements** supplied to this evaluator context.

Do not search for, request, inspect, or infer hidden gold annotations, expected mechanisms, route signatures, reference proofs, prior hidden-run scoring, or prior transcripts containing those materials.

For every case:

1. build a compact proof map;
2. identify the cognitive hotspot;
3. freeze a pre-construction state;
4. state the obstacle;
5. derive Required Properties before naming the final construction;
6. give a genuine Candidate Family when applicable;
7. select and locally test a route;
8. identify predicted mechanisms;
9. give a semantic route signature;
10. distinguish chosen / derived / existential / convenient constants or witnesses;
11. give a learner-facing explanation;
12. calibrate fidelity only as M1, M2, or M3-provisional.

Never assign final M3 during blind generation.

Do not optimize for matching a canonical textbook proof. Preserve valid alternative routes.

If discovery motivation cannot be reconstructed answer-independently, lower the fidelity estimate.

At the end emit one prediction file conforming to `fresh_hidden_prediction_schema_v0.1.json`.

After emitting it, do not revise predictions using gold or scoring information.

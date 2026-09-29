# ProofAtlas — Integrated Skill v0.2 Integration Specification

## Product milestone

Integrated Skill v0.2 is the first ProofAtlas version in which the three previously independent research layers become one product pipeline:

Motivation Fidelity
→ Construction Archaeology
→ Cognitive Proof Graph
→ Learner-facing Explanation

This is not a fixed full-depth run for every question. The Skill is an orchestrator that invokes only the layers needed by the user's intent and the proof's cognitive hotspots.

## Runtime stages

### Stage 0 — Intent and depth

Infer:
- user intent;
- requested mode;
- learner level if available;
- whether the request is about validity, motivation, construction, constants, theorem role, or teaching;
- minimum useful depth.

### Stage 1 — Proof map

Create a compact strategy map before deep analysis.

### Stage 2 — Hotspot detection

Identify construction, theorem, strategy, and conceptual hotspots. Routine derivation stays compressed.

### Stage 3 — Local Motivation Fidelity

Run M3 only where the explanation wants to claim why one might reasonably try a move.

### Stage 4 — Construction Archaeology

Run CA only where multiple choices, constraints, constants, branches, policies, or presentation compression interact.

### Stage 5 — CPG semantic handoff

Represent significant objects and relations internally using the frozen Cognitive Proof Graph semantics.

The graph is the consistency/audit layer, not the learner-facing format.

### Stage 6 — Validation

Audit:
- identity;
- scope;
- layer separation;
- causal order;
- ConstructionPolicy completeness;
- constant provenance;
- fidelity.

### Stage 7 — Learner projection

Produce only the structure useful for the current learner and mode.

## Selective internal depth

A proof such as differentiable implies continuous has one important representation move and almost no Constant Archaeology.

A limsup subsequence proof requires a recursive ConstructionPolicy.

Uniform-limit continuity benefits from bridge analysis, error budgeting, and threshold ordering.

Therefore Integrated Skill v0.2 must support adaptive internal depth rather than impose the same trace on every proof.

## Conceptual orchestration state

The pipeline may be viewed as passing forward:

    proofatlas_state:
      request:
        mode:
        depth:
        learner_context:

      proof_map:
        goal:
        phases:
        theorem_interfaces:
        hotspots:

      motivation_records:
        - hotspot:
          fidelity:
          obstacle:
          required_properties:
          search_space:
          selection:
          local_test:

      construction_archaeology:
        routes:
        episodes:
        units:
        policies:
        constraint_events:
        constant_provenance:
        presentation_mappings:

      cpg:
        schema_version: 1.0-rc1
        validation_status:

      learner_projection:
        sections:
        omitted_internal_detail:

This is an orchestration contract, not a replacement for the formal CPG schema.

## Failure policy

If M3 fails:
- downgrade the motivation explanation;
- do not block a valid Why-It-Works explanation.

If CA reconstruction is ambiguous:
- preserve multiple plausible preimages or use a lower-confidence structural explanation.

If CPG audit detects a scope, identity, or causal conflict:
- repair the reconstruction before presenting it;
- if unresolved, omit the unsupported discovery claim.

If the learner asks only for simple verification:
- do not expose the full integrated pipeline.

## Product acceptance gates

Integrated Skill v0.2 should satisfy:

1. Mode routing — narrow questions do not trigger unnecessary archaeology.
2. M3 isolation — discovery claims use Motivation Fidelity; verification claims do not borrow M3 language.
3. CA selectivity — routine algebra does not become Units.
4. No fidelity inflation — CA never upgrades weak M3.
5. CPG identity — repeated mathematical referents remain stable.
6. Scope safety — branch/child-local assumptions do not leak.
7. Alternative preservation — valid blind alternative Routes survive.
8. Constant calibration — convenient values are not labeled necessary.
9. Theorem preparation — important theorem-input manufacturing is not hidden behind theorem names.
10. Progressive disclosure — learner output is simpler than internal representation.
11. Transfer value — deep explanations end with a reusable pattern where appropriate.
12. Stop discipline — explanation stops when additional archaeology no longer helps.

## Product boundary

Integrated Skill v0.2 does not require:
- graph visualization;
- a graph database;
- formula AST;
- learner profile persistence;
- automatic theorem proving;
- public API;
- a complete proof-pattern ontology.

The milestone succeeds when the existing protocols operate as one coherent teaching workflow.

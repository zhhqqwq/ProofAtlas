---
name: proof-understanding
description: >
  Use when a learner wants to understand an existing mathematical proof, diagnose
  hidden reasoning gaps, reconstruct why a nontrivial proof move could reasonably
  be discovered, trace auxiliary constructions and constants, explain theorem roles,
  compare routes, or learn reusable proof patterns. Use Motivation Fidelity for local
  discovery claims, Construction Archaeology for multi-step construction histories,
  and the Cognitive Proof Graph internally to preserve identity, scope, causality,
  alternatives, and presentation compression. Prefer progressive disclosure over
  dumping internal structure.
---

# ProofAtlas — Integrated Proof Understanding Skill v0.2

## Mission

Help learners understand what a polished proof compresses.

Recover, when useful:

- proof structure;
- hidden logical steps;
- theorem roles;
- construction hotspots;
- auxiliary objects and bridge terms;
- parameter and constant provenance;
- constraint evolution;
- alternative routes;
- informative failures;
- search-to-presentation compression;
- transferable proof patterns.

Do not merely paraphrase the reference proof.

Do not claim to recover an author's historical thought process without source evidence.

## Architecture

Use the following layered pipeline selectively:

Motivation Fidelity
→ Construction Archaeology
→ Cognitive Proof Graph
→ Learner-facing Projection

The pipeline is not a mandatory full run for every question.

### Motivation Fidelity owns

- pre-construction state;
- obstacle;
- Required Properties;
- Candidate Family / SearchSpace;
- blind candidate generation and selection;
- local test;
- M1 / M2 / M3-provisional / M3 calibration.

### Construction Archaeology owns

- Construction Units;
- Episodes and Routes;
- Construction Policies;
- Constraint Ledger;
- Constant provenance;
- informative branches;
- Search-to-Presentation mapping.

### Cognitive Proof Graph owns internally

- stable entity identity;
- Claim vs MathematicalEntity separation;
- scopes and visibility;
- assertion vs event relations;
- logical/search/presentation separation;
- causal partial order;
- cross-layer mappings;
- presentation Mentions.

Do not expose raw graph records to ordinary learners unless explicitly requested.

### Learner-facing Projection owns

Turning the audited structure into the smallest useful explanation for the learner.

## Core invariants

Never violate these distinctions:

- Why It Works != Why One Might Try It.
- Reference Answer != Search Objective.
- Claim != MathematicalEntity.
- Logical Dependency != Search Causality != Presentation Order.
- Reasoning Visibility != Graph Addressability.
- Contextual Role != Intrinsic Identity.
- No new choice => no new Construction Unit.

## Mode router

Infer the narrowest useful mode from the learner's request. The learner does not need to name a mode.

Supported modes:

- map
- diagnose
- expand
- motivate
- construct
- trace-constant
- theorem-role
- rederive
- compare
- teach
- verify
- quiz

### map

Return the proof stages, main strategy, key theorem roles, and at most a few cognitive hotspots. Do not run full archaeology unless needed.

### diagnose

Identify the smallest missing layer: algebra, hidden theorem, hidden condition, missing lemma, motivation, strategy, concept, main-idea burial, theorem role, or analytic idea.

### expand

Expand compressed validity reasoning. Do not manufacture discovery motivation unless the learner also asks why the move was tried.

### motivate

Run Motivation Fidelity for the local construction.

### construct

Explain how an auxiliary function, bridge, subsequence, parameter, decomposition, witness, or policy can be built. Use M3 locally and CA when multiple decisions interact.

### trace-constant

Trace salient thresholds, epsilon splits, min/max choices, localization constants, and normalization factors from functional need to polished form.

### theorem-role

Explain the theorem trigger, preconditions, local role, global role, structural transformation, removal effect, mathematical idea, and transfer pattern.

### rederive

Hide polished choices as search inputs. Allow ugly or nonoptimal valid forms. Compare with the reference only after the forward route is frozen.

### compare

Compare proof routes by mechanism, assumptions, theorem dependence, search commitments, construction cost, pedagogical visibility, and presentation compression. Do not force a universal winner.

### teach

Default integrated teaching mode. Use progressive disclosure and invoke deep protocols only at important hotspots.

### verify

Check validity and hidden assumptions. Do not automatically infer discovery motivation.

### quiz

Ask learner-facing questions derived from the audited structure. Do not reveal raw graph/debug records.

## Input normalization

Identify when available:

- theorem or exercise statement;
- reference proof;
- learner question;
- learner level;
- allowed theorems/tools;
- requested depth;
- whether the request concerns validity, discovery, or both.

If learner level is unknown, use the apparent proof level and explain prerequisites only when relevant.

Do not ask for information that is unnecessary to make useful progress.

## Proof map first

Before deep analysis, form a compact map:

Goal
→ major transformation
→ theorem/construction phases
→ conclusion

Identify the main strategy, theorem interfaces, construction hotspots, and likely presentation compression.

This map is not yet a discovery reconstruction.

## Cognitive hotspot gate

Run deep Construction Archaeology only for genuine construction hotspots such as:

- auxiliary object;
- bridge term;
- nontrivial parameter or threshold;
- subsequence / diagonal / nested selection;
- error decomposition or budget;
- theorem-input manufacturing;
- bad-object / contradiction witness;
- localization;
- min/max merge;
- salient magic constant;
- normalization;
- major representation change;
- informative branch or retry.

Routine algebra, deterministic substitution, standard inequalities, and routine theorem verification normally remain compressed.

## Motivation Fidelity — local M3 protocol

When explaining why a nontrivial move might be tried:

1. Freeze the pre-construction state: goal, obstacle, available facts, allowed tools, active constraints, and learner-available proof patterns.
2. Exclude the final construction, polished constants, future lemmas, and future success information.
3. Identify the remaining degree of freedom.
4. Derive Required Properties before candidate form.
5. Give Required Properties provenance: goal, obstacle, interface, theorem, constraint, or representation.
6. Label requirements as hard, route-enabling, simplifying, or preference.
7. Remove candidate names and answer-specific constants as an answer-leak audit.
8. Define a functional Candidate Family before instances.
9. Generate a small blind shortlist, normally 2–5 candidates.
10. Preserve co-preferred or underdetermined choices.
11. Select without reference privilege.
12. Locally test the candidate.
13. Retain failed candidates only when they had prior justification and information gain.
14. Compare to the reference only after the search decision is frozen.

Use:

- M1: post-hoc utility only;
- M2: structurally plausible;
- M3-provisional: forward-reconstructible but memorization resistance not adequately tested;
- M3: all M3 gates including answer-independence and memorization challenge pass.

Historical support is separate.

Never raise a local M-level merely because CA later makes the whole story coherent.

## Construction Unit segmentation

A Construction Unit is one locally coherent search obligation.

Start a new Unit when there is a meaningful new:

- degree of freedom;
- local goal;
- obstacle;
- independent constraint choice;
- candidate family;
- branch/retry;
- nested construction.

Do not split merely because there is a new formula line.

Use counterfactual separability: if A is fixed, can B be independently replaced by another legal choice while the local proof remains meaningful? If yes, they tend to be separate Units.

Close a Unit once the choice has been tested, the proof state has updated, and continuing requires either a new search obligation or only routine derivation.

## Episode and Route formation

An Episode is one coherent strategy phase.

Use high-level goal, strategy commitment, artifact flow, invariant, and exit condition to group Units.

Do not make one Episode per Unit.

Promote a local subproblem to a child Episode only if it has real substance, such as multiple meaningful Units, an independent strategy, its own invariant, a nontrivial call/return contract, or reasonable standalone modularity.

Use separate Routes for genuinely alternative high-level strategies. Preserve a valid blind alternative route even when it differs from the reference.

## ConstructionPolicy

Use a first-class ConstructionPolicy for recursive constructions such as subsequences, nested intervals, diagonal selections, and iterative approximation.

A policy must expose:

- state;
- admissible choices;
- selection rule;
- invariant;
- progress measure;
- generated artifact.

Do not reduce a recursive construction to only its final sequence or object.

## Constraint Ledger

Record only search-significant constraints: those that restrict candidate space, activate a theorem, maintain an invariant, create a parameter choice, reject a branch, explain a salient constant, or participate in merge/replace.

Keep separate:

- provenance;
- search role;
- logical strength;
- scope;
- lifecycle.

Do not conflate redundant, discharged, abandoned, and out-of-scope.

Support introduce, strengthen, specialize, relax, replace, merge, discharge, abandon, scope exit, and conflict detection.

Search/event order is a causal partial order, not a fabricated total chronology.

## Constant Archaeology

For salient constants only, use Need Before Number.

Trace as applicable:

functional need
→ parameter/search family
→ constraint
→ specialization
→ coarsening
→ derived value
→ merge
→ normalization
→ polished constant

Separate:

- value necessity;
- role necessity;
- route necessity;
- optimality.

Do not call a convenient feasible value optimal without evidence.

Do not create fake parameter families around the reference number.

Distinguish origins:

- chosen;
- derived;
- existential witness;
- theorem supplied;
- inherited;
- normalized.

Backward provenance does not establish forward discovery motivation. Use M3 if claiming why someone might choose the value.

## Search-to-Presentation Map

Treat the polished proof as a projection of richer internal structure.

Allow:

- many-to-one compression;
- one-to-many presentation;
- hidden structure;
- reordered structure;
- deleted branches;
- presentation-only notation.

Words such as “take”, “let”, “clearly”, theorem names, min/max, and sudden constants are inspection triggers, not evidence of a unique hidden history.

Reverse archaeology may have multiple supported preimages.

Use reconstruction confidence:

- forced;
- strong;
- plausible;
- speculative.

Do not present speculative recovery as fact.

## Internal Cognitive Proof Graph handoff

For nontrivial construction analysis, maintain an internal representation compatible with CPG schema_version 1.0-rc1.

Stable substrate:

- Entity
- Scope
- Relation/Event
- Mention

First-class object families:

- MathematicalEntity
- Claim
- Route
- Episode
- Unit
- ConstructionPolicy
- SearchSpace
- Theorem
- PresentationSpan

Roles such as goal, constraint, candidate, artifact, witness, theorem input, and returned guarantee must not duplicate underlying identity.

## CPG integrity rules

Keep the same MathematicalEntity identity when the same referent moves across candidate selection, artifact flow, theorem input, and presentation mentions.

Do not merge two entities merely because they are mathematically equal.

Use a Claim for a truth-apt proposition.

For example:

- f_N is a MathematicalEntity.
- “f_N is continuous” is a Claim.

Scope rules:

- ancestor information may be visible downward;
- child/branch-local information is not visible upward without export/import;
- sibling-route artifacts are isolated;
- archaeology may address hidden or closed records without making them available for reasoning.

Relation rules:

- assertion relation != event relation;
- logical/search/presentation layers stay distinct;
- theorem application is an n-ary logical event;
- min/max merge is an n-ary event;
- event causal parents form an acyclic partial order;
- absence of a causal edge does not prove independence.

## Internal validation gate

Before relying on a reconstructed structure for a deep learner explanation, audit:

1. stable identity;
2. Claim/object separation;
3. scope visibility;
4. route isolation;
5. relation layer;
6. assertion/event distinction;
7. participant roles/cardinality;
8. causal acyclicity;
9. ConstructionPolicy completeness;
10. constant provenance consistency;
11. presentation/search order separation;
12. fidelity calibration.

If a reconstruction violates these invariants, repair or downgrade it before presenting it.

Do not invent graph structure merely to make the representation complete.

## Theorem Role Analysis

For important theorem uses, explain as relevant:

- theorem interface;
- required preconditions;
- mapping from current facts to those preconditions;
- local role;
- global role;
- trigger signal;
- why the theorem is structurally useful;
- what breaks if it is removed;
- mathematical idea;
- transfer pattern.

Separate theorem preparation from theorem invocation.

A polished phrase such as “By IVT” may compress substantial work constructing the theorem's inputs.

## Learner-facing projection

Do not reveal the raw internal audit by default.

Prefer:

1. Proof Map — main stages.
2. Cognitive Hotspot — the step carrying the main construction burden.
3. Why It Works — mathematical validity.
4. Why One Might Try It — only when Motivation Fidelity supports the claim.
5. Construction Lineage — goal → obstacle → required property → choice → constraint → result.
6. Constants / Constraints — only salient ones.
7. What the Textbook Compressed — 1–3 high-value compression points.
8. Transfer Pattern — reusable idea for the next proof.

## Depth control

Use the lowest sufficient depth.

### L1 — Quick

Use for maps, simple diagnosis, theorem-role questions, and ordinary clarification.

### L2 — Teaching — default

Use selected Units, the main Episode, important constraints/constants, one or more justified M3 reconstructions, and useful presentation compression.

### L3 — Research / Archaeology

Use only when the user asks for deep reconstruction, design work, comparison, or audit. May include Routes, branches, nested M3, full constraint history, ConstructionPolicy, constant provenance, CPG-level audit, and alternative preimages.

## Stop rules

Stop decompression when:

- remaining steps are routine derivation;
- no new search-significant constraint appears;
- salient constants have been explained;
- theorem preparation has been exposed enough;
- further structure adds little transfer value;
- the learner's actual question is already answered.

Maximal detail is not the same as good teaching.

## Integrated audit

Before finalizing a deep explanation, check:

### Fidelity
- Did any motivation use the reference answer as a search input?
- Was any M-level inflated?

### Construction
- Are Units based on search obligations?
- Are Episodes strategy phases rather than arbitrary groups?
- Are child Episodes substantive?
- Are valid alternative Routes preserved?

### Constraints / constants
- Are convenient conditions mislabeled as necessary?
- Is constant provenance non-fake?
- Are existential witnesses distinguished from chosen parameters?

### Graph integrity
- Are identities stable?
- Is scope respected?
- Are logical/search/presentation relations separated?
- Is causality a partial order rather than an invented chronology?

### Pedagogy
- Is the main proof idea still visible?
- Did the explanation answer the learner's question?
- Did internal machinery leak unnecessarily?

## Output calibration

Never say “This is exactly how the author thought” unless a source establishes it.

Prefer:

- “A forward-reconstructible reason to try this is…”
- “Structurally, the step is motivated by…”
- “One plausible search route is…”
- “The proof text compresses the following constraints…”
- “This constant is convenient rather than forced.”

When reconstruction is underdetermined, say so.

## Integrated product rule

The internal protocols exist to improve the learner-facing explanation, not to make the learner read a schema.

Use Motivation Fidelity to control discovery claims.

Use Construction Archaeology to recover formation history.

Use the CPG to preserve semantic consistency.

Then teach only the useful structure.

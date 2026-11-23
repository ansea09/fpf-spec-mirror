---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__002_problem-frame.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:1 — Problem frame"
line_start: 66411
line_end: 66432
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "A.6.5"
  - "A.6.REL"
  - "B.3"
  - "C.22"
  - "C.22.2"
  - "E.18.1"
  - "E.23"
  - "G.11"
keywords:
---

### C.22.PFR:1 - Problem frame

**Use this when.** Use this pattern when an actual condition may be adverse for one entity and use, and a receiving claim needs to distinguish the actual Problem from a signal, criterion description, evaluation, assessment claim, ProblemCard, or claim that no suitable method is currently known.

**First useful move.** Name the actual-condition relation. Then name the predicate, entity, scope, and interval for which that predicate applies. If the condition falls on the adverse side of that applicable predicate, say plainly: "This condition is a problem for this entity in this scope." Expose a PFR occurrence only when another claim needs that Problem identity.

**What goes wrong if missed.** A card or evaluation result is allowed to create a Problem; the same criterion is applied to the wrong entity or scope; a new description edition creates a false new Problem; or one continuously adverse episode is split every time evidence is sampled. Conversely, two adverse episodes separated by actual non-adverse behavior collapse into one occurrence.

**What this buys.** Actual Problems can exist before discovery, can be referenced while still ongoing, and can be distinguished across repeated adverse episodes. One applicability relation supplies the predicate, problem-for entity, claim scope, and declared criterion-applicability window used by PFR; its actual occurrence extent is separately derived from uninterrupted obtaining. Measurements, evaluations, evidence, claims, cards, and method search remain available without becoming Problem identity.

**Battery example.** A technician needs to know whether a vehicle may be released for its intended start. Recover the release rule, its battery and load conditions, and what the available reading establishes under those conditions. A bound wholly below the permitted voltage can settle that decision. A different question arises if a service history must identify the particular low-voltage episode. That use needs an actual voltage-state relation with defined participants, conditions of occurrence and temporal identity. The reading, alarm and report can support the claim about the battery. The formal PFR occurrence remains unresolved while those grounds are missing.

Once such a governor exists, the applicability relation can connect its selected voltage predicate to the vehicle, intended-start `U.ClaimScope`, and declared criterion-applicability window; discovering a method still changes solvability rather than PFR actuality.

**Use another pattern when.** Use `C.22.2` when the current object is a problem-side card, signal, hypothesis, forecast, scenario, anticipated-condition claim, or reviewable formulation rather than an actual PFR.

Use `C.27` when a rate, rhythm, recovery, or regime claim is being used to change action, `C.28` when causal support is at issue, or the direct forecast, scenario, counterfactual, or anticipated-condition governor when that claim is current.

Use the selected A.19 comparison, `G.4` acceptance, state, gate, or measurement pattern when the current question is how to evaluate or support the adverse predicate.

Use `E.18.1`, `E.23`, and the direct NQD or OEE patterns for repeated problematization, search, work, evaluation, and continuation.


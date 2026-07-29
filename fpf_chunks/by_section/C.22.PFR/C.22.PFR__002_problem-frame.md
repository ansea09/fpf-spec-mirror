---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__002_problem-frame.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:1 — Problem frame"
line_start: 51314
line_end: 51327
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
  - "actual adverse condition"
  - "actual adverse episode"
  - "assessment and evidence separation"
  - "condition-to-predicate input rule"
  - "exact problem-for entity and use"
  - "independent criterion-applicability relation"
---

### C.22.PFR:1 - Problem frame

**Use this when.** Use this pattern when an actual condition may be adverse for one exact entity and use, and a receiving claim needs to distinguish the actual Problem from a signal, criterion description, evaluation, assessment claim, ProblemCard, or claim that no suitable method is currently known.

**First useful move.** Name the actual-condition relation. Then name the exact predicate, entity, scope, and interval for which that predicate applies. If the condition falls on the adverse side of that applicable predicate, say plainly: "This condition is a problem for this entity in this scope." Expose a PFR occurrence only when another claim needs that Problem identity.

**What goes wrong if missed.** A card or evaluation result is allowed to create a Problem; the same criterion is applied to the wrong entity or scope; a new description edition creates a false new Problem; or one continuously adverse episode is split every time evidence is sampled. Conversely, two adverse episodes separated by actual non-adverse behavior collapse into one occurrence.

**What this buys.** Actual Problems can exist before discovery, can be referenced while still ongoing, and can be distinguished across repeated adverse episodes. One exact applicability relation supplies the predicate, problem-for entity, claim scope, and declared criterion-applicability window used by PFR; its actual occurrence extent is separately derived from uninterrupted obtaining. Measurements, evaluations, evidence, claims, cards, and method search remain available without becoming Problem identity.

**Early battery contrast.** A battery-voltage condition below the applicable vehicle-start bound can already participate in an actual PFR before anyone notices it. A later maintenance card is an episteme describing that condition and Problem; writing or accepting the card creates neither. Discovering a supported charging or replacement method changes present solvability, not the still-adverse condition. Only actual change of the condition, loss of criterion applicability, or cessation of adverse predicate truth ends that PFR.

**Not this pattern when.** Use `C.22.2` when the current object is a problem-side card, signal, hypothesis, forecast, scenario, anticipated-condition claim, or reviewable formulation rather than an actual PFR. Use `C.27`, `C.28`, or the exact direct forecast, scenario, counterfactual, or anticipated-condition governor when that claim is current. Use the selected A.19 comparison, `G.4` acceptance, state, gate, or measurement pattern when the current question is how to evaluate or support the adverse predicate. Use `E.18.1`, `E.23`, and the direct NQD or OEE patterns for repeated problematization, search, work, evaluation, and continuation.


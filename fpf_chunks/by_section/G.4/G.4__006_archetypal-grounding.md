---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__006_archetypal-grounding.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:5 — Archetypal Grounding"
line_start: 99585
line_end: 99615
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.18"
  - "A.19"
  - "A.2.1"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.23"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.6"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CAL Pack@CG-Frame"
  - "Context charter"
  - "acceptance clause"
  - "legal flow"
  - "pass \\"
  - "typed operator card"
---

### G.4:5 - Archetypal Grounding

**Tell.** A CG‑Frame must choose and justify a set of candidate methods (possibly a selected set or archive) under explicit legality, evidence, and scope constraints. CHR provides the typed measurement basis; CAL declares auditable predicates and flows that separately grounded runtime work may apply.

**Show 1 (in‑context CAL pack skeleton).**
Context: R&D selected-set choice. CHR defines `SafetyClass(ord↑)`, `CostUSD_2026(ratio↓)`, `Readiness(nominal)`.

* `CAL.Operator: DominatesPareto`
  Signature over CHR types, precondition references CHR guard macros.
* `CAL.AcceptanceClause: AC_SafetyGate`
  Typed predicate binding `SafetyClass` (and its levels) with Context‑local thresholds; unknown handling uses tri‑state pins.
* `CAL.Flow: Flow_ParetoPortfolio`
  Produces a selected-set result kind; gates by `AC_SafetyGate` and `AC_Budget`.
* `CAL.EvidenceProfile: EP_SafetyEvidence`
  Declares anchor ids and freshness policy pins required for `SCR`.

Downstream, `G.5` consumes only the handoff manifest: clause ids, operator ids, and evidence profile ids (no embedded thresholds).

**Show 2 (explicit cross‑context import).**
A `SafetyClass` value is imported from a different Context or plane. CAL may still author an acceptance clause using that value, but only after the reuse is made explicit as a published crossing bundle and the CAL artifacts cite the relevant ids/pins. The CAL pack remains Context‑local; portability is achieved through explicit crossings and citations, not by silently widening scope.

**Show 3 (one performed acceptance evaluation).**

A dated Work occurrence `EvalWork-2026-07-30-17` has `SafetyEvaluatorSystem-17` as its actual performer, enacts exact `SafetyAcceptanceMethod`, occurs within `SafetyEvaluationTeamSystem-17`, and binds candidate `C-17` plus the current C.16 measurement-result episteme to `AC_SafetyGate` through the declared `A.6.1` operation application. The performer and containing System are independently admitted.

Because this worked case says that the Work was performed under an assignment, its local work context admits kind `SafetyAcceptanceEvaluatorSystemRole` under A.2 and declares `SafetyAcceptanceEvaluationAssignment` as a `U.SystemRoleAssignment` species under A.2.1. The species defines holder, assigned-kind, and evaluation-candidate participant meanings. Its rule appoints the holder to evaluate that candidate under the applicable safety-acceptance clause; one occurrence lasts for the maximal uninterrupted interval in which the predicate remains true for fixed values.

Occurrence `SafetyAcceptanceEvaluationAssignment-17` has `SafetyEvaluatorSystem-17` as holder, `SafetyAcceptanceEvaluatorSystemRole` as assigned-kind value, and `C-17` as evaluation candidate. It covers the Work interval. The holder is the performer, and the case establishes that this Work was performed under this assignment, so the F.6 relation obtains for that pair. A different overlapping assignment held by the same performer would not establish this attribution.

The C.16 episteme states the measured safety characteristic, scale, attributed value, uncertainty, model, calibration, and measurement Work; it is neither the raw detector output nor the acceptance verdict. The clause application obtains `unknown` because the uncertainty interval crosses the threshold. A separate C.2.1 episteme asserts that exact verdict and cites its provenance under A.10 and, when the EvidenceGraph extension is present, G.6; G.11 supplies currentness. A later C.11 result may record `defer`, and its claim uses the verdict episteme through an exact premise or decision-use relation. Any decision-making Work remains separate. The clause card, proof-ledger row, evidence edge, and decision record do not retroactively establish the measurement Work or the evaluation occurrence.


---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__006_archetypal-grounding.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:5 — Archetypal Grounding"
line_start: 100001
line_end: 100025
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.18"
  - "A.19"
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

A dated work occurrence `EvalWork-2026-07-30-17` has a performer through `U.RoleAssignment`, enacts `SafetyAcceptanceMethod`, and binds candidate `C-17` plus the current C.16 measurement-result episteme to `AC_SafetyGate` through the declared `A.6.1` operation application. The C.16 episteme states the measured safety characteristic, scale, attributed value, uncertainty, model, calibration, and measurement work; it is neither the raw detector output nor the acceptance verdict. The clause application obtains `unknown` because the uncertainty interval crosses the threshold. A separate C.2.1 episteme asserts that exact verdict and cites its A.10/G.6 provenance; G.11 supplies currentness. Later C.11 decision work binds that episteme as a premise and records defer. The clause card, proof-ledger row, evidence edge, and decision record do not retroactively establish the measurement work or the evaluation occurrence.


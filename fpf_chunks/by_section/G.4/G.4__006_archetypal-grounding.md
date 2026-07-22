---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__006_archetypal-grounding.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:5 — Archetypal Grounding"
line_start: 95774
line_end: 95794
dependencies:
  - "A.10"
  - "A.18"
  - "A.19"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
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
  - "CAL authoring"
  - "RSCRTriggerKindId"
  - "acceptance clauses"
  - "admissibility gates"
  - "edition pins"
  - "evidence profiles"
  - "operators"
  - "tri-state admissibility"
  - "Γ-fold hooks"
  - "Φ/Ψ/Φ_plane policy pins"
---

### G.4:5 - Archetypal Grounding

**Tell.** A CG‑Frame must choose and justify a set of candidate methods (possibly a selected set or archive) under explicit legality, evidence, and scope constraints. CHR provides the typed measurement basis; CAL turns it into executable, auditable predicates and flows.

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


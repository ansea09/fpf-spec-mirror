---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__005_forces.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:3 — Forces"
line_start: 33626
line_end: 33633
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "ConstraintValidity"
  - "Eulerian"
  - "GateFit"
  - "MVPK"
  - "PathSlice"
  - "Sentinel"
  - "SquareLaw"
  - "TransformationFlowStructure"
  - "flow"
---

### A.20:3 - Forces

* **Separation of concerns.** Internal mechanism laws are distinct from external `GateProfile` fit.
* **Auditability.** MVPK faces include pins and references only; no new numeric claims; editions and Γ are pinned where applicable.
* **Graph discipline.** One edge kind; all crossings mediated by gates; SquareLaw on every crossing.
* **Reproducible valuation.** Flow = valuation over `U.Transfer`, with slice‑local refresh bounded by sentinels.
* **LEX hygiene.** ASCII Tech labels, twin Tech and Plain registers, registered tokens.


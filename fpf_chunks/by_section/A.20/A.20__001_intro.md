---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__001_intro.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:intro — Intro"
line_start: 33757
line_end: 33767
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

## A.20 - Flow Constraint Validity — Eulerian

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative for flow valuations used by `E.18` `TransformationFlowStructure` under the Eulerian operational interpretation.

**Tech-name.** `FlowConstraintValidity` for transformation-flow valuations
**Plain-name.** Flow constraint validity (Eulerian interpretation)

**E.24.UK settlement.** A.20 does not admit `U.Flow` or `U.Flow.ConstraintValidity` as durable U-kinds. It governs the non-U constraint-validity relation for E.18 transformation-flow valuations. `U.Transfer` remains the single relation kind selected by E.18; `FlowConstraintValidity` is a pattern-local technical label for the step-local CV claim, status, and witness discipline.


---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism: Law-Governed Operation Algebra over a Subject Kind"
section_id: "A.6.1:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__011_rationale.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.6.1 — U.Mechanism: Law-Governed Operation Algebra over a Subject Kind"
  - "A.6.1:10 — Rationale"
line_start: 9602
line_end: 9607
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "B.3"
  - "C.16"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.18"
  - "E.20"
  - "F.18"
  - "U.BoundedContext"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "AdmissibilityConditions"
  - "Bridge‑only"
  - "LawSet"
  - "Mechanism"
  - "OperationAlgebra"
  - "Transport"
---

### A.6.1:10 - Rationale

Mechanisms need a kernel shape because many FPF practices declare reusable operation families: scope operations, normalization operations, selector operations, comparison operations, publication operations, and scoring operations. Without one shape, each practice invents local vocabulary for operations, laws, guards, reuse, and realization.

Binding mechanisms to A.6.0 Signature discipline keeps declaration and realization separate. The Signature carries boundary semantics; realization varies under monotonicity. Bridge-only transport and Reliability-only penalties keep cross-context losses visible without mutating Formality or Guarantee.


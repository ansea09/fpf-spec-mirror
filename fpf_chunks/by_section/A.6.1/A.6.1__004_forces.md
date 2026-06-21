---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
section_id: "A.6.1:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__004_forces.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.6.1 — U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
  - "A.6.1:3 — Forces"
line_start: 10378
line_end: 10388
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

### A.6.1:3 - Forces

| Force | Tension |
| --- | --- |
| Locality and transport | Semantics are context-local, but mechanisms often need explicit cross-context or cross-plane use. Transport must be Bridge-only, and penalties belong in Reliability. |
| Expressivity and compliance | Rich operation algebras must stay within characteristic-space, measurement, comparison, and unit-compliance rules. |
| Time determinacy | Admissibility predicates often depend on time, but implicit "latest" assumptions make reuse unreplayable. |
| Slot clarity and specialization depth | Multi-level specialization needs stable SlotKinds and monotone ValueKind narrowing; positional parameters are not enough. |
| Signature hygiene | Imported signatures must remain opaque; mechanisms use `imports`, `provides`, and ClaimIds rather than redeclaring foreign laws. |
| Method and mechanism proximity | The same project phrase can point to a method, method description, mechanism, work plan, dated work, or evidence value; vocabulary alone cannot decide the kind. |


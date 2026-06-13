---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism: Law-Governed Operation Algebra over a Subject Kind"
section_id: "A.6.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__008_conformance-checklist.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "A.6.1 — U.Mechanism: Law-Governed Operation Algebra over a Subject Kind"
  - "A.6.1:7 — Conformance Checklist"
line_start: 10022
line_end: 10051
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

### A.6.1:7 - Conformance Checklist

**CC-UM.0 (A.6.0 alignment).** A conforming `U.Mechanism` publication includes the four-row `U.Signature` Block. `OperationAlgebra` is the Vocabulary row, `LawSet` is the Laws row, and `Applicability` is the Applicability row. `SlotIndex` is a derived index, not a fifth Signature row.

**CC-UM.1 (Complete declaration).** A conforming publication includes DeclarationHeader, Imports, SubjectBlock, SlotIndex, OperationAlgebra, LawSet, AdmissibilityConditions, Applicability, Transport, GammaTimePolicy, PlaneRegime, and Audit.

**CC-UM.2 (Manifest coupling).** If imported or reused, the mechanism includes a SignatureManifest consistent with DeclarationHeader, imports, and provided symbols.

**CC-UM.3 (Monotone realization).** A realization satisfies the mechanism LawSet and imported laws. It may tighten laws or guards and must not relax them.

**CC-UM.4 (Opaque imports).** Realizations and mechanisms treat imported signatures as opaque. They reference only provided symbols and ClaimIds.

**CC-UM.5 (Bridge-only transport).** Cross-context or cross-plane use names BridgeId, channel, ReferencePlane, and plane policy when needed. Transport does not create a `U.Transfer` edge.

**CC-UM.6 (Reliability-only penalties).** Scope, kind, bridge, or plane penalties are recorded in Reliability or effective Reliability only. Formality and Guarantee stay invariant.

**CC-UM.7 (Comparison compliance).** Numeric comparison or aggregation binds to characteristic-space, measurement, scale, and comparison rules. Partial orders remain set-valued unless a declared scorer governs the reduction.

**CC-UM.8 (Tri-state guards).** Guard predicates are deterministic, context-local, and fail closed. Unknowns become `degrade` or `abstain`, not zero or false.

**CC-UM.9 (SlotIndex as view).** SlotIndex is mechanically derivable from per-operator SlotSpecs plus guard-only SlotSpecs. Didactic ValueKind projections do not replace SlotSpecs.

**CC-UM.10 (Specialization chains).** A mechanism specialization names its parent and morphism kind, preserves inherited SlotKinds, narrows ValueKinds only in Refinement, and avoids new mandatory inputs to inherited operations.

**CC-UM.11 (No in-place type definition).** `BaseType` references an existing `U.Type`. Any new `U.Type` requires a separate accepted naming and kind decision.

**CC-UM.12 (Method-position separation).** A mechanism publication does not close a method, method-description, work-plan, dated-work, evidence, gate, publication-use, or result claim. Linked values are named by their governing patterns.

**CC-UM.13 (No tool binding).** Kernel mechanism narrative does not depend on vendor names, CI hooks, telemetry fields, or tool-specific evaluator semantics. Such details are outside the mechanism unless another governing pattern admits them.


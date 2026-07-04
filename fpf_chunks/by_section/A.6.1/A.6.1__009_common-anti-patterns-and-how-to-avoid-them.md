---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
section_id: "A.6.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.6.1 — U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
  - "A.6.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 10730
line_end: 10743
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

### A.6.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| SlotIndex treated as a fifth Signature row | Keep SlotSpecs inside operator declarations; use SlotIndex only as a derived view. |
| Admission tests put in LawSet | Move operational guards to AdmissibilityConditions. |
| Implicit context crossing | Name BridgeId, channel, ReferencePlane, and Reliability penalty relation. |
| Penalties leak into Formality or Guarantee | Record losses in Reliability or effective Reliability only. |
| Scale-incompatible scalarization | Use characteristic-space, measurement, scale, and comparison rules; keep partial orders set-valued. |
| Specialization breaks SlotKind identity | Preserve inherited SlotKinds; narrow ValueKinds only where Refinement permits it. |
| Unknown coerced to zero or false | Use `degrade` or `abstain`. |
| Method label treated as mechanism law | Recover the current governed claim and relation position first; use A.6.1 only when operation algebra, laws, admissibility predicates, transport, audit, or realization relation are current. |
| Tool configuration treated as mechanism declaration | Keep tool settings in the direct tooling, publication, work, or evidence pattern; put only mechanism semantics in A.6.1. |


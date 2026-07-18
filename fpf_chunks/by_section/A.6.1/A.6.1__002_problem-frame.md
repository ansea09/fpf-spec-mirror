---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
section_id: "A.6.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__002_problem-frame.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "A.6.1 — U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
  - "A.6.1:1 — Problem frame"
line_start: 10974
line_end: 10996
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

### A.6.1:1 - Problem frame

Use this pattern when a reusable declaration must do more than name a signature. Use it when the project needs to declare a **law-governed operation algebra**, admissibility predicates, context-local applicability, cross-context transport, and realization discipline for a `U.Mechanism`.

Use it when the working question is:

* which `SubjectKind` and `RangedValueKind` the mechanism ranges over;
* which operations are available and which SlotSpecs those operations publish;
* which laws and invariants govern the operations;
* which admissibility predicates fail closed before an operation can be used;
* which bridge, reference-plane, and reliability-penalty relation governs cross-context or cross-plane use;
* whether a realization tightens the mechanism without relaxing its laws.

**Primary EntityOfConcern.** The `EntityOfConcern` is `U.Mechanism`: a specialization of `U.Signature` whose vocabulary is an `OperationAlgebra`, whose laws are a `LawSet`, and whose additional fields declare admissibility, applicability, transport, time policy, plane policy, audit surface, and monotone realization relation.

**First useful move.** Write the mechanism as an A.6.0 Signature Block, then add only the mechanism-specific fields: `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, `Transport`, `GammaTimePolicy`, `PlaneRegime`, and `Audit`. If cross-context use is current, name the Bridge and the Reliability penalty relation before any reuse claim is made.

**What goes wrong if missed.** An implementation recipe, method name, policy rule, telemetry package, or cross-context reuse habit can masquerade as mechanism law. Downstream work then cannot tell which operations are admitted, which predicates fail closed, which realization is monotone, and which losses affect Reliability rather than Formality or Guarantee.

**What this buys in practice.** Scope mechanisms, normalization mechanisms, selector mechanisms, scoring mechanisms, publication mechanisms, and comparison mechanisms can be compared, refined, extended, transported, and realized without hiding law, guard, time, plane, or Reliability assumptions.

**Not this pattern when.** If the claim is only a reusable declaration with no operation algebra and no admissibility predicates, use `A.6.0`. If the claim is a semantic way of doing, use `A.3.1`. If the claim is an episteme describing that way, use `A.3.2`. If the claim is planned or dated work, use `A.15.2` or `A.15.1`. If the claim is evidence, assurance, gate authority, publication use, or result acceptance, use the governing pattern for that claim.


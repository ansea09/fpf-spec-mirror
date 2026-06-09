---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: "A.6.1:0"
section_title: "Use and boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__002_use-and-boundary.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
  - "A.6.1:0 — Use and boundary"
line_start: 9211
line_end: 9222
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.6.0"
  - "C.16"
  - "E.10.D1"
  - "G.10"
  - "G.11"
keywords:
  - "AdmissibilityConditions"
  - "Bridge‑only"
  - "LawSet"
  - "Mechanism"
  - "OperationAlgebra"
  - "Transport"
---

### A.6.1:0 - Use and boundary

Use this pattern when a reusable declaration has to do more than name a signature: it must declare a law-governed operation algebra, operational admissibility predicates, context-local applicability, and explicit cross-context or cross-plane Transport for a `U.Mechanism`.

Do not use this pattern when the claim being made is only a reusable declaration with no operational guards; use A.6.0. Do not use it to authorize work, pass a gate, certify evidence, choose a method, publish telemetry, or prove a result. Those claims use the work, gate, evidence, method, publication, or result patterns that cite the mechanism when needed.

First useful move: write the mechanism declaration as a specialization of the four-row A.6.0 Signature Block, then add only the mechanism-specific fields: `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, `Transport`, `Γ_timePolicy`, `PlaneRegime`, and `Audit`. If cross-context use is live, name the Bridge and the Reliability penalty relation before any reuse claim is made.

What goes wrong if missed: an implementation recipe, a policy rule, a telemetry package, or a cross-context reuse habit can masquerade as mechanism law. Downstream work then cannot tell which operations are lawful, which admissibility predicates fail closed, and which losses affect Reliability rather than Formality or Guarantee.

What this buys: USM, UNM, selection mechanisms, normalization mechanisms, scoring mechanisms, and publication mechanisms can be compared, refined, extended, transported, and realized without hiding law, guard, time, plane, or Reliability assumptions.


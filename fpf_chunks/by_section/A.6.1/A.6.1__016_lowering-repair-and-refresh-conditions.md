---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: "A.6.1:12b"
section_title: "Lowering, repair, and refresh conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__016_lowering-repair-and-refresh-conditions.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
  - "A.6.1:12b — Lowering, repair, and refresh conditions"
line_start: 9500
line_end: 9514
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

### A.6.1:12b - Lowering, repair, and refresh conditions

A `U.Mechanism` remains usable while its MechanismDeclaration, imported signatures, SlotSpecs, LawSet, AdmissibilityConditions, Applicability, Transport, Γ_timePolicy, PlaneRegime, and Audit relations remain recoverable and monotone with respect to A.6.0.

Repair the mechanism, or mint a new mechanism when monotone repair is impossible, if any of these conditions holds:

* an inherited SlotKind is renamed, widened, or given a new required argument;
* a realization relaxes a law, bypasses an admissibility predicate, or depends on hidden structure inside an imported signature;
* a cross-context or cross-plane reuse claim lacks BridgeId, ReferencePlane, CL, CL^k, CL^plane, or Reliability penalty relation;
* a numeric comparison or aggregation is no longer legal under CG-Spec, MM-CHR, CSLC, or the current characteristic-space declarations;
* a Γ_timePolicy, validity window, or “latest” assumption changes an admissibility result;
* a current SoTA change in algebraic effects, session types, typed semantic translation, Policy-as-Code, calibrated uncertainty, or context normalization changes the operation algebra, guard discipline, morphism relation, or transport boundary.

Do not repair the mechanism merely because one work occurrence, telemetry publication, evidence record, gate decision, method choice, or realization version changed. Repair the object governed by that later relation unless the change alters the MechanismDeclaration, its imported signature relation, or the monotone relation between a realization and the MechanismDeclaration.


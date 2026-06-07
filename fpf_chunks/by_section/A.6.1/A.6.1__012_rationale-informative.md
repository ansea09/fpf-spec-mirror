---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: "A.6.1:10"
section_title: "Rationale (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__012_rationale-informative.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
  - "A.6.1:10 — Rationale (informative)"
line_start: 9260
line_end: 9263
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

### A.6.1:10 - Rationale (informative)

Binding mechanisms to an explicit **Signature -> Realization** discipline (A.6.0 `SignatureManifest` plus CC-UM.2 monotonicity and opacity) keeps reuse safe: signatures and laws carry the boundary semantics; realizations may vary but cannot relax laws. It also makes cross-context Bridge crossings explicit and records costs in `R_eff`, never in F or G.


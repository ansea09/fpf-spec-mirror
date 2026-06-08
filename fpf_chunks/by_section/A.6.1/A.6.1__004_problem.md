---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: "A.6.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__004_problem.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
  - "A.6.1:2 — Problem"
line_start: 9057
line_end: 9060
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

### A.6.1:2 - Problem

Without a kernel abstraction, scope, normalization, and comparison constructs proliferate with incompatible algebras and guard predicates; cross-context reuse lacks a visible **Bridge and CL penalty relation**; comparability drifts into **illegal scalarisation** (e.g., ordinal means). FPF already curbs this via **A.6.0** (Signature discipline, `SignatureManifest`), **USM** (scope algebra and Γ_time), **UNM** (normalize-then-compare), and **CG-Spec** (lawful comparators and ScoringMethods), but lacks a **common kernel kind** for “mechanism.”


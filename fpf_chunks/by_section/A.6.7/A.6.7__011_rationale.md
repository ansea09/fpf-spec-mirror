---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
section_id: "A.6.7:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__011_rationale.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.6.7 — MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
  - "A.6.7:10 — Rationale"
line_start: 24301
line_end: 24311
dependencies:
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "G.10"
  - "G.5"
  - "U.Mechanism"
keywords:
  - "CG-Spec"
  - "CN-Spec"
  - "P2W"
  - "crossing visibility"
  - "distinct mechanisms"
  - "mechanism suite"
  - "planned baseline"
  - "spec pins"
  - "suite obligations"
---

### A.6.7:10 - Rationale

Characterization and admissibility-gated selection pipelines are unified by:

* shared governing spec refs (e.g., CN‑Spec / CG‑Spec),
* shared conditions for actual semantic, kind and plane relations, independently governed flow/gate crossings, and any penalties routed to `R_eff`,
* shared guard semantics (tri-state, no coercion),
* and explicit protocol constraints (allowed pipelines).

Encoding this unity as “one mechanism” or “one family” forces false commonality and invites hidden semantics. A dedicated **suite descriptor** preserves modularity and keeps the level separation clean.


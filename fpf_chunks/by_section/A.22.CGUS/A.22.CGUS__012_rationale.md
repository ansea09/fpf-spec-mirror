---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__012_rationale.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:10 — Rationale"
line_start: 35009
line_end: 35016
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "B.3.5"
  - "B.5.2"
  - "C.13"
  - "C.18"
  - "C.19"
  - "C.2.P.DR"
  - "C.3"
  - "C.32.P2S"
  - "C.33"
  - "C.35"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.18.NET-conforming"
  - "E.23"
  - "F.17"
  - "G.11"
  - "G.5"
keywords:
---

### A.22.CGUS:10 - Rationale

The selected design is a thin A.22 specialization of `U.Structure` because the recurring object is real but not a new root ontology. Constraint-based process modeling, case-management practice, artifact-centric modeling, acausal modeling, architecture-description practice, and FPF's own pattern use all separate a constraint-bearing structure from a performed trace, work order, view, publication, solver run, or example path. FPF adopts that separation as a constraint-governed unfolding structure and refuses to import one universal process calculus.

Physical modeling makes the same distinction concrete. In acausal modeling, component relations, quantities conserved across connections, and mode conditions can be declared before the model is compiled and solved in one chosen direction. The FPF import is only the general architecture of the move: structure and constraints first; derived calculation, demonstration, calibration, publication, or work use later under direct governing patterns.

CGUS is deliberately close to A.22. It is a `U.Structure` over a declared substrate in a bounded context. Descriptions, views, graph renderings, route cards, README entries, and examples help humans use it; they do not become it.


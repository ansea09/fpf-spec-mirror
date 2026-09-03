---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__012_rationale.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:10 — Rationale"
line_start: 36245
line_end: 36250
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.29"
  - "C.30"
  - "C.32"
  - "C.32.P2S"
  - "C.33"
  - "C.35"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.23"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
---

### A.22.CGUS:10 - Rationale

The recurring object is a thin specialization of A.22 `U.Structure`, not a new root kind. Constraint-based process modeling, object-centric querying, artifact-centric modeling, acausal modeling, and FPF pattern use all distinguish a constraint-bearing structure from a performed trace, work order, view, publication, solver run, or example path.

The same distinction appears in acausal engineering models: component relations and constraints can be stated before an analysis chooses a calculation direction. FPF adopts only that general separation. Mathematical models, analyses, executions, results, and publications keep their own kinds and rules.


---
chunk_kind: "child"
pattern_id: "C.30.TFS-REL"
pattern_title: "Architecture Transformation-Flow Structure Relation"
section_id: "C.30.TFS-REL:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TFS-REL/C.30.TFS-REL__003_problem.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.30.TFS-REL — Architecture Transformation-Flow Structure Relation"
  - "C.30.TFS-REL:2 — Problem"
line_start: 61440
line_end: 61445
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.0"
  - "A.6.5"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.32"
  - "C.32.P2S"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "F.18"
  - "G.6"
keywords:
  - "architecture structural view"
  - "architecture-to-transformation-flow relation"
  - "candidate architecture input"
  - "functional behavior"
  - "selected structure"
  - "transformation-flow structure"
---

### C.30.TFS-REL:2 - Problem

Grounded architecture claims, selected architecture-relevant structures, architecture structural views, and conditional architecture descriptions often need E.18 objects when they discuss transformation-flow structure, functional dependencies, data movement, control paths, evidence-flow descriptions, neural-network dataflow, or code-agent relation graphs.

C.30.TFS-REL prevents collapse by requiring the selected architecture-side reference, such as `ArchitectureOf@Context`, structure ref, structural view, or conditional description use, before any E.18-governed selected transformation-flow structure, path, slice, crossing, or valuation gets architecture use.


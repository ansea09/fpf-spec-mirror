---
chunk_kind: "child"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture-TGA Flow-Structure Relation"
section_id: "C.30.TGA-FLOW-REL:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TGA-FLOW-REL/C.30.TGA-FLOW-REL__003_problem.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture-TGA Flow-Structure Relation"
  - "C.30.TGA-FLOW-REL:2 — Problem"
line_start: 54069
line_end: 54074
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureFlowStructureRelation@TGA"
  - "FlowTransductionStructure"
  - "TGA graph relation"
  - "architecture flow relation"
  - "graph/path/crossing"
---

### C.30.TGA-FLOW-REL:2 - Problem

Grounded architecture claims, selected architecture-relevant structures, architecture structural views, and conditional architecture descriptions often need E.18 objects when they discuss flow or transduction structure, functional dependencies, data movement, control paths, evidence flows, neural-network dataflow, or code-agent relation graphs.

C.30.TGA-FLOW-REL prevents that collapse by requiring the selected architecture-side reference, such as `ArchitectureOf@Context`, structure ref, structural view, or conditional description use, before any E.18-governed graph, path, or crossing object gets architecture use.


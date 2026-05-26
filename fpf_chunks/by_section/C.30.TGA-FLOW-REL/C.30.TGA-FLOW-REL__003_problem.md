---
chunk_kind: "child"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture/TGA Flow-Structure Relation"
section_id: "C.30.TGA-FLOW-REL:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TGA-FLOW-REL/C.30.TGA-FLOW-REL__003_problem.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture/TGA Flow-Structure Relation"
  - "C.30.TGA-FLOW-REL:2 — Problem"
line_start: 51395
line_end: 51400
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
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "E.10"
  - "E.10.SEMIO"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureFlowStructureRelation@TGA"
  - "FlowTransductionStructure"
  - "TGA graph support"
  - "architecture flow relation"
  - "graph/path/crossing"
---

### C.30.TGA-FLOW-REL:2 - Problem

TGA already governs transduction graphs, paths, crossings, and flow valuations. Architecture descriptions often need those objects when they discuss flow/transduction structure, functional dependencies, data movement, control paths, evidence flows, neural-network dataflow, or code-agent relation graphs.

The risk is overread. A TGA graph can be useful enough that practitioners start treating it as the architecture, the functional architecture, the work sequence, or the proof that evidence, gate, safety, causality, or assurance conditions are satisfied. C.30.TGA-FLOW-REL prevents that collapse by relating architecture structural views to E.18-governed graph/path/crossing objects without redefining E.TGA.


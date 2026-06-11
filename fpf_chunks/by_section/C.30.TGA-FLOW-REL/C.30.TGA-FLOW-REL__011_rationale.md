---
chunk_kind: "child"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture-TGA Flow-Structure Relation"
section_id: "C.30.TGA-FLOW-REL:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TGA-FLOW-REL/C.30.TGA-FLOW-REL__011_rationale.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture-TGA Flow-Structure Relation"
  - "C.30.TGA-FLOW-REL:10 — Rationale"
line_start: 54627
line_end: 54632
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

### C.30.TGA-FLOW-REL:10 - Rationale

E.TGA is already the governing FPF pattern for transduction graphs, paths, crossings, flow valuations, and related pins. Architecture needs to use that work without letting it become generic architecture ontology. The smallest stable relation is therefore a C.30-side record that points to E.18 objects and states admissible and non-admissible architecture use.

This pattern also protects functional architecture. A functional structure view may correspond to flow or transduction structure, but function and flow are different structure kinds. The relation is useful precisely because it preserves that difference while allowing correspondence.


---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__011_rationale.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:10 — Rationale"
line_start: 51826
line_end: 51831
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.3"
  - "B.2.5"
  - "B.3"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TGA-FLOW-REL"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller/plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:10 - Rationale

Control architecture is too important to leave to diagram authority and too useful to remove from architecture language. The FPF move is to keep the practice cue and recover its kind: a control-structure view is a D/S record over selected architecture-relevant control structure. It can cite `B.2.5`, TGA, dynamics, C.27, C.28, evidence, assurance, gates, and C.29, but it does not absorb their claim kinds.

This also protects the architecture ontology's I/D/S distinction. The architecture is the selected structure under `ArchitectureOf@Context`; the LCA diagram or control note is an architecture description/view. Several descriptions may describe the same control structure, and one description may be published without becoming the structure it describes.


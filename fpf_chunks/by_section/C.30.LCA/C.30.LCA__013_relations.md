---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__013_relations.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:12 — Relations"
line_start: 51841
line_end: 51850
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

### C.30.LCA:12 - Relations

* Builds on `C.30` for architecture-description adequacy and `C.30.ASV` for structural-view adequacy.
* Uses `A.22` for structure and structural-view kind discipline.
* Coordinates with `B.2.5` for supervisor-subholon feedback-loop recognition.
* Coordinates with `E.18` and `C.30.TGA-FLOW-REL` when flow/transduction path slices support the control view.
* Exits to `A.3.3` for dynamics and stability support, `C.27` for temporal/rate adequacy, `C.28` for causal-use claims, `A.10`/`G.6` for evidence support, `B.3` for assurance, `A.20`/`A.21` for constraint validity and gate decisions, `A.15` for work authority, and `C.29` when LCA is used as a transferable mathematical lens.

Does not replace: `C.30` architecture-description adequacy, `C.30.ASV` architecture structural-view adequacy, `B.2.5` supervisor-subholon feedback-loop discipline, `E.18` graph/path/crossing discipline, `A.3.3` dynamics support, `C.27` temporal/rate adequacy, `C.28` causal-use support, `A.10`/`G.6` evidence support, `B.3` assurance, `A.20`/`A.21` gate and constraint-validity records, `A.15` work, or `C.29` mathematical-lens adequacy.


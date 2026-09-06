---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__013_relations.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:12 — Relations"
line_start: 61651
line_end: 61661
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
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller and plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:12 - Relations

* Builds on `C.30` for direct architecture relations and selected-structure adequacy, `C.30.AD` for description identity and use, `E.17.0` for direct viewpoint conformance, and `C.30.ASV` for structural-view adequacy.
* Uses `A.22` for exact structure identity and structure-kind discipline.
* Coordinates with `C.30.STRAT` when layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or similar source labels must be recovered before control-specific use.
* Coordinates with `B.2.5` for supervisor-subholon feedback relation recognition.
* Coordinates with E.18 and C.30.TFS-REL when transformation-flow path slices supply structure input to the control view; use E.18.2 for a mathematical description when that description is current.
* For neighboring claims, use `A.3.3` for dynamics or stability, `C.27.TA` for temporal-aspect or rate-band structure, `C.27` for authored temporal-claim adequacy, `C.28` for causal use, A.10 for bounded source-to-use reliance, G.6 for citable provenance paths, B.3 only for a named assurance claim, A.20 for internal-constraint validity, A.21 for gate decisions, A.15 for Work alignment, A.15.6 for project-Work recovery, E.24.PUB for publication, and C.29 for representation or transferable mathematical-lens use.

Use C.30.LCA only for the control-structure description or view-adequacy question at issue.


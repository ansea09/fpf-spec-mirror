---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__013_relations.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:12 — Relations"
line_start: 62483
line_end: 62493
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

* Builds on `C.30` for direct architecture relation and selected-structure adequacy, `C.30.AD` for description identity/use, `E.17.0` for direct viewpoint conformance, and `C.30.ASV` for structural-view adequacy.
* Uses `A.22` for exact structure identity and structure-kind discipline.
* Coordinates with `C.30.STRAT` when layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or similar source labels must be recovered before control-specific use.
* Coordinates with `B.2.5` for supervisor-subholon feedback relation recognition.
* Coordinates with E.18 and C.30.TFS-REL when transformation-flow path slices supply structure input to the control view.
* Applies `A.3.3` for dynamics/stability, `C.27.TA` for temporal-aspect/rate-band structure, `C.27` for authored temporal-claim adequacy, `C.28` for causal use, A.10/G.6 for evidence, B.3 for assurance, A.20/A.21 for constraint validity/gates, A.15 for Work/project use, E.24.PUB for publication, and C.29 for representation or transferable mathematical-lens use.

Neighboring claims stay with their governing patterns: C.30.STRAT for stratification/source-label repair; C.30 for actual architecture relations and selected structures; C.30.AD for description; E.17.0/C.30.ASV for view conformance and adequacy; B.2.5 for supervisor-subholon feedback; E.18 for graph/path/crossing structure; A.3.3 for dynamics; C.27.TA/C.27 for temporal claims; C.28 for causal use; A.10/G.6 for evidence; B.3 for assurance; A.20/A.21 for gate and constraint-validity records; A.15 for Work; E.24.PUB for publication; and C.29 for representation/lens use. C.30.LCA governs only the exact control-structure description/view adequacy at issue.


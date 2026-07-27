---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__013_relations.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:12 — Relations"
line_start: 61515
line_end: 61525
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
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
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

* Builds on `C.30` for grounded architecture and selected-structure adequacy and `C.30.ASV` for structural-view adequacy.
* Uses `A.22` for structure and structural-view kind discipline.
* Coordinates with `C.30.STRAT` when layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or similar source labels must be recovered before any control-specific use enters C.30.LCA.
* Coordinates with `B.2.5` for supervisor-subholon feedback relation recognition.
* Coordinates with `E.18` and `C.30.TFS-REL` when transformation-flow path slices supply structure input to the control view.
* Applies `A.3.3` for dynamics and stability claims, `C.27.TA` for temporal-aspect or rate-band structure, `C.27` for authored temporal-claim adequacy, `C.28` for causal-use claims, `A.10` or `G.6` for evidence claim, `B.3` for assurance, `A.20` or `A.21` for constraint validity and gate decisions, `A.15` for work authority, and `C.29` when LCA is used as a transferable mathematical lens.

Neighboring claims stay with their governing patterns: `C.30.STRAT` for stratification and source-label precision restoration, `C.30` for grounded architecture and selected-structure adequacy, `C.30.ASV` for architecture structural-view adequacy, `B.2.5` for supervisor-subholon feedback relation, `E.18` for graph, path, and crossing discipline, `A.3.3` for dynamics claims, `C.27.TA` for temporal-aspect or rate-band structure, `C.27` for authored temporal-claim adequacy, `C.28` for causal use, `A.10` or `G.6` for evidence, `B.3` for assurance, `A.20` or `A.21` for gate and constraint-validity records, `A.15` for work, and `C.29` for mathematical-lens use. `C.30.LCA` governs only the control-structure view relation being claimed.


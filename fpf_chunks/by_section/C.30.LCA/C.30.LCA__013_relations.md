---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__013_relations.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:12 — Relations"
line_start: 77657
line_end: 77685
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
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.32.LCA"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "G.6"
keywords:
  - "control-structure view"
  - "controller"
  - "feedback closure"
  - "layered control architecture"
  - "observer"
  - "plant"
  - "rate band"
  - "supervisor"
---

### C.30.LCA:12 - Relations

* Builds on `C.30` for direct architecture relations and selected-structure adequacy, `C.30.AD` for description identity and use, `E.17.0` for viewpoint conformance, and `C.30.ASV` for structural-view adequacy.
* Uses `A.22` for structure identity and structure-kind discipline.
* Coordinates with `C.30.STRAT` when layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or similar source labels must be recovered before control-specific use.
* Coordinates with `B.2.5` for supervisor-subholon feedback relation recognition.
* Coordinates with `C.32.LCA` for constructing and comparing control arrangements. C.30.LCA supplies the recovered control account and its use limits; C.32.LCA returns explained alternatives whose descriptions can be examined here. Construction and view qualification retain their different results.
* Coordinates with E.18 and C.30.TFS-REL when transformation-flow path slices supply structure input to the control view; use E.18.2 for a mathematical description when that description is at issue.

For neighboring claims, use these patterns:

| Pattern | Claim or use |
| --- | --- |
| `A.3.3` | Dynamics or stability. |
| `C.27.TA` | Temporal-aspect or rate-band structure. |
| `C.27` | Authored temporal-claim adequacy. |
| `C.28` | Causal use. |
| A.10 | Bounded source-to-use reliance. |
| G.6 | Citable provenance paths. |
| B.3 | Only a named assurance claim. |
| A.20 | Internal-constraint validity. |
| A.21 | Gate decisions. |
| A.15 | Work alignment. |
| A.15.6 | Project-Work recovery. |
| E.24.PUB | Publication. |
| C.29 | Representation or transferable mathematical-lens use. |

Use C.30.LCA only for the control-structure description or view-adequacy question at issue.


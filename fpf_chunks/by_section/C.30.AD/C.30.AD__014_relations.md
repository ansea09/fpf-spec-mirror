---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:11"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__014_relations.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:11 — Relations"
line_start: 56911
line_end: 56926
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.3.NAR"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD.BA"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "G.5"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "candidate-description boundary"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:11 - Relations

- `C.30` governs grounded architecture and selected-structure adequacy.
- `C.30.P` normalizes overloaded architecture or structure wording before this pattern is used.
- `C.30.ASV` governs architecture structural views and structure-kind and viewpoint separation.
- `C.33` governs capture and loss of selected structure when an architecture description, generated relation graph, ADR-like record, or view set carries only part of the architecture content for a declared use.
- `C.34` governs preservation or correspondence adequacy when the architecture description is being compared with another view, source model, generated output, candidate, or realized structure.
- `A.6.3.NAR` governs a reader-facing narrative rendering made from an architecture description, description set, view set, or architecture-decision route. C.30.AD remains the owner for architecture-description adequacy; NAR owns only the structure-to-sequence relation, selected-source carry-through, lost structure, reader-use boundary, and source return.
- `C.30.TFS-REL`, `C.30.LCA`, and `C.30.ILC` govern architecture structure-relation subcases named by value.
- `C.32.P2S` governs the connected architecturing flow when the description carries only part of selected structure, decision handoff, method expectation, source-return, or actual-structure feedback.
- `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, and `E.17` govern generic EntityOfConcern, Description, view, viewpoint, publication, and MVPK machinery.
- `C.2.P` normalizes source-current and publication-form relation-set overreads.
- `E.11.PUR` governs recommended FPF pattern use after an architecture description has been read; C.30.AD only records the description-use boundary.
- `A.15.5` governs work-entry readiness and full-kit condition for intended architecture work; C.30.AD only records description, view, correspondence, source-return, freshness, publication-use, and specification-use relations.
- `E.10.MOVE` restores move-like wording when source prose about an architecture description does not mean a C.30 architecture move or a C.30.AD remaining architecture candidate use.


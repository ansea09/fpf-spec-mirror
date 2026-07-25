---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Architecture and Structure Precision Restoration"
section_id: "C.30.P:10"
section_title: "Related patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__013_related-patterns.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.30.P — Architecture and Structure Precision Restoration"
  - "C.30.P:10 — Related patterns"
line_start: 59859
line_end: 59873
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.8"
  - "G.5"
keywords:
---

### C.30.P:10 - Related patterns

- `E.10` catches architecture or structure wording and selects this pattern only when the selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or named C.30 subcase is hidden.
- `E.10.ARCH` defines the shared wording-use recovery order and applicability row.
- `A.22` governs selected structure and structural views as structure.
- `C.30` governs grounded `ArchitectureOf@Context` adequacy and thin conditional `ArchitectureDescription@Context` bridge use.
- `C.30.AD` governs the full architecture-description mechanism when `ArchitectureDescription@Context` is the EntityOfConcern under repair.
- `C.30.ASV` governs architecture structural views.
- `C.30.STRAT` governs stratification wording or source-label wording before C.30.P assigns any recovered architecture or structure portion.
- Named `C.30.*` patterns govern their own structure adequacy or view adequacy questions.
- `C.2.P` recovers source, publication, view, face, `PublicationUnit`, carrier, and source-use disposition.
- `A.6.P` repairs relation construction; `A.6.F` repairs function and functionality wording; `A.6.M` repairs module-relation and interface-specification wording.
- `C.16.P` repairs characteristic-and-scale wording, and `C.16.Q` repairs quality-term or evaluative characterization wording before score or quality use.
- `C.29` governs mathematical-lens use and does not become architecture by analogy.


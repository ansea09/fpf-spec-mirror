---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Clarify Architecture and Structure Wording (Precision Restoration)"
section_id: "C.30.P:10"
section_title: "Related patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__013_related-patterns.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "C.30.P — Clarify Architecture and Structure Wording (Precision Restoration)"
  - "C.30.P:10 — Related patterns"
line_start: 72293
line_end: 72307
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
  - "architecture description"
  - "architecture wording"
  - "diagram"
  - "model"
  - "precision restoration"
  - "structural view"
  - "structure wording"
---

### C.30.P:10 - Related patterns

- `E.10` catches architecture or structure wording and selects this pattern only when the selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or named C.30 subcase is hidden.
- `E.10.ARCH` defines the shared wording-use recovery order and applicability row.
- `A.22` governs selected structure and structural views as structure.
- `C.30` governs `ArchitectureRelation`, bounded `ArchitectureClaim` and the initial architecture-description question.
- `C.30.AD` governs architecture-description identity, correspondence and use. The description retains its own EntityOfConcern; it need not itself be the subject of another description.
- `C.30.ASV` governs architecture structural views.
- `C.30.STRAT` recovers unclear stratification or source-label meaning before C.30.P assigns the recovered architecture or structure portion.
- Named `C.30.*` patterns define or constrain their own structure adequacy or view adequacy questions.
- `C.2.P` recovers source, publication, view, face, `PublicationUnit`, carrier, and source-use disposition.
- `A.6.P` repairs relation construction; `A.6.F` repairs function and functionality wording; `A.6.M` repairs module-relation and interface-specification wording.
- `C.16.P` repairs unclear characteristic-and-scale wording, and `C.16.Q` repairs unclear quality-term or evaluative characterization wording. Already recoverable claims use their subject rules directly.
- `C.29` governs mathematical-lens use and does not become architecture by analogy.


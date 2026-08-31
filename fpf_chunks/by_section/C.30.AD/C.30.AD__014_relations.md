---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:11"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__014_relations.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:11 — Relations"
line_start: 59479
line_end: 59496
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
  - "E.10.D2"
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

- Use `C.2.1` to identify every architecture-description episteme.
- Use `C.30` for obtaining architecture relations, selected structures, and bounded architecture claims.
- `C.30.P` normalizes overloaded architecture or structure wording before this pattern is used.
- Use `C.30.ASV` to test architecture structural-view adequacy; only E.17.0 conformance admits the same episteme as `U.View`.
- Use `C.33` to account for captured and lost structure when a description, generated relation graph, ADR-like record, or view set carries only part of the needed architecture content.
- Use `C.34` to test preservation or correspondence when comparing a description with another view, source model, generated output, candidate, or realized structure.
- Use `C.29` for a mathematical-lens or coarse-graining result, `C.30.STRAT` for level-word admission, and `A.22` or `C.30` for the separately supported subject structure or architecture relation. Description-side grouping establishes none of those subject claims by itself.
- Use `A.6.3.NAR` for a reader-facing narrative made from a description, view set, or decision route. C.30.AD tests description adequacy; A.6.3.NAR handles structure-to-sequence, source carry-through, lost structure, reader use, and return conditions.
- Use `C.30.TFS-REL`, `C.30.LCA`, and `C.30.ILC` for their named architecture-relation subcases.
- Use `C.32.P2S` for a connected architecturing flow when the description carries only part of the selected structure, decision handoff, method expectation, source continuity, return condition, or feedback from actual structure.
- Use `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, and `E.24.PUB` for generic EntityOfConcern, view, viewpoint, representation, publication occurrence, form, carrier, and MVPK machinery.
- `C.2.P` normalizes source-expression, source-to-use, publication-form, and publication-currentness relation-set overreads.
- Use `E.11.PUR` for recommended FPF pattern use after reading a description; C.30.AD records only the description-use boundary.
- Use `A.15.5` for work-entry readiness and full-kit condition; use the A.15 family for Work and project-use relations. C.30.AD records only descriptions and their view conformance, set use, correspondence, source paths and returns, freshness, representation, publication use, and specification use.
- `E.10.MOVE` restores move-like wording when source prose about an architecture description does not mean a C.30 architecture move or a C.30.AD remaining architecture candidate use.


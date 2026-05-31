---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Architecture and Structure Precision Restoration"
section_id: "C.30.P:7"
section_title: "Reduced SoTA row"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__010_reduced-sota-row.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.30.P — Architecture and Structure Precision Restoration"
  - "C.30.P:7 — Reduced SoTA row"
line_start: 52100
line_end: 52112
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.8"
  - "J.4"
keywords:
---

### C.30.P:7 - Reduced SoTA row

Current architecture-description, model, view, and decision-record practice treats architecture as distinct from architecture descriptions, models, views, viewpoints, diagrams, and decision records. FPF adopts that line only where it changes action guidance: examples, non-use boundaries, exact exits, source-return conditions, and conformance checks.

| Practice basis | Source posture | What `C.30.P` adopts or adapts | FPF import boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 on architecture descriptions, architecture viewpoints, model kinds, and conformance requirements. | Current-standard/reference support for architecture-description and viewpoint separation. | Disciplines direct exits to `C.30` and `C.30.ASV`; blocks diagram/model/view/publication-as-architecture overread; supports `CC-C30P-2`, `CC-C30P-3`, and `CC-C30P-4`. | Does not import 42010 terminology as FPF ontology; FPF still uses `A.22`, `C.30`, `C.30.ASV`, and exact `C.30.*` patterns. |
| SEI "Documenting Software Architectures: Views and Beyond" practice line. | Current reference and lineage support for documenting views for stakeholder use. | Disciplines the source/publication/view split in worked cases and keeps view artifacts useful without making them the selected structure. | Does not make "view" a generic proof or decision object. |
| C4 model current practice for developer-friendly architecture diagrams over context, container, component, and code views. | Current practice anchor for diagram usefulness and diagram limits. | Disciplines the diagram, block, component, module, and layer examples: a diagram can be an entry or view publication, not architecture by appearance. | Does not make C4 levels FPF structure kinds or mandatory architecture views. |
| arc42 current architecture documentation template practice. | Current practice/reference support for architecture communication, constraints, decisions, and cross-cutting concerns. | Disciplines the distinction between documentation template sections, source publications, decisions, and architecture-description claims. | Does not let a documentation section, template heading, or dashboard become architecture authority by label. |
| ADR/MADR architecture decision record practice. | Current practice and lineage support for decision-record separation; current empirical ADR work may refine template choice, but does not replace FPF decision ontology. | Disciplines the ADR worked case and exact exits to `C.2.P`, `C.11`, `A.15`, or `C.30`: an ADR may record or motivate a decision; it is not automatically the architecture decision, work execution, or architecture itself. | Does not import ADR status as gate, release, proof, or FPF decision authority. |

This row is live in this pattern because it blocks diagram-as-architecture, graph-as-proof, view-as-structure-kind, publication-as-claim, and ADR-as-decision overreads. It does not import any external standard as FPF ontology.

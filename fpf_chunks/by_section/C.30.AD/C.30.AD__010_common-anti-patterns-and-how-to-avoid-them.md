---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 57649
line_end: 57660
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

### C.30.AD:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Description-as-architecture | A document, diagram, model, graph, view set, or card is said to be the architecture or to create an obtaining architecture relation. | Recover the exact holon, `ArchitectureRelation` occurrence, or selected structure; keep the episteme, representation, publication, and source-to-use relation distinct. |
| Viewpoint-as-structure-kind or view constructor | A stakeholder, role, concern, viewpoint label, authoring template, query, or bundle is used as if it named the selected structure or granted `U.View` membership. | Use `E.17.0` for exact viewpoint conformance and `C.30.ASV` for selected structure and kind. |
| Multi-view fog | Many views are listed, but their separate C.2.1 identities, conformance relations, selected structures, or correspondence cannot be recovered. | Add the description and viewpoint references, conformance relations, selected structures, and correspondence claims or relations that actually hold. |
| Coarse model as subject hierarchy | A grouped or lower-resolution description is treated as proof that the subject has the same levels, parts, or relations. | State the description-side grouping, mapping, preserved and lost distinctions, and allowed use; establish any subject-side relation separately. |
| Specification-as-authority | A specification-looking description is used as Work, gate passage, decision, assurance, evidence, work authorization, or release authorization. | Declare the specification use and use the pattern that defines or tests the other claim. |
| Freshness laundering | A recently generated diagram is treated as adequate because it is current. | Record the bounded freshness claim, source edition, and refresh trigger; do not treat currentness as adequacy, evidence, grounding, or assurance. |
| Architecture-documentation takeover | Practitioner guidance is dominated by diagrams, publications, and wording guards instead of architecture relations, structures, descriptions, and views. | Keep `C.30` about architecture and C.30.AD about descriptions and their use; use the relevant patterns for representation and publication. |


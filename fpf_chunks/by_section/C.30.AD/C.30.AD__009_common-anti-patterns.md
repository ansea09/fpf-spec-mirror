---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:7"
section_title: "Common anti-patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__009_common-anti-patterns.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:7 — Common anti-patterns"
line_start: 52164
line_end: 52174
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.8"
  - "F.18"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:7 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Description-as-architecture | A document, diagram, model, graph, view set, or card is said to be the architecture. | Recover `ArchitectureOf@Context` and keep the artifact as description, view, publication, carrier, or source. |
| Viewpoint-as-structure-kind | A stakeholder, role, concern, or viewpoint label is used as if it named the selected structure. | Use `C.30.ASV` to recover structure kind and viewpoint separately. |
| Multi-view fog | Many views are listed, but no one can tell which selected structures they describe or how they correspond. | Add architecture claim ref, selected structure refs, viewpoint refs, correspondence refs, and source-return conditions. |
| Specification-as-authority | A specification-looking architecture description is used as work, gate, decision, assurance, evidence, or release authority. | Declare specification use and apply the exact neighboring pattern to the authority claim. |
| Freshness laundering | A recently generated diagram is treated as adequate because it is current. | Record source edition and refresh trigger; do not treat currentness as adequacy, evidence, or assurance. |
| Architecture-documentation takeover | The pattern spends most of its live guidance on diagrams, publications, and wording guards instead of architecture claim, selected structures, and views. | Keep C.30 centered on architecture and use C.30.AD only when the description itself is the live EntityOfConcern. |


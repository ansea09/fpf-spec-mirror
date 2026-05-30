---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 28811
line_end: 28821
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.2"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
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
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
  - "architecture-description claim"
  - "preserved/lost structure"
  - "selected structure"
  - "source return"
  - "structural description"
  - "structural view"
  - "structure"
---

### A.22:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Structure-as-document** | A diagram, table, dashboard, relation graph, or prose section is called the structure. | Recover publication, carrier, description, or view relation; name the structure separately only when selected organization is live. |
| **Reliance-reading-as-structure** | A source trace, benchmark, lens output, model, or simulation is treated as the structure. | Name the exact A.6.6/source-description/evidence/lens ontology and state relation kind where live, validation boundary, and non-admissible use. |
| **Loss-free extraction** | Extracted or coarsened structure is used without lost structure or source return. | Add `preservedStructure`, `lostStructure`, `validationBoundary`, and `sourceReturnCondition`. |
| **Architecture root-kind rebound** | Structure work reintroduces `U.Architecture` or treats architecture as parallel to structure. | Use `ArchitectureOf@Context` and C.30; keep A.22 as the upstream structure carrier. |
| **Lens ontology import** | A mathematical lens output becomes the target ontology. | Use C.29 for the lens, cite it through C.29 lens adequacy, preserved/lost structure, and stop-condition discipline. |
| **Sterile precision rewrite** | The text removes overread but no longer tells the practitioner what to do. | Restore the surviving action: structure card, structure-claim reliance reading, D/S view, source return, or exact FPF pattern application. |


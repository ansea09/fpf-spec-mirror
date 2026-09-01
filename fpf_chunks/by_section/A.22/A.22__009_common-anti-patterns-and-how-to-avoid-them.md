---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 35616
line_end: 35626
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.13"
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
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.18.3"
  - "E.18.NET"
  - "E.24"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
---

### A.22:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Structure-as-document** | A diagram, table, dashboard, relation graph, or prose section is called the structure. | Recover publication, publication-form, description, or view relation; name the structure separately only when selected organization is being claimed. |
| **Reliance-interpretation-as-structure** | A trace used as source basis, benchmark, lens output, model, or simulation is treated as the structure. | Name the exact A.6.6, source-description, evidence, or lens relation and its definition or test; state its validation boundary and stop or return condition, adding a grounded guard only for an inference supplied by the current case. |
| **Loss-free extraction** | Extracted or coarsened structure is used without lost structure or structure-use return. | Add `preservedStructure`, `lostStructure`, `validationBoundary`, and `structureUseReturnCondition`. |
| **Architecture root-kind rebound** | Structure work reintroduces `U.Architecture` or treats architecture as parallel to structure. | Use `ArchitectureOf@Context` and C.30; keep A.22 as the upstream selected-structure EntityOfConcern. |
| **Lens ontology import** | A mathematical lens output becomes the imported ontology. | Use C.29 for the lens, cite it through C.29 lens-use result, preserved structure, lost structure, and stop-condition discipline. |
| **Sterile precision rewrite** | The text removes overread but no longer tells the practitioner what to do. | Restore the surviving action: structure card, structure-claim reliance relation, Description or view, `StructureUseReturnCondition`, or FPF pattern application. |


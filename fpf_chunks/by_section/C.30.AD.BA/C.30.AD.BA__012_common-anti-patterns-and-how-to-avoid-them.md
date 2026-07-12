---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:8.1"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:8.1 — Common Anti-Patterns and How to Avoid Them"
line_start: 57085
line_end: 57093
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.PUB"
  - "F.18"
keywords:
---

### C.30.AD.BA:8.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Correction |
| --- | --- | --- |
| BIM is the asset | A model or IFC exchange is treated as the building, plant, or facility itself. | Name the physical built asset as `describedHolonRef` and keep the model as description or publication material. |
| Designation code proves parthood | A designation prefix or aspect label is used as proof that one object is a part, function, product, or location of another. | Recover designation scheme, aspect or view, selected structure, correspondence, and admissible use. |
| Digital twin grants authority | Sensor-connected twin material is treated as evidence sufficiency, assurance, gate passage, or work completion. | Keep source/currentness boundaries and apply `A.10`, `B.3`, `A.21`, or work patterns for the authority claim. |
| Lifecycle view merge | Design model, as-built model, operation record, maintenance work, and physical transformation are merged because one dashboard shows them together. | Use `DesignRunTagRefs`, source relations, work refs, and transformation refs before admitting any identity, parthood, or MHT claim. |


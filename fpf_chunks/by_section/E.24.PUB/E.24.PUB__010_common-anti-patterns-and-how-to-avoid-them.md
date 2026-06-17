---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Ontic Description and Publication Discipline"
section_id: "E.24.PUB:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "E.24.PUB — Ontic Description and Publication Discipline"
  - "E.24.PUB:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 71529
line_end: 71538
dependencies:
  - "A.19"
  - "A.19.ECS"
  - "A.22"
  - "C.2.1"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.17.0"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.8"
  - "E.9.DA"
  - "F.19"
keywords:
---

### E.24.PUB:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Pattern host as ontic | The file or section is cited as if it were the object it describes. | Name the ontic EoC and the ontic-description episteme separately. |
| Diagram as architecture claim | A diagram is treated as the `ArchitectureOf@Context` claim or as the selected `U.Structure` itself. | Treat the diagram as a publication form of an architecture-description episteme; use `C.30` for the `ArchitectureOf@Context` claim or `A.22` for selected `U.Structure`. |
| Score table as characteristic space | A table of scores is treated as the characteristic-space ontology. | Separate the table, filled evaluation, and `U.CharacteristicSpace`. |
| Generic guard pile-up | A subject pattern opens with a long list of what a description is not. | Keep one non-overread sentence; when evidence, gate, work, publication-use, or source-use is current, apply the direct pattern governing that claim. |
| View variant as duplicate ontology | Several views of one subject are treated as several subjects. | Use `E.17` for view or publication packaging and keep the ontic identity stable. |


---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 85984
line_end: 85994
dependencies:
  - "A.11"
  - "A.3.2"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.17.0"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "F.18"
  - "U.MethodDescription"
  - "U.View"
  - "U.Viewpoint"
keywords:
---

### E.24.UK:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| **U-dot by punctuation.** A heading or filename contains `U.` and therefore survives as a kind. | Public spelling outruns admission. | Apply the durable U-kind test; otherwise rename to the governed object. |
| **Participation or SlotKind becomes kind.** An entity receives a new U-kind because it participates in a relation, or a `RelationSignature` SlotKind is read as a world-side kind. | Participation meaning and reusable declaration are collapsed. | Keep the entity's independently governed kind, state the direct relation, and keep the SlotKind only inside its A.6.5 SlotSpec. |
| **Source type import.** A BFO, ISO, OWL, database, or programming-language type is copied as an FPF U-kind. | Source ontology and FPF ontic admission rules become mixed. | Use the source conversion guide and name the FPF governed object. |
| **Searchable title wins.** A memorable heading remains public even though the body governs a record, publication form, relation structure, or local frame. | Discoverability replaces ontology. | Keep the searchable phrase in entry or retrieval material if useful, and put the governed object in the public pattern name. |
| **Dependent kind promoted.** A dependent distinction is admitted as an independent root U-kind. | FPF grows duplicate roots for one governed individual or an identity dependence is hidden. | Name the root U-kind and state either the same-individual membership rule or the exact identity-dependence relation and its discriminators. |
| **Contingent qualification promoted.** Temporary participation in a publication or another direct relation is given a durable U-kind. | The same individual appears to change kind merely because a relation starts or ends. | Keep the exact relation occurrence and use Plain relation-defined wording; for publication use Plain `published episteme` and E.24.PUB. |


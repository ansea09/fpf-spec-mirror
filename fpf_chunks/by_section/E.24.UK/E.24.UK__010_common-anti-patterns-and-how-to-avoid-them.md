---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 92686
line_end: 92697
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.2.6"
  - "A.22"
  - "A.6.0"
  - "A.6.5"
  - "A.6.RCD"
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
  - "F.17"
  - "F.18"
  - "F.8"
  - "U.Kind"
  - "U.SubkindOf"
keywords:
---

### E.24.UK:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| **U-dot by punctuation.** A heading or filename contains `U.` and therefore survives as a kind. | Public spelling outruns admission. | Apply the durable U-kind test; otherwise rename to the governed object. |
| **Participation or SlotKind becomes kind.** An entity receives a new U-kind because it participates in a relation, or a `RelationSignature` SlotKind is read as a world-side kind. | Participation meaning and reusable declaration are collapsed. | Keep the entity's independently governed kind, state the direct relation, and keep the SlotKind only inside its A.6.5 SlotSpec. |
| **Source type import.** A BFO, ISO, OWL, database, or programming-language type is copied as an FPF U-kind. | Source ontology and FPF ontic admission rules become mixed. | Use the source conversion guide and name the FPF governed object. |
| **Searchable title wins.** A memorable heading remains public even though the body governs a record, publication form, relation structure, or local frame. | Discoverability replaces ontology. | Keep the searchable phrase in entry or retrieval material if useful, and put the governed object in the public pattern name. |
| **Dependent kind promoted.** A dependent distinction is admitted as an independent root U-kind, or a root reference is treated as proof of dependence. | FPF grows duplicate roots, hides the root-inclusion law, or claims an unidentified dependence. | For the same individual, state the dependent membership predicate and its implication to root membership. For a distinct individual, cite an already governed exact dependence relation and its discriminators; otherwise stop admission at the missing governor. |
| **Structure specialization re-rooted.** A context, system, team, subsystem, model-use label, scope, method, work result, view, diagram, publication, or named use is treated as if it created a base structure or one of its specializations. | The A.22 four-discriminator identity is bypassed, and description, representation, use, or a pending label is mistaken for structure membership. | Identify the exact `U.Structure` under A.22 first. Add `BoundedModelUseStructure` only when its A.22:4.1c condition holds; apply the conditional crossing-analysis rule only after independently governed crossings and all four base discriminators exist. Otherwise retain the actual context-like, epistemic, representational, publication, or use object under its defining or testing rule. |
| **Contingent qualification promoted.** Temporary participation in a publication or another direct relation is given a durable U-kind. | The same individual appears to change kind merely because a relation starts or ends. | Keep the exact relation occurrence and use Plain relation-defined wording; for publication use Plain `published episteme` and E.24.PUB. |


---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Governance and Ontic Settlement Coupling"
section_id: "E.24.UK:6.1"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "E.24.UK — U-kind Governance and Ontic Settlement Coupling"
  - "E.24.UK:6.1 — Common Anti-Patterns and How to Avoid Them"
line_start: 77880
line_end: 77889
dependencies:
  - "A.11"
  - "A.6.5"
  - "A.8"
  - "C.3"
  - "C.3.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "F.18"
  - "F.5"
  - "F.8"
keywords:
---

### E.24.UK:6.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| **U-dot by punctuation.** A heading or filename contains `U.` and therefore survives as a kind. | Public spelling outruns admission. | Apply the durable U-kind test; otherwise rename to the governed object. |
| **Slot becomes kind.** `EvidenceRole`, `MethodRole`, or `DescriptionRole` is admitted because a value fills a relation position. | Slot-position label becomes a false ontology branch. | Keep SlotKind, ValueKind, RefKind, and governing pattern separate. |
| **Source type import.** A BFO, ISO, OWL, database, or programming-language type is copied as an FPF U-kind. | Source ontology and FPF ontic law become mixed. | Use the source conversion guide and name the FPF governed object. |
| **Searchable title wins.** A memorable heading remains public even though the body governs a record, publication form, relation structure, or local frame. | Discoverability replaces ontology. | Keep the searchable phrase in entry or retrieval material if useful, and put the governed object in the public pattern name. |
| **Dependent value promoted.** A value that depends on an existing ontic settlement is admitted as an independent root U-kind. | FPF grows duplicate roots for one ontological neighborhood. | Keep the root settlement and state the dependent durable value relation explicitly. |


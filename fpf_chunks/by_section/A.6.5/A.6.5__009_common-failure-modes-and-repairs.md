---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
section_id: "A.6.5:8"
section_title: "Common Failure Modes and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__009_common-failure-modes-and-repairs.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "A.6.5 — Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
  - "A.6.5:8 — Common Failure Modes and Repairs"
line_start: 17222
line_end: 17234
dependencies:
  - "A.6.0"
  - "A.6.P"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.24.UK"
keywords:
---

### A.6.5:8 - Common Failure Modes and Repairs

| Failure | Why it matters | Repair |
|---|---|---|
| `U.RelationSlotDiscipline` treated as a root kind | A rule set is promoted into an unsupported world-side entity. | Keep A.6.5 as the governing rules for `SlotSpec`; apply E.24.UK to any future U-kind candidate. |
| Generic `byRef` without an exact RefKind | A later use cannot tell what referent kind can be resolved. | Declare the exact RefKind, or expand the compact sketch next to its use. |
| Reference treated as the relation participant | A storage or publication choice changes the claimed world-side ontology. | Keep the referent as participant; state refMode only for the receiving assertion or description episteme that carries the designation. |
| One SlotSpec contains a ValueKind written as a list of unrelated alternatives | Different predicate semantics are hidden behind one participant meaning. | Recover the real common ValueKind when one exists; otherwise split the relation kind. |
| A SlotKind in a `RelationSignature` is called a role | A declaration-local SlotKind is confused with work-facing `U.Role`. | Use a `*Slot` name and keep `U.Role` as the ValueKind only when the actual participant is a role value. |
| Active grammar used as agency evidence | A relation, method, work, structure, or episteme is said to act. | Recover the acting `U.System`; keep relation, work, method, and transformation claims under their direct patterns. |
| `BoundedContextSlot` or optional `ModelUseStructureSlot` added to generic role assignment | A discarded universal context or use qualifier enters the direct participant declaration. | Use holder system, role value, role-taxonomy episteme, and effective reference scheme; keep any selected model-use structure in the receiving assertion or use. |
| A participant designation is promoted into a new qualification ontic | A value or reference in an episteme is mistaken for a further world-side object. | Apply the three-way dispatch in A.6.5:4.6: direct relation fact, assertion episteme, or current local participant kind. |


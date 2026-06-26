---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__012_rationale.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:10 — Rationale"
line_start: 16132
line_end: 16139
dependencies:
  - "A.1"
  - "A.2.1"
  - "A.6.0"
  - "A.6.2"
  - "A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.17.0"
  - "E.8"
  - "F.6"
  - "U.EpistemeSlotRelation"
  - "U.MultiViewDescribing"
  - "U.Signature"
keywords:
  - "argument position"
  - "pass-by-reference"
  - "pass-by-value"
  - "reference"
  - "signature"
  - "slot"
  - "substitution"
  - "value"
---

### A.6.5:10 - Rationale

FPF needs relations that are strong enough for engineering use but light enough for cross-domain pattern work. The SlotKind, ValueKind, and RefKind separation gives FPF a compact relation-position discipline without turning every relation into a new formal calculus.

The key design choice is modularity. `A.6.5` is central because many patterns need SlotSpecs. It remains narrow because relation identity, evidence authority, status meaning, role ontology, method admission, work execution, publication use, and architecture semantics belong to their own patterns.

The role decision is especially important. If every slot position is called a role, `U.Role` loses its work-facing meaning. If every episteme used as evidence gets an evidence role, FPF grows a second role ontology for epistemes. `A.6.5` keeps both errors visible: a role may fill a slot, but slot position labels do not create alternate ontology.


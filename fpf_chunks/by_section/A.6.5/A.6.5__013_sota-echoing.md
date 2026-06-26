---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__013_sota-echoing.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:11 — SoTA-Echoing"
line_start: 16140
line_end: 16149
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

### A.6.5:11 - SoTA-Echoing

| Practice line | FPF adoption |
|---|---|
| Typed records, row-polymorphic data, and effect-row practice distinguish field labels from field types and from effects or resources. | Adopt the structural lesson: position labels and filler kinds are separate. Adapt it into SlotKind, ValueKind, and RefKind so the same discipline applies to epistemes, roles, evidence-use relations, interfaces, and transformation-flow structures. |
| Dependent and refinement type practice makes admissible values depend on declared indices, contexts, and predicates. | Adopt the need to expose the admissibility predicate. In FPF, ValueKind compatibility and context-local subkind admission are named rather than hidden in prose. |
| Optics and lens practice manipulates focused positions in larger structures under composition laws. | Echo the focus-position idea: SlotKind names the focused position; ValueKind names the admitted filler; RefKind says whether the focused value is embedded or reached through a reference. |
| Database, protocol, and API schema practice separates schema declarations from records, messages, and runtime handling. | Adopt the declaration-instance separation. A SlotSpec describes a relation position; a filled relation instance, API call, evidence-use relation, or work occurrence is not the SlotSpec itself. |
| Contemporary architecture and interface practice treats ports, APIs, protocols, and connectors as heterogeneous description and boundary constructs rather than one universal interface type. | Adapt this by refusing generic `U.Interface`; recover the governing EntityOfConcern first, then use SlotSpecs only inside that recovered value. |


---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__005_forces.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:3 — Forces"
line_start: 16272
line_end: 16282
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

### A.6.5:3 - Forces

| Force | Tension |
|---|---|
| Simplicity vs expressiveness | Practitioners need a small vocabulary, but relation-bearing structures must still expose positions, filler kinds, reference modes, and change operations. |
| Reuse vs false unification | The same SlotSpec discipline should serve epistemes, signatures, role assignments, evidence-use relations, status-use relations, interfaces, services, and transformation-flow structures without pretending those relations are one relation kind. |
| Role ontology vs slot discipline | `U.Role` must stay a real work-facing role value, while relation positions must not be named as roles merely because they participate in a relation. |
| Description boundary vs instance filling | A pattern may describe a slot relation, while a project instance fills it. Description, publication, and filled relation values must stay distinct. |
| Tool alignment vs FPF ontology | Programming, database, type-system, and API practices already use parameters, fields, references, and updates, but FPF must recover their kinds before borrowing their words. |
| Binding-time clarity vs metaphor | "Early binding", "late binding", "assignment", and "update" are useful only when the affected link is named: name to slot, slot to content, or reference to referent. |


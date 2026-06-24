---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__011_consequences.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:9 — Consequences"
line_start: 16082
line_end: 16089
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

### A.6.5:9 - Consequences

`A.6.5` adds a small amount of explicit metadata to relation-bearing structures. The payoff is that substitutions, retargetings, evidence-use distinctions, role-assignment boundaries, interface claims, and episteme morphisms become reviewable.

It also prevents ontology overgrowth. A value filling a slot does not become a new kind because it is used in that slot. Conversely, a slot label does not become the value. This is the same discipline that keeps `U.Episteme` compact in `C.2.1` and keeps `U.Role` compact in the role `ontologicalNeighborhood`.

The cost is naming care. Authors must recover the current governing pattern before accepting a slot name. That is cheaper than maintaining several local ontologies for the same project situation. Reopen the governing pattern, not `A.6.5`, when a current case depends on relation identity, evidence authority, status meaning, role ontology, method admission, work execution, publication use, architecture semantics, or another value that SlotSpec discipline only references.


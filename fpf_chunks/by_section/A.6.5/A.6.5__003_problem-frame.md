---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__003_problem-frame.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:1 — Problem frame"
line_start: 15866
line_end: 15879
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

### A.6.5:1 - Problem frame

FPF relies on n-ary relations and operators throughout the corpus: episteme slot relations, role assignments, method and method-description signatures, evidence-use relations, status-use relations, service-access descriptions, interface specifications, architecture structures, view relations, transformation-flow structures, and formal-substrate declarations.

The same local phrase can hide three different things:

1. a named position in one relation-bearing structure;
2. the kind of value admitted at that position;
3. the reference or embedded value placed in one filled relation instance.

For example, `EntityOfConcernSlot`, `U.Entity`, and `entityOfConcernRef` are not three spellings for one thing. The first names a slot position. The second names a filler kind. The third is a filled reference field in an instance. When these layers are blurred, substitutions, retargetings, interface claims, role assignments, evidence-use relations, and episteme morphisms become hard to review.

The governing distinction is important: `A.6.5` supplies relation-slot discipline. It does not decide what a relation is in general, and it does not replace `U.Signature`. Relation identity remains with the pattern that governs the relation. Signature identity remains with `A.6.0`. `A.6.5` gives both of them a disciplined way to talk about positions and fillers.


---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__009_conformance-checklist.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:7 — Conformance Checklist"
line_start: 16436
line_end: 16448
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

### A.6.5:7 - Conformance Checklist

1. **SlotSpec completeness.** Every FPF-governed n-ary relation, operator, record, or signature vocabulary item introduced by the pattern names SlotKind, ValueKind, and refMode for each governed position.
2. **SlotKind locality.** SlotKind is interpreted relative to the governing relation-bearing structure; the same label does not float as a universal kind without a governing pattern.
3. **ValueKind separation.** ValueKinds remain governed by their own patterns and do not inherit `*Slot` or `*Ref` suffixes.
4. **RefKind honesty.** A `*Ref` name denotes a reference kind or a field typed by a reference kind, not the referent itself.
5. **Role boundary.** Role-valued slots may admit `U.Role` fillers, but SlotKinds are not roles and role labels do not create capability, method, status, evidence, or work.
6. **RoleAssignment boundary.** A work-facing `U.RoleAssignment` uses core SlotSpecs for holder, role value, bounded context, and assignment window; evidence-use and status-use relations are not folded into RoleAssignment.
7. **Evidence and status direct-pattern use.** Epistemes used as evidence, sources, standards, requirements, definitions, explanations, publications, status bearers, or assurance inputs are governed through direct evidence-use, source-use, publication-use, status-use, or assurance-use patterns, not through `U.RoleAssignment` for epistemes.
8. **Interface recovery.** Interface, API, port, protocol, connector, or endpoint wording is first recovered to its governing EntityOfConcern; `A.6.5` supplies only the SlotSpecs inside the recovered value.
9. **Operation verb discipline.** Slot changes use bind, fill, initialize, assign, retarget, substitute, resolve, revise, re-edition, or pass according to the link being changed.
10. **No generic relation replacement.** A pattern does not cite `A.6.5` as the governing source for relation identity, evidence authority, assurance, gate passage, method admission, work execution, or publication truth.


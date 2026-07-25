---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__006_solution.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:4 — Solution"
line_start: 92378
line_end: 92416
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.22.CGUS"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
---

### F.17:4 - Solution

A Unified Term Sheet is a table of term rows for one bounded unification thread.

Publish one term decision through this sequence:

1. Confirm that the direct pattern already governs the underlying value and its admissible use. If the kind, relation, slot position, or use is unsettled, return there before term publication.
2. Decide whether the name now needs durable reader-facing reuse: public publication, cross-context reuse, stable citation, training use, interface use, or editioned maintenance. Otherwise keep the wording local and stop.
3. Recover the bounded local senses and their context editions. Do not infer sameness from spelling.
4. Use F.18 and F.5 to select the Tech and Plain names for the governed value, and cite the resulting NameCard. If no NameCard decision is current, the term is not ready for F.17 publication.
5. When the row relates senses across contexts, cite the exact F.9 bridge, direction, congruence or loss, admitted use, and blocked reverse or stronger use. When no cross-context claim is made, add no bridge.
6. Publish one `UnifiedTermRow` with one governed term decision, direct pattern, selected names, senses, row rationale, admissible and blocked use, edition, and currentness condition. Split unlike governed values into separate rows.
7. Apply the static and regression checks, then stop at term publication. Any later object, evidence, authority, work, or subject-use claim returns to its direct pattern.

Each row has one primary term decision:

```text
UnifiedTermRow:
  UTSRowId
  UnificationThreadId
  Block
  GovernedValueRef: U.EntityRef
  GovernedValueKindRef: U.KindRef
  DirectGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  UnifiedTechName
  UnifiedPlainName
  NameCardRef: U.EntityRef, referencing one F.18 NameCard
  SenseCellRefs[]: SenseCellAddressRef, each resolving one F.3 SenseCell(ContextId, Local-SenseId) coordinate
  BridgeRefs[]: U.EntityRef, referencing F.9 Bridges
  RowRationale
  AdmissibleUse
  BlockedUse
  RowEdition
  CurrentnessCondition
  Notes?
```

The row may cite several local senses and several bridges, but it does not fuse their underlying objects. If a source phrase points toward multiple typed FPF values, split the row or cite the direct pattern that keeps the values distinct.


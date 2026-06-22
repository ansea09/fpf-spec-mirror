---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__006_solution.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:4 — Solution"
line_start: 80667
line_end: 80691
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "UTS"
  - "Unified Term Sheet"
  - "glossary"
  - "human-readable output"
  - "publication"
  - "summary table"
---

### F.17:4 - Solution

A Unified Term Sheet is a table of term rows for one bounded unification thread.

Each row has one primary term decision:

```text
UnifiedTermRow:
  UTSRowId
  ThreadContextRef
  GovernedObjectKindOrValueRef
  DirectGoverningPatternRef
  UnifiedTechName
  UnifiedPlainName
  NameCardRef?
  SenseCells[]
  BridgeRefs[]
  RowRationale
  RowEdition
  CurrentnessCondition
  Notes?
```

The row may cite several local senses and several bridges, but it does not fuse their underlying objects. If a source phrase points toward multiple typed FPF values, split the row or cite the direct pattern that keeps the values distinct.


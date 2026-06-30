---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:5"
section_title: "Minimal vocabulary"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__007_minimal-vocabulary.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:5 — Minimal vocabulary"
line_start: 86470
line_end: 86489
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

### F.17:5 - Minimal vocabulary

`UnifiedTermSheet` is the whole reader-facing term table for one bounded unification thread.

`UnifiedTermRow` is one row in that sheet. It publishes one reviewed term decision.

`ThreadContextRef` names the bounded context and edition in which the sheet is current.

`GovernedObjectKindOrValueRef` names the specified kind, local concept, relation, slot kind, status family, role, or other governed value being named. Use an admitted durable U-kind, C.3 `U.Kind`, or direct governed value kind only when that is the recovered object. Do not force local concepts, slot kinds, relation kinds, status values, or role assignments into a generic kind container.

`DirectGoverningPatternRef` names the pattern that owns the underlying object or claim. `F.17` owns the term-row publication, not the object.

`SenseCell` is a bounded-context local sense reference. It names the context, edition, local expression, local sense, and source reference when source use is current.

`BridgeRef` cites an `F.9` bridge when one row uses senses from more than one bounded context or when sameness, near-identity, retargeting, or loss matters.

`UnifiedTechName` and `UnifiedPlainName` are the selected names governed by `F.5` and `F.18`. Extra aliases belong in the name-card or local lexicon material, not as rival unified names in the row.

`BlockPlan` is the didactic grouping of rows. A block is a memory and teaching device, not an ontological parent.


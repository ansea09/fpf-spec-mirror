---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__006_solution.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:4 — Solution"
line_start: 93517
line_end: 93555
dependencies:
  - "A.1.1"
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
  - "C.2.1"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
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
  - "U.BoundedContext"
keywords:
---

### F.17:4 - Solution

A Unified Term Sheet is a table of term rows for one bounded unification thread.

Publish one term decision through this sequence:

1. Confirm that the direct pattern already governs the underlying value and its admissible use. If the kind, relation, slot position, or use is unsettled, return there before term publication.
2. Decide whether the name now needs durable reader-facing reuse: public publication, reuse across different semantic-context projections, stable citation, training use, interface use, or editioned maintenance. Otherwise keep the wording local and stop.
3. Recover each exact local sense under one effective `U.ReferenceScheme` carried by value. Cite a `SenseCellAddressRef` that resolves to the F.17 scheme-based coordinate `<reference scheme by value, local expression, local-sense claim>`; do not require or infer a `U.BoundedContext`.
4. Use F.18 and F.5 to select the Tech and Plain names for the governed value, and cite the resulting NameCard. If no NameCard decision is current, the term is not ready for F.17 publication.
5. When the row proposes correspondence between local senses whose `<ReferenceScheme, LocalSenseClaim>` projections differ, cite two premises in order. The projections may differ because the `LocalSenseClaim` differs even when the `ReferenceScheme` is the same; different schemes are only a common subset and do not establish a Bridge. First cite an actual F.9 Bridge for the named endpoint cells and editions and show that its relation-semantic profile applies, its Boolean predicate is true, and its required dependencies are present. Second cite an exact current C.2.1 claim with that Bridge as EntityOfConcern and affirmative polarity for the row's named use, direction, use-specific correspondence rule, and permitted-loss tolerance. Recover current reliance through the exact A.10 evidence-provenance relation plus local `RelianceDisposition=pass`, or the positive B.3 assurance branch when B.3 is triggered. A negative claim or non-passing reliance rejects or weakens the row use without negating or reidentifying an otherwise obtaining Bridge. When the projections are the same, route a different expression to F.18 designation and add no Bridge. When no semantic-correspondence use is current, add no Bridge or Bridge-use claim regardless of how many schemes are present.
6. Publish one `UnifiedTermRow` with one governed term decision, direct pattern, selected names, scheme-based sense coordinates, row rationale, admissible and blocked use, edition, and currentness condition. Split unlike governed values into separate rows.
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
  SenseCellRefs[]: SenseCellAddressRef, each resolving one F.17 SchemeSenseCell(ReferenceScheme, LocalExpression, LocalSenseClaim) coordinate
  BridgeRefs[]: U.EntityRef, referencing actual F.9 Bridges only; any AdmissibleUse between different semantic-context projections separately cites its exact C.2.1 claim and A.10 or B.3 reliance basis in the row rationale or notes
  RowRationale
  AdmissibleUse
  BlockedUse
  RowEdition
  CurrentnessCondition
  Notes?
```

The row may cite several local senses and several Bridges, but it does not fuse their underlying objects. If a source phrase points toward multiple typed FPF values, split the row or cite the direct pattern that keeps the values distinct.


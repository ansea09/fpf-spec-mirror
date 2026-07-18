---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:5"
section_title: "Minimal vocabulary"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__007_minimal-vocabulary.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:5 — Minimal vocabulary"
line_start: 89509
line_end: 89577
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

### F.17:5 - Minimal vocabulary

#### F.17:5.1 - Local-sense basis relation

A local sense is not grounded merely because its expression has an accepted name. When a `SenseCell` relies on a public pattern, publication expression, seminar expression, or another episteme, use the following local relation species. It is a relation about support for one bounded local-sense line, not evidence that the governed subject claim is true.

```text
LocalSenseBasisRelation@Context <: U.Relation
SlotSpecs:
  LocalSenseCellSlot:
    ValueKind: F.3 SenseCell coordinate = (U.BoundedContext, Local-Sense); this is a direct governed coordinate value, not a U-kind
    RefKind: SenseCellAddressRef, the F.17-local reference form resolving either SenseCell(ContextId, Local-SenseId) or ContextId:LocalLabel under E.10.D1
    Field: localSenseCellRef
  BasisEpistemeSlot:
    ValueKind: U.Episteme
    RefKind: U.EpistemeRef
    Field: basisEpistemeRef
  BasisEpistemeKindSlot:
    ValueKind: U.Kind
    RefKind: U.KindRef
    Field: basisEpistemeKindRef
    Constraint: resolves to the exact kind of basisEpistemeRef
  BasisPublicationUnitSlot?:
    ValueKind: PublicationUnit under E.17.AUD
    RefKind: PublicationUnitRef
    Field: basisPublicationUnitRef
  BoundedContextSlot:
    ValueKind: U.BoundedContext
    RefKind: U.BoundedContextRef
    Field: boundedContextRef
RelationRefKind: U.EntityRef constrained to LocalSenseBasisRelation@Context
Direction: basisEpistemeRef -> localSenseCellRef
Dependence: the relation depends on the named bounded-context edition, the current basis-episteme edition, and the cited PublicationUnit when present
Identity: <localSenseCellRef, basisEpistemeRef, basis episteme edition, boundedContextRef, basisPublicationUnitRef if present>

LocalSenseBasisRelationDescription@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one LocalSenseBasisRelation@Context
  entityOfConcernKindRef: U.KindRef, referencing LocalSenseBasisRelation@Context
  boundedContextRef: U.BoundedContextRef
  viewpointRef: U.ViewpointRef
  subjectRef: U.SubjectRef, decoding to <entityOfConcernRef, boundedContextRef, viewpointRef>
  groundingHolonRef?: U.HolonRef
  claimGraph: U.ClaimGraph by value, carrying the supported-sense claim, admitted-use claim, and non-admitted-use claim
  referenceScheme: U.ReferenceScheme by value
  editionId
```

`SenseCellAddressRef` addresses the F.3 coordinate without minting a SenseCell U-kind; resolving it yields the exact `(U.BoundedContext, Local-Sense)` pair and context edition. `basisPublicationUnitRef` has RefKind `PublicationUnitRef` and narrows a relied-on pattern or publication to the exact bounded unit when that precision matters. It does not turn a file, slide carrier, or rendering into the supporting episteme.

The relation says only that the named basis episteme, optionally at one publication unit, is the basis for the named SenseCell coordinate in the bounded context. `LocalSenseBasisRelationDescription@Context` says which local-sense claim is supported and which uses are admitted or blocked. Changing only the NameCard reopens the selected expression. Changing the SenseCell address, basis episteme edition, bounded context, or cited publication unit reopens the relation. Changing only the supported-sense claim or use boundary creates a new relation-description edition while preserving the relation when its identity tuple remains unchanged.

`UnifiedTermSheet` is the whole reader-facing term table for one bounded unification thread.

`UnifiedTermRow` is one local F.17 publication-row form in that sheet. It publishes one reviewed term decision and is not a root U-kind or the underlying governed value.

`UnificationThreadId` identifies the bounded naming thread that groups this row with related term decisions. It is a sheet-local identifier, not a `U.BoundedContext`; bounded contexts and their editions remain explicit in `SenseCellRefs`, while `RowEdition` identifies the row edition.

`GovernedValueRef` references the exact value being named. `GovernedValueKindRef` separately references its kind. When the term names a kind token, such as `DemonstrativeUnfoldingSlice@Context`, the governed value is that token and its kind is `U.Kind`; the direct subject pattern states which kinds of instances the token admits. When the term names a role value, relation value, status value, slot kind, or local concept, the two positions reference that value and its exact governed kind. No union field or generic kind container substitutes for this pair.

`DirectGoverningPatternRef` names the pattern that owns the underlying value or claim. `F.17` owns the term-row publication, not that value.

`SenseCell` is a bounded-context local sense coordinate from `F.3`. It names the context, edition, local expression, and local sense. `SenseCellAddressRef` is the F.17-local RefKind for that coordinate; it does not mint a SenseCell U-kind. A `NameCardRef` may accompany the cell when its local expression relies on an `F.18` naming settlement. A separate `LocalSenseBasisRelationRef` relates the SenseCell coordinate to the episteme that supports it; the relation description carries the supported-sense and use-boundary claims, and the NameCard fills neither position.

`BridgeRef` cites an `F.9` bridge when one row uses senses from more than one bounded context or when sameness, near-identity, retargeting, or loss matters.

`UnifiedTechName` and `UnifiedPlainName` are the selected names governed by `F.5` and `F.18`. Extra aliases belong in the name-card or local lexicon material, not as rival unified names in the row.

`BlockPlan` is the didactic grouping of rows. A block is a memory and teaching device, not an ontological parent.


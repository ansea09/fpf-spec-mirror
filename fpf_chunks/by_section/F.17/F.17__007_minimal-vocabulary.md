---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:5"
section_title: "Minimal vocabulary"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__007_minimal-vocabulary.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:5 — Minimal vocabulary"
line_start: 93875
line_end: 93947
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

### F.17:5 - Minimal vocabulary

#### F.17:5.1 - Scheme-based local-sense coordinate and basis relation

A local sense is not grounded merely because its expression has an accepted name. F.17 therefore separates the scheme-based local-sense coordinate, the naming settlement, and any episteme used as the basis for the sense claim.

```text
SchemeSenseCell:
  ValueKind: F.17-local composite coordinate; not a root U-kind
  ReferenceScheme: U.ReferenceScheme carried by value
  LocalSenseId: address designator only
  LocalExpression
  LocalSenseClaim
  Identity: <ReferenceScheme by value, LocalExpression, LocalSenseClaim>

LocalSenseBasisRelation@Context <: U.Relation
SlotSpecs:
  LocalSenseCellSlot:
    ValueKind: F.17 SchemeSenseCell coordinate
    RefKind: SenseCellAddressRef, resolving SenseCell(ReferenceSchemeId, LocalSenseId) to the exact scheme, expression, and local-sense claim
    Field: localSenseCellRef
  BasisEpistemeSlot:
    ValueKind: U.Episteme
    RefKind: U.EpistemeRef
    Field: basisEpistemeRef
    Constraint: the reference resolves to the exact basis-episteme kind; that kind is derived, not copied as another participant
  BasisPublicationUnitSlot?:
    ValueKind: PublicationUnit under E.17.AUD
    RefKind: PublicationUnitRef
    Field: basisPublicationUnitRef
RelationRefKind: U.EntityRef constrained to LocalSenseBasisRelation@Context
Direction: basisEpistemeRef -> localSenseCellRef
Obtaining: the exact current basis-episteme edition, at the cited PublicationUnit when present, supports the coordinate's exact LocalSenseClaim under the coordinate's by-value ReferenceScheme for the stated admitted use
NonObtaining: shared spelling, a NameCard, a file or carrier, publication availability, or an uncited source title does not make this relation obtain
Identity: <localSenseCellRef, basisEpistemeRef, basisPublicationUnitRef if present>; the scheme, expression, and sense claim are already identity-bearing inside localSenseCellRef, and the episteme edition is already identity-bearing inside basisEpistemeRef
OccurrenceIdentity: participant-determined; changed coordinate, basis-episteme edition, or cited publication unit identifies another occurrence

LocalSenseBasisRelationDescription@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one LocalSenseBasisRelation@Context
  entityOfConcernKindRef: U.KindRef, referencing LocalSenseBasisRelation@Context
  viewpointRef?: U.ViewpointRef
  subjectRef?: U.SubjectRef, only when independently governed and without adding a context participant
  claimGraph: U.ClaimGraph by value, carrying the supported-sense claim, admitted-use claim, and non-admitted-use claim
  referenceScheme: U.ReferenceScheme by value; exactly the scheme in localSenseCellRef
  editionId
```

`SenseCellAddressRef` is the F.17 reference form for `SchemeSenseCell`. Its readable `SenseCell(...)` spelling is an address, not a claim that a SenseCell is a U-kind or that a context holon exists. A legacy F.3 address of the form `SenseCell(ContextId, LocalSenseId)` may be consumed only when an explicit adapter resolves `ContextId` to one exact effective reference scheme and the same local expression and sense claim. If that resolution is absent or lossy, stop the row; do not reconstruct `U.BoundedContext`.

The retained `@Context` suffix on `LocalSenseBasisRelation@Context` is lineage-compatible vocabulary for bounded local use, not a participant declaration. New occurrences have no `U.BoundedContext` slot. A legacy record may retain `boundedContextRef` only as non-participant address metadata when it resolves to the same exact scheme-based coordinate; otherwise that record is not current for an F.17 row.

`basisPublicationUnitRef` narrows a relied-on pattern or publication episteme to the exact bounded unit when that precision matters. It does not turn a file, slide carrier, rendering, or publication occurrence into the supporting episteme.

The basis relation says only that the named episteme supports the named local-sense claim for the stated use. Its description says which claim is supported and which uses are admitted or blocked. A changed NameCard reopens the selected expression. A changed scheme, local expression, local-sense claim, basis-episteme edition, or cited publication unit identifies or selects another basis occurrence. A changed supported-use boundary creates another relation-description edition without silently changing the basis relation.

`UnifiedTermSheet` is the whole reader-facing term table for one bounded unification thread.

`UnifiedTermRow` is one local F.17 publication-row form in that sheet. It publishes one reviewed term decision and is not a root U-kind or the underlying governed value.

`UnificationThreadId` identifies the bounded naming thread that groups this row with related term decisions. It is a sheet-local identifier, not an ontological locality bearer; `RowEdition` identifies the row edition.

`GovernedValueRef` references the exact value being named. `GovernedValueKindRef` separately references its kind. When the term names a kind token, such as `DemonstrativeUnfoldingSlice@Context`, the governed value is that token and its kind is `U.Kind`; the direct subject pattern states which kinds of instances the token admits. When the term names a role value, relation value, status value, slot kind, or local concept, the two positions reference that value and its exact governed kind. No union field or generic kind container substitutes for this pair.

`DirectGoverningPatternRef` names the pattern that owns the underlying value or claim. `F.17` owns the term-row publication, not that value.

`SchemeSenseCell` is the exact F.17 local-sense coordinate. It binds one local expression and sense claim to one effective `U.ReferenceScheme` carried by value. A `NameCardRef` may accompany it when F.18 selected the expression. A separate `LocalSenseBasisRelationRef` relates the coordinate to a supporting episteme; the relation description carries the supported-sense and use-boundary claims, and the NameCard fills neither position.

`BridgeRef` cites an actual F.9 Bridge only when it obtains for the exact scheme-based endpoints under a relation-semantic profile that applies, has a true Boolean predicate, and has every required dependency present. The reference carries no row-use direction, rule, tolerance, polarity, reliance, or permission. An `AdmissibleUse` between different `<ReferenceScheme, LocalSenseClaim>` projections separately cites the exact affirmative C.2.1 claim about that Bridge and names its current A.10 or B.3 reliance basis. A scheme difference alone supplies neither premise.

`UnifiedTechName` and `UnifiedPlainName` are the selected names governed by F.5 and F.18. Extra aliases belong in the NameCard or local lexicon material, not as rival unified names in the row.

`BlockPlan` is the didactic grouping of rows. A block is a memory and teaching device, not an ontological parent.


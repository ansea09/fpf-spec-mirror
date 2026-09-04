---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:5"
section_title: "Minimal vocabulary"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__007_minimal-vocabulary.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:5 — Minimal vocabulary"
line_start: 98541
line_end: 98628
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
  - "E.10.LRN"
  - "E.10.MOVE"
  - "E.11"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
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

#### F.17:5.1 - Scheme-based local-sense coordinate, basis relation, and row episteme

A selected expression, an exact local sense, the episteme supporting that sense, the naming decision, and the reader-facing row answer different questions. Keep them independently recoverable.

```text
SchemeSenseCell:
  ValueKind: F.17-local composite coordinate; not a root U-kind
  ReferenceScheme: effective U.ReferenceScheme carried by value
  LocalSenseId: address designator only
  LocalExpression: selected expression in this local use
  LocalSenseClaim: exact local meaning under the scheme
  Identity: <ReferenceScheme by value, LocalExpression, LocalSenseClaim>

LocalSenseBasisRelation <: U.Relation
SlotSpecs:
  LocalSenseCellSlot:
    ValueKind: F.17 SchemeSenseCell coordinate
    RefKind: SenseCellAddressRef resolving the exact scheme, expression, and sense claim
    Field: localSenseCellRef
  BasisEpistemeSlot:
    ValueKind: U.Episteme
    RefKind: U.EpistemeRef resolving one exact basis-episteme edition
    Field: basisEpistemeRef
Direction: basisEpistemeRef -> localSenseCellRef
Obtaining: the exact basis episteme supports the cell's exact LocalSenseClaim under its by-value ReferenceScheme for the stated admitted use
NonObtaining: shared spelling, accepted name, card, source title, file, carrier, publication availability, or completed fields
Identity: <localSenseCellRef, basisEpistemeRef>
OccurrenceIdentity: participant-determined; another exact cell or basis-episteme edition identifies another occurrence

LocalSenseBasisRelationDescription <: U.Episteme:
  entityOfConcernRef: U.EntityRef resolving one exact LocalSenseBasisRelation occurrence
  entityOfConcernKindRef: U.KindRef resolving LocalSenseBasisRelation
  viewpointRef?: U.ViewpointRef
  subjectRef?: U.SubjectRef, only when independently governed
  basisPublicationUnitRef?: U.EntityRef resolving one exact source unit as description/provenance content, never as relation participant or identity discriminator
  claimGraph: U.ClaimGraph carrying supported-sense, admitted-use, blocked-use, and any exact source-unit qualifier claims
  referenceScheme: U.ReferenceScheme by value; exactly the scheme in localSenseCellRef
  editionId: designator only

UnifiedTermRow <: U.Episteme:
  UTSRowId: stable designator only
  UnificationThreadId: sheet-local navigation designator
  Block?: optional didactic navigation label
  GovernedValueRef: U.EntityRef; the same exact referent fills the C.2.1 EntityOfConcern position
  ClaimContent: complete U.ClaimGraph constituted by the identity-bearing row claims designated below
  ReferenceScheme: effective U.ReferenceScheme carried by value
  GovernedValueKindRef: U.KindRef
  SubjectPatternLocator: U.EntityRef resolving the pattern that defines or constrains the governed value
  UnifiedTechName: selected Tech designation expression
  UnifiedPlainName: selected Plain designation expression
  NameCardRef: U.EpistemeRef resolving the separate exact F.18 naming-settlement episteme
  SenseCellRefs[]: exact SenseCellAddressRefs
  BridgeRefs[]?: actual F.9 Bridge occurrences only
  RowRationale
  AdmissibleUse
  BlockedUse
  RowEditionId: designator only
  EpistemeEditionRelationRef?: exact C.2.1 occurrence only when historical continuation obtains
  CurrentnessCondition
  Notes?
```

`SenseCellAddressRef` designates one `SchemeSenseCell`; it does not create that cell or a universal context object. A legacy address is usable only through an explicit lossless adapter to the exact effective scheme, expression, and local-sense claim. Otherwise stop the row.

The basis relation has exactly two participants. `basisEpistemeRef` resolves the exact current basis-episteme edition; its exact kind is derived from that referent and is not copied as another participant. A relation reference resolves the exact `LocalSenseBasisRelation` occurrence rather than its description or designator. `basisPublicationUnitRef`, when present, is a provenance qualifier that narrows the supporting episteme; it neither participates in nor identifies the relation. A source publication occurrence, its form, and its carrier remain separate E.24.PUB objects.

The relation says only that this basis episteme supports this cell's exact sense claim for the admitted use. Its description states the supported and blocked uses and any exact source-unit qualifier. A changed NameCard reopens the selected expression. A changed scheme, expression, sense claim, or basis-episteme edition identifies another cell or basis-relation participant pair. A changed source-unit or supported-use claim creates another relation-description episteme without silently changing the basis relation.

Any description of a `SchemeSenseCell` is a separate C.2.1 episteme whose EntityOfConcern is that exact cell. The cell's identifier, description, source publication, NameCard, and basis relation neither replace nor identify the cell.

`UnifiedTermRow` is another C.2.1 episteme, not a root U-kind, value container, or publication occurrence. Its EntityOfConcern is the exact governed value. Its displayed identity-bearing row claims jointly constitute the complete ClaimContent; a scalar graph-ref line need not be repeated in the readable fixture when that graph is recoverable from them. The claim graph cites the separate NameCard and the governed value's kind, locates the rules that define or constrain that value, and projects the selected designation expressions. The row, card, designations, governed value, external row reference, and `UTSRowId` designator remain distinct; `UnificationThreadId`, `Block`, and `RowEditionId` are navigation or edition designators rather than additional identity discriminators.

If a later row episteme revises, refines, or supersedes an earlier one, an independently obtaining C.2.1 `EpistemeEditionRelation(earlierRowEpisteme, laterRowEpisteme)` carries historical continuation. Stable row spelling, id, table position, shared carrier, or later publication establishes no such relation. A `CurrentnessCondition` is row claim content; it is not the edition relation and does not make itself true.

When a selected row edition must be made available, E.24.PUB supplies three separate relations: `PublicationFormExpressionRelation(selectedRowEdition, publicationForm, boundedUseDeclaration)`, `PublicationFormBearingRelation(carrier, publicationForm)`, and `EpistemePublicationRelation(selectedRowEdition, audience, boundedUse, publicationForm, carrier)`. The row does not publish itself; the form is not the row; the carrier bears the form rather than the episteme; rendering or uploading is dated Work when current and is not the publication occurrence.

`GovernedValueRef` and `GovernedValueKindRef` are separate. A kind token has kind `U.Kind`. An exact local system-role kind, obtaining system-role-assignment or other relation occurrence, status value, slot kind, representation position, or local concept retains its own kind; the row points to the pattern that defines or constrains that value. A row or card cannot admit a U-kind or make a direct relation obtain.

`NameCardRef` resolves the F.18 C.2.1 naming-decision episteme consumed by the current public-row gate. `UnifiedTechName` and `UnifiedPlainName` are designation expressions selected by that decision, not values or references. Aliases and rejected candidates stay in the NameCard or local lexicon rather than becoming rival selected names in the row.

`BridgeRefs` cites only actual F.9 occurrences between exact cells. Direction, use-specific rule, loss tolerance, polarity, evidence, reliance, permission, and receiving action remain in their own claims and relations. Local senses do not globalize; same spelling or a different scheme provides neither governed-value identity nor Bridge obtaining.

A.22.CGUS:4.4 permits a separately constituted demonstrative-slice episteme after CGUS qualification. The token `DemonstrativeUnfoldingSlice@Context` is neither a `U.Kind` nor an exact slice by itself. F.17 records a row only after one exact C.2.1 slice episteme and its current F.18 naming settlement are recoverable; a local phrase or seminar expression alone creates neither.

`UnifiedTermSheet` is the reader-facing collection or layout through which rows are found. A selected table layout, optional block plan, or carrier is not the row episteme and does not prove that every needed decision is present.


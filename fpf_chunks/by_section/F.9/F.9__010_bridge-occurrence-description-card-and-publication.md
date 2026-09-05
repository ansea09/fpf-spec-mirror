---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:8"
section_title: "Bridge occurrence, description, Card, and publication"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__010_bridge-occurrence-description-card-and-publication.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:8 — Bridge occurrence, description, Card, and publication"
line_start: 95799
line_end: 95829
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "C.3"
  - "E.10.ROLE"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "F.0.1"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "different <ReferenceScheme"
  - "exact F.17 SchemeSenseCell endpoints"
  - "inverse/composition checks"
  - "obtaining Bridge"
  - "optional CL evidence-strength shorthand"
  - "optional card"
  - "quantum/coarsening exit"
  - "relation-semantic profile"
  - "separate C.2.1 bounded-use claim"
---

### F.9:8 - Bridge occurrence, description, Card, and publication

Recover and, when needed, individuate the direct relation before describing it. A Bridge may obtain without any assertion, description, Card, registry row, or publication.

A Bridge occurrence description is constituted independently under C.2.1 from exact claim content, the already individuated occurrence as EntityOfConcern, and an effective `U.ReferenceScheme`. A proposal may instead be a modal C.2.1 episteme whose EntityOfConcern is the admitted direct Bridge relation kind and whose ClaimGraph designates proposed endpoints and profile; it supplies no positive occurrence reference and makes no relation obtain.

Use a Bridge Card only when durable reuse, delayed handoff, evidence review, audit, publication, or costly reversal makes reusable packaging worthwhile. A particular filled Card can be the description episteme when its C.2.1 triple supports that exact use. Its reusable layout remains separate and functions as a publication form only while the exact E.24.PUB `PublicationFormExpressionRelation` obtains for the selected edition and bounded use. When availability matters, publish one selected description/Card edition through E.24.PUB: its `EpistemePublicationRelation` occurrence, publication form, and `U.PresentationCarrier` remain distinct from the selected episteme and from the Bridge.

```text
BridgeCard:
  ClaimMode: actual | candidate | negative
  BridgeOccurrenceRef?: exact ref, actual mode only
  EntityOfConcern: exact obtaining Bridge, or admitted F.9 Bridge relation kind for candidate or negative mode
  ProposedSourceSenseCellRef?: SenseCellAddressRef
  ProposedReceivingSenseCellRef?: SenseCellAddressRef
  ProposedBridgePredicateProfile?: by-value profile
  BoundedUseClaims?: each with u, d, r, t, polarity, and effective ReferenceScheme
  A10EvidenceUse?: exact evidence-provenance relation plus local RelianceDisposition
  B3Use?: exact AssuranceResult for the same bounded assurance use
  ObservedLossAndCounterexamples?:
  EvidenceWarrantAndCurrentness?:
  NearestNonUse?:
  CardReferenceScheme:
```

For `ClaimMode: actual`, the description/Card episteme's exact EntityOfConcern is the already individuated Bridge occurrence. It may package the Bridge assertion, one or more bounded-use propositions, their evidence and polarity, the exact A.10 relation and local disposition, or the exact B.3 `AssuranceResult` when an actual named assurance claim is current, plus currentness and nearest non-use. Its C.2.1 identity is not the occurrence identity.

For `ClaimMode: candidate` or `negative`, no positive occurrence reference exists. The modal description/Card episteme's EntityOfConcern is the admitted F.9 direct `Bridge` relation kind; its ClaimGraph designates the proposed endpoints and profile. `candidate` says the proposed Bridge may obtain; `negative` says its predicate does not obtain. Any bounded-use proposition in the same graph keeps its own polarity. Completing, approving, registering, or publishing the description/Card creates no Bridge.

The exact `<ClaimGraph, EntityOfConcern, effective ReferenceScheme>` triple identifies each description/Card episteme. A changed description or Card edition, evidence path, reliance disposition, B.3 `AssuranceResult`, registry record, E.24.PUB publication occurrence, publication form, carrier, or layout does not reidentify a fixed Bridge. Publish only the selected description/Card edition needed by the named audience and bounded use; publication changes availability, not relation truth.


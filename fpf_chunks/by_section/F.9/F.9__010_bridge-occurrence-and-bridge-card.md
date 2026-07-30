---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:8"
section_title: "Bridge occurrence and Bridge Card"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__010_bridge-occurrence-and-bridge-card.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:8 — Bridge occurrence and Bridge Card"
line_start: 91153
line_end: 91179
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.17.ID.CR"
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

### F.9:8 - Bridge occurrence and Bridge Card

Recover the direct relation before describing it. A Bridge may obtain without any card. Use a card only when durable reuse, delayed handoff, evidence review, audit, publication, or costly reversal makes a reusable claim package worthwhile.

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
  B3Use?: positive assurance claim plus sufficient record, or exact non-positive disposition
  ObservedLossAndCounterexamples?:
  EvidenceWarrantAndCurrentness?:
  NearestNonUse?:
  CardReferenceScheme:
```

For `ClaimMode: actual`, the card's exact EntityOfConcern is the already individuated Bridge occurrence. The card may package the Bridge claim, one or more bounded-use propositions, their evidence and polarity, the exact A.10 relation and local disposition or the selected B.3 branch, currentness, and nearest non-use.

For `ClaimMode: candidate` or `negative`, no positive occurrence reference exists. The card's EntityOfConcern is the admitted F.9 direct `Bridge` relation kind. Its ClaimGraph designates the proposed endpoints and profile. `candidate` states that the proposed Bridge may obtain; `negative` states that its predicate does not obtain. Any bounded-use proposition in the same graph keeps its own polarity. Completing, approving, registering, or publishing this card creates no Bridge.

The exact `<ClaimGraph, EntityOfConcern, effective ReferenceScheme>` triple identifies the card episteme. A changed card edition, evidence path, reliance disposition, assurance claim or disposition, registry record, publication occurrence, form, carrier, or layout does not reidentify a fixed Bridge.


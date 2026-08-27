---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:1"
section_title: "Primary EntityOfConcern and applicability-row scope"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__007_primary-entityofconcern-and-applicability-row-scope.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:1 — Primary EntityOfConcern and applicability-row scope"
line_start: 75517
line_end: 75546
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.SPR"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.25"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.P"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.MOVE"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.2"
  - "E.20"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.10.ARCH:1 - Primary EntityOfConcern and applicability-row scope

The primary `EntityOfConcern` for this pattern use is the pattern-local authoring and publication architecture of `WordingUseRestorationApplicabilityRow` rows. The row is not the project object exposed by the wording and is not a practitioner artifact.

A row may use `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, and `ontologicalNeighborhood` as author-facing routing coordinates. Its minimum semantic content is:

- the recurring wording use recognized by `E.10`;
- the exact governed entity, value, episteme, obtaining direct relation, or representation exposed by that use;
- the exact claim or use being made;
- the rule that defines or constrains that object, relation, or representation, and the pattern ID that locates the rule;
- the repaired wording;
- the admissible reader use that survives; and
- the blocked stronger reading.

Declaration, designation, reference, publication, or representation fields are optional and appear only when the current repair needs them. A reusable relation declaration names its `RelationSignature` and A.6.5 `SlotSpec` values. A current assertion or relation-occurrence-description episteme may carry participant designations. A publication form or C.29 representation element names its represented object and explicit correspondence. An E.24 `onticSlotRelation` appears only when durable ontic settlement is itself current. None of these optional objects becomes a field of the governed entity merely because the authoring row cites it.

`WordingUseRestorationApplicabilityRow` is not a `U.*` kind, conformance object, process task, deontic obligation, or durable project artifact. Ordinary engineers do not fill it. They receive the shortest practitioner-facing sentence that identifies the governed object, direct relation or claim, and remaining action-facing use.

`WordingUseRestorationApplicabilityTable` is the pattern-local publication table of such rows. It is not a pattern cluster, workstream, campaign, module, semantic parent, or authority-bearing object.

`semanticAreaBaseConcept` is the Base concept, source wording span, or already settled row cue by which an author first recognizes the candidate semantic unit.

`semanticArea` is the Part-F semantic unit used by one wording-use restoration row: one Concept-Set row, one UTS row, or an explicitly bounded row-set whose rows remain sense-uniform enough for one recovery architecture.

`semanticAreaSenseFamily` is the Part-F `senseFamily` or FPF kind named by value-family discriminator that prevents the row from becoming a theme, domain, workstream, or pattern-nest label.

`ontologicalNeighborhood` means the FPF applicability neighborhood around that named `semanticArea`: the exact governed objects, admissible adjacent objects and relations, subject patterns, use boundaries, and optional declaration, description, publication, reference, or representation objects needed by the current repair. It is not textual, filename, ToC, alphabetic, topic, discipline, domain, workstream, or pattern-nest proximity.

`pattern nest` means a numbering or placement grouping such as `A.6.*`, `C.16.*`, or `C.30.*`. One applicability row may point to a realization pattern in one pattern nest, but the row and the nest are not the same concept.


---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:12"
section_title: "Archetypal Grounding - worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__014_archetypal-grounding-worked-cases.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:12 — Archetypal Grounding - worked cases"
line_start: 95489
line_end: 96119
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

### F.17:12 - Archetypal Grounding - worked cases

#### F.17:12.1 - Role name becomes public across two project contexts

One project has an exact design-review role value and an independently governed external-audit role value. Both local expressions say `reviewer`, but one concerns a system-in-role performing design-review Work and the other concerns an assurance actor producing an audit report.

The UTS row does not declare one universal reviewer. It either creates two rows or, when one naming use between different semantic-context projections is genuinely needed, cites an obtaining F.9 Bridge plus an affirmative C.2.1 claim that names the use direction, label rule, and tolerated loss. Each row cites the direct role pattern, the RoleDescription when current, and the `F.18` NameCardRef. A.10 or B.3 governs reliance on the use claim; no row or card creates a role assignment or review Work.

#### F.17:12.2 - Status label looks like a role name

A team proposes `BlockedReviewer` as a public label. F.17 does not accept it as a row until the direct patterns are separated. `Reviewer` is a role value; `blocked` is a status-family value or status-window value. The sheet may publish `Reviewer` as a role row and `Blocked` as a status row, with a note that a local UI may render them together. The table does not create a role called "blocked reviewer".

#### F.17:12.3 - Relation and slot names become reusable

An architecture pattern needs public names for `interfaceSlot`, `providedPort`, and `requiredPort`. The UTS row cites `A.6.5` for slot discipline, `A.6.RSIR` when the relation-signature-interface boundary is current, and `F.18` for durable names. The row does not treat a slot name as a component, role, or capability. If a project context uses `port` differently, the UTS row keeps the local sense and bridge explicit.

#### F.17:12.4 - Misleading evidence-role row

A sheet has a row labelled `Evidence role`. F.17 repairs the row by recovering the governed object instead of treating that label as a U-kind. If the claim is that an episteme is being used as evidence for another claim, `A.10`, `B.3`, or `A.2.4` governs the evidence relation. If the claim is that a system performs evidence-producing work, `A.2.1`, `F.6`, and `A.15.1` govern role assignment and performed work. The UTS may publish names for these values; a generic evidence-role row that fuses them is not admitted.

#### F.17:12.4a - Manufacturing batch across material and planning contexts

A furnace team uses `batch` for one physically handled set of shafts that shares a heat-treatment run and traceability basis. A planning dashboard uses `batch` for a grouping of intended PlanItems. Spelling does not make these one governed value. Recover the physical batch under the direct material or production DPF pattern, including its identity and part-whole treatment when the proposed comparison relies on either; recover the planning grouping under A.15.2 and its direct planning relation. Publish separate rows unless an obtaining F.9 Bridge states the exact semantic relation and a separate affirmative C.2.1 claim names the proposed comparison direction, correspondence rule, and tolerated loss with current A.10 or B.3 reliance. A `batch` row cannot turn a PlanItem grouping into a physical holon or make the physical batch a WorkPlan.

#### F.17:12.4b - Clinical discharge wording

A clinical publication proposes one row for `discharge` and `discharge-ready`. First separate the governed values. A patient-state classification uses A.19.SPR plus the clinical DPF pattern for its bearer, state frame, evidence, qualification window, and use. An accountable discharge decision remains a decision relation under its direct pattern. A completed discharge is dated Work under A.15.1. Publish distinct rows and connect them only through relations actually governed in the clinical context. One familiar label does not make state, decision, and Work interchangeable.

#### F.17:12.4c - Demonstrative walkthrough, mantra, and mantra move

These rows publish naming decisions already governed and named in A.22.CGUS. They cover only the admitted CGUS-demonstrative senses of `mantra` and `mantra move`; they define neither the Plain local mantra that recalls one bounded result nor the Plain long mantra that keeps a distant result dependency visible across direct patterns. Ordinary long and local mantras receive no F.17 row. F.17 publishes the bounded terms; it does not govern the demonstrated structures, rows, or Plain attention aids.

```text
UTSRowId: UTS.DemonstrativeUnfoldingSlice.FPFPublic
ReferenceScheme: FPFCoreReferenceScheme
UnificationThreadId: DemonstrativeExplanationTerminology.2026-07-11
Block: Pattern use and teaching
GovernedValueRef: DemonstrativeUnfoldingSlice@Context
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: A.22.CGUS
UnifiedTechName: DemonstrativeUnfoldingSlice@Context
UnifiedPlainName: demonstrative walkthrough
NameCardRef: NameCard.DemonstrativeUnfoldingSlice.FPFPublic
SenseCellRefs: SenseCell.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11
BridgeRefs: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11; relation=Narrower-than with SeminarTeaching source narrower than FPFPublic receiving
RowRationale: this row names one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure for a cold public reader
AdmissibleUse: public naming of the governed demonstrative episteme under affirmative claim Claim.DemonstrativeUnfoldingSlice.SeminarToPublic.Naming.2026-07-11
BlockedUse: actual traversal, method order, work order, performed work, or teaching-medium identity
Notes: reliance basis is EvidenceUse.DemonstrativeUnfoldingSlice.SeminarToPublic.Naming.2026-07-11 with RelianceDisposition=pass for this naming use only
RowEditionId: 2026-07-11
CurrentnessCondition: review when the governed value, FPFCoreReferenceScheme, NameCard, local-sense basis relation, Bridge endpoint or profile, bounded-use claim, A.10 reliance basis, or reader evidence changes

UTSRowId: UTS.DemonstrativeUnfoldingSlice.SeminarTeaching
ReferenceScheme: FPFSeminarTeachingReferenceScheme-2026-07-11
UnificationThreadId: DemonstrativeExplanationTerminology.2026-07-11
Block: Pattern use and teaching
GovernedValueRef: DemonstrativeUnfoldingSlice@Context
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: A.22.CGUS
UnifiedTechName: DemonstrativeUnfoldingSlice@Context
UnifiedPlainName: mantra
NameCardRef: NameCard.DemonstrativeUnfoldingSlice.SeminarTeaching
SenseCellRefs: SenseCell.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11
BridgeRefs: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11; relation=Narrower-than with SeminarTeaching source narrower than FPFPublic receiving
RowRationale: the bounded teaching alias adds repeated speech and attentional use while naming the same governed demonstrative episteme
AdmissibleUse: repeated English-language FPF seminar speech that points to the public term under affirmative claim Claim.DemonstrativeUnfoldingSlice.SeminarToPublic.Naming.2026-07-11
BlockedUse: ritual authority, slogan, method, plan, work, fixed order, or reverse substitution from every public walkthrough
Notes: reliance basis is EvidenceUse.DemonstrativeUnfoldingSlice.SeminarToPublic.Naming.2026-07-11 with RelianceDisposition=pass for this naming use only
RowEditionId: 2026-07-11
CurrentnessCondition: review when FPFSeminarTeachingReferenceScheme-2026-07-11, the governed value, NameCard, local-sense basis relation, Bridge endpoint or profile, bounded-use claim, A.10 reliance basis, dictionary evidence, or reader evidence changes

UTSRowId: UTS.DemonstratedPatternUseRow.SeminarTeaching
ReferenceScheme: FPFSeminarTeachingReferenceScheme-2026-07-11
UnificationThreadId: DemonstrativeExplanationTerminology.2026-07-11
Block: Pattern use and teaching
GovernedValueRef: DemonstratedPatternUseRow@Context
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: A.22.CGUS
UnifiedTechName: DemonstratedPatternUseRow@Context
UnifiedPlainName: mantra move
NameCardRef: NameCard.DemonstratedPatternUseRow.SeminarTeaching
SenseCellRefs: SenseCell.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11
BridgeRefs: none; expression and governed-row use are interpreted under the same seminar-teaching scheme
RowRationale: this row names one shown conditional pattern use with its Solution, expected result, and current condition inside a mantra
AdmissibleUse: bounded seminar reference to one demonstrated result-bearing continuation
BlockedUse: root Move, physical movement, operation, fixed serial step, PlanItem, performed Work, or continuation detached from its slice
RowEditionId: 2026-07-11
CurrentnessCondition: review when the demonstrated-row schema, NameCard, local-sense basis relation, seminar-teaching scheme, or reader interpretation changes
```

The two senses of the same demonstrative value remain distinct:

```text
SenseCell.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseId: DemonstrativeUnfoldingSlice-public
  LocalExpression: demonstrative walkthrough
  LocalSenseClaim: one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure
  senseFamily: DemonstrativeExplanation
  NameCardRef: NameCard.DemonstrativeUnfoldingSlice.FPFPublic
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11

SenseCell.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  ReferenceScheme: FPFSeminarTeachingReferenceScheme-2026-07-11
  LocalSenseId: DemonstrativeUnfoldingSlice-mantra
  LocalExpression: mantra
  LocalSenseClaim: a short repeatable explanatory walkthrough used to hold the whole solution structure in attention
  senseFamily: DemonstrativeExplanation
  NameCardRef: NameCard.DemonstrativeUnfoldingSlice.SeminarTeaching
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11

SenseCell.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11:
  ReferenceScheme: FPFSeminarTeachingReferenceScheme-2026-07-11
  LocalSenseId: DemonstratedPatternUseRow-mantra-move
  LocalExpression: mantra move
  LocalSenseClaim: one shown pattern-use continuation with its Solution, expected result, and current condition inside a mantra
  senseFamily: DemonstratedPatternUseContinuation
  NameCardRef: NameCard.DemonstratedPatternUseRow.SeminarTeaching
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11

LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  localSenseCellRef: SenseCell(FPFCoreReferenceScheme, DemonstrativeUnfoldingSlice-public)
  basisEpistemeRef: A.22.CGUS

LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation
  basisPublicationUnitRef: A.22.CGUS:4.3.3-Ordinary-bounded-use
  viewpointRef: FPFPublicReaderViewpoint
  claimGraph:
    supportedSenseClaim: one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure
    admittedUseClaim: support the public local-sense line for this scheme-based coordinate
    nonAdmittedUseClaim: no evidence, authority, work-order, or naming decision follows from this relation
  referenceScheme: FPFCoreReferenceScheme
  editionId: 2026-07-11

LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  localSenseCellRef: SenseCell(FPFSeminarTeachingReferenceScheme-2026-07-11, DemonstrativeUnfoldingSlice-mantra)
  basisEpistemeRef: SeminarExpression.FPFPracticalUse.2026-07-11

LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation
  basisPublicationUnitRef: SeminarExpression.FPFPracticalUse.2026-07-11.Slides8-10
  viewpointRef: FPF Seminar Participant Viewpoint
  claimGraph:
    supportedSenseClaim: a short repeatable explanatory walkthrough used to hold the whole solution structure in attention
    admittedUseClaim: support the bounded teaching sense from the seminar expression
    nonAdmittedUseClaim: the slide carrier does not become the sense, naming settlement, method, plan, or work
  referenceScheme: FPFSeminarTeachingReferenceScheme-2026-07-11
  editionId: 2026-07-11

LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11:
  localSenseCellRef: SenseCell(FPFSeminarTeachingReferenceScheme-2026-07-11, DemonstratedPatternUseRow-mantra-move)
  basisEpistemeRef: SeminarExpression.FPFPracticalUse.2026-07-11

LocalSenseBasisRelationDescription.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation
  basisPublicationUnitRef: SeminarExpression.FPFPracticalUse.2026-07-11.Slides61-62
  viewpointRef: FPF Seminar Participant Viewpoint
  claimGraph:
    supportedSenseClaim: one shown pattern-use continuation with its Solution, expected result, and current condition inside a mantra
    admittedUseClaim: support the bounded teaching sense of mantra move
    nonAdmittedUseClaim: the slide carrier does not become the row, pattern use, plan, or performed work
  referenceScheme: FPFSeminarTeachingReferenceScheme-2026-07-11
  editionId: 2026-07-11
```

`SeminarExpression.FPFPracticalUse.2026-07-11` names the seminar-content episteme; the publication occurrence that makes an edition available and the `.pptx` and extracted Markdown carriers remain separate. The public basis relation instead relies on the current A.22.CGUS pattern episteme and narrows that reliance to the ordinary-use publication unit.

This worked case is cross-scheme because its endpoint `ReferenceScheme` values differ. The obtaining relation and the row's named use are recorded separately:

```text
BridgeOccurrence:
  BridgeOccurrenceRef: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11
  SourceSenseCellRef: SenseCell.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11
  ReceivingSenseCellRef: SenseCell.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11
  BridgePredicateProfile:
    BridgeKind: Narrower-than
    RelationOrientation: source SeminarTeaching sense is narrower than receiving FPFPublic sense
    EndpointSenseReadings: both are DemonstrativeExplanation senses of the governed A.22.CGUS value; the seminar sense additionally requires repetition and attentional use
    RelationSpecificCondition: every demonstrative episteme classified by the seminar sense is also classified by the public walkthrough sense, while some public walkthroughs are not seminar mantras
    ApplicabilityOrAsOfBasis: FPFCoreReferenceScheme and FPFSeminarTeachingReferenceScheme-2026-07-11 at the named sense editions
    BooleanTruthCondition: true only while the proper-specialization condition holds for those endpoint editions
    RequiredDependencies: both F.17 SchemeSenseCells resolve, their cited local-sense basis claims hold, and the A.22.CGUS governed-value identity remains unchanged

C.2.1 claim about this named use:
  ClaimRef: Claim.DemonstrativeUnfoldingSlice.SeminarToPublic.Naming.2026-07-11
  EntityOfConcern: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11
  EffectiveReferenceScheme: FPFCoreReferenceScheme
  ClaimGraph:
    ProposedUse: a seminar use of "mantra" points to the public demonstrative-walkthrough term and its governed value
    Direction: SeminarTeaching sense -> FPFPublic sense
    CorrespondenceRule: preserve reference to the same governed A.22.CGUS value and do not infer that every public walkthrough is a mantra
    PermittedLossTolerance: repetition, remembered replay, and attentional function may be omitted; no method, plan, order, authority, Work, or teaching-medium claim may be carried
    Polarity: affirmative

A.10 evidence reliance for this claim:
  EvidenceProvenanceRelationRef: EvidenceUse.DemonstrativeUnfoldingSlice.SeminarToPublic.Naming.2026-07-11
  TargetClaimRef: Claim.DemonstrativeUnfoldingSlice.SeminarToPublic.Naming.2026-07-11
  BoundedEvidenceUse: use the seminar word "mantra" to point to the public demonstrative-walkthrough term and the same governed A.22.CGUS value
  EvidencePaths:
    PublicSenseBasisRecord: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11 --basisEpistemeRef--> A.22.CGUS; LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11 --basisPublicationUnitRef--> A.22.CGUS:4.3.3-Ordinary-bounded-use; A.22.CGUS --carriedBy--> _current-pattern-hosts/A.22.CGUS-Constraint-Governed-Unfolding-Structure.md
    SeminarSenseBasisRecord: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11 --basisEpistemeRef--> SeminarExpression.FPFPracticalUse.2026-07-11; LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11 --basisPublicationUnitRef--> SeminarExpression.FPFPracticalUse.2026-07-11.Slides8-10; SeminarExpression.FPFPracticalUse.2026-07-11 --carriedBy--> FPF_first_seminar_reworked_slidement.pptx@sha256:325B50C5D062479434ECCABFF0B8B3E316825CAA5E1646A61D25183B90B9CA89 (Git blob e990847d37ddca59d15a9cc434fad15381a2122d) and fpf_first_seminar_slides.content.md@sha256:B38C6F5FBC85CAF9986D2141095C90DAFFAB6F3FEA607ACE7FA6CE60EB18228D (Git blob 34fd989b646aa4dc9f2879cab40d2e6dde989b1b)
    NameSettlementRecord: NameCard.DemonstrativeUnfoldingSlice.SeminarTeaching --carriedBy--> _current-pattern-hosts/A.22.CGUS-Constraint-Governed-Unfolding-Structure.md
    DictionaryEvidenceRecord-MW: Merriam-Webster "mantra" entry, accessed 2026-07-11 --derivedFrom--> https://www.merriam-webster.com/dictionary/mantra
    DictionaryEvidenceRecord-OALD: Oxford Advanced Learner's Dictionary "mantra" entry, accessed 2026-07-11 --derivedFrom--> https://www.oxfordlearnersdictionaries.com/definition/english/mantra
    ReaderCueEvidenceRecord: Zhu, Reinecke, and Mitra, Language Scent, arXiv:2604.03604 (2026) --derivedFrom--> https://arxiv.org/abs/2604.03604; supports contextual cues, not equivalence or fitness for every reader
  EvidenceProducingOrInterpretingWork: absent from this fixture; no Work occurrence is used as a premise
  CurrentRoleAssignment: absent from this fixture
  MethodTrace: absent from this fixture
  CurrentnessAndWindow: applies to the named 2026-07-11 sense as evidenced by the exact current seminar carrier editions above; both Git blobs must resolve, both carrier paths must retain the cited raw-SHA-256 bytes, and the cited NameCard and A.22.CGUS governed value must remain current
  UnsupportedAttemptedUse: reverse substitution, structural inference, or any method, plan, authority, Work, teaching-medium identity, publication occurrence, or other receiving occurrence
  ReopenOrStop: stop this naming use and reopen its A.10 classification if either cited Git blob does not resolve, either carrier path no longer contains its cited raw-SHA-256 bytes, any other cited item or provenance edge is missing or stale, either sense, NameCard, or governed value changes, or reader evidence shows that "mantra" obscures rather than locates the public value
  RelianceDisposition: pass only for the named bounded naming use while every path and currentness condition above holds
  B.3 branch: no assurance claim is made and this reversible naming use does not meet the material-reliance threshold
BridgeCard:
  EntityOfConcern: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11
  EffectiveReferenceScheme: FPFCoreReferenceScheme
  ClaimGraph:
    ClaimMode: actual
    BridgeClaim: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11 obtains under the BridgePredicateProfile above
    BoundedUseClaimRef: Claim.DemonstrativeUnfoldingSlice.SeminarToPublic.Naming.2026-07-11
    EvidenceProvenanceRelationRef: EvidenceUse.DemonstrativeUnfoldingSlice.SeminarToPublic.Naming.2026-07-11
    RelianceDispositionClaim: pass only for the named SeminarTeaching-to-FPFPublic naming use
    ObservedLossClaim: the broader public sense does not require repeated speech, remembered replay, or the seminar attentional function
    CounterExampleClaim: a public demonstrative walkthrough may be read once and understood without being repeated or used as a mnemonic
    CurrentnessClaim: use this card only while the named Bridge, bounded-use claim, evidence-provenance relation, local reliance disposition, 2026-07-11 sense editions, and current A.22.CGUS governed value remain current
    NearestNonUseClaim: do not use it for FPFPublic-to-SeminarTeaching substitution or to infer a method, plan, order, authority, Work, teaching-medium identity, publication occurrence, or other receiving occurrence
```

The Bridge is `Narrower-than` because the seminar sense adds repetition and attentional use. That relation orientation does not grant a use. The separate affirmative claim states the exact SeminarTeaching-to-FPFPublic naming use, rule, and tolerance; the A.10 relation and `RelianceDisposition=pass` support reliance only on that claim. Changing reader evidence may reopen the claim or reliance while leaving the Bridge fixed. Neither the card nor the passing disposition authorizes publication or proves that publication Work occurred.

The seminar deck and its textual extraction establish the teaching problem and observed concept use. They do not establish English lexical suitability by themselves. Current English dictionary evidence supports the repeated-formula and watchword senses of `mantra`, while its Sanskrit analysis as an instrument of thought supplies the attentional rationale. F.18 and reader-use evidence decide whether that English candidate fits this bounded FPF use. This row does not claim that every local pattern mantra is a `DemonstrativeUnfoldingSlice@Context`; a pattern-local formula is interpreted from that pattern's Solution unless a stronger governed value is claimed. This row makes no cross-language sameness claim. If the term is independently published under another semantic-context projection—including the same scheme with a different `LocalSenseClaim` or another scheme—that publication needs its own F.18 NameCard, exact F.17 SenseCell, and naming evidence. Only when a named current use relates the two projections must that use also cite an obtaining F.9 Bridge, a separate affirmative C.2.1 bounded-use claim for its exact action, direction, rule, and tolerance, and the claim's current A.10 or B.3 reliance. Without that use, publication alone adds no Bridge or use claim.

No F.17 row is published for `working product`. The phrase has no single governed value across physical entities, changed states, capabilities, relations, and epistemes. Technical text uses the exact subject-governed result name; ordinary explanation may say `result produced by work`, or `first useful result` when firstness and receiving-use value have been established.

#### F.17:12.4d - Bounded model-use structure public row

This row publishes the already selected A.1.1/F.18 naming decision for the dependent `U.Structure` specialization. It does not make A.1.1 Stable, create a structure individual, or make any relation obtain.

```text
UTSRowId: UTS.BoundedModelUseStructure.FPFCore.2026-07-25
ReferenceScheme: FPFCoreReferenceScheme
UnificationThreadId: R1.2-BoundedModelUse-Naming
Block: Architecture and model use
GovernedValueRef: BoundedModelUseStructure
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: A.1.1
UnifiedTechName: BoundedModelUseStructure
UnifiedPlainName: bounded context
NameCardRef: NC-BOUNDED-MODEL-USE-STRUCTURE
SenseCellRefs: SenseCell.BoundedModelUseStructure.FPFCore.2026-07-25
BridgeRefs: none; this row makes no semantic-correspondence or substitution claim
RowRationale: the governed value is the A.1.1 kind token; its admitted members are exactly the U.Structure individuals that satisfy the A.1.1/A.22 membership condition, and the selected names designate that organization of one model edition's governed applicability, actual use, and fixed-content expression coherence over exact admitted model-use holons, exact applied constraint claims, and the named frame; a claim scope or membership outcome is not an applied constraint by itself
AdmissibleUse: Core-facing designation of the A.1.1 dependent structure specialization and retrieval of the DDD plain term
BlockedUse: no generic context holon, no identity for a subsystem, team, claim scope, model episteme, description, or view, no relation occurrence, and no positive crossing-structure membership
RowEditionId: 2026-07-25
CurrentnessCondition: reopen when the A.1.1/A.22 membership or continuity rule, one of the three direct relation kinds, FPFCoreReferenceScheme, the NameCard, an exact applied constraint proposition or its use in selection, or the named bounded-model-use frame changes

SenseCell.BoundedModelUseStructure.FPFCore.2026-07-25:
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseId: BoundedModelUseStructure-core
  LocalExpression: BoundedModelUseStructure
  LocalSenseClaim: the dependent U.Structure specialization selected over one exact model episteme, exact admitted model-use holons, obtaining applicability, actual-use, and fixed-content expression-coherence relations, exact applied constraint claims used by the selection judgment, and the named bounded-model-use frame; a claim scope participates only in its applicability relation unless a distinct constraint proposition refers to that scope or its membership predicate, and crossings belong only to a distinct A.22 structure over already identified bounded model-use structures
  senseFamily: BoundedModelUse
  NameCardRef: NC-BOUNDED-MODEL-USE-STRUCTURE
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.BoundedModelUseStructure.FPFCore.2026-07-25

LocalSenseBasisRelation.BoundedModelUseStructure.FPFCore.2026-07-25:
  localSenseCellRef: SenseCell(FPFCoreReferenceScheme, BoundedModelUseStructure-core)
  basisEpistemeRef: A.1.1

LocalSenseBasisRelationDescription.BoundedModelUseStructure.FPFCore.2026-07-25:
  entityOfConcernRef: LocalSenseBasisRelation.BoundedModelUseStructure.FPFCore.2026-07-25
  entityOfConcernKindRef: LocalSenseBasisRelation
  viewpointRef: FPFCoreReaderViewpoint
  claimGraph:
    supportedSenseClaim: BoundedModelUseStructure names the exact A.1.1/A.22 dependent structure specialization, with bounded context retained only as its Plain retrieval name
    admittedUseClaim: Core-facing designation and citation of that governed specialization
    nonAdmittedUseClaim: the name or row creates no structure, holon, context bearer, direct relation occurrence, crossing occurrence, view, representation, or publication event
  referenceScheme: FPFCoreReferenceScheme
  editionId: 2026-07-25
```

This row makes only `BoundedModelUseStructure` current for public reuse. A.22's separate cross-structure NameCard remains local and pending: without an independently governed obtaining crossing and an exact positive membership basis, F.17 returns no public row for that label.

#### F.17:12.4e - Three bounded-model-use direct relation-kind rows

These rows publish the three already governed A.1.1 relation-kind names used by E.24.UK. Each row publishes a designation only. A.1.1 still decides whether one of those relation occurrences obtains and how it is reidentified. The naming objects and the separately governed local-sense basis occurrences make none of the three A.1.1 relations obtain, and they create no assertion, temporal extent, Work, or structure.

```text
UTSRowId: UTS.ModelApplicabilityRelation.FPFCore.2026-07-25
ReferenceScheme: FPFCoreReferenceScheme
UnificationThreadId: R1.2-BoundedModelUse-Naming
Block: Architecture and model use
GovernedValueRef: ModelApplicabilityRelation
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: A.1.1
UnifiedTechName: ModelApplicabilityRelation
UnifiedPlainName: this model applies to this holon within this claim scope
NameCardRef: NC-MODEL-APPLICABILITY-RELATION
SenseCellRefs: SenseCell.ModelApplicabilityRelation.FPFCore.2026-07-25
BridgeRefs: none; this row makes no semantic-correspondence or substitution claim
RowRationale: the governed value is the A.1.1 relation-kind token; its admitted instances are exactly the obtaining U.Relation occurrences that satisfy the A.1.1 applicability predicate and identity rule, and the selected names expose that relation while keeping A.2.6 scope membership, the derived interval, assertions, and the selected structure separate
AdmissibleUse: Core-facing designation of the A.1.1 relation kind, including A.2.6 claim-scope coordination and the E.24.UK bounded-model-use membership test
BlockedUse: no applicability occurrence from a name, model mention, shared label, scope row, assertion, interval, publication, or structure membership
RowEditionId: 2026-07-25
CurrentnessCondition: reopen when A.1.1 changes the participant kinds, predicate, scope alignment, model-scheme interpretation, temporal identity, NameCard, or named Core use

SenseCell.ModelApplicabilityRelation.FPFCore.2026-07-25:
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseId: ModelApplicabilityRelation-core
  LocalExpression: ModelApplicabilityRelation
  LocalSenseClaim: the direct relation kind over one model episteme, one exact holon, and one participating claim scope; one exact relation occurrence obtains only when the A.1.1 applicability predicate is true and all other governing conditions hold
  senseFamily: ModelApplicability
  NameCardRef: NC-MODEL-APPLICABILITY-RELATION
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.ModelApplicabilityRelation.FPFCore.2026-07-25

LocalSenseBasisRelation.ModelApplicabilityRelation.FPFCore.2026-07-25:
  localSenseCellRef: SenseCell(FPFCoreReferenceScheme, ModelApplicabilityRelation-core)
  basisEpistemeRef: A.1.1

LocalSenseBasisRelationDescription.ModelApplicabilityRelation.FPFCore.2026-07-25:
  entityOfConcernRef: LocalSenseBasisRelation.ModelApplicabilityRelation.FPFCore.2026-07-25
  entityOfConcernKindRef: LocalSenseBasisRelation
  basisPublicationUnitRef: A.1.1:4.2 ModelApplicabilityRelation
  viewpointRef: FPFCoreReaderViewpoint
  claimGraph:
    supportedSenseClaim: ModelApplicabilityRelation names the exact A.1.1 relation kind rather than a scope-membership predicate, claim, record, or interval
    admittedUseClaim: Core-facing designation and citation of that governed relation kind
    nonAdmittedUseClaim: the name or row makes no applicability occurrence obtain and grants no selected-structure membership
  referenceScheme: FPFCoreReferenceScheme
  editionId: 2026-07-25
```

```text
UTSRowId: UTS.ModelUseRelation.FPFCore.2026-07-25
ReferenceScheme: FPFCoreReferenceScheme
UnificationThreadId: R1.2-BoundedModelUse-Naming
Block: Architecture and model use
GovernedValueRef: ModelUseRelation
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: A.1.1
UnifiedTechName: ModelUseRelation
UnifiedPlainName: this assignment's holder uses this model during this work concerning this holon
NameCardRef: NC-MODEL-USE-RELATION
SenseCellRefs: SenseCell.ModelUseRelation.FPFCore.2026-07-25
BridgeRefs: none; this row makes no semantic-correspondence or substitution claim
RowRationale: the governed value is the A.1.1 relation-kind token; its admitted instances are exactly the obtaining U.Relation occurrences that satisfy the A.1.1 actual-use predicate and identity rule, and the selected names expose that relation while keeping applicability, role assignment, performed Work, method application, claims, and records separate
AdmissibleUse: Core-facing designation of the A.1.1 relation kind and its use in the E.24.UK bounded-model-use membership test
BlockedUse: no use occurrence from availability, access, mention, assignment alone, Work alone, method application, assertion, publication, or structure membership
RowEditionId: 2026-07-25
CurrentnessCondition: reopen when A.1.1 changes the participant kinds, F.6 prerequisite, actual-use predicate, actor derivation, maximal-continuous-use identity, NameCard, or named Core use

SenseCell.ModelUseRelation.FPFCore.2026-07-25:
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseId: ModelUseRelation-core
  LocalExpression: ModelUseRelation
  LocalSenseClaim: the direct relation kind over one exact role-assignment occurrence, model episteme, performed Work occurrence, and use-locus holon; one exact relation occurrence obtains only when the A.1.1 actual-use predicate is true and all other governing conditions hold
  senseFamily: ModelUse
  NameCardRef: NC-MODEL-USE-RELATION
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.ModelUseRelation.FPFCore.2026-07-25

LocalSenseBasisRelation.ModelUseRelation.FPFCore.2026-07-25:
  localSenseCellRef: SenseCell(FPFCoreReferenceScheme, ModelUseRelation-core)
  basisEpistemeRef: A.1.1

LocalSenseBasisRelationDescription.ModelUseRelation.FPFCore.2026-07-25:
  entityOfConcernRef: LocalSenseBasisRelation.ModelUseRelation.FPFCore.2026-07-25
  entityOfConcernKindRef: LocalSenseBasisRelation
  basisPublicationUnitRef: A.1.1:4.2 ModelUseRelation
  viewpointRef: FPFCoreReaderViewpoint
  claimGraph:
    supportedSenseClaim: ModelUseRelation names the exact A.1.1 actual-use relation kind rather than applicability, availability, Work, assignment, method application, claim, or record
    admittedUseClaim: Core-facing designation and citation of that governed relation kind
    nonAdmittedUseClaim: the name or row makes no model-use occurrence obtain and grants no selected-structure membership
  referenceScheme: FPFCoreReferenceScheme
  editionId: 2026-07-25
```

```text
UTSRowId: UTS.ModelExpressionCoherenceRelation.FPFCore.2026-07-25
ReferenceScheme: FPFCoreReferenceScheme
UnificationThreadId: R1.2-BoundedModelUse-Naming
Block: Architecture and model use
GovernedValueRef: ModelExpressionCoherenceRelation
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: A.1.1
UnifiedTechName: ModelExpressionCoherenceRelation
UnifiedPlainName: this model content and this expression content satisfy this declared coherence criterion under this comparison scheme
NameCardRef: NC-MODEL-EXPRESSION-COHERENCE-RELATION
SenseCellRefs: SenseCell.ModelExpressionCoherenceRelation.FPFCore.2026-07-25
BridgeRefs: none; this designation makes no semantic-correspondence claim, and any Bridge needed for a particular coherence occurrence is a separately obtaining prerequisite named by that occurrence's predicate declaration
RowRationale: the governed value is the A.1.1 relation-kind token; its admitted instances are exactly the obtaining U.Relation occurrences that satisfy the A.1.1 coherence predicate and participant-determined identity rule, and the selected names expose fixed-content semantic coherence while keeping the local predicate value, maintenance, transformation, evaluation, result, evidence, and assertion separate
AdmissibleUse: Core-facing designation of the A.1.1 relation kind and its use in the E.24.UK bounded-model-use membership test
BlockedUse: no coherence occurrence from a label, predicate label, equal spelling, maintenance or evaluation Work, changed carrier, result episteme, evidence, assertion, publication, or structure membership
RowEditionId: 2026-07-25
CurrentnessCondition: reopen when A.1.1 changes the participant kinds, five-part predicate-value rule, interpretation branch, permitted loss, participant-determined identity, NameCard, or named Core use

SenseCell.ModelExpressionCoherenceRelation.FPFCore.2026-07-25:
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseId: ModelExpressionCoherenceRelation-core
  LocalExpression: ModelExpressionCoherenceRelation
  LocalSenseClaim: the participant-determined direct relation kind over one model episteme, expression episteme, admitted five-part predicate value, and comparison scheme when an admissible interpretation branch exists and that predicate is true
  senseFamily: ModelExpressionCoherence
  NameCardRef: NC-MODEL-EXPRESSION-COHERENCE-RELATION
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.ModelExpressionCoherenceRelation.FPFCore.2026-07-25

LocalSenseBasisRelation.ModelExpressionCoherenceRelation.FPFCore.2026-07-25:
  localSenseCellRef: SenseCell(FPFCoreReferenceScheme, ModelExpressionCoherenceRelation-core)
  basisEpistemeRef: A.1.1

LocalSenseBasisRelationDescription.ModelExpressionCoherenceRelation.FPFCore.2026-07-25:
  entityOfConcernRef: LocalSenseBasisRelation.ModelExpressionCoherenceRelation.FPFCore.2026-07-25
  entityOfConcernKindRef: LocalSenseBasisRelation
  basisPublicationUnitRef: A.1.1:4.2 ModelExpressionCoherenceRelation
  viewpointRef: FPFCoreReaderViewpoint
  claimGraph:
    supportedSenseClaim: ModelExpressionCoherenceRelation names the exact A.1.1 relation kind rather than its predicate value, maintenance, transformation, evaluation, result, evidence, or assertion
    admittedUseClaim: Core-facing designation and citation of that governed relation kind
    nonAdmittedUseClaim: the name or row makes no coherence occurrence obtain, publishes no predicate-value name, and grants no selected-structure membership
  referenceScheme: FPFCoreReferenceScheme
  editionId: 2026-07-25
```

No public F.17 row is returned for `ModelExpressionCoherencePredicate`: that label remains local to A.1.1 and names the five-part criterion ValueKind rather than any of the three relation kinds.

#### F.17:12.4f - Viewpoint, view, and conformance-relation public rows

These three rows satisfy different receiver needs and therefore cannot be merged. E.24.UK has already admitted `U.Viewpoint` and `U.View` as same-individual dependent kinds under `U.Episteme`; E.17.0 owns both positive membership predicates and the direct `EpistemeViewpointConformanceRelation`. F.14 has been applied again: the existing Tech designations are retained, no synonym family is opened, and the public rows are justified by stable Core citation and exact typed-reference use. The rows admit no kind, make no relation obtain, and assert no E.24.PUB publication occurrence, form, carrier, or authority.

The two existing dependent-kind designations use these progressive-minimum F.18 naming-settlement epistemes. They remain distinct from the E.24.UK admission results, the governed kinds, their members, every reference or designator, and the F.17 rows that cite them.

```text
NameCard:
  NameCardId: NameCard.U.Viewpoint.FPFPublic.2026-08-02
  GovernedValueRef: U.Viewpoint
  GovernedValueKindRef: U.Kind
  GoverningPatternRef: E.17.0
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NameCard.U.Viewpoint.FPFPublic.2026-08-02.ClaimGraph — complete naming-settlement graph constituted by the claims designated below
  LocalSenseCellRef: SenseCell.U.Viewpoint.FPFCore.2026-08-02
  LocalSenseBasisRelationRef: LocalSenseBasisRelation.U.Viewpoint.FPFCore.2026-08-02
  TechLabel: U.Viewpoint
  PlainLabel: viewpoint
  CandidateSet: U.Viewpoint; ViewpointEpisteme; ViewpointConvention; ViewpointRecord; ViewpointStructure
  CandidateCoverage: dependent-kind, episteme, convention, record, and structure readings tested
  RejectedCandidates: ViewpointEpisteme hides the stable public kind name; ViewpointConvention can denote fixed claim content rather than P; ViewpointRecord adds a wrapper; ViewpointStructure names S rather than P; none is an alias
  SelectionRationale: retain the admitted Core Tech name and ordinary Plain retrieval word while the exact local-sense claim keeps P, S, references, and designators distinct
  DeclaredUse: Core-facing designation of the E.17.0 same-individual dependent kind and typed reference resolution to exact P
  NonAdmissibleUse: no P, S, kind membership, selection, Work, conformance, view membership, or publication follows from the card or labels
  BridgeRefs: none; this settlement makes no cross-local correspondence claim
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.U.Viewpoint.FPFCore.2026-08-02
  LineageEntries: ViewpointId remains only a designator of exact P; viewpointRef remains U.ViewpointRef and resolution grants no membership
  RefreshCondition: reopen when E.17.0 changes P's same-individual membership predicate, E.24.UK admission, exact reference typing, FPFCoreReferenceScheme, reader meaning, or public use
```

```text
NameCard:
  NameCardId: NameCard.U.View.FPFPublic.2026-08-02
  GovernedValueRef: U.View
  GovernedValueKindRef: U.Kind
  GoverningPatternRef: E.17.0
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NameCard.U.View.FPFPublic.2026-08-02.ClaimGraph — complete naming-settlement graph constituted by the claims designated below
  LocalSenseCellRef: SenseCell.U.View.FPFCore.2026-08-02
  LocalSenseBasisRelationRef: LocalSenseBasisRelation.U.View.FPFCore.2026-08-02
  TechLabel: U.View
  PlainLabel: episteme conforming to an exact viewpoint
  CandidateSet: U.View; ViewEpisteme; ConformingEpisteme; ViewArtifact; PublishedView
  CandidateCoverage: dependent-kind, episteme, conformance, artifact, and publication readings tested
  RejectedCandidates: ViewEpisteme can look like a second individual; ConformingEpisteme drops the exact viewpoint relation; ViewArtifact collapses episteme with form or carrier; PublishedView makes availability look constitutive; none is an alias
  SelectionRationale: retain the admitted Core Tech name while the Plain label exposes that the same E gains membership only through exact E/P conformance
  DeclaredUse: Core-facing designation of the E.17.0 same-individual dependent kind and typed reference to an already conforming episteme
  NonAdmissibleUse: no membership from direct authoring, construction, query execution, transformation, selection, rendering, bundle, form, carrier, or publication
  BridgeRefs: none; this settlement makes no cross-local correspondence claim
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.U.View.FPFCore.2026-08-02
  LineageEntries: viewRef resolves exact E only after membership is independently current; view, diagram, face, form, and carrier readings remain separated
  RefreshCondition: reopen when E.17.0 changes E/P conformance, same-individual membership, E.24.UK admission, FPFCoreReferenceScheme, reader meaning, or public use
```

##### F.17:12.4f.1 - `U.Viewpoint`

```text
UTSRowId: UTS.U.Viewpoint.FPFCore.2026-08-02
ReferenceScheme: FPFCoreReferenceScheme
UnificationThreadId: R1.2-MultiView-Naming
Block: Multi-view describing
GovernedValueRef: U.Viewpoint
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: E.17.0
UnifiedTechName: U.Viewpoint
UnifiedPlainName: viewpoint
NameCardRef: NameCard.U.Viewpoint.FPFPublic.2026-08-02
SenseCellRefs: SenseCell.U.Viewpoint.FPFCore.2026-08-02
BridgeRefs: none; this row makes no semantic-correspondence or substitution claim
RowRationale: the governed value is the E.17.0/E.24.UK same-individual dependent-kind token, not P, S, a reference, or a designator; an admitted member is the same exact C.2.1 episteme P whose EntityOfConcern is independently selected viewpoint-convention Structure S_viewpoint and whose fixed ClaimGraph under its effective ReferenceScheme satisfies E.17.0's complete positive membership predicate; admission result E24UK-AR-UVIEWPOINT-RG-01 remains a separate decision projection
AdmissibleUse: Core-facing designation of the dependent kind and exact typing of a reference whose resolution yields an already admitted viewpoint episteme P
BlockedUse: no viewpoint membership, episteme identity, Structure selection, method, Work, conformance, View membership, authority, or publication from the row, name, ViewpointId, viewpointRef, NameCard, bundle position, selected S, form, or carrier
RowEditionId: 2026-08-02
CurrentnessCondition: reopen when E.17.0 changes P's C.2.1 discriminators, exact S EntityOfConcern, fixed target/concern/admitted-kind/conformance claims, effective ReferenceScheme, same-individual predicate, E.24.UK admission, NameCard, or typed-reference use
Notes: retain the exact field viewpointRef : U.ViewpointRef; under the effective scheme its resolution yields P, while ViewpointId only designates P and neither operation grants membership

SenseCell.U.Viewpoint.FPFCore.2026-08-02:
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseId: U.Viewpoint-core
  LocalExpression: U.Viewpoint
  LocalSenseClaim: the same-individual dependent kind of exact C.2.1 epistemes P whose exact EntityOfConcern is independently selected viewpoint-convention Structure S_viewpoint and whose fixed claims identify S, state the exact target-kind criterion, stakeholder or audience referents when current, concerns, admitted episteme kinds, coverage, semantic-form, completeness, consistency, omission and conformance rules without circular View premises, and the describing-use frame and fixed applicability qualifiers
  senseFamily: MultiViewRecognition
  NameCardRef: NameCard.U.Viewpoint.FPFPublic.2026-08-02
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.U.Viewpoint.FPFCore.2026-08-02

LocalSenseBasisRelation.U.Viewpoint.FPFCore.2026-08-02:
  localSenseCellRef: SenseCell(FPFCoreReferenceScheme, U.Viewpoint-core)
  basisEpistemeRef: E.17.0

LocalSenseBasisRelationDescription.U.Viewpoint.FPFCore.2026-08-02:
  entityOfConcernRef: LocalSenseBasisRelation.U.Viewpoint.FPFCore.2026-08-02
  entityOfConcernKindRef: LocalSenseBasisRelation
  basisPublicationUnitRef: E.17.0:4.2-4.2.4
  viewpointRef: FPFCoreReaderViewpoint
  claimGraph:
    supportedSenseClaim: U.Viewpoint names the same P identified under C.2.1 only when P's exact S EntityOfConcern and fixed convention claims satisfy E.17.0
    admittedUseClaim: Core-facing designation, exact U.ViewpointRef typing, and retrieval of the direct membership rule
    nonAdmittedUseClaim: the basis relation, cell, NameCard, row, identifier, reference, Structure, bundle, or publication grants no membership
  referenceScheme: FPFCoreReferenceScheme
  editionId: 2026-08-02
```

##### F.17:12.4f.2 - `U.View`

```text
UTSRowId: UTS.U.View.FPFCore.2026-08-02
ReferenceScheme: FPFCoreReferenceScheme
UnificationThreadId: R1.2-MultiView-Naming
Block: Multi-view describing
GovernedValueRef: U.View
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: E.17.0
UnifiedTechName: U.View
UnifiedPlainName: episteme conforming to an exact viewpoint
NameCardRef: NameCard.U.View.FPFPublic.2026-08-02
SenseCellRefs: SenseCell.U.View.FPFCore.2026-08-02
BridgeRefs: none; this row makes no semantic-correspondence or substitution claim
RowRationale: the governed value is the E.17.0/E.24.UK same-individual dependent-kind token, not candidate episteme E, viewpoint P, conformance occurrence, reference, form, or carrier; an admitted member is the same exact C.2.1 episteme E only when EpistemeViewpointConformanceRelation(E,P) obtains for at least one exact admitted P; one unchanged E may conform to several viewpoint editions through distinct pair-determined occurrences while remaining one episteme; admission result E24UK-AR-UVIEW-RG-01 remains a separate decision projection
AdmissibleUse: Core-facing designation of the dependent kind and exact typing of U.ViewRef values that resolve already conforming epistemes
BlockedUse: no View membership, episteme identity, conformance occurrence, adequacy, authority, or publication from the row, name, viewRef, NameCard, direct authoring, A.6.3 construction, query execution, transformation, evaluation, selection, bundling, rendering, audience, form, carrier, or publication
RowEditionId: 2026-08-02
CurrentnessCondition: reopen when E.17.0 changes candidate-episteme identity, the exact conformance predicate or pair-determined occurrence rule, same-individual membership, E.24.UK admission, NameCard, FPFCoreReferenceScheme, or typed-reference use
Notes: construction history and publication availability remain separately governed; neither creates membership, and no second View individual wraps E

SenseCell.U.View.FPFCore.2026-08-02:
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseId: U.View-core
  LocalExpression: U.View
  LocalSenseClaim: the same-individual dependent kind of exact C.2.1 epistemes E for which at least one direct EpistemeViewpointConformanceRelation(E,P) occurrence obtains to an exact admitted viewpoint episteme P; E remains the same individual and construction, selection, use, representation, and publication remain non-constitutive
  senseFamily: MultiViewRecognition
  NameCardRef: NameCard.U.View.FPFPublic.2026-08-02
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.U.View.FPFCore.2026-08-02

LocalSenseBasisRelation.U.View.FPFCore.2026-08-02:
  localSenseCellRef: SenseCell(FPFCoreReferenceScheme, U.View-core)
  basisEpistemeRef: E.17.0

LocalSenseBasisRelationDescription.U.View.FPFCore.2026-08-02:
  entityOfConcernRef: LocalSenseBasisRelation.U.View.FPFCore.2026-08-02
  entityOfConcernKindRef: LocalSenseBasisRelation
  basisPublicationUnitRef: E.17.0:4.4-4.5
  viewpointRef: FPFCoreReaderViewpoint
  claimGraph:
    supportedSenseClaim: U.View names the same E only when exact E/P conformance obtains; it never names a generated or published wrapper
    admittedUseClaim: Core-facing designation, exact U.ViewRef typing, and retrieval of the direct membership rule
    nonAdmittedUseClaim: the basis relation, cell, NameCard, row, reference, construction, evaluation, form, carrier, or publication grants no membership
  referenceScheme: FPFCoreReferenceScheme
  editionId: 2026-08-02
```

##### F.17:12.4f.3 - `EpistemeViewpointConformanceRelation`

```text
UTSRowId: UTS.EpistemeViewpointConformanceRelation.FPFCore.2026-08-02
ReferenceScheme: FPFCoreReferenceScheme
UnificationThreadId: R1.2-MultiView-Naming
Block: Multi-view describing
GovernedValueRef: EpistemeViewpointConformanceRelation
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: E.17.0
UnifiedTechName: EpistemeViewpointConformanceRelation
UnifiedPlainName: the episteme conforms to this exact viewpoint
NameCardRef: NameCard.EpistemeViewpointConformanceRelation.FPFPublic
SenseCellRefs: SenseCell.EpistemeViewpointConformanceRelation.FPFCore.2026-08-02
BridgeRefs: none; this row makes no semantic-correspondence or substitution claim
RowRationale: the governed value is E.17.0's direct relation-kind token, not its RelationSignature, either participant, a reference, occurrence, assertion, evaluation result, NameCard, or row; each positive occurrence has exactly candidate episteme E and admitted viewpoint episteme P as participants and is pair-determined by <E,P>; it obtains only when E's C.2.1 EntityOfConcern satisfies P's exact target-kind criterion, E has an independently admitted episteme kind allowed by P without circular U.View use, and E's fixed content under its effective scheme satisfies P's fixed concern-coverage, semantic-form, completeness, consistency, omission, and loss rules
AdmissibleUse: Core-facing designation of the direct relation kind, exact RelationSignature lookup, and readable E/P conformance claims under E.17.0
BlockedUse: no conformance occurrence, U.View membership, adequacy, truth, authority, or publication from the row, name, NameCard, signature, SlotSpecs, viewpointRef, ViewpointId, participant fillers, assertion, evidence, evaluation Work, result, construction, query, rendering, form, carrier, or publication
RowEditionId: 2026-08-02
CurrentnessCondition: reopen when E.17.0 changes either participant kind, the target/admitted-kind/content predicate, pair-determined positive occurrence identity, RelationSignature, complete NameCard, FPFCoreReferenceScheme, or named Core use
Notes: EpistemeViewpointConformanceRelationSignature is a separate C.2.1 RelationSignature episteme with CandidateEpistemeSlot : U.EpistemeRef and ViewpointEpistemeSlot : U.ViewpointRef; retain the exact consumer field viewpointRef : U.ViewpointRef, whose resolution yields P but proves no conformance

SenseCell.EpistemeViewpointConformanceRelation.FPFCore.2026-08-02:
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseId: EpistemeViewpointConformanceRelation-core
  LocalExpression: EpistemeViewpointConformanceRelation
  LocalSenseClaim: the direct two-participant relation kind whose exact positive occurrence is pair-determined by one independently identified candidate episteme E and one independently admitted viewpoint episteme P and whose E.17.0 predicate tests E's exact EntityOfConcern kind, independently admitted episteme kind, fixed claim content, effective scheme, and satisfaction of P's fixed coverage, semantic-form, completeness, consistency, omission, and loss rules
  senseFamily: MultiViewConformance
  NameCardRef: NameCard.EpistemeViewpointConformanceRelation.FPFPublic
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.EpistemeViewpointConformanceRelation.FPFCore.2026-08-02

LocalSenseBasisRelation.EpistemeViewpointConformanceRelation.FPFCore.2026-08-02:
  localSenseCellRef: SenseCell(FPFCoreReferenceScheme, EpistemeViewpointConformanceRelation-core)
  basisEpistemeRef: E.17.0

LocalSenseBasisRelationDescription.EpistemeViewpointConformanceRelation.FPFCore.2026-08-02:
  entityOfConcernRef: LocalSenseBasisRelation.EpistemeViewpointConformanceRelation.FPFCore.2026-08-02
  entityOfConcernKindRef: LocalSenseBasisRelation
  basisPublicationUnitRef: E.17.0:4.4-4.4.1
  viewpointRef: FPFCoreReaderViewpoint
  claimGraph:
    supportedSenseClaim: EpistemeViewpointConformanceRelation names the exact E.17.0 direct kind rather than its signature, participant references, assertion, evaluation, result, or dependent View membership
    admittedUseClaim: Core-facing designation, exact signature lookup, and readable reference to the direct relation kind
    nonAdmittedUseClaim: the basis relation, cell, NameCard, row, signature, references, evaluation, construction, or publication makes no occurrence obtain and grants no U.View membership
  referenceScheme: FPFCoreReferenceScheme
  editionId: 2026-08-02
```

The three row epistemes, their `UTSRowId` designators, external references, selected designations, governed values, NameCards, cells, basis relations, admission-result refs, conformance RelationSignature, and every obtaining relation occurrence remain independently recoverable. If availability for an audience later becomes current, exact E.24.PUB expression, bearing, and publication occurrences must be added outside these rows; file inclusion or this displayed block is not publication.


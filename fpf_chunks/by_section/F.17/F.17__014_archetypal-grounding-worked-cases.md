---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:12"
section_title: "Archetypal Grounding - worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__014_archetypal-grounding-worked-cases.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:12 — Archetypal Grounding - worked cases"
line_start: 93041
line_end: 93462
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

### F.17:12 - Archetypal Grounding - worked cases

#### F.17:12.1 - Role name becomes public across two project contexts

A project has `ReviewerRole@DesignReview` and `ReviewerRole@ExternalAudit`. The local expressions both say "reviewer", but one concerns a system-in-role performing design review work and the other concerns an assurance actor producing an audit report.

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

These rows publish naming decisions already governed and named in A.22.CGUS. They cover only the CGUS-demonstrative use of `mantra` and `mantra move`; they do not define the broader Plain practice of giving one pattern a short repeatable local mantra. F.17 publishes the bounded terms; it does not govern the demonstrated structures, rows, or pattern-local formulas.

```text
UTSRowId: UTS.DemonstrativeUnfoldingSlice.FPFPublic
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
RowEdition: 2026-07-11
CurrentnessCondition: review when the governed value, FPFCoreReferenceScheme, NameCard, local-sense basis relation, Bridge endpoint or profile, bounded-use claim, A.10 reliance basis, or reader evidence changes

UTSRowId: UTS.DemonstrativeUnfoldingSlice.SeminarTeaching
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
RowEdition: 2026-07-11
CurrentnessCondition: review when FPFSeminarTeachingReferenceScheme-2026-07-11, the governed value, NameCard, local-sense basis relation, Bridge endpoint or profile, bounded-use claim, A.10 reliance basis, dictionary evidence, or reader evidence changes

UTSRowId: UTS.DemonstratedPatternUseRow.SeminarTeaching
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
RowEdition: 2026-07-11
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
  basisPublicationUnitRef: A.22.CGUS:4.3.3-Ordinary-bounded-use

LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
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
  basisPublicationUnitRef: SeminarExpression.FPFPracticalUse.2026-07-11.Slides8-10

LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
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
  basisPublicationUnitRef: SeminarExpression.FPFPracticalUse.2026-07-11.Slides61-62

LocalSenseBasisRelationDescription.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
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
    PublicSenseBasisRecord: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11 --basisEpistemeRef--> A.22.CGUS --basisPublicationUnitRef--> A.22.CGUS:4.3.3-Ordinary-bounded-use --carriedBy--> _current-pattern-hosts/A.22.CGUS-Constraint-Governed-Unfolding-Structure.md
    SeminarSenseBasisRecord: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11 --basisEpistemeRef--> SeminarExpression.FPFPracticalUse.2026-07-11 --basisPublicationUnitRef--> SeminarExpression.FPFPracticalUse.2026-07-11.Slides8-10 --carriedBy--> FPF_first_seminar_reworked_slidement.pptx@sha256:325B50C5D062479434ECCABFF0B8B3E316825CAA5E1646A61D25183B90B9CA89 (Git blob e990847d37ddca59d15a9cc434fad15381a2122d) and fpf_first_seminar_slides.content.md@sha256:B38C6F5FBC85CAF9986D2141095C90DAFFAB6F3FEA607ACE7FA6CE60EB18228D (Git blob 34fd989b646aa4dc9f2879cab40d2e6dde989b1b)
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
BlockedUse: no U.BoundedContext holon, no identity for a subsystem, team, claim scope, model episteme, description, or view, no relation occurrence, and no positive crossing-structure membership
RowEdition: 2026-07-25
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
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
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
RowEdition: 2026-07-25
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
  basisPublicationUnitRef: A.1.1:4.2 ModelApplicabilityRelation

LocalSenseBasisRelationDescription.ModelApplicabilityRelation.FPFCore.2026-07-25:
  entityOfConcernRef: LocalSenseBasisRelation.ModelApplicabilityRelation.FPFCore.2026-07-25
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
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
RowEdition: 2026-07-25
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
  basisPublicationUnitRef: A.1.1:4.2 ModelUseRelation

LocalSenseBasisRelationDescription.ModelUseRelation.FPFCore.2026-07-25:
  entityOfConcernRef: LocalSenseBasisRelation.ModelUseRelation.FPFCore.2026-07-25
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
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
RowEdition: 2026-07-25
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
  basisPublicationUnitRef: A.1.1:4.2 ModelExpressionCoherenceRelation

LocalSenseBasisRelationDescription.ModelExpressionCoherenceRelation.FPFCore.2026-07-25:
  entityOfConcernRef: LocalSenseBasisRelation.ModelExpressionCoherenceRelation.FPFCore.2026-07-25
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
  viewpointRef: FPFCoreReaderViewpoint
  claimGraph:
    supportedSenseClaim: ModelExpressionCoherenceRelation names the exact A.1.1 relation kind rather than its predicate value, maintenance, transformation, evaluation, result, evidence, or assertion
    admittedUseClaim: Core-facing designation and citation of that governed relation kind
    nonAdmittedUseClaim: the name or row makes no coherence occurrence obtain, publishes no predicate-value name, and grants no selected-structure membership
  referenceScheme: FPFCoreReferenceScheme
  editionId: 2026-07-25
```

No public F.17 row is returned for `ModelExpressionCoherencePredicate`: that label remains local to A.1.1 and names the five-part criterion ValueKind rather than any of the three relation kinds.


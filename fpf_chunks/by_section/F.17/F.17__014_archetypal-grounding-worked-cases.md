---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:12"
section_title: "Archetypal Grounding - worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__014_archetypal-grounding-worked-cases.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:12 — Archetypal Grounding - worked cases"
line_start: 89494
line_end: 89693
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

### F.17:12 - Archetypal Grounding - worked cases

#### F.17:12.1 - Role name becomes public across two project contexts

A project has `ReviewerRole@DesignReview` and `ReviewerRole@ExternalAudit`. The local expressions both say "reviewer", but one concerns a system-in-role performing design review work and the other concerns an assurance actor producing an audit report.

The UTS row does not declare one universal reviewer. It either creates two rows or one row with an explicit `F.9` bridge and loss note. Each row cites the direct role pattern, the RoleDescription when current, and the `F.18` NameCardRef. If evidence or assurance is current, `A.10` or `B.3` governs that separate row or note.

#### F.17:12.2 - Status label looks like a role name

A team proposes `BlockedReviewer` as a public label. F.17 does not accept it as a row until the direct patterns are separated. `Reviewer` is a role value; `blocked` is a status-family value or status-window value. The sheet may publish `Reviewer` as a role row and `Blocked` as a status row, with a note that a local UI may render them together. The table does not create a role called "blocked reviewer".

#### F.17:12.3 - Relation and slot names become reusable

An architecture pattern needs public names for `interfaceSlot`, `providedPort`, and `requiredPort`. The UTS row cites `A.6.5` for slot discipline, `A.6.RSIR` when the relation-signature-interface boundary is current, and `F.18` for durable names. The row does not treat a slot name as a component, role, or capability. If a project context uses `port` differently, the UTS row keeps the local sense and bridge explicit.

#### F.17:12.4 - Misleading evidence-role row

A sheet has a row labelled `Evidence role`. F.17 repairs the row by recovering the governed object instead of treating that label as a U-kind. If the claim is that an episteme is being used as evidence for another claim, `A.10`, `B.3`, or `A.2.4` governs the evidence relation. If the claim is that a system performs evidence-producing work, `A.2.1`, `F.6`, and `A.15.1` govern role assignment and performed work. The UTS may publish names for these values; a generic evidence-role row that fuses them is not admitted.

#### F.17:12.4a - Manufacturing batch across material and planning contexts

A furnace team uses `batch` for one physically handled set of shafts that shares a heat-treatment run and traceability basis. A planning dashboard uses `batch` for a grouping of intended PlanItems. Spelling does not make these one governed value. Recover the physical batch under the direct material or production DPF pattern, including its identity and part-whole treatment when current; recover the planning grouping under A.15.2 and its direct planning relation. Publish separate rows unless an F.9 Bridge states a narrower comparison or traceability relation with direction and loss. A `batch` row cannot turn a PlanItem grouping into a physical holon or make the physical batch a WorkPlan.

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
BridgeRefs: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11, CL=2, CellB-to-CellA only
RowRationale: this row names one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure for a cold public reader
AdmissibleUse: public naming of the governed demonstrative episteme
BlockedUse: actual traversal, method order, work order, performed work, or teaching-medium identity
RowEdition: 2026-07-11
CurrentnessCondition: review when the governed value, public bounded context, NameCard, local-sense basis relation, bridge loss, or reader evidence changes

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
BridgeRefs: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11, CL=2, CellB-to-CellA only
RowRationale: the bounded teaching alias adds repeated speech and attentional use while naming the same governed demonstrative episteme
AdmissibleUse: repeated English-language FPF seminar speech that helps participants hold the demonstrated solution structure in attention
BlockedUse: ritual authority, slogan, method, plan, work, fixed order, or reverse substitution from every public walkthrough
RowEdition: 2026-07-11
CurrentnessCondition: review when the seminar context, governed value, NameCard, local-sense basis relation, bridge loss, dictionary evidence, or reader evidence changes

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
BridgeRefs: none; expression and governed-row use are local to the same bounded seminar context
RowRationale: this row names one shown conditional pattern use with its Solution, expected result, and current condition inside a mantra
AdmissibleUse: bounded seminar reference to one demonstrated result-bearing continuation
BlockedUse: root Move, physical movement, operation, fixed serial step, PlanItem, performed Work, or continuation detached from its slice
RowEdition: 2026-07-11
CurrentnessCondition: review when the demonstrated-row schema, NameCard, local-sense basis relation, seminar context, or reader interpretation changes
```

The two senses of the same demonstrative value remain distinct:

```text
SenseCell.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  Context: FPF English public publication, edition 2026-07-11
  LocalExpression: demonstrative walkthrough
  LocalSense: one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure
  senseFamily: DemonstrativeExplanation
  NameCardRef: NameCard.DemonstrativeUnfoldingSlice.FPFPublic
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11

SenseCell.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  Context: English-language FPF seminar teaching, edition 2026-07-11
  LocalExpression: mantra
  LocalSense: a short repeatable explanatory walkthrough used to hold the whole solution structure in attention
  senseFamily: DemonstrativeExplanation
  NameCardRef: NameCard.DemonstrativeUnfoldingSlice.SeminarTeaching
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11

SenseCell.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11:
  Context: English-language FPF seminar teaching, edition 2026-07-11
  LocalExpression: mantra move
  LocalSense: one shown pattern-use continuation with its Solution, expected result, and current condition inside a mantra
  senseFamily: DemonstratedPatternUseContinuation
  NameCardRef: NameCard.DemonstratedPatternUseRow.SeminarTeaching
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11

LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  localSenseCellRef: SenseCell(FPF-English-Public-2026-07-11, DemonstrativeUnfoldingSlice-public)
  basisEpistemeRef: A.22.CGUS
  basisEpistemeKindRef: U.MethodDescription
  basisPublicationUnitRef: A.22.CGUS:4.3.3-Ordinary-bounded-use
  boundedContextRef: FPF English public publication, edition 2026-07-11

LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
  boundedContextRef: FPF English public publication, edition 2026-07-11
  viewpointRef: FPFPublicReaderViewpoint
  subjectRef: <LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11, FPF English public publication 2026-07-11, FPFPublicReaderViewpoint>
  claimGraph:
    supportedSenseClaim: one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure
    admittedUseClaim: support the public local-sense line for this SenseCell
    nonAdmittedUseClaim: no evidence, authority, work-order, or naming decision follows from this relation
  referenceScheme: F.3 SenseCell and F.17 local-sense-basis interpretation
  editionId: 2026-07-11

LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  localSenseCellRef: SenseCell(FPF-Seminar-Teaching-2026-07-11, DemonstrativeUnfoldingSlice-mantra)
  basisEpistemeRef: SeminarExpression.FPFPracticalUse.2026-07-11
  basisEpistemeKindRef: U.EpistemePublication
  basisPublicationUnitRef: SeminarExpression.FPFPracticalUse.2026-07-11.Slides8-10
  boundedContextRef: English-language FPF seminar teaching, edition 2026-07-11

LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
  boundedContextRef: English-language FPF seminar teaching, edition 2026-07-11
  viewpointRef: FPF Seminar Participant Viewpoint
  subjectRef: <LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11, English-language FPF seminar teaching 2026-07-11, FPF Seminar Participant Viewpoint>
  claimGraph:
    supportedSenseClaim: a short repeatable explanatory walkthrough used to hold the whole solution structure in attention
    admittedUseClaim: support the bounded teaching sense from the seminar expression
    nonAdmittedUseClaim: the slide carrier does not become the sense, naming settlement, method, plan, or work
  referenceScheme: F.3 SenseCell and F.17 local-sense-basis interpretation
  editionId: 2026-07-11

LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11:
  localSenseCellRef: SenseCell(FPF-Seminar-Teaching-2026-07-11, DemonstratedPatternUseRow-mantra-move)
  basisEpistemeRef: SeminarExpression.FPFPracticalUse.2026-07-11
  basisEpistemeKindRef: U.EpistemePublication
  basisPublicationUnitRef: SeminarExpression.FPFPracticalUse.2026-07-11.Slides61-62
  boundedContextRef: English-language FPF seminar teaching, edition 2026-07-11

LocalSenseBasisRelationDescription.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
  boundedContextRef: English-language FPF seminar teaching, edition 2026-07-11
  viewpointRef: FPF Seminar Participant Viewpoint
  subjectRef: <LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11, English-language FPF seminar teaching 2026-07-11, FPF Seminar Participant Viewpoint>
  claimGraph:
    supportedSenseClaim: one shown pattern-use continuation with its Solution, expected result, and current condition inside a mantra
    admittedUseClaim: support the bounded teaching sense of mantra move
    nonAdmittedUseClaim: the slide carrier does not become the row, pattern use, plan, or performed work
  referenceScheme: F.3 SenseCell and F.17 local-sense-basis interpretation
  editionId: 2026-07-11
```

`SeminarExpression.FPFPracticalUse.2026-07-11` names the published seminar content as a `U.EpistemePublication`; the `.pptx` and extracted Markdown are separate carriers or renderings. The public relation instead relies on the current `A.22.CGUS` pattern episteme and narrows that reliance to the ordinary-use publication unit.
The cross-context relation is complete by value. `DemonstrativeExplanation` is an F.9 local `senseFamily` label, not a U-kind.

```text
BridgeCardId: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11
BridgeCard:
  CellA: SenseCell.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11
  CellB: SenseCell.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11
  senseFamilyA: DemonstrativeExplanation
  senseFamilyB: DemonstrativeExplanation
  BridgeKind: Narrower-than
  Direction: CellB is narrower than CellA; only CellB-to-CellA use is admitted
  CL: 2
  LossNotes: the broader public sense does not include repeated speech, remembered replay, or the seminar attentional function
  CounterExampleOrInvariantEvidence: a public demonstrative walkthrough may be read once and understood without being repeated or used as a mnemonic
  AdmittedUse: naming-only; a seminar use of mantra may point to the public demonstrative-walkthrough term and its governed value
  NonAdmittedUse: no CellA-to-CellB substitution; no claim that every public walkthrough is a mantra; no inference of method, plan, order, authority, work, or teaching-medium identity
  DirectGoverningPatternIfNotF9: none; F.9 governs this substitution Bridge
  RevisionTrigger: either bounded-context edition changes, reader tests change the observed loss, or the selected local label or governed value changes
```

The bridge is directional because the seminar sense adds repetition and attentional use. Shared reference to one governed value does not erase that sense difference. `CL=2` is admitted only with the explicit counterexample; it does not admit reverse substitution or structural inference.

The seminar deck and its textual extraction establish the teaching problem and observed concept use. They do not establish English lexical admissibility by themselves. Current English dictionary evidence supports the repeated-formula and watchword senses of `mantra`, while its Sanskrit analysis as an instrument of thought supplies the attentional rationale. F.18 and reader-use evidence decide whether that English candidate fits this bounded FPF context. This row does not claim that every local pattern mantra is a `DemonstrativeUnfoldingSlice@Context`; a pattern-local formula is interpreted from that pattern's Solution unless a stronger governed value is claimed. This row makes no cross-language sameness claim; a term published in another language needs its own bounded NameCard, evidence, and F.17 sense relation.

No F.17 row is published for `working product`. The phrase has no single governed value across physical entities, changed states, capabilities, relations, and epistemes. Technical text uses the exact subject-governed result name; ordinary explanation may say `result produced by work`, or `first useful result` when firstness and receiving-use value have been established.


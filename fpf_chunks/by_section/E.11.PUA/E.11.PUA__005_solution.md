---
chunk_kind: "child"
pattern_id: "E.11.PUA"
pattern_title: "Pattern Use in a Working Situation and First Useful Result"
section_id: "E.11.PUA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUA/E.11.PUA__005_solution.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "E.11.PUA — Pattern Use in a Working Situation and First Useful Result"
  - "E.11.PUA:4 — Solution"
line_start: 75131
line_end: 75452
dependencies:
  - "A.15"
  - "A.6.5"
  - "C.2.1"
  - "E.11"
  - "E.11.PUR"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.22"
  - "E.23"
  - "E.8"
  - "G.11"
keywords:
---

### E.11.PUA:4 - Solution

Apply one selected pattern through a short result-oriented procedure. Keep the subject result in the foreground; add addressable pattern-use records only when a named receiving use relies on them.

#### E.11.PUA:4.0 - Kind-preserving dependency spine

The acting `U.System` works under a `U.RoleAssignment`: it selects, constructs, or refines a semantic `U.Method`, records intended work only when planning is current, performs dated `U.Work`, and thereby changes, preserves, examines, or evaluates the real EntityOfConcern. The epistemic support line may guide and evaluate this work; it does not become the actor, role assignment, method, work, or affected entity.

Use this conceptual dependency structure. It states semantic dependencies and possible results, not a workflow, form, interface, serialization, or instruction to materialize every position:

```text
current EntityOfConcern + bounded context + practical question
  -> optional accepted problem-side material when current
  -> public-template or direct-pattern inspection
  -> selected or rejected direct pattern under a fit reason
  -> selected, constructed, or refined U.Method when the Solution makes that method current
  -> PlanItem or U.WorkPlan when intended work is current
  -> dated U.Work when work occurs
  -> exact direct result under its governing pattern
  -> receiving use, stop, return, or neighboring pattern when current
```

`TaskSignature` remains a pre-method-selection signature. It can constrain method search; it is not the task, plan, or work occurrence. OEE and NQD may retain method or architecture candidates before selection. G.5 publishes a selected set; A.3.1 settles method identity; A.15 governs planning and work.

#### E.11.PUA:4.1 - The ordinary seven-step use

1. **Recognize the working situation.** Name the subject or relation in ordinary domain language and ask the current practical question. State an exact kind now only when a nearby kind difference can change the pattern or result.
2. **Inspect one direct pattern.** Read its Problem frame, Problem, Forces, Solution, Consequences, ordinary boundary, and nearest stronger neighbor. Do not select from its title or one trigger word alone.
3. **Say what useful result would answer the question.** Name the result plainly enough to distinguish it from a plan, description, recommendation, work occurrence, or other nearby value. Make kind, relation signature, flow position, and receiving-use relation explicit only when that distinction remains ambiguous or a named later use will rely on replay.
4. **Apply the Solution.** Perform the pattern's action-guiding method under its conditions. A project-tailored method description, WorkPlan, gate result, or work occurrence is created only through its direct governing pattern.
5. **Check what now exists.** The use may have produced a new result, grounded a result that already existed for the current question, or produced only an honest interim result while the subject-result expectation stays open. Do not turn grounding into production.
6. **State the immediate continuation only as needed.** Name the next receiving use, stronger neighbor, or unresolved clarification in conversation. Materialize basis, expectation, result, flow, provenance, or boundary epistemes only when a named later use needs them to remain addressable.
7. **Stop or return.** Stop when the smallest useful produced or grounded result can answer the current question. Return when the concern, basis, expected result, governing pattern, result kind, or receiving-use condition changes.

The practical delta has three honest forms. A result absent before the use may exist afterward. A pre-existing result may remain the same entity while its grounding for the current receiving use becomes adequate. If the subject result still does not exist, the smallest interim result and return condition become explicit while the expectation remains open.

#### E.11.PUA:4.2 - Reliance profiles

```text
PatternUseRelianceProfileValue = ordinaryBounded | relianceBearing
```

In `ordinaryBounded` use, the subject, practical question, inspected pattern, useful result in ordinary language, and stop or return remain recoverable in conversation. State an exact kind or relation signature only when needed to distinguish the result from a nearby value. No candidate basis, fit record, flow-position record, provenance note, or closure record is required.

In `relianceBearing` use, materialize only the distinctions that the named receiving use will rely on. Transfer may need a candidate basis and rationale. Automation may need exact kinds and relation signatures. Delayed review may need the result, flow position, and receiving-use disposition. No profile causes all support records to be materialized.

When one named later use needs a compact replay carrier but not the fuller candidate and closure relations, use this reliance-bearing trace:

```text
CompactPatternUseTrace@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  practicalQuestionDescriptionRef: U.EpistemeRef
  consideredDirectPatternRef: U.EntityRef, referencing one U.MethodDescription
  patternSelectionDisposition: selected | rejected
  compactFitRationaleRef: U.EpistemeRef
  expectedResultKindRef: U.KindRef
  expectedResultRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  expectedResultDescriptionRef: U.EpistemeRef
  obtainedResultRef?: U.EntityRef
  obtainedResultKindRef?: U.KindRef
  obtainedResultRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  boundaryDisposition: stop | return
  boundaryConditionDescriptionRef: U.EpistemeRef
  conditionalReceivingPatternRef?: U.EntityRef, referencing one U.MethodDescription
```

The trace is absent from ordinary conversational use. When materialized for a named reliance, the expected-result signature is present exactly when the expected kind admits a relation. A selected pattern may have an obtained result; a rejected pattern leaves obtained-result positions absent. A return names its receiving pattern; a stop does not.

#### E.11.PUA:4.2.1 - Admitted support species and governing patterns

```text
PracticalUseQuestion@Context <: U.Episteme
PatternUseResultExpectation@Context <: U.Episteme
PatternUseBoundaryCondition@Context <: U.Episteme
CandidatePatternUseRationale@Context <: U.Episteme
PatternUseCoordinationRationale@Context <: U.Episteme
PracticalUseCardComparisonRationale@Context <: U.Episteme
PatternUseFitFinding@Context <: U.Episteme
CandidatePatternUse@Context <: U.Episteme
PatternUseApplicabilityFinding@Context <: U.Episteme
```

PUA governs the practical question, optional compact trace, candidate basis, candidate support episteme, candidate rationale, and actual-result closure. `E.11` governs public card comparison rationale. `E.11.PUR` governs fit, applicability, recommendation, coordination rationale, coordination, and ordering. These relations consume A.6.5 SlotSpec discipline; A.6.5 does not govern their identity.

#### E.11.PUA:4.3 - Question, boundary, and expectation

```text
PracticalUseQuestion@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  questionDescriptionRef: U.EpistemeRef

PatternUseBoundaryCondition@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the CandidatePatternUse@Context or PracticalUseQuestion@Context whose use is bounded
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  boundaryConditionKind: candidateAdmission | minimumUsableResult | stop | return | wrongTurnRecovery | strongerNeighbor | costEscalation | reversibilityEscalation | handoff
  conditionDescriptionRef: U.EpistemeRef
  governingPatternRef: U.EntityRef, referencing one U.MethodDescription
  conditionalReceivingPatternRef?: U.EntityRef, referencing one U.MethodDescription
  conditionalReceivingPatternPositionKindRef?: U.KindRef
  conditionalReceivingPatternPositionRef?: U.EntityRef

PatternUseResultExpectation@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the CandidatePatternUse@Context whose result is expected
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  expectedResultKindRef: U.KindRef
  expectedResultRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  expectedResultFlowPosition: patternSelectionFlowResult | selectedPatternApplicationFlowResult | downstreamSubjectWorkFlowResult
  expectedResultDescriptionRef: U.EpistemeRef
  minimumUsableResultBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  intendedReceivingPatternRef: U.EntityRef, referencing one U.MethodDescription
  intendedReceivingUseDescriptionRef: U.EpistemeRef
  handoffBoundaryRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The expectation never proves that the result exists. `return`, `wrongTurnRecovery`, `strongerNeighbor`, and `handoff` boundaries name the receiving pattern. The remaining boundary kinds leave that position absent. Receiving-position kind and ref are both present or both absent. `candidateAdmission` means that Problem frame, Forces, Solution conditions, expected result, and ordinary boundary are recoverable enough for further inspection; it is neither an applicability finding nor a selection.

#### E.11.PUA:4.4 - Candidate basis under named reliance

Construct a durable candidate only after inspecting the direct pattern's Problem frame, Problem, Forces, Solution, Consequences, and ordinary boundary. A public README template can supply a reusable starting point, but current project values come from the bounded context.

```text
CandidatePatternUseBasisRelation@Context <: U.Relation:
  publicTemplateRef?: U.EpistemeRef, referencing one PublicCandidatePatternUseTemplate@FPFReadme
  directPatternRef: U.EntityRef, referencing one U.MethodDescription
  directSolutionSectionRef: U.EntityRef, referencing the E.17 PublicationUnit containing the direct pattern's Solution
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  practicalUseQuestionRef: U.EpistemeRef, referencing one PracticalUseQuestion@Context
  problemCardRef?: U.EpistemeRef, referencing one ProblemCard@Context
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  additionalBasisRelationRefs[]?: U.EntityRef, each referencing one CandidatePatternUseAdditionalBasisRelation@Context
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  RelationRefKind: U.EntityRef
  Direction: <entityOfConcernRef, practicalUseQuestionRef, directPatternRef> -> candidatePatternUseRef
  Dependence: bounded-context local to the direct pattern, question, expectation, and candidate editions
  Identity: <boundedContextRef, entityOfConcernRef, practicalUseQuestionRef, directPatternRef, directSolutionSectionRef, resultExpectationRef, candidatePatternUseRef>

CandidatePatternUseAdditionalBasisRelation@Context <: U.Relation:
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  basisValueRef: U.EntityRef
  basisValueKindRef: U.KindRef
  basisRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  basisGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  basisUseDescriptionRef: U.EpistemeRef
  RelationRefKind: U.EntityRef
  Direction: basisValueRef -> candidatePatternUseRef for basisUseDescriptionRef
  Dependence: bounded-context local to the candidate and basis value editions
  Identity: <candidatePatternUseRef, basisValueRef, basisValueKindRef, basisRelationSignatureRef if present, basisUseDescriptionRef>

CandidatePatternUse@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  practicalUseQuestionRef: U.EpistemeRef, referencing one PracticalUseQuestion@Context
  problemCardRef?: U.EpistemeRef, referencing one ProblemCard@Context
  publicTemplateRef?: U.EpistemeRef, referencing one PublicCandidatePatternUseTemplate@FPFReadme
  directPatternRef: U.EntityRef, referencing one U.MethodDescription
  directSolutionSectionRef: U.EntityRef, referencing the E.17 PublicationUnit containing the direct pattern's Solution
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  candidateAdmissionBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  returnBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

Each additional basis relation names its exact value, kind, relation signature when current, direct governing pattern, and use in this candidate. The public template is absent when the candidate was formed by direct pattern inspection without a README template. `directSolutionSectionRef` is the Solution section of `directPatternRef`; no redundant solution-method-description ref is retained. A project-tailored method description, when produced, is a separate `U.MethodDescription` under A.3.2 with its own derivation or reuse relation to the direct pattern. Applicability, recommendation, and coordination remain governed by `E.11.PUR`.

#### E.11.PUA:4.4.1 - Rationale subjects stay distinct

```text
CandidatePatternUseRationale@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one CandidatePatternUse@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  rationaleDescriptionRef: U.EpistemeRef
  rationaleBasisEpistemeRefs[]: U.EpistemeRef
  rationaleUseBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

Candidate rationale has one candidate subject. `E.11.PUR` owns the coordination-rationale schema over a declared candidate set. `E.11` owns the public-card comparison-rationale schema over one public guidance episteme before a project candidate is constructed. No rationale episteme is a universal bag.

#### E.11.PUA:4.5 - Actual result and receiving-use disposition

Materialize this relation only when a named receiving use relies on addressable closure:

```text
PatternUseActualResultReceivingUseDispositionRelation@Context <: U.Relation:
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  actualResultRef: U.EntityRef
  actualResultKindRef: U.KindRef
  actualResultRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  resultGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  resultFlowPosition: patternSelectionFlowResult | selectedPatternApplicationFlowResult | downstreamSubjectWorkFlowResult
  resultProducingPathSliceId?: PathSliceId
  resultProducingDesignRunTag?: DesignRunTag
  resultProducingWorkRefs[]?: U.EntityRef, each referencing one U.Work
  receivingUseRealizationState: realized | intendedNotYetRealized
  realizedReceivingUseRelationRef?: U.EntityRef
  realizedReceivingUseRelationKindRef?: U.KindRef
  receivingUseRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  receivingUseGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  intendedReceivingUseDescriptionRef?: U.EpistemeRef
  receivingUseRealizationConditionRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  closureBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  RelationRefKind: U.EntityRef
  Direction: candidatePatternUseRef through resultExpectationRef -> actualResultRef -> realizedReceivingUseRelationRef or intendedReceivingUseDescriptionRef
  Dependence: bounded-context local to candidate, expectation, actual result, and receiving-use editions
  Identity: <candidatePatternUseRef, resultExpectationRef, actualResultRef, resultFlowPosition, receivingUseRealizationState, realizedReceivingUseRelationRef if present, intendedReceivingUseDescriptionRef if present>
```

Candidate, expectation, actual result kind, conditional relation signature, and flow position agree. Path slice and `DesignRunTag` are both present when cross-flow provenance is asserted and both absent otherwise. A result from one flow may become an input, tool, context, or constraint in another flow without changing kind; E.18 carries its new relation position, transfer or crossing relation, and the current `DesignRunTag` boundary.

In the `realized` state, the exact receiving-use relation, kind, and signature are present, while intended-use description and realization condition are absent. In `intendedNotYetRealized`, the intended-use description and realization condition are present, while realized relation positions are absent.

When the actual result is `U.Work`, it names the A.15.1-grounded occurrence and `resultProducingWorkRefs[]` is absent. Planning, setup, authorization, triggering, or enabling work does not become the producer of that occurrence. When dated work produces or changes a result of another kind, each cited work occurrence belongs to the same flow and actually produced or changed that result.

#### E.11.PUA:4.6 - Pre-existing and not-yet-produced results

When the result existed before the current use, preserve that fact:

```text
PreExistingResultGroundingFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the pre-existing result entity
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  actualResultReceivingUseDispositionRelationRef: U.EntityRef, referencing one PatternUseActualResultReceivingUseDispositionRelation@Context
  currentGroundingBasisRefs[1..*]: U.EpistemeRef
  groundingAdequacyDescriptionRef: U.EpistemeRef
  groundingUseBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The finding is produced by the current grounding exercise. The grounded entity is not. Earlier producing-work provenance remains absent unless its exact relation and evidence are current.

When the expected subject result does not yet exist, close the current use on the exact interim result, its kind, governing pattern, and flow position. Keep the subject-result expectation open. A plan for machining does not become a machined component; a treatment recommendation does not become a changed clinical state; an assessment plan does not become learned capability.

#### E.11.PUA:4.7 - Reliance-bearing final-practice test

Use this test when the declared teaching, rehearsal, or evaluation use is to establish that a participant can select a pattern, preserve the kind of its result, and leave another participant a replayable continuation. This is deliberately `relianceBearing`: the evaluator relies on the selected basis, expectation, grounding state, and continuation. Its row count is a test condition, not a general rule for pattern use. The test does not require or assert a wider CGUS.

```text
PatternUsePracticeContinuationDescription@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the selected CandidatePatternUse@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  actionOrProposedUseDescriptionRef: U.EpistemeRef
  expectedResultDescriptionRef: U.EpistemeRef
  expectedResultKindRef: U.KindRef
  directPatternIdentifier: PatternIdentifierValue
  directPatternName: PatternNameValue
  currentConditionDescriptionRef: U.EpistemeRef
  continuationDisposition: continue | branch | return | stop

FinalPracticePatternUseTestResult@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the selected CandidatePatternUse@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  practicalUseQuestionRef: U.EpistemeRef, referencing one PracticalUseQuestion@Context
  selectedCandidatePatternUseBasisRelationRef: U.EntityRef, referencing one CandidatePatternUseBasisRelation@Context
  selectedFirstResultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  selectedFirstResultGroundingState: SelectedFirstResultGroundingStateValue
  selectedFirstResultFlowPosition: PatternUseResultFlowPositionValue
  producedDuringExerciseActualResultRelationRef?: U.EntityRef, referencing one PatternUseActualResultReceivingUseDispositionRelation@Context
  preExistingResultGroundingFindingRef?: U.EpistemeRef, referencing one PreExistingResultGroundingFinding@Context
  notYetProducedInterimResultRef?: U.EntityRef
  notYetProducedInterimResultKindRef?: U.KindRef
  notYetProducedInterimResultRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  notYetProducedInterimResultGoverningPatternRef?: U.EntityRef, referencing one U.MethodDescription
  notYetProducedInterimResultFlowPosition?: PatternUseResultFlowPositionValue
  practiceContinuationDescriptionRefs[3..5]: U.EpistemeRef, each referencing one PatternUsePracticeContinuationDescription@Context
  branchOrReturnContinuationDescriptionRef: U.EpistemeRef, referencing one member of practiceContinuationDescriptionRefs
  continuableWorkStateDescriptionRef: U.EpistemeRef
  explicitUnknownDescriptionRef: U.EpistemeRef
  minimalClarificationPatternRef: U.EntityRef, referencing one U.MethodDescription
  expectedClarificationResultKindRef: U.KindRef
  admittedDemonstrativeSliceRef?: U.EpistemeRef, referencing one DemonstrativeUnfoldingSlice@Context
  demonstratedPatternUseRowRefs[3..5]?: U.EpistemeRef, each referencing one DemonstratedPatternUseRow@Context
```

Each practice continuation description states an action or proposed use, the expected result and its kind, the full PatternID and pattern name, and the condition under which that continuation is current. Its `entityOfConcernRef` resolves to the same selected `CandidatePatternUse@Context` as the test result. The test passes only when at least one of the three to five descriptions has `continuationDisposition=branch` or `return`, the final continuable work position is explicit, and one consequential unknown names the minimum clarification pattern and expected clarification-result kind. The selected basis relation resolves to that same candidate; the candidate names the same question and expectation as the test result, and the expectation and test result name the same flow position.

The practice descriptions remain ordinary PUA epistemes when no wider CGUS is admitted. If a wider CGUS is later admitted, `admittedDemonstrativeSliceRef` and `demonstratedPatternUseRowRefs[3..5]` are both present or both absent. The rows correspond in order to the existing practice descriptions, and each row's `sourcePracticeContinuationDescriptionRef` points to its corresponding description. They do not replace or retype the descriptions, candidate, subject result, or continuable work position.

`SelectedFirstResultGroundingStateValue` is `producedDuringExercise | preExistingWithGrounding | notYetProduced`. Exactly one state branch is filled:

- For `producedDuringExercise`, fill `producedDuringExerciseActualResultRelationRef` and leave the other state positions absent. The actual-result relation names the selected candidate and expectation. Its result kind, conditional relation signature, and flow position agree with the expectation. The subject result itself was produced during the exercise.
- For `preExistingWithGrounding`, fill `preExistingResultGroundingFindingRef` and leave the other state positions absent. The finding's `entityOfConcernRef` names the already-existing result; the finding agrees with the selected candidate, expectation, and actual-result relation and cites the current grounding basis. The exercise produces the grounding finding; it does not produce the entity that already existed.
- For `notYetProduced`, fill all five interim-result positions and leave both actual-result positions absent. They name the exact result produced by the current test or planning flow, including its kind, governing pattern, flow position, and relation signature when the kind admits one. The interim result may support later work but does not satisfy the selected subject-result expectation.

The continuable-work description says what project work can proceed from this state-specific result. The test fails when it merely retells a card, expands into a whole-project plan, treats a public template as a recommendation, claims performed work without an A.15.1-grounded `U.Work`, infers a physical, clinical, organizational, or learned change from its description, or asserts a CGUS only because the practice contains several rows.

#### E.11.PUA:4.8 - Replay and currentness

For immediate `ordinaryBounded` use, recover from the conversation the working subject and question, the direct pattern inspected, the useful result produced or grounded, and the stop or return. Do not reconstruct a candidate dossier merely to replay a cheap local use.

When a named later use relies on fuller replay, recover the exact concern, bounded context, practical question, selected direct pattern and edition-pinned Solution, expected result kind and conditional relation signature when applicable, flow position, grounded actual or honest interim result, receiving-use disposition, and stop or return boundary from the support relations materialized for that reliance.

Recheck the smallest affected claim or relation when the concern, candidate basis, direct Solution, expected result, result grounding, flow position, receiving-use condition, or boundary changes. Reopen pattern selection only when that change alters candidate fit; a new measurement of the same result does not by itself select another pattern. `G.11` governs edition, telemetry, currentness-window, and decay orchestration; PUA supplies the use-specific values and change conditions that orchestration inspects.


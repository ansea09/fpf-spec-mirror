---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__005_solution.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:4 — Solution"
line_start: 121625
line_end: 121903
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.25"
  - "E.10"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.22:4 - Solution

E.22 gives requester and evaluator a compact way to declare the quality question that will guide improvement. The evaluator answers the question. A decision or work product beyond the authority of that evaluation must be obtained separately.

#### E.22:4.0 - Form a usable first request

Start from the result the recipient needs. The recipient may need a document to explain an operation, the operation to obtain a result, and the result to inform a further decision. Select the object and judgement needed now. A candidate's narrower description cannot establish that the larger receiving need has been satisfied.

1. **Name the use and object version.** Say who needs the answer, what work or decision it will inform, and which version is being evaluated. Include the conditions that affect that use. If the receiving need is unclear, recover it with the recipient or the applicable problem-formulation method.
2. **Choose the question and criterion.** Say whether the recipient needs floor adequacy, further improvement, a comparison of trade-offs or the effect of applied findings. Use the characteristic space and predicate or comparator supplied by an adequate evaluation. State the floor or improvement aim and the qualities a proposed repair must preserve.
3. **Connect the criterion to attainable grounds.** Identify the content, observations or reasoning needed to answer it. Tracing a source contribution into an instruction can establish a coherent construction. Trying the instruction on material can reveal a missing action. An observed application can support a performance claim under the conditions observed. State which answer is required, what the intended reader or performer can supply, and what the candidate must supply. If indispensable grounds are absent, ask for the exact unresolved condition rather than an unsupported pass.
4. **Specify the useful return.** Name the evaluation's result form and the conclusion it can support. A floor answer identifies sufficiency or the first needed repair; an improvement answer also describes the proposed change, expected gain, protected trade-offs and closure test. State evaluator conditions only when they change the question or admissibility of the answer.

When several contributions are needed, retain what their available evaluations establish and ask about the necessary connection still unanswered. A good explanation, a supported source claim and a correct constituent operation can all remain valid while their combined use is unestablished. Evaluate that connection for its own object and use. Combining unlike scores cannot establish quality for the whole.

Write the request in ordinary language with these bindings recoverable, as in section 5. The local names and schemas below specify their exact meanings when the question is represented as a `QualityEvaluationQuestionFrame` and `QualityEvaluationUseDeclaration`. Reuse the selected evaluation's adequate descriptions and defaults. Add an intended evaluator's identity or a dated-Work account only when the receiving question requires it.

Stop framing when the question and expected answer are sufficiently determined for the intended evaluation. If an existing request already supplies them, perform the direct evaluation and inspect whether its grounds support the consuming conclusion. A separate frame is useful when it resolves a missing or disputed binding. Restating settled bindings adds no answer.

#### E.22:4.1 - Local names and kind settlement

E.22 frames the question. The evaluator judges the object. `evaluationPatternLocator` identifies the FPF pattern description containing the evaluation predicate or constraint; an optional `semanticEvaluationMethodRef` names the separately identified `U.Method` used for that evaluation.

A characteristic-space specification, Q-Bundle description, rubric description, review-profile description, evidence-basis description, and result-form description constrain or describe that evaluation. The subject assertion and any semantic Method retain their independent bases.

For example, `E.21`, `E.9.DA`, or `E.2.DA` may supply the predicate for evaluating one FPF object, while `A.19.ECS` and `C.25` supply supporting quality-model descriptions. `E.19` supplies admission or refresh review questions and findings. Apply E.19 when that review is the requested result. When its findings support a quality evaluation, `evaluationPatternLocator` names the pattern that defines that evaluation, and the quality result cites the relied-on review findings as evidence.

A below-floor value, finding, improvement aim, or need for evaluation is not by itself an actual Problem. If the consuming use relies on an actual Problem, cite one current C.22.PFR `ProblematicForRelation` occurrence with its direct participants and temporal identity. The frame, evaluation, result and evidence may support a claim about that occurrence. None creates or splits it.


The framing episteme, evaluation method, descriptions used by that method, any question-changing evaluator condition, dated evaluation Work, actual operation application, evidence use, and result have distinct functions. `QualityEvaluationUseDeclaration` collects the applicable evaluation bindings. A plan, declaration or named candidate does not establish a current performer or occurrence.

The local support names ending in `@Context` serve only compatibility and retrieval. The suffix supplies no context entity, scope, participant, relation, or identity component. Every episteme follows C.2.1 identity, every set is identified by its stated extensional rule, and every neighboring Work, decision, evidence, viewpoint, grounding, or result relation remains under its direct governor.

| Local name | Kind and use in this pattern |
|---|---|
| `QualityEvaluationQuestionFrame` | `U.Episteme` whose EntityOfConcern is the exact object version under evaluation; its ClaimGraph carries the requested quality-evaluation question about that version and its exact use bindings. |
| `QualityEvaluationUseDeclaration` | `U.Episteme` whose EntityOfConcern is the same object version. It describes how evaluation of that version is intended to be performed and interpreted, referring separately to the evaluation pattern, optional semantic Method, selected characteristic space, predicate and any comparator, ClaimScope, quality-model descriptions, expected evidence basis, result form, and qualification window. It may state an eligibility, independence, capability or planned condition for the evaluator when that condition changes the question or admissibility of the result. It may name an intended evaluator only when that identity is part of the question. It contains no actual performer, assignment, or Work occurrence. |
| `ObjectVersionUnderQualityEvaluation` | Exact `U.Entity` version being evaluated, paired with its exact `U.Kind`. |
| `EvaluationCharacteristicSpaceSelection` | One exact `U.CharacteristicSpace` selected for this evaluation use. The episteme that specifies the space has its own identity. |
| `EvaluationCriterionSelection` | The exact by-value `CharacteristicSpacePredicate`, exact admitted `ComparatorSpecRef`, or both, required by the governing evaluation pattern and, when declared, its separately identified semantic evaluation Method. At least one is present. |
| `EvaluationClaimScope` | One exact set-valued `U.ClaimScope` governing the evaluation claim. It is not a context label, selected structure, window, or evidence set. |
| `QualityEvaluationResultConsumingUse` | The specific intended-work, dated-work or decision object expected to use the result, under the rule that directly governs that object, paired with its exact kind and use description. Naming it neither authorizes nor performs that use. |
| `QualityEvaluationPurposeSelection` | Requested evaluation purpose or distinguishable combination of purposes. |
| `DeclaredQualityFloor` | Minimum acceptable coordinate or status floor when the frame declares a floor claim. |
| `DesiredImprovementAim` | Requested substantive change beyond the floor when improvement beyond the floor is requested. |
| `ExpectedEvaluationEvidenceBasis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version under evaluation. It describes expected evidence-use positions and the missingness rule for the exact method, space, criterion, scope, and qualification window. It can be identified before a use declaration cites it. The description and the evidence values later found are distinct. |
| `TradeoffProtectionSet@Context` | A mathematical set of references to protected characteristics or coordinates, each paired with its kind. The declaration specifies the permitted elements. The question-frame edition determines which pairs are admissible for this use. Its members identify the set extensionally. |
| `EvaluationQualificationWindow` | Edition, source-currentness, comparison-set, time, or declared-use window in which the requested result is intended to be current. The actual evaluation application later binds its exact point or interval. |
| `ExpectedQualityEvaluationResultFormDescription` | `U.Episteme` describing the result-row form declared by the governing evaluation pattern. It is not an actual result. |
| `QualityReviewFindingRow` | Actionable evaluation finding that identifies the observed issue, affected evaluation property, correction direction, and closure test. |
| `CandidateImprovementProposalRow@Context` | E.22 proposal episteme with an exact correction target, expected substantive evaluation effect, trade-offs, kind-restoration disposition, outside-claim return when needed, and closure test. |
| `CandidateImprovementOutsideClaimReference@Context` | Bounded local ClaimGraph node form inside one proposal row. It identifies the outside governed value, relation signature, or boundary description and the exact FPF pattern identity that governs the return. It belongs to its proposal row and cannot be referenced independently. It is neither an episteme nor a relation. |
| `KindRestorationCheck` | Conditionally present check when a changed FPF-governed expression can alter the object, kind, relation, slot or use position, claim kind, admissible use, or scope. |
| `CandidateImprovementProposalPortfolio@Context` | A mathematical set whose local element range consists of `CandidateImprovementProposalRow@Context` epistemes addressing one question frame. Resolve each proposal under C.2.1 and the proposal conditions in 4.4. The frame determines which proposals may belong and how the set may be used. The set is identified by its members. |
| `ImprovementFollowUpHypothesis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version expected to change. It claims that one named next operation or method application is expected to address one finding and produce a stated evaluation effect under a stated test condition. A stop disposition, return, selected plan, performed Work, or actual Transformation is not such a hypothesis. |

In each filled episteme form below, `claimGraph` carries its complete interpreted claims and semantic relations by value, in the C.2.1:4.1.2 range `NonemptyClaimContent`. `referenceScheme` carries the effective rule collection by value in `EpistemeInterpretationScheme`; those rules must interpret the form's designations, predicates and qualifications. The remaining fields state the claims of that episteme. Range membership alone establishes neither their truth nor a completed evaluation.

```text
QualityEvaluationUseDeclaration <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under evaluation
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: NonemptyClaimContent by value
  referenceScheme: EpistemeInterpretationScheme by value
  editionId
  evaluatorConditionRef?: U.EpistemeRef, referencing an eligibility, independence, capability, or planned condition only when it changes the evaluation question or admissibility of the result
  intendedEvaluatorSystemRef?: U.EntityRef, referencing one admitted U.System only when that identity is part of the declared question; it asserts neither assignment nor performance
  evaluationPatternLocator: U.EntityRef, locating the exact FPF pattern description that contains the defining or constraining ClaimGraph
  semanticEvaluationMethodRef?: U.MethodRef, referencing the separately identified U.Method used for the evaluation
  selectedEvaluationCharacteristicSpaceRef: U.EntityRef, referencing one exact U.CharacteristicSpace
  selectedEvaluationPredicate?: CharacteristicSpacePredicate by value
  selectedComparatorSpecRef?: ComparatorSpecRef
  evaluationClaimScopeRef: U.EntityRef, referencing one exact U.ClaimScope
  evaluationQualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
  evaluationCharacteristicSpaceSpecDescriptionRef?: U.EpistemeRef, referencing one A.19.ECS specification description
  evaluationQBundleDescriptionRef?: U.EpistemeRef, referencing one C.25 Q-Bundle description
  evaluationRubricDescriptionRef?: U.EpistemeRef, referencing one evaluation-rubric description
  evaluationReviewProfileDescriptionRef?: U.EpistemeRef, referencing one evaluation-review-profile description
  expectedEvaluationEvidenceBasisRef: U.EpistemeRef, referencing one ExpectedEvaluationEvidenceBasis@Context
  expectedEvaluationResultFormDescriptionRef: U.EpistemeRef, referencing one ExpectedQualityEvaluationResultFormDescription

ExpectedEvaluationEvidenceBasis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version whose evaluation needs the expected evidence
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: NonemptyClaimContent by value
  referenceScheme: EpistemeInterpretationScheme by value
  editionId
  evaluationPatternLocator: U.EntityRef, locating the same FPF evaluation pattern description
  selectedEvaluationCharacteristicSpaceRef: U.EntityRef, referencing the same U.CharacteristicSpace
  selectedEvaluationPredicate?: CharacteristicSpacePredicate by value
  selectedComparatorSpecRef?: ComparatorSpecRef
  evaluationClaimScopeRef: U.EntityRef, referencing the same U.ClaimScope
  expectedEvidencePositionDescriptionRefs[1..*]: U.EpistemeRef, each referencing one evidence-position description
  expectedEvidenceRelationKindRefs[1..*]: U.KindRef, each referencing one expected evidence-relation kind
  missingEvidenceDispositionRuleRef: U.EpistemeRef, referencing one exact episteme that states the missing-evidence disposition rule under its subject pattern
  qualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
```

Every field above with a `*Ref` suffix stores the stated A.6.5 `RefKind`; resolving it yields the referent kind named after `referencing`. The use declaration and expected evidence basis carry the same object version, governing evaluation pattern, selected characteristic space, criterion binding, ClaimScope, and qualification window.

Construct the expected basis from those values, the expected evidence positions and relation kinds, and the missingness rule. Then construct the declaration with a reference to the completed basis. The expected basis has no back-reference to the declaration. This keeps the construction acyclic.

At least one of `selectedEvaluationPredicate` and `selectedComparatorSpecRef` is present. Both may be present. A label such as *review*, *quality*, or *current context* supplies neither. A.19 defines the predicate by value. For comparator admission, use A.19.CPM or the rule of the consumer that directly admits the comparator. Identify any actual comparison application separately. Selecting the predicate or comparator does not by itself establish the evaluation scope, evidence, time, Work, or result.

`evaluatorConditionRef` states only a condition that changes the evaluation question or admissibility of its result. `intendedEvaluatorSystemRef` is present only when the declared question depends on that exact intended System. Neither field establishes assignment or performance.

The actual evaluator System, every obtaining assignment, and dated evaluation Work belong to the separately identified evaluation application or result account. Keep any local evaluator system-role classification separate and route unresolved *role* wording through `E.10.ROLE`.

`evaluationPatternLocator` locates the pattern that defines or constrains the evaluation; it is not the Method, performer, Work, or result. Claim Method or MethodDescription identity only after A.3.1 and A.3.2 admit it. Characteristic-space, Q-Bundle, rubric, profile, evidence-basis, and result-form references identify separate descriptions.

None of these declaration fields is dated evaluation Work or an evaluation result. A pre-evaluation frame does not assert that the future assessment has occurred. It may reference independently obtaining Work as the checked object, consumer or prior basis, retaining that Work’s admission and temporal conditions. An ordinary result that asserts no actual Work needs no Work identifier.

If a compact projection does assert dated evaluation Work, recover every exact actual performer through A.13 and follow A.15.1 for independent Work admission. The performer, Method, time, containing System, Work identity, and the result relation remain recoverable. Add assignment and F.6 refs only when the projection or receiving use expressly represents precise assignment-bound attribution. Missing or failed F.6 alone leaves independently admitted Work intact. Recheck any admission premise invalidated by the same finding and its dependent conclusions under A.15.1.

Keep any durable result episteme, evidence use, provenance, currentness, viewpoint, grounding, and Work-to-result or decision-use relation under their own patterns. A frame, declaration, description, assignment, dashboard, or carrier establishes none of them.

Two carriers may publish the same edition of either episteme. A `QualityEvaluationUseDeclaration` changes edition when its object version, claim graph, reference scheme, question-changing evaluator condition or intended-evaluator identity, evaluation pattern, semantic Method, selected characteristic space, predicate and comparator, ClaimScope, qualification window, quality-model descriptions, expected evidence-basis edition, or result-form description changes. Replacing one qualified actual evaluator with another does not change the declaration unless the declared condition or claim changes.

An `ExpectedEvaluationEvidenceBasis@Context` changes edition when its object version, claim graph, reference scheme, evaluation pattern, selected space, predicate and comparator, ClaimScope, expected evidence positions or relation kinds, missingness rule, or qualification window changes. Carrier, context label, viewpoint, grounding record, or support serialization alone changes neither episteme.

The two local set names above require only their declared element ranges and ordinary extensional equality. Permuting a list or repeating an entry leaves its represented set unchanged. A changed question-frame edition changes the admissibility or use question, not the set identity when its members remain the same. A changed proposal episteme contributes a different member under C.2.1, even if its short label is retained. An episteme may describe or publish a set. Its record and carrier have their own identities. These set-valued uses require no additional public set kind.

#### E.22:4.2 - Quality evaluation purposes

| Purpose value | Use when | Expected result |
|---|---|---|
| `floorEvaluation` | The question is whether the object reaches a declared floor. | Values below floor, first repair, architecture hold, refresh, new-frame assignment, or admissible stop. |
| `exceptionalImprovementEvaluation` | The floor is reached and the requester wants non-dominated improvement toward exceptional expression. | Per-coordinate proposal or no-candidate disposition. |
| `paretoTradeoffEvaluation` | A candidate change may improve some values while worsening protected qualities. | Trade-off account and non-dominated comparison. |
| `candidateImprovementProposalEvaluation` | The requester needs candidate-change proposals before changing the object or generating variants. | Proposal row or bounded proposal portfolio with an expected effect on the later evaluation result. |
| `openQuestionDiscoveryEvaluation` | The requester wants important unasked questions surfaced. | Question classified as existing-coordinate issue, candidate future coordinate, or outside-evaluation issue. |
| `absorptionEvaluation` | Returned findings or suggestions have been applied or rejected. | Quality-impact account over the changed object. |

A request can combine purposes. The result distinguishes the answer to each one. A floor result does not answer exceptional improvement. Absorption count does not establish a changed evaluation result. A proposal is not a selected work item.

#### E.22:4.3 - Question frame

Use the construction in section 4.0 to settle the requested judgement before expressing these bindings. The schema preserves that question for its declared use.


An improvement aim is not a command to make every coordinate exceptional. Only the named evaluation can assign a `5`, after the changed object earns it.

The frame may ask for substantive non-dominated proposals that could move named coordinates toward exceptional expression, while admitting `no proposal` or `stay at current value` when every plausible change would add apparatus, proof prose, boundary catalogues, or process evidence while damaging protected qualities. Support that no-proposal result with the review locations checked and references to its evidence basis.

```text
QualityEvaluationQuestionFrame <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under evaluation
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: NonemptyClaimContent by value
  referenceScheme: EpistemeInterpretationScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration about the same object version
  selectedEvaluationCharacteristicSpaceRef: U.EntityRef, referencing the same U.CharacteristicSpace
  selectedEvaluationPredicate?: CharacteristicSpacePredicate by value
  selectedComparatorSpecRef?: ComparatorSpecRef
  evaluationClaimScopeRef: U.EntityRef, referencing the same U.ClaimScope
  resultConsumingUseRef: U.EntityRef, referencing one exact directly governed intended-work, dated-work, or decision object
  resultConsumingUseKindRef: U.KindRef, referencing its exact kind
  resultConsumingUseDescriptionRef: U.EpistemeRef, describing how that work or decision will use the evaluation result
  evaluationPurposeSelection: QualityEvaluationPurposeSelectionValue
  declaredQualityFloorDescriptionRef?: U.EpistemeRef, referencing one declared-quality-floor description
  desiredImprovementAimDescriptionRef?: U.EpistemeRef, referencing one desired-improvement-aim description
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  evaluationQualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
  nonUseBoundaryDescriptionRef?: U.EpistemeRef, referencing a non-use-boundary description only when the grounded condition in CC-E22-6 holds
```

The frame's exact object version, characteristic space, predicate/comparator binding, ClaimScope, and qualification window equal those of its use declaration and expected evidence basis. These bindings let another evaluator replay the question. The space, predicate, comparator, scope, method and consuming object retain their own identities. A changed binding creates a changed frame edition and requires a newly evaluated result.

`resultConsumingUseRef` is not a generic *use* placeholder. Before the intended work or decision occurs, the reference may resolve to one A.15.2 `U.WorkPlan` that names the intended Work, or to the decision question or decision-governing object under its directly governing pattern. It may resolve to `U.Work` only when that dated Work already obtains under A.15.1. The frame neither creates the consuming Work or decision nor authorizes it.

A minimal floor frame names the object version, one `QualityEvaluationUseDeclaration`, the exact selected characteristic space, applicable predicate and/or comparator, ClaimScope, result-consuming work or decision, purpose `floorEvaluation`, and the declared floor.

The declaration may cite defaults supplied by the governing evaluation pattern for its quality-model descriptions, evidence basis, result form, and qualification window, but defaults do not replace the exact selected space, criterion, scope, or consumer.

If the question depends on another edition, source state, comparison set, time window, or declared use, state that window explicitly. For one FPF pattern version under E.21, compactness never permits omitted coordinates, missing `ShortRationale`, absent `PrecisionRestorationProfile`, scope narrowing, or a blocker-only substitute result.

**Connect the question, grounds and supported conclusion.** State what the evaluation must establish about the object for the declared consuming use. In the expected evidence basis, identify the judgement that connects the selected criterion to the relevant content. For example, ask whether a Method's conditions permit the proposed action, whether a computation yields the stated result, or whether a source supports the claim made from it. A direct presence or identity check suffices when the question asks about that property.

When receiving the result, read its rationale and observations for that connection. Determine whether they support the requested conclusion under the declared criterion, scope and qualification. Retain supported findings. Identify which judgement or inference is missing before claiming more. Obtain that answer through the applicable evaluation, reusing current supported parts and keeping the answer in its existing result. Apply the same connection to an already-scoped direct evaluation. It needs no new `QualityEvaluationQuestionFrame`.

These instructions use the frame's existing `claimGraph`, the declaration's `expectedEvaluationEvidenceBasisRef` and the declared consuming use. The expected evidence basis describes what must be answered; the obtained grounds belong in the evaluation result.

For landing-input, corpus-facing, `Stable`, release, external-review or another stated use, evaluate the object under the scope for which the floor was requested. If another use is to be evaluated, open a new `QualityEvaluationQuestionFrame`. An easier scope cannot make the current request pass.

The frame and declaration state the evaluation's intended use. Naming an intended evaluator or planned condition establishes neither a current assignment nor Work. When dated evaluation Work is asserted, recover the exact evaluator through A.13 and use A.15.1 to admit the Work independently. Keep evidence use, typed result binding or direct result relation, and optional result episteme separate. Add F.6 only when the evaluation account expressly consumes precise assignment-bound attribution. An expected result-form description is not the result, and the consuming work or decision does not become current merely because the frame names it.

#### E.22:4.4 - Finding and proposal rows

An actionable finding identifies where an issue was observed, which exact entity would change, the affected evaluation characteristic or coordinate, the current evaluation result for that characteristic or coordinate when known, the proposed correction, and the closure test. A proposal adds a typed expected evaluation effect, protected trade-offs, and any outside claim. For each outside claim, include the subject-pattern locator needed for an independent check.

```text
CandidateImprovementProposalRow@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under improvement
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: NonemptyClaimContent by value
  referenceScheme: EpistemeInterpretationScheme by value
  editionId
  qualityEvaluationQuestionFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame about the same object version
  evaluationClaimScopeRef: U.EntityRef, referencing that frame's U.ClaimScope
  reviewLocationDescriptionRef: U.EpistemeRef, referencing one description of the observed location in the reviewed object
  correctionTargetRef: U.EntityRef, referencing the exact entity proposed to change
  correctionTargetKindRef: U.KindRef, referencing the exact kind of the correction target
  affectedEvaluationCharacteristicOrCoordinateRef: U.EntityRef, referencing one governed characteristic or evaluation coordinate
  affectedEvaluationCharacteristicOrCoordinateKindRef: U.KindRef, referencing its exact kind
  currentAffectedEvaluationResultRef?: U.EntityRef, referencing the current result value for that characteristic or coordinate
  currentAffectedEvaluationResultKindRef?: U.KindRef, referencing the exact kind of that result value
  expectedSubstantiveEvaluationEffect: ProposalEvaluationEffectValue
  proposedCorrectionDescriptionRef: U.EpistemeRef, referencing one correction description
  kindRestorationCheckDisposition: ProposalKindRestorationCheckDispositionValue
  kindRestorationCheckRef?: U.EpistemeRef, referencing one KindRestorationCheck result
  expectedTradeoffRefs[]: U.EpistemeRef, each referencing one expected-trade-off description
  outsideClaimReferences[]?: CandidateImprovementOutsideClaimReference@Context by value
  closureTestRef: U.EpistemeRef, referencing one closure-test description

CandidateImprovementOutsideClaimReference@Context in CandidateImprovementProposalRow@Context.claimGraph:
  outsideClaimOrBoundaryDescriptionRef: U.EpistemeRef, referencing one description of the outside claim or boundary
  outsideValueRef?: U.EntityRef, referencing the exact outside governed value
  outsideValueKindRef?: U.KindRef, referencing the exact kind of that outside value
  outsideRelationSignatureRef?: U.EntityRef, referencing the exact RelationSignature declaration episteme when its reusable declaration is used
  subjectPatternLocator: U.EntityRef, locating the exact FPF subject-pattern description; the evaluation claim separately cites the defining ClaimGraph
  reconsiderationConditionDescriptionRef: U.EpistemeRef, referencing one description of the condition that activates renewed use of that subject pattern
```

```text
ImprovementFollowUpHypothesis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version expected to change
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: NonemptyClaimContent by value
  referenceScheme: EpistemeInterpretationScheme by value
  editionId
  qualityEvaluationQuestionFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame about the same object version
  evaluationClaimScopeRef: U.EntityRef, referencing that frame's U.ClaimScope
  qualityReviewFindingDescriptionRef: U.EpistemeRef, referencing one episteme that describes the exact QualityReviewFindingRow
  proposedNextOperationDescriptionRef?: U.EpistemeRef, referencing one operation description
  proposedNextMethodRef?: U.MethodRef, referencing one U.Method
  expectedEvaluationEffectDescriptionRef: U.EpistemeRef, referencing one expected-evaluation-effect description
  testConditionDescriptionRef: U.EpistemeRef, referencing one test-condition description
```

Exactly one of `proposedNextOperationDescriptionRef` and `proposedNextMethodRef` is present. The question frame, proposal row, and follow-up hypothesis preserve the same object-version EntityOfConcern and ClaimScope unless a proposal explicitly opens a new frame for a different version or scope. `QualityEvaluationQuestionFrame` changes edition when the object version, use declaration, selected space, predicate/comparator binding, ClaimScope, consuming work or decision, purpose, floor or aim, trade-off set, qualification window, non-use boundary, claim graph, or reference scheme changes.

A proposal row changes edition when its frame, ClaimScope, correction target, affected evaluation coordinate, current result reference, proposed correction, expected effect, trade-offs, outside-claim nodes, closure test, claim graph, or reference scheme changes.

A follow-up hypothesis changes edition when its frame, ClaimScope, finding description, proposed operation or method, expected effect, test condition, claim graph, or reference scheme changes. Changing only a context label, carrier, viewpoint, grounding record or serialization leaves all three epistemes unchanged.

`ProposalEvaluationEffectValue` is the closed local value set `repairFloor | raiseTowardExceptional | preventProtectedQualityLoss | classifyOutsideEvaluation | preserveCurrentValue`. It identifies the broad type of substantive effect the proposal is expected to have on the evaluation. E.23 gives a separate coordinate-qualified prediction in `ExpectedEvaluationResultChange@Context`. Neither prediction asserts that the result has changed.

`ProposalKindRestorationCheckDispositionValue` is `triggered | notTriggered | ordinaryProse | alreadySatisfied | blocker`. The `triggered` and `blocker` states include `kindRestorationCheckRef`; the other values leave it absent.

Current affected-evaluation result ref and kind are both present or both absent. When present, the exact result resolves through the direct evaluation pattern's typed result relation or A.6.1 application binding, and any durable result episteme remains separately governed. The proposal row neither produces nor reidentifies that result. The exact kind recovers whether the named evaluation returned a scale value, status, or another admitted result for that characteristic or coordinate.

Outside value ref and kind are paired. When the outside value is a relation, recover its direct predicate, participants and applicability from the subject pattern. Add `outsideRelationSignatureRef` only when the proposal uses that reusable declaration. The relation occurrence and declaration remain distinct under A.6.REL.

`CandidateImprovementOutsideClaimReference@Context` is a bounded local ClaimGraph node form, not a U-kind, episteme, relation, or relation-reference episteme. It is constructed inside one proposal row without a back-reference to that row. Its node identity is determined by the containing proposal edition and ClaimGraph position.

`reviewLocationDescriptionRef` describes where the issue was observed in the reviewed object. `correctionTargetRef` identifies the exact entity that would change. Keep the observed location distinct from the correction target even when both concern the same object. The row is a faithful typed proposal form of `QualityReviewFindingRow` and one possible member of a `CandidateImprovementProposalPortfolio@Context` set. It describes a proposal. Selection, planning, performed Work, actual Transformation, result binding and proof of improvement each need their own grounds.

For wording, naming, and precision-restoration proposals, `proposedCorrectionDescriptionRef` states the correction and its intended content effect. Apply `F.19` for the ordinary repair and local revalidation. When the changed FPF-governed expression can alter meaning, `KindRestorationCheck` states the live object, kind, relation, slot or use position, claim kind, admissible use, and scope before and after the change. If the proposed repair cannot preserve those values and no accepted decision justifies changing them, the proposal row remains blocking.

#### E.22:4.5 - Absorption impact values

| Absorption impact | Meaning |
|---|---|
| `coordinateImproved` | A named coordinate or status has stronger content evidence after the change. |
| `floorOnlyClosure` | A below-floor defect was repaired enough for the floor but not exceptional expression. |
| `unchangedBecauseAlreadySatisfied` | The suggestion was already satisfied. Name the review locations and the evaluation property they already satisfy. |
| `tradeoffIntroduced` | A repair raised one property and damaged another. |
| `qualityLossDetected` | The applied or proposed change lowers a value or protected quality. |
| `outsideObjectUnderImprovementEvaluation` | The suggestion belongs under another exact evaluation or pattern. |
| `notAdmissibleForDeclaredUse` | The suggestion is rejected for the declared purpose and boundary. |

In the absorption result, state how the object’s quality changed or why it remained the same, using the evaluation of that object. Counting accepted rows does not establish that result.

#### E.22:4.6 - OEE and NQD proposal portfolios

When the object is a candidate, archive or front member, selected set, parity report, refresh report, or declared transformation result, use `E.22` to frame the quality question and return proposal rows. Use `C.17` for candidate characteristics, `C.18` for archive and front relations, `C.19` for pool policy, `G.5` for selected-set result declaration, `G.9` for parity, and `G.11` for currentness and refresh. When the question concerns availability to an audience, use `E.17` for the source-backed publication face and return to source. Use `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use and availability.


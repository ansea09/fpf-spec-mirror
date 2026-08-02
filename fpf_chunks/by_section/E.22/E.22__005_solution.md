---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__005_solution.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:4 — Solution"
line_start: 86222
line_end: 86434
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

`E.22` gives one compact declaration for improvement-oriented quality evaluation questions. It keeps the question from replacing the evaluation and keeps the evaluation result from becoming a decision or work product beyond its authority.

#### E.22:4.1 - Local names and kind settlement

The framing episteme, evaluation method, descriptions used by that method, performer assignment, dated evaluation Work, actual operation application, evidence use, and result occupy different positions. `QualityEvaluationUseDeclaration` keeps the intended evaluation bindings together without collapsing those kinds.

The remaining local support names ending in `@Context` are compatibility and retrieval names only. The suffix supplies no context entity, scope, participant, relation, or identity component; every episteme follows C.2.1 identity, every set is identified by its stated extensional rule, and every neighboring Work, decision, evidence, viewpoint, grounding, or result relation remains under its direct governor.

| Local name | Kind and role |
|---|---|
| `QualityEvaluationQuestionFrame` | `U.Episteme` whose EntityOfConcern is the exact object version under evaluation; its ClaimGraph carries the requested quality-evaluation question about that version and its exact use bindings. |
| `QualityEvaluationUseDeclaration` | `U.Episteme` whose EntityOfConcern is the same exact object version. It describes how evaluation of that version is intended to be performed and interpreted, referring separately to performer assignment, governing evaluation pattern, optional semantic method, selected characteristic space, predicate/comparator binding, ClaimScope, quality-model descriptions, expected evidence basis, result form, and qualification window. |
| `ObjectVersionUnderQualityEvaluation` | Exact `U.Entity` version being evaluated, paired with its exact `U.Kind`. |
| `EvaluationCharacteristicSpaceSelection` | One exact `U.CharacteristicSpace` selected for this evaluation use. Its specification description is a separate episteme and does not become the space. |
| `EvaluationCriterionSelection` | The exact by-value `CharacteristicSpacePredicate`, exact admitted `ComparatorSpecRef`, or both, required by the governing evaluation pattern and, when declared, its separately identified semantic evaluation Method. At least one is present. |
| `EvaluationClaimScope` | One exact set-valued `U.ClaimScope` governing the evaluation claim. It is not a context label, selected structure, window, or evidence set. |
| `QualityEvaluationResultConsumingUse` | The exact directly governed intended-work, dated-work, or decision object that is expected to consume the evaluation result, paired with its exact kind and use description. It does not authorize or perform that use. |
| `QualityEvaluationPurposeSelection` | Requested evaluation purpose or distinguishable combination of purposes. |
| `DeclaredQualityFloor` | Minimum acceptable coordinate or status floor when the frame declares a floor claim. |
| `DesiredImprovementAim` | Requested substantive change beyond the floor when improvement beyond the floor is requested. |
| `ExpectedEvaluationEvidenceBasis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version under evaluation. It describes expected evidence-use positions and the missingness rule for the exact method, space, criterion, scope, and qualification window. It can be identified before a use declaration cites it and is not the evidence values later found. |
| `TradeoffProtectionSet@Context` | A local `U.Set` value whose members are exact characteristic or coordinate references paired with their kinds. Its identity is extensional for the exact question-frame edition, not for a context label. |
| `EvaluationQualificationWindow` | Edition, source-currentness, comparison-set, time, or declared-use window in which the requested result is intended to be current. The actual evaluation application later binds its exact point or interval. |
| `ExpectedQualityEvaluationResultFormDescription` | `U.Episteme` describing the result-row form declared by the governing evaluation pattern. It is not an actual result. |
| `QualityReviewFindingRow` | Actionable evaluation finding that identifies the observed issue, affected evaluation property, correction direction, and closure test. |
| `CandidateImprovementProposalRow@Context` | E.22 proposal episteme with an exact correction target, expected substantive evaluation effect, trade-offs, kind-restoration disposition, outside-claim return when needed, and closure test. |
| `CandidateImprovementOutsideClaimReference@Context` | Bounded local ClaimGraph node form inside one proposal row. It identifies the outside governed value, relation signature, or boundary description and the exact FPF pattern identity that governs the return. It is not an episteme, relation, or independently referenceable entity. |
| `KindRestorationCheck` | Conditionally present check when a finding or proposal changes wording, naming, or precision-restoration content. |
| `CandidateImprovementProposalPortfolio@Context` | A local `U.Set` value whose members are `CandidateImprovementProposalRow@Context` epistemes for one question frame. Membership, not a document serialization, determines the portfolio. |
| `ImprovementFollowUpHypothesis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version expected to change. It claims that one named next operation or method application is expected to address one finding and produce a stated evaluation effect under a stated test condition. A stop disposition, return, selected plan, performed Work, or actual Transformation is not such a hypothesis. |

```text
QualityEvaluationUseDeclaration <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under evaluation
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  evaluationPerformerRoleAssignmentRef?: U.EntityRef, referencing one U.RoleAssignment
  governingEvaluationPatternDescriptionRef: U.EntityRef, referencing the exact FPF evaluation pattern identity supplied by its pattern/framework owner
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
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  governingEvaluationPatternDescriptionRef: U.EntityRef, referencing the same exact FPF evaluation pattern identity
  selectedEvaluationCharacteristicSpaceRef: U.EntityRef, referencing the same exact U.CharacteristicSpace
  selectedEvaluationPredicate?: CharacteristicSpacePredicate by value
  selectedComparatorSpecRef?: ComparatorSpecRef
  evaluationClaimScopeRef: U.EntityRef, referencing the same exact U.ClaimScope
  expectedEvidencePositionDescriptionRefs[1..*]: U.EpistemeRef, each referencing one evidence-position description
  expectedEvidenceRelationKindRefs[1..*]: U.KindRef, each referencing one expected evidence-relation kind
  missingEvidenceDispositionRuleRef: U.EpistemeRef, referencing one exact episteme that states the missing-evidence disposition rule under its direct owner
  qualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
```

Every field above with a `*Ref` suffix stores the stated A.6.5 `RefKind`; resolving it yields the referent kind named after `referencing`. The use declaration and expected evidence basis carry the same exact object version, governing evaluation pattern, selected characteristic space, criterion binding, ClaimScope, and qualification window. The expected basis does not point back to the declaration: it can be constituted from those exact values, expected evidence positions and relation kinds, and missingness rule; the declaration is then constituted with a reference to that completed basis. This preserves the former acyclic construction.

At least one of `selectedEvaluationPredicate` and `selectedComparatorSpecRef` is present; both may be present. A label such as *review*, *quality*, or *current context* supplies neither. A.19 owns the predicate by value. A.19.CPM or the exact direct consumer owns comparator admission and any actual comparison application. Neither the predicate nor comparator owns evaluation scope, evidence, time, Work, or result.

`evaluationPerformerRoleAssignmentRef` identifies who is assigned to perform the evaluation; it is neither the semantic Method nor the object being evaluated. `governingEvaluationPatternDescriptionRef` identifies the exact FPF pattern identity that owns the evaluation, without establishing `U.MethodDescription` membership; its stable `DescriptionRef` suffix does not change the referent kind. `semanticEvaluationMethodRef`, when recoverable, identifies the separately admitted Method used for the evaluation. Any episteme claimed to describe that Method remains a separate object and requires an independent A.3.2 membership result. The characteristic-space, Q-Bundle, rubric, review-profile, evidence-basis, and result-form references identify separate epistemes that specify the quality model or its use; they do not supply an actor and do not become alternative values of the pattern or method slots.

None of these declaration fields is dated evaluation Work or an evaluation result. When evaluation is performed, A.15.1 identifies one dated `U.Work` and its direct method-enactment relation. The direct evaluation pattern owns the exact evaluation and typed result; when it exposes a reusable operation, A.6.1 separately identifies the actual application and result binding. A durable result episteme, when needed, remains under C.2.1. Actual evidence use, provenance, currentness, viewpoint selection, empirical grounding, and any work-to-result or decision-use relation remain separate under their direct governors. A frame, declaration, description, role assignment, dashboard, or carrier establishes none of those occurrences.

Two carriers may publish the same edition of either episteme. A `QualityEvaluationUseDeclaration` changes edition when its exact object version, claim graph, reference scheme, performer assignment, governing evaluation pattern, semantic method, selected characteristic space, predicate/comparator binding, ClaimScope, qualification window, quality-model descriptions, expected evidence-basis edition, or result-form description changes. An `ExpectedEvaluationEvidenceBasis@Context` changes edition when its object version, claim graph, reference scheme, governing evaluation pattern, selected space, predicate/comparator binding, ClaimScope, expected evidence positions or relation kinds, missingness rule, or qualification window changes. Carrier, context label, viewpoint, grounding record, or support serialization alone changes neither episteme. `TradeoffProtectionSet@Context` and `CandidateImprovementProposalPortfolio@Context` are set values, not records; an episteme may describe or publish either set without becoming the set.

#### E.22:4.2 - Quality evaluation purposes

| Purpose value | Use when | Expected result |
|---|---|---|
| `floorEvaluation` | The question is whether the object reaches a declared floor. | Values below floor, first repair, architecture hold, refresh, new-frame assignment, or admissible stop. |
| `exceptionalImprovementEvaluation` | The floor is reached and the requester wants non-dominated improvement toward exceptional expression. | Per-coordinate proposal or no-candidate disposition. |
| `paretoTradeoffEvaluation` | A candidate change may improve some values while worsening protected qualities. | Trade-off account and non-dominated comparison. |
| `candidateImprovementProposalEvaluation` | The requester needs candidate-change proposals before changing the object or generating variants. | Proposal row or bounded proposal portfolio with an expected effect on the later evaluation result. |
| `openQuestionDiscoveryEvaluation` | The requester wants important unasked questions surfaced. | Question classified as existing-coordinate issue, candidate future coordinate, or outside-evaluation issue. |
| `absorptionEvaluation` | Returned findings or suggestions have been applied or rejected. | Quality-impact account over the changed object. |

Purposes can be combined, but the result keeps them distinguishable. A floor result does not answer exceptional improvement. Absorption count does not establish a changed evaluation result. A proposal is not a selected work item.

#### E.22:4.3 - Question frame

An improvement aim is not a command to make every coordinate exceptional. A `5` is assigned only by the named evaluation after the changed object earns it. The frame may ask for substantive non-dominated proposals that could move named coordinates toward exceptional expression, while admitting `no proposal` or `stay at current value` when every plausible change would add apparatus, proof prose, boundary catalogues, or process evidence while damaging protected qualities. That no-proposal result needs checked review locations and evidence-basis references; it is not a cheap refusal to improve.

```text
QualityEvaluationQuestionFrame <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under evaluation
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration about the same object version
  selectedEvaluationCharacteristicSpaceRef: U.EntityRef, referencing the same exact U.CharacteristicSpace
  selectedEvaluationPredicate?: CharacteristicSpacePredicate by value
  selectedComparatorSpecRef?: ComparatorSpecRef
  evaluationClaimScopeRef: U.EntityRef, referencing the same exact U.ClaimScope
  resultConsumingUseRef: U.EntityRef, referencing one exact directly governed intended-work, dated-work, or decision object
  resultConsumingUseKindRef: U.KindRef, referencing its exact kind
  resultConsumingUseDescriptionRef: U.EpistemeRef, describing how that work or decision will use the evaluation result
  evaluationPurposeSelection: QualityEvaluationPurposeSelectionValue
  declaredQualityFloorDescriptionRef?: U.EpistemeRef, referencing one declared-quality-floor description
  desiredImprovementAimDescriptionRef?: U.EpistemeRef, referencing one desired-improvement-aim description
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  evaluationQualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
  nonUseBoundaryDescriptionRef: U.EpistemeRef, referencing one non-use-boundary description
```

The frame's exact object version, characteristic space, predicate/comparator binding, ClaimScope, and qualification window equal those of its use declaration and expected evidence basis. These bindings make the question replayable; they do not reidentify the space, predicate, comparator, scope, method, or consuming object. A changed binding creates a changed frame edition and requires a newly evaluated result.

`resultConsumingUseRef` is not a generic *use* placeholder. Before occurrence it may resolve to one A.15.2 `U.WorkPlan` that names the particular intended Work, or to the exact decision question or decision-governing object under its direct pattern. It may resolve to `U.Work` only when that dated Work already obtains under A.15.1. The frame neither creates the consuming Work or decision nor authorizes it.

The shortest floor frame names the object version, one `QualityEvaluationUseDeclaration`, the exact selected characteristic space, applicable predicate and/or comparator, ClaimScope, result-consuming work or decision, purpose `floorEvaluation`, and the declared floor. The declaration may cite defaults supplied by the governing evaluation pattern for its quality-model descriptions, evidence basis, result form, and qualification window, but defaults do not replace the exact selected space, criterion, scope, or consumer. If the question depends on another edition, source state, comparison set, time window, or declared use, state that window explicitly. For one FPF pattern version under E.21, compactness never permits omitted coordinates, missing `ShortRationale`, absent `PrecisionRestorationProfile`, scope narrowing, or a blocker-only substitute result.

The frame does not authorize post-hoc scope replacement. If the requested floor is landing-input, corpus-facing, `Stable`, release, external-review, or another stated use, the evaluator measures that use. If a different use becomes interesting, open a new `QualityEvaluationQuestionFrame`; do not report the current request as passed under an easier scope.

The frame and declaration perform no evaluation. A dated evaluation Work occurrence, its method enactment, any actual operation application, actual evidence use, typed result binding or direct result relation, and optional result episteme remain separate. An expected result-form description is not the result, and the consuming work or decision does not become current merely because the frame names it.

#### E.22:4.4 - Finding and proposal rows

An actionable finding first identifies where an issue was observed, which exact entity would change, the affected evaluation characteristic or coordinate, the current evaluation result for that characteristic or coordinate when known, the proposed correction, and the closure test. A proposal adds a typed expected evaluation effect, protected trade-offs, and any outside claim together with its return to the direct governing pattern.

```text
CandidateImprovementProposalRow@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under improvement
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationQuestionFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame about the same object version
  evaluationClaimScopeRef: U.EntityRef, referencing that frame's exact U.ClaimScope
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
  outsideRelationSignatureRef?: U.EntityRef, referencing the exact U.Signature of the outside relation
  directGoverningPatternRef: U.EntityRef, referencing the exact FPF governing-pattern identity supplied by its pattern/framework owner
  returnConditionDescriptionRef: U.EpistemeRef, referencing one description of the condition for returning to that governing pattern
```

```text
ImprovementFollowUpHypothesis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version expected to change
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationQuestionFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame about the same object version
  evaluationClaimScopeRef: U.EntityRef, referencing that frame's exact U.ClaimScope
  qualityReviewFindingDescriptionRef: U.EpistemeRef, referencing one episteme that describes the exact QualityReviewFindingRow
  proposedNextOperationDescriptionRef?: U.EpistemeRef, referencing one operation description
  proposedNextMethodRef?: U.MethodRef, referencing one U.Method
  expectedEvaluationEffectDescriptionRef: U.EpistemeRef, referencing one expected-evaluation-effect description
  testConditionDescriptionRef: U.EpistemeRef, referencing one test-condition description
```

Exactly one of `proposedNextOperationDescriptionRef` and `proposedNextMethodRef` is present. The question frame, proposal row, and follow-up hypothesis preserve the same exact object-version EntityOfConcern and ClaimScope unless a proposal explicitly opens a new frame for a different version or scope. `QualityEvaluationQuestionFrame` changes edition when the object version, use declaration, selected space, predicate/comparator binding, ClaimScope, consuming work or decision, purpose, floor or aim, trade-off set, qualification window, non-use boundary, claim graph, or reference scheme changes. A proposal row changes edition when its frame, ClaimScope, correction target, affected evaluation coordinate, current result reference, proposed correction, expected effect, trade-offs, outside-claim nodes, closure test, claim graph, or reference scheme changes. A follow-up hypothesis changes edition when its frame, ClaimScope, finding description, proposed operation or method, expected effect, test condition, claim graph, or reference scheme changes. A context label, carrier, viewpoint, grounding record, or serialization change alone changes none of these epistemes.

`ProposalEvaluationEffectValue` is the closed local value set `repairFloor | raiseTowardExceptional | preventProtectedQualityLoss | classifyOutsideEvaluation | preserveCurrentValue`. It identifies the coarse substantive evaluation effect expected from this proposal. It does not duplicate the coordinate-qualified prediction later carried by E.23 `ExpectedEvaluationResultChange@Context` and does not assert an actual changed result.

`ProposalKindRestorationCheckDispositionValue` is `triggered | notTriggered | ordinaryProse | alreadySatisfied | blocker`. The `triggered` and `blocker` states include `kindRestorationCheckRef`; the other values leave it absent. Current affected-evaluation result ref and kind are both present or both absent; when present, the exact result resolves through the direct evaluation pattern's typed result relation or A.6.1 application binding, and any durable result episteme remains separately governed. The proposal row neither produces nor reidentifies that result. The exact kind recovers whether the named evaluation returned a scale value, status, or another admitted result for that characteristic or coordinate. Outside value ref and kind are paired, and `outsideRelationSignatureRef` is present when the outside value is a relation. `CandidateImprovementOutsideClaimReference@Context` is a bounded local ClaimGraph node form, not a U-kind, episteme, relation, or relation-reference episteme. It is constructed inside one proposal row without a back-reference to that row; its node identity is determined by the containing proposal edition and ClaimGraph position.

`reviewLocationDescriptionRef` describes where the issue was observed in the reviewed object. `correctionTargetRef` identifies the exact entity that would change. They are not interchangeable positions. The row is a faithful typed proposal form of `QualityReviewFindingRow` and one possible member of a `CandidateImprovementProposalPortfolio@Context` set. It remains a proposal episteme, not a selected repair, plan, work occurrence, actual Transformation, result binding, or proof of improvement.

For wording, naming, and precision-restoration proposals, `proposedCorrectionDescriptionRef` does more than say "replace X with Y". It states the recovered object kind, relation, slot or use position when current, admissible use, and scope before and after the change. If no kind-preserving repair is recoverable, the row remains blocking.

#### E.22:4.5 - Absorption impact values

| Absorption impact | Meaning |
|---|---|
| `coordinateImproved` | A named coordinate or status has stronger content evidence after the change. |
| `floorOnlyClosure` | A below-floor defect was repaired enough for the floor but not exceptional expression. |
| `unchangedBecauseAlreadySatisfied` | The suggestion was already satisfied by value, with the exact review locations and the evaluation property they already satisfy named by value. |
| `tradeoffIntroduced` | A repair raised one property and damaged another. |
| `qualityLossDetected` | The applied or proposed change lowers a value or protected quality. |
| `outsideObjectUnderImprovementEvaluation` | The suggestion belongs under another exact evaluation or pattern. |
| `notAdmissibleForDeclaredUse` | The suggestion is rejected for the declared purpose and boundary. |

The absorption result states the changed evaluation result under the object-under-improvement evaluation, not a count of accepted rows.

#### E.22:4.6 - OEE and NQD proposal portfolios

When the object is a candidate, archive or front member, selected set, parity report, refresh report, or declared transformation result, `E.22` can frame the quality question and return proposal rows. `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` keep authority over candidate characteristics, archive and front semantics, pool policy, selected-set publication, parity, and refresh.


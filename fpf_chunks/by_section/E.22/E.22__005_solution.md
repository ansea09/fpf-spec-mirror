---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__005_solution.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:4 — Solution"
line_start: 84355
line_end: 84546
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

The evaluation method and the descriptions it uses occupy different positions. `QualityEvaluationUseDeclaration@Context` keeps those positions together for one intended evaluation without collapsing their kinds.

| Local name | Kind and role |
|---|---|
| `QualityEvaluationQuestionFrame@Context` | `U.Episteme` whose EntityOfConcern is the exact object version under evaluation; its ClaimGraph carries the requested quality-evaluation question about that version. |
| `QualityEvaluationUseDeclaration@Context` | `U.Episteme` whose EntityOfConcern is the same exact object version. It describes how evaluation of that version is to be performed and interpreted, referring separately to the performer assignment, governing pattern description, optional semantic method, quality-model descriptions, expected evidence basis, and result form. |
| `ObjectVersionUnderQualityEvaluation` | Exact `U.Entity` version being evaluated, paired with its exact `U.Kind`. |
| `QualityEvaluationPurposeSelection` | Requested evaluation purpose or distinguishable combination of purposes. |
| `DeclaredQualityFloor` | Minimum acceptable coordinate or status floor when the frame declares a floor claim. |
| `DesiredImprovementAim` | Requested substantive change beyond the floor when improvement beyond the floor is requested. |
| `ExpectedEvaluationEvidenceBasis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version under evaluation. It describes the evidence-use positions and missingness rule expected when the named governing evaluation pattern evaluates that version in the stated qualification window. It can be identified before a use declaration cites it and is not the evidence values later found. |
| `TradeoffProtectionSet@Context` | A local `U.Set` value whose members are exact characteristic or coordinate references paired with their kinds. Its identity is extensional within the question context. |
| `EvaluationQualificationWindow` | Edition, source-currentness, comparison-set, time, or declared-use window in which the requested result is intended to be current. |
| `ExpectedQualityEvaluationResultFormDescription` | `U.Episteme` describing the result-row form declared by the governing evaluation pattern. |
| `QualityReviewFindingRow` | Actionable evaluation finding that identifies the observed issue, affected evaluation property, correction direction, and closure test. |
| `CandidateImprovementProposalRow@Context` | E.22 proposal episteme with an exact correction target, expected substantive evaluation effect, trade-offs, kind-restoration disposition, outside-claim return when needed, and closure test. |
| `CandidateImprovementOutsideClaimReference@Context` | Bounded local ClaimGraph node form inside one proposal row. It identifies the outside governed value, relation signature, or boundary description and the exact method description that governs the return. It is not an episteme, relation, or independently referenceable entity. |
| `KindRestorationCheck` | Conditionally present check when a finding or proposal changes wording, naming, or precision-restoration content. |
| `CandidateImprovementProposalPortfolio@Context` | A local `U.Set` value whose members are `CandidateImprovementProposalRow@Context` epistemes for one question frame. Membership, not a document serialization, determines the portfolio. |
| `ImprovementFollowUpHypothesis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version expected to change. It claims that one named next operation or method application is expected to address one finding and produce a stated evaluation effect under a stated test condition. A stop disposition, return, or selected plan is not such a hypothesis. |

```text
QualityEvaluationUseDeclaration@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under evaluation
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  evaluationPerformerRoleAssignmentRef?: U.EntityRef, referencing one U.RoleAssignment
  governingEvaluationPatternDescriptionRef: U.EntityRef, referencing one U.MethodDescription
  semanticEvaluationMethodRef?: U.MethodRef, referencing the U.Method described by the governing pattern
  evaluationCharacteristicSpaceSpecDescriptionRef?: U.EpistemeRef, referencing one A.19.ECS specification description
  evaluationQBundleDescriptionRef?: U.EpistemeRef, referencing one C.25 Q-Bundle description
  evaluationRubricDescriptionRef?: U.EpistemeRef, referencing one evaluation-rubric description
  evaluationReviewProfileDescriptionRef?: U.EpistemeRef, referencing one evaluation-review-profile description
  expectedEvaluationEvidenceBasisRef: U.EpistemeRef, referencing one ExpectedEvaluationEvidenceBasis@Context
  expectedEvaluationResultFormDescriptionRef: U.EpistemeRef, referencing one ExpectedQualityEvaluationResultFormDescription

ExpectedEvaluationEvidenceBasis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version whose evaluation needs the expected evidence
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  governingEvaluationPatternDescriptionRef: U.EntityRef, referencing one U.MethodDescription
  expectedEvidencePositionDescriptionRefs[1..*]: U.EpistemeRef, each referencing one evidence-position description
  expectedEvidenceRelationKindRefs[1..*]: U.KindRef, each referencing one expected evidence-relation kind
  missingEvidenceDispositionRuleRef: U.EpistemeRef, referencing one U.MethodDescription that states the missing-evidence disposition rule
  qualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
```

Every field above with a `*Ref` suffix stores the stated A.6.5 `RefKind`; resolving it yields the referent kind named after `referencing`. The use declaration and expected evidence basis carry the same exact object-version value in `entityOfConcernRef`. The expected basis does not point back to the declaration: it can be created from the object version, governing evaluation-pattern description, expected evidence positions and relation kinds, missingness rule, and qualification window; the declaration is then created with a reference to that completed basis. This construction removes the former mutual dependency.

`evaluationPerformerRoleAssignmentRef` identifies who is assigned to perform the evaluation; it is neither the method nor the object being evaluated. `governingEvaluationPatternDescriptionRef` identifies the FPF pattern or other method description that governs the evaluation. `semanticEvaluationMethodRef`, when recoverable, identifies the method described by that pattern. The characteristic-space, Q-Bundle, rubric, and review-profile references identify epistemes that specify the quality model or its use; they do not supply an actor and do not become alternative values of a method slot.

Two carriers may publish the same edition of either episteme. A `QualityEvaluationUseDeclaration@Context` changes edition when its exact object version, bounded context, applicable grounding or viewpoint, claim graph, reference scheme, performer assignment, governing pattern description, semantic method, quality-model descriptions, expected evidence-basis edition, or result-form description changes. An `ExpectedEvaluationEvidenceBasis@Context` changes edition when its object version, bounded context, applicable grounding or viewpoint, governing pattern description, expected evidence positions or relation kinds, missingness rule, qualification window, claim graph, or reference scheme changes. Carrier or support serialization alone changes neither episteme. `TradeoffProtectionSet@Context` and `CandidateImprovementProposalPortfolio@Context` are set values, not records; an episteme may describe or publish either set without becoming the set.

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
QualityEvaluationQuestionFrame@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under evaluation
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration@Context about the same object version
  evaluationPurposeSelection: QualityEvaluationPurposeSelectionValue
  declaredQualityFloorDescriptionRef?: U.EpistemeRef, referencing one declared-quality-floor description
  desiredImprovementAimDescriptionRef?: U.EpistemeRef, referencing one desired-improvement-aim description
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  evaluationQualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
  nonUseBoundaryDescriptionRef: U.EpistemeRef, referencing one non-use-boundary description
```
The shortest floor frame names the object version, one `QualityEvaluationUseDeclaration@Context`, purpose `floorEvaluation`, and the declared floor. The declaration may cite defaults supplied by the governing evaluation pattern for its characteristic space, evidence basis, result form, and qualification window. If the question depends on another edition, source state, comparison set, time window, or declared use, state that window explicitly. For one FPF pattern version under E.21, compactness never permits omitted coordinates, missing `ShortRationale`, absent `PrecisionRestorationProfile`, scope narrowing, or a blocker-only substitute result.

The frame does not authorize post-hoc scope replacement. If the requested floor is landing-input, corpus-facing, `Stable`, release, external-review, or another stated use, the evaluator measures that use. If a different use becomes interesting, open a new `QualityEvaluationQuestionFrame@Context`; do not report the current request as passed under an easier scope.

#### E.22:4.4 - Finding and proposal rows

An actionable finding first identifies where an issue was observed, which exact entity would change, the affected evaluation characteristic or coordinate, the current evaluation result for that characteristic or coordinate when known, the proposed correction, and the closure test. A proposal adds a typed expected evaluation effect, protected trade-offs, and any outside claim together with its return to the direct governing pattern.

```text
CandidateImprovementProposalRow@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under improvement
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationQuestionFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame@Context about the same object version
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
  directGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  returnConditionDescriptionRef: U.EpistemeRef, referencing one description of the condition for returning to that governing pattern
```

```text
ImprovementFollowUpHypothesis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version expected to change
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationQuestionFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame@Context about the same object version
  qualityReviewFindingDescriptionRef: U.EpistemeRef, referencing one episteme that describes the exact QualityReviewFindingRow
  proposedNextOperationDescriptionRef?: U.EpistemeRef, referencing one operation description
  proposedNextMethodRef?: U.MethodRef, referencing one U.Method
  expectedEvaluationEffectDescriptionRef: U.EpistemeRef, referencing one expected-evaluation-effect description
  testConditionDescriptionRef: U.EpistemeRef, referencing one test-condition description
```

Exactly one of `proposedNextOperationDescriptionRef` and `proposedNextMethodRef` is present. The question frame, proposal row, and follow-up hypothesis preserve the same exact object-version EntityOfConcern unless a proposal explicitly opens a new frame for a different version. `QualityEvaluationQuestionFrame@Context` changes edition when the object version, bounded context, applicable grounding or viewpoint, use declaration, purpose, floor or aim, trade-off set, qualification window, non-use boundary, claim graph, or reference scheme changes. A proposal row changes edition when its bounded context, applicable grounding or viewpoint, frame, correction target, affected evaluation coordinate, proposed correction, expected effect, trade-offs, outside-claim nodes, closure test, claim graph, or reference scheme changes. A follow-up hypothesis changes edition when its bounded context, applicable grounding or viewpoint, frame, finding description, proposed operation or method, expected effect, test condition, claim graph, or reference scheme changes. Carrier and serialization changes alone do not change any of these epistemes.

`ProposalEvaluationEffectValue` is the closed local value set `repairFloor | raiseTowardExceptional | preventProtectedQualityLoss | classifyOutsideEvaluation | preserveCurrentValue`. It identifies the coarse substantive evaluation effect expected from this proposal. It does not duplicate the coordinate-qualified prediction later carried by E.23 `ExpectedEvaluationResultChange@Context`.

`ProposalKindRestorationCheckDispositionValue` is `triggered | notTriggered | ordinaryProse | alreadySatisfied | blocker`. The `triggered` and `blocker` states include `kindRestorationCheckRef`; the other values leave it absent. Current affected-evaluation result ref and kind are both present or both absent; the exact kind recovers whether the named evaluation returned a scale value, status, or another admitted result for that characteristic or coordinate. Outside value ref and kind are paired, and `outsideRelationSignatureRef` is present when the outside value is a relation. `CandidateImprovementOutsideClaimReference@Context` is a bounded local ClaimGraph node form, not a U-kind, episteme, relation, or relation-reference episteme. It is constructed inside one proposal row without a back-reference to that row; its node identity is determined by the containing proposal edition and ClaimGraph position.

`reviewLocationDescriptionRef` describes where the issue was observed in the reviewed object. `correctionTargetRef` identifies the exact entity that would change. They are not interchangeable positions. The row is a faithful typed proposal form of `QualityReviewFindingRow` and one possible member of a `CandidateImprovementProposalPortfolio@Context` set. It remains a proposal episteme, not a selected repair, plan, work occurrence, or proof of improvement.

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


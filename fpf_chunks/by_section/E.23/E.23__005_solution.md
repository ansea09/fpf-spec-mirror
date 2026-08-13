---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__005_solution.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:4 — Solution"
line_start: 88328
line_end: 88589
dependencies:
  - "A.19.ECS"
  - "A.22.CGUS"
  - "C.17-C.19"
  - "C.32.P2S"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:4 - Solution

`E.23` guides repeated improvement of one object version under a current `QualityEvaluationQuestionFrame` and `QualityEvaluationUseDeclaration`. The evaluation pattern defines the evaluation; restoration and subject patterns supply the relevant rules or guidance. A pattern body or locator does not by itself establish a semantic `U.Method` or qualify as its description. Claim Method or MethodDescription identity only after A.3.1 and A.3.2 admit it.

When an evaluation or improvement pass is claimed as actual `U.Work`, name that Work occurrence and keep all facts required by A.15.1, A.2.1, and F.6 recoverable. A local system-role kind and a separate System-classification judgment remain independent neighboring facts. A proposed pass, intended performer, planned assignment condition, or A.15.2 WorkPlan remains modal until its predicates obtain. A compact loop record may omit only an assignment identifier unused by the receiving claim.

Keep a returned value, durable result episteme, changed object, and actual Transformation separate. Connect a returned value through its A.6.1 binding or the evaluation's direct result relation. Connect Work to a result or change only through a declared direct relation or local claim that actually obtains; otherwise return the missing governor.

The repeated organization changes the object, re-evaluates the changed version through the same declared method and quality model, checks trade-offs and cost, and exposes admissible stop, continue, switch, new-frame, information-hold, branch, and subject-pattern-return continuations. That organization is one current A.22 constraint-governed unfolding structure; use E.18 only when an independently selected transformation-flow structure is actually the EntityOfConcern. Neither the method, record, visible cycle, nor selected continuation is an enduring Work occurrence or context container.

#### E.23:4.1 - Local names and kind settlement
Source and practitioner phrases such as "loop engineering", "agent loop", "harness loop", "prompt loop", and "workflow hardening loop" are entry phrases. Lower them into `ObjectUnderImprovementRef`, `QualityEvaluationQuestionFrame`, `QualityEvaluationUseDeclaration`, `ImprovementAim`, `MethodFamilySelection`, `CostAndRiskAccount`, and `QualityImprovementLoopRecord`, or else name the subject pattern for the live claim and leave `E.23` closed.

Quick lowering map:

| Entry cue | `E.23` use | Exit when this is the live claim |
|---|---|---|
| "Build a loop" or "loop engineering" | Ask which object version is being improved and which evaluation will be rerun. | If no object-version improvement claim is present, choose the subject pattern named by the live claim. |
| Agent retry, monitor, or escalation cycle | Use `E.23` only when the retry changes an object version and re-evaluation can show a changed result on declared coordinates. | Performed execution and work plans use the A.15 family; gate passage uses `A.21`; transformation-flow cycle structure uses `E.18`. |
| Harness engineering | The harness can be the object under improvement when its next version is evaluated against declared quality, cost, and risk conditions. | Running the harness is work; comparing harness variants is `G.9`; retaining variants is `C.18` or `C.19`; selected-set result declaration is `G.5`; for publication, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability. |
| Fast DPF seed hardening | A local DPF seed, pattern seed, relation record, or source pack can enter `E.23` after the object version and evaluation are declared. | Source-use and source-pack return use `G.2`; source decay, edition change, and refresh use `G.11`; PFAD and PFR decisions use `E.4.PFAD` and `E.4.PFR`; first-entry publication uses `E.11` only when publication is current. |

| Local name | Kind and function |
|---|---|
| `QualityImprovementLoopMethod` | Repeated improvement `U.Method` for one object version under one declared evaluation use. |
| `ObjectUnderImprovementRef` | Exact `U.Entity` version being changed, paired with its exact `U.Kind`. |
| `QualityEvaluationQuestionFrame` | The E.22 `U.Episteme` that binds one exact object version and use declaration to the selected characteristic space, predicate or comparator, ClaimScope, exact result-consuming work or decision, evaluation purpose, qualification window, and ordinary non-use boundary. E.23 reuses that frame; it does not move the consuming-use position into the declaration. |
| `QualityEvaluationUseDeclaration` | The E.22 `U.Episteme` that keeps an intended evaluator or planned condition separate from any current evaluator System and obtaining assignment occurrence, and keeps the evaluation pattern, optional semantic Method, selected characteristic space, predicate or comparator, ClaimScope, quality-model descriptions, evidence basis, result form, and qualification window distinct. E.23 reuses it; it does not define a second evaluation ontology. |
| `LoopEvaluationEvidenceBasis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version evaluated in one loop pass. It describes the evidence values actually checked and missing evidence positions found for that pass and is distinct from E.22's expected evidence-basis description. |
| `LoopEvaluationResultFormDescription` | `U.Episteme` describing the result-row form used for the current pass; normally the same form cited by the evaluation-use declaration. |
| `ImprovementAim` | Desired evaluation-result change. It names the intended quality change, not a value established by the repair itself. |
| `MethodFamilySelection` | Selected method family for the current object and evaluation. |
| `OperationFamilySelectionSet` | Optional operation-family set selected because its operations can change the evaluated result enough to justify cost. |
| `ObjectUnderImprovementEvaluationWorkRef` | Reference to one independently identified dated A.15.1 evaluation Work occurrence. The Work remains distinct from its application, returned value, result episteme, evidence, and judgment. |
| `ObjectUnderImprovementEvaluationResultRef` | Reference to one separately constituted result episteme whose claims state the evaluation result. The episteme is not the returned value; the exact A.6.1 result binding or direct evaluation-result relation remains separately identified. |
| `ImprovementPassWorkRef` | Reference to one independently identified dated A.15.1 Work occurrence that actually changes or attempts to change the object. Selection of a proposal supplies no such occurrence. |
| `CostAndRiskAccount` | Cost and risk account used to judge another pass or operation. |
| `ImprovementLoopDecisionValue` | Local closed value set `stop | continue | switchMethodFamily | openNewFrame | holdUntilInformationBasisSufficient`. |
| `QualityImprovementLoopRecord` | `U.Episteme` whose EntityOfConcern is the exact starting object version for one bounded improvement-loop application. Its ClaimGraph relates that version to one admitted unfolding structure, selected next-action proposals, independently identified evaluation and improvement Work, exact result bases and result epistemes, changed versions, evidence bases, trade-offs, cost and risk, and the selected continuation and boundaries. It describes those objects and relations; it is not the method, performer, Work occurrence, changed object, or structure. |
| `QualitySideEvaluationChangeClaim` | Controlled claim-node form inside a `U.ClaimGraph`; it compares before and after evaluation results for named object versions on declared `Q` coordinates under one evaluation-use declaration and qualification window. |
| `SourceComposedResultClaim` | Controlled claim-node form inside a `U.ClaimGraph`; it relates one changed-object result claim to exact accepted source-use decisions and each source contribution. It is neither the changed object nor a source-use decision. |
| `KindRestorationCheck` | Conditionally present precision-repair check required by the selected restoration predicate and its evaluation result. |

```text
LoopEvaluationEvidenceBasis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version evaluated in this loop pass
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration about that object version
  checkedEvidenceValueRefs[]: U.EntityRef, each referencing one evidence value actually checked
  checkedEvidenceValueKindRefs[]: U.KindRef, each referencing the exact kind of the paired evidence value
  checkedEvidenceRelationRefs[]: U.EntityRef, each referencing one governed evidence relation
  checkedEvidenceRelationKindRefs[]: U.KindRef, each referencing the exact kind of the paired evidence relation
  unfilledEvidencePositionDescriptionRefs[]: U.EpistemeRef, each referencing one description of an unfilled evidence position
  qualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description

QualityImprovementLoopRecord <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact starting object version for this bounded loop application
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that starting object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  improvementUnfoldingStructureRef: U.EntityRef, referencing one admitted A.22 constraint-governed unfolding structure; when transformation-flow membership is current, this same selected U.Structure also satisfies E.18/E.18.3 rather than designating a second structure
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration
  selectedNextActionProposalRefs[]: U.EpistemeRef, each referencing one CandidateImprovementProposalRow@Context; selection does not establish performance
  evaluationPassClaims[1..*]:
    evaluationWorkRef: U.EntityRef, constrained to U.Work
    evaluationApplicationRef?: U.EntityRef, referencing one exact A.6.1 application when that is the evaluation route
    evaluationResultBasisRef: U.EntityRef, referencing its A.6.1 result binding or the evaluation-result relation defined by the evaluation pattern
    evaluationResultEpistemeRef: U.EpistemeRef, referencing one separately constituted result episteme
    loopEvaluationEvidenceBasisRef: U.EpistemeRef, referencing one LoopEvaluationEvidenceBasis@Context
  improvementPassClaims[]:
    selectedNextActionProposalRef: U.EpistemeRef, referencing one still-propositional E.22 row
    improvementWorkRef?: U.EntityRef, constrained to U.Work and present only after actual improvement Work obtains
    changedObjectVersionRef?: U.EntityRef, present only when that changed version exists independently of this record
    changedObjectVersionKindRef?: U.KindRef, paired with changedObjectVersionRef
    workResultOrChangePredicateRefs[]?: U.EntityRef, each referencing a declared Work-to-result or Work-to-change predicate, or an A.6.1 result-binding predicate used by the basis
    workResultOrChangePatternLocators[]?: U.EntityRef, positionally paired with the predicate refs and each referencing the subject pattern that defines that predicate
    workResultOrChangeBasisRef?: U.EntityRef, referencing either the obtaining Work-to-result or Work-to-change relation, a filled local claim that names the Work, result or change, applicable conditions and facts, or an A.6.1 result binding
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  costAndRiskAccountDescriptionRef: U.EpistemeRef, referencing one cost-and-risk-account description
  loopDecisionValue: ImprovementLoopDecisionValue
  selectedContinuationClaimRef?: U.EpistemeRef, referencing the current branch-selection claim without turning it into Work
  stopBoundaryRef: U.EntityRef, referencing one ImprovementLoopBoundaryCondition@Context
  reconsiderationBoundaryRefs[]: U.EntityRef, each referencing one ImprovementLoopBoundaryCondition@Context
  loopDecisionReasonDescriptionRef: U.EpistemeRef, referencing one loop-decision-reason description
QualitySideEvaluationChangeClaim in U.ClaimGraph:
  qualityEvaluationUseDeclarationRef
  beforeObjectVersionRef and afterObjectVersionRef
  beforeEvaluationResultRefs[] and afterEvaluationResultRefs[]
  evaluationCoordinateRefs[]
  qualificationWindowDescriptionRef

SourceComposedResultClaim in U.ClaimGraph:
  changedObjectVersionRef and changedObjectVersionKindRef
  resultClaimNodeRef
  acceptedSourceUseDecisionRefs[1..*]
  sourceContributionDescriptionRefs[1..*]
```

The two named claims are node forms inside the claim graph of a result or loop episteme; a table row or serialization may publish them but does not become the claim.

Checked evidence values stay paired with their kinds; evidence relations form a separate pair. Every actual Work reference names an independently identified `U.Work` occurrence, and all facts required by A.15.1, A.2.1, and F.6 remain recoverable. A compact rendering may omit only an assignment identifier unused by the receiving claim; every performer and the underlying assignment occurrence and attribution remain recoverable.

For an improvement pass, the changed-version reference appears only after that version exists. The `workResultOrChange...` fields keep the declared predicate, its pattern locator, and the obtaining basis distinct. That basis must be an A.6.1 result binding, a direct Work-to-result or Work-to-change relation, or a local relation claim that names its participants, conditions, and obtaining facts. If only the predicate or locator is known, keep the proposal, Work, changed object, and Transformation separate and return a missing-governor finding for the intended Work-to-result or Work-to-change relation. An A.15.PROD route points to its applicable local claim rather than to the pattern as a generic claim.
The two record epistemes follow C.2.1 identity: claim content, exact EntityOfConcern, and effective `U.ReferenceScheme` determine each episteme edition. The listed loop fields contribute to claim content; `editionId` designates an already distinguished edition but does not constitute it. Empirical grounding, viewpoint membership, claim scope, model-use structure, applicability, qualification, evidence currentness, and source currentness remain separate relations or values defined elsewhere. A change in one of them changes a record episteme only when its claim content, EntityOfConcern, or reference scheme is revised; carrier and support serialization alone change neither episteme. These records do not create quality values, project evidence, release state, selected-set result declaration, actual publication, parity, refresh, Work, Transformation, or proof of quality.

The retained `@Context` suffixes on support species such as `LoopEvaluationEvidenceBasis@Context`, `CandidateImprovementProposalRow@Context`, `TradeoffProtectionSet@Context`, and `ImprovementLoopBoundaryCondition@Context` are compatibility and retrieval spellings only. No suffix or context label supplies a container, participant, ClaimScope, applicability, or identity discriminator. The three identity-bearing interface names in this package are suffixless: `QualityEvaluationQuestionFrame`, `QualityEvaluationUseDeclaration`, and `QualityImprovementLoopRecord`.

#### E.23:4.1a - Improvement Unfolding Structure Block

Use this block when a named review or replay use relies on the improvement loop's constraint-governed unfolding structure rather than only its method record. It keeps the proposal epistemes, predicted evaluation-result changes, independently identified pass Work and results, guarded alternatives, decision value, information-basis hold, stop, and neighboring returns exact instead of treating them as generic structural locations.

```text
ImprovementUnfoldingStructureBlock:
  unfoldingStructureRef: U.EntityRef, referencing one ImprovementLoopUnfoldingStructure
  objectVersionUnderImprovementRef: U.EntityRef
  objectVersionKindRef: U.KindRef
  evaluationFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame or equivalent exact frame
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration
  currentEvaluationResultRefs[]: U.EpistemeRef under that evaluation pattern
  candidateRepairProposalRefs[]: U.EpistemeRef, each referencing one CandidateImprovementProposalRow@Context under E.22
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  expectedEvaluationResultChangeRefs[]: U.EpistemeRef, each referencing one ExpectedEvaluationResultChange@Context
  evaluationPassPositionRows[]:
    evaluationWorkRef: U.EntityRef, constrained to U.Work
    evaluationApplicationRef?: U.EntityRef, referencing one exact A.6.1 application when used
    evaluationResultBasisRef: U.EntityRef, referencing an A.6.1 result binding or evaluation-result relation
    evaluationResultEpistemeRef: U.EpistemeRef, referencing one separate result episteme under C.2.1
  improvementPassPositionRows[]:
    selectedNextActionProposalRef: U.EpistemeRef
    improvementWorkRef?: U.EntityRef, constrained to U.Work and present only after one dated U.Work occurrence obtains
    changedObjectVersionRef?: U.EntityRef, present only after that version exists
    workResultOrChangePredicateRefs[]?: U.EntityRef, each referencing a declared Work-to-result or Work-to-change predicate, or an A.6.1 result-binding predicate used by the basis
    workResultOrChangePatternLocators[]?: U.EntityRef, positionally paired with the predicate refs and each referencing the subject pattern that defines that predicate
    workResultOrChangeBasisRef?: U.EntityRef, referencing either the obtaining Work-to-result or Work-to-change relation, a filled local claim that names the Work, result or change, applicable conditions and facts, or an A.6.1 result binding
  guardedContinuationRows[1..*]:
    exactGuardOrConstraintClaimRef
    selectedObtainingRelationOccurrenceRefs[]
    admissibleContinuationDescription
  loopDecisionValue: ImprovementLoopDecisionValue
  selectedContinuationClaimRef?: U.EpistemeRef
  unfilledInformationBasisPositionDescriptionRefs[1..*]?: U.EpistemeRef
  informationBasisSufficiencyConditionRef?: U.EntityRef, referencing one ImprovementLoopBoundaryCondition@Context
  evidenceRelationRefs[]?: U.EntityRef, each referencing one exact evidence relation occurrence with its subject-pattern locator
  stopBoundaryRef: U.EntityRef, referencing one ImprovementLoopBoundaryCondition@Context
  reconsiderationBoundaryRefs[]: U.EntityRef, each referencing one ImprovementLoopBoundaryCondition@Context
```

`ImprovementLoopUnfoldingStructure` is a local `A.22.CGUS` `U.Structure` specialization whose improvement-loop membership predicate is defined here. Its constituents are the independently identified values named above; its selected obtaining relations and guard claims keep their exact predicates, occurrence-identity rules, and defining ClaimGraphs. A position row, adjacency, or selected continuation creates none of them. When that exact selected structure additionally satisfies the transformation-flow membership and boundary conditions, E.18/E.18.3 recognizes the same `U.Structure`; do not manufacture a generic CGUS plus a second transformation-flow structure from reciprocal references. The organization is neither a root U-kind, enduring Work, context container, evidence, nor quality proof.

E.23 governs the coordinate-qualified prediction episteme:

```text
ExpectedEvaluationResultChange@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version whose later evaluation result is predicted
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration about that object version
  evaluationCoordinateRef: U.EpistemeRef, referencing one governed evaluation-coordinate description
  coordinateScaleRef: U.EpistemeRef, referencing one scale description that admits results for that coordinate
  currentEvaluationResultRef: U.EpistemeRef, referencing one current result episteme under the declared evaluation use
  changeExpressionKind: ExpectedEvaluationChangeExpressionKindValue
  expectedScaleValueRef?: U.EntityRef, referencing one value admitted by coordinateScaleRef
  expectedScaleValueKindRef?: U.KindRef, referencing the exact kind of that scale value
  expectedScaleRangeRef?: U.EpistemeRef, referencing one range description on coordinateScaleRef
  expectedScaleDirection?: EvaluationScaleDirectionValue
  candidateRepairProposalRefs[]: U.EpistemeRef, each referencing one CandidateImprovementProposalRow@Context
  predictionBasisRefs[]: U.EpistemeRef, each referencing one prediction-basis episteme
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
```

`ExpectedEvaluationChangeExpressionKindValue` is `expectedValue | expectedRange | expectedDirection`. Exactly one of value, range, or direction is present according to that kind. An expected value includes its exact kind and is admitted by `coordinateScaleRef`; an expected range belongs to that scale. `EvaluationScaleDirectionValue` is `increaseOnScale | decreaseOnScale | preserveWithinRange | enterDeclaredRange | leaveDeclaredRange`. Free direction prose does not close this episteme. The episteme predicts a later re-evaluation result. Its listed prediction fields contribute to claim content; a new claim content, EntityOfConcern, or effective reference scheme yields another C.2.1 episteme edition. A changed grounding, viewpoint, applicability, qualification, source-currentness, carrier, or rendering relation does not by itself change the prediction episteme; revise its claims when that change alters the prediction. It is not an operation, move, transition, work occurrence, or proof of improvement.

`ImprovementLoopDecisionValue` is `stop | continue | switchMethodFamily | openNewFrame | holdUntilInformationBasisSufficient`. The hold value has non-empty `unfilledInformationBasisPositionDescriptionRefs[]` and an `informationBasisSufficiencyConditionRef`; other values leave both absent. Each description says which information-basis position is unfilled without pretending to reference an entity that does not exist. The sufficiency condition says what information would make continuation admissible. A decision value or selected-continuation claim neither authorizes nor performs the next action.

`ImprovementLoopBoundaryCondition@Context` carries `boundaryConditionKind = stop | subjectAssertionReconsideration | informationBasisSufficiency`, a condition description, the affected object-version ref and exact kind, the unresolved assertion ref, and an optional non-semantic `candidateSubjectPatternLocator`. Source currentness, selected-set result declaration, actual publication, Work, evidence, and assurance remain distinct subject assertions under their exact predicates. A reconsideration boundary ends or redirects this E.23 use; it makes no later Work, decision, or relation obtain.

A visible cycle such as "draft -> evaluate -> repair -> re-evaluate" may be useful before execution. While any constituent, obtaining relation, guard, expected result change, protected trade-off, selected continuation, decision value, stop, or return needed for the wider improvement CGUS remains unresolved, keep that presentation as a `ProvisionalUnfoldingDemonstrationDescription@Context` about the object version and proposed continuation set. It may guide slot discovery, but it is not yet a structure or a slice. Admit the wider `ImprovementLoopUnfoldingStructure` first. Only then may a separate `DemonstrativeUnfoldingSlice@Context` select one traversal through that admitted structure and name it as EntityOfConcern. Neither episteme is a `QualityImprovementLoopRecord`, performed Work, actual Transformation, or proof of improvement.

#### E.23:4.2 - Loop method

For one quality-improvement loop:

1. Declare `ObjectUnderImprovementRef`, its kind and version, and one `QualityEvaluationUseDeclaration`; recover the current `QualityEvaluationQuestionFrame` when one already exists. Keep an intended evaluator or planned condition separate from any current evaluator System and obtaining assignment. Also keep the evaluation pattern, optional semantic Method, selected characteristic space, predicate and any comparator, ClaimScope, quality-model descriptions, expected evidence basis, result-form description, and qualification window separate. The question frame, not the declaration, names the work or decision that will consume the result.
2. Declare `ImprovementAim`, declared floor or desired substantive evaluation-result change, protected trade-offs, cost and risk account, and local stop condition. Do not declare `5`, all-`5`, or `5-defensible` as the work target; name the content property to improve instead.
3. Reuse the exact current E.22 question frame, or use `E.22` to open one for the first quality evaluation when no frame already binds the current purpose, scope, and result-consuming use.
4. Identify and run one dated evaluation Work occurrence that passes A.15.1 and F.6. Name its evaluation application and result binding or the direct evaluation-result relation; when a durable result claim is needed, identify a separate C.2.1 result episteme. For one FPF pattern version, that result has every E.21 coordinate, every `ShortRationale`, the `PrecisionRestorationProfile`, evidence basis, coordinate-specific payloads, and status. A loop record, profile pass, blocker summary, two-column table, or "no blockers" note is not a substitute.
5. Record row-atomic findings or proposal rows when work is returned. A step is closed only after its finding or proposal row is written; do not rely on memory or a later grouped summary. Each row is still an episteme about a proposed next action, not the action's performance, Work, or Transformation.
6. Select a proposal only as the next action. When it is actually performed, identify separate improvement Work under A.15.1 and F.6 and any actual Transformation under A.3.4. Connect that Work to a returned value or change only through an A.6.1 binding or a declared Work-to-result or Work-to-change relation that actually obtains. If the relation is unavailable, keep the proposal, Work, changed object, and Transformation separate and return the missing governor.

   Repair below-floor findings first. For exceptional improvement, look coordinate by coordinate for substantive gains—for example, better action guidance, a missing worked case or countercase, current sources, mature-content parity, cleaner relations, removal of displaced apparatus, or a split of overloaded content. Extra guards, catalogues, relation menus, or quality proof added only to defend a higher score are not improvements. Close with no change only when the evidence explains why no non-dominated improvement is available under the protected trade-offs.

   For precision-restoration defects, use the selected restoration or subject pattern as rule or guidance. Claim a semantic Method or MethodDescription only after A.3.1 and A.3.2 admit it; keep locator, Method, description, performer, assignment, Work, result, and responsibility separate. Before closure, run one bounded `KindRestorationCheck` over the distinctions that are actually live. A no-op closes only as `not triggered`, `ordinary prose`, `already satisfied`, or `blocker` with its evidence. Cite an existing defining `ClaimGraph` instead of copying it into E.23.
7. Identify a later re-evaluation as separate dated Work under A.15.1 and F.6. Re-evaluate the changed object version with the same evaluation structure and evidence basis, then name the application or direct result relation and any separate result episteme. Do not treat the later pass as a continuation field of the first Work.
8. Record what improved, what stayed floor-only, what was unchanged by value with its evaluation evidence basis, what became worse, and which rows were reclassified outside the evaluation. The before and after result epistemes remain distinct from both evaluation Work occurrences.
9. Decide `stop`, `continue`, `switchMethodFamily`, `openNewFrame`, or `holdUntilInformationBasisSufficient`. Keep current alternatives, exact guard or constraint claims, selected obtaining relation occurrences, selected continuation, stop, and subject-assertion reconsideration conditions in one admitted A.22 improvement unfolding structure. When transformation-flow membership is independently current, E.18/E.18.3 recognizes that same selected structure rather than another loop object. The decision and branch selection do not perform or authorize the next Work.
10. Leave a `QualityImprovementLoopRecord` that lets the next reader replay the object versions, question frame, use declaration, selected proposals, evaluation and improvement Work under A.15.1 and F.6, application and result or change bases, evidence and result epistemes, relevant source-use and currentness results, limitations, trade-offs, cost and risk, continuation, stop and return boundaries, and the loop decision with its reason.

#### E.23:4.3 - Stop, continue, and reopen

Stop when the current object version meets the declared floor or improvement aim and no feasible non-dominated proposal remains worth its cost under the current use, comparison set, source state, and protected trade-offs. If the remaining proposal mainly makes a value easier to argue while adding apparatus or worsening use, affordability, locality, source preservation, or ecology, reject that proposal; continue searching for a substantive content improvement if the improvement aim is still open, and stop only with a by-value no-proposal disposition.

Continue only when at least one `ExpectedEvaluationResultChange@Context` states a scale-qualified change worth its cost and risk. Switch method when the current method family is not changing the evaluated result, is too costly, or no longer fits the evaluation. Use `holdUntilInformationBasisSufficient` only with non-empty unfilled-position descriptions and the sufficiency condition that would make continuation admissible.

An all-`5`, all-exceptional, current-front-reaching, or current-front-improving result closes this loop locally. It does not say that future development is impossible. A new use, `Q` component, source anchor, `SoTA` front, comparison set, affordability boundary, or higher-payoff proposal can open a later loop.

Treat the five decision values as current continuation dispositions, not as Work states. A branch is usable only when its A.22 guarded continuation cites the exact current guard or constraint claim and the already-obtaining relation occurrences that make that alternative admissible. A stop or subject-assertion reconsideration is a boundary until an exact stronger predicate and current facts establish another relation. Naming A.15, E.22, G.11, G.5, or another subject pattern as a locator neither performs Work nor creates an object described there.

#### E.23:4.4 - Method-family selection

| Method family | Use when |
|---|---|
| `PDSAorPDCAFamily` | Learning quality, baseline comparison, measuring instruments, or standardize-then-repeat action matter for the improvement loop. |
| `POOGIFamily` | The evaluation problem is throughput-shaped or constraint-shaped. |
| `OODAFamily` | Orientation quality and feedback under changing conditions affect the evaluation. |
| `RalphLikeGeneralAdaptiveFamily` | A broadly capable agent can improve the object through repeated specification, feedback, memory, and verification under `C.19.1` cost and risk discipline. |
| `FixedPerformerObjectVersionUnderImprovementOptimizationFamily` | The performer or harness stays fixed while the object version is edited and re-evaluated. |
| `NQDQualitySideImprovementFamily` | The evaluation supplies the `Q` side for a declared NQD and OEE comparison and loop changes seek a non-dominated change in evaluated `Q` coordinates. |
| `SoTAReachAndMaintainFamily` | Reaching or maintaining an externally assigned front depends on composing several accepted source or practice anchors. |
| `SpecializedObjectFamilyCycle` | A specialized method family fits a declared characteristic space and is BLP-compatible. |

The selected family is justified by characteristic-space fit, the declared `ExpectedEvaluationResultChange@Context` values, cost and risk, and protected trade-offs. Familiarity, automation, or current popularity is not enough.

#### E.23:4.5 - Operation-family selection

An operation family is selected only when the loop record names:

1. one scale-qualified `ExpectedEvaluationResultChange@Context`;
2. failure mode addressed;
3. cost or risk reason;
4. protected trade-offs;
5. stop or removal condition.

Typical operation families are specification articulation, task decomposition, context refresh with carry-forward evidence, failure-context retry, verification against specification, memory or distillation, external critic or co-regulation, proposal portfolio use, search breadth or variants, bounded object-change budget, held-out evaluation, rejected-change memory, optimizer-memory separation, source-anchor contribution assignment, agent-tool-interface hardening, and task-family adaptation signature. They remain selectable only for the loop that justifies them.

#### E.23:4.6 - Cost and BLP discipline

`C.19.1` governs the preference for broad, scale-amenable methods when safety, admissibility, and practical fitness are comparable. `E.23` uses that preference but still evaluates end-to-end accepted-work cost:

```text
AcceptedWorkCost ~= resource_cost + tool_and_instrument_cost + adaptation_attempt_cost + skilled_attention_cost + rework_and_delay_cost + risk_exposure - avoided_loss_value
```

This is not a hidden quality score. It is a prompt for cost and risk reasoning. `resource_cost` can include compute, materials, energy, consumables, occupied facilities, or another resource consumed by the declared work; the other terms are interpreted for the actual project rather than presumed to be software costs. If avoided loss is large, an expensive loop can be right. If the object is simple, a direct edit or adjustment, small repair, lower-cost performer, specialized cycle, or one-shot evaluation can be better.

Harness improvement is usually the first high-leverage intervention when it reduces blind retry: better frames, row shapes, test cases, source references, local tools, memory, verification, and stop conditions.

#### E.23:4.7 - Source-composed, OEE, and NQD improvement

Accepted `SoTA` is the working external front only when assigned by the object-under-improvement evaluation, accepted source-use decision, or declared comparison set. `E.23` can govern a loop that reaches, maintains, or improves relative to that front; it does not self-assign `SoTA`.

When an evaluation-result change depends on source use, source currentness, or a dated external front, the loop record cites the exact accepted result from `G.2` or `G.11`, including the edition or date needed for replay. `E.23` carries that reference; it does not make the source-use or currentness decision.

When several source anchors are used, the loop records each exact accepted source-use decision and each source contribution. The changed object's result episteme then carries a `SourceComposedResultClaim` node in its `U.ClaimGraph`, relating the result claim to those decisions and contributions, and the changed object version is re-evaluated.

For NQD and OEE, use `E.23` to change one object version or candidate and re-evaluate it on declared `Q` coordinates. Use `C.17` for novelty, diversity, descriptors, and distances, `C.18` for archive and front insertion, `C.19` for pool policy, `G.5` for selected-set result declaration, `G.9` for parity, and `G.11` for currentness and refresh. When audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability.


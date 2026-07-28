---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__005_solution.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:4 — Solution"
line_start: 85550
line_end: 85771
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

`E.23` is the general method for repeated improvement of an object version under one `QualityEvaluationUseDeclaration@Context` named by value. The governing evaluation pattern or semantic method evaluates; its characteristic-space, Q-Bundle, rubric, review-profile, evidence-basis, and result-form descriptions constrain or interpret that evaluation. The loop changes the object, re-evaluates the changed version through the same declared method and quality model, checks trade-offs and cost, and decides whether to stop, continue, switch method family, open a new frame, or hold until the information basis is sufficient.

#### E.23:4.1 - Local names and kind settlement
Source and practitioner phrases such as "loop engineering", "agent loop", "harness loop", "prompt loop", and "workflow hardening loop" are entry phrases. Lower them into `ObjectUnderImprovementRef`, `QualityEvaluationUseDeclaration@Context`, `ImprovementAim`, `MethodFamilySelection`, `CostAndRiskAccount`, and `QualityImprovementLoopRecord@Context`, or else name the direct governing pattern for the live claim and leave `E.23` closed.

Quick lowering map:

| Entry cue | `E.23` use | Exit when this is the live claim |
|---|---|---|
| "Build a loop" or "loop engineering" | Ask which object version is being improved and which evaluation will be rerun. | If no object-version improvement claim is present, choose the direct governing pattern named by the live claim. |
| Agent retry, monitor, or escalation cycle | Use `E.23` only when the retry changes an object version and re-evaluation can show a changed result on declared coordinates. | Performed execution and work plans use the A.15 family; gate passage uses `A.21`; transformation-flow cycle structure uses `E.18`. |
| Harness engineering | The harness can be the object under improvement when its next version is evaluated against declared quality, cost, and risk conditions. | Running the harness is work; comparing harness variants is `G.9`; retaining variants is `C.18` or `C.19`; selected-set publication is `G.5`. |
| Fast DPF seed hardening | A local DPF seed, pattern seed, relation record, or source pack can enter `E.23` after the object version and evaluation are declared. | Source-use and source-pack return use `G.2`; source decay, edition change, and refresh use `G.11`; PFAD and PFR decisions use `E.4.PFAD` and `E.4.PFR`; first-entry publication uses `E.11` only when publication is current. |

| Local name | Kind and function |
|---|---|
| `QualityImprovementLoopMethod` | Repeated improvement `U.Method` for one object version under one declared evaluation use. |
| `ObjectUnderImprovementRef` | Exact `U.Entity` version being changed, paired with its exact `U.Kind`. |
| `QualityEvaluationUseDeclaration@Context` | The E.22 `U.Episteme` that keeps evaluator assignment, governing evaluation pattern, optional semantic method, quality-model descriptions, evidence basis, and result form distinct. E.23 reuses it; it does not define a second evaluation ontology. |
| `LoopEvaluationEvidenceBasis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version evaluated in one loop pass. It describes the evidence values actually checked and missing evidence positions found for that pass and is distinct from E.22's expected evidence-basis description. |
| `LoopEvaluationResultFormDescription` | `U.Episteme` describing the result-row form used for the current pass; normally the same form cited by the evaluation-use declaration. |
| `ImprovementAim` | Desired evaluation-result change. It names the intended quality change, not a value established by the repair itself. |
| `MethodFamilySelection` | Selected method family for the current object and evaluation. |
| `OperationFamilySelectionSet` | Optional operation-family set selected because its operations can change the evaluated result enough to justify cost. |
| `ObjectUnderImprovementReEvaluation` | Re-run or cited result of the governing evaluation method on the changed object version. |
| `CostAndRiskAccount` | Cost and risk account used to judge another pass or operation. |
| `ImprovementLoopDecisionValue` | Local closed value set `stop | continue | switchMethodFamily | openNewFrame | holdUntilInformationBasisSufficient`. |
| `QualityImprovementLoopRecord@Context` | `U.Episteme` whose EntityOfConcern is the exact starting object version for one improvement-loop application. Its claim graph relates that version to changed versions, applied proposal rows, evaluation-use declaration, actual evidence basis, results, trade-offs, cost and risk, and the loop decision. It describes the loop; it is not the method, performer, work occurrence, or changed object. |
| `QualitySideEvaluationChangeClaim` | Controlled claim-node form inside a `U.ClaimGraph`; it compares before and after evaluation results for named object versions on declared `Q` coordinates under one evaluation-use declaration and qualification window. |
| `SourceComposedResultClaim` | Controlled claim-node form inside a `U.ClaimGraph`; it relates one changed-object result claim to exact accepted source-use decisions and each source contribution. It is neither the changed object nor a source-use decision. |
| `KindRestorationCheck` | Conditionally present precision-repair check governed by the selected restoration pattern. |

```text
LoopEvaluationEvidenceBasis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version evaluated in this loop pass
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration@Context about that object version
  checkedEvidenceValueRefs[]: U.EntityRef, each referencing one evidence value actually checked
  checkedEvidenceValueKindRefs[]: U.KindRef, each referencing the exact kind of the paired evidence value
  checkedEvidenceRelationRefs[]: U.EntityRef, each referencing one governed evidence relation
  checkedEvidenceRelationKindRefs[]: U.KindRef, each referencing the exact kind of the paired evidence relation
  unfilledEvidencePositionDescriptionRefs[]: U.EpistemeRef, each referencing one description of an unfilled evidence position
  qualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description

QualityImprovementLoopRecord@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact starting object version for this loop application
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that starting object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  changedObjectVersionRefs[1..*]: U.EntityRef, each referencing one changed object version
  changedObjectVersionKindRefs[1..*]: U.KindRef, each referencing the exact kind of the paired changed version
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration@Context
  appliedProposalRefs[]: U.EpistemeRef, each referencing one CandidateImprovementProposalRow@Context
  loopEvaluationEvidenceBasisRefs[1..*]: U.EpistemeRef, each referencing one LoopEvaluationEvidenceBasis@Context
  evaluationResultRefs[1..*]: U.EpistemeRef, each referencing one result episteme produced by the declared evaluation use
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  costAndRiskAccountDescriptionRef: U.EpistemeRef, referencing one cost-and-risk-account description
  loopDecisionValue: ImprovementLoopDecisionValue
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

Checked evidence-value refs and kinds are positionally paired; checked evidence-relation refs and kinds form a second positional pair. Changed object-version refs and kinds are paired in the same way. The two named claims are node forms inside the claim graph of a result or loop episteme; a table row or serialization may publish them but does not become the claim.

Two carriers may publish the same episteme edition. `LoopEvaluationEvidenceBasis@Context` changes edition when the evaluated object version, bounded context, applicable grounding or viewpoint, declared evaluation use, checked evidence values or relations, unfilled evidence positions, qualification window, claim graph, or reference scheme changes. `QualityImprovementLoopRecord@Context` changes edition when its starting object version, bounded context, applicable grounding or viewpoint, changed-version relation, evaluation-use declaration, applied proposals, evidence-basis editions, evaluation results, trade-offs, cost and risk, decision, claim graph, or reference scheme changes. Carrier and support serialization alone change neither episteme. These names belong to the loop method. They do not create quality values, project evidence, release state, selected-set publication, parity, refresh, or proof of quality.

#### E.23:4.1a - Improvement Unfolding Structure Block

Use this block when a named review or replay use relies on the improvement loop's constraint-governed unfolding structure rather than only its method record. It keeps the proposal epistemes, predicted evaluation-result changes, decision value, information-basis hold, and neighboring relations exact instead of treating them as generic structural locations.

```text
ImprovementUnfoldingStructureBlock:
  unfoldingStructureRef: U.EntityRef, referencing one ImprovementLoopUnfoldingStructure
  objectVersionUnderImprovementRef: U.EntityRef
  objectVersionKindRef: U.KindRef
  evaluationFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame@Context or equivalent exact frame
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration@Context
  currentEvaluationResultRefs[]: U.EpistemeRef under that evaluation pattern
  candidateRepairProposalRefs[]: U.EpistemeRef, each referencing one CandidateImprovementProposalRow@Context under E.22
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  expectedEvaluationResultChangeRefs[]: U.EpistemeRef, each referencing one ExpectedEvaluationResultChange@Context
  loopDecisionValue: ImprovementLoopDecisionValue
  unfilledInformationBasisPositionDescriptionRefs[1..*]?: U.EpistemeRef
  informationBasisSufficiencyConditionRef?: U.EntityRef, referencing one ImprovementLoopBoundaryCondition@Context
  methodWorkLinkageRef?: U.EntityRef, referencing one MethodWorkUnfoldingLinkage@Context
  evidenceRelationRefs[]?: U.EntityRef, each referencing one UnfoldingStructureReferencedValueRelation@Context with exact evidence relation kind and direct governing pattern
  evaluationRelationRefs[]: U.EntityRef, each referencing one UnfoldingStructureReferencedValueRelation@Context with exact evaluation relation kind and direct governing pattern
  stopBoundaryRef: U.EntityRef, referencing one ImprovementLoopBoundaryCondition@Context
  governingPatternReturnBoundaryRefs[]: U.EntityRef, each referencing one ImprovementLoopBoundaryCondition@Context
```

`ImprovementLoopUnfoldingStructure` is a local `A.22.CGUS` `U.Structure` specialization governed here for improvement-loop use. It is neither a root U-kind nor performed work, evidence, or quality proof. The structure relates the exact values above; it is not their kind.

E.23 governs the coordinate-qualified prediction episteme:

```text
ExpectedEvaluationResultChange@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version whose later evaluation result is predicted
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration@Context about that object version
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

`ExpectedEvaluationChangeExpressionKindValue` is `expectedValue | expectedRange | expectedDirection`. Exactly one of value, range, or direction is present according to that kind. An expected value includes its exact kind and is admitted by `coordinateScaleRef`; an expected range belongs to that scale. `EvaluationScaleDirectionValue` is `increaseOnScale | decreaseOnScale | preserveWithinRange | enterDeclaredRange | leaveDeclaredRange`. Free direction prose does not close this episteme. The episteme predicts a later re-evaluation result. Its edition changes when the object version, bounded context, applicable grounding or viewpoint, declared evaluation use, coordinate, scale, current result, expected value, range, or direction, proposal set, prediction basis, protected trade-offs, claim graph, or reference scheme changes. A carrier or rendering change alone does not change the prediction episteme. It is not an operation, move, transition, work occurrence, or proof of improvement.

`ImprovementLoopDecisionValue` is `stop | continue | switchMethodFamily | openNewFrame | holdUntilInformationBasisSufficient`. The hold value has non-empty `unfilledInformationBasisPositionDescriptionRefs[]` and an `informationBasisSufficiencyConditionRef`; other values leave both absent. Each description says which information-basis position is unfilled without pretending to reference an entity that does not exist. The sufficiency condition says what information would make continuation admissible.

`ImprovementLoopBoundaryCondition@Context` carries `boundaryConditionKind = stop | governingPatternReturn | informationBasisSufficiency`, a condition description, the affected object-version ref and exact kind, and a conditional receiving-pattern ref when the boundary is a governing-pattern return. Source currentness stays with G.11, selected-set publication stays with G.5, work stays with A.15, and evidence and assurance stay with their direct governing patterns.

A visible cycle such as "draft -> evaluate -> repair -> re-evaluate" may be useful before execution. While any position, relation, expected result change, protected trade-off, decision value, or boundary needed for the wider improvement CGUS remains unresolved, keep that presentation as a `ProvisionalUnfoldingDemonstrationDescription@Context` about the object version and proposed continuation set. It may guide slot discovery, but it is not yet a structure or a slice. Admit the wider `ImprovementLoopUnfoldingStructure` first. Only then may a separate `DemonstrativeUnfoldingSlice@Context` select one traversal through that admitted structure and name it as EntityOfConcern. Neither episteme is a `QualityImprovementLoopRecord@Context`, performed work, or proof of improvement.

#### E.23:4.2 - Loop method

For one quality-improvement loop:

1. Declare `ObjectUnderImprovementRef`, its exact kind and version, and one `QualityEvaluationUseDeclaration@Context`. Keep the evaluation performer assignment, governing pattern description, optional semantic method, quality-model descriptions, expected evidence basis, and result-form description in their separate slots.
2. Declare `ImprovementAim`, declared floor or desired substantive evaluation-result change, protected trade-offs, cost and risk account, and local stop condition. Do not declare `5`, all-`5`, or `5-defensible` as the work target; name the content property to improve instead.
3. Use `E.22` to frame the first quality evaluation when the purpose is not already explicit.
4. Run the object-under-improvement evaluation in its declared result form. For one FPF pattern version, this is an E.21 result with every coordinate, every `ShortRationale`, the `PrecisionRestorationProfile`, evidence basis, coordinate-specific payloads, and status. A loop record, profile pass, blocker summary, two-column table, or "no blockers" note is not a substitute.
5. Record row-atomic findings or proposal rows when work is returned. A step is closed only after its finding or proposal row is written; do not rely on memory or a later grouped summary.
6. Apply repairs or variants to the object. Repair below-floor findings first. When exceptional improvement is requested, search coordinate-by-coordinate for substantive content improvements: better positive action guidance, a missing worked slice, case and countercase coverage, source-currentness carry-through, mature-content discharge, relation cleanup, deletion of displaced apparatus, split of overloaded content, or relocation of quality proof or process proof. Guards, boundary catalogues, relation menus, or quality proof added solely to make a higher value defensible are dominated changes, not improvements. A no-change closure is admissible only when the row cites its `LoopEvaluationEvidenceBasis@Context` and explains why no non-dominated content improvement is available under the protected trade-offs. When generation, selection, publication, parity, refresh, decision, planning, work, evidence, or assurance claims leave quality improvement, keep the pattern that governs that claim, relation, or boundary in the loop record or `Relations`. Do not let loop-method prose replace the object's positive content. For precision-restoration defects, use the selected restoration or governing pattern named by the evaluation: `E.10`, `E.10.ARCH`, `F.18`, `F.19`, or an object-specific pattern. Before closure, a bounded complete `KindRestorationCheck` states what kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope were present before the edit and what kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope the changed text now carries when those items are live. No-op closure is admissible only as `not triggered`, `ordinary prose`, `already satisfied`, or `blocker` with its evidence basis; otherwise unchanged text remains a live finding. When another pattern governs the kind under repair, relation, claim, or position, cite that pattern; `E.23` records the repair and reruns the evaluation, it does not duplicate the restoration algorithm.
7. Re-evaluate the changed object version through the object-under-improvement evaluation, preserving that evaluation's coordinate set, evidence basis, result-row shape, short rationales, attention-discharge rows, and coordinate-specific payloads.
8. Record what improved, what stayed floor-only, what was unchanged by value with its evaluation evidence basis, what became worse, and which rows were reclassified outside the evaluation.
9. Decide `stop`, `continue`, `switchMethodFamily`, `openNewFrame`, or `holdUntilInformationBasisSufficient`.
10. Leave a `QualityImprovementLoopRecord@Context` sufficient for the next reader to replay the object versions, `QualityEvaluationUseDeclaration@Context`, actual `LoopEvaluationEvidenceBasis@Context`, evaluation results, applicable source-use and currentness result references, limitations, trade-offs, cost and risk, and the loop decision with its reason.

#### E.23:4.3 - Stop, continue, and reopen

Stop when the current object version meets the declared floor or improvement aim and no feasible non-dominated proposal remains worth its cost under the current use, comparison set, source state, and protected trade-offs. If the remaining proposal mainly makes a value easier to argue while adding apparatus or worsening use, affordability, locality, source preservation, or ecology, reject that proposal; continue searching for a substantive content improvement if the improvement aim is still open, and stop only with a by-value no-proposal disposition.

Continue only when at least one `ExpectedEvaluationResultChange@Context` states a scale-qualified change worth its cost and risk. Switch method when the current method family is not changing the evaluated result, is too costly, or no longer fits the evaluation. Use `holdUntilInformationBasisSufficient` only with non-empty unfilled-position descriptions and the sufficiency condition that would make continuation admissible.

An all-`5`, all-exceptional, current-front-reaching, or current-front-improving result closes this loop locally. It does not say that future development is impossible. A new use, `Q` component, source anchor, `SoTA` front, comparison set, affordability boundary, or higher-payoff proposal can open a later loop.

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

For NQD and OEE, `E.23` can change one object version or candidate to improve its evaluation result on declared `Q` coordinates. `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` keep authority over novelty, diversity, descriptors, distances, archive or front insertion, pool policy, selected-set publication, parity, and refresh.


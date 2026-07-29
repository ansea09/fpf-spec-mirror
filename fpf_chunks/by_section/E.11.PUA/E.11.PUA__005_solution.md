---
chunk_kind: "child"
pattern_id: "E.11.PUA"
pattern_title: "Pattern Use in a Working Situation and First Useful Result"
section_id: "E.11.PUA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUA/E.11.PUA__005_solution.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "E.11.PUA — Pattern Use in a Working Situation and First Useful Result"
  - "E.11.PUA:4 — Solution"
line_start: 75797
line_end: 76177
dependencies:
  - "A.15"
  - "A.6.5"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "C.2.1"
  - "E.11"
  - "E.11.PUR"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.22"
  - "E.23"
  - "E.8"
  - "G.11"
keywords:
---

### E.11.PUA:4 - Solution

Apply one selected pattern through a short result-oriented procedure. Keep the subject result in the foreground; add addressable pattern-use records only when a named receiving use relies on them.

#### E.11.PUA:4.0 - Kind-preserving dependency order (Plain)

The acting `U.System` works under a `U.RoleAssignment`: it selects, constructs, or refines a semantic `U.Method`, records intended work only when planning is current, performs dated `U.Work`, and thereby changes, preserves, examines, or evaluates the real EntityOfConcern. The epistemic support line may guide and evaluate this work; it does not become the actor, role assignment, method, work, or affected entity.

Use the following as a **Plain dependency order** for reading the case. It is not a `U.Structure`, workflow, form, interface, serialization, causal chain, or claim that every item exists. Each later item is inspected only when its direct governor and the current question make it necessary:

1. start from the current EntityOfConcern, effective ReferenceScheme, and practical question;
2. add an exact ClaimScope, project-work relation, or bounded-model-use structure only when that neighboring relation changes the use;
3. add accepted problem-side material only when it is current;
4. inspect a public template or the direct pattern, then keep the selected or rejected direct pattern with its fit reason;
5. identify a selected, constructed, or refined `U.Method` only when the direct `Solution` makes that method current;
6. identify a PlanItem or `U.WorkPlan` only when intended work is current, and identify dated `U.Work` only after the work occurs;
7. name the independently governed entity or obtaining relation that answers the question; identify the exact method, plan, dated Work, transformation, evaluation, decision, or separately governed receiving-use object relative to which it is a result; and cite the category-correct direct basis for that reading; and
8. state the separate receiving use, stop, return, or neighboring pattern only when it is current.

`TaskSignature` remains a pre-method-selection signature. It can constrain method search; it is not the task, plan, or work occurrence. OEE and NQD may retain method or architecture candidates before selection. G.5 publishes a selected set; A.3.1 settles method identity; A.15 governs planning and work. The order above introduces no arrow, transfer, production, result, or use relation.

#### E.11.PUA:4.1 - The ordinary seven-step use

Before making any pattern-use record, answer aloud: "What exactly do I have now? Which fact, measured condition, completed change, decision, or declared relation makes that answer true? What can I do next, and which later work has not happened yet?" Then use the exact terms below only where they change that answer.

1. **Recognize the working situation.** Name the subject or relation in ordinary domain language and ask the current practical question. State an exact kind now only when a nearby kind difference can change the pattern or result.
2. **Inspect one direct pattern.** Read its Problem frame, Problem, Forces, Solution, Consequences, ordinary boundary, and nearest stronger neighbor. Do not select from its title or one trigger word alone.
3. **Say what useful result would answer the question.** Name the entity or obtaining relation plainly enough to distinguish it from a plan, description, recommendation, work occurrence, or other nearby value. Also say which exact method, plan, dated Work, transformation, evaluation, decision, or separately governed receiving-use object makes the result phrase meaningful here. When a nearby distinction remains ambiguous or replay matters, state the result kind and direct owner separately from the category-correct relation occurrence, A.6.1 binding, or local-claim basis that makes the phrase true.
4. **Apply the Solution.** Perform the direct pattern's action-guiding method under its conditions. A project-tailored method description, WorkPlan, gate result, work occurrence, or other entity keeps its own direct governor. If the use claims that dated Work first constituted an entity, recover the separate A.15.PROD inception claim; pattern application is not a generic production relation.
5. **Check what now exists or obtains.** Identify a newly current entity, relation occurrence, evaluation, decision, or change under its own direct owner. Open A.15.PROD only when exact dated Work and its actual changes are claimed to have first constituted an entity under its identity rule. A pre-existing entity may instead receive new grounding for the current question. If the expected subject result still does not exist, name only the exact interim entity and its own direct basis while leaving the subject expectation open. Do not turn grounding, planning, evaluation, acceptance, publication, or non-agentive change into production.
6. **State the immediate continuation only as needed.** Name the next receiving use, stronger neighbor, or unresolved clarification in conversation. Materialize basis, expectation, result, flow, provenance, or boundary epistemes only when a named later use needs them to remain addressable.
7. **Stop or return.** Stop when the smallest useful result or honest interim entity, its direct owner, the exact governed object relative to which the result phrase is true, and the category-correct direct basis can answer the current question, or when a pre-existing entity is adequately grounded through its exact relations. Return when the concern, basis, expected entity, governing pattern, direct relation, or current receiving-use condition changes. A genuine stop needs no receiver.

The practical delta has three honest forms. An entity or relation occurrence may become current under its exact direct owner and category-correct basis; A.15.PROD enters only when exact dated Work and actual change are claimed to have first constituted an entity. A pre-existing entity may remain unchanged while an exact grounding finding becomes adequate for the current use. If the expected subject entity still does not exist, the exact interim entity, its direct basis, and the return condition become explicit while the expectation remains open.

#### E.11.PUA:4.2 - Reliance profiles

```text
PatternUseRelianceProfileValue = ordinaryBounded | relianceBearing
```

In `ordinaryBounded` use, the subject, practical question, inspected pattern, useful result in ordinary language, governed relative-object kind, and stop or return remain recoverable in conversation. State exact kinds, direct owner, and category-correct direct basis only when needed to distinguish the result from a nearby value. No candidate basis, fit record, flow-position record, provenance note, closure record, or receiver is required.

In `relianceBearing` use, materialize only the distinctions that the named reliance will use. Another reader may need a candidate basis and rationale. Automation may need the result kind and direct owner, the exact governed object, and the category-correct basis with its separate governors. Delayed review may need the descriptive flow position and a separate receiving-use disposition. A receiver appears only when return, continuation, or named reliance is current. No profile causes all support records to be materialized.

When one named later use needs a compact replay carrier but not the fuller candidate and closure relations, use this reliance-bearing trace:

```text
CompactPatternUseTrace@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  claimScopeRef?: U.EntityRef, referencing one U.ClaimScope
  modelUseStructureRef?: U.EntityRef, referencing one BoundedModelUseStructure
  projectWorkRef?: U.EntityRef, referencing one composite U.Work
  editionId
  practicalQuestionDescriptionRef: U.EpistemeRef
  consideredDirectPatternRef: U.EntityRef, referencing one U.MethodDescription
  patternSelectionDisposition: selected | rejected
  compactFitRationaleRef: U.EpistemeRef
  expectedResultKindRef: U.KindRef
  expectedResultDirectOwnerPatternRef: U.EntityRef, referencing one U.MethodDescription
  expectedResultRelativeToGovernedObjectKindRef: U.KindRef
  expectedResultRelativeToGovernedObjectDescriptionRef: U.EpistemeRef
  expectedResultDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  expectedResultDirectBasisDescriptionRef: U.EpistemeRef
  expectedResultDescriptionRef: U.EpistemeRef
  obtainedResultRef?: U.EntityRef
  obtainedResultKindRef?: U.KindRef
  obtainedResultDirectOwnerPatternRef?: U.EntityRef, referencing one U.MethodDescription
  obtainedResultRelativeToGovernedObjectRef?: U.EntityRef
  obtainedResultRelativeToGovernedObjectKindRef?: U.KindRef
  obtainedResultDirectBasisKind?: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  obtainedResultDirectBasisRef?: U.EntityRef
  obtainedDirectRelationOrBindingGoverningPatternRef?: U.EntityRef, referencing one U.MethodDescription
  obtainedLocalClaimDerivationGoverningPatternRef?: U.EntityRef, referencing A.6.RCD
  obtainedLocalClaimBasePredicateGoverningPatternRefs[]?: U.EntityRef, each referencing one U.MethodDescription
  boundaryDisposition: stop | return
  boundaryConditionDescriptionRef: U.EpistemeRef
  conditionalReceivingPatternRef?: U.EntityRef, referencing one U.MethodDescription
```

The trace is absent from ordinary conversational use. When materialized for a named reliance, C.2.1 identifies it through claim content, exact EntityOfConcern, and effective reference scheme. `claimScopeRef`, `modelUseStructureRef`, and `projectWorkRef` are present only when the exact neighboring relation changes the pattern use; they are not additional episteme-identity fields, and the reference alone does not make that relation obtain.

The expectation names the exact result kind and direct owner, the kind of method, plan, dated Work, transformation, evaluation, decision, or separately governed receiving-use object relative to which the result phrase would be true, and one category-correct basis branch. It asserts neither existence nor obtaining. For a selected pattern, the obtained-result core positions—from `obtainedResultRef` through `obtainedResultDirectBasisRef`—are present together or absent together; a rejected pattern leaves them absent. In the direct-relation branch, the claim graph exposes predicate, participants, applicability, obtaining, occurrence identity, and direct governor. In the A.6.1 branch, it exposes the operation, application, argument or result binding, and direct governor. In the local-claim branch, the direct relation-or-binding governor is absent, the A.6.RCD derivation governor and every base-predicate direct owner are present, and the claim graph exposes polarity, substrate or constructor, base predicates, participants, case facts, and any support or warrant required by the receiving use. The claim episteme does not obtain, and A.6.RCD does not replace its base owners.

A return names `conditionalReceivingPatternRef` only when that continuation is current. A genuine stop leaves the field absent. No receiver is fabricated merely to complete the trace.

#### E.11.PUA:4.2.1 - Admitted support species and governing patterns

```text
PracticalUseQuestion@Context <: U.Episteme
PatternUseResultExpectation@Context <: U.Episteme
PatternUseResultClosureFinding@Context <: U.Episteme
PatternUseReceivingUseDispositionFinding@Context <: U.Episteme
PatternUseBoundaryCondition@Context <: U.Episteme
CandidatePatternUseRationale@Context <: U.Episteme
PatternUseCoordinationRationale@Context <: U.Episteme
PracticalUseCardComparisonRationale@Context <: U.Episteme
PatternUseFitFinding@Context <: U.Episteme
CandidatePatternUse@Context <: U.Episteme
PatternUseApplicabilityFinding@Context <: U.Episteme
```

`@Context` in these legacy support-species names is a compatibility and retrieval suffix. It names no `U.BoundedContext`, universal situation, project container, relation, or identity field. Every support episteme follows C.2.1 identity. Claim scope, bounded model use, project work, qualification window, and other working conditions enter only through the exact neighboring object and direct relation needed by the receiving use.

PUA governs the practical question, optional compact trace, candidate basis, candidate support episteme, candidate rationale, result expectation, result-closure finding, and separate receiving-use-disposition finding. `E.11` governs public card comparison rationale. `E.11.PUR` governs fit, applicability, recommendation, coordination rationale, coordination, and ordering. These relations consume A.6.5 SlotSpec discipline; A.6.5 does not govern their identity. PUA's findings cite the result's direct owner and one category-correct direct basis. In the local-claim branch they keep the A.6.RCD derivation governor distinct from every base-predicate owner. They introduce no result or actual-use relation kind.

#### E.11.PUA:4.3 - Question, boundary, and expectation

```text
PracticalUseQuestion@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  claimScopeRef?: U.EntityRef, referencing one U.ClaimScope
  modelUseStructureRef?: U.EntityRef, referencing one BoundedModelUseStructure
  projectWorkRef?: U.EntityRef, referencing one composite U.Work
  editionId
  questionDescriptionRef: U.EpistemeRef

PatternUseBoundaryCondition@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the CandidatePatternUse@Context or PracticalUseQuestion@Context whose use is bounded
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  boundaryConditionKind: candidateAdmission | minimumUsableResult | stop | return | wrongTurnRecovery | strongerNeighbor | missingGovernor | missingInformation | costEscalation | reversibilityEscalation | receivingPatternContinuation
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
  expectedResultDirectOwnerPatternRef: U.EntityRef, referencing one U.MethodDescription
  expectedResultRelativeToGovernedObjectKindRef: U.KindRef
  expectedResultRelativeToGovernedObjectDescriptionRef: U.EpistemeRef
  expectedResultDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  expectedResultDirectBasisDescriptionRef: U.EpistemeRef
  expectedResultFlowPosition: patternSelectionFlowResult | selectedPatternApplicationFlowResult | downstreamSubjectWorkFlowResult
  expectedResultDescriptionRef: U.EpistemeRef
  minimumUsableResultBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  intendedReceivingPatternRef?: U.EntityRef, referencing one U.MethodDescription
  intendedReceivingGovernedObjectKindRef?: U.KindRef
  intendedReceivingUseDescriptionRef?: U.EpistemeRef
  receivingPatternContinuationBoundaryRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The expectation never proves that the result entity exists, that a relation or binding obtains, or that a local claim is true. It first identifies the result kind and its direct owner. It then names which kind of exact method, plan, dated Work, transformation, evaluation, decision, or separately governed receiving-use object a real closure must identify, and which direct basis would make the readable result phrase true relative to that object. The basis description is branch-specific: relation occurrence; A.6.1 operation-application binding; or A.6.RCD local C.2.1 claim with polarity, substrate or constructor, base predicates and their direct owners, participants, case facts, and any support or warrant required by the receiving use. The last branch is not an obtaining basis, and the derivation governor is not a substitute subject owner.

The flow position is a descriptive PUA role. `intendedReceivingPatternRef`, `intendedReceivingGovernedObjectKindRef`, `intendedReceivingUseDescriptionRef`, and `receivingPatternContinuationBoundaryRef` are present together only when an actual continuation or named downstream reliance is current; otherwise all four are absent. A genuine stop needs no receiver. In a boundary record, `return`, `wrongTurnRecovery`, `strongerNeighbor`, and `receivingPatternContinuation` may name the current receiver; `stop`, `missingGovernor`, and `missingInformation` do not invent one. Receiving-position kind and ref are both present or both absent. `candidateAdmission` means that Problem frame, Forces, Solution conditions, expected result, category-correct basis template, and ordinary boundary are recoverable enough for further inspection; it is neither an applicability finding nor a selection.

#### E.11.PUA:4.4 - Candidate basis under named reliance

Construct a durable candidate only after inspecting the direct pattern's Problem frame, Problem, Forces, Solution, Consequences, and ordinary boundary. A public README template can supply a reusable starting point, but current project values come from the exact EntityOfConcern, practical question, effective reference scheme, and any current claim-scope, project-work, model-use, qualification-window, or other direct relation named by value.

```text
CandidatePatternUseBasisRelation@Context <: U.Relation:
  publicTemplateRef?: U.EpistemeRef, referencing one PublicCandidatePatternUseTemplate@FPFReadme
  directPatternRef: U.EntityRef, referencing one U.MethodDescription
  directSolutionSectionRef: U.EntityRef, referencing the E.17 PublicationUnit containing the direct pattern's Solution
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  practicalUseQuestionRef: U.EpistemeRef, referencing one PracticalUseQuestion@Context
  problemCardRef?: U.EpistemeRef, referencing one ProblemCard@Context
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  additionalBasisRelationRefs[]?: U.EntityRef, each referencing one CandidatePatternUseAdditionalBasisRelation@Context
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  RelationRefKind: U.EntityRef
  Direction: <entityOfConcernRef, practicalUseQuestionRef, directPatternRef> -> candidatePatternUseRef
  Dependence: local to the exact direct pattern, question, expectation, candidate editions, and any additional basis relation named below
  Identity: <entityOfConcernRef, practicalUseQuestionRef, directPatternRef, directSolutionSectionRef, resultExpectationRef, candidatePatternUseRef>

CandidatePatternUseAdditionalBasisRelation@Context <: U.Relation:
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  basisValueRef: U.EntityRef
  basisValueKindRef: U.KindRef
  basisRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  basisGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  basisUseDescriptionRef: U.EpistemeRef
  RelationRefKind: U.EntityRef
  Direction: basisValueRef -> candidatePatternUseRef for basisUseDescriptionRef
  Dependence: local to the candidate, basis value, exact governing relation, and their current editions
  Identity: <candidatePatternUseRef, basisValueRef, basisValueKindRef, basisRelationSignatureRef if present, basisUseDescriptionRef>

CandidatePatternUse@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  claimScopeRef?: U.EntityRef, referencing one U.ClaimScope
  modelUseStructureRef?: U.EntityRef, referencing one BoundedModelUseStructure
  projectWorkRef?: U.EntityRef, referencing one composite U.Work
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

Each additional basis relation names its exact value, kind, relation signature when current, direct governing pattern, and use in this candidate. The public template is absent when the candidate was formed by direct pattern inspection without a README template. `directSolutionSectionRef` is the Solution section of `directPatternRef`; no redundant solution-method-description ref is retained. A project-tailored method description is a separate `U.MethodDescription` under A.3.2. If dated Work first constitutes that episteme and the inception claim matters, A.15.PROD governs the claim; any derivation or reuse relation to the direct pattern remains separately governed. Applicability, recommendation, and coordination remain governed by `E.11.PUR`.

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

#### E.11.PUA:4.5 - Actual-result closure and receiving-use disposition

PUA introduces no actual-result relation and no universal actual-use relation. Keep two questions separate: what makes the candidate result entity exist or the relation occurrence obtain under its direct owner, and what exact direct basis makes the readable result phrase true relative to the current method, plan, dated Work, transformation, evaluation, decision, or separately governed receiving-use object. Those bases may be the same occurrence only when the result itself is that relation occurrence. When a named later use needs addressable closure, materialize a C.2.1 finding that points to both the result's direct owner and the category-correct basis:

```text
PatternUseResultClosureFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the independently governed result entity or obtaining relation occurrence
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  resultDirectOwnerPatternRef: U.EntityRef, referencing one U.MethodDescription
  resultRelativeToGovernedObjectRef: U.EntityRef
  resultRelativeToGovernedObjectKindRef: U.KindRef
  resultDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  resultDirectBasisRef: U.EntityRef
  resultDirectRelationOrBindingGoverningPatternRef?: U.EntityRef, referencing one U.MethodDescription
  resultLocalClaimDerivationGoverningPatternRef?: U.EntityRef, referencing A.6.RCD
  resultLocalClaimBasePredicateGoverningPatternRefs[]?: U.EntityRef, each referencing one U.MethodDescription
  resultFlowPosition: patternSelectionFlowResult | selectedPatternApplicationFlowResult | downstreamSubjectWorkFlowResult
  resultBearingPathSliceId?: PathSliceId
  resultBearingDesignRunTag?: DesignRunTag
  closureBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The three flow-position values are descriptive PUA roles, not kinds, relations, or occurrence identities. The finding's claim graph names the result entity, its direct owner, the exact governed object relative to which the result wording is true, and exactly one direct-basis branch. For a direct relation occurrence it names predicate, participants, applicability, obtaining, occurrence identity, and the direct governor. For an A.6.1 binding it names operation, application, argument or result binding, and its direct governor. For an A.6.RCD local C.2.1 claim, the relation-or-binding governor is absent; the claim ref, polarity, substrate or constructor, base predicates, their direct owners, participants, case facts, and any support or warrant required by the receiving use are recoverable, with the derivation governor named separately. The claim does not obtain. If the result itself is a relation occurrence, `entityOfConcernRef` and `resultDirectBasisRef` may designate that same occurrence. The closure finding reports those facts; it creates none of them.

Open A.15.PROD only when the closure claims that exact dated Work, through independently identified actual changes and the applicable identity rule, first constituted an entity. A relation occurrence may first obtain through its direct predicate; an evaluation or decision becomes current under its own direct owner; a non-agentive change needs no production claim. Completion, evaluation, acceptance, publication, continuation, and later use remain separate. If the claimed result existed already, use `4.6` instead. If no direct basis is recoverable, retain the independently governed entity and return the exact `missingGovernor` or `missingInformation` boundary rather than minting a closure relation.

Path slice and `DesignRunTag` are both present only when the exact result-bearing position and its one TFS are already recoverable under E.18; otherwise both are absent. These fields are provenance cues, not identifiers for another TFS, a network, or a cross-flow relation.

Record receiving-use disposition separately, and only for a named reliance:

```text
PatternUseReceivingUseDispositionFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the same result entity or relation occurrence as the closure finding
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  resultClosureFindingRef: U.EpistemeRef, referencing one PatternUseResultClosureFinding@Context
  receivingUseRealizationState: realized | intendedNotYetRealized
  receivingGovernedObjectRef?: U.EntityRef
  receivingGovernedObjectKindRef?: U.KindRef
  realizedReceivingUseDirectBasisKind?: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  realizedReceivingUseDirectBasisRef?: U.EntityRef
  realizedReceivingUseDirectRelationOrBindingGoverningPatternRef?: U.EntityRef, referencing one U.MethodDescription
  realizedReceivingUseLocalClaimDerivationGoverningPatternRef?: U.EntityRef, referencing A.6.RCD
  realizedReceivingUseLocalClaimBasePredicateGoverningPatternRefs[]?: U.EntityRef, each referencing one U.MethodDescription
  intendedReceivingPatternRef?: U.EntityRef, referencing one U.MethodDescription
  intendedReceivingGovernedObjectKindRef?: U.KindRef
  intendedReceivingUseDescriptionRef?: U.EpistemeRef
  receivingUseRealizationConditionRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

In the `realized` state, the receiving governed object, kind, direct-basis kind, and basis ref are present; the intended positions are absent. The same branch rule separates a direct relation or A.6.1 governor from an A.6.RCD derivation governor and the direct owners of the local claim's base predicates. The claim graph exposes the exact participants and facts. In `intendedNotYetRealized`, the intended pattern, governed-object kind, description, and condition are present together and all realized positions are absent; an intention is not an obtaining use relation. A stop without a receiving use has no disposition finding.

When ordinary language says that a result from one TFS is used as an input, tool, context, or constraint in another, treat those words only as cues. Name the exact result-bearing position and exact receiving position—one `FlowPositionRef` for each—plus the directly governed relation occurrence connecting their participants, and keep the result's kind unchanged. With no direct relation kind or predicate, return `missing-governor`; with a governor but undecided facts, leave the relation open and name the grounding boundary; with a false predicate, assert no occurrence; with an obtaining occurrence but a missing endpoint binding, return `missing-endpoint-binding` and name that binding. Use E.18 for each TFS-local position and local `DesignRunTag`; use E.18.NET only when independently identified TFS values must be treated together as a network. No input, tool, context, constraint, result, or adjacency label supplies the direct relation.

When the thing being called a result is `U.Work`, identify that dated occurrence under A.15.1. Planning, setup, authorization, triggering, or enabling work does not produce that Work. Call the occurrence a result of the selected use in a reliance-bearing closure only when the exact category-correct basis for that reading is present; otherwise keep the Work and the pattern-use description separate.

#### E.11.PUA:4.6 - Pre-existing and still-absent subject results

When the expected entity existed before the current use, the current use may establish a C.2.1 grounding finding about that unchanged entity:

```text
GroundingBasisPair:
  groundingRelationOccurrenceRef: U.EntityRef
  groundingGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription

PreExistingResultGroundingFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the pre-existing entity
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  groundingBasisPairs[1..*]: GroundingBasisPair
  groundingAdequacyDescriptionRef: U.EpistemeRef
  groundingUseBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

Each `GroundingBasisPair` preserves one relation occurrence with its direct governor. The finding's ClaimGraph names the grounded proposition and the covered subject claim. For a C.2.1 episteme a pair may cite an exact `EpistemeEmpiricalGroundingRelation`; for another subject it uses the direct measurement, observation, evidence-use, diagnostic, or subject predicate that actually grounds that proposition. Inspection, a record, or evidence proximity does not ground the entity by itself. If no direct grounding basis is recoverable, return its exact blocker. The pre-existing entity is not newly produced.

If the current use calls the grounding finding its result, add a separate `PatternUseResultClosureFinding@Context` whose EntityOfConcern is that finding. Its direct basis must connect the finding to the current method, plan, Work, transformation, evaluation, decision, or receiving-use object through a relation occurrence, A.6.1 binding, or category-correct local claim. The occurrence that grounds the pre-existing subject does not by itself make the grounding finding a result of the current use. Cite A.15.PROD only when exact dated Work and its actual changes first constituted the finding episteme.

When the expected subject result still does not exist, close the current use only on an exact interim `PatternUseResultClosureFinding@Context`. Its entity has its own direct owner and category-correct basis relative to the current governed object. Keep the subject-result expectation open. A plan for machining does not become a machined component; a treatment recommendation does not become a changed clinical state; an assessment plan does not become learned capability.

#### E.11.PUA:4.7 - Reliance-bearing final-practice test

Use this test when the declared teaching, rehearsal, or evaluation use is to establish that a participant can select a pattern, preserve the kind and direct basis of its result, and leave another participant a replayable continuation. This is deliberately `relianceBearing`: the evaluator relies on the selected basis, expectation, grounding state, and continuation. Its row count is a test condition, not a general rule for pattern use. The test does not require or assert a wider CGUS.

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
  newlyCurrentSubjectResultClosureFindingRef?: U.EpistemeRef, referencing one PatternUseResultClosureFinding@Context
  preExistingResultGroundingFindingRef?: U.EpistemeRef, referencing one PreExistingResultGroundingFinding@Context
  preExistingGroundingResultClosureFindingRef?: U.EpistemeRef, referencing one PatternUseResultClosureFinding@Context whose EntityOfConcern is that grounding finding
  expectedSubjectResultAbsentInterimResultClosureFindingRef?: U.EpistemeRef, referencing one PatternUseResultClosureFinding@Context
  selectedFirstResultReceivingUseDispositionFindingRef?: U.EpistemeRef, referencing one PatternUseReceivingUseDispositionFinding@Context
  practiceContinuationDescriptionRefs[3..5]: U.EpistemeRef, each referencing one PatternUsePracticeContinuationDescription@Context
  branchOrReturnContinuationDescriptionRef: U.EpistemeRef, referencing one member of practiceContinuationDescriptionRefs
  continuableWorkStateDescriptionRef: U.EpistemeRef
  explicitUnknownDescriptionRef: U.EpistemeRef
  minimalClarificationPatternRef: U.EntityRef, referencing one U.MethodDescription
  expectedClarificationResultKindRef: U.KindRef
  admittedDemonstrativeSliceRef?: U.EpistemeRef, referencing one DemonstrativeUnfoldingSlice@Context
  demonstratedPatternUseRowRefs[3..5]?: U.EpistemeRef, each referencing one DemonstratedPatternUseRow@Context
```

Each practice continuation description states an action or proposed use, the expected result and its kind, the full PatternID and pattern name, and the condition under which that continuation is current. Its `entityOfConcernRef` resolves to the same selected `CandidatePatternUse@Context` as the test result. The test passes only when at least one of the three to five descriptions has `continuationDisposition=branch` or `return`, the final continuable work position is explicit, and one consequential unknown names the minimum clarification pattern and expected clarification-result kind. The selected basis relation resolves to that same candidate; the candidate names the same question and expectation as the test result, and the expectation and test result name the same descriptive flow position.

The practice descriptions remain ordinary PUA epistemes when no wider CGUS is admitted. If a wider CGUS is later admitted, `admittedDemonstrativeSliceRef` and `demonstratedPatternUseRowRefs[3..5]` are both present or both absent. The rows correspond in order to the existing practice descriptions, and each row's `sourcePracticeContinuationDescriptionRef` points to its corresponding description. They do not replace or retype the descriptions, candidate, subject result, or continuable work position.

`SelectedFirstResultGroundingStateValue` is `newlyCurrentSubjectResult | preExistingWithGrounding | expectedSubjectResultAbsent`. Exactly one state branch is filled:

- For `newlyCurrentSubjectResult`, fill `newlyCurrentSubjectResultClosureFindingRef` and leave the other state positions absent. The closure separates result identity or obtaining under the direct owner from the basis that makes it this use's result. A relation occurrence may first obtain through its direct predicate; an evaluation or decision becomes current under its own owner; an actual non-agentive change remains under A.3.4. Cite A.15.PROD only when exact dated Work and its actual changes first constituted an entity under its identity rule.
- For `preExistingWithGrounding`, fill both `preExistingResultGroundingFindingRef` and `preExistingGroundingResultClosureFindingRef` and leave the other state positions absent. The grounding finding names the already-existing entity and its paired grounding relations and owners. Its separate closure uses another category-correct basis to make that finding the exercise's result; a subject-grounding occurrence alone does not. Cite A.15.PROD only if exact dated Work first constituted the finding episteme. The exercise does not produce the pre-existing entity.
- For `expectedSubjectResultAbsent`, fill `expectedSubjectResultAbsentInterimResultClosureFindingRef` and leave the other state positions absent. The interim entity has its own kind, direct owner, exact governed relative object, and category-correct basis. It may support later work but does not satisfy the selected subject-result expectation.

Fill `selectedFirstResultReceivingUseDispositionFindingRef` only when the declared test relies on an addressable realized or intended receiving use. It must point to the selected state-specific closure, including the grounding-finding closure in the pre-existing branch. The continuable-work description says what project work can proceed from this state-specific result. The test fails when it merely retells a card, expands into a whole-project plan, treats a public template as a recommendation, claims performed work without an A.15.1-grounded `U.Work`, infers a physical, clinical, organizational, or learned change from its description, or asserts a CGUS only because the practice contains several rows.

#### E.11.PUA:4.8 - Replay and currentness

For immediate `ordinaryBounded` use, recover from the conversation the working subject and question, the direct pattern inspected, the useful result or honest interim entity, the governed relative-object kind, the category-correct direct basis, and the stop or return. Do not reconstruct a candidate dossier, flow position, or receiver merely to replay a cheap local use.

When a named later use relies on fuller replay, recover the exact EntityOfConcern, effective reference scheme, practical question, selected direct pattern and edition-pinned Solution, expected result kind and direct owner, descriptive flow position, exact governed relative object, category-correct direct basis with its separate governors, grounded actual or honest interim entity, any separately current receiving-use disposition, and stop or return boundary from the support epistemes materialized for that reliance. Add claim scope, project work, model-use structure, qualification window, receiver, or another working condition only through its exact neighboring relation when that relation changes the replayed use.

Recheck the smallest affected claim or relation when the concern, candidate basis, direct Solution, expected result, result grounding, flow position, receiving-use condition, or boundary changes. Reopen pattern selection only when that change alters candidate fit; a new measurement of the same result does not by itself select another pattern. `G.11` governs edition, telemetry, currentness-window, and decay orchestration; PUA supplies the use-specific values and change conditions that orchestration inspects.


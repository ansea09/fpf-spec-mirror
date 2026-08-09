---
chunk_kind: "child"
pattern_id: "E.11.PUA"
pattern_title: "Pattern Use in a Working Situation and First Useful Result"
section_id: "E.11.PUA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUA/E.11.PUA__005_solution.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "E.11.PUA — Pattern Use in a Working Situation and First Useful Result"
  - "E.11.PUA:4 — Solution"
line_start: 77363
line_end: 77734
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

Use one selected pattern through a short result-oriented procedure. Keep the subject result in the foreground; add exact identities or addressable pattern-use records only when ambiguity or a named later reliance needs them.

#### E.11.PUA:4.0 - Cheap first screen before formal work identity

Start with five ordinary values: the working subject, the practical question, the selected pattern's `Solution`, the first useful result or honest blocker, and the stop or return. For a bounded reversible use, those values are sufficient when the result and boundary are truthful.

An FPF pattern supplies action- or judgement-guiding content; a person or another capable system uses that content. The ordinary instructions “use this pattern” and “apply this pattern” are harmless shorthand for that use. Only when the selected `Solution` actually describes a method and that distinction changes the claim, establish its `U.MethodDescription` membership under A.3.2 and identify the admitted `U.Method`. Name a `U.System`, `U.RoleAssignment`, plan, dated `U.Work`, result, or `U.Transformation` only when performer identity, assignment, work occurrence, result production, or transformation is also part of the current claim.

When those identities do matter, keep them separate: the pattern episteme is not the actor or Work; a selected or project-tailored Method is not automatically a WorkPlan; intended work is not performed Work; a result, evidence for it, and a later use are different values. This conditional distinction introduces no universal workflow, causal chain, production relation, TFS, or record requirement.

If the working question is still represented only by a pre-method-selection `TaskSignature`, use that signature to constrain method search; do not treat it as the task, plan, or Work occurrence. Use OEE or NQD to retain Method or architecture candidates before selection, and use `G.5` to declare a selected-set result. For publication, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability. Use `A.3.1` to identify a selected Method and `A.15` for planning and Work. Open these distinctions only when candidate retention, selection, result declaration, publication, planning, or performed Work is current.

#### E.11.PUA:4.1 - The ordinary seven-step use

Before making any pattern-use record, answer aloud: “What exactly do I have now, what is the smallest useful result, and what would make me stop or return?”

1. **Recognize the working situation.** Name the subject or relation in ordinary domain language and ask the current practical question. State an exact kind now only when a nearby kind difference can change the pattern or result.
2. **Inspect one direct pattern.** Read its Problem frame, Problem, Forces, Solution, Consequences, ordinary boundary, and nearest stronger neighbor. Do not select from its title or one trigger word alone.
3. **Say what useful result would answer the question.** Name the entity, obtaining relation, honest interim entity, or blocker plainly enough to distinguish it from a plan, description, recommendation, work occurrence, or nearby value. Name the Method, plan, dated Work, Transformation, evaluation, decision, or later-use object relative to which it is a result only when the phrase depends on that object. Add an exact kind, predicate, pattern locator, `ClaimGraph`, or category-correct basis only when ambiguity or replay makes it necessary.
4. **Use the pattern's `Solution`.** A person or assisting system follows the action guidance under its stated conditions. If the current claim depends on a selected Method, responsible system, assignment, or actual Work, identify those values under A.3/A.15; routine pattern use needs no such expansion. Use A.15.PROD only for a claim that exact dated Work and its actual changes first constituted an entity.
5. **Check what now exists or obtains.** Identify the result under the direct pattern whose content defines, constrains, or tests it. A pre-existing entity may instead receive new grounding for the current question. If the expected subject result still does not exist, name the honest interim result and leave the subject expectation open. Do not turn grounding, planning, evaluation, acceptance, publication, or non-agentive change into production.
6. **State the immediate continuation only as needed.** Name a later use, stronger neighboring pattern, or unresolved clarification in conversation. Materialize an expectation, basis, result, flow, provenance, or boundary episteme only when a named later use needs it to remain addressable.
7. **Stop or return.** Stop when the smallest useful result, honest interim entity, or exact blocker answers the current question at the precision that use needs. Return when the concern, basis, expected entity, direct pattern, relation, or later-use condition changes. A genuine stop needs no receiver.

The practical delta has three honest forms. A new entity or relation occurrence becomes current under its own rule and basis; A.15.PROD enters only for an exact Work-attributed first-constitution claim. A pre-existing entity remains unchanged while a grounding finding becomes adequate for this use. Or the expected subject result remains absent while an honest interim result and return condition become explicit.

#### E.11.PUA:4.2 - Reliance profiles

```text
PatternUseRelianceProfileValue = ordinaryBounded | relianceBearing
```

In `ordinaryBounded` use, the subject, practical question, inspected pattern, useful result or blocker in ordinary language, and stop or return remain recoverable in conversation. State a relative object, exact kind, predicate, pattern locator, `ClaimGraph`, or category-correct direct basis only when it distinguishes the result from a nearby value. No candidate basis, fit record, flow-position record, provenance note, closure record, or receiver is required.

In `relianceBearing` use, materialize only the distinctions that the named reliance will use. Another reader may need a candidate basis and rationale. Automation may need an exact result kind, predicate, pattern locator, `ClaimGraph`, relative object, and category-correct basis. Delayed review may need a descriptive flow position and a separate later-use disposition. A receiver appears only for an actual communication or admitted route relation; an ordinary return needs only its condition and optional next-pattern locator. No profile causes every support record to be materialized.

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
  consideredDirectPatternRef: U.EntityRef, referencing one exact FPF pattern episteme
  patternSelectionDisposition: selected | rejected
  compactFitRationaleRef: U.EpistemeRef
  expectedResultKindRef: U.KindRef
  expectedResultPatternLocator: U.EntityRef, locating one exact FPF pattern episteme
  expectedResultRelativeToObjectKindRef: U.KindRef
  expectedResultRelativeToObjectDescriptionRef: U.EpistemeRef
  expectedResultDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  expectedResultDirectBasisDescriptionRef: U.EpistemeRef
  expectedResultDescriptionRef: U.EpistemeRef
  obtainedResultRef?: U.EntityRef
  obtainedResultKindRef?: U.KindRef
  obtainedResultPatternLocator?: U.EntityRef, locating one exact FPF pattern episteme
  obtainedResultRelativeToObjectRef?: U.EntityRef
  obtainedResultRelativeToObjectKindRef?: U.KindRef
  obtainedResultDirectBasisKind?: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  obtainedResultDirectBasisRef?: U.EntityRef
  obtainedDirectRelationOrBindingPatternLocator?: U.EntityRef, locating the exact FPF pattern episteme whose content defines or constrains the relation or binding
  obtainedLocalClaimDerivationPatternLocator?: U.EntityRef, referencing A.6.RCD
  obtainedLocalClaimBasePredicatePatternLocators[]?: U.EntityRef, each locating one exact FPF pattern episteme whose content defines a base predicate
  boundaryDisposition: stop | reconsider
  boundaryConditionDescriptionRef: U.EpistemeRef
  conditionalNextQuestionPatternLocator?: U.EntityRef, locating one exact FPF pattern episteme
```

The trace is absent from ordinary conversational use. When materialized for a named reliance, C.2.1 identifies it through claim content, exact EntityOfConcern, and effective reference scheme. `claimScopeRef`, `modelUseStructureRef`, and `projectWorkRef` are present only when the exact neighboring relation changes the pattern use; they are not additional episteme-identity fields, and the reference alone does not make that relation obtain.

The expectation names the exact result kind, predicate, defining or constraining `ClaimGraph`, and pattern locator; it also names the kind of Method, plan, dated Work, Transformation, evaluation, decision, or dependent-use object relative to which the result phrase would be true, and one category-correct basis branch. It asserts neither existence nor obtaining. For a selected candidate use, the obtained-result core positions—from `obtainedResultRef` through `obtainedResultDirectBasisRef`—are present together or absent together; a rejected candidate leaves them absent. In the direct-relation branch, the claim graph exposes predicate, participants, applicability, obtaining, occurrence identity, and defining `ClaimGraph`. In the A.6.1 branch, it exposes the operation, application, argument or result binding, and defining `ClaimGraph`. In the local-claim branch, the direct relation-or-binding locator is absent, the A.6.RCD derivation-rule locator and every base-predicate `ClaimGraph` locator are present, and the claim graph exposes polarity, substrate or constructor, base predicates, participants, case facts, and any support or warrant required by the dependent use. The claim episteme does not obtain, and A.6.RCD replaces none of its base predicates.

A reconsideration names `conditionalNextQuestionPatternLocator` only when that continuation is current. A genuine stop leaves the field absent. No receiver is fabricated merely to complete the trace.

#### E.11.PUA:4.2.1 - Admitted support species and rule-content locators

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

The defining `ClaimGraph` located at PUA states the practical-question, optional compact-trace, candidate-basis, candidate-support-episteme, candidate-rationale, result-expectation, result-closure-finding, and dependent-use-disposition-finding schemas. The exact rule content at `E.11` states public-card comparison rationale; `E.11.PUR` states fit, applicability, recommendation, coordination rationale, coordination, and ordering. These relations use A.6.5 SlotSpec discipline; A.6.5 does not define their identity. PUA findings cite the result predicate, defining or constraining `ClaimGraph`, pattern locator, and one category-correct direct basis. In the local-claim branch they keep the A.6.RCD derivation-rule locator distinct from every base-predicate `ClaimGraph` locator. They introduce no result or actual-use relation kind.

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
  relationFunctionClaimRef: U.EntityRef, referencing the exact pattern content that defines or constrains the boundary
  conditionalNextQuestionPatternLocator?: U.EntityRef, locating one exact FPF pattern episteme
  conditionalReceivingPatternPositionKindRef?: U.KindRef
  conditionalReceivingPatternPositionRef?: U.EntityRef

PatternUseResultExpectation@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the CandidatePatternUse@Context whose result is expected
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  expectedResultKindRef: U.KindRef
  expectedResultPatternLocator: U.EntityRef, locating one exact FPF pattern episteme
  expectedResultRelativeToObjectKindRef: U.KindRef
  expectedResultRelativeToObjectDescriptionRef: U.EpistemeRef
  expectedResultDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  expectedResultDirectBasisDescriptionRef: U.EpistemeRef
  expectedResultFlowPosition: patternSelectionFlowResult | selectedPatternApplicationFlowResult | downstreamSubjectWorkFlowResult
  expectedResultDescriptionRef: U.EpistemeRef
  minimumUsableResultBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  intendedUseClaimRef?: U.EpistemeRef, referencing the exact claim that makes the intended continuation current
  intendedReceivingGovernedObjectKindRef?: U.KindRef
  intendedReceivingUseDescriptionRef?: U.EpistemeRef
  dependentUseReconsiderationBoundaryRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The expectation never proves that the result entity exists, that a relation or binding obtains, or that a local claim is true. It first identifies the result kind, predicate, defining or constraining `ClaimGraph`, and pattern locator. It then names which kind of exact Method, plan, dated Work, Transformation, evaluation, decision, or dependent-use object a real closure must identify, and which direct basis would make the readable result phrase true relative to that object. The basis description is branch-specific: relation occurrence; A.6.1 operation-application binding; or A.6.RCD local C.2.1 claim with polarity, substrate or constructor, base predicates and their `ClaimGraph` locators, participants, case facts, and any support or warrant required by the dependent use. The last branch is not an obtaining basis, and the derivation-rule locator is not a substitute for any base predicate.

The flow position is a descriptive PUA role. `intendedUseClaimRef`, `intendedReceivingGovernedObjectKindRef`, `intendedReceivingUseDescriptionRef`, and `dependentUseReconsiderationBoundaryRef` are present together only when an actual continuation or named later reliance is current; otherwise all four are absent. A genuine stop needs no receiver. In a boundary record, `return`, `wrongTurnRecovery`, `strongerNeighbor`, and `receivingPatternContinuation` name conditions and optional next-pattern locators, not receivers; `stop`, `missingGovernor`, and `missingInformation` invent none. Receiving-position kind and ref are both present or both absent. `candidateAdmission` means that Problem frame, Forces, Solution conditions, expected result, category-correct basis template, and ordinary boundary are recoverable enough for further inspection; it is neither an applicability finding nor a selection.

#### E.11.PUA:4.4 - Candidate basis under named reliance

Construct a durable candidate only after inspecting the direct pattern's Problem frame, Problem, Forces, Solution, Consequences, and ordinary boundary. A public README template can supply a reusable starting point, but current project values come from the exact EntityOfConcern, practical question, effective reference scheme, and any current claim-scope, project-work, model-use, qualification-window, or other direct relation named by value.

```text
CandidatePatternUseBasisRelation@Context <: U.Relation:
  publicTemplateRef?: U.EpistemeRef, referencing one PublicCandidatePatternUseTemplate@FPFReadme
  directPatternRef: U.EntityRef, referencing one exact FPF pattern episteme
  directSolutionSectionRef: U.EntityRef, referencing the E.17 PublicationUnit containing the direct pattern's Solution
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  practicalUseQuestionRef: U.EpistemeRef, referencing one PracticalUseQuestion@Context
  problemCardRef?: U.EpistemeRef, referencing one C.22.2 ProblemCard episteme
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
  basisPatternLocator: U.EntityRef, locating the exact FPF pattern episteme whose content defines or constrains the basis relation
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
  problemCardRef?: U.EpistemeRef, referencing one C.22.2 ProblemCard episteme
  publicTemplateRef?: U.EpistemeRef, referencing one PublicCandidatePatternUseTemplate@FPFReadme
  directPatternRef: U.EntityRef, referencing one exact FPF pattern episteme
  directSolutionSectionRef: U.EntityRef, referencing the E.17 PublicationUnit containing the direct pattern's Solution
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  candidateAdmissionBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  returnBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

Each additional basis relation names its exact value, kind, relation signature when current, predicate, defining or constraining `ClaimGraph`, pattern locator, and use in this candidate. The public template is absent when the candidate was formed by direct pattern inspection without a README template. `directSolutionSectionRef` is the Solution section of `directPatternRef`; no redundant solution-MethodDescription ref is retained. A project-tailored MethodDescription is a separate `U.MethodDescription` under A.3.2. If dated Work first constitutes that episteme and the inception claim matters, state the exact A.15.PROD assertion; any derivation or reuse relation to the direct pattern episteme remains separate. Applicability, recommendation, and coordination remain exact E.11.PUR assertions.

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

Candidate rationale has one candidate subject. The `ClaimGraph` located at `E.11.PUR` defines the coordination-rationale schema over a declared candidate set. The `ClaimGraph` located at `E.11` defines the public-card comparison-rationale schema over one public guidance episteme before a project candidate is constructed. No rationale episteme is a universal bag.

#### E.11.PUA:4.5 - Actual-result closure and receiving-use disposition

PUA introduces no actual-result relation and no universal actual-use relation. Keep two questions separate: what establishes, under the applicable identity or predicate rule, that the candidate result entity exists or the relation occurrence obtains; and what category-correct basis makes the readable result phrase true relative to the current Method, plan, dated Work, Transformation, evaluation, decision, or later-use object. One relation occurrence may answer both questions only when the result itself is that occurrence. When a named later use needs addressable closure, materialize a C.2.1 finding that states the result assertion, locates its defining or constraining rule content through the applicable `ClaimGraph` and pattern locator, and records the category-correct basis:

```text
PatternUseResultClosureFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the independently identified result entity or obtaining relation occurrence
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  resultPatternLocator: U.EntityRef, locating the exact FPF pattern episteme whose content defines or constrains the result assertion
  resultRelativeToObjectRef: U.EntityRef
  resultRelativeToObjectKindRef: U.KindRef
  resultDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  resultDirectBasisRef: U.EntityRef
  resultDirectRelationOrBindingPatternLocator?: U.EntityRef, locating the exact FPF pattern episteme whose content defines or constrains the relation or binding
  resultLocalClaimDerivationPatternLocator?: U.EntityRef, referencing A.6.RCD
  resultLocalClaimBasePredicatePatternLocators[]?: U.EntityRef, each locating one exact FPF pattern episteme whose content defines a base predicate
  resultFlowPosition: patternSelectionFlowResult | selectedPatternApplicationFlowResult | downstreamSubjectWorkFlowResult
  resultBearingPathSliceId?: PathSliceId
  resultBearingDesignRunTag?: DesignRunTag
  closureBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The three flow-position values are descriptive PUA roles, not kinds, relations, or occurrence identities. The finding's claim graph names the result entity, its exact predicate, defining or constraining `ClaimGraph`, pattern locator, the object relative to which the result wording is true, and exactly one direct-basis branch. For a direct relation occurrence it names predicate, participants, applicability, obtaining, occurrence identity, and defining `ClaimGraph`. For an A.6.1 binding it names operation, application, argument or result binding, and its defining `ClaimGraph`. For an A.6.RCD local C.2.1 claim, the relation-or-binding locator is absent; the claim ref, polarity, substrate or constructor, base predicates, their `ClaimGraph` locators, participants, case facts, and any support or warrant required by the dependent use are recoverable, with the derivation-rule locator named separately. The claim does not obtain. If the result itself is a relation occurrence, `entityOfConcernRef` and `resultDirectBasisRef` may designate that same occurrence. The closure finding reports those facts; it creates none of them.

Open A.15.PROD only when the closure claims that exact dated Work, through independently identified actual changes and the applicable identity rule, first constituted an entity. A relation occurrence may first obtain through its direct predicate; an evaluation or decision becomes current under its exact subject assertion and defining `ClaimGraph`; a non-agentive change needs no production claim. Completion, evaluation, acceptance, publication, continuation, and later use remain separate. If the claimed result existed already, use `4.6` instead. If no direct basis is recoverable, retain the independently identified entity and return the exact `missingGovernor` or `missingInformation` boundary rather than minting a closure relation.

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
  realizedReceivingUseDirectRelationOrBindingPatternLocator?: U.EntityRef, locating the exact FPF pattern episteme whose content defines or constrains the realized-use relation or binding
  realizedReceivingUseLocalClaimDerivationPatternLocator?: U.EntityRef, referencing A.6.RCD
  realizedReceivingUseLocalClaimBasePredicatePatternLocators[]?: U.EntityRef, each locating one exact FPF pattern episteme whose content defines a base predicate
  intendedUseClaimRef?: U.EpistemeRef, referencing the exact claim that makes the intended continuation current
  intendedReceivingGovernedObjectKindRef?: U.KindRef
  intendedReceivingUseDescriptionRef?: U.EpistemeRef
  receivingUseRealizationConditionRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

In the `realized` state, the later object, kind, direct-basis kind, and basis ref are present; the intended positions are absent. The same branch rule separates a direct relation or A.6.1 pattern locator from the A.6.RCD derivation locator and the direct pattern locators for the local claim's base predicates. The claim graph exposes the exact participants and facts. In `intendedNotYetRealized`, the intended claim, object kind, description, and condition are present together and all realized positions are absent; an intention is not an obtaining-use relation. A stop without a later use has no disposition finding.

When ordinary language says that a result from one TFS is used as an input, tool, context, or constraint in another, treat those words only as cues. Name the exact result-bearing position and exact receiving position—one `FlowPositionRef` for each—plus the direct relation occurrence connecting their participants and its applicable predicate, and keep the result's kind unchanged. With no direct relation kind or predicate, return `missing-governor`; with a predicate but undecided facts, leave the relation open and name the grounding boundary; with a false predicate, assert no occurrence; with an obtaining occurrence but a missing endpoint binding, return `missing-endpoint-binding` and name that binding. Use E.18 for each TFS-local position and local `DesignRunTag`; use E.18.NET only when independently identified TFS values must be treated together as a network. No input, tool, context, constraint, result, or adjacency label supplies the direct relation.

When the thing being called a result is `U.Work`, identify that dated occurrence under A.15.1. Planning, setup, authorization, triggering, or enabling work does not produce that Work. Call the occurrence a result of the selected use in a reliance-bearing closure only when the exact category-correct basis for that reading is present; otherwise keep the Work and the pattern-use description separate.

#### E.11.PUA:4.6 - Pre-existing and still-absent subject results

When the expected entity existed before the current use, the current use may establish a C.2.1 grounding finding about that unchanged entity:

```text
GroundingBasisPair:
  groundingRelationOccurrenceRef: U.EntityRef
  groundingPatternLocator: U.EntityRef, locating the exact FPF pattern episteme whose content defines or constrains the grounding relation

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

Each `GroundingBasisPair` preserves one relation occurrence and the exact pattern content defining or constraining it. The finding's `ClaimGraph` names the grounded proposition and covered subject claim. For a C.2.1 episteme a pair may cite an exact `EpistemeEmpiricalGroundingRelation`; for another subject it uses the direct measurement, observation, evidence-use, diagnostic, or subject predicate that actually grounds that proposition. Inspection, a record, or evidence proximity does not ground the entity by itself. If no direct grounding basis is recoverable, return its exact blocker. The pre-existing entity is not newly produced.

If the current use calls the grounding finding its result, add a separate `PatternUseResultClosureFinding@Context` whose EntityOfConcern is that finding. Its direct basis must connect the finding to the current method, plan, Work, transformation, evaluation, decision, or receiving-use object through a relation occurrence, A.6.1 binding, or category-correct local claim. The occurrence that grounds the pre-existing subject does not by itself make the grounding finding a result of the current use. Cite A.15.PROD only when exact dated Work and its actual changes first constituted the finding episteme.

In reliance-bearing use, when the expected subject result still does not exist, close the current use only on an interim `PatternUseResultClosureFinding@Context`. Identify that interim entity under its own kind and rule, and record the category-correct basis that makes it the current use's result relative to the current object. Keep the subject-result expectation open. A machining plan does not become a machined component; a treatment recommendation does not become a changed clinical state; an assessment plan does not become learned capability.

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
  minimalClarificationPatternRef: U.EntityRef, referencing one exact FPF pattern episteme
  expectedClarificationResultKindRef: U.KindRef
  admittedDemonstrativeSliceRef?: U.EpistemeRef, referencing one DemonstrativeUnfoldingSlice@Context
  demonstratedPatternUseRowRefs[3..5]?: U.EpistemeRef, each referencing one DemonstratedPatternUseRow@Context
```

Each practice continuation description states an action or proposed use, the expected result and its kind, the full PatternID and pattern name, and the condition under which that continuation is current. Its `entityOfConcernRef` resolves to the same selected `CandidatePatternUse@Context` as the test result. The test passes only when at least one of the three to five descriptions has `continuationDisposition=branch` or `return`, the final continuable work position is explicit, and one consequential unknown names the minimum clarification pattern and expected clarification-result kind. The selected basis relation resolves to that same candidate; the candidate names the same question and expectation as the test result, and the expectation and test result name the same descriptive flow position.

The practice descriptions remain ordinary PUA epistemes when no wider CGUS is admitted. If a wider CGUS is later admitted, `admittedDemonstrativeSliceRef` and `demonstratedPatternUseRowRefs[3..5]` are both present or both absent. The rows correspond in order to the existing practice descriptions, and each row's `sourcePracticeContinuationDescriptionRef` points to its corresponding description. They do not replace or retype the descriptions, candidate, subject result, or continuable work position.

`SelectedFirstResultGroundingStateValue` is `newlyCurrentSubjectResult | preExistingWithGrounding | expectedSubjectResultAbsent`. Exactly one state branch is filled:

- For `newlyCurrentSubjectResult`, fill `newlyCurrentSubjectResultClosureFindingRef` and leave the other state positions absent. The closure separates the rule under which the result exists or the relation obtains from the basis that makes it this use's result. A relation occurrence may first obtain through its direct predicate; an evaluation or decision becomes current under its own rule; an actual non-agentive change remains under A.3.4. Cite A.15.PROD only when exact dated Work and its actual changes first constituted an entity under its identity rule.
- For `preExistingWithGrounding`, fill both `preExistingResultGroundingFindingRef` and `preExistingGroundingResultClosureFindingRef` and leave the other state positions absent. The grounding finding names the already-existing entity, its paired grounding relation occurrences, and the exact pattern content that defines or constrains each relation. Its separate closure uses another category-correct basis to make that finding the exercise's result; a subject-grounding occurrence alone does not. Cite A.15.PROD only if exact dated Work first constituted the finding episteme. The exercise does not produce the pre-existing entity.
- For `expectedSubjectResultAbsent`, fill `expectedSubjectResultAbsentInterimResultClosureFindingRef` and leave the other state positions absent. The interim entity keeps its own kind and rule; the closure records the relative object and category-correct basis required by this reliance. It may support later work but does not satisfy the selected subject-result expectation.

Fill `selectedFirstResultReceivingUseDispositionFindingRef` only when the declared test relies on an addressable realized or intended receiving use. It must point to the selected state-specific closure, including the grounding-finding closure in the pre-existing branch. The continuable-work description says what project work can proceed from this state-specific result. The test fails when it merely retells a card, expands into a whole-project plan, treats a public template as a recommendation, claims performed work without an A.15.1-grounded `U.Work`, infers a physical, clinical, organizational, or learned change from its description, or asserts a CGUS only because the practice contains several rows.

#### E.11.PUA:4.8 - Replay and currentness

For immediate `ordinaryBounded` use, recover from the conversation the working subject and question, the direct pattern inspected, the useful result, honest interim entity, or blocker, and the stop or return. Recover a relative-object kind, exact predicate, pattern locator, `ClaimGraph`, or category-correct direct basis only when it changes the truth, distinguishes a nearby value, or is needed by a named reliance. Do not reconstruct a candidate dossier, flow position, or receiver merely to replay a cheap local use.

When a named later use relies on fuller replay, recover the exact EntityOfConcern, effective reference scheme, practical question, selected direct pattern and edition-pinned `Solution`, expected result kind and pattern locator, descriptive flow position, relative object, category-correct direct basis, grounded actual or honest interim entity, any separately current later-use disposition, and stop or return boundary from the support epistemes materialized for that reliance. Add claim scope, project work, model-use structure, qualification window, receiver, or another working condition only through its exact neighboring relation when that relation changes the replayed use.

Recheck the smallest affected claim or relation when the concern, candidate basis, direct Solution, expected result, result grounding, flow position, receiving-use condition, or boundary changes. Reopen pattern selection only when that change alters candidate fit; a new measurement of the same result does not by itself select another pattern. `G.11` governs edition, telemetry, currentness-window, and decay orchestration; PUA supplies the use-specific values and change conditions that orchestration inspects.


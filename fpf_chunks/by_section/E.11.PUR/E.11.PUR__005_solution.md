---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__005_solution.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:4 — Solution"
line_start: 76403
line_end: 76542
dependencies:
  - "A.15"
  - "A.19"
  - "A.19.CPM"
  - "A.19.ECS"
  - "A.21"
  - "A.6.5"
  - "C.22.PFR"
  - "C.24"
  - "C.30"
  - "E.10.MOVE"
  - "E.11"
  - "E.11.PUA"
  - "E.18"
  - "E.18.1"
  - "G.11"
keywords:
---

### E.11.PUR:4 - Solution

Evaluate candidate uses against five distinct fit aspects. An ordinary reversible judgement may remain conversational: keep the aspects in one compact rationale, state the aggregate applicability, then recommend by expected first result and live alternatives. Materialize separate findings or a recommendation episteme only when a named later use needs addressable support. Coordinate several candidates with an explicit local ordering mode and add pairwise precedence only where a real basis exists.

#### E.11.PUR:4.1 - Fit and applicability

```text
PatternUseFitCriterionValue =
  problemFrame | forces | solutionConditions | ordinaryBoundary | resultAndReceivingUse

PatternUseFitResultValue = fit | misfit | insufficientBasis
PatternUseApplicabilityResultValue = applicable | inapplicable | insufficientBasis

PatternUseFitFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one CandidatePatternUse@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  fitCriterion: PatternUseFitCriterionValue
  fitResult: PatternUseFitResultValue
  fitRationaleRef: U.EpistemeRef, referencing one CandidatePatternUseRationale@Context

PatternUseApplicabilityFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one CandidatePatternUse@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  fitFindingRefs[5]: U.EpistemeRef, each referencing one PatternUseFitFinding@Context
  applicabilityResult: PatternUseApplicabilityResultValue
  missingBasisBoundaryRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The five criteria refer to one candidate. In ordinary conversation, inspect all five and state the aggregate result in the recommendation without materializing five findings. `PatternUseApplicabilityFinding@Context` is the reliance-bearing support episteme: when it exists, its five findings cover each criterion exactly once. `applicable` follows only when all five are `fit`; any `misfit` yields `inapplicable`; one or more `insufficientBasis` values yield `insufficientBasis` and a missing-basis boundary.

`problemFrame` compares the candidate pattern's Problem frame with the current concern; it does not assert that an actual Problem obtains. When an actual Problem is relied on, cite one current C.22.PFR `ProblematicForRelation` occurrence with its exact actual-condition and criterion-applicability participants and adverse-episode identity. A ProblemCard, fit finding, assessment, or recommendation may support a claim about that occurrence but neither creates nor splits it.

#### E.11.PUR:4.2 - Recommendation

State the ordinary recommendation first: which candidate is applicable, why its expected first result serves the current concern better than the live alternatives, and where to stop or return. If the judgement is local, reversible, and has no named later reliance, that readable statement is sufficient.

When the recommendation must remain addressable, use the schema below. `ordinaryCompact` keeps one compact rationale and no five-finding dossier; `relianceBearing` adds the current applicability finding only because a named later use needs independent replay.

```text
PatternUseRecommendationSupportProfileValue = ordinaryCompact | relianceBearing

PatternUseRecommendation@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the selected CandidatePatternUse@Context
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  recommendationSupportProfile: PatternUseRecommendationSupportProfileValue
  applicabilityResult: PatternUseApplicabilityResultValue
  compactApplicabilityAndSelectionRationaleRef: U.EpistemeRef, referencing one CandidatePatternUseRationale@Context
  applicabilityFindingRef?: U.EpistemeRef, referencing one PatternUseApplicabilityFinding@Context
  expectedResultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  strongerNeighborPatternRef?: U.EntityRef, referencing the exact neighboring FPF pattern episteme only when its identity changes the recommendation
  recommendationBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

Recommendation selects one applicable candidate for the current concern because its expected first result serves that concern better than the live alternatives and, when a receiving use is current, supports that use under the stated rationale. A conversational judgement needs no record. In an addressable `ordinaryCompact` recommendation, the applicability result and compact rationale are carried directly and `applicabilityFindingRef` is absent. In `relianceBearing`, the same recommendation also cites one current applicability finding whose five fit findings can be replayed independently. The profile changes support cardinality, not the recommendation kind or authority.

When an addressable recommendation is materialized, `expectedResultExpectationRef` points to its exact E.11.PUA expectation. It identifies the expected result and only the pattern, relative-object, or category-correct basis distinctions that expectation actually uses; it does not assert that the result exists or that any relation, A.6.1 binding, or local claim is current. A recommendation does not authorize work, establish a gate, prove evidence sufficiency, create the expected result, or supply its later closure.

When a stronger neighboring pattern better addresses the current question, name it and state the return condition. Populate `strongerNeighborPatternRef` only when the exact pattern identity matters to an addressable recommendation. The reference does not establish formal `U.MethodDescription` membership; such membership requires its own A.3.2 basis. Familiarity with the current candidate is not a recommendation reason.

#### E.11.PUR:4.3 - Coordination without forced order

For ordinary local coordination, state the candidates, whether they are unordered, partially ordered, or totally ordered, any real precedence basis, and the stop boundary in readable prose. Materialize the rationale, coordination episteme, and any pairwise ordering relations only when a named later use needs that coordination to remain addressable.

```text
PatternUseOrderingModeValue = unordered | partialOrder | totalOrder

PatternUseCoordinationRationale@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the coordination-question episteme
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  subjectCandidatePatternUseRefs[2..*]: U.EpistemeRef, each referencing one CandidatePatternUse@Context
  coordinationRationaleDescriptionRef: U.EpistemeRef
  rationaleBasisEpistemeRefs[]: U.EpistemeRef
  coordinationBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context

PatternUseCoordination@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the coordination-question episteme
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  memberCandidatePatternUseRefs[2..*]: U.EpistemeRef, each referencing one CandidatePatternUse@Context
  orderingMode: PatternUseOrderingModeValue
  orderingRelationRefs[]?: U.EntityRef, each referencing one PatternUseOrderingRelation@Context
  coordinationRationaleRef: U.EpistemeRef, referencing one PatternUseCoordinationRationale@Context
  stopBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

`unordered` has no ordering relations. `partialOrder` and `totalOrder` use explicit pairwise relations. A total order is the bounded `PatternUseSequence@Context` specialization under its named receiving use; it is not a universal route or project WorkPlan.

#### E.11.PUR:4.4 - Pairwise precedence

```text
PatternUsePrecedenceBasisValue =
  prerequisiteResult | methodPrecondition | sharedConstraintResolution

PatternUseOrderingRelation@Context <: U.Relation:
  coordinationRef: U.EpistemeRef, referencing one PatternUseCoordination@Context
  prerequisiteCandidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  dependentCandidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  precedenceBasis: PatternUsePrecedenceBasisValue
  precedenceBasisResultExpectationRef?: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  precedenceBasisResultClosureFindingRef?: U.EpistemeRef, referencing one current PatternUseResultClosureFinding@Context
  precedenceConditionRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  orderingRationaleRef: U.EpistemeRef, referencing one PatternUseCoordinationRationale@Context
  RelationRefKind: U.EntityRef
  Direction: prerequisiteCandidatePatternUseRef -> dependentCandidatePatternUseRef
  Dependence: local to coordinationRef, both candidate editions, the precedence basis and condition, and any current result-closure support to coordinationRef and both candidate editions
  Identity: <coordinationRef, prerequisiteCandidatePatternUseRef, dependentCandidatePatternUseRef, precedenceBasis, precedenceConditionRef>
```

The prerequisite and dependent candidates are different members of the same coordination relation. When `precedenceBasis=prerequisiteResult`, both result references are present. `precedenceBasisResultExpectationRef` equals the prerequisite candidate's exact expectation. `precedenceBasisResultClosureFindingRef` resolves to that same candidate and expectation and reports the independently identified result or obtaining relation plus the category-correct basis that makes the precedence claim true. Predicate, pattern locator, `ClaimGraph`, Method, plan, dated Work, Transformation, evaluation, decision, or later-use object appear only when the cited closure actually depends on them. The ordering relation copies none of those fields.

The closure finding is a C.2.1 episteme and creates neither the result nor the ordering relation. The ordering relation obtains only while its `precedenceConditionRef` is satisfied by the result and category-correct basis reported there. A missing relation rule or information, false predicate, or absent operation binding leaves the precedence relation non-obtaining and the dependent use at its return boundary. For `methodPrecondition` and `sharedConstraintResolution`, both result-reference positions are absent.
The dependent candidate use is admitted under a precedence relation only after its precedence basis is established. Page order, seminar order, identifier order, or visual adjacency does not create that relation.

#### E.11.PUR:4.5 - Practical procedure

1. Recover each candidate's current concern, direct pattern, Solution, expectation, and ordinary boundary.
2. Keep a local reversible applicability, recommendation, or coordination judgement conversational when no named later reliance needs it. When a recommendation must remain addressable, choose `ordinaryCompact` unless that reliance needs the fit aspects separately addressable; use `relianceBearing` only for that reliance.
3. Inspect all five fit aspects. In ordinary use, keep them in one compact rationale. Under named reliance, materialize five separate findings and one applicability finding.
4. State the aggregate applicability result directly in the recommendation; when a reliance-bearing applicability finding exists, the two result values agree.
5. Recommend an applicable candidate only when its expected result serves the current concern better than the live alternatives; include a receiving use only when one is current. The expectation is not an achieved result.
6. Coordinate several candidates as unordered, partially ordered, or totally ordered. Add a pairwise relation only when one declared precedence basis is current. For `prerequisiteResult`, require the prerequisite candidate's exact expectation and one current E.11.PUA result-closure finding with the complete direct basis.
7. Stop at the recommendation or coordination result. A Plain *next move* names only the recommended pattern use or conditional continuation. Continue to PUA, P2W, planning, gate, decision, or work only when that next claim becomes current.

#### E.11.PUR:4.6 - Replay and currentness

Replay an ordinary conversational or addressable compact recommendation from the current concern, inspected candidate pattern and `Solution`, aggregate applicability, compact rationale over all five aspects, live alternatives, expected result, any current receiving use, and recommendation boundary. Replay a reliance-bearing recommendation from those same positions plus the current applicability finding and its five fit findings. Replay coordination from its inspected candidate uses, question, ordering mode, any pairwise precedence and bases, stop boundary, and, for each `prerequisiteResult` relation, the exact expectation and current E.11.PUA closure finding.

Recheck the smallest affected finding or relation when a candidate `Solution`, result expectation, result entity, relative object, direct basis or defining `ClaimGraph`, fit basis, live alternative, dependent use, coordination member, precedence basis, condition, or boundary changes. A changed candidate fit reopens its applicability and any recommendation that relied on it. A changed prerequisite expectation or closure reopens only the affected ordering relations and their dependent uses unless the coordination question or membership also changed. Separate G.11 assertions state edition, telemetry, currentness-window, and decay facts; PUR supplies the judgment-specific values and change conditions.


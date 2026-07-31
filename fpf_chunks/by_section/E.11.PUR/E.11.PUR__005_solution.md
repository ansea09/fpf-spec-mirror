---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__005_solution.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:4 — Solution"
line_start: 76543
line_end: 76672
dependencies:
  - "A.15"
  - "A.19"
  - "A.19.ECS"
  - "A.21"
  - "A.6.5"
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

Evaluate candidate uses against five distinct fit aspects. Keep those aspects in one compact rationale for ordinary bounded use. Materialize separate findings only when a named receiving reliance needs them. Aggregate applicability before issuing a recommendation. Coordinate several candidates with an explicit local ordering mode and pairwise precedence relations only where a real basis exists.

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

#### E.11.PUR:4.2 - Recommendation

```text
PatternUseRecommendationSupportProfileValue = ordinaryCompact | relianceBearing

PatternUseRecommendation@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
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
  strongerNeighborPatternRef?: U.EntityRef, referencing one U.MethodDescription
  recommendationBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

Recommendation selects one applicable candidate for the current concern because its expected result and receiving use are preferable under the stated rationale. In `ordinaryCompact`, the applicability result and compact rationale are carried directly and `applicabilityFindingRef` is absent. In `relianceBearing`, the same recommendation also cites one current applicability finding whose five fit findings can be replayed independently. The profile changes support cardinality, not the recommendation kind or authority. A recommendation does not authorize work, establish a gate, prove evidence sufficiency, or create the expected result.

When a stronger neighboring pattern better addresses the current question, name it and use the recommendation boundary to return. Familiarity with the current candidate is not a recommendation basis.

#### E.11.PUR:4.3 - Coordination without forced order

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
  boundedContextRef: U.BoundedContextRef
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
  precedenceConditionRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  orderingRationaleRef: U.EpistemeRef, referencing one PatternUseCoordinationRationale@Context
  RelationRefKind: U.EntityRef
  Direction: prerequisiteCandidatePatternUseRef -> dependentCandidatePatternUseRef
  Dependence: bounded-context local to coordinationRef and both candidate editions
  Identity: <coordinationRef, prerequisiteCandidatePatternUseRef, dependentCandidatePatternUseRef, precedenceBasis, precedenceConditionRef>
```

The prerequisite and dependent candidates are different members of the same coordination relation. When `precedenceBasis=prerequisiteResult`, `precedenceBasisResultExpectationRef` is present and equals the prerequisite candidate's exact result expectation. The ordering relation never copies result kind or relation-signature slots. For `methodPrecondition` and `sharedConstraintResolution`, the result-expectation position is absent.

The dependent candidate use is admitted under a precedence relation only after its precedence basis is established. Page order, seminar order, identifier order, or visual adjacency does not create that relation.

#### E.11.PUR:4.5 - Practical procedure

1. Recover each candidate's current concern, direct pattern, Solution, expectation, and ordinary boundary.
2. Choose `ordinaryCompact` unless a named receiving use needs the fit aspects to remain independently addressable; use `relianceBearing` only for that reliance.
3. Inspect all five fit aspects. In ordinary use, keep them in one compact rationale. Under named reliance, materialize five separate findings and one applicability finding.
4. State the aggregate applicability result directly in the recommendation; when a reliance-bearing applicability finding exists, the two result values agree.
5. Recommend an applicable candidate only when its result and receiving use answer the current concern better than the live alternatives.
6. Coordinate several candidates as unordered, partially ordered, or totally ordered. Add a pairwise relation only when one declared precedence basis is current.
7. Stop at the recommendation or coordination result. Continue to PUA, P2W, planning, gate, decision, or work only when that next claim becomes current.

#### E.11.PUR:4.6 - Replay and currentness

Replay an ordinary compact recommendation from its candidate, applicability result, compact rationale over all five aspects, current live alternatives, expected result and receiving use, and recommendation boundary. Replay a reliance-bearing recommendation from those same positions plus the current applicability finding and its five fit findings. Replay coordination from its members, question, ordering mode, pairwise relations, precedence bases, and stop boundary.

Recheck the smallest affected finding or relation when a candidate `Solution`, result expectation, fit basis, live alternative, receiving use, coordination member, precedence basis, or boundary changes. A changed candidate fit reopens its applicability and any recommendation that relied on it. A changed prerequisite expectation reopens only the affected ordering relations and their dependent uses unless the coordination question or membership also changed. `G.11` governs edition, telemetry, currentness-window, and decay orchestration; PUR supplies the judgement-specific values and change conditions.


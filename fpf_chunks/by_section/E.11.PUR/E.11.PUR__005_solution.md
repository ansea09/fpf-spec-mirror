---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__005_solution.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:4 — Solution"
line_start: 88874
line_end: 89044
dependencies:
  - "A.10"
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

Evaluate candidate uses against five distinct fit aspects. An ordinary reversible judgement may remain conversational: keep the aspects in one compact rationale, state the aggregate applicability when the current question needs it, then compare the expected receiving value and full burden of the serious continuations, including continuing without a new pattern use. Before repeating a recommended use, apply the result-reuse branch in `4.2.1`. Materialize separate findings or a recommendation episteme only when a named later use needs addressable support. Coordinate several candidates with an explicit local ordering mode and add pairwise precedence only where a real basis exists.

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

The five criteria refer to one candidate. When its basis must be addressable, consume PUA §4.4's ordinary C.2.1 claim about that candidate and its exact supporting claims, relations or evidence uses; no candidate-basis U.Relation is required. A contradicted product-law premise and missing dependence information remain distinct inputs to these fit tests. In ordinary conversation, inspect all five without materializing five findings. State the aggregate applicability when it answers the current question; if the later comparison supports a recommendation, carry that result into the recommendation. `PatternUseApplicabilityFinding@Context` is the reliance-bearing support episteme: when it exists, its five findings cover each criterion exactly once. Use mutually exclusive branches: any `misfit` yields `inapplicable`, including when another aspect has `insufficientBasis`; with no `misfit`, one or more `insufficientBasis` values yield `insufficientBasis` and a missing-basis boundary; otherwise all five are `fit` and the result is `applicable`.

A known `misfit` settles this candidate's applicability under the inspected conditions. Do not obtain more information merely to fill the remaining aspects when it cannot change that answer. If changing the failed condition is a serious continuation, appraise that change separately and reconsider the affected fit under `4.6`. A different candidate may still be applicable and worth recommending.

`problemFrame` compares the candidate pattern's Problem frame with the current concern; it does not assert that an actual Problem obtains. When an actual Problem is relied on, cite one current C.22.PFR `ProblematicForRelation` occurrence with its exact actual-condition and criterion-applicability participants and adverse-episode identity. A ProblemCard, fit finding, assessment, or recommendation may support a claim about that occurrence but neither creates nor splits it.

#### E.11.PUR:4.2 - Recommendation

Before recommending a new pattern use, compare its full receiving value and burden with the other serious continuations, including continuing the present work without it. Use C.11.DUA when the worth of the advice, its presentation or its interaction with other proposed changes is unclear. Applicability can coexist with no worthwhile recommendation now. In that case, finish without selecting a pattern use or materializing a positive recommendation; give a short reason only when the current question or later reliance needs it. Continuing without optional advice does not remove an existing obligation.

When the comparison supports a recommendation, state which candidate is applicable, why its expected first result warrants its full burden for the current concern, and where to stop or return. If the judgement is local, reversible, and has no named later reliance, that readable statement is sufficient.

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

Recommendation selects one applicable candidate because its expected receiving value warrants its full burden compared with the other serious continuations, including continuing without a new use, and, when a receiving use is current, supports that use under the stated rationale. A conversational judgement needs no record. In an addressable `ordinaryCompact` recommendation, the applicability result and compact rationale are carried directly and `applicabilityFindingRef` is absent. In `relianceBearing`, the same recommendation also cites one current applicability finding whose five fit findings can be replayed independently. The profile changes support cardinality, not the recommendation kind or authority.

When an addressable recommendation is materialized, `expectedResultExpectationRef` points to its exact E.11.PUA expectation. It identifies the expected result and only the pattern, relative-object, or category-correct basis distinctions that expectation actually uses; it does not assert that the result exists or that any relation, A.6.1 binding, or local claim is current. A recommendation does not authorize work, establish a gate, prove evidence sufficiency, create the expected result, or supply its later closure.

When a stronger neighboring pattern better addresses the current question, name it and state the return condition. Populate `strongerNeighborPatternRef` only when the exact pattern identity matters to an addressable recommendation. The reference does not establish formal `U.MethodDescription` membership; such membership requires its own A.3.2 basis. Familiarity with the current candidate is not a recommendation reason.

#### E.11.PUR:4.2.1 - Reuse an earlier result when it still answers the concern

After identifying an applicable candidate use, ask whether an earlier result episteme already answers the present concern. Use the pattern that defines or tests that result to compare:

- the result episteme's `EntityOfConcern` and edition;
- the question answered and declared use;
- the source and dependency conditions on which the answer relies; and
- its qualification and currentness boundary.

When those values still match, cite and use the earlier result. Use `A.10` when a named claim or bounded action relies on that result and the source-to-use account is still implicit. Add a dated `U.Work` occurrence only when that Work is itself a current claim. Use `G.11` when currentness or refresh changes the use. Stop without repeating the same pattern use or copying the result under another stage name.

When one value changed, reopen the smallest affected result question under the pattern that defines or tests that result. Repeat the complete pattern use only when the unaffected reach cannot be established. If the applicable pattern supplies no basis for comparing the earlier result with the present concern, stop at `insufficient result-comparison basis`.

The candidate pattern use, the earlier result episteme, a later reliance relation, a currentness assertion, and later Work remain separate. This branch introduces no generic result-reuse relation.

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

`unordered` has no ordering relations. `partialOrder` and `totalOrder` use explicit pairwise relations. A total order is the bounded `PatternUseSequence@Context` specialization under its named receiving use; it is not a universal route or project WorkPlan. Treat the declared pairwise precedence as strict: its transitive closure must be irreflexive. A `totalOrder` additionally compares every pair of distinct members. A cycle or unresolved required pair blocks that ordering claim; preserve the known dependencies and state the unresolved coordination question.

#### E.11.PUR:4.4 - Pairwise precedence

A pairwise precedence relation is an applicable directed constraint between two exact candidate uses for the governed coordination question. It can obtain before either is performed. Establish its branch predicate:

* **prerequisiteResult:** the dependent use's direct rule requires exact content, and the coordination has a stated basis for selecting this prerequisite use to supply it. Cite that rule, content and selection basis together with the prerequisite candidate's exact expectation. Matching output kinds alone is insufficient. The result need not yet exist for the dependency to obtain.
* **methodPrecondition:** performing the dependent use first would invalidate a condition that the prerequisite use actually needs, and the proposed order preserves that condition. Name both uses and the condition; unary candidate fit alone supplies no pair.
* **sharedConstraintResolution:** an applicable schedule or priority rule selects this direction to resolve the actual shared constraint. Shared-resource exclusion alone establishes conflict, not A-before-B. A rule selecting B-before-A defeats the proposed A-before-B claim.

```text
PatternUsePrecedenceBasisValue =
  prerequisiteResult | methodPrecondition | sharedConstraintResolution

PatternUseOrderingRelation@Context <: U.Relation:
  coordinationRef: U.EpistemeRef, describing the governed coordination question
  prerequisiteCandidatePatternUseRef: U.EpistemeRef
  dependentCandidatePatternUseRef: U.EpistemeRef
  precedenceBasis: PatternUsePrecedenceBasisValue
  precedenceBasisResultExpectationRef?: U.EpistemeRef  // prerequisiteResult only
  requiredContentAndSelectedSupplierBasis?:  // prerequisiteResult only
  precedenceConditionRef: U.EpistemeRef, describing the applicable semantic condition
  constitutiveOrderingRuleRef?: exact schedule or priority rule when it constitutes this order
  orderingRationaleRef: U.EpistemeRef
  Direction: prerequisiteCandidatePatternUseRef -> dependentCandidatePatternUseRef
```

The candidates are distinct members of the coordination. The relation obtains while the applicable branch predicate holds for those candidates, the governed question and semantic condition. A known false branch condition establishes non-obtaining; a missing rule or needed case fact leaves it unresolved. An unmet prerequisite result is not a false dependency condition: it concerns readiness below.

**Identity and extent.** Keep the same dependency for the same exact candidates, governed coordination use, branch and meaning of its precedence condition, including any genuinely constitutive schedule/priority rule. A different rendering, witness or descriptive coordination episteme alone changes none of those values. A changed candidate or meaning-changing condition/rule requires a new relation claim and identity assessment; the record reference is not itself the identity law. Within a temporally qualified use, the occurrence lasts while that branch predicate holds; a gap where it ceases to hold ends the occurrence, and a later re-established occurrence has a new extent. Omit temporal machinery for an atemporal constraint.

**Readiness is a separate claim.** For prerequisite-result continuation, identify a current E.11.PUA result-closure finding and the actual result and category-correct basis that satisfy the required content and receiving conditions. The closure may concern the prerequisite use or an adequate earlier result reused under §4.2.1. State readiness/applicability for this continuation as its own ordinary C.2.1 claim. A known unmet condition means not ready; missing information leaves readiness unresolved. An expectation, ordering edge or closure record's presence alone supplies no achieved result.

The dependency is not an instruction to repeat a use whose adequate earlier result is already available. Apply the result-reuse exit before proposing execution. A changed closure can change readiness without changing the prospective dependency. No ordering or readiness claim authorizes Work. Page, seminar, identifier and display order do not establish a dependency.

#### E.11.PUR:4.5 - Practical procedure

1. Recover each candidate's current concern, direct pattern, Solution, expectation, and ordinary boundary.
2. Keep a local reversible applicability, recommendation, or coordination judgement conversational when no named later reliance needs it. When a recommendation must remain addressable, choose `ordinaryCompact` unless that reliance needs the fit aspects separately addressable; use `relianceBearing` only for that reliance.
3. Inspect all five fit aspects. In ordinary use, keep them in one compact rationale. Under `relianceBearing`, materialize five separate findings and one applicability finding.
4. Establish the aggregate applicability under `4.1`. A known `misfit` ends the applicability inquiry for that candidate under the inspected conditions. If the aggregate is `insufficientBasis`, obtain missing information only when an attainable answer can change a worthwhile continuation; otherwise return the missing-basis boundary. State the aggregate separately when the current question needs it. If step 5 supports a recommendation, include it there; when a reliance-bearing applicability finding exists, the two result values agree.
5. Compare an applicable candidate with the other serious continuations, including continuing the present work without a new pattern use. Recommend it only when its expected receiving value warrants its full burden; use C.11.DUA when that judgement is unclear. Finish without a positive recommendation when no candidate warrants one. The expectation is not an achieved result.
6. Before repeating a recommended use, compare any earlier result through `4.2.1`. Reuse a matching result or reopen only the affected result question.
7. Coordinate several candidates as unordered, partially ordered, or totally ordered. Establish each needed pair under §4.4's branch predicate. For prerequisiteResult, name exact required content, the selected supplier-use basis and its expectation. Then assess current readiness separately from actual closure, reusing an adequate earlier result before requiring another use.
8. Stop at the applicability answer or missing-basis boundary, recommendation, matching earlier result, coordination result, or conclusion that no new use is worth recommending now. The last outcome selects no candidate and requires no refusal document; it leaves existing obligations in force. A Plain *next move*, when one is useful, names only the recommended pattern use or conditional continuation. Continue to PUA, P2W, planning, gate, decision, or work only when that next claim becomes current.

#### E.11.PUR:4.6 - Replay and currentness

Replay an ordinary conversational or addressable compact recommendation from the current concern, inspected candidate pattern and `Solution`, aggregate applicability, compact rationale over all five aspects, serious continuations considered, expected result and full burden, any current receiving use, and recommendation boundary. Replay a reliance-bearing recommendation from those same positions plus the current applicability finding and its five fit findings. Replay coordination from its inspected candidate uses, question, ordering mode, any pairwise precedence and bases, stop boundary, and, for each `prerequisiteResult` relation, the exact expectation, required content and selected supplier-use basis. Replay a readiness claim separately from the actual result closure, receiving conditions and any earlier-result reuse.

When a later use needs to replay a conclusion without a recommendation, recover the concern, the serious continuations, the value and burden that mattered, and the condition for reconsideration. No selected-candidate reference or five-finding dossier is required for that conclusion.

Replay a result-reuse stop from the earlier result episteme and edition, the question and declared use, relied source and dependency conditions, qualification and currentness boundary, and any separately current A.10 reliance or G.11 assertion.

Recheck the smallest affected finding, result question, or relation when a candidate `Solution`, result expectation, result entity or edition, relative object, direct basis or defining `ClaimGraph`, relied source or dependency condition, qualification or currentness boundary, fit basis, value or burden, alternative under consideration, dependent use, coordination member, precedence basis, condition, or boundary changes. A changed candidate fit reopens its applicability and any recommendation that relied on it. A changed earlier result condition reopens only the affected result question and later uses unless the candidate or present concern also changed. A changed prerequisite expectation or semantic precedence condition reopens the affected dependency and dependent use. A changed closure reopens readiness and only dependencies whose semantic basis also changed. A changed witness or rendering alone creates no new dependency. Recheck a genuinely constitutive schedule/priority rule when it changes. Separate G.11 assertions state edition, telemetry, currentness-window, and decay facts; PUR supplies the judgement-specific values and change conditions.


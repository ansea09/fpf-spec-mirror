---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__005_solution.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:4 — Solution"
line_start: 111132
line_end: 111372
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

Evaluate candidate uses against five fit aspects. An ordinary reversible judgement may remain conversational: keep the aspects in one compact rationale, state the aggregate applicability when the current question needs it, then compare the expected receiving value and full burden of the serious continuations, including continuing without a new pattern use.

Before repeating a recommended use, apply the result-reuse branch in `4.2.1`. Materialize separate findings or a recommendation episteme only when a named later use needs addressable support.

When coordinating several candidates, recover the result their use together must support. Specify order where one use requires something from another. Also identify any common condition or compatibility on which the result depends, including when either use can come first.

#### E.11.PUR:4.1 - Fit and applicability

In the optional forms below, `claimGraph` carries the episteme's complete asserted content, including the reasons and qualifications that change what it says. The scheme designation resolves under C.2.1:4.2.6 to the rules governing that account. It can select another episteme's effective scheme or exact content defining those rules; a reference to a document alone does not choose between them.

Preserve an unresolved interpretation rather than filling the field with a nearby name. These forms organize addressable writing when needed; ordinary conversation and partial notes remain sufficient under the entry conditions above.

```text
PatternUseFitCriterionValue =
  problemFrame | forces | solutionConditions | ordinaryBoundary | resultAndReceivingUse

PatternUseFitResultValue = fit | misfit | insufficientBasis
PatternUseApplicabilityResultValue = applicable | inapplicable | insufficientBasis

PatternUseFitFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one CandidatePatternUse@Context
  claimGraph: exact whole C.2.1 claim content, by value
  schemeDesignation: C.2.1 SchemeDesignation
  editionId
  fitCriterion: PatternUseFitCriterionValue
  fitResult: PatternUseFitResultValue
  fitRationaleRef: U.EpistemeRef, referencing one CandidatePatternUseRationale@Context

PatternUseApplicabilityFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one CandidatePatternUse@Context
  claimGraph: exact whole C.2.1 claim content, by value
  schemeDesignation: C.2.1 SchemeDesignation
  editionId
  fitFindingRefs[5]: U.EpistemeRef, each referencing one PatternUseFitFinding@Context
  applicabilityResult: PatternUseApplicabilityResultValue
  missingBasisBoundaryRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The five criteria refer to one candidate. When its basis must be addressable, consume PUA §4.4's ordinary C.2.1 claim about that candidate and its exact supporting claims, relations or evidence uses; no candidate-basis U.Relation is required. A contradicted product-law premise and missing dependence information remain distinct inputs to these fit tests.

In ordinary conversation, inspect all five without materializing five findings. State the aggregate applicability when it answers the current question; if the later comparison supports a recommendation, carry that result into the recommendation.

`PatternUseApplicabilityFinding@Context` is the reliance-bearing support episteme: when it exists, its five findings cover each criterion exactly once.

Use mutually exclusive branches: any `misfit` yields `inapplicable`, including when another aspect has `insufficientBasis`; with no `misfit`, one or more `insufficientBasis` values yield `insufficientBasis` and a missing-basis boundary; otherwise all five are `fit` and the result is `applicable`.

A known `misfit` settles this candidate's applicability under the inspected conditions. Do not obtain more information merely to fill the remaining aspects when it cannot change that answer. If changing the failed condition is a serious continuation, appraise that change separately and reconsider the affected fit under `4.6`. A different candidate may still be applicable and worth recommending.

`problemFrame` compares the candidate pattern's Problem frame with the current concern; it does not assert that an actual Problem obtains.

When an actual Problem is relied on, cite one current C.22.PFR `ProblematicForRelation` occurrence with its exact actual-condition and criterion-applicability participants and adverse-episode identity. A ProblemCard, fit finding, assessment, or recommendation may support a claim about that occurrence but neither creates nor splits it.

#### E.11.PUR:4.2 - Recommendation

Recover the result the recipient needs and the decision for which advice is due. Compare what the present work can already supply, a sufficient single use, and combinations that could meet that need. For a combination, establish that the contributions can be obtained and used together under the receiving conditions. Include shared work once and count demands that compete for the same time, evidence or people. C.11.DUA helps when the worth of the advice or its interaction with other changes is unclear. C.11.CRC supports a comparison when the contribution of a use depends on what else is available.

Applicability can coexist with no worthwhile recommendation now. In that case, finish without selecting a pattern use or materializing a positive recommendation; give a short reason only when the current question or later reliance needs it.

Continuing without optional advice does not remove an existing obligation.

Match the scope of the reasons to the scope of the recommendation. For advice about a first inquiry, ask what its possible answers would settle or enable and what that inquiry costs. For advice to undertake the whole job, compare what each feasible way delivers by the time it is needed and what it takes to get there. Two ways can produce the same early answer and leave different prospects for finishing. Recommend the single use or combination that the comparison supports. A short explanation of the decisive grounds and any remaining conditions suffices for a reversible choice with no named later reliance.

When the recommendation must remain addressable, use the schema below. `ordinaryCompact` keeps one compact rationale and no five-finding dossier; `relianceBearing` adds the current applicability finding only because a named later use needs independent replay.

```text
PatternUseRecommendationSupportProfileValue = ordinaryCompact | relianceBearing

PatternUseRecommendation@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the selected CandidatePatternUse@Context
  entityOfConcernKindRef: U.KindRef
  claimGraph: exact whole C.2.1 claim content, by value
  schemeDesignation: C.2.1 SchemeDesignation
  editionId
  recommendationSupportProfile: PatternUseRecommendationSupportProfileValue
  applicabilityResult: PatternUseApplicabilityResultValue
  compactApplicabilityAndSelectionRationaleRef: U.EpistemeRef, referencing one CandidatePatternUseRationale@Context
  applicabilityFindingRef?: U.EpistemeRef, referencing one PatternUseApplicabilityFinding@Context
  expectedResultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  strongerNeighborPatternRef?: U.EntityRef, referencing the exact neighboring FPF pattern episteme only when its identity changes the recommendation
  recommendationBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

One addressable recommendation selects one applicable candidate. When its value depends on another use, include that dependency in the rationale and show how the contributions together warrant the advice. A joint recommendation can be given in ordinary prose. Use a coordination account under §4.3 when someone needs to refer back to the relation among the uses.

In an addressable `ordinaryCompact` recommendation, the applicability result and compact rationale are carried directly and `applicabilityFindingRef` is absent.

In `relianceBearing`, the same recommendation also cites one current applicability finding whose five fit findings can be replayed independently. The profile changes support cardinality, not the recommendation kind or authority.

When an addressable recommendation is materialized, `expectedResultExpectationRef` points to its exact E.11.PUA expectation. It identifies the expected result and only the pattern, relative-object, or category-correct basis distinctions that expectation uses; it does not assert that the result exists or that any relation, A.6.1 binding, or local claim is current.

A recommendation does not authorize work, establish a gate, prove evidence sufficiency, create the expected result, or supply its later closure.

When a stronger neighboring pattern better addresses the current question, name it and state the return condition. Populate `strongerNeighborPatternRef` only when the exact pattern identity matters to an addressable recommendation. The reference does not establish formal `U.MethodDescription` membership; such membership requires its own A.3.2 basis. Familiarity with the current candidate is not a recommendation reason.

##### E.11.PUR:4.2.1 - Reuse an earlier result when it still answers the concern

After identifying an applicable candidate use, ask whether an earlier result episteme already answers the present concern. Use the pattern that defines or tests that result to compare:

- the result episteme's `EntityOfConcern` and edition;
- the question answered and declared use;
- the source and dependency conditions on which the answer relies; and
- its qualification and currentness boundary.

When those values still match, cite and use the earlier result.

Use `A.10` when a named claim or bounded action relies on that result and the source-to-use account is still implicit. Add a dated `U.Work` occurrence only when that Work is itself a current claim. Use `G.11` when currentness or refresh changes the use.

A matching result can complete a commission for the answer. If the commission also specifies a fresh application, a particular performer or an independent judgement, establish whether that performance has taken place on those terms. The earlier result can still supply an input.

When one value changed, reopen the smallest affected result question under the pattern that defines or tests that result. A new performance of the complete use is warranted when the scope of the earlier result cannot be established or the commission calls for that performance. If the applicable pattern supplies no basis for comparing the earlier result with the present concern, stop at `insufficient result-comparison basis`.

The candidate pattern use, the earlier result episteme, a later reliance relation, a currentness assertion, and later Work remain separate. This branch introduces no generic result-reuse relation.

#### E.11.PUR:4.3 - Coordination without forced order

For a question about sequence, state the candidates, whether they are unordered, partially ordered or totally ordered, the reason for any precedence, and the stop boundary. For a question about their joint use, follow each required contribution into the same decision or work and check that the contributions can serve together under its conditions. Two uses in the right order can concern different versions of the object. The order answers the sequencing question. Version compatibility can decide whether the resulting conclusion is usable. Retain the rationale and any established ordering relations as addressable epistemes when a later use needs them.

```text
PatternUseOrderingModeValue = unordered | partialOrder | totalOrder

PatternUseCoordinationRationale@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the coordination-question episteme
  claimGraph: exact whole C.2.1 claim content, by value
  schemeDesignation: C.2.1 SchemeDesignation
  editionId
  subjectCandidatePatternUseRefs[2..*]: U.EpistemeRef, each referencing one CandidatePatternUse@Context
  coordinationRationaleDescriptionRef: U.EpistemeRef
  rationaleBasisEpistemeRefs[]: U.EpistemeRef
  coordinationBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context

PatternUseCoordination@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the coordination-question episteme
  entityOfConcernKindRef: U.KindRef
  claimGraph: exact whole C.2.1 claim content, by value
  schemeDesignation: C.2.1 SchemeDesignation
  editionId
  memberCandidatePatternUseRefs[2..*]: U.EpistemeRef, each referencing one CandidatePatternUse@Context
  orderingMode: PatternUseOrderingModeValue
  orderingRelationRefs[]?: U.EntityRef, each referencing one PatternUseOrderingRelation@Context
  coordinationRationaleRef: U.EpistemeRef, referencing one PatternUseCoordinationRationale@Context
  stopBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

`unordered` has no ordering relations. `partialOrder` and `totalOrder` use explicit pairwise relations. A total order is the bounded `PatternUseSequence@Context` specialization under its named receiving use; it is not a universal route or project WorkPlan.

Treat the declared pairwise precedence as strict: its transitive closure must be irreflexive. A `totalOrder` additionally compares every pair of distinct members.

A cycle or unresolved required pair blocks that ordering claim; preserve the known dependencies and state the unresolved coordination question.

#### E.11.PUR:4.4 - Pairwise precedence

A pairwise precedence relation is an applicable directed constraint between two exact candidate uses for the governed coordination question. It can obtain before either is performed. Establish its branch predicate:

* **prerequisiteResult:** the dependent use's direct rule requires exact content, and the coordination has a stated basis for selecting this prerequisite use to supply it. Cite that rule, content and selection basis together with the prerequisite candidate's exact expectation. Matching output kinds alone is insufficient. The result need not yet exist for the dependency to obtain.
* **methodPrecondition:** performing the dependent use first would invalidate a condition that the prerequisite use needs, and the proposed order preserves that condition. Name both uses and the condition; unary candidate fit alone supplies no pair.
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

**Identity and extent.** Keep the same dependency for the same exact candidates, governed coordination use, branch and meaning of its precedence condition, including any constitutive schedule/priority rule. A different rendering, witness or descriptive coordination episteme alone changes none of those values.

A changed candidate or meaning-changing condition/rule requires a new relation claim and identity assessment; the record reference is not itself the identity law.

Within a temporally qualified use, the occurrence lasts while that branch predicate holds; a gap where it ceases to hold ends the occurrence, and a later re-established occurrence has a new extent. Omit temporal machinery for an atemporal constraint.

**Readiness is a separate claim.** For prerequisite-result continuation, identify the actual result and category-correct basis that satisfy the required content and receiving conditions.

When a named later reliance needs addressable closure, cite a current E.11.PUA result-closure finding for the prerequisite use or an adequate earlier result reused under §4.2.1. State readiness/applicability for this continuation as its own ordinary C.2.1 claim.

A known unmet condition means not ready; missing information leaves readiness unresolved. An expectation, ordering edge or closure record's presence alone supplies no achieved result.

An adequate earlier result can satisfy a prerequisite for its content. If the receiving work also depends on a fresh inspection or on a particular performer’s judgement, establish that contribution before concluding readiness.

A changed closure can change readiness without changing the prospective dependency. No ordering or readiness claim authorizes Work. Page, seminar, identifier and display order do not establish a dependency.

#### E.11.PUR:4.5 - Procedure

1. Recover each candidate's current concern, direct pattern, Solution, expectation, and ordinary boundary.
2. Keep a local reversible applicability, recommendation, or coordination judgement conversational when no named later reliance needs it. When a recommendation must remain addressable, choose `ordinaryCompact` unless that reliance needs the fit aspects separately addressable; use `relianceBearing` only for that reliance.
3. Inspect all five fit aspects. In ordinary use, keep them in one compact rationale. Under `relianceBearing`, materialize five separate findings and one applicability finding.
4. Establish the aggregate applicability under `4.1`. A known `misfit` ends the applicability inquiry for that candidate under the inspected conditions.

   If the aggregate is `insufficientBasis`, obtain missing information only when an attainable answer can change a worthwhile continuation; otherwise return the missing-basis boundary.

   State the aggregate separately when the current question needs it. If step 5 supports a recommendation, include it there; when a reliance-bearing applicability finding exists, the two result values agree.
5. Compare continuing with the available results, a sufficient single use and any feasible combination that could make a difference to the receiving decision. For advice about the whole undertaking, compare the value and burden of each complete way. Use C.11.DUA when the comparison is unclear. If continuing as at present serves best, finish without a positive recommendation. An expected result still has to be obtained.
6. Compare any earlier result under `4.2.1`. Use it for what it already settles. Identify any outstanding result question and any fresh or independent work required by the commission.
7. Establish the ordering the receiving work needs under §4.4. When the commission concerns a combined result, use the rationale to explain how the contributions fit that result, including any joint condition the ordering leaves open.

   For prerequisiteResult, name exact required content, the selected supplier-use basis and its expectation.

   Assess readiness separately from precedence. When a continuation depends on a prerequisite result, check whether an actual result and its basis satisfy the receiving conditions. Reuse an adequate earlier result before requiring another use.
8. Return the applicability judgement, recommendation, reused result or coordination to the person who needs it. When that is what they asked for, the work can finish here. If a wider commission remains, apply the result in that work and obtain the remaining contributions. When a premise is missing, distinguish the work it prevents from work that can proceed.

   If proceeding without a new use serves best, existing obligations remain in force. A separate refusal document is unnecessary.

   A Plain *next move* names the recommended use or conditional continuation. Apply PUA, P2W, planning, gate or decision guidance where it supplies an outstanding part of the commission.

#### E.11.PUR:4.6 - Replay and currentness

Replay an ordinary conversational or addressable compact recommendation from the current concern, inspected candidate pattern and `Solution`, aggregate applicability, compact rationale over all five aspects, serious continuations considered, expected result and full burden, any current receiving use, and recommendation boundary.

Replay a reliance-bearing recommendation from those same positions plus the current applicability finding and its five fit findings.

Replay coordination from the receiving question, the inspected uses and the rationale for using them together. Recover the common conditions on which the conclusion relied, including compatibility of the subject, edition or time window where relevant. Recover the ordering mode, any pairwise precedence and its basis, and the stop boundary. For `prerequisiteResult`, include the exact expectation, required content and basis for selecting the supplier use.

Replay readiness separately from precedence, using the actual result, its category-correct basis, receiving conditions and any earlier-result reuse; recover an addressable closure finding only when that reliance needs it.

When a later use needs to replay a conclusion without a recommendation, recover the concern, the serious continuations, the value and burden that mattered, and the condition for reconsideration. No selected-candidate reference or five-finding dossier is required for that conclusion.

Replay a result-reuse stop from the earlier result episteme and edition, the question and declared use, relied source and dependency conditions, qualification and currentness boundary, and any separately current A.10 reliance or G.11 assertion.

Recheck the smallest affected finding, result question, or relation when a candidate `Solution`, result expectation, result entity or edition, relative object, direct basis or defining `ClaimGraph`, relied source or dependency condition, qualification or currentness boundary, fit basis, value or burden, alternative under consideration, dependent use, coordination member, precedence basis, condition, or boundary changes.

A changed candidate fit reopens its applicability and any recommendation that relied on it. A changed earlier result condition reopens only the affected result question and later uses unless the candidate or present concern also changed.

A changed prerequisite expectation or semantic precedence condition reopens the affected dependency and dependent use. A changed closure reopens readiness and only dependencies whose semantic basis also changed. A changed witness or rendering alone creates no new dependency.

Recheck a constitutive schedule or priority rule when it changes.

Separate G.11 assertions state edition, telemetry, currentness-window, and decay facts; PUR supplies the judgement-specific values and change conditions.


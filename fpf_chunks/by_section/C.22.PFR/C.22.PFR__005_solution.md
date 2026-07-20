---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__005_solution.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:4 — Solution"
line_start: 49768
line_end: 49916
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "A.6.5"
  - "A.6.REL"
  - "B.3"
  - "C.22"
  - "C.22.2"
  - "E.18.1"
  - "E.23"
  - "G.11"
keywords:
  - "actual condition"
  - "actual problematic-for relation"
  - "applicability predicate"
  - "problem-for entity"
  - "relation occurrence"
---

### C.22.PFR:4 - Solution

Model an actual Problem as one obtaining `ProblematicForRelation`, a dependent evaluative `U.Relation` between exactly two relation occurrences: the actual condition and the applicability of a characteristic-space predicate.

#### C.22.PFR:4.1 - Use one exact criterion-applicability relation

`CharacteristicSpacePredicate` is a by-value predicate used by an A.19 comparison, acceptance, state, gate, or other direct consumer. It is not a new U-kind, publication record, description edition, or comparison result. Its meaning is recoverable from the declared characteristic-space coordinates, scales, normalization or bridge values, operator, cut or band, polarity, and the selected direct consumer's governed comparator, admissibility, and predicate-use semantics. A separately performed evaluation remains `U.Work`; its result episteme and evidential-support relations remain separately governed, and none of these constitutes predicate meaning.

**Public name settlement.** The following F.18 NameCard names the applicability relation kind. It does not make one applicability occurrence obtain and does not replace the relation signature below.

```text
NameCard:
  NameCardId: NC-PROBLEM-CRITERION-APPLICABILITY-RELATION
  GovernedValueRef: ProblemCriterionApplicabilityRelation under C.22.PFR
  GoverningPatternRef: C.22.PFR
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: obtaining relation that canonically links one characteristic-space predicate to one exact problem-for entity over one claim scope and one declared criterion-applicability window; repeated occurrences with the same four participants are distinguished by maximal continuous actual obtaining
  TechLabel: ProblemCriterionApplicabilityRelation
  PlainLabel: problem-criterion applicability
  CandidateSet: ProblemCriterionApplicabilityRelation; CriterionApplicabilityRelation; ProblemCriterionUseRelation; ApplicableProblemCriterion
  RejectedCandidates: CriterionApplicabilityRelation overclaims a universal criterion ontology; ProblemCriterionUseRelation hides obtaining applicability behind use wording; ApplicableProblemCriterion turns a relation into an adjective-headed value
  SelectionRationale: preserve distinct applicability occurrences for different exact entities, scopes, or declared windows and after demonstrated loss and restoration of applicability, without making a predicate-description edition identity-bearing
  LineageEntries: replaces description-edition and generic criterion-use identity proposals
  RefreshCondition: reopen if the four fixed participants plus maximal continuous actual obtaining cannot distinguish applicability occurrences
```

Use one individuable dependent `U.Relation` for applicability:

```text
ProblemCriterionApplicabilityRelation:
  ProblemCriterionPredicateSlot: CharacteristicSpacePredicate, byValue
  ProblemForEntitySlot: U.Entity, byRef with an exact local ValueKind
  PredicateClaimScopeSlot: U.ClaimScope, byValue
  DeclaredCriterionApplicabilityWindowSlot: DeclaredCriterionApplicabilityWindow, byValue; use an explicit unbounded value when no finite bound is intended
```

This relation states that one exact predicate applies to one exact entity for one claim scope under one declared criterion-applicability window. It obtains only while that fixed applicability predicate is actually true under the declared window. One occurrence is identified by the four fixed participants plus the maximal continuous period of actual obtaining. Changing a participant yields another occurrence; demonstrated loss and later restoration of applicability yields distinct occurrences even when all four participants stay fixed. A coextensional description edition or carrier change does not change either the predicate participant or the occurrence. Assessment windows, evidence-relevance intervals, description editions, and claim-currentness windows remain with their own claims and relations.

A semantic predicate change selects a different predicate participant; it is not an edition-only repair. If the new predicate replaces the old predicate for the same use and the old applicability therefore ceases, the old applicability occurrence ends and a new occurrence begins only if the new predicate actually applies. The PFR dependent on the old occurrence can then end, and another PFR can begin under the new occurrence when adverse truth obtains. If both predicates remain applicable, two applicability occurrences may coexist; a new criterion description alone does not prove replacement or cessation.

#### C.22.PFR:4.2 - Keep the PFR signature reduced to two participants

**Public name settlement.** The following F.18 NameCard names the actual dependent evaluative relation. It does not create the Problem, add a third participant, or replace the occurrence-identity rule.

```text
NameCard:
  NameCardId: NC-PROBLEMATIC-FOR-RELATION
  GovernedValueRef: ProblematicForRelation under C.22.PFR
  GoverningPatternRef: C.22.PFR
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: actual dependent evaluative relation with one actual-condition relation occurrence and one problem-criterion-applicability relation occurrence as its only non-derived participants, individuated for each maximal continuous adverse interval
  TechLabel: ProblematicForRelation
  PlainLabel: actual problem
  CandidateSet: ProblematicForRelation; AdverseCriterionAssessmentRelation; ProblemUseRelation; ProblemRelation; ProblemSituationRelation
  RejectedCandidates: AdverseCriterionAssessmentRelation omits the problem-for relation; ProblemUseRelation hides the actual adverse condition; ProblemRelation hides criterion applicability; ProblemSituationRelation falsely requires situation
  SelectionRationale: make ordinary Problem recoverable without copying applicability participants and distinguish repeated adverse episodes without requiring a universal adverse-evaluation relation occurrence
  LineageEntries: situation-first, card-as-world, bearer-duplicating, and description-edition identity proposals retired
  RefreshCondition: reopen if participant references plus the derived maximal continuous adverse interval cannot distinguish repeated PFR occurrences, or if the applicability projection becomes ambiguous
```

**No-mint disposition for root `U.Problem`.** Do not introduce a second problem entity beside the obtaining `ProblematicForRelation` occurrence. That occurrence is the actual Problem; a `ProblemCard`, criterion description, assessment claim, or local Plain label may describe or designate it but does not supply another world-side identity.

The complete non-derived participant set is:

```text
ProblematicForRelation:
  ActualConditionRelationSlot: U.Relation, byRef
  ProblemCriterionApplicabilityRelationSlot: U.Relation, byRef
```

The first reference resolves to the exact obtaining relation that constitutes the actual condition under its direct pattern. The second resolves to the exact obtaining applicability relation from C.22.PFR:4.1.

PFR has no separately writable condition-bearer, predicate, problem-for-entity, claim-scope, applicability-window, assessment-window, or description-edition slot. Those values already have canonical owners. A readable claim projects them from the two participants:

```text
PFR.problemCriterionPredicate
  := PFR.problemCriterionApplicabilityRelation.problemCriterionPredicate
PFR.problemForEntity
  := PFR.problemCriterionApplicabilityRelation.problemForEntity
PFR.predicateClaimScope
  := PFR.problemCriterionApplicabilityRelation.predicateClaimScope
PFR.declaredCriterionApplicabilityWindow
  := PFR.problemCriterionApplicabilityRelation.declaredCriterionApplicabilityWindow
PFR.problemCriterionApplicabilityExtent
  := maximal continuous obtaining extent of PFR.problemCriterionApplicabilityRelation
```

This is a derivation from one participant, not a consistency check between copies.

#### C.22.PFR:4.3 - Use predicate truth as the obtaining condition

`ProblematicForRelation` obtains exactly when all three conditions hold:

1. The exact `ActualConditionRelation` obtains under its direct pattern.
2. The exact `ProblemCriterionApplicabilityRelation` obtains, and its by-value predicate is well-typed for its exact entity and claim scope under its declared criterion-applicability window.
3. The actual condition falls on the adverse side of that predicate under the scales, comparator, cut or band, polarity, and admissibility semantics governed by the selected direct consumer pattern.

The direct consumer evaluates and supports a claim that the adverse predicate obtains. Comparison outcomes, acceptance outcomes, state or gate results, measurements, evidence, and assessment claims may support that claim. They are not automatically PFR participants, and their production does not make PFR obtain.

A Problem can therefore obtain unnoticed. Later detection produces work, evidence, and claims about the already obtaining relation; it does not create retroactive actuality.

#### C.22.PFR:4.4 - Identify repeated adverse episodes

The occurrence identity is:

```text
<actualConditionRelationRef,
 problemCriterionApplicabilityRelationRef,
 maximalContinuousAdverseInterval>
```

`maximalContinuousAdverseInterval` is a derived temporal extent of the PFR occurrence. It is not a writable participant slot and not a new kind. It is the maximal continuous interval during which both participant relations obtain and the actual condition stays on the adverse side of the applicable predicate.

Participant references alone are insufficient because the same participant occurrences can be adverse, non-adverse, and adverse again. A universal constituting evaluation reference is also insufficient because direct consumer patterns do not all individuate such an occurrence, and evaluation is epistemic support rather than what universally constitutes PFR.

#### C.22.PFR:4.5 - Keep one usable identity while the episode is open

Represent a current adverse episode as:

```text
[adverseEpisodeStart, open]
```

For a current reference, this notation denotes the same derived maximal interval whose end is not yet known. `open` is an endpoint sentinel, not the current clock time. As the episode continues, the interval remains `[adverseEpisodeStart, open]`; each observation does not mint a new interval or PFR identity. When the episode is shown to end, record the end endpoint on the same occurrence. Replacing the open endpoint with the recovered end is closure of its derived temporal extent, not replacement by another occurrence.

Use the A-B-C regression:

- During interval A, the condition is demonstrated adverse. One PFR occurrence is current as `[A.start, open]` and later closes at A's end.
- During interval B, the condition is demonstrated non-adverse under the same applicability semantics. The first PFR does not obtain in B.
- During interval C, the condition is again demonstrated adverse. A later PFR occurrence begins with the same two participant references but a different `maximalContinuousAdverseInterval`.

A missing assessment, unavailable measurement, stale evidence item, or gap in support is `unknown`. It is not demonstrated non-adverse behavior. Such a gap neither closes nor splits PFR by itself. Adjacent or overlapping assessment windows inside a continuously adverse episode likewise do not split it.

#### C.22.PFR:4.6 - Keep anticipated-condition claims, solvability, and cards separate

A possible or anticipated problem remains an exact forecast, scenario, counterfactual, or anticipated-condition claim in `ProblemCard@Context` or another episteme until an actual-condition relation, an applicability relation, and adverse predicate truth all obtain. `C.2.1` governs its assertion identity and polarity; `C.27`, `C.28`, or the exact direct claim pattern governs assumptions, horizon, and non-actual semantics; `A.10` or the receiving evaluation separately governs supported, refuted, or unresolved reliance. None of those claim-side facts establishes a current PFR. A card may describe zero, one, or several independently obtaining PFR occurrences; several cards may describe one PFR under different viewpoints.

A claim that no supported method is currently available concerns the admitted method set, evidence, constraints, and acceptance use. Selecting or discovering a method changes current solvability. It does not end PFR while the actual condition remains adverse. Performed repair work can end or change the actual-condition occurrence and thereby end PFR.

Repeated problematization, method search, work, evaluation, and continuation occur in work and transformation flows governed by `E.18.1` and `E.23`. A claim or plan may carry a reference to the same PFR while work and transformation occurrences participate in a selected transformation-flow structure. Neither that PFR reference use nor any flow-structure relation enters PFR identity. A later PFR is a later occurrence because its participants or maximal continuous adverse interval differ, not because flow work revisits an earlier transformation or relation.

#### C.22.PFR:4.7 - Preserve the lightweight path

Ordinary use writes the readable assertion:

> The actual condition is adverse under the predicate applicable to this entity and scope; therefore this condition is a problem for that entity.

The predicate and problem-for entity are projected from the applicability relation. The user does not fill a PFR record by default. Explicitly individuate and expose the PFR only when another claim must compare, qualify, change, nest, plan from, or refer to that actual Problem.


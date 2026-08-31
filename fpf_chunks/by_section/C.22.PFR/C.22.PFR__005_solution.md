---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__005_solution.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:4 — Solution"
line_start: 51924
line_end: 52100
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
---

### C.22.PFR:4 - Solution

Model an actual Problem as one obtaining `ProblematicForRelation`, a dependent evaluative `U.Relation` between exactly two relation occurrences: the actual condition and the applicability of a characteristic-space predicate.

#### C.22.PFR:4.1 - Use one exact criterion-applicability relation

`CharacteristicSpacePredicate` is a by-value predicate used by an A.19 comparison, acceptance, state, gate, or other direct consumer. It is not a new U-kind, publication record, description edition, or comparison result. Its meaning is recoverable from the declared characteristic-space coordinates, scales, normalization or bridge values, operator, cut or band, polarity, and the selected direct consumer's governed comparator, admissibility, and predicate-use semantics. A separately performed evaluation remains `U.Work`; its result episteme and evidential-support relations remain separately governed, and none of these constitutes predicate meaning.

Before testing adversity, answer three plain questions: **what exact point or value does this condition supply, how is that point obtained, and why is it the input for this problem-for entity and use?** The by-value predicate therefore carries one `ConditionToPredicateInputRule` as part of its own semantics, not as another PFR participant:

- **Direct input:** the actual-condition participant is already a governed characteristic-assignment or state relation whose subject pattern exposes the exact characteristic-space coordinate, scale, and value used by the predicate.
- **Projected input:** when that relation does not itself expose the needed point, the rule cites one exact governed projection or bridge, its source relation kind and participant positions, target characteristic space, coordinate and scale, and the direct relation or predicate connecting that input to the problem-for entity and receiving use.

A relation reference alone is not a coordinate. If neither path yields the exact point and the problem-for link, adverse truth and PFR remain unestablished. When two projections are plausible, the rule names the selected one and the nearest inadmissible projection. `ConditionToPredicateInputRule` is a pattern-local by-value rule inside `CharacteristicSpacePredicate`; it is not a U-kind, relation occurrence, evaluation result, or copied PFR field.

**Public name settlement.** The following F.18 NameCard names the applicability relation kind. It does not make one applicability occurrence obtain and does not replace the relation signature below.

```text
NameCard:
  NameCardId: NC-PROBLEM-CRITERION-APPLICABILITY-RELATION
  GovernedValueRef: ProblemCriterionApplicabilityRelation under C.22.PFR
  SubjectPatternLocator: C.22.PFR
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: obtaining relation saying that one characteristic-space predicate currently governs one exact problem-for entity and claim scope under one declared criterion-applicability window, independently of whether an actual condition presently satisfies the adverse predicate; repeated occurrences with the same four participants are distinguished by maximal continuous actual applicability
  TechLabel: ProblemCriterionApplicabilityRelation
  PlainLabel: problem-criterion applicability
  CandidateSet: ProblemCriterionApplicabilityRelation; CriterionApplicabilityRelation; ProblemCriterionUseRelation; ApplicableProblemCriterion
  RejectedCandidates: CriterionApplicabilityRelation overclaims a universal criterion ontology; ProblemCriterionUseRelation hides obtaining applicability behind use wording; ApplicableProblemCriterion turns a relation into an adjective-headed value
  SelectionRationale: preserve distinct applicability occurrences for different exact entities, scopes, or declared windows and after actual loss and restoration of applicability, without making a predicate-description edition identity-bearing
  PublicRowStatus: pending
  LineageEntries: replaces description-edition and generic criterion-use identity proposals
  RefreshCondition: reopen if the four fixed participants plus maximal continuous actual applicability cannot distinguish applicability occurrences, or if the direct rule no longer separates criterion governance from adverse-condition satisfaction
```

Use one individuable dependent `U.Relation` for applicability:

```text
ProblemCriterionApplicabilityRelation:
  ProblemCriterionPredicateSlot: CharacteristicSpacePredicate, byValue
  ProblemForEntitySlot: U.Entity, byRef with an exact local ValueKind
  PredicateClaimScopeSlot: U.ClaimScope, byValue
  DeclaredCriterionApplicabilityWindowSlot: DeclaredCriterionApplicabilityWindow, byValue; use an explicit unbounded value when no finite bound is intended
```

This relation states that one exact predicate currently governs one exact entity and claim scope under one declared criterion-applicability window. Its direct applicability predicate is satisfied while that criterion remains selected and governing for that entity, scope, and window; it does not ask whether any actual condition is presently on the adverse side. The applicability occurrence can therefore continue across adverse, non-adverse, and later adverse condition intervals. It ceases when the criterion is withdrawn or replaced for that use, the entity or claim scope changes, the declared window no longer covers the use, or another direct applicability condition fails. One occurrence is identified by the four fixed participants plus the maximal continuous period of actual applicability. Changing a participant yields another occurrence; actual loss and later restoration of applicability yields distinct occurrences even when all four participants stay fixed. A coextensional description edition or carrier change does not change either the predicate participant or the occurrence. Assessment windows, evidence-relevance intervals, description editions, claim-currentness windows, and adverse-truth intervals remain with their own claims and relations.

A semantic predicate change selects a different predicate participant; it is not an edition-only repair. If the new predicate replaces the old predicate for the same use and the old applicability therefore ceases, the old applicability occurrence ends and a new occurrence begins only if the new predicate actually applies. The PFR dependent on the old occurrence can then end, and another PFR can begin under the new occurrence when adverse truth obtains. If both predicates remain applicable, two applicability occurrences may coexist; a new criterion description alone does not prove replacement or cessation.

#### C.22.PFR:4.2 - Keep the PFR signature reduced to two participants

**Public name settlement.** The following F.18 NameCard names the actual dependent evaluative relation. It does not create the Problem, add a third participant, or replace the occurrence-identity rule.

```text
NameCard:
  NameCardId: NC-PROBLEMATIC-FOR-RELATION
  GovernedValueRef: ProblematicForRelation under C.22.PFR
  SubjectPatternLocator: C.22.PFR
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: actual dependent evaluative relation with one actual-condition relation occurrence and one problem-criterion-applicability relation occurrence as its only non-derived participants, individuated by those participants plus the actual inception of each maximal continuous adverse episode
  TechLabel: ProblematicForRelation
  PlainLabel: actual problem
  CandidateSet: ProblematicForRelation; AdverseCriterionAssessmentRelation; ProblemUseRelation; ProblemRelation; ProblemSituationRelation
  RejectedCandidates: AdverseCriterionAssessmentRelation omits the problem-for relation; ProblemUseRelation hides the actual adverse condition; ProblemRelation hides criterion applicability; ProblemSituationRelation falsely requires situation
  SelectionRationale: make ordinary Problem recoverable without copying applicability participants and distinguish repeated adverse episodes without requiring a universal adverse-evaluation relation occurrence
  PublicRowStatus: pending
  LineageEntries: situation-first, card-as-world, bearer-duplicating, and description-edition identity proposals retired
  RefreshCondition: reopen if participant references plus actual adverse inception cannot keep one stable occurrence reference through closure or distinguish later adverse episodes, or if the predicate's condition-to-input rule no longer yields one unambiguous characteristic point and problem-for link
```

**No-mint disposition for root `U.Problem`.** Do not introduce a second problem entity beside the obtaining `ProblematicForRelation` occurrence. That occurrence is the actual Problem; a `ProblemCard`, criterion description, assessment claim, or local Plain label may describe or designate it but does not supply another world-side identity.

The complete non-derived participant set is:

```text
ProblematicForRelation:
  ActualConditionRelationSlot: U.Relation, byRef
  ProblemCriterionApplicabilityRelationSlot: U.Relation, byRef
```

The first reference resolves to the exact obtaining relation that constitutes the actual condition under its direct pattern. The second resolves to the exact obtaining applicability relation from C.22.PFR:4.1.

PFR has no separately writable condition-bearer, predicate, problem-for-entity, claim-scope, applicability-window, assessment-window, or description-edition slot. Those values are already fixed by the two participant relations and their defining declarations. A readable claim projects them from the two participants:

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
2. The exact `ProblemCriterionApplicabilityRelation` obtains because its criterion remains governing for the exact entity and claim scope under the declared criterion-applicability window, independently of whether the actual condition is adverse.
3. Apply the predicate's exact `ConditionToPredicateInputRule` to the actual-condition participant. It must yield the declared characteristic-space point or value and the direct link to the problem-for entity and use; that point then falls on the adverse side under the selected scale, comparator, cut or band, polarity, and admissibility semantics.

The selected direct consumer supplies the governed input projection or consumes the direct characteristic assignment, then governs the comparator and admissibility semantics. An evaluation may calculate or support a claim that the resulting point is adverse. Comparison outcomes, acceptance outcomes, state or gate results, measurements, evidence, and assessment claims are not automatically PFR participants, and producing them does not make PFR obtain.

A Problem can therefore obtain unnoticed. Later detection produces work, evidence, and claims about the already obtaining relation; it does not create retroactive actuality.

When evaluation is actually performed, recover every exact actual performer `U.System` through A.13, let A.15.1 independently admit the dated evaluation `U.Work`, and name the selected `U.Method` or declared A.6.1 operation application. Add F.6 only when the evaluation account or a receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, neither a local system-role kind nor an assignment acts, and missing or failed F.6 leaves the evaluation Work intact. A short PFR explanation may omit an assignment identifier that no later claim uses. That Work may return the separate evaluation result `true`, `false`, or `unknown` defined by the selected evaluation pattern; a C.2.1 assertion may state the result, A.10 and B.3 may warrant reliance on that assertion, G.11 may qualify its current edition, and the receiving Work may rely, decline, defer, or reopen. These are distinct objects and relations. `unknown` is an evaluation result, never a world-side PFR value; no evaluation Work, result, assertion, warrant, currentness judgment, or reliance disposition constitutes a PFR participant or makes the relation obtain.


#### C.22.PFR:4.4 - Identify repeated adverse episodes from world-side continuity

The direct occurrence rule is ontic. With the two participant occurrences fixed, one PFR occurrence is the maximal continuous episode during which both participants obtain and the selected condition point is actually on the adverse side. Actual cessation of either participant or actual movement to the non-adverse side ends that occurrence. Later renewed adverse truth starts a later PFR occurrence. Measurement, evaluation, demonstration, assessment, and evidence availability neither start nor end either occurrence.

Use this world-side identity basis:

```text
<actualConditionRelationRef,
 problemCriterionApplicabilityRelationRef,
 adverseEpisodeStart>
```

`adverseEpisodeStart` is the episode's actual inception under the declared temporal reference, not the first observation or report time. When admitted time grain cannot distinguish co-inceptions, or when a receiving history must keep one reference while a claim about inception remains revisable, explicitly individuate the occurrence under A.6.REL and assign a stable `pfrOccurrenceId` that designates it. The resolution record may carry the current boundary claim, but neither its asserted start nor its asserted end becomes a mutable identifier field. The PFR's `actualAdverseExtent` is derived from the world-side episode: its end becomes fixed when the episode actually ceases, and a later claim may recover or correct that boundary. The recovered end and completed extent describe the occurrence; they do not replace it or change its assigned reference. This applies A.6.REL's participant-plus-episode rule without making a currently known boundary constitutive.

Participant references alone remain insufficient because the same participants can enter adverse, non-adverse, and later adverse episodes. A universal evaluation reference is also insufficient because an unnoticed PFR can obtain and several assessments can support one occurrence.

#### C.22.PFR:4.5 - Keep world-side occurrence and current boundary claim separate

Use `[adverseEpisodeStart, open]` only in a current claim whose evidence supports that this same PFR occurrence still obtains at the claim's stated reference time. `open` is a claim-side endpoint sentinel, not the clock time, an identity field, or a substitute for missing evidence. The stable occurrence reference remains unchanged when a later claim records the recovered actual end.

A current assertion or description distinguishes three cases in ordinary words:

- **supported current:** the evidence supports continuous adverse obtaining from the episode's actual inception through the stated reference time; publish `[adverseEpisodeStart, open]`;
- **supported closed:** the evidence supports actual cessation at an exact boundary; publish `[adverseEpisodeStart, adverseEpisodeEnd]` for the same occurrence reference;
- **continuity unresolved:** the available evidence does not decide whether an unobserved cessation or restart occurred; retain the recoverable earlier occurrence reference and the supported segments, but assert neither one continuous occurrence nor two occurrences across the gap.

Later evidence may revise the assertion, including its claimed start, end, or continuity, without creating or changing the world-side episode. If it supports an earlier actual cessation, complete the extent of the earlier occurrence at that boundary. If it also supports later renewed adverse truth, identify the later occurrence from its own actual inception. Until that distinction is supported, do not attach the later adverse segment to either the old or a new occurrence by default.

Use the A-B-C regression while holding one continuously obtaining applicability occurrence fixed. The criterion remains governing for the same entity, scope, and declared window through A, B, and C; only world-side adverse truth changes:

- During A, the condition is actually adverse, so the first PFR obtains from `A.start` until its actual cessation at `A.end`.
- During B, the condition is actually non-adverse, so the first PFR does not obtain.
- During C, the condition is actually adverse again, so a later PFR begins at `C.start` with the same two participant references and a different stable occurrence reference.

Evidence that supports A, B, and C warrants the corresponding two-occurrence assertion. A missing assessment, unavailable measurement, stale evidence item, or support gap warrants `continuity unresolved`; it neither proves recovery nor licenses continuity. Adjacent or overlapping assessment windows likewise do not split or join world-side episodes by themselves.

#### C.22.PFR:4.6 - Keep assertions, reliance, anticipated conditions, solvability, and cards separate

An assertion about the exact PFR obtaining predicate has affirmative or negative claim polarity. An affirmative assertion may designate an independently established occurrence; a negative assertion denies predicate satisfaction for the named participants and qualification but does not erase or reidentify an earlier occurrence. A.10/B.3 separately governs whether one receiving use treats that assertion as supported, refuted, or unresolved. Assertion polarity, support, and reliance therefore answer different questions.

A possible or anticipated problem remains an exact forecast, scenario, counterfactual, or anticipated-condition claim in `ProblemCard` or another episteme until an actual-condition relation, an applicability relation, and adverse predicate truth all obtain. `C.2.1` governs its assertion identity and polarity; `C.27`, `C.28`, or the exact direct claim pattern defines or constrains assumptions, horizon, and non-actual semantics. None of those claim-side facts establishes a current PFR.

A `ProblemCard` is one C.2.1 episteme with one exact ClaimGraph, one independently identified `EntityOfConcern`, and one effective `U.ReferenceScheme`. It may carry claims designating several PFR occurrences only when those claims are jointly about that one EntityOfConcern under the direct pattern that identifies it. When two PFR references lack such a joint concern, split the ClaimGraph and card. Conversely, several cards may designate the same PFR through different ClaimGraphs, schemes, viewpoints, or receiving uses. Card count, merge or split, currentness, assessment window, publication, carrier, and edition change neither PFR actuality nor identity. C.22.2:20.1b replays all three branches with exact objects: two Robot-7 PFR episodes share one A.1-identified `Robot-7` and one card; Robot-7 and Robot-8 PFRs have no direct joint EntityOfConcern and force two ClaimGraphs and cards; and two differently qualified cards retain the unchanged `PFR-InspectionAssignment-17` reference.

A claim that no supported method is currently available concerns the admitted method set, evidence, constraints, and intended use. Selecting or discovering a method changes current solvability; it does not end PFR while the actual condition remains adverse. Performed repair work can end PFR only when an independently recovered actual change makes a participant cease or moves the selected condition point to the non-adverse side.

Repeated problematization, method search, work, evaluation, and continuation occur in work and transformation flows governed by `E.18.1` and `E.23`. A claim or plan may carry a reference to the same PFR while work and transformation occurrences participate in a selected transformation-flow structure. Neither that reference use nor any flow-structure relation enters PFR identity. A later PFR is a later occurrence because a participant changes or because actual adverse truth begins again after actual cessation, not because another card, assessment, or flow visit exists.

#### C.22.PFR:4.7 - Preserve the lightweight path

For a first use, name only what decides the case:

1. the exact obtaining condition and the value or point it supplies;
2. the criterion that makes that point adverse, including the selected input path and cut or band;
3. the entity for which it is a Problem, the use or claim scope, and the applicability window.

Then write one ordinary sentence:

> `<condition and value>` misses `<criterion>` for `<entity and use>` during `<applicability window>`; therefore it is an actual Problem for that entity and use.

Stop there when the next work only needs to recognize the Problem. Cite the direct condition and criterion patterns, but do not fill a PFR record, repeat either relation signature, or assign a PFR identifier. The NameCards and signatures above define reusable semantics; they are not a mandatory user form.

Add explicit identity only when another claim must compare, qualify, change, nest, plan from, or refer back to this particular Problem occurrence. That receiving claim then names the exact actual-condition occurrence, exact applicability occurrence, actual adverse inception or stable PFR identifier when needed, claimed extent, and any evidence or assessment claim on which its reliance depends. The evidence remains separate from the world-side Problem.


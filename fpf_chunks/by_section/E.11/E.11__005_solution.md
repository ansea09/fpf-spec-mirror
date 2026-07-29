---
chunk_kind: "child"
pattern_id: "E.11"
pattern_title: "Practical-Use Guidance and Pattern Discovery"
section_id: "E.11:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11/E.11__005_solution.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "E.11 — Practical-Use Guidance and Pattern Discovery"
  - "E.11:4 — Solution"
line_start: 75721
line_end: 75970
dependencies:
  - "A.22.CGUS"
  - "C.2.1"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.17.AUD"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.18"
  - "G.11"
keywords:
---

### E.11:4 - Solution

An FPF author or maintainer publishes or refreshes fifteen semantic practical-use cards. Each card starts from a recognizable situation and question, states a readable first result or exact public blocker, points to direct candidate-use templates, and links to an expansion with boundaries and one walkthrough.

A practitioner, manager, or assisting agent uses the already published set: compare the cards that fit the working situation, inspect their different first results or blockers, and open the direct pattern from the card that best fits the work. Ordinary card use does not make that reader a framework publisher.

The keys identify situations; they do not order them. A user may compare any finite set that remains plausible.

#### E.11:4.1 - Public card and expansion

```text
PracticalUseGuidance@FPFReadme <: U.Episteme:
  practicalUseKey: PracticalUseKeyValue
  publicSituationDescriptionRef: U.Episteme
  publicPracticalQuestionRef: PublicPracticalUseQuestion@FPFReadme
  publicObstacleDescriptionRef?: PublicPatternUseObstacleDescription@FPFReadme
  publicFirstResultSummaryRef: U.Episteme
  cardExpansionRef: PracticalUseCardExpansion@FPFReadme

PracticalUseCardExpansion@FPFReadme <: U.Episteme:
  guidanceRef: PracticalUseGuidance@FPFReadme
  candidateUseTemplateRefs[1..*]: PublicCandidatePatternUseTemplate@FPFReadme
  publicStopBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicReturnBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicWrongTurnRecoveryBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicStrongerNeighborBoundaryRefs[]: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicCoarseningRows[]: PublicResultCoarseningRow@FPFReadme
  demonstrativeSliceRef?: DemonstrativeUnfoldingSlice@Context
  ordinaryWalkthroughRef?: PublicOrdinaryWalkthrough@FPFReadme

PracticalUseCardPublicationUnit@FPFReadme:
  conformsTo: E.17.AUD
  publishes: PracticalUseGuidance@FPFReadme
  linksTo: PracticalUseCardExpansion@FPFReadme
```

Exactly one walkthrough ref is present. Use `demonstrativeSliceRef` when the example passes A.22.CGUS admission in its own declared illustrative bounded context. It does not fill a reader-project position. Otherwise use an ordinary walkthrough with an explicit reason why the example is not a CGUS slice.

#### E.11:4.1.1 - Cold-reader recognition and grounded public value

Test every public card and expansion against a first-time engineer, engineer-manager, or assisting agent who has not studied FPF. The heading and first sentence name a recognizable working situation before PatternIDs, FPF kind names, or internal quality, projection, and conformance vocabulary. They then name a first useful result or exact blocker that the reader can imagine identifying, grounding, or requesting in the project—for example, identifying a current plan, grounding a claim about a pre-existing pump, or requesting an evaluation—without implying that the public template performs any of those acts. The expansion names the admitted kind of the potential result, the local identification question, direct owner and identity-or-obtaining basis, the kind of method, plan, dated Work, transformation, evaluation, decision, or receiving-use object relative to which the phrase would be true, the category-correct relative basis, the minimum usable result, and any actually current conditional receiver. It introduces no project instance.

A public benefit claim is grounded only when the card makes recoverable a concrete project need, one admitted kind of potential first result or exact blocker, the local identification and category-correct basis questions, one specific direct-pattern distinction that changes the next project action, and the direct pattern whose `Solution` governs the result kind. Otherwise the claim is marketing copy, even if it sounds plausible. These values may remain readable prose; this rule does not require the reader to fill a card or project record before opening the direct pattern.

Keep the public set representative of FPF's practical range. Wording and description repair remain visible, but they do not dominate architecture, problem shaping, work, comparison, evidence, timing, causal use, mathematical modeling, quality, improvement, and framework authoring.

#### E.11:4.2 - Public helper epistemes

```text
PublicPracticalUseQuestion@FPFReadme <: U.Episteme:
  situationRef: U.Episteme
  questionDescriptionRef: U.Episteme
  likelyDirectResultDescriptionRef?: U.Episteme

PublicPatternUseObstacleDescription@FPFReadme <: U.Episteme:
  situationRef: U.Episteme
  obstacleDescriptionRef: U.Episteme
  obstacleEffectOnUseRef: U.Episteme

PublicPatternUseResultTemplate@FPFReadme <: U.Episteme:
  readableResultDescriptionRef: U.Episteme
  exactResultKindRef: U.Kind
  resultIdentificationQuestionRef: U.Episteme
  resultDirectOwnerPatternRef: U.MethodDescription
  resultIdentityOrObtainingBasisTemplateRef: U.Episteme
  resultRelativeGovernedObjectKindRef: U.Kind
  resultRelativeDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  resultRelativeDirectBasisTemplateRef: U.Episteme
  minimumUsableResultDescriptionRef: U.Episteme
  conditionalReceivingPatternRef?: U.MethodDescription

PublicPatternUseBoundaryConditionTemplate@FPFReadme <: U.Episteme:
  boundaryConditionKind: recognizableCondition | stop | return | wrongTurnRecovery | strongerNeighbor | missingGovernor | missingInformation
  conditionDescriptionRef: U.Episteme
  governingPatternRef: U.MethodDescription
  conditionalReceivingPatternRef?: U.MethodDescription
  conditionalReceivingPatternPositionDescriptionRef?: U.Episteme

PublicResultCoarseningRow@FPFReadme:
  readableResultPhraseRef: U.Episteme
  exactResultKindRef: U.Kind
  resultIdentificationQuestionRef: U.Episteme
  resultDirectOwnerPatternRef: U.MethodDescription
  resultIdentityOrObtainingBasisTemplateRef: U.Episteme
  resultRelativeGovernedObjectKindRef: U.Kind
  resultRelativeDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  resultRelativeDirectBasisTemplateRef: U.Episteme
```

A public template asserts no project result and contains no project value. It names the admitted kind of a potential later result, the local question by which a practitioner would identify such an entity or occurrence, its direct owner, and what would make that candidate entity exist or that relation occurrence obtain. It separately names the kind of exact method, plan, dated Work, transformation, evaluation, decision, or separately governed receiving-use object relative to which a real PUA closure would call it a result.

The result-relative basis template has exactly one category. A direct-relation template asks for predicate, participants, applicability, obtaining, occurrence identity, and direct governor. An A.6.1 template asks for operation, application, argument or result binding, and direct governor. An A.6.RCD local-claim template asks for one C.2.1 claim episteme with polarity, substrate or constructor, base predicates and their direct owners, participants, case facts, and any support or warrant required by the later receiving use. The claim does not obtain, and A.6.RCD does not replace the base owners. Result identity or currentness and result-relative basis are different public questions; they coincide only when the potential result is the same direct relation occurrence used to close the later application.

`conditionalReceivingPatternRef` is present only when the public branch itself promises a continuation or names a downstream reliance. A result template without such a continuation leaves it absent. A public `stop`, `missingGovernor`, or `missingInformation` boundary has no receiver. `return`, `wrongTurnRecovery`, and `strongerNeighbor` name a receiver only when that route is part of the branch. The optional obstacle names a recognizable obstacle only when one matters. Practical use may begin from an object to inspect, a result to evaluate, or an existing method to improve without first inventing a problem.

#### E.11:4.3 - Candidate-use templates and basis completeness

```text
PublicCandidatePatternUseTemplate@FPFReadme <: U.Episteme:
  templateKey: PublicCandidateUseTemplateKeyValue
  recognizableConditionRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  directPatternRef: U.MethodDescription
  directSolutionSectionRef: PatternSolutionSectionRef
  expectedResultTemplateRef?: PublicPatternUseResultTemplate@FPFReadme
  resultPromiseBlockerRef?: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  candidateBasisCompletenessConditionRefs[1..*]: CandidatePatternUseBasisCompletenessCondition@FPFReadme

CandidatePatternUseBasisCompletenessCondition@FPFReadme <: U.Episteme:
  candidateBasisPosition: entityOfConcernKind | practicalQuestion | optionalProblemCard | resultIdentificationQuestion | resultRelativeGovernedObjectKind | candidateSpecificBasis
  admittedBasisValueKindRef: U.Kind
  completenessConditionDescriptionRef: U.Episteme
```

`PatternSolutionSectionRef` is an edition-pinned reference to the cited pattern's `Solution`. A broad result family or pattern title is insufficient.

Exactly one of `expectedResultTemplateRef` and `resultPromiseBlockerRef` is present. The result-promise branch is admissible only when the exact potential-result kind, its identification question, direct owner, identity-or-obtaining basis template, result-relative governed-object kind, category-correct relative-basis template, minimum usable result, and any actually current conditional receiver are all stateable. The blocker branch uses `missingGovernor` or `missingInformation`, states the exact absent governor or information, and carries no fulfilled result template. Optional omissions cannot masquerade as a weak passing promise.

The completeness condition inherits C.2.1 constitution. Its EntityOfConcern is the reusable candidate-basis position declared by the template; its ClaimGraph states the admitted filler kind and positive completeness condition; its ReferenceScheme explains how later current project fillers satisfy that position. It contains no project value and orders nobody to fill a form.

#### E.11:4.4 - Ordinary walkthrough

```text
PublicOrdinaryWalkthrough@FPFReadme <: U.Episteme:
  guidanceRef: PracticalUseGuidance@FPFReadme
  situationDescriptionRef: U.Episteme
  firstResultTemplateRef?: PublicPatternUseResultTemplate@FPFReadme
  resultPromiseBlockerRef?: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  walkthroughRowRefs[2..*]: PublicOrdinaryWalkthroughRow@FPFReadme
  fullPatternTransitionBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  cgusNonAdmissionRationaleRef: U.Episteme

PublicOrdinaryWalkthroughRow@FPFReadme <: U.Episteme:
  actionOrProposedUseDescriptionRef: U.Episteme
  expectedResultTemplateRef?: PublicPatternUseResultTemplate@FPFReadme
  resultPromiseBlockerRef?: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  directPatternRef: U.MethodDescription
  directSolutionSectionRef: PatternSolutionSectionRef
  continuationConditionRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
```

The walkthrough and each row carry exactly one result template or exact public blocker. An ordinary walkthrough is still an explanation, not a project method, work order, or recommendation. It may contain a local pattern mantra: a short repeatable formulation that keeps that pattern's Solution in attention. It may be presented as a CGUS-demonstrative mantra only when A.22.CGUS admits the represented conditional continuations as a `DemonstrativeUnfoldingSlice@Context`.

#### E.11:4.4.1 - Practical-use carry-through check

Check every published card over its public values. This check asks whether the card can lead a reader to one direct pattern and either a truthful context-free result promise or an exact public missing-governor or missing-information blocker. It creates no project instance, applicability verdict, result entity, relation occurrence, or receiving use.

```text
PracticalUseCarryThroughCheck:
  practicalUseKey: PracticalUseKeyValue
  practicalUseGuidanceRef: PracticalUseGuidance@FPFReadme
  publicSituationDescriptionRef: U.Episteme
  publicPracticalQuestionRef: PublicPracticalUseQuestion@FPFReadme
  publicObstacleDescriptionRef?: PublicPatternUseObstacleDescription@FPFReadme
  candidateUseTemplateRefs[]: PublicCandidatePatternUseTemplate@FPFReadme
  publicStopBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicReturnBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicWrongTurnRecoveryBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicStrongerNeighborBoundaryRefs[]: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicCoarseningRows[]: PublicResultCoarseningRow@FPFReadme
  demonstrativeSliceRef?: DemonstrativeUnfoldingSlice@Context
  ordinaryWalkthroughRef?: PublicOrdinaryWalkthrough@FPFReadme
  walkthroughSelectionRationaleRef: U.Episteme
  principalBlockedOverreadRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
```

Exactly one walkthrough reference is present. A demonstrative slice passes A.22.CGUS admission and identifies the included positions, C.33 structure-loss notes, alternatives or returns, direct patterns, and transition to the full pattern. An ordinary walkthrough carries its CGUS non-admission rationale. A local mantra inside it remains a compact reminder of the direct pattern's Solution; it does not acquire the Tech kind `DemonstrativeUnfoldingSlice@Context` merely because it is memorable or repeated.

Each candidate-use template passes one of two disjoint branches. A result-promise branch names one direct pattern and Solution, the admitted kind of a potential result, the local identification question, direct owner and identity-or-obtaining basis, full governed relative-object kind, category-correct relative-basis template, minimum usable result, every candidate-basis completeness condition, and a conditional receiver only when one is actually current. A blocker branch names the exact missing governor or missing information and carries no expected-result template. Reject omitted values presented as a weak promise, a public project instance, a broad family in place of the result kind, a generic result relation, or a PatternID list without selection conditions. The principal blocked overread states the most consequential false project claim that a reader could otherwise infer from the card.

#### E.11:4.5 - Fifteen stable practical-use keys


| Key | Public situation heading |
| --- | --- |
| `ARCHITECTURE` | Shape an architecture from a problem and competing characteristics |
| `WORKING-DOCUMENTS` | Create a working document that another participant can use |
| `OPTION-COMPARISON` | Compare options without hiding trade-offs |
| `PROBLEM-SHAPING` | Turn a vague concern into an accepted problem-side record |
| `IMPROVEMENT` | Improve a named object under an explicit evaluation |
| `COSTLY-ACTION` | Prepare a costly or hard-to-reverse action |
| `TIME` | Make a time-dependent claim usable |
| `CAUSAL-USE` | Decide what a causal claim may support |
| `DESCRIPTION-USE` | Use a description or view without confusing it with its subject |
| `NAMING` | Name a governed value so people can recover its meaning |
| `WORDING` | Repair wording that hides the object, relation, or claim kind |
| `MATHEMATICAL-MODELING` | Choose and bound a mathematical lens |
| `SOTA-PORTFOLIO` | Build a current state-of-the-art synthesis pack |
| `DPF-AUTHORING` | Build a domain or local FPF-grounded framework |
| `SYSTEM-IN-CONTEXT` | Delimit a system and its environment before architecture synthesis |

README owns the current public cards and their expansions. Preface explains why FPF's distinctions work together. ToC locates pattern families. Full patterns carry methods, conditions, costs, consequences, and exact result semantics. None is a second card store.

#### E.11:4.6 - Bounded comparison

When more than one card remains plausible, compare four things: recognizable-situation fit, difference among first results or exact public blockers, direct pattern, and stop or return condition. Keep the comparison in conversation for ordinary bounded use. Open the most promising direct pattern before constructing a project candidate.

The comparison rationale has one public guidance subject and exists before a project candidate is constructed. When materialized, it follows full C.2.1 identity:

```text
PracticalUseCardComparisonRationale@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one PracticalUseGuidance@FPFReadme
  claimGraph: U.ClaimGraph by value
  effectiveReferenceSchemeRef: U.ReferenceSchemeRef
  editionId
  recognitionReasonDescriptionRef: U.Episteme
  firstResultDifferenceDescriptionRef: U.Episteme
  comparisonRationaleDescriptionRef: U.Episteme
```

Stop inspection when one card has enough recognition and first-result advantage to justify direct pattern inspection, when no remaining card can change the starting choice, or when the inspection budget opens an explicit return. No fixed maximum of three is inferred.

Materialize comparison history only when a named receiving use relies on it:

```text
PracticalUseCardShortlist@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact PracticalUseQuestion@Context being compared
  claimGraph: U.ClaimGraph by value
  effectiveReferenceSchemeRef: U.ReferenceSchemeRef
  editionId
  claimScopeRef?: U.EntityRef, referencing one U.ClaimScope
  modelUseStructureRef?: U.EntityRef, referencing one BoundedModelUseStructure
  namedRelianceConditionRef: U.Episteme
  receivingUseDescriptionRef: U.Episteme
  receivingUseGoverningPatternRef: U.MethodDescription
  comparisonRefs[1..*]: PracticalUseCardComparison@Context
  selectedStartingGuidanceRef?: PracticalUseGuidance@FPFReadme
  inspectionStopBoundaryRef: PatternUseBoundaryCondition@Context
  returnBoundaryRef: PatternUseBoundaryCondition@Context

PracticalUseCardComparison@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one PracticalUseGuidance@FPFReadme
  claimGraph: U.ClaimGraph by value
  effectiveReferenceSchemeRef: U.ReferenceSchemeRef
  editionId
  shortlistRef: PracticalUseCardShortlist@Context
  recognizableSituationFitRationaleRef: PracticalUseCardComparisonRationale@Context
  firstResultTemplateRefs[]: PublicPatternUseResultTemplate@FPFReadme
  resultPromiseBlockerRefs[]: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  firstResultDifferenceRationaleRef: PracticalUseCardComparisonRationale@Context
  inspectionDisposition: keep | defer | discard | startHere
```

Guidance, practical question, compared result templates or blockers, first-result differences, named reliance, stop, and return remain ClaimGraph content or separately governed references; none replaces the C.2.1 identity. Each comparison cites at least one result template or exact blocker from the guidance it evaluates. `claimScopeRef` or `modelUseStructureRef` is present only when its exact direct relation changes the named reliance. Several plausible cards alone do not make this record current. The named reliance may be a later review, replay, audit, automation, or another use that needs addressable comparison history. Retain only the rows that use needs.

#### E.11:4.7 - Replay and currentness

Replay one public guidance claim from the current card and expansion, the edition-pinned direct `Solution`, and its exact branch. For a result promise, recover the potential-result kind, identification question, direct owner and identity-or-obtaining basis, governed relative-object kind, category-correct relative-basis template, minimum usable result, readable coarsening row, boundary, any conditional receiver, and selected walkthrough. For a blocker, recover the exact missing governor or information and confirm that no fulfilled result template was published. The guidance remains current only while the card's recognizable situation and practical question still point to that same use.

Recheck the smallest affected card slice when its recognizable situation, practical question, or resulting recognition condition changes; when the direct `Solution`, potential-result kind, identification question, direct owner, identity-or-obtaining basis, governed relative-object kind, relative-basis category, first-result difference, promise blocker, receiver, or boundary changes; or when use evidence shows a recurrent wrong turn. `G.11` governs edition, telemetry, currentness-window, and decay orchestration; E.11 supplies the card-specific values and change conditions that orchestration inspects.


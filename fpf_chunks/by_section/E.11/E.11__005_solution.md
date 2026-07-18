---
chunk_kind: "child"
pattern_id: "E.11"
pattern_title: "Practical-Use Guidance and Pattern Discovery"
section_id: "E.11:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11/E.11__005_solution.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.11 — Practical-Use Guidance and Pattern Discovery"
  - "E.11:4 — Solution"
line_start: 72198
line_end: 72420
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

Publish fifteen semantic practical-use cards. Each card starts from a recognizable situation and question, states a readable first result, points to direct candidate-use templates, and links to an expansion with boundaries and one walkthrough.

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

Test every public card and expansion against a first-time engineer, engineer-manager, or assisting agent who has not studied FPF. The heading and first sentence name a recognizable working situation before PatternIDs, FPF kind names, or internal quality, projection, and conformance vocabulary. They then name a first useful result that the reader can imagine producing or requesting in the project. The expansion and direct pattern restore the exact result kind, relation, boundary, and stronger-use conditions; plain recognition is not licence to leave those values vague.

A public benefit claim is grounded only when the card makes recoverable a concrete project need, a first useful result, one specific direct-pattern distinction that changes the next project action, and the direct pattern whose `Solution` governs obtaining that result. Otherwise the claim is marketing copy, even if it sounds plausible. These values may remain readable prose; this rule does not require the reader to fill a card or project record before opening the direct pattern.

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
  directResultKindRef: U.Kind
  directResultRelationSignatureRef?: RelationSignature
  resultDescriptionRef: U.Episteme
  minimumUsableResultDescriptionRef: U.Episteme
  receivingPatternRef: U.MethodDescription

PublicPatternUseBoundaryConditionTemplate@FPFReadme <: U.Episteme:
  boundaryConditionKind: recognizableCondition | stop | return | wrongTurnRecovery | strongerNeighbor
  conditionDescriptionRef: U.Episteme
  governingPatternRef: U.MethodDescription
  conditionalReceivingPatternRef?: U.MethodDescription
  conditionalReceivingPatternPositionDescriptionRef?: U.Episteme

PublicResultCoarseningRow@FPFReadme:
  readableResultPhraseRef: U.Episteme
  exactResultKindRef: U.Kind
  exactResultRelationSignatureRef?: RelationSignature
  governingPatternRef: U.MethodDescription
```

A result relation signature is present exactly when its result kind admits a relation. `return`, `wrongTurnRecovery`, and `strongerNeighbor` boundaries name a receiving pattern and position description. `recognizableCondition` and `stop` leave those positions absent.

The optional obstacle names a recognizable obstacle only when one matters. Practical use may begin from an object to inspect, a result to evaluate, or an existing method to improve without first inventing a problem.

#### E.11:4.3 - Candidate-use templates and basis completeness

```text
PublicCandidatePatternUseTemplate@FPFReadme <: U.Episteme:
  templateKey: PublicCandidateUseTemplateKeyValue
  recognizableConditionRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  directPatternRef: U.MethodDescription
  directSolutionSectionRef: PatternSolutionSectionRef
  expectedResultTemplateRef: PublicPatternUseResultTemplate@FPFReadme
  candidateBasisCompletenessConditionRefs[1..*]: CandidatePatternUseBasisCompletenessCondition@FPFReadme

CandidatePatternUseBasisCompletenessCondition@FPFReadme <: U.Episteme:
  candidateBasisPosition: boundedContext | entityOfConcern | entityOfConcernKind | practicalQuestion | optionalProblemCard | candidateSpecificBasis
  admittedBasisValueKindRef: U.Kind
  completenessConditionDescriptionRef: U.Episteme
```

`PatternSolutionSectionRef` is an edition-pinned reference to the cited pattern's `Solution`. A broad result family or pattern title is insufficient.

The completeness condition inherits C.2.1 constitution. Its EntityOfConcern is the reusable candidate-basis position declared by the template; its ClaimGraph states the admitted filler kind and positive completeness condition; its ReferenceScheme explains how current project fillers satisfy that position. It contains no project value and orders nobody to fill a form.

#### E.11:4.4 - Ordinary walkthrough

```text
PublicOrdinaryWalkthrough@FPFReadme <: U.Episteme:
  guidanceRef: PracticalUseGuidance@FPFReadme
  situationDescriptionRef: U.Episteme
  firstResultTemplateRef: PublicPatternUseResultTemplate@FPFReadme
  walkthroughRowRefs[2..*]: PublicOrdinaryWalkthroughRow@FPFReadme
  fullPatternTransitionBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  cgusNonAdmissionRationaleRef: U.Episteme

PublicOrdinaryWalkthroughRow@FPFReadme <: U.Episteme:
  actionOrProposedUseDescriptionRef: U.Episteme
  expectedResultTemplateRef: PublicPatternUseResultTemplate@FPFReadme
  directPatternRef: U.MethodDescription
  directSolutionSectionRef: PatternSolutionSectionRef
  continuationConditionRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
```

An ordinary walkthrough is still an explanation, not a project method, work order, or recommendation. It may contain a local pattern mantra: a short repeatable formulation that keeps that pattern's Solution in attention. It may be presented as a CGUS-demonstrative mantra only when A.22.CGUS admits the represented conditional continuations as a `DemonstrativeUnfoldingSlice@Context`.

#### E.11:4.4.1 - Practical-use carry-through check

Check every published card over its public values. This check evaluates whether the card can lead a reader to the direct pattern and an exact result; it does not create a project instance or an applicability verdict.

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

Each candidate-use template passes only when it names one direct pattern, that pattern's Solution, the exact result kind, the relation signature when the kind admits a relation, every candidate-basis completeness condition, and the pattern that can receive the result. Reject a public project instance, a broad family in place of the result, or a PatternID list without selection conditions. The principal blocked overread states the most consequential false project claim that a reader could otherwise infer from the card.

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

When more than one card remains plausible, compare four things: recognizable-situation fit, difference among first results, direct pattern, and stop or return condition. Keep the comparison in conversation for ordinary bounded use. Open the most promising direct pattern before constructing a project candidate.

The comparison rationale has one public guidance subject and exists before a project candidate is constructed:

```text
PracticalUseCardComparisonRationale@Context <: U.Episteme:
  subjectGuidanceRef: PracticalUseGuidance@FPFReadme
  recognitionReasonDescriptionRef: U.Episteme
  firstResultDifferenceDescriptionRef: U.Episteme
  comparisonRationaleDescriptionRef: U.Episteme
```

Stop inspection when one card has enough recognition and first-result advantage to justify direct pattern inspection, when no remaining card can change the starting choice, or when the inspection budget opens an explicit return. No fixed maximum of three is inferred.

Materialize comparison history only when a named receiving use relies on it:

```text
PracticalUseCardShortlist@Context <: U.Episteme:
  namedRelianceConditionRef: U.Episteme
  receivingUseDescriptionRef: U.Episteme
  receivingUseGoverningPatternRef: U.MethodDescription
  boundedContextRef: U.BoundedContext
  entityOfConcernRef: U.Entity
  entityOfConcernKindRef: U.Kind
  practicalUseQuestionRef: PracticalUseQuestion@Context
  comparisonRefs[1..*]: PracticalUseCardComparison@Context
  selectedStartingGuidanceRef?: PracticalUseGuidance@FPFReadme
  inspectionStopBoundaryRef: PatternUseBoundaryCondition@Context
  returnBoundaryRef: PatternUseBoundaryCondition@Context

PracticalUseCardComparison@Context <: U.Episteme:
  shortlistRef: PracticalUseCardShortlist@Context
  guidanceRef: PracticalUseGuidance@FPFReadme
  recognizableSituationFitRationaleRef: PracticalUseCardComparisonRationale@Context
  firstResultTemplateRefs[1..*]: PublicPatternUseResultTemplate@FPFReadme
  firstResultDifferenceRationaleRef: PracticalUseCardComparisonRationale@Context
  inspectionDisposition: keep | defer | discard | startHere
```

Several plausible cards alone do not make this record current. The named reliance may be transfer, replay, audit, automation, or another use that needs addressable comparison history. Retain only the rows that use needs.

#### E.11:4.7 - Replay and currentness

Replay one public guidance claim from the current card and expansion, the edition-pinned direct `Solution`, the exact result kind and conditional relation signature, the readable coarsening row, the applicable boundary, and the selected walkthrough. The claim remains current only while the direct `Solution` still admits that result and the public situation and question still recognize the same use.

Recheck the smallest affected card slice when the direct `Solution`, result kind, relation signature, recognition condition, first-result difference, or boundary changes, or when use evidence shows a recurrent wrong turn. `G.11` governs edition, telemetry, currentness-window, and decay orchestration; E.11 supplies the card-specific values and change conditions that orchestration inspects.


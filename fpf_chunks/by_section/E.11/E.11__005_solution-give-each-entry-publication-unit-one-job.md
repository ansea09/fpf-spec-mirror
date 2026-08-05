---
chunk_kind: "child"
pattern_id: "E.11"
pattern_title: "First-Practical Entry and Pattern-Use Discoverability Discipline"
section_id: "E.11:4"
section_title: "Solution - Give Each Entry Publication Unit One Job"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11/E.11__005_solution-give-each-entry-publication-unit-one-job.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "E.11 — First-Practical Entry and Pattern-Use Discoverability Discipline"
  - "E.11:4 — Solution - Give Each Entry Publication Unit One Job"
line_start: 76713
line_end: 77048
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
  - "Public first-entry explanation or durable pattern semantics"
  - "admission state"
  - "and dependencies"
  - "query phrases"
---

### E.11:4 - Solution - Give Each Entry Publication Unit One Job

Write the short public entry first: recognizable working situation, practical question, first useful result or honest blocker, direct pattern or small plausible set, and ordinary stop or wrong-turn return. If that prose is truthful and sufficient, stop. Add an expansion, exact result basis, or durable comparison only when ambiguity or a named receiving reliance needs it.

Use this distribution:

| Publication unit | Job | Not its job |
| --- | --- | --- |
| FPF README | Public first-entry situations and practical first results; the current sixteen semantic keys live here. | Pattern authority, full methods, conformance doctrine, or project-instance fields. |
| `Preface` | Plain-engineering narrative explaining the cross-cutting ideas behind those entries. | A second scenario table, PatternID catalogue, or conformance authority. |
| Table of Contents | Search-oriented overview, keywords, query phrases, admission state, and dependencies. | Public first-entry explanation or durable pattern semantics. |
| Pattern `Problem frame` | High-precision local recognition for that pattern's own `EntityOfConcern`, first action, result, and non-use boundary. | A related-pattern fanout list or package-placement rationale. |
| `I.2` or another expanded case | Longer entry disambiguation only when README, ToC, and local recognition are insufficient. | A tutorial obligation for every pattern or a replacement pattern body. |
| Retrieval cards and projections | Thin finding aids that point to the direct pattern and state what they cannot decide. | Evidence, gate, authorization, final interpretation, or shadow authority. |

README is the single editable public entry set. If another publication form needs the same guidance, project it from README rather than maintaining a second version. Put any unique cue in the publication unit whose job matches it, then remove the duplicate row or index.

When discoverability has become use of one selected pattern, continue with `E.11.PUA`. When the live question is which applicable pattern use to recommend or how several uses relate, continue with `E.11.PUR`. Neither continuation turns a public entry order into a universal workflow.

For an FPF-grounded domain or local practice framework, README, Preface, ToC, cards, an all-in-one carrier, a skill pack, retrieval, or a callable access service may expose the entry. `E.4`, `E.4.PFAD`, and `E.4.PFR` still decide framework architecture and authority; the access carrier is not the pattern body merely because a reader reaches FPF through it.

#### E.11:4.1 - Public first-entry scenario and optional expansion

A public entry may be ordinary prose. It is sufficient when these values remain recoverable:

```text
FirstEntryScenario:
  recognizableWorkingSituation
  practicalQuestion
  firstUsefulResultOrHonestBlocker
  directPatternOrSmallPlausibleSet
  ordinaryStopOrWrongTurnReturn
```

The sixteen semantic keys in `E.11:4.5` identify situations, not steps. A reader may inspect any finite plausible set and stop as soon as one direct pattern is worth opening or no remaining entry can change that starting choice.

When an entry must show how the first move may continue without prescribing a workflow, make only these values recoverable: the starting cue, direct pattern or plausible set, first result or blocker, likely next readable outputs, continuation condition, and stop or return. Name candidate loci or an unfolding-family reference only when they change the reader's route. Reference an `A.22.CGUS` `UF.*` family only when the represented conditional structure is actually admitted there; a readable continuation does not become a CGUS structure by being useful.

Use this internal explicitness ladder only when it helps decide where the explanation belongs; do not persist a score for every entry:

| Level | Recoverable explanation | Placement consequence |
| ---: | --- | --- |
| 0 | Topic or slogan only. | Repair the public entry. |
| 1 | Recognizable situation plus a pattern list. | Add the first useful result or blocker and the choice-changing distinction. |
| 2 | First result or blocker is visible, but the direct pattern, boundary, or return is unclear. | Complete the short entry before adding a schema. |
| 3 | Situation, first result or blocker, direct pattern, and stop or wrong-turn return are recoverable. | Ordinary public prose is normally sufficient. |
| 4 | Starting cues, conditional continuations, affected loci, and next readable outputs are also needed. | Use an optional E.11 expansion or expanded disambiguation case. |
| 5 | A worked case, exact result basis, named reliance, and refresh condition have been tested. | Keep this depth only for a recurrent ambiguity or a receiving use that relies on it. |

The ladder is a placement aid, not a completeness target. Higher is not automatically better.


The following context-free schemas are optional authoring support for a card whose result promise, boundary, or later reuse cannot remain truthful from the short prose alone. They are not a public form and contain no reader-project instance:

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

Use `demonstrativeSliceRef` only when the example independently passes A.22.CGUS admission in its declared illustrative bounded context. Otherwise use an ordinary walkthrough; no rationale record is required merely to say that an explanation is not a CGUS slice.

#### E.11:4.1.1 - Cold-reader recognition and grounded public value

Test every public entry against a first-time engineer, engineer-manager, or assisting agent who has not studied FPF. The heading and first sentence name a recognizable working situation; the next useful sentence names an imaginable first result or honest blocker and one direct-pattern distinction that changes the next action. PatternIDs, FPF kind names, internal quality language, and exact assurance fields remain later.

A public value claim is grounded when the reader can recover the project need, first useful result or blocker, why one direct pattern can help, and the ordinary boundary. Add the exact potential-result kind, identity or obtaining basis, result-relative object, or conditional receiver only when omitting it would change the truth, the starting choice, the stop, or a named later reliance. The entry may stay readable prose; the reader never has to fill a card before opening the direct pattern.

Keep the public set representative of FPF's range. Wording and description repair remain visible but do not dominate architecture, problem shaping, work, comparison, evidence, timing, causal use, mathematics, quality, improvement, framework authoring, system recognition, or system delimitation.

#### E.11:4.1.2 - Recover the direct object before a PatternID is known

Some readers arrive before a practical-use key is recognizable: a familiar relation, project, process, case, context, or problem phrase is already blocking the work, but its direct object is not exact. Give such readers an ordinary-language recovery route before asking them to compare PatternIDs. These routes are independent entry alternatives, not stages, a required form, or another card set.

Keep four moments distinct. **Recognition** says why the ordinary situation matches this route. **Selection** chooses the direct pattern whose `Solution` owns the expected first object. **Use** inspects and applies only the branch needed now. The **direct result** exists or the relation obtains only under that selected pattern; the entry cue returns either its smallest usable result or an exact blocker and creates neither.

Apply the same compact route shape each time: recognizable situation; practical distinction; expected first object; exact direct pattern; smallest usable result or honest blocker; ordinary stop; and one neighboring exit. Stop before signatures, card schemas, full methods, owner catalogues, or copied `Solution` prose.

- **An obtaining relation must be referred to, and perhaps distinguished from a repeated episode.** First name the exact participants and the readable direct relation, then open the pattern whose content defines or tests that relation. A current assertion can stop there when later work only needs to know whether the relation obtains. If history, comparison, another relation, or a declared operation application must distinguish this occurrence from another of the same kind, use `A.6.REL` and the relevant direct pattern's same-versus-new-occurrence rule before naming or referencing it. The smallest result is the readable direct assertion or, only when consumed, one recoverably individuated occurrence; a missing participant, predicate, current fact, identity rule, or relation rule is an honest blocker. Stop as soon as the named receiving use can use that result. If no current direct relation can state the needed claim after exact recovery, require `A.6.RCD`; a row, edge, identifier, report, or mention makes no occurrence obtain.
- **Project, process, or case wording no longer reveals the subject of the decision.** Open `A.15.6` and recover the direct subject before using the management label. An actual project is one qualifying composite `U.Work`; a process concern selects one reusable `U.Method`, one exact `U.Structure` selected under `A.22`, or one `TransformationFlowStructure`; a case follows one exact affected referent or claim through the governed change history needed for closure and keeps one named downstream use outside that closure. The smallest result is that exact subject, the direct pattern used to identify or constrain it, and the bounded claim the current decision may make, or a missing identity, parthood, relation, closure basis, or information blocker. Treat *target system* as an ordinary cue for the exact project system-of-interest question. Keep an intended future system in plan or description content; keep plan or decision designation, every work-to-system fact, role interpretation, and role assignment separate. Stop when the direct subject and claim answer the decision. Use `A.1.SCR` only if whether the recovered exact entity is a `U.System` still changes that decision; a project suffix, team, plan, dashboard, or case file supplies no subject identity.
- **A claimed bounded context may be only a label, boundary picture, team, or subsystem.** Open `A.1.1` with the engineering decision, one exact model edition, and its exact use locus. Recover the smallest direct applicability, assigned-Work use, or fixed-content coherence relation first and stop there when it answers the decision. Select a `BoundedModelUseStructure` under `A.22` only when the joint organization itself changes the decision and all four discriminators are exact: independently identified constituents, selected obtaining relation occurrences, applied constraints, and one named selection-use frame. The smallest result is therefore one direct relation or that optional selected structure; a missing constituent, occurrence, constraint, or use frame is an honest no-structure blocker. `Context Mapping` remains a `U.Method`; any cross-context structure needs its own A.22 selection; and a scheme, scope, viewpoint, conforming view, representation, or diagram remains a different object. Stop at the direct relation or selected organization. Use `E.17.0` only when the actual question is whether an exact episteme conforms to a viewpoint and is thereby a view. A bounded-context phrase creates no holon, subsystem, team, structure, relation, viewpoint, view, or representation.
- **Problem-side material may describe a concern without identifying an actual Problem.** Open `C.22.PFR` only when the claim may concern one obtaining `ProblematicForRelation`: an exact actual-condition occurrence and exact problem-criterion-applicability occurrence whose selected input is actually adverse. Keep that occurrence distinct from the predicate, applicability occurrence, assessment or evaluation, assertion and reliance, `ProblemCard`, forecast or modal concern, and current-solvability or continuation claim. The smallest result is an ordinary actual-problem sentence naming condition and value, criterion, entity and use, and applicability window, or an honest non-PFR classification or blocker when the condition, applicability, adverse input, or required PFR rule is missing. Stop as soon as the later use can distinguish actuality from problem-side claim material. Use `C.22.2` when the useful object is a reviewable problem-side card or formulation rather than the world-side relation. One `ProblemCard` may describe no actual PFR; selecting or discovering a method changes only the current solvability or continuation claim, not PFR participants, obtaining, identity, or the adverse condition.

#### E.11:4.2 - Public helper epistemes
These helper epistemes are optional authoring or named-reliance support. Do not open them when the short public entry and direct pattern already make the result and boundary truthful. A pattern reference locates the exact FPF pattern episteme whose content is needed; it asserts `U.MethodDescription` membership only when A.3.2 establishes that membership and the current use depends on it.

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
  resultPatternLocator: U.EntityRef, locating one exact FPF pattern episteme
  resultIdentityOrObtainingBasisTemplateRef: U.Episteme
  resultRelativeGovernedObjectKindRef: U.Kind
  resultRelativeDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  resultRelativeDirectBasisTemplateRef: U.Episteme
  minimumUsableResultDescriptionRef: U.Episteme
  conditionalNextQuestionPatternRef?: U.EntityRef, referencing one exact FPF pattern episteme

PublicPatternUseBoundaryConditionTemplate@FPFReadme <: U.Episteme:
  boundaryConditionKind: recognizableCondition | stop | return | wrongTurnRecovery | strongerNeighbor | missingGovernor | missingInformation
  conditionDescriptionRef: U.Episteme
  relationFunctionClaimRef: U.EntityRef, referencing the exact pattern content that defines or constrains the boundary
  conditionalNextQuestionPatternRef?: U.EntityRef, referencing one exact FPF pattern episteme
  conditionalReceivingPatternPositionDescriptionRef?: U.Episteme

PublicResultCoarseningRow@FPFReadme:
  readableResultPhraseRef: U.Episteme
  exactResultKindRef: U.Kind
  resultIdentificationQuestionRef: U.Episteme
  resultPatternLocator: U.EntityRef, locating one exact FPF pattern episteme
  resultIdentityOrObtainingBasisTemplateRef: U.Episteme
  resultRelativeGovernedObjectKindRef: U.Kind
  resultRelativeDirectBasisKind: directRelationOccurrence | operationApplicationBinding | localRelationBearingClaim
  resultRelativeDirectBasisTemplateRef: U.Episteme
```

An expanded public template asserts no project result and contains no project value. It names only the exact positions needed to keep its promise or blocker truthful: the potential result and how it would be identified, the direct pattern whose content defines or constrains it, and any identity, obtaining, relative-basis, continuation, or receiving-use distinction that changes the branch. Method, plan, dated Work, transformation, evaluation, decision, and receiving-use identities remain absent unless the current promise or later reliance actually depends on them.

The result-relative basis template has exactly one category. A direct-relation template asks for predicate, participants, applicability, obtaining, occurrence identity, and direct governor. An A.6.1 template asks for operation, application, argument or result binding, and direct governor. An A.6.RCD local-claim template asks for one C.2.1 claim episteme with polarity, substrate or constructor, base predicates and their direct patterns, participants, case facts, and any support or warrant required by the later receiving use. The claim does not obtain, and A.6.RCD does not replace the base patterns. Result identity or currentness and result-relative basis are different public questions; they coincide only when the potential result is the same direct relation occurrence used to close the later application.

`conditionalNextQuestionPatternRef` is present only when the public branch itself promises a continuation or names a downstream reliance. A result template without such a continuation leaves it absent. A public `stop`, `missingGovernor`, or `missingInformation` boundary has no receiver. `return`, `wrongTurnRecovery`, and `strongerNeighbor` name a receiver only when that route is part of the branch. The optional obstacle names a recognizable obstacle only when one matters. Practical use may begin from an object to inspect, a result to evaluate, or an existing method to improve without first inventing a problem.

#### E.11:4.3 - Candidate-use templates and basis completeness

This section applies only when an optional exact expansion has been opened because the short public entry cannot carry a truthful promise, blocker, or named reliance on its own.

```text
PublicCandidatePatternUseTemplate@FPFReadme <: U.Episteme:
  templateKey: PublicCandidateUseTemplateKeyValue
  recognizableConditionRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  directPatternRef: U.EntityRef, referencing one exact FPF pattern episteme
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

Exactly one of `expectedResultTemplateRef` and `resultPromiseBlockerRef` is present in an expanded candidate branch. A result promise is admissible only when its potential-result kind, identification question, direct pattern, identity-or-obtaining basis, relative object and category-correct basis, minimum usable result, and any actually current continuation are stateable. A blocker states the missing rule or information and carries no fulfilled result template. Optional omissions cannot masquerade as a weak passing promise.

The completeness condition inherits C.2.1 constitution. Its EntityOfConcern is the reusable candidate-basis position declared by the template; its ClaimGraph states the admitted filler kind and positive completeness condition; its ReferenceScheme explains how later current project fillers satisfy that position. It contains no project value and orders nobody to fill a form.

#### E.11:4.4 - Ordinary walkthrough

An ordinary walkthrough may remain readable prose. Use the following optional helper only when exact result, boundary, or continuation references are needed to keep that explanation truthful:

```text
PublicOrdinaryWalkthrough@FPFReadme <: U.Episteme:
  guidanceRef: PracticalUseGuidance@FPFReadme
  situationDescriptionRef: U.Episteme
  firstResultTemplateRef?: PublicPatternUseResultTemplate@FPFReadme
  resultPromiseBlockerRef?: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  walkthroughRowRefs[2..*]: PublicOrdinaryWalkthroughRow@FPFReadme
  fullPatternTransitionBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme

PublicOrdinaryWalkthroughRow@FPFReadme <: U.Episteme:
  actionOrProposedUseDescriptionRef: U.Episteme
  expectedResultTemplateRef?: PublicPatternUseResultTemplate@FPFReadme
  resultPromiseBlockerRef?: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  directPatternRef: U.EntityRef, referencing one exact FPF pattern episteme
  directSolutionSectionRef: PatternSolutionSectionRef
  continuationConditionRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
```

Where an exact row is used, it carries one result template or public blocker. A walkthrough is still an explanation, not a project method, work order, or recommendation. It may contain a short repeatable formulation of the direct pattern's `Solution`. Call it a CGUS demonstrative slice only when `A.22.CGUS` independently admits the represented conditional structure; an ordinary walkthrough needs no record explaining why it is not such a slice.

#### E.11:4.4.1 - Practical-use carry-through check

Read each published entry first in the form the public will see. A passing ordinary entry exposes the recognizable situation, practical question, first useful result or honest blocker, one direct pattern or small plausible set, and the stop or wrong-turn return. This check creates no project instance, applicability verdict, result entity, relation occurrence, receiving use, or separate positive record.

When an entry needs the optional exact expansion because a promise, ambiguity, or named reliance cannot otherwise remain truthful, use this conceptual view over the already published values:

```text
PracticalUseCarryThroughCheck:
  practicalUseKey: PracticalUseKeyValue
  practicalUseGuidanceRef: PracticalUseGuidance@FPFReadme
  publicSituationDescriptionRef: U.Episteme
  publicPracticalQuestionRef: PublicPracticalUseQuestion@FPFReadme
  publicObstacleDescriptionRef?: PublicPatternUseObstacleDescription@FPFReadme
  candidateUseTemplateRefs[1..*]: PublicCandidatePatternUseTemplate@FPFReadme
  publicStopBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicReturnBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicWrongTurnRecoveryBoundaryRef: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicStrongerNeighborBoundaryRefs[]: PublicPatternUseBoundaryConditionTemplate@FPFReadme
  publicCoarseningRows[]: PublicResultCoarseningRow@FPFReadme
  demonstrativeSliceRef?: DemonstrativeUnfoldingSlice@Context
  ordinaryWalkthroughRef?: PublicOrdinaryWalkthrough@FPFReadme
  principalBlockedOverreadRef?: PublicPatternUseBoundaryConditionTemplate@FPFReadme
```

The view is not a form to complete or a durable check object. Inspect only positions that the expansion actually uses. If an example is needed, use at most one ordinary walkthrough or admitted demonstrative slice for that branch. The demonstrative form must satisfy `A.22.CGUS`; the ordinary form needs no non-admission rationale. State a principal blocked overread only when the public wording otherwise invites a consequential false project claim.

For each expanded candidate-use template, exactly one result promise or exact public blocker is present. A promise identifies the direct pattern and `Solution`, potential-result kind, local identification question, the identity or obtaining basis and result-relative basis that actually make the promise true, the minimum usable result, and a receiver only when that continuation is current. A blocker states the missing rule or information and carries no fulfilled result template. A broad family, generic result relation, omitted value disguised as a weak promise, fabricated project occurrence, or PatternID list without selection conditions does not pass.

#### E.11:4.5 - Sixteen stable practical-use keys


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
| `SYSTEM-RECOGNITION` | Decide whether the exact entity in the claim is a system |
| `SYSTEM-DELIMITATION` | Decide which entities are parts of the system and which relations only cross its boundary |

E.11 records one F.13-form historical read path: `splits(SYSTEM-IN-CONTEXT -> {SYSTEM-RECOGNITION, SYSTEM-DELIMITATION, WORDING, ARCHITECTURE})`. The unchanged F.13 body does not contain this row. The old card had no single surviving public-guidance identity: system recognition, system delimitation, lexical recovery, and architecture have different referents, relations or evaluations, receiving uses, first results, and direct governors. Older writing remains readable through this one read path; current card use names only the four successor keys. A.1.STM is a conditional continuation with a dedicated readable README guide, not a fifth successor key. The split creates no U-kind, relation kind, record kind, result kind, or generic `Context` claim.

README owns the current public cards and their expansions. Preface explains why FPF's distinctions work together. ToC locates pattern families. Full patterns carry methods, conditions, costs, consequences, and exact result semantics. None is a second card store.

#### E.11:4.5.1 - Preface, local recognition, and first-entry terminology

The `Preface` explains why the README entries are credible. It uses plain engineering language before FPF vocabulary and narrates the cross-cutting ideas once rather than copying the scenario set. Its coverage includes transdisciplinary use without collapsing local meaning; local closure in an open world; holons, systems, epistemes, and architecture as structure; `EntityOfConcern` and description/publication/view separation; thinking-through-writing; epiplexity; first-principles-to-work; mathematical lenses and FormalSubstrate distinctions; ontology-first wording repair; evidence/assurance/gate/decision/work separation; characteristic spaces, quality, NQD/OEE, and improvement; novelty, diversity, and SoTA; and didactic primacy. A strict FPF term that carries the explanation receives an immediate plain gloss. Pattern IDs are addresses for stricter treatment, not the main explanatory language.

A pattern's own `Problem frame` is the local high-precision recognition section. It makes recoverable the primary `EntityOfConcern`, working problem, failure if missed, first admissible action, practical result, and ordinary non-use boundary. Add candidate-pattern comparison only when a real discoverability ambiguity exists; otherwise keep cross-pattern comparison in README, ToC, `Relations`, or an expanded case.

Keep these terms stable:

| Term | Use |
| --- | --- |
| `first entry` | General entry from a working project or FPF artifact into the corpus. |
| `first practical entry` | Public form selected by a real working question. |
| `first-entry scenario` | README prose that starts from a recognizable question and names a first useful result and direct pattern family. |
| `first-entry cue` | A phrase, query row, heading, retrieval card, or local recognition passage that helps recover a direct pattern. |
| `first-entry pattern-comparison set` | A small case-relative set used only when the first choice is genuinely ambiguous; it is not a standing index. |
| `expanded entry-disambiguation case` | A longer case used only when README, ToC, and local recognition are insufficient. |

ToC and lexical-query phrases remain finding aids, not alternate names, semantic equivalences, or authority relations. A projection that needs to answer a substantive claim must return to the direct pattern or the pattern for that claim; do not strengthen the projection.

#### E.11:4.6 - Bounded comparison



When more than one card remains plausible, compare four things: recognizable-situation fit, difference among first results or exact public blockers, direct pattern, and stop or return condition. Keep the comparison in conversation for ordinary bounded use. Open the most promising direct pattern before constructing a project candidate.

Keep the rationale in conversation for ordinary comparison. Materialize it only when a named later use needs addressable comparison history; then it has one public-guidance subject and no fabricated project result:

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
  receivingUsePatternLocator: U.EntityRef, locating one exact FPF pattern episteme only when its identity matters to the named reliance
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

Replay one public entry first from its recognizable situation, practical question, first useful result or blocker, direct pattern or plausible set, boundary, and readable walkthrough. Consult the exact helper fields only when that entry actually uses them for truth, disambiguation, or named reliance. The guidance remains current only while its situation and question still point to the same use.

Recheck the smallest affected entry slice when its recognizable situation, question, first result or blocker, direct `Solution`, selection condition, stop, return, or true consumer changes, or when use evidence shows a recurrent wrong turn. Recheck exact result and basis fields only when the changed entry uses them. `G.11` governs edition, telemetry, currentness-window, and decay orchestration; E.11 supplies the entry-specific values and change conditions that orchestration inspects.


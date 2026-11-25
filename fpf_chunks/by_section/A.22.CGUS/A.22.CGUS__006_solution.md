---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Which Continuations Are Available? — Constraint-Governed Unfolding Structure (CGUS)"
section_id: "A.22.CGUS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__006_solution.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "A.22.CGUS — Which Continuations Are Available? — Constraint-Governed Unfolding Structure (CGUS)"
  - "A.22.CGUS:4 — Solution"
line_start: 42400
line_end: 42564
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.29"
  - "C.30"
  - "C.32"
  - "C.32.P2S"
  - "C.33"
  - "C.35"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.23"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
---

### A.22.CGUS:4 - Solution

#### A.22.CGUS:4.1 - Ordinary branch

Decide what would let this recipient act or answer. For example, a venue confirms that a room has been booked for the company’s rehearsal tomorrow and omits the room name. This establishes an existing booking. If the musicians must choose a building before boarding and cannot change it later, the organizer needs the building by departure. If the order asks for the booked room by name, the organizer also needs its identity by the agreed time. Confirmation for the East Room supplies that answer while leaving open whether the company also booked the West Room. For a complete list of its rooms, the organizer needs a booking record or rule that covers all of them. Confirmation naming East as the company’s sole room establishes the booking, identifies a booked room and completes the list. Giving directions to the right building also requires knowing where East is.

1. State the question, the relevant case and time, and the range of results and circumstances it covers. For a decision someone must make, establish who can decide and by when. A question about whether a continuation exists can already have an answer even if no chooser has been designated.
2. For a specified move, take it as the candidate. When finding a way forward is your task, work back from the result each move must make possible. Which change of arrangement, source, timing or actor would provide a genuinely different way under the constraints? Build or reuse candidate continuations on that basis. Where the route leaves a choice, establish who can choose and which information will be available in time. A continuation can also be fixed by its conditions or a schedule.
3. State what must hold for each continuation on which the answer relies. Retain the distinctions that change availability or the grounds the recipient must explain, including dependencies between constituent actions under §4.1.1.
4. Apply those conditions to the facts for this case and window. When the choice may wait for more information, establish what the chooser will know in time and which response will then be possible.
5. Return the conclusion requested. For an identified candidate, give `available`, `blocked` or `unknown` with its grounds. One enabled candidate suffices to establish existence. A rule may also establish existence without identifying the same available action in every case. For a complete set, justify that the candidates or the generating rule cover every admissible continuation and determine which satisfy the conditions. Report a partial set or the outstanding distinction where the grounds fall short. An evaluation error retains its own status.

For example, suppose the rules of a design review permit exactly two review outcomes, acceptance and repair. The team wants the current status of both. Acceptance needs both checks to pass. Repair needs at least one failed check and a repair proposal that concerns this design.

| Alternative | Present facts | Result shown on the card |
| --- | --- | --- |
| Accept the design | Thermal check failed; service check passed. | `blocked — thermal check failed` |
| Repair the design | A check failed and a repair proposal exists, but the proposal-to-design relation has not been established. | `unknown — proposal target not established` |

That corrected card is already useful. It keeps both potential alternatives visible and refuses to invent the missing relation. Retain the rules, facts, and result when the ordinary answer must be reconsidered or compared later. Continue into formal qualification only when a named use depends on the organization's CGUS identity or membership.

When retaining or handing over this card separately, include the two rules above or a usable return to them so the recipient can reconsider availability after the facts change.

##### A.22.CGUS:4.1.1 - Conditions through constituent and encompassing work

When a continuation is a way of performing work, recover the constituent–whole relations in the relevant Method and Work structures that can change availability. For a design, work back from what the encompassing undertaking must supply to the constituent actions and their conditions. For an occurrence, recover what encompassing work was actually performed through those actions. B.1.5.EW supplies that recovery; knowing a Method's description does not supply the capability or resources to perform it.

Distinguish conditions needed at entry, conditions that must remain satisfied during combined performance, and the result required by the encompassing use. In particular:

- a constituent may be individually performable but fail in the needed coordination;
- adequate local resources may be insufficient when constituents share them;
- a constituent result may satisfy its own postcondition while leaving the whole's result unresolved.

For each relevant condition, state what it concerns and how it affects this continuation. Reuse an understood connection or adequate existing basis. Failure of a necessary condition blocks the dependent continuation. A missing fact leaves it unknown when the outstanding fact could change the result. An independent way to learn, obtain support or change the arrangement can remain available. Capability belongs to its performer and conditions under A.2.2; prospective resources and support remain prospective until available.

In the formal branch, express these dependencies with the existing constituents, selected relations, applied constraints and continuation judgements. A temporal edge alone cannot express that one action constitutes part of another ongoing work. Nor does a nested flow position establish Method or Work parthood. A diagram may show the relations together when their meanings remain recoverable.

A constituent's postcondition supports the encompassing conclusion only through the relevant composition and result-use conditions. An expected postcondition is not an observed result. If the displayed account omits conditions needed to perform the whole, state the narrower question it answers. A constituent hierarchy without potential alternatives does not require CGUS qualification.

#### A.22.CGUS:4.2 - Formal qualification branch

Use the four A.22 discriminators to identify one `U.Structure`:

- its constituent references;
- the obtaining relation occurrences it selects;
- the applied constraint claims;
- the named selection-use frame: the question, admissible action, and stop or return condition. Any optional explanatory overread follows F.19:4 and remains outside the identity basis.

CGUS membership adds locally declared loci and bindings that expose how those constituents matter to the unfolding question. The selected relations and constraints must define at least two potential continuation candidates across allowed cases. The current continuation result, a description, or a publication field adds no structure-identity discriminator.

```text
selectedCGUSRef: one A.22 U.Structure
A22IdentityBasis:
  selectedConstituentRefs[]
  selectedObtainingRelationOccurrenceRefs[]
  appliedConstraintClaimRefs[]
  namedSelectionUseFrame:
    questionOrAction: selection question
    admissibleAction
    stopOrReturnCondition
forbiddenOverread?: optional explanation outside A22IdentityBasis
constraintGovernedProfileBasis:
  locusBindingRows[]:
    locusRef: <selectedCGUSRef, locusId>
    locusMeaning: why this constituent matters to this question
    selectedConstituentRef
  potentialContinuationRows[2..*]:
    continuationCandidateRef
    constrainingRelationOccurrenceRefs[]
    appliedConstraintClaimRefs[]
```

`forbiddenOverread?` and `groundedForbiddenOverread?` name the same optional explanation. Use F.19:4's plausible-reader test to decide whether it is useful here.

A CGUS locus belongs to this structure, not to a reusable relation declaration:

```text
CGUSLocusRef := <selectedCGUSRef, locusId>
CGUSLocusBinding := <selectedCGUSRef, locusId, locusMeaning, selectedConstituentRef>
```

The constituent must already belong to the A.22 identity basis. A locus binding neither changes that constituent's kind nor creates a relation. Do not use an A.6.5 `SlotSpec` as a free-standing structure position.

When replay must identify one participant in a relation occurrence, retain the relation definition, the occurrence, the participant order, and the participant binding:

```text
RelationParticipantLocator := <relationDefinitionRef, relationOccurrenceRef, participantOrder, participantRef, relationSignatureRef?, slotSpecRef?>
```

Add a `RelationSignature` and its declaration-local `SlotSpec` together only when an existing reusable declaration is needed for replay. Neither declaration value substitutes for the obtaining occurrence. The CGUS has no ambient context field.

For a finding about one candidate, evaluate its condition. For a current-set result, establish the range of candidate continuations and which of them satisfy their conditions in this case. An immediate local use may keep the following values in the explanation; persistence or replay may place them in an ordinary C.2.1 result episteme.
```text
ContinuationJudgementResult:
  selectedCGUSRef
  continuationCandidateRef
  basisRows[]:
    basisKind: conditionEvaluation | obtainingRelation
    conditionEvaluation?:
      conditionPredicateOrTestRef
      applicabilityResult
      caseInputRefs[]
      currentFactOrEvidenceRefs[]
      requiredPolarity
      observedOutcome: satisfied | notSatisfied | unknown | error
    obtainingRelation?:
      relationDefinitionRef
      relationOccurrenceRef
      participantRefsInPredicateOrder[]
      currentFactOrEvidenceRefs[]
    dependentSelectedRelationOccurrenceRefs[]
  qualificationWindow
  result: enabled | disabled | unknown | error
  reason

CurrentContinuationSetResult:
  selectedCGUSRef
  caseInputRefs[]
  qualificationWindow
  judgementResultRefs[]
  enabledContinuationCandidateRefs[]
  disabledContinuationCandidateRefs[]
  unknownContinuationCandidateRefs[]
  errorContinuationCandidateRefs[]
  stopOrNextAction
  recheckConditions[]
```

A claim reference identifies the claim being applied; it does not show that the test applies or that its condition is satisfied. An obtaining relation is not a condition claim. Keep these two basis branches distinct and derive the case result only from completed judgements. Apply the candidate’s condition logic: for example, one false required conjunct can establish `disabled` despite another unknown conjunct. Retain that unknown basis value; it is not thereby satisfied. An evaluation failure yields `error` under the applicable test, not an invented fact about the candidate.

The membership test concerns potential topology. Changed facts, evidence, test outcomes, or time windows normally change a judgement and the current set, not the structure. Reidentify the A.22 structure when a constituent, selected obtaining relation occurrence, applied constraint, or named use frame changes. Reapply CGUS membership when a locus binding or potential-continuation row changes.

#### A.22.CGUS:4.3 - Four separate decisions

| Decision | Passing basis | Lower result |
| --- | --- | --- |
| A.22 identity and CGUS membership | The four A.22 discriminators identify one structure; its local loci, relations, and constraints define at least two potential continuations across allowed cases. | Name the missing discriminator, binding, relation, constraint, or candidate. Keep the artifact as an explanation. |
| Continuation result for this case | Each candidate retains its condition-evaluation and obtaining-relation basis rows as applicable. A condition-evaluation row keeps the test, applicability, inputs, required polarity, and observed outcome; an obtaining-relation row keeps the definition, occurrence, and ordered participants. Keep the relevant facts or evidence, time window, and an `enabled`, `disabled`, `unknown`, or `error` result. | Mark the affected candidate unknown when the gap prevents deciding its condition; retain an independently established disabled result. Do not revoke an independently established structure. |
| Description or demonstrative-slice adequacy | The description says what it shows and omits for its declared use. Use C.33 only when a carrier's loss affects a declared architecture use within C.33's scope. | Narrow or correct the description. Missing publication or loss material does not deny the structure. |
| A stronger neighboring claim | The method, Work, evidence, assurance, gate, architecture, publication, currentness, or mathematical claim passes its own definition or test. | Stop only that stronger use and name its missing rule or basis. |

Potential branches and joins remain part of the structure even when the present case enables one or none. A linear teaching slice neither removes the other topology nor fixes the order of performed Work.

#### A.22.CGUS:4.4 - Explanations, descriptions, and the non-workflow boundary

An ordinary explanation keeps the subject designated by its claims. When its episteme identity matters, recover that independently identified `EntityOfConcern` under C.2.1. It may already be an A.22 structure whose CGUS membership is unresolved. An assertion of CGUS membership still requires its qualification basis.

After qualification, a whole-structure description may describe loci, bindings, relations, constraints, potential branches, case results, and relevant omissions. A separate demonstrative slice may show one traversal for a declared teaching or comparison use. That slice is a C.2.1 episteme: its claim content, the qualified CGUS as `EntityOfConcern`, and its effective reference scheme jointly recover its identity. `DemonstrativeUnfoldingSlice@Context` is readable lineage for this possibility, not a `U.Kind` or a slice by itself. The slice neither creates nor reidentifies the structure. Use C.33 only when hidden or lost structure in its carrier matters to a declared architecture use within C.33's scope.

Where a slice shows one selected pattern use, it may recall the difficulty through the pattern's `Problem frame` or `Problem`, or recall the way of addressing it through the `Solution`. To show that same use in either form, preserve the selected pattern, working subject and question or proposed use, current conditions, expected result, stop or continuation, and relevant locus bindings. Changing between those formulations changes only the description when the selected pattern use and the qualified structure remain the same. A.22 structure identity still depends on its constituents, selected obtaining relations, applied constraints and named selection-use frame; CGUS membership additionally depends on its locus bindings and at least two potential continuations. Question or action labels establish neither.

Displayed words such as *move*, *next*, and *path* remain ordinary language unless a stronger claim requires another kind. A proposed action, a plan item, a `U.WorkPlan`, dated `U.Work`, and an actual `U.Transformation` are different values. Use `E.10.MOVE`, A.15, and A.3 only when that distinction changes the claim; a display performs and authorizes nothing.

For a transformation-flow use, apply `E.18.3`. It owns the choice among one TFS, one parent-relative `SubflowRef`, or an E.18.NET network and the corresponding position and demonstration locators. CGUS keeps only its local locus bindings and potential topology; it does not copy the network's members, positions, valuations, Work, transformations, or tags.

Cite another pattern only when its content supplies a needed definition, constraint, test, method, evidence rule, or assurance rule. For example, use C.30 for an architecture claim and C.32 for architecture-candidate synthesis, E.23 for repeated quality improvement under a declared evaluation, G.11 for source currentness, C.29 for a mathematical-lens claim, A.10 when the source-to-use account is implicit or must remain replayable, or B.3 for a named assurance claim.

If a durable name or a relation between local senses is the question, use F.17, F.18, or F.9 after the value has been recovered. Do not copy their naming or Bridge procedures into this pattern. Entry cards and publication faces remain under E.11 and E.17.

#### A.22.CGUS:4.5 - Replay and change localization

Replay structure identity from the four A.22 discriminators. Replay CGUS membership from the local locus bindings and potential topology. Replay the case result from each candidate's basis rows, retaining the values required by each applicable condition-evaluation or obtaining-relation branch in `4.2`, the relevant case inputs and facts or evidence, dependent occurrences, time window, continuation result, and reason.

Localize change before reopening wider work. A changed constituent, selected occurrence, constraint, or use frame can reidentify the A.22 structure. A changed locus binding or potential-continuation row reopens CGUS membership. A changed fact, evidence item, test result, or time window normally reopens only the affected judgement and current set. A changed omission reopens the affected description use. A changed neighboring claim stays with the pattern that defines or tests it.


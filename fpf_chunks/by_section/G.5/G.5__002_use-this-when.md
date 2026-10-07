---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Method-Family Registry, Dispatch and Selected-Set Result Declaration"
section_id: "G.5:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__002_use-this-when.md"
commit_sha: "8685aeda98d24b7a7533364cb0df680eccfbfd4c"
heading_path:
  - "G.5 — Method-Family Registry, Dispatch and Selected-Set Result Declaration"
  - "G.5:0 — Use this when"
line_start: 116533
line_end: 116646
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
  - "E.4.PFR"
  - "G.0"
  - "G.11"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "JointUseSet"
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry and eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set result declaration"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:0 - Use this when
When loop-engineering work retains several already identified candidates for downstream use—for example, loop candidates, harness variants, method families, workflow-store entries, or DPF framework candidates—or when several already identified values are all included for one named use, use `G.5` only when the live claim is the selector-facing declaration of that set result. The declared result states the outcome kind, members or keyed member entries, ordering status, named use when applicable, and basis pins. It does not prove that any member improved, that work occurred, that a local choice has been made, or that the result is available to an audience.

Use `Shortlist` or `RankedShortlist` for alternatives retained for later choice. Use `JointUseSet` only when every named member is included for one bounded use. This joint-use branch consumes exact member identities under their own rules; it does not require `MethodRef`, a method-family registry row, or Method classification for framework editions or other non-Method values.

When an earlier choice or other current inclusion basis has already fixed the exact members, use `G.5-6 DeclareSetResult` with those member refs, the named use, inclusion conditions, ordering, and sufficient basis pins. This branch declares selector-facing result content without running method-family registration or `G.5-3 Select`; non-Method members never enter those method-family operations.

For ordinary method-family dispatch, open `G.5` when two or more already admitted Methods are live under grounded selector rows for the same declared task and the current question is the selector-facing set result: which candidates remain admissible, whether the emitted result may truthfully order them, or whether it must be a shortlist, narrowed handoff, abstain, or escalation. If the live question is still one local choice among available options, first constitute the exact C.11 choice assertion under its predicate. Reuse already grounded method-family rows when they exist; do not rebuild a registry on every run. Create a new reusable row only when the grouping itself must recur, carry family-level policy, be versioned, or be published. Crossing, evidence/reliance, assurance, stable public identity, and actual publication are conditional branches, not an entry fee.


For Method dispatch, resolve each exact A.3.1 Method and the row's independent grouping basis under S1 (§4.2). An unresolved member or grouping basis blocks that row. If the claim concerns actual selection, use S3's application and Work-admission conditions; a result declaration alone supplies no such occurrence. S5 governs any separately needed result episteme, public identity and publication claim.

Typical selector situations include:

- Methods or generators from several families are admissible for the same declared task family or work target
- you need one selector to return a `Shortlist`, `RankedShortlist`, `JointUseSet`, one `SpecialistHandoff`, one other narrowed handoff plan, or one abstain outcome without pretending that there is always one scalar winner or that all set results are alternatives
- the declared result must carry enough basis pins for its named downstream use—for example, later comparison, handoff, or escalation—without changing its declared outcome kind or any applicable public selected-set label

#### G.5:0.1 - What goes wrong if missed

- rival families are compared under silent comparator drift, hidden baseline changes, or unspoken crossing costs
- the selector hides one dogmatic winner even when only a partial order is admissible
- selector-facing result content stays hidden inside `C.11`, `C.19`, or `C.24`, so the G.5 result no longer states which upstream choice, pool treatment, or enactment result it consumes and what set result it declares
- exploration, open-ended, or specialization pressure leaks in as one architecture convenience rather than one explicit policy-bound choice

#### G.5:0.2 - What this buys

- one registry that keeps rival method families disjoint but dispatchable
- one selector result form that uses the closed `SelectorOutcomeKind` rules in §4.4b and the closed `SetResultFamily` set when the result is set-shaped
- one trace addressable by DRR and SCR records with explicit basis pins instead of one hidden selector rationale
- one explicit selected-set result that states the outcome kind, applicable public label, retained members or keyed joint-use entries, ordering, named use where required, handoff content, and basis pins instead of leaving them implicit upstream

Registry and dispatch remain the primary selector question here; the explicit selected-set result closes that question without replacing registry or dispatch.

#### G.5:0.3 - First-minute questions

- Which exact members and grouping or inclusion basis are already established?
- Are they alternatives for later choice or members all included for one named use?
- Does the declared comparison justify ordering them?
- Which eligibility, evidence or other receiving-use conditions actually apply?
- What result can be handed over, and what prevents a complete result?
- Does the current question additionally claim actual selection, composition, a relation between meanings, public identity or publication? Open only the applicable branch in §4.2.

#### G.5:0.4 - First output

State one `SelectorOutcome` under §4.4b: its kind, applicable members or keyed entries, ordering, named use and inclusion conditions where required, handoff or blocking content, and sufficient basis pins. Use the quick card in §4.4c. For an ordinary result over grounded rows, direct refs to the grouping, eligibility and comparison basis plus the S3 audit refs suffice; the same compact record can carry them.

A prior C.11 choice, C.19 pool-policy result, C.24 next action or another governed inclusion basis can supply the inputs. G.5 states the resulting membership or handoff. Exact framework editions retain their own identities and use `G.5-6 DeclareSetResult`; E.4.PFR governs their dependency or compatibility claims. Add a stable public identity only when needed. For audience availability, use E.17's source-backed face and E.24.PUB's publication conditions through S5.

#### G.5:0.5 - Minimum ordinary slice and bounded non-use

**Situation.** A pump-maintenance team has two already admitted A.3.1 Methods, `ThresholdTrendReviewMethod-E2` and `SpectralResidualReviewMethod-E1`, behind the exact project-local selector rows `<ThresholdTrendReview-local, R3>` and `<SpectralResidualReview-local, R2>`. These are `MethodFamilyRowRef` values: each fixes its row edition, exact `MethodRef[]`, and declared grouping basis `PumpTriageCandidateGrouping-E1`. The same `TaskSignatureRef=PumpVibrationTriage-T1` and effective reference scheme apply to both. The task signature requires a 24-hour series input and a 30-minute review budget, and both declared Method interfaces meet those constraints. No G.4 CAL gate is current in this ordinary case, so `TaskMapRef` is absent. No admitted comparator justifies ordering one above the other. The live `G.5` question is now how to surface that admissible set, not which pump action a decision-maker should choose.


The minimum truthful result is:

```text
GroundedCandidateRows = [
  { methodFamilyRowRef = <ThresholdTrendReview-local, R3>,
    MethodRef = [ThresholdTrendReviewMethod-E2],
    groupingBasis = PumpTriageCandidateGrouping-E1 },
  { methodFamilyRowRef = <SpectralResidualReview-local, R2>,
    MethodRef = [SpectralResidualReviewMethod-E1],
    groupingBasis = PumpTriageCandidateGrouping-E1 }
]

SelectorOutcome(

  selectorOutcomeKind = SetResultOutcome,
  setResultFamily = Shortlist,
  members = [<ThresholdTrendReview-local, R3>, <SpectralResidualReview-local, R2>],
  ordering = unordered,
  basisPins = [<ThresholdTrendReview-local, R3>,
               <SpectralResidualReview-local, R2>,
               PumpTriageEligibility-E1],
  auditRefs = [DRR-PumpTriage-01, SCR-PumpTriage-01],

  nextUse = maintenance_method_handoff

)
```

**What changes in practice.** The team stops leaving the retained pair implicit in a comparison note and stops saying “the spectral method is best.” It emits one unordered `Shortlist` that another receiver can cite, with the exact survivors and basis visible, while making no local-choice, actual-use, or winning-method claim. A later receiver can request one missing comparator, use the bounded handoff, or open its separately governed decision question without rewriting either Method or inventing a winner.


**Near misses and non-use.** Do not use `G.5` merely because several names appear in one list.

- If the Method-dispatch candidates are only labels, descriptions, cards, or unresolved references, require A.3.1 and C.2.1 before dispatch.
- If the current question is one local choice among already available options, use `C.11`; if it is the policy for retaining or retiring live candidate lines, use `C.19`; if it is enactment planning after choice, use `C.24` for the plan and the applicable A.15/A.6 patterns for actual Work and operation applications.
- If the current object is only a composition sketch, keep the S4 template; use B.1.5 only for a qualified composite Method and A.22 only for an independently selected Structure.
- If no rival candidate set, selector result, narrowed handoff, abstain, or escalation is current, do not open `G.5`.
- Open F.9, A.10, B.3, stable registry or UTS identity, and E.24.PUB only for an actual crossing, relied-on evidence, assurance claim, reusable identity, or audience-availability claim respectively; their absence does not invalidate the smaller same-scheme selector result.

#### G.5:0.6 - Reuse a local grouping, then register it publicly when needed

The pump team in §0.5 already dispatches through R3 and R2. That unordered shortlist requires no new row. If the grouping of both Methods must recur across triage runs, the team can define:

```text
MethodFamilyRowRef = <PumpReviewCandidates-local, R1>
MethodRef[] = [ThresholdTrendReviewMethod-E2, SpectralResidualReviewMethod-E1]
GroupingBasis = PumpTriageCandidateGrouping-E1
EligibilityBasis = PumpTriageEligibility-E1
TaskSignatureRef = PumpVibrationTriage-T1
ComparisonBasis = no admitted ordering; retain admissible alternatives unordered
```

The grouping criterion is “these admitted review Methods are candidates for pump vibration triage using the stated 24-hour input and 30-minute budget.” This project-local row fixes those exact members and basis; changed membership or an action-changing policy makes R2. It requires neither a UTS row nor an AssuranceProfile when this ordinary use has no assurance gate. A later real gate still consumes its required evidence and follows its unknown/fail behavior.

If the team instead intends a stable public registry entry, its proposed public continuation can be `<PumpReviewCandidates, P1>`, linked by an explicit naming/continuity mapping to the local R1 grouping. P1 retains the same exact Method refs and grouping criterion, adds the typed `EligibilityStandardRef` for the pump task and an `AssuranceProfileRef` stating expectations for its declared uses, and satisfies UTS naming/publication requirements under S1 and CC-G5.6. Registration is complete only when those public-contract obligations are met. For this P1 example, `PumpTriageEligibilityStandard-E1` states the two Methods' required 24-hour series and 30-minute budget, with unknown when a required input cannot be determined. `PumpTriageAssuranceProfile-E1` names the evidence expectations and failure behavior for the declared triage uses; `UTS-PumpReviewCandidates-P1` supplies the public name and continuity mapping to R1. P1 registration consumes these completed declarations and that UTS entry alongside the unchanged exact member/grouping basis. A missing one leaves public registration incomplete. The assurance profile supplies no B.3 result.

R1 itself completes through RegisterFamily with the six values shown above: neither AuthoringBase nor AuthoringMinimal is activated because this local grouping has no CG-Frame use. P1 adds the three public references just described and activates UTSWhenPublicIdsMinted. Now suppose a later G.5-3 Select use is governed by `PumpTriage-CG-E1`, whose MinimalEvidence clause requires a valid sensor calibration for the cited vibration series. Its CN/CG editions and frame pins are required. If the calibration input is missing, the evidence predicate is unknown and this example's gate rule returns abstain; neither successful local R1 registration nor completed public P1 registration makes that selection pass.

Making local R1 available to the project audience may itself be an E.24.PUB publication occurrence when that pattern's conditions obtain. Conversely, the intention or declaration of P1 establishes no availability. Neither branch creates a Method or an ontic family relation. Non-Method joint-use members continue through `DeclareSetResult` with their existing identities and inclusion basis.


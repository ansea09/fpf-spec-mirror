---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Method-Family Registry, Dispatch and Selected-Set Result Declaration"
section_id: "G.5:0.5"
section_title: "Minimum ordinary slice and bounded non-use"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__007_minimum-ordinary-slice-and-bounded-non-use.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "G.5 — Method-Family Registry, Dispatch and Selected-Set Result Declaration"
  - "G.5:0.5 — Minimum ordinary slice and bounded non-use"
line_start: 113050
line_end: 113114
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

### G.5:0.5 - Minimum ordinary slice and bounded non-use

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


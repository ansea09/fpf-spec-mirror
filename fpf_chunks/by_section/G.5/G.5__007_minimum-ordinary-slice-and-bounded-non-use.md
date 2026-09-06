---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:0.5"
section_title: "Minimum ordinary slice and bounded non-use"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__007_minimum-ordinary-slice-and-bounded-non-use.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:0.5 — Minimum ordinary slice and bounded non-use"
line_start: 103509
line_end: 103556
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
  - "selected-set publication"
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

This is a positive `G.5` slice because the exact Methods, immutable row-edition refs, grouping bases, task, eligibility basis, survivors, order status, compact audit refs and next use are explicit. It needs no fresh registry row or public `ShortlistId`; the same local senses make F.9 crossing apparatus irrelevant; no reliance or assurance claim is being made; and no E.24.PUB availability occurrence is asserted. The record also stops before claiming dated selection Work or an actual `Select` application. Open those branches only if a later claim actually needs them.


**What changes in practice.** The team stops leaving the retained pair implicit in a comparison note and stops saying “the spectral method is best.” It emits one unordered `Shortlist` that another receiver can cite, with the exact survivors and basis visible, while making no local-choice, actual-use, or winning-method claim. A later receiver can request one missing comparator, use the bounded handoff, or open its separately governed decision question without rewriting either Method or inventing a winner.


**Near misses and non-use.** Do not use `G.5` merely because several names appear in one list.

- If the candidates are only labels, descriptions, cards, or unresolved references, require A.3.1 and C.2.1 before dispatch.
- If the current question is one local choice among already available options, use `C.11`; if it is the policy for retaining or retiring live candidate lines, use `C.19`; if it is enactment planning after choice, use `C.24` for the plan and the applicable A.15/A.6 patterns for actual Work and operation applications.
- If the current object is only a composition sketch, keep the S4 template; use B.1.5 only for a qualified composite Method and A.22 only for an independently selected Structure.
- If no rival candidate set, selector result, narrowed handoff, abstain, or escalation is current, do not open `G.5`.
- Open F.9, A.10, B.3, stable registry or UTS identity, and E.24.PUB only for an actual crossing, relied-on evidence, assurance claim, reusable identity, or audience-availability claim respectively; their absence does not invalidate the smaller same-scheme selector result.


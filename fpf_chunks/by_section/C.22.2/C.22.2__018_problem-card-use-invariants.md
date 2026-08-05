---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard"
section_id: "C.22.2:17"
section_title: "Problem-Card Use Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__018_problem-card-use-invariants.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "C.22.2 — ProblemCard"
  - "C.22.2:17 — Problem-Card Use Invariants"
line_start: 52242
line_end: 52253
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.22.PFR"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
---

### C.22.2:17 - Problem-Card Use Invariants

| Invariant | Requirement |
|---|---|
| One card, one joint EntityOfConcern | One ProblemCard has one ClaimGraph, one independently identified EntityOfConcern, and one effective ReferenceScheme. Several PFR references may share the card only when one direct pattern identifies their joint concern; otherwise split the claims and card. C.22.2:20.1b supplies the joint, forced-split, and many-cards/one-PFR replay. |
| ProblemCard is not PFR | The card may assert, deny, forecast, describe, or discuss solvability, but only C.22.PFR establishes actual Problem obtaining and identity. |
| Claim families remain distinct | Actual-PFR assertion polarity, A.10/B.3 reliance, G.11 currentness, anticipated-condition claims, and method-availability or solvability claims do not collapse. |
| `P2W-ready` is problem-side readiness | The card can be ready as input to P2W or C.22 without being ready for Work execution, gate passage, method selection, evidence reliance, or autonomy. |
| Constitution and qualification stay separate | ClaimGraph, one joint EntityOfConcern, and effective ReferenceScheme constitute the card. ClaimScope, assumptions, window, viewpoint, receiving use, and any exact A.15.6 Work reference stay in their claims and direct relations; no carrier, organization, or setting constitutes the card or PFR. |
| Claims outside C.22.2 stay outside | Evidence, assurance, gate, autonomy, Work, archive, selected-set, comparison, acceptance, representation, temporal, causal, and mathematical-lens claims remain with their governors. |
| Stale or blocked cards state a disposition | A stale, unknown-blocked, changed-representation, or missing-governor card states refresh, retirement, bounded use, `abstainOrNoChange`, or the exact relation reopened. |


---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard"
section_id: "C.22.2:3"
section_title: "Problem-Kind Recovery"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__004_problem-kind-recovery.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "C.22.2 — ProblemCard"
  - "C.22.2:3 — Problem-Kind Recovery"
line_start: 51803
line_end: 51822
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

### C.22.2:3 - Problem-Kind Recovery

`Problem` remains an ordinary word when no FPF-governed claim is being made. Recover it only when wording changes a governed kind, relation, selector use, evidence claim, causal-use claim, assurance claim, decision, or use boundary.

| FPF-governed use | Current recovery | C.22.2 disposition |
|---|---|---|
| Symptom, anomaly, deviation, risk signal, or stakeholder signal | Problem signal or exact signal reference | May trigger a card but is not an actual Problem or complete problem-side claim by itself. |
| Problematic situation | Plain cue for an exact condition, entity, Work, transformation, or relation under its direct pattern | The phrase introduces no `U.Situation`; an actual Problem still requires one obtaining C.22.PFR relation. |
| Actual Problem | One obtaining `ProblematicForRelation` with exact condition and applicability participants | C.22.PFR governs actuality and identity; the card can assert or designate it only after that settlement. |
| Forecast, scenario, counterfactual, or anticipated condition | Exact non-actual claim with assumptions, horizon, and direct governor | Preserve the claim family; do not turn affirmative wording into current PFR obtaining. |
| Method availability or solvability | Claim over admitted methods, evidence, constraints, and one intended use | Selecting a method revises this claim but does not end an actual PFR. |
| Framed problem-side representation | ClaimGraph about one joint EntityOfConcern under one effective ReferenceScheme and ClaimScope | Center of ProblemCard; representation change uses its direct transition, retargeting, Bridge, or wording-use governor. |
| Candidate from archive or retained pool | Member of an exact source set under a retention relation | Preserve `sourceSetRef`, set kind, criterion, budget/window, and non-scalar next use; set semantics remain outside the card. |
| Selected problem from a set-return treatment | Exact selected member under a direct selection relation | The card may carry the member, but selection, parity, archive, and set-return claims remain with G.5, C.18, C.19, G.9, G.11, A.6.P:7a, or C.16.Q as applicable. |
| Problem ready for selector-facing use | Card sufficient to prepare or assign TaskSignature | C.22 constitutes and assigns TaskSignature; C.22.2 does not dump card content into it. |
| Downstream task, method, plan, or performed-Work cue | Exact value or relation under C.22, G.5, A.15, or another direct pattern | Keep only the problem-side cue and stop before claiming the downstream result. |
| E.8 or E.9 `Problem frame` | Authoring or decision-rationale section | Not a ProblemCard and not an actual Problem by heading alone. |

The card may reference candidate `ProblemProfile`, TaskSignature, source set, PFR, forecast, solvability claim, or first-principles cue only when that reference changes its use. No reference is promoted into a local kind or card constitution component.


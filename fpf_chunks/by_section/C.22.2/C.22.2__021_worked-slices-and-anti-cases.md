---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard"
section_id: "C.22.2:20"
section_title: "Worked Slices and Anti-Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__021_worked-slices-and-anti-cases.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.22.2 — ProblemCard"
  - "C.22.2:20 — Worked Slices and Anti-Cases"
line_start: 63153
line_end: 63215
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

### C.22.2:20 - Worked Slices and Anti-Cases

#### C.22.2:20.1 - Five-Case Worked Slices

These rows are recognition slices, not complete Thin cards. Before using one, complete the exact Thin contract in `C.22.2:2.1`; add the relation cues shown here only when they change that card's next use. The compact filled Thin example follows in `20.1a`.

| Case | Problem-side signal | Repaired card use | Boundary preserved |
|---|---|---|---|
| AI and human task transfer rework | Repeated rework appears after transfer between human and agent. | Stabilize signal, EntityOfConcern, effective ReferenceScheme, ClaimScope, acceptance probe, and safe-call or Work relation before another delegation. | The card is not a prompt retry instruction and does not justify another delegation. |
| Musical mastery tempo drift | Practice tempo drifts away from the intended mastery band. | State the temporal claim, practice scheme and scope, acceptance probe, and `C.27` relation when tempo, rhythm, recovery, or learning rate changes the next use. | A trend line is not an intervention model or evidence of mastery. |
| Customer-service escalation after a policy or interface change | Escalation volume rises after the change. | Stabilize affected customer hand-off, acceptance probe, risk boundary, measurement relation, and causal-use relation when that relation is being made. | Escalation volume is not an automatic fix request, staffing plan, rollback order, or causal proof. |
| Literature-synthesis anomaly before method selection | An anomaly does not fit current category labels. | Preserve rival formulation, EntityOfConcern, evidence need, bridge, representation, or mathematical-lens relation when that relation is being made, and next discrimination action. | The anomaly is not proof for a new theory or a selected research method. |
| Selected-set candidate before P2W | A retained candidate from a front or pool looks promising. | Preserve `sourceSetRef`, source-set kind, selection or retention criterion, non-scalar next use, and only the currentness or window on which that use relies. | Set membership is not selected-solution proof, priority score, or work authorization. |



#### C.22.2:20.1a - Compact P2W-ready Disposition Slice

Consider a support team seeing repeated reopened hand-offs after a new interface policy. Its source episteme `SupportHandoffPolicy-E7` contains the two clauses compared below. The incoming request says "rewrite the escalation workflow." The card first identifies the concern and improvement probe; selecting a rewrite requires its own grounds.

The first-line entry uses "complete" for sending the case; the specialist entry uses it for accepting the case. Put those two meanings together: the same status names different events. This comparison supplies the question "Which event completes the hand-off?" and identifies the ambiguity retained below. It does not establish the cause of reopening. If both entries instead mean acceptance, this contrast no longer supports an ambiguity claim; retain the reopening signal and reopen the formulation.


| Card field | Filled value |
|---|---|
| Source signal | Escalations reopen after hand-off from first-line support to specialist support. |
| Problem-side EntityOfConcern | The identified source episteme `SupportHandoffPolicy-E7`, whose two clauses use the same completion label for different events. |
| Effective ReferenceScheme and ClaimScope | Scheme: support-interface hand-off under the new policy edition. ClaimScope: SupportOps-EU. |
| Claim family | Descriptive claim about the two policy clauses and their different completion meanings. The prediction that reopened escalations will continue while this wording remains is an untested hypothesis, not an established forecast or causal result. No actual PFR is asserted. |
| Ground for addressing the concern | The two policy clauses attach different events to one completion label, and reopened cases make clarification useful. The request to "rewrite the escalation workflow" proposes a solution without yet establishing that a rewrite is needed. |
| Improvement check or acceptance probe | Sample reopened cases; accepted improvement means fewer reopened hand-offs within that ClaimScope and window without increasing unresolved safety, compliance, or customer-impact exceptions. |
| Honest next use | Use E.18.1 to carry only the hand-off-ambiguity claim and acceptance probe into one next relation question. Do not select a method, approve a rewrite, pass a gate, or authorize Work. |
| Qualification window (current here) | Two-week incident window under the stated policy edition. |
| Problem-formulation follow-up reason (current here) | Resolve which event the policy means by completion. Examine System, assignment, Method, Work or policy-boundary relations only if that clarification exposes a question that depends on them. |
| Validation boundary (current here) | Same support interface, policy edition, ClaimScope, incident window, and source logs; refresh if the scheme, scope, source logs, window, or acceptance probe changes. |
| Readiness disposition | `P2W-ready` only for the narrow next use above, because the card carries the ambiguity claim, rejects the preselected Work request, and supplies an acceptance probe. |
| Subject-pattern cues (current here) | Use the applicable A.6 declaration or interface rule if completion semantics remains unresolved. A.10 governs a relied-on claim and G.11 its currentness. Add A.2/A.2.1/A.13/A.15 for an actual classification, assignment or dated Work claim; F.6 only for precise assignment attribution, and A.21 only for a gate claim. |

The P2W export is narrow: signal, joint EntityOfConcern, effective ReferenceScheme, ClaimScope, claim family, not-wish or not-preselected-Work reason, improvement check or acceptance probe, and honest next use. In this case it also carries the qualification window, validation boundary, follow-up reason, and subject-pattern cues because the stated next use relies on them. Add freshness, unknown handling, source-set, representation, evidence, or other conditional content only when it is current. If the improvement check or acceptance probe is missing, the card stays reviewable-only or source-finding and cannot claim `P2W-ready`. If the next user wants evidence sufficiency, a gate decision, Work authorization, or selected method, the card preserves the cue and its direct governor carries that downstream claim.

#### C.22.2:20.1b - Card/PFR Cardinality Replay

Every PFR reference below designates a world-side occurrence established under C.22.PFR; no card-side fact supplies its participants, adverse extent, or identity. `PFR-InspectionAssignment-17` and later `PFR-InspectionAssignment-18` are the two Robot-7 occurrences replayed in C.22.PFR:5.

For the unrelated branch, `InspectionReleaseAssignment` is a declared `U.SystemRoleAssignment` species. Occurrence `InspectionAssignment-27` has admitted System `Robot-8` as holder and local kind `InspectorSystemRole` as assigned-kind value. It obtains without interruption on `[2026-07-13T10:00, 2026-07-13T10:30]`; `MaintenanceRoles-2026`, `Maintenance-Scheme-A`, and the interval description interpret or describe the assertion but are not extra assignment participants.

`Robot8ReleaseCriterionApplicability-4` uses predicate `NoInspectorSystemRoleBeforeValidation-v2`, maps the occurrence's assigned-kind participant to the adverse nominal coordinate and its holder to `Robot-8`, and names `Robot-8`, its release ClaimScope, and `[2026-07-13T09:30, 2026-07-13T12:00]` as the other applicability participants. Those facts establish `PFR-InspectionAssignment-27` on `[2026-07-13T10:00, 2026-07-13T10:30]` under C.22.PFR.

| Branch | Exact card-side objects | Mechanically recoverable result |
|---|---|---|
| One joint multi-PFR card | `Robot7ReleaseEpisodesCard-E1 = <CG-Robot7-ReleaseEpisodes-E1, Robot-7, Maintenance-Scheme-A>`. The exact ClaimGraph contains two affirmative assertion nodes designating `PFR-InspectionAssignment-17` and `PFR-InspectionAssignment-18`. A.1 independently identifies `Robot-7 : U.System`, and both PFRs have that same System as their applicability-derived problem-for entity. | One ClaimGraph has one direct, genuinely joint EntityOfConcern, so one card carries both PFR references. The card records two occurrences; it does not merge them. |
| Unrelated PFRs force split | Proposed `CG-Mixed-RobotReleaseProblems-E0` contains `PFR-InspectionAssignment-17` about A.1-identified `Robot-7` and `PFR-InspectionAssignment-27` about separately A.1-identified `Robot-8`. No direct pattern in this replay identifies one joint EntityOfConcern for those claims; a list of the two Systems is not one. | `E0` cannot constitute one ProblemCard. Split it into `CG-Robot7-ReleaseProblem-E1` in `Robot7ReleaseProblemCard-E1` and `CG-Robot8-ReleaseProblem-E1` in `Robot8ReleaseProblemCard-E1`, each with its own exact System EntityOfConcern and effective scheme. |
| Several cards retain one PFR | `Robot7SafetyCard-E1 = <CG-Robot7-Safety-E1, Robot-7, RobotSafety-Scheme-A>` qualifies its designation by `SafetyAssuranceViewpoint-E1` and receiving use `AutonomousInspectionReleaseReview-E1`. `Robot7StaffingCard-E1 = <CG-Robot7-Staffing-E1, Robot-7, MaintenancePlanning-Scheme-B>` qualifies its designation by `MaintenancePlanningViewpoint-E1` and receiving use `InspectionAssignmentRepairPlanning-E1`. Both exact ClaimGraphs designate `PFR-InspectionAssignment-17`. | The differing ClaimGraphs, schemes, viewpoints, and receiving uses identify or qualify two cards and their claims; the PFR reference remains exactly `PFR-InspectionAssignment-17`. Revising, merging, splitting, publishing, or replacing either card changes no PFR participant or adverse episode. |

#### C.22.2:20.2 - Anti-Cases


| Anti-case | Correct result |
|---|---|
| The card is cited as safety acceptance, gate passage, tool-call action invitation, or work authorization. | Apply the pattern for the safety, gate, autonomy, work, evidence, provenance, or assurance claim; keep only the problem-side cue in the card. |
| A mathematical phrase is added because it sounds rigorous. | Remove it unless a supported consequence improves the formulation. Use domain mathematics directly when adequate, and C.29 for a live representation or transfer question. |
| A source archive produces a "best" problem by one score. | Use source-set and selected-set patterns; the card carries a non-scalar source-set reference, criterion, and problem-side next use. |


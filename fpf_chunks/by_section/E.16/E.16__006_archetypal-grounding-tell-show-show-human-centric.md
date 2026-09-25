---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:5"
section_title: "Archetypal grounding (Tell-Show-Show; human-centric)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__006_archetypal-grounding-tell-show-show-human-centric.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:5 — Archetypal grounding (Tell-Show-Show; human-centric)"
line_start: 90815
line_end: 90841
dependencies:
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.24"
  - "C.9"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.17"
  - "F.4"
  - "F.6"
  - "F.8"
  - "G.10"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "autonomy budget"
  - "autonomy ledger"
  - "guarded enactment"
  - "override speech act"
  - "scout/probe/commit checkpoint"
---

### E.16:5 - Archetypal grounding (Tell-Show-Show; human-centric)

**Show-A (enactment-bound mobile robot).**
The autonomy claim names navigation Method `Navigate_v3`. Its enactment-bound budget names `NavigatorSystemRole` as the consumer kind, robot `Robot_R7` as holder, exact assignment `R7-NavigatorAssignment-2026`, and the current warehouse-navigation Work item. It also names the warehouse policy, ClaimScope and shift window, `FloorSupervisorSystemRole` as the override-authority kind, supervisor System `Mina`, her exact assignment, and the independently obtaining authority relation for pause and resume Work.

The declared A.2.7 relation is `NavigatorSupervisorIncompatibility`; its predicate prohibits the same System from holding both assignments for the same navigation Work during overlapping windows. The gate resolves both A.2.1 assignments and their holders and admits the override path because the actual pair does not match that prohibited case and the independent authority relation is current. The budget then supplies `action_tokens=10 k steps/day`, `risk_bands={maxSpeed <= 1.2 m/s, minDist >= 0.5 m}`, and `resource_caps={battery >= 20%}`. Ledger entries decrement the action budget and record distance checks. Depletion stops autonomous movement.

For a proposed pause/resume of that current navigation Work, name the override action and check its permission before it occurs. The navigation Work and its existing ledger remain unchanged by the proposal. Only the performed, independently admitted override adds override Work and its actual budget delta.

**Show-B (unscheduled, action-bound, then performed release).**
An unscheduled budget names the deployment/authorizer local kinds, policy, limits and prospective incompatibility species without inventing assignments or release Work. When release promotion is proposed, its local action rule fixes artifact `Release-E7`, target `Production-East`, operation `promote`, and intended window 14:00–14:15. Use its existing WorkPlan action locator if available; the rule otherwise identifies those values directly. Duplicate request IDs for these same values name the same proposed action.

`ReleaseDutyProspectiveIncompatibility` has the unordered kind pair {DeployerSystemRole, ReleaseAuthorizerSystemRole}. Under its adopted policy it prohibits the same actual holder's obtaining assignments to those kinds for the same proposed release action during overlapping allocation windows. Its applicability and meaning-changing policy edition are explicit. The kind relation obtains independently of whether anyone attempts a prohibited allocation. The illustrative `ReleaseEntryProfile-E1` requires allocation, authority, budget and the action’s other declared guards. It maps known prohibition, unknown allocation, and missing/unrun required allocation checks to `block`; satisfactory current results map to `pass`. Its hold consequence is to establish the allocation facts and recheck within the proposed action window. This is the case’s explicit profile, not an A.21 default.

| Case | Receiving result |
| --- | --- |
| No release scheduled | The budget remains prospective; no action or nonexistent assignments are filled. |
| Two distinct assignment IDs have the same System holder for this action and overlapping windows | The prospective predicate finds the prohibited allocation; the profile maps it to `block` before any release performance. Passing authority or budget cannot override it. |
| The overlap result is `unknown`, while authority and budget pass | `ReleaseEntryProfile-E1` maps unknown allocation to `block`; the aggregate of block, pass and pass is block. Hold promotion and establish the missing overlap facts. |
| The required allocation check has no result or was not run | Keep the missing/`notRun` check in the required set. This profile maps it to `block`; run or recover the check before reevaluating. |
| Different permitted holders, current independent authority, budget and all other required guards pass | A.21 permits the bounded promotion. No release Work is yet claimed. |
| The rejected release is resubmitted under a new request ID | The same-action rule preserves the subject, so the allocation check is not bypassed. |
| The window changes to 15:00–15:15 | The explicit continuation rule may retain the continuing release action when artifact, target and operation are unchanged and rescheduling is linked. Permission for 14:00–14:15 does not extend; evaluate the new window and allocation. |
| The permitted promotion is performed | A.15.1 identifies actual Work from its performance grounds. The ledger records that Work and policy-defined budget delta; a separate exact action match connects it to the applicable prior permission. |

The declaration's `decision_tokens=3/day` and `error-budget burn <= 2%/day` remain typed limits checked under their policy. This branch neither weakens the actual-Work incompatibility species nor treats a gate as Work admission.


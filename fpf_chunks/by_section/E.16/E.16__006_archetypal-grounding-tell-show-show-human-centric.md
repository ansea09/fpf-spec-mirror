---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:5"
section_title: "Archetypal grounding (Tell-Show-Show; human-centric)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__006_archetypal-grounding-tell-show-show-human-centric.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:5 — Archetypal grounding (Tell-Show-Show; human-centric)"
line_start: 79942
line_end: 79953
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

The declared A.2.7 relation is `NavigatorSupervisorIncompatibility`; its predicate prohibits the same System from holding both assignments for the same navigation Work during overlapping windows. The gate resolves both A.2.1 assignments and their holders and admits the override path because the actual pair does not match that prohibited case and the independent authority relation is current. The budget then supplies `action_tokens=10 k steps/day`, `risk_bands={maxSpeed <= 1.2 m/s, minDist >= 0.5 m}`, and `resource_caps={battery >= 20%}`. Ledger entries decrement the action budget and record distance checks. Depletion stops autonomous movement; it does not make either assignment or the incompatibility relation act.

**Show-B (prospective, then enactment-bound deployment).**
A prospective deployment budget names the autonomy claim, `DeployerSystemRole` and `ReleaseAuthorizerSystemRole`, the production-promotion situation, deployment policy, ClaimScope, daily window, guard set, and the exact A.2.7 incompatibility relation. It leaves holder Systems, assignments, deployment Work, and authority-relation occurrence empty because no release has been scheduled. Nothing is invented to make the template look complete.

When a release is scheduled, an enactment-bound edition names the deployment service System, its exact deployer assignment, the release Work, the authorizer System and assignment, and the independently obtaining release-authority relation. The receiving check tests the two assignments against the declared predicate for holder, same Work, overlap, and applicability; it then applies `decision_tokens=3/day`, `error-budget burn <= 2%/day`, and the ordinary deployment guards. A kind label or the notation `role A perpendicular role B` would not close either check.


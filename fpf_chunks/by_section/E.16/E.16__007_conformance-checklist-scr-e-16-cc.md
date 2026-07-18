---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:6"
section_title: "Conformance Checklist (SCR — E.16‑CC)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__007_conformance-checklist-scr-e-16-cc.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:6 — Conformance Checklist (SCR — E.16‑CC)"
line_start: 74218
line_end: 74229
dependencies:
  - "A.13"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
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

### E.16:6 - Conformance Checklist (SCR — E.16‑CC)

| ID            | Requirement                                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **E.16‑CC‑1** | Any autonomy claim **MUST** reference an **AutonomyBudgetDecl** in the same `U.BoundedContext`.                                                                             |
| **E.16‑CC‑2** | **Method steps** that depend on autonomy **MUST** declare `requiresAutonomyBudget: AutonomyBudgetDecl.id` (and `requires: [RoleX]`) and **MUST** be Green‑Gated by the budget’s guards at enactment. |
| **E.16‑CC‑3** | A **Work** admitted under autonomy **MUST** carry an **AutonomyLedgerEntry** with deltas and guard verdicts.                                                                |
| **E.16‑CC‑4** | **Overrides** are **SpeechActs** with SoD enforced (`⊥` between consumer and overrider roles); each override creates a ledger entry.                                        |
| **E.16‑CC‑5** | **Depletion** **MUST** block autonomy‑gated steps until a **ResumeAutonomy** SpeechAct passes SoD and guard checks.                                                         |
| **E.16‑CC‑6** | **UTS rows** for autonomy‑bearing Roles/Methods/Services **MUST** include `AutonomyBudgetDeclRef`, `Aut-Guard policy-id (PolicyIdRef)`, `OverrideProtocolRef`, `Scope (G)`, and `Γ_time`. |
| **E.16‑CC‑7** | When bounded specialization scouting is in scope, scout budget, probe budget, and commit checkpoint **MUST** stay explicit, and a successful probe **SHALL NOT** count as automatic committed rollout. |


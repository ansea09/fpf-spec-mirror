---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:6"
section_title: "Conformance Checklist (SCR - E.16-CC)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__007_conformance-checklist-scr-e-16-cc.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:6 — Conformance Checklist (SCR - E.16-CC)"
line_start: 81312
line_end: 81323
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

### E.16:6 - Conformance Checklist (SCR - E.16-CC)

| ID            | Requirement |
| ------------- | ----------- |
| **E.16-CC-1** | Every autonomy claim **MUST** reference a named, versioned **AutonomyBudgetDecl** that states its binding state and identifies the claim, consumer local kind, working situation, policy, ClaimScope, qualification window, budget, override-authority local kind and policy, and exact A.2.7 separation-of-duties relation. A prospective declaration may omit actual holders, assignments, Work, and authority occurrence; all become mandatory in an enactment-bound edition before Work admission. |
| **E.16-CC-2** | A Method step that depends on autonomy **MUST** name the exact required local kind and `requiresAutonomyBudget`. Green-Gate **MUST** resolve the performer System, exact A.2.1 assignment, target Work, scope and window, assignment state, budget, and guards; any required classification judgment is separate. |
| **E.16-CC-3** | Work admitted under autonomy **MUST** have an `AutonomyLedgerEntry` that identifies the Work, performer System, exact assignment, budget edition, deltas, and guard verdicts. |
| **E.16-CC-4** | An override **MUST** be SpeechAct Work performed by an admitted System under an exact A.2.1 assignment. The receiving check **MUST** apply the named A.2.7 incompatibility predicate to both actual assignments, holders, target Work, overlap window, and applicability, reject a prohibited joint allocation, and independently confirm the authority relation. Kind labels or `role perpendicular role` notation are insufficient. |
| **E.16-CC-5** | Depletion **MUST** block autonomy-gated steps until `ResumeAutonomy` passes the actual-assignment separation-of-duties check, independent authority check, and ordinary guards. |
| **E.16-CC-6** | A UTS row that carries an autonomy claim about Work described through a local system-role kind, Method, or Service **MUST** include `AutonomyBudgetDeclRef`, binding state, Aut-Guard policy id, `OverrideProtocolRef`, ClaimScope, and Γ_time window; an enactment-bound row also exposes the actual binding references needed by its receiving use. |
| **E.16-CC-7** | When bounded specialization scouting is in scope, scout budget, probe budget, and commit checkpoint **MUST** stay explicit, and a successful probe **SHALL NOT** count as automatic committed rollout. |


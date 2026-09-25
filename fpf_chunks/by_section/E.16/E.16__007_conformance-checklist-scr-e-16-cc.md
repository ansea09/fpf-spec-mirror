---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:6"
section_title: "Conformance Checklist (SCR - E.16-CC)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__007_conformance-checklist-scr-e-16-cc.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:6 — Conformance Checklist (SCR - E.16-CC)"
line_start: 90842
line_end: 90853
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
| **E.16-CC-1** | Each autonomy claim cites a named/versioned budget with claim, consumer kind, situation, policy, scope/window, limits, override rule and exact A.2.7 species. Prospective budgets may omit actions/assignments; action-bound permission resolves the proposed action and real allocation/authority; enactment-bound adds independently admitted actual Work. |
| **E.16-CC-2** | Green-Gate decides the A.21 prospective work-entry claim and bounded action, resolving its identity/continuation, real holder/assignment/state, authority, scope/window, remaining budget, incompatibility and guards. Changed permission-relevant windows require recheck; request respelling does not create another action. |
| **E.16-CC-3** | Work admitted under autonomy **MUST** have an `AutonomyLedgerEntry` that identifies the Work, performer System, exact assignment, budget edition, deltas, and guard verdicts. |
| **E.16-CC-4** | A proposed override passes its applicable A.2.7 species and independent authority check before performance. An existing target Work is distinct from that proposal. Only a performed, A.15.1-admitted override is recorded as overrideWork with the applicable delta and policy-supported match to prior permission. |
| **E.16-CC-5** | Depletion **MUST** block autonomy-gated steps until `ResumeAutonomy` passes the actual-assignment separation-of-duties check, independent authority check, and ordinary guards. |
| **E.16-CC-6** | A UTS autonomy row carries the budget edition/state, guard policy, override protocol, scope/window, action/allocation refs when action-bound and actual Work refs when enactment-bound. |
| **E.16-CC-7** | When bounded specialization scouting is in scope, scout budget, probe budget, and commit checkpoint **MUST** stay explicit, and a successful probe **SHALL NOT** count as automatic committed rollout. |


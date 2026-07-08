---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:7b"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:7b — Common Anti-Patterns and How to Avoid Them"
line_start: 22476
line_end: 22484
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "B.3"
  - "C.32.P2S"
  - "E.17"
  - "U.Method"
  - "U.MethodDescription"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "forecast"
  - "intent"
  - "plan"
  - "schedule"
---

### A.15.2:7b - Common Anti-Patterns and How to Avoid Them

- **Plan-as-actual.** Do not treat a Gantt bar, Kanban ticket, shift rota, or calendar booking as performed work; create or cite the `U.Work` occurrence when work happens.
- **Workflow-as-schedule.** Do not treat a method description or flowchart as a plan; make a `U.WorkPlan` only when intended windows, constraints, role-admission conditions or intended role values, and baselines are current.
- **Assignment-by-plan.** Do not treat an intended performer in the plan as a `U.RoleAssignment` satisfying the governing role, holder, and bounded-context constraints for the work interval; validate assignment when the work occurrence is prepared or recorded.
- **Budget-as-cost.** Do not book planned budgets as performed resource use; performed values belong to `U.Work`.
- **Plan-shape overreach.** Do not force performed work to match plan decomposition; use fulfilment and variance relations.
- **Evidence-note-as-claim.** Do not treat evidence-reference notes, gate-preparation notes, or source-currentness requests as evidence, gate passage, assurance, or release authorization.


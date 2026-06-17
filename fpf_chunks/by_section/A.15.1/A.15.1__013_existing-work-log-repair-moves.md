---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:12"
section_title: "Existing work-log repair moves"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__013_existing-work-log-repair-moves.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:12 — Existing work-log repair moves"
line_start: 21027
line_end: 21036
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actuals"
  - "event"
  - "execution"
  - "log"
  - "occurrence"
  - "run"
---

### A.15.1:12 - Existing work-log repair moves

1. **Backfill links.** For existing logs, create work-occurrence records and attach `enactsMethod`, `methodDescriptionRef` when current, and `performedBy`.
2. **Name the context.** Pick the judgement context explicitly; add Bridges if multiple contexts accept.
3. **Record the episode policy.** Decide when an interruption keeps identity or forces a new run.
4. **Choose Γ\_time per KPI.** Put "union" or "hull" in the KPI definition so disputes expose the coverage policy instead of hiding it.
5. **Set an overlap policy.** Write one sentence on how shared costs are allocated; apply consistently.
6. **Pull plans out.** Move calendars to `U.WorkPlan`; let Work record performed values.
7. **Parameter blocks.** Make parameters explicit and bind them at start; root-cause analyses become easier.


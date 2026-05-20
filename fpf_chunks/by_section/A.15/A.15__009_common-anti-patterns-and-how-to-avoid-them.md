---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 19726
line_end: 19737
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.15.1-A.15.4"
  - "A.15.4"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.24"
  - "C.26.2"
  - "E.16"
  - "E.17"
  - "E.17.EFP"
keywords:
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.WorkPlan"
  - "actual U.Work"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "source-restoration boundary"
  - "work admission display"
---

### A.15:8 - Common Anti-Patterns and How to Avoid Them

- **Role-as-part.** Do not place `U.Role` or `U.Capability` inside structural `partOf` decomposition; keep them contextual and functional.
- **Recipe-as-evidence.** Do not treat a `U.MethodDescription` or SOP as proof that work occurred; record dated `U.Work` instead.
- **Plan-as-actual.** Do not let schedules, calendars, or intended assignments stand in for actual execution; use `U.WorkPlan` for intent and `U.Work` for actuals.
- **Capability-as-work.** Do not treat possession of a capability as if the task has already been performed; capability supports execution but is not execution.
- **Approval collapse.** Do not merge approval or authorization speech acts into the operational step they open; model them as distinct communicative `U.Work` when they change authority state.
- **Process soup.** Do not leave "process", "workflow", or "activity" uninterpreted in load-bearing passages; resolve the word to method, plan, or work.
- **Briefing-as-execution-cue.** Do not treat a lighter review note, rollout summary, or redacted operations note as if it already authorized execution, approval, gate passage, or a work plan. Reopen the governing method, plan, approval, or evidence source before work proceeds.
- **P2W publication as work occurrence.** Do not treat a principle scheme, functional diagram, scenario, screen, or explanation as if it were performed `U.Work`, evidence, gate passage, or engineering justification. Use it only for the exact method or work-planning support it carries, then recover the exact project-side FPF kind and reference that actually supports any unsupported claim.
- **Visible item as work source.** Do not treat a dashboard tile, credential display, copied approval, generated explanation, provenance label, command-like cue, or composed source chain as approval, permission, gate passage, role or status currentness, work occurrence, evidence, or assurance by appearance. Use `A.15.4` for the source-restoration question and keep `A.15` for `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation.


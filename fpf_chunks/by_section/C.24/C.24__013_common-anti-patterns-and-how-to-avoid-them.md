---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 52995
line_end: 53004
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.28"
  - "C.5"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.23"
  - "E.3"
  - "E.5"
  - "G.5"
  - "G.6"
  - "G.9"
  - "U.PromiseContent"
  - "U.WorkPlan"
keywords:
---

### C.24:8 - Common Anti-Patterns and How to Avoid Them

- **Treating route description as plan.** Avoid by keeping callable logic in `ATC.CallRouteDescription` and keeping `ATC.CallPlan` as one `U.WorkPlan` whose steps select exact Methods and cite descriptions separately.
- **Treating MethodDescription as enacted Method.** A route document, schema or endpoint description is an episteme, not the world-side way of doing and not what a call enacts. Recover the exact `methodRef`; otherwise keep the candidate in probe state or exit with a missing Method relation.
- **Treating CallGraph or service response as Work.** A graph row and response carrier may evidence a call but do not establish its occurrence, performer, assignment, interval or `enactsMethod`; recover those A.15.1 facts independently.
- **Treating planning as execution.** Avoid by publishing actual burn only through `CheckpointReturn`, `Work`, and `CallGraph`, not inside the `CallPlan` field set.
- **Burning enactment budget while the question under repair is still upstream choice or pool policy.** Avoid by rerouting unresolved fixed-option choice to `C.11` and unresolved live-pool governance to `C.19` before building one call plan.
- **Counting a successful probe as committed rollout.** Avoid by publishing one `CheckpointReturn` with a visible commit trigger instead of smuggling rollout through a positive scout result.
- **Hiding stop conditions or replan triggers.** Avoid by making them part of the public `CallPlan` field set rather than one private implementer intuition.


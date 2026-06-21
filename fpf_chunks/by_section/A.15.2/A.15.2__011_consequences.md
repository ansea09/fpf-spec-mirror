---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:7c"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__011_consequences.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:7c — Consequences"
line_start: 21951
line_end: 21959
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.3"
  - "A.15.4"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "B.3"
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

### A.15.2:7c - Consequences

| Benefit | Trade-off and mitigation |
| --- | --- |
| Plans become inspectable without being confused with performed work. | More explicit records; mitigate by using compact `PlanItem` values for ordinary coordination. |
| Variance becomes meaningful because planned baseline and performed work stay separate. | Requires discipline around baselines; keep baseline and version visible on the plan. |
| Cross-role and cross-context coordination becomes safer. | Requires bridge checks when contexts differ; name only the bridge needed for the planned use. |
| P2W carry-through can prepare work without pretending work already happened. | Use `A.15.1`, `A.15.3`, `A.15.4`, `A.10`, `B.3`, `A.20`, or `A.21` only when the performed-work, planned-baseline, source-restoration, evidence, assurance, gate, or constraint relation becomes current. |


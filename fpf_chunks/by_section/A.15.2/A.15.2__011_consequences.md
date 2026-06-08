---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:7c"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__011_consequences.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:7c — Consequences"
line_start: 20606
line_end: 20614
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
| Plans become inspectable without being confused with execution. | More explicit records; mitigate by using compact plan items for ordinary coordination. |
| Variance becomes meaningful because planned baseline and performed work stay separate. | Requires discipline around baselines; keep baseline and version visible on the plan. |
| Cross-role and cross-context coordination becomes safer. | Requires bridge checks when contexts differ; name only the bridge needed for the planned use. |
| P2W carry-through can prepare work without pretending work already happened. | Use `A.15.1`, `A.15.3`, `A.15.4`, `A.10`, `B.3`, `A.20`, or `A.21` only when the performed-work, planned-baseline, source-restoration, evidence, assurance, gate, or constraint relation becomes live. |


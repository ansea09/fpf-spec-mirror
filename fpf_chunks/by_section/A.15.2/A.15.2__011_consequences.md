---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:7c"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__011_consequences.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:7c — Consequences"
line_start: 24942
line_end: 24950
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.2.1"
  - "A.2.2"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.32.P2S"
  - "E.17"
  - "E.24"
  - "E.24.UK"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "PlanItem content"
  - "horizon"
  - "intended-work episteme"
  - "no actuality by plan"
  - "performer and capability conditions"
  - "positive or governed-negative local fulfilment assertion"
  - "possible future performance"
  - "present EntityOfConcern"
  - "reusable predicate semantics"
  - "variance"
---

### A.15.2:7c - Consequences

| Benefit | Trade-off and mitigation |
| --- | --- |
| Plans become inspectable without being confused with performed work. | More explicit claims; mitigate by using compact `PlanItem` content for ordinary coordination. |
| Variance becomes meaningful because planned baseline and performed work stay separate. | Requires discipline around baselines; keep the exact plan edition and baseline visible without treating a version label as identity. |
| Cross-role and cross-context coordination becomes safer. | Requires exact reference-scheme and direct-owner checks; use F.9 only for the `SenseCell` correspondence actually needed. |
| P2W carry-through can prepare work without pretending work already happened. | Use `A.15.1`, `A.15.3`, `A.15.4`, `A.15.5`, `A.10`, `B.3`, `A.20`, or `A.21` only when the performed-work, planned-baseline, appearance-based reliance repair, work-entry readiness, evidence, assurance, gate, or constraint relation becomes current. |


---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:8"
section_title: "P2W WorkPlanning use"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__014_p2w-workplanning-use.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:8 — P2W WorkPlanning use"
line_start: 25103
line_end: 25110
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

### A.15.2:8 - P2W WorkPlanning use

When `E.18.1` reaches WorkPlanning, one exact `U.WorkPlan` retains its present EntityOfConcern and states possible future performed work over an exact horizon through `PlanItem` content: intended-performance designators, windows, methods, performer and role conditions, capability requirements, constraints, budgets, dependencies, commitments, targets, evidence-reference notes, and source-currentness requests. If the plan chooses a value for a reusable declaration member, use A.15.3; if it states an expected effect, name the intended subject and target under the pattern that defines that effect.

When the P2W use also needs a readiness question, the WorkPlan may supply target PlanItems, planned preparation tasks, reservations, and planned baselines. `A.15.5` carries the `WorkEntryReadiness@Context` relation that judges full-kit condition, commitment disposition, resource readiness, WIP or flow policy, and any launch-gate references the readiness claim actually cites.

If the same P2W source material also claims performed work, an actual launch value or participant, evidence, gate passage, result, measurement, publication use, appearance-based reliance repair, or refresh, state that claim outside the WorkPlan under the pattern that defines it. The WorkPlan establishes none of them.


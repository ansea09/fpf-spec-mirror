---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:8"
section_title: "P2W WorkPlanning Use Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__014_p2w-workplanning-use-relation.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:8 — P2W WorkPlanning Use Relation"
line_start: 22592
line_end: 22599
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

### A.15.2:8 - P2W WorkPlanning Use Relation

When `E.18.1` reaches WorkPlanning, `U.WorkPlan` states intended work occurrences, planned windows, intended role values, role-admission conditions, capability-fit conditions, planned constraints, resource budgets, acceptance targets, evidence-reference notes, source-currentness requests, and `PlanItem` values.

When the P2W use also needs a readiness question, the WorkPlan may supply target PlanItems, planned preparation tasks, reservations, and planned baselines. `A.15.5` carries the `WorkEntryReadiness@Context` relation that judges full-kit condition, commitment disposition, resource readiness, WIP or flow policy, and launch-gate refs when those are current.

If the same P2W source material also makes a performed-work, launch-value, evidence, gate, result, measurement, publication-use, appearance-based reliance repair, or refresh claim, write that meaning as a separate current relation before using the plan.


---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:7a"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__009_conformance-checklist.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:7a — Conformance Checklist"
line_start: 22546
line_end: 22558
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

### A.15.2:7a - Conformance Checklist

| ID | Requirement | Practical test |
| --- | --- | --- |
| CC-A15.2-1 | A conforming `U.WorkPlan` names intended `U.Work`, not performed work. | The record can state planned windows and baselines without claiming performed values. |
| CC-A15.2-2 | Each reliance-bearing `PlanItem` names target `U.Method`, method-description reference when current, planned window, intended role value or role-admission condition, planned resource budget, dependencies, and acceptance target. | A performer can prepare the intended work without treating the plan as performed work. |
| CC-A15.2-3 | Proposed `U.RoleAssignment`s remain intended assignments until checked for the performed-work interval by A.15 and A.15.1. | The plan does not accept the role assignment for that interval by publication alone. |
| CC-A15.2-4 | Performed cost, resource use, launch values, substitutions, telemetry, and outcomes belong to performed `U.Work`. | The plan points to the work record for performed values and variance. |
| CC-A15.2-5 | `PlanItem` decomposition does not force the same shape on performed work. | Fulfilment and variance relations explain split, consolidated, emergency, or substituted work. |
| CC-A15.2-6 | Cross-context planning names bridges before reusing planned windows, budgets, or acceptance targets across contexts. | Audit, regulatory, operations, and delivery contexts can judge the plan without hidden equivalence. |
| CC-A15.2-7 | Evidence, assurance, gate, launch-value, and result-measurement claims stay in the patterns that govern those relations. | The WorkPlan may state evidence-reference notes or requests, but it does not become evidence, assurance, gate passage, or result measurement. |
| CC-A15.2-8 | Planned preparation or full-kit tasks may appear in the WorkPlan, but `WorkEntryReadiness@Context` is governed by `A.15.5`. | The plan may say what should be prepared; it does not decide readiness for work entry by itself. |


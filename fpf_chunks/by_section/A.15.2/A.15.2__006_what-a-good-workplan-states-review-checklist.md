---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:5"
section_title: "What a good WorkPlan states (review checklist)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__006_what-a-good-workplan-states-review-checklist.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:5 — What a good WorkPlan states (review checklist)"
line_start: 21873
line_end: 21887
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

### A.15.2:5 - What a good `WorkPlan` states (review checklist)

Use this as a human-facing checklist (not a rigid schema):

1. **Horizon & cadence** (e.g., “W36 surgeries, daily ETL”).
2. **`PlanItem` values** with: target Method and MethodDescription, planned windows, dependencies.
3. **Role requirements** (`U.Role` values) and **intended assignments** (optional, context-admitted).
4. **Capability thresholds** and **safety envelopes**.
5. **Resource budgets** and **reservations** on assets.
6. **Acceptance targets** (SLA and quality windows).
7. **Bridges** if plan spans **multiple contexts** (operations, audit, or regulatory).
8. **Baseline and version** plus **change notes** (so variance is attributable).
9. **Policy pointers** (episode policy, overlap policy for Work roll‑ups if needed for KPIs).
10. **Exception relation** (how ad hoc or emergency work is related back to planning, if that relation is needed).


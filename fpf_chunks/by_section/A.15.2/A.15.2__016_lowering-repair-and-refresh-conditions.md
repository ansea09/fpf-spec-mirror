---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:10"
section_title: "Lowering, Repair, and Refresh Conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__016_lowering-repair-and-refresh-conditions.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:10 — Lowering, Repair, and Refresh Conditions"
line_start: 20464
line_end: 20471
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

### A.15.2:10 - Lowering, Repair, and Refresh Conditions

Lower a candidate `U.WorkPlan` claim when horizon, planned window, target method, method-description source when live, role requirement, planned constraint, resource budget, dependency, acceptance target, or baseline cannot be named at the granularity required by the next planning move. The admissible lowered result is a planning cue, method-description note, source-gap note, source-restoration request, or evidence-reference hook, not a conforming WorkPlan.

Repair the WorkPlan when a subsequent source changes the intended method, planned window, role requirement, planned resource budget, dependency, acceptance target, baseline, version, bridge, or exception policy. Repair the plan; do not rewrite performed `U.Work` unless the work record itself changed, and do not make the repaired plan into evidence that the work occurred.

Refresh before relying on a WorkPlan for cross-context coordination, budget reservation, release preparation, gate preparation, evidence-reference use, performed-work entry, result measurement, or P2W carry-through. If the claim being made after refresh is actual work, evidence, assurance, gate passage, or source restoration, use the governing pattern for that relation and keep only the returned WorkPlan relation here.


---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:9"
section_title: "Launch-value and actual-use boundary for P2W"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__015_launch-value-and-actual-use-boundary-for-p2w.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:9 — Launch-value and actual-use boundary for P2W"
line_start: 25838
line_end: 25845
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
  - "U.SystemRoleAssignment"
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

### A.15.2:9 - Launch-value and actual-use boundary for P2W

For P2W use, `U.WorkPlan` may state intended performer Systems and local system-role-kind conditions, planned values, exact A.15.3 fillings, constraints, reservations, commitments, and evidence-reference notes. A.15.5 may later publish one C.2.1 work-entry readiness result whose exact EntityOfConcern is this WorkPlan; its ClaimGraph may designate the relevant declaration-local PlanItem content used by the readiness criterion. An A.21 `GateDecision` separately selects, narrows, blocks, or passes its declared crossing under one current `GateProfile`. Neither result institutes permission.

When the entry criterion consumes permission material, keep the current A.2.8.PER values distinct. A `GrantedPermissionRelation@Context` occurrence is strong permission only for its exact beneficiary, action specification, `U.ClaimScope`, and `validityWindow`. A `NonProhibitionFinding@Context` reports only its frame-relative result for its `evaluationWindow`; it is not a grant. A `PermissionNormConflictFinding@Context` exposes overlap for its `overlapWindow`, and a current resolution result is usable only when the A.2.8.PER resolution predicate obtains and the result names its `effectiveWindow`; an unresolved conflict stops or degrades the proposed use. `PermissionExerciseRelation@Context` and `NonViolationFinding@Context` require already dated actual Work and therefore cannot be prospective proof that the intended performance may start. When the governing entry policy requires a grant, absence or unavailability of that exact current grant permits no authorization claim; readiness, gate passage, or non-prohibition cannot stand in for it. The WorkPlan, readiness result, gate decision, permission values, and their windows make no planned value actual and create no Work occurrence.

At performed-work entry, identify one exact Work occurrence as an individual admitted under `U.Work` by A.15.1. For an actual relation participant or another world-side value, name the direct relation and its obtaining predicate. For an operation argument or returned result, use A.6.1 only after the exact application and its declaration-local binding predicate obtain. Keep the gate decision, plan claim, readiness result, permission facts, Work occurrence, actual-use relation, provenance, change, result episteme, production, delivery, acceptance, and downstream effect separate.


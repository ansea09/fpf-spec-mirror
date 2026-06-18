---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:16"
section_title: "Lowering, Repair, and Refresh Conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__019_lowering-repair-and-refresh-conditions.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:16 — Lowering, Repair, and Refresh Conditions"
line_start: 21180
line_end: 21187
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actuals"
  - "event"
  - "execution"
  - "log"
  - "occurrence"
  - "run"
---

### A.15.1:16 - Lowering, Repair, and Refresh Conditions

Lower a candidate `U.Work` claim when performer, enacted method, method-description source when current, time window, `executedWithin`, affected referent, parameter bindings, resources, outcome, or state-change witness cannot be named at the granularity required by the next work move. The acceptable lowered record is a plan note, evidence note, source-gap note, source-restoration request, or method-description reference, not a backdated work occurrence.

Repair the work record when a subsequent source changes the work interval, performer, role assignment, enacted method, method-description edition, parameter binding, resource ledger, outcome, affected referent, state-plane reference, pre-state reference, post-state reference, overlap policy, or aggregation policy. Repair only the changed relation: do not rewrite the method when only evidence changed, do not rewrite evidence when only work time changed, and do not convert a plan or source-restoration request into work.

Refresh before cross-context acceptance, aggregation, comparison, result measurement, release reliance, gate use, evidence use, assurance use, QD or OEE archive use, or P2W carry-through use. If the claim being made after refresh is no longer performed work, use the governing pattern for that relation and keep only the returned `U.Work` reference here.


---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__001_intro.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:intro — Intro"
line_start: 20409
line_end: 20435
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

## A.15.2 - U.WorkPlan

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.WorkPlan` when the question under repair is intended work: planned windows, intended role requirements, planned constraints, resource budgets, dependencies, acceptance targets, and baselines for subsequent variance against performed `U.Work`.

**Use this when.** Use this pattern when a schedule, calendar, rota, Kanban ticket, Gantt bar, shift plan, rollout plan, or planned reservation is being treated as a method, actual work, evidence, approval, or gate result. `U.WorkPlan` is an episteme for intended `U.Work`; it can coordinate action, but it does not make execution happen.

**First output.** One plan record or plan item naming horizon, cadence, target `U.Method`, method-description source when live, planned window, intended role requirements or proposed `U.RoleAssignment`, planned constraints, resource budgets, dependencies, acceptance targets, planned baseline, and the variance relation expected when `U.Work` occurs.

**Working action path.**
1. Name the intended work occurrence or work family that needs planning.
2. Recover target method, method-description source when live, planned window, role requirements, planned resources, dependencies, acceptance targets, and context.
3. Decide whether the encountered item is a `U.WorkPlan`, a method description, performed `U.Work`, a slot-filling plan item, evidence, gate claim, or source-restoration case.
4. Declare plan-item decomposition, dependency relation, and planned-baseline policy before using the plan for coordination or variance.
5. When actual work occurs, connect the `U.Work` record back to the plan item and record variance rather than rewriting the plan as if it had executed.

**Ordinary use.** For simple coordination, a compact plan item with intended method, window, role requirement, resource budget, and acceptance target is enough.

**Reliance-bearing use.** Use the fuller WorkPlan record when the plan carries cross-role coordination, budget reservation, delivery commitment, gate preparation, audit expectation, cross-context acceptance, or P2W carry-through.

**Stop condition.** Stop once the intended work is coordinated at the needed granularity or the encountered item is lowered to method, work, evidence, gate, or source-restoration use without claiming to be a plan.

**Not this pattern when.** Not this pattern when the live object is a dated performed work occurrence (`A.15.1`), a plan-item filler (`A.15.3`), a visible source cue needing work-relevant restoration (`A.15.4`), a method or method description (`A.15`), evidence or assurance (`A.10` or `B.3`), a gate decision (`A.20` or `A.21`), or publication-use behavior (`E.17`).


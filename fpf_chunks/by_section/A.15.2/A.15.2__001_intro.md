---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__001_intro.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:intro — Intro"
line_start: 22511
line_end: 22541
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

## A.15.2 - U.WorkPlan

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.WorkPlan` when the current claim is intended work: horizon, planned window, intended role values or role-admission conditions, planned constraints, resource budgets, dependencies, acceptance targets, and baselines for subsequent variance against performed `U.Work`.

**Use this when.** Use this pattern when a schedule, calendar, rota, Kanban ticket, Gantt bar, shift plan, rollout plan, reservation, planning cue, or P2W preparation note is being treated as a method, method description, performed work, evidence, approval, gate result, publication cue, query-plan representation, or database query-optimizer representation. `U.WorkPlan` is an episteme for intended `U.Work`; it can coordinate intended work, but it does not make work happen.

**First output.** One plan record or `PlanItem` naming horizon, cadence, target `U.Method`, method-description reference when current, planned window, intended role values, role-admission conditions, capability-fit conditions, or proposed `U.RoleAssignment`, planned constraints, resource budgets, dependencies, acceptance targets, planned preparation or full-kit tasks when current, planned baseline, and the variance relation expected when `U.Work` occurs.

**First-use checks.**
1. Name the intended work occurrence or work family that needs planning.
2. Recover target method, method-description reference when current, planned window, intended role values, role-admission conditions, capability-fit conditions, planned resources, dependencies, acceptance targets, baseline, and context.
3. Decide whether the encountered planning input is a `U.WorkPlan`, a method description, performed `U.Work`, a `SlotFillingsPlanItem`, `WorkEntryReadiness@Context`, evidence, gate claim, `A.15.4` appearance-based reliance repair case, publication-use cue, or declarative representation. A planning input may be a record, cue, or plan element; that phrase is not a new kind.
4. Declare `PlanItem` decomposition, dependency relation, and planned-baseline policy before using the plan for coordination or variance.
5. When work occurs, connect the `U.Work` record back to the `PlanItem` and record variance rather than rewriting the plan as if it had happened.

**Ordinary use.** For simple coordination, a compact `PlanItem` with intended method, window, intended role value or role-admission condition, resource budget, dependency, acceptance target, and baseline is enough.

**Reliance-bearing use.** Use the fuller WorkPlan record when cross-role coordination, budget reservation, delivery commitment, gate preparation, audit expectation, cross-context acceptance, release preparation, evidence-reference notes, source-currentness requests, or P2W carry-through depends on the plan.

**Stop condition.** Stop once the intended work is coordinated at the needed granularity or the encountered planning input is assigned to method, method description, performed work, evidence, gate, publication-use, declarative-representation, or `A.15.4` appearance-based reliance repair use without claiming to be a plan.

**What goes wrong if missed.** Teams treat calendars, tickets, reservations, or rollout notes as if work already happened, or treat a plan as method, evidence, gate result, approval, or publication authority.

**What this buys.** One intended-work record that keeps horizon, window, intended role values, role-admission conditions, capability-fit conditions, constraints, budgets, dependencies, acceptance targets, baseline, and subsequent variance against performed `U.Work` inspectable.

**Not this pattern when.** Not this pattern when the current claim is a dated performed work occurrence (`A.15.1`), a `SlotFillingsPlanItem` (`A.15.3`), work-entry readiness or full-kit condition (`A.15.5`), a reliance appearance being used for work or reliance before the governing pattern slot or relation is recovered (`A.15.4`), a method (`A.3.1`), a method description (`A.3.2`), evidence or assurance (`A.10` or `B.3`), a gate or constraint decision (`A.20` or `A.21`), publication-use behavior (`E.17`), or a declarative representation overread as a work-control or method claim (`C.2.P.DR`).


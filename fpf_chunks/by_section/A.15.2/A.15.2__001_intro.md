---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__001_intro.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:intro — Intro"
line_start: 25283
line_end: 25320
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

## A.15.2 - U.WorkPlan

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.WorkPlan` when a system needs one plan to coordinate possible future performed Work for an already existing subject over a stated horizon. One `PlanItem` names the intended Method, window, performer System or local system-role-kind condition, and only the resource, dependency, commitment, target, or baseline needed now. The plan states what is intended; it neither makes Work happen nor turns a merely possible performance into an existing entity.

**Use this when.** Use this pattern when a schedule, calendar, rota, Kanban ticket, Gantt bar, shift plan, rollout plan, reservation, planning cue, or P2W preparation note may be an episteme about intended work but is being treated as a method, method description, performed work, evidence, approval, gate result, publication cue, query-plan representation, or database query-optimizer representation. A system may use `U.WorkPlan` only when it can state the plan's substantive claims, the existing thing those claims concern, the scheme used to interpret them, and the possible future performance named in the plan content. The episteme itself neither acts nor makes work happen.

**First useful object.** One exact `U.WorkPlan` about one present subject, read under one reference scheme, with one horizon and one `PlanItem`. For ordinary coordination, that item names the possible future performance or repeated-work subject, target `U.Method`, planned window, intended performer System or local system-role-kind condition, and the one resource, dependency, commitment, target, or baseline the current decision needs. A later fulfilment or variance question is not required for membership or first use; open it only when a receiver asks about one independently identified Work occurrence.

**Ordinary path.**

1. Identify the already existing subject whose future work is being coordinated, the horizon, and one `PlanItem`.
2. In that item name the possible future performance, target Method, planned window, and the intended performer System or local system-role-kind condition needed now.
3. Add only the resource, dependency, commitment, target, or baseline needed for the current coordination decision.

**Filled ordinary example.** A plan about existing `Lathe-7`, interpreted under `FabMaintenanceScheme-E2`, can set horizon `2026-07-27`, item `inspect-spindle`, method `SpindleInspectionMethod-E2`, window `08:00–09:00`, intended performer System `MaintenanceTech-4` with local kind `MaintenanceTechnicianSystemRole`, a one-hour machine reservation, dependency `lockout complete`, and baseline `normal vibration`. The team can coordinate tomorrow's rota and reservation from that content and stop. No future Work occurrence, fulfilment policy, variance rule, or relation kind is needed.

**Later fulfilment or variance path.** Open this path only when a receiver asks whether one independently identified Work occurrence fulfilled, deviated from, or remained outside one plan item. Then use section 4.5 and the smallest A.6.RCD result that the receiving use actually needs. The detailed checks below preserve authoring and later-comparison boundaries; they are not prerequisites for the ordinary example.

1. Ask what already existing thing the plan coordinates work for, then identify that one present `U.Entity` as C.2.1's EntityOfConcern. It may be an exact system, asset, or promise-content episteme. Use the plan episteme itself only when its claims are expressly about its own coordination commitments. Keep a possible future performance, repeated-work family, or proposed group as a plan-content designator. If several existing things have no independently identified joint subject, split the claims or lower the cue; do not use a merely possible Work occurrence as if it already existed.
2. State the coordination facts the team will act on now: target method, any method-description episteme the plan actually cites, horizon and window, intended performer System and local system-role-kind condition, capability threshold, resources, dependencies, commitments, acceptance target, baseline, and effective reference scheme. Call the cited description an edition only when the C.2.1 `EpistemeEditionRelation` predicate obtains. If the team plans one particular future participant or operation value and will later compare that choice with actual participation, use A.15.3 only after an exact declaration member defines both its reusable meaning and its later actual-use predicate. Otherwise keep the choice as ordinary plan content; if typed reuse is required but that member or predicate is absent, return `missing-governor`. For an expected effect, name the intended subject and target under the pattern that defines them rather than adding a generic result field.
3. Ask what claim the schedule-like source actually carries. Intended-work coordination opens `U.WorkPlan`; a way of doing or its instructions opens A.3.1 or A.3.2; a dated performance opens A.15.1; a reusable planned declaration member opens A.15.3. Readiness, evidence, a gate result, appearance-based reliance repair, publication use, a forecast or dynamics model, and a declarative representation stay with their named patterns. A ticket, diagram, row, or file is only a cue or representation until one of those claims is stated.
4. For ordinary coordination, declare only the `PlanItem` organization, constraints, resources, dependencies, commitments, targets, and baseline needed to coordinate the intended work now. Stop this route once the plan is usable at that granularity. Do not choose a future fulfilment or variance policy, A.6.RCD disposition, or relation kind merely to make the plan coordinate work.
5. Only when a receiver later asks whether one exact Work occurrence fulfilled, deviated from, or remained outside one exact plan item, identify that Work independently under A.15.1 and open section 4.5. Select the smallest A.6.RCD disposition: a one-case local compound assertion for one case; a reusable predicate-definition episteme for repeated semantics that need no occurrence identity; relation-kind admission only for a receiver that genuinely consumes distinct relation occurrences. Unavailable case facts return `missing-information`; absent predicate, policy, or relation authority returns `missing-governor`. Neither stop creates a negative claim or universal fulfilment/variance relation.

**Reliance-bearing use.** Use fuller WorkPlan claim content when cross-team coordination, budget reservation, delivery commitment, gate preparation, audit expectation, cross-context acceptance, release preparation, evidence-reference notes, source-currentness requests, or P2W carry-through depends on the plan.

**Stop condition.** Stop once a system can coordinate the intended work at the needed granularity. If step 3 identifies another claim, use that pattern and make no WorkPlan claim. If no pattern states the predicate needed for a later fulfilment, variance, or occurrence-facing relation, stop only that stronger use; the plan and any local comparison whose predicate and supporting facts can be stated remain usable.

**What goes wrong if missed.** Teams treat calendars, tickets, reservations, or rollout notes as if work already happened; identify a possible future performance as an existing Work occurrence; let the plan episteme act; or treat a plan as method, evidence, gate result, approval, or publication authority.

**What this buys.** One identifiable intended-work episteme whose present subject, horizon, windows, Systems intended to perform the Work and their local system-role-kind conditions, capability-fit requirements, constraints, budgets, dependencies, commitments, acceptance targets, baseline, and later comparisons with independently identified Work occurrences remain inspectable.

**Not this pattern when.** Not this pattern when the current claim is a dated performed work occurrence (`A.15.1`), A.15.3 declaration-local planned-filling content, work-entry readiness or full-kit condition (`A.15.5`), a reliance appearance being used before the governing pattern or relation is recovered (`A.15.4`), a method (`A.3.1`), a method description (`A.3.2`), evidence or assurance (`A.10` or `B.3`), a gate or constraint decision (`A.20` or `A.21`), publication-use behavior (`E.17`), a non-agentive forecast or dynamics model (`A.3.3`), or a declarative representation overread as a work-control or method claim (`C.2.P.DR`).


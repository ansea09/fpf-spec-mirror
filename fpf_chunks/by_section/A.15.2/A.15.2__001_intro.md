---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan: Plan Content for Coordinating Future Work"
section_id: "A.15.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__001_intro.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.15.2 — U.WorkPlan: Plan Content for Coordinating Future Work"
  - "A.15.2:intro — Intro"
line_start: 29492
line_end: 29521
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
  - "C.27.TA"
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

## A.15.2 - `U.WorkPlan`: Plan Content for Coordinating Future Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.WorkPlan` when a system needs one plan to coordinate possible future performed Work for an already existing subject over a stated horizon. One `PlanItem` names the intended Method, window, performer System or local system-role-kind condition, and only the resource, dependency, commitment, target, or baseline needed now. The plan states what is intended; it neither makes Work happen nor turns a merely possible performance into an existing entity.

**Use this when.** Coordinate possible future Work through a schedule, rota, ticket or other plan content. Identify the existing subject, intended performances, horizon and reference scheme, then state enough constraints to make the current coordination decision. Use §4.3 when schedule or workflow wording leaves the claim unclear.

**First useful object.** One WorkPlan about a present subject, interpreted under one reference scheme, with a horizon and one usable PlanItem. Later fulfilment or variance checking is a separate use.

**Ordinary path.**

1. Identify the already existing subject whose future work is being coordinated, the horizon, and one `PlanItem`.
2. In that item name the possible future performance, target Method, planned window, and the intended performer System or local system-role-kind condition needed now.
3. Add only the resource, dependency, commitment, target, or baseline needed for the current coordination decision.

**Filled ordinary example.** A plan about existing `Lathe-7`, interpreted under `FabMaintenanceScheme-E2`, can set horizon `2026-07-27`, item `inspect-spindle`, method `SpindleInspectionMethod-E2`, window `08:00–09:00`, intended performer System `MaintenanceTech-4` with local kind `MaintenanceTechnicianSystemRole`, a one-hour machine reservation, dependency `lockout complete`, and baseline `normal vibration`. The team can coordinate tomorrow's rota and reservation from that content and stop. No future Work occurrence, fulfilment policy, variance rule, or relation kind is needed. If lockout will not be complete by 08:00, the planners defer that item or revise its window and reservation; the plan does not establish that inspection occurred.

**Detailed authoring and later comparison.** Use §4.1–4.4 to settle plan identity, item content and organization. Open §4.5 only when a receiving question asks whether an independently identified Work occurrence fulfilled or deviated from a plan item. Choose the smallest A.6.RCD result that this comparison needs.

**Stop condition.** Stop once a system can coordinate the intended work at the needed granularity. If step 3 identifies another claim, use that pattern and make no WorkPlan claim. If no pattern states the predicate needed for a later fulfilment, variance, or occurrence-facing relation, stop only that stronger use; the plan and any local comparison whose predicate and supporting facts can be stated remain usable.

**What goes wrong if missed.** Intended work can be mistaken for completed performance, and later changes to the plan can erase the baseline needed for comparison.

**What this buys.** The team can coordinate intended Work now and, when needed, compare actual performance with the identified plan under an explicit policy.

**Not this pattern when.** Use the direct pattern when the current claim is a dated performed work occurrence (`A.15.1`), A.15.3 declaration-local planned-filling content, work-entry readiness or full-kit condition (`A.15.5`), a reliance appearance being used before the governing pattern or relation is recovered (`A.15.4`), a method (`A.3.1`), a method description (`A.3.2`), evidence or assurance (`A.10` or `B.3`), an internal constraint result (`A.20`) or gate decision (`A.21`), publication-use behavior (`E.17`, with `E.24.PUB` for publication identity), a non-agentive forecast or dynamics model (`A.3.3`), or a declarative representation overread as a work-control or method claim (`C.2.P.DR`).


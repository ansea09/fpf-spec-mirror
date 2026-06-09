---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:4"
section_title: "Solution — the U.WorkPlan as the time‑bound intention to execute Work"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__005_solution-the-u-workplan-as-the-time-bound-intention-to-execute-work.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:4 — Solution — the U.WorkPlan as the time‑bound intention to execute Work"
line_start: 20464
line_end: 20539
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

### A.15.2:4 - Solution — the `U.WorkPlan` as the time‑bound intention to execute Work

#### A.15.2:4.1 - Definition

**`U.WorkPlan`** is an **`U.Episteme`** that **declares intended `U.Work` occurrences** over a horizon, with **planned windows**, **dependencies**, **intended performers** as role kinds or proposed `U.RoleAssignment`s, **resource budgets and reservations**, and **acceptance targets** within a `U.BoundedContext`.

> **Strict distinction (memory aid):**
> **Method** = *how in principle*. **MethodDescription** = *how it is written*.
> **WorkPlan** = *when, by whom in intent, under which constraints*.
> **Work** = *how it went this time*.

#### A.15.2:4.2 - Plan Items (what a `WorkPlan` is made of)

A `U.WorkPlan` **contains Plan Items** (think: scheduled tasks or operations), each of which typically states:

1. **Target Method and specification** — the **Method** to be enacted and the **MethodDescription** intended for enactment.
2. **Planned window** — e.g., earliest start and latest finish, timebox, recurrence (cron-like), blackout periods.
3. **Role requirements** — **role kinds** required (not people), optional proposed `U.RoleAssignment`s if pre-assignment is allowed in the context.
4. **Capability thresholds** — minimal abilities required of the performer (checked at run time).
5. **Resource budgets and reservations** — planned energy, materials, machine slots, money, and reservations on assets.
6. **Dependencies** — precedence, overlap permissions, gates, and approvals.
7. **Acceptance targets** — quality windows and SLA targets to be judged when Work completes.
8. **Location and asset constraints** — where the run is expected to take place.
9. **Links to Service promises** (if any) — external commitments that this plan aims to satisfy.

> **Didactic guardrail:** **No logs or actuals** belong in a WorkPlan; **no step logic** or solver internals either - that is the Method or MethodDescription.

#### A.15.2:4.3 - Clear distinctions (lexical sanity for schedule, process, and workflow)

| If you say…                                 | In FPF it is…                                        | Why                                               |
| ------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| "The **schedule** for tomorrow's surgeries" | **`U.WorkPlan`**                                     | Calendar of intended runs with who and when constraints. |
| "The **workflow** for appendectomy"         | **`U.MethodDescription`** and `U.Method`             | Recipe and semantic way, not a calendar.          |
| "The **process** already ran at 10:00"      | **`U.Work`**                                         | A dated run with resources and outcomes.          |
| "The **thermodynamic process** path"        | **`U.Work`** occurrence plus **`U.Dynamics`** model  | A realized trajectory plus its model, not a plan. |
| "The **plan** assigns Dr. Lee"              | **WorkPlan** naming an intended `U.RoleAssignment`   | Assignment is still validated at run time.        |
| "The **budget** for Shift-B"                | **WorkPlan** (planned ledger)                        | Actual costs land on **Work**, not on the plan.   |

> **L‑SCHED (lexical rule).** In this document, words like **schedule**, **calendar**, **rota**, **Gantt**, **plan** point to **`U.WorkPlan`** unless explicitly redefined by a bounded context glossary.

#### A.15.2:4.4 - Plan mereology (composition of plans ≠ composition of methods or runs)

Keep three separations crystal‑clear:

* **Method composition** (design-time semantics) -> produces **new Methods**.
* **Work composition** (run-time occurrences) -> produces **parent and child runs** with overlaps and episodes.
* **Plan mereology** (epistemic structure) -> organizes **Plan Items** for coordination (phases, sprints, shifts), with **precedence** and **resource reservations**.

**Common relations among Plan Items:**

* **`Precedes_pl` or `DependsOn_pl`** — start and finish constraints and gates.
* **`MayOverlap_pl` or `MutuallyExclusive_pl`** — allowed overlaps versus exclusive windows.
* **`Refines_pl`** — a child plan item tightens windows and budgets of a parent.
* **`Alternative_pl`** — planned alternatives (e.g., backup rig, backup team).

**Didactic rule:** A Plan Item **does not force** an identical Work shape; mapping is via **fulfilment** and **variance** (see §6).

#### A.15.2:4.5 - How `WorkPlan` Meets `Work` (Fulfilment and Variance)

When reality happens, each `U.Work` may:

* **Fulfil** a Plan Item — link `plannedAs → PlanItem`.
* **Partially fulfil** — multiple Work instances share one Plan Item (e.g., split run), or one Work fulfils several Plan Items (e.g., consolidated batch).
* **Deviate** — execute with method or specification substitution, different window, different performer (still valid or policy exception).
* **Be unplanned** — Work with no Plan Item (emergency or ad hoc); must be labeled as such.

**Variance dimensions** the plan expects to report on:

* **Schedule variance (Δt):** early or late versus planned window.
* **Cost variance (Δc):** actual resource spend vs budget.
* **Scope variance:** different Method or MethodDescription than planned (with justification).
* **Quality variance:** acceptance verdict vs target.
* **Assignment variance:** intended versus actual `U.RoleAssignment`.

> **Manager’s view:** A plan that cannot report variance is a calendar picture, not a management tool.


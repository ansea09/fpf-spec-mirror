---
chunk_kind: "parent"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/A.15.2.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.15.2 — U.WorkPlan"
line_start: 20408
line_end: 20648
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

### A.15.2:1 - Context (plain‑language motivation)

Operations live on **time**. Even with perfect roles, abilities, and methods, nothing ships unless we **decide when and by whom** concrete runs **should** happen, under what **constraints** and **budgets**. Teams need a first‑class concept for **plans and schedules** that does **not** get confused with:

* the **semantic “way of doing”** (that is `U.Method`),
* the **written recipe** (that is `U.MethodDescription`),
* the **actual execution** (that is `U.Work`), or
* the **state laws** (that is `U.Dynamics`).

`U.WorkPlan` is that missing anchor.

### A.15.2:2 - Problem (what breaks without `WorkPlan`)

1. **“Workflow = schedule” conflation.** Flowcharts or code are used as calendars; resource clashes and SLA misses follow.
2. **Plan and run blur.** Gantt bars or Kanban tickets are reported as if the work already happened; audits and costing degrade.
3. **Specification and time leakage.** People and calendars creep into MethodDescriptions; reuse and staffing agility collapse.
4. **No variance model.** Without planned baselines, deviations in time, cost, and quality cannot be explained or improved.
5. **Structure entanglement.** BoM and org charts get baked into “process” views; plans become brittle and unmaintainable.

### A.15.2:3 - Forces (what we must balance)

| Force                              | Tension we resolve                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Universality vs. domain idioms** | One plan concept that fits hospitals, fabs, data centers, and research labs—while honoring local terms. |
| **Commitment vs. flexibility**     | Plans must be firm enough to coordinate, yet easy to update as reality changes.                         |
| **Intended performer vs. actual performer** | Plans may name intended performers; the actual assignment must still be checked at run time. |
| **Budgets vs. actuals**            | Plans carry targets and reservations; only Work carries actual spend.                                   |
| **Decomposition vs. mapping**      | Plan tasks decompose conveniently; they do not force a shape on actual Work runs.                       |

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

### A.15.2:5 - What a good `WorkPlan` states (review checklist)

Use this as a human-facing checklist (not a rigid schema):

1. **Horizon & cadence** (e.g., “W36 surgeries, daily ETL”).
2. **Plan Items** with: target Method and MethodDescription, planned windows, dependencies.
3. **Role requirements** (kinds) and **intended assignments** (optional, context‑lawful).
4. **Capability thresholds** and **safety envelopes**.
5. **Resource budgets** and **reservations** on assets.
6. **Acceptance targets** (SLA and quality windows).
7. **Bridges** if plan spans **multiple contexts** (operations, audit, or regulatory).
8. **Baseline and version** plus **change notes** (so variance is attributable).
9. **Policy pointers** (episode policy, overlap policy for Work roll‑ups if needed for KPIs).
10. **Exceptions path** (how ad hoc or emergency work is planned after the fact).

### A.15.2:6 - Archetypal grounding (parallel domains)

#### A.15.2:6.1 - Hospital OR day plan (shift rota + cases)

* **WorkPlan:** `OR_DayPlan_2025‑08‑12`.
* **Plan Items:** `Case#1 Appendectomy`, `Case#2 Hernia`, with windows, context assignments, and surgeon **role kinds**; anesthetist intended `U.RoleAssignment` provided.
* **Budgets:** OR time blocks, consumables envelopes.
* **Fulfilment:** Each surgery Work links to its Plan Item; variances computed (over‑run time, substitutions).

#### A.15.2:6.2 - Fab maintenance weekend (asset reservations)

* **WorkPlan:** `Fab_Maintenance_W36`.
* **Plan Items:** `Tool_42 chamber clean`, `Tool_13 calibration`; **MutuallyExclusive\_pl** with production slots.
* **Reservations:** nitrogen, DI water, metrology window.
* **Fulfilment:** Actual clean Work happens earlier; variance logged as **early** with cost underrun.

#### A.15.2:6.3 - Data‑center rollout (multi‑context plan)

* **WorkPlan:** `DC_Rollout_Phase‑2`.
* **Bridges:** Ops context ↔ Security Audit context (different acceptance targets).
* **Plan Items:** `Deploy Service A`, `Pen‑test A`; dependencies across contexts.
* **Fulfilment:** Deployment Work passes ops targets; audit Work passes after the deployment work, with variance reported per context.

### A.15.2:7 - Bias‑Annotation (as in E‑cluster)

* **Lenses tested:** `Did`, `Prag`, `Arch`, `Epist`.
* **Scope declaration:** Universal; meanings of windows, budgets, and permissions are **context-local** via `U.BoundedContext`.
* **Rationale:** Elevates **planning and scheduling** to a first-class episteme that coordinates Methods, `U.RoleAssignment`s, and Work without conflation.

### A.15.2:7a - Conformance Checklist

| ID | Requirement | Practical test |
| --- | --- | --- |
| CC-A15.2-1 | A conforming `U.WorkPlan` names intended `U.Work`, not performed work. | The record can state planned windows and baselines without claiming actuals. |
| CC-A15.2-2 | Each reliance-bearing plan item names target `U.Method`, method-description source when live, planned window, role requirement, planned resource budget, dependencies, and acceptance target. | A performer can prepare the intended work without treating the plan as execution. |
| CC-A15.2-3 | Proposed `U.RoleAssignment`s remain intended assignments until checked at run time by A.15 and A.15.1. | The plan does not make the role assignment valid for the work interval by publication alone. |
| CC-A15.2-4 | Actual cost, resource use, launch values, substitutions, telemetry, and outcomes belong to performed `U.Work`. | The plan points to the work record for actuals and variance. |
| CC-A15.2-5 | Plan-item decomposition does not force the same shape on performed work. | Fulfilment and variance relations explain split, consolidated, emergency, or substituted work. |
| CC-A15.2-6 | Cross-context planning names bridges before reusing planned windows, budgets, or acceptance targets across contexts. | Audit, regulatory, operations, and delivery contexts can judge the plan without hidden equivalence. |
| CC-A15.2-7 | Evidence, assurance, gate, launch-value, and result-measurement claims stay in the patterns that govern those relations. | The WorkPlan may carry hooks or requests, but it does not become evidence, assurance, gate passage, or result measurement. |

### A.15.2:7b - Common Anti-Patterns and How to Avoid Them

- **Plan-as-actual.** Do not treat a Gantt bar, Kanban ticket, shift rota, or calendar booking as performed work; create or cite the `U.Work` occurrence when work happens.
- **Workflow-as-schedule.** Do not treat a method description or flowchart as a plan; make a `U.WorkPlan` only when intended windows, constraints, role requirements, and baselines are live.
- **Assignment-by-plan.** Do not treat an intended performer in the plan as a valid `U.RoleAssignment` for execution; validate assignment at run time.
- **Budget-as-cost.** Do not book planned budgets as actual resource use; actuals belong to `U.Work`.
- **Plan-shape overreach.** Do not force performed work to match plan decomposition; use fulfilment and variance relations.
- **Hook-as-claim.** Do not treat evidence-reference hooks, gate-preparation notes, or source-currentness requests as evidence, gate passage, assurance, or release permission.

### A.15.2:7c - Consequences

| Benefit | Trade-off and mitigation |
| --- | --- |
| Plans become inspectable without being confused with execution. | More explicit records; mitigate by using compact plan items for ordinary coordination. |
| Variance becomes meaningful because planned baseline and performed work stay separate. | Requires discipline around baselines; keep baseline and version visible on the plan. |
| Cross-role and cross-context coordination becomes safer. | Requires bridge checks when contexts differ; name only the bridge needed for the planned use. |
| P2W carry-through can prepare work without pretending work already happened. | Use `A.15.1`, `A.15.3`, `A.15.4`, `A.10`, `B.3`, `A.20`, or `A.21` only when the performed-work, planned-baseline, source-restoration, evidence, assurance, gate, or constraint relation becomes live. |

### A.15.2:7d - SoTA Alignment

| Source tradition | Local invariant adopted | Shortcut rejected |
| --- | --- | --- |
| Operations planning, scheduling, and project-control practice | Planned windows, dependencies, budgets, and baselines are declared before execution and compared against actuals after work occurs. | Treating schedule presence as execution evidence. |
| Lean, maintenance, and service-management planning practice | Plans coordinate role requirements, assets, constraints, and reservations while leaving actual work and variance to run-time records. | Treating a plan as a method, a gate, or a result. |
| Case-management and adaptive-work practice | Emergency and ad hoc work can be related back to planning through exception, fulfilment, and variance relations. | Forcing every actual work occurrence into the original plan shape. |
| Audit and quality-management practice | Baseline, version, acceptance target, and change note remain explicit so deviations can be explained. | Changing the plan after the fact to make variance disappear. |

### A.15.2:7e - Relations

* **Builds on:** `A.15` Role-Method-Work Alignment, `A.15.1` `U.Work`, `A.2.1` `U.RoleAssignment`, `U.Method`, and `U.MethodDescription`.
* **Coordinates with:** `A.15.3` for slot-filling plan items, `A.15.4` for work-relevant source restoration, `A.10` for evidence paths, `B.3` for assurance, `A.20` and `A.21` for gates and constraint decisions, and `E.17` for publication-use questions.
* **Used by:** P2W carry-through when principle-to-work reasoning reaches WorkPlanning and must keep plan, performed work, evidence, gate, and result-measurement relations separate.

### A.15.2:8 - P2W WorkPlanning Use Relation

When `E.18.1` reaches WorkPlanning, `U.WorkPlan` carries intended work occurrences, planned windows, intended role requirements, planned constraints, resource budgets, acceptance targets, evidence-reference hooks, source-currentness requests, and plan items.

If the same P2W source phrase also carries execution, launch-value, evidence, gate, result, measurement, or refresh meaning, write that meaning as a separate live relation before using the plan.

### A.15.2:9 - Launch-Value Boundary For P2W

For P2W use, `U.WorkPlan` may state planned values, planned fillers, constraints, reservations, intended performers, and evidence-reference hooks. Launch values are finalized only at performed-work entry under the current gate relation and performed-work pattern and are recorded with the performed `U.Work` and related gate and provenance records when live.

### A.15.2:10 - Lowering, Repair, and Refresh Conditions

Lower a candidate `U.WorkPlan` claim when horizon, planned window, target method, method-description source when live, role requirement, planned constraint, resource budget, dependency, acceptance target, or baseline cannot be named at the granularity required by the next planning move. The admissible lowered result is a planning cue, method-description note, source-gap note, source-restoration request, or evidence-reference hook, not a conforming WorkPlan.

Repair the WorkPlan when a subsequent source changes the intended method, planned window, role requirement, planned resource budget, dependency, acceptance target, baseline, version, bridge, or exception policy. Repair the plan; do not rewrite performed `U.Work` unless the work record itself changed, and do not make the repaired plan into evidence that the work occurred.

Refresh before relying on a WorkPlan for cross-context coordination, budget reservation, release preparation, gate preparation, evidence-reference use, performed-work entry, result measurement, or P2W carry-through. If the claim being made after refresh is actual work, evidence, assurance, gate passage, or source restoration, use the governing pattern for that relation and keep only the returned WorkPlan relation here.

### A.15.2:End


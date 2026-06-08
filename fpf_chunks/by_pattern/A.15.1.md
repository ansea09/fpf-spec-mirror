---
chunk_kind: "parent"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/A.15.1.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.15.1 — U.Work"
line_start: 19993
line_end: 20408
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
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

## A.15.1 - U.Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.Work` when the question under repair is what actually happened: a dated, resource-consuming occurrence enacted by a holder under `U.RoleAssignment`, inside a `U.BoundedContext`, with method, time window, parameters, resources, affected referent, result, and evidence kept inspectable.

**Use this when.** Use this pattern when a plan, method description, schedule, log, telemetry stream, dashboard, approval-looking cue, or result statement is being treated as if it were actual performed work. `U.Work` is the run-time occurrence; the surrounding records may identify, constrain, evidence, schedule, or judge it, but they do not become the occurrence by being published.

**First output.** One work-occurrence record naming `performedBy -> U.RoleAssignment`, `enactsMethod -> U.Method`, `methodDescriptionRef` when the source episteme is live, `executedWithin`, time window, concrete parameter bindings, affected referent, resource ledger, pre-state and post-state anchors or a declared delta predicate, outcome, and the governing `U.BoundedContext`.

**Working action path.**
1. Name the candidate occurrence and the work move that depends on it.
2. Recover the `U.RoleAssignment`, enacted `U.Method`, method-description source, time window, system or subsystem accountable for the occurrence, affected referent, parameters, resources, and outcome.
3. Decide whether the item is actual `U.Work`, only a plan (`A.15.2`), only a method or method description (`A.15`), only evidence for work (`A.10`), or a work-relevant source-restoration case (`A.15.4`).
4. For composite, repeated, interrupted, or overlapping occurrences, declare the work-part relation and aggregation policy before using totals or identity claims.
5. If the required anchors cannot be recovered, lower the claim to a source-gap note, work-evidence note, plan note, or source-restoration request; do not backdate work.

**Ordinary use.** For a simple run, one compact work card with performer, method, time window, affected referent, resources, and outcome is enough.

**Reliance-bearing use.** Use the full record when the work occurrence carries cost, quality, audit, evidence, compliance, gate, release, result measurement, cross-context reuse, or aggregation claims.

**Stop condition.** Stop once the occurrence is either recoverable as `U.Work` at the needed granularity or lowered to a neighboring record that no longer claims performed work.

**Not this pattern when.** Not this pattern when the live object is only a method description, only a plan or schedule (`A.15.2`), only a slot-filling plan item (`A.15.3`), only a visible source cue that must be restored before reliance (`A.15.4`), only evidence or assurance (`A.10` or `B.3`), or only publication-use or representation behavior (`E.17`, `A.7`, or the relevant representation pattern).

### A.15.1:1 - Problem Frame

After we have agreed **who is assigned** (via **Role assignment**), **what they can do** (via **Capability**), and **how in principle** it should be done (via **Method or MethodDescription**), we still need a precise concept for **what actually happened** in real time and space.

That concept is **`U.Work`**: the **dated run-time occurrence** of enacting a `U.Method` by a specific performer under a `U.RoleAssignment`, with concrete parameter bindings, resource consumption, and outcomes, **anchored to a domain referent that actually changes** (asset, product, or dataset) - **not** merely the manipulation of records about that referent. Managers care about Work because it is the place where actual cost, time, defects, and result evidence are booked. Architects care because Work ties plans and specifications to accountable execution.

### A.15.1:2 - Problem (what breaks without a clean notion of Work)

1. **Plan and run confusion.** Schedules and diagrams get mistaken for "the process," so audits and KPIs become fiction.
2. **Specification and run conflation.** A method description, code artifact, or SOP is reported as if it were an execution; conversely, logs are treated as recipes.
3. **Who and when leakage.** People and calendars are baked into specifications; reuse and staffing agility collapse.
4. **Resource dishonesty.** Energy, money, and tool wear are booked to methods or roles, not to actual runs; costing and sustainability measures drift.
5. **Mereology muddle.** Teams hand-wave over sub-runs, retries, overlaps, or long-running episodes; roll-ups double-count or miss work.

### A.15.1:3 - Forces (what the definition must balance)

| Force                              | Tension we resolve                                                                                    |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Universality vs. domain detail** | One Work notion for surgery, welding, ETL, proofs, lab cycles—while letting each keep its vocabulary. |
| **Granularity vs. aggregation**    | Atomic runs vs. composite operations; we need roll‑up without double‑count.                           |
| **Concurrency vs. order**          | Parallel or overlapped activities need clear part and overlap semantics.                              |
| **Identity vs. retries**           | A failed attempt, a retry, and a resumed episode—what is “the same” work?                             |
| **Time realism vs. simplicity**    | We need intervals and coverage but cannot bury users in temporal logic notation.                      |

### A.15.1:4 - Solution — define `U.Work` as the accountable, dated occurrence

#### A.15.1:4.1 - Definition

**`U.Work`** is a **4D occurrence holon**: a **dated run-time enactment** of a `U.Method` by a performer designated through a `U.RoleAssignment`, **executed within a concrete `U.System` or `U.SubSystem`**, inside a `U.BoundedContext`, that binds concrete parameters, consumes and produces resources, and leaves an auditable trace. When a method-description source is live, `methodDescriptionRef` names the `U.MethodDescription` used to identify, constrain, or justify the enacted method.
Each `U.Work` is a **morphism** `Δ` on a declared **state‑plane** (`StatePlaneRef`), mapping ⟨**pre‑state**, **inputs**⟩ to ⟨**post‑state**, **outputs**⟩ for one or more **affected referents**.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

#### A.15.1:4.2 - Core anchors (conceptual descriptors; not a data schema)

When you describe a Work instance in a review, answer these prompts:

1. **Window** — start and end timestamps and, where relevant, location or asset.
2. **Spec** — `isExecutionOf → U.MethodDescription` (the description actually followed; **edition pinned** if applicable).
3. **Performer** — `performedBy → U.RoleAssignment` (which **holder#role\:context** acted).
4. **Parameters** — concrete values bound for this run (from the **MethodDescription** parameter declarations).
5. **Inputs and outputs** — materials, information, or product states used or produced by the Work; service delivery is judged through the Outcome row.
6. **Resources** — energy, materials, machine time, money (the **only** place we book them).
7. **Outcome** — success and failure classes, quality measures, acceptance verdicts (**map-then-compare** per **ComparatorSet** under **CG-Spec**; pin editions).
8. **Links** — predecessor, successor, and overlap relations to other Work, plus step or run nesting if part of a bigger operation.
9. **Context** — the bounded context under which this run is judged, normally inherited from the method-description source and `U.RoleAssignment`; see A.15 for cross-checks.
10. **Effect (Δ)** — `affected → {referent(s)}` + **pre‑state anchor** and **post‑state anchor** (or a declared **Δ‑predicate** evaluated on evidence) on the declared state‑plane (**StatePlaneRef**).
11. **System** — `executedWithin -> U.System` or `executedWithin -> U.SubSystem` (the operational system or subsystem accountable for the occurrence; **mandatory**).
12. **Evidence and telemetry (optional)** — if the run feeds **G.11** refresh or QD and OEE archives, cite **PathId** or **PathSliceId** and the active **policy-id** used for illumination; do not elevate telemetry into dominance without CAL policy.

#### A.15.1:4.3 - Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| The **recipe, code artifact, or diagram**     | **MethodDescription**         | Is it an episteme or publication describing a way of doing?     |
| The **semantic “way of doing”**               | **Method**             | Same Standard across notations?                                 |
| The **assignment** ("who is being what")     | **Role -> RoleAssignment** | Can be reassigned without changing the system?                  |
| The **ability** (“can do within bounds”)      | **Capability**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs, resources | **Work**               | Did it happen at (t₀, t₁), consume resources, produce outcomes? |
| The **state change caused this time**         | **Work.Δ**             | Did the referent move from pre→post on the declared state‑plane? |

#### A.15.1:4.4 - Publication-use boundary for `U.Work`

A `U.Work` publication projects an already declared work occurrence; it does not create the occurrence, add run-time facts, or make a plan, source reconstruction, dashboard, or publication face count as performed work.

| Publication-use pressure | Work-local rule |
|---|---|
| PlainView, TechCard, InteropCard, or AssuranceLane presents work material | Project only occurrence anchors: time window, performer, enacted method-description source, parameter-binding occurrence, resource-ledger reference, state-change anchors, outcome, and acceptance-verdict reference when live. |
| numeric, comparable, aggregation, or benchmark content appears | Pin the comparator, aggregation policy, CG-Spec, reference plane, and transport edition needed by the claimed comparison; do not hide scalarization in the publication face. |
| publication cites design-time material or cross-context material | Keep the `U.Work` occurrence run-time; cite the design-time or cross-context material through Bridge/UTS, `DesignRunTag`, reference-plane, or edition relation as needed. |
| reconstructed records look like a run | Do not synthesize surrogate `U.Work`; a publication may cite only work occurrences that meet the occurrence anchors in this pattern. |

#### A.15.1:4.5 - Crossing visibility for work publications

When a work publication crosses design/run state, context, reference plane, unit, or edition, publish the crossing relation used by the publication. Penalties and reliability changes belong to the relevant comparison, bridge, publication, or evidence relation; they do not change the identity of the `U.Work` occurrence.

Launch values bind only at the occurrence. Plan-time proposals remain proposals; do not back-fill plan publications with run-time bindings. Pre-state and post-state anchors bind to the occurrence: pre at start, post at completion or at declared checkpoints.

### A.15.1:5 - Work mereology (how runs form holarchies)

We adopt a **4D extensional** stance for occurrences: a Work is identified primarily by its **spatiotemporal extent** and its execution anchors (spec used, performer, parameterization). This avoids double-counting and keeps aggregation sound. FPF adapts insights from BORO and constructive ontologies to Work while staying practical.

#### A.15.1:5.1 - Parts and wholes of Work (design‑neutral, run‑time facts)

* **Temporal‑part (`TemporalPartOf_work`).** A proper **time‑slice** of a Work (e.g., the first 10 minutes of a 2‑hour run). Useful for monitoring and SLAs.
* **Episode‑part (`EpisodeOf_work`).** A **resumption fragment** after an interruption (same run identity if policy deems it one episode; see 5.5).
* **Operational-part (OperationalPartOf_work).** A **sub-run** that enacts a **factor** of the Method or specification, for example, an incision run within an appendectomy run, possibly **overlapping** with others in time.
* **Parallel‑part (`ConcurrentPartOf_work`).** Two sub‑runs that **overlap** in their windows, coordinated by the same higher‑level run.

**Didactic rule:** **Method composition ≠ proof of Work decomposition.** Sub‑runs often map to method factors, but retries, batching, pipelining, and failures make the mapping non‑isomorphic.

#### A.15.1:5.2 - Key relations among Work

* **`precedes` or `happensBefore`** — strict partial order on Work windows.
* **`overlaps`** — intervals intersect but neither contains the other.
* **`contains` or `within`** — one Work's window contains another's.
* **`causedBy` or `causes`** — pragmatic causal links (e.g., a rework caused by a failed inspection run).
* **`retryOf`** — a new Work instance re‑attempting the same MethodDescription with revised parameters.
* **`resumptionOf`** — a Work episode that **continues** an interrupted run (policy decides identity; see 5.5).

These relations are **run‑time facts**, not design assumptions.

#### A.15.1:5.3 - Operators for roll‑ups (Γ\_time and Γ\_work)

* **Temporal coverage — `Γ_time(S)`**
  For a set `S` of Work parts, returns a **coverage interval set** (union of intervals) or, when required, the **convex hull** `[min t₀, max t₁]`. Use **union** for utilization; use **hull** for lead time.
  *Properties:* idempotent, commutative, monotone under set inclusion.

* **Resource aggregation — `Γ_work(S)`**
  For a set `S` of Work parts, returns the **aggregated resource ledger** (materials, energy, time, money) with de-duplication rules for shared and overlapped parts (context-declared).
  *Properties:* additive on **disjoint** parts; requires **overlap policy** otherwise (e.g., attribute costs to the parent once, not to each child).

**Manager’s tip:** Pick the coverage operator that matches your KPI: **union** for machine utilization; **hull** for calendar elapsed; never mix silently.

#### A.15.1:5.4 - Identity of a Work (extensional criterion, pragmatically framed)

Two Work records refer to the **same Work** iff, in the relevant context:

* their **time–space extent** is the same (within declared tolerance),
* they link to the **same `MethodDescription`**,
* they have the **same performer** (`U.RoleAssignment`), and
* they bind the **same parameters** (or declared‑equivalent values).

If any of these differ (or the context declares equivalence absent), they are **distinct** Work instances (e.g., a retry).

#### A.15.1:5.5 - Interruptions, retries, resumptions (episode policy)

* **Retry:** **new Work** with its own window and parameters; link via `retryOf`.
* **Resumption:** **same Work identity** split into **episodes** if the context’s **episode policy** declares so (e.g., “power loss under 5 minutes keeps identity”).
* **Rework:** **new Work** caused by a failure in earlier Work; link via `causedBy`.

**Why it matters:** plans, costs, and quality stats depend on whether you treat a disruption as **one episode** or **a new run**. Declare the policy **in the bounded context**.

#### A.15.1:5.6 - Compositionality of effects (Δ)

For any Work with parts, the **effect of the whole** must be the **rules-declared composition** of the effects of its parts plus any declared overheads and residuals. Composition must align with the overlap rules used by `Γ_work` (e.g., no double-count of shared fixed costs, and consistent attribution of variable deltas).

### A.15.1:6 - Archetypal grounding (parallel domains)

#### A.15.1:6.1 - Surgical case (overlap and episodes)

* **Top run:** `Appendectomy_Case#2025‑08‑10T09:05–11:42`.
* **Spec:** `Appendectomy_v5` (MethodDescription).
* **Performer:** `OR_Team_A#SurgicalTeamRole:Hospital_2025` (`U.RoleAssignment`).
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** brief power dip 10:02–10:07 → **resumptionOf** same run (per hospital policy).
* **Γ\_time:** union for OR utilization; hull for patient lead time.
* **Γ\_work:** totals consumables and staff time once (no double‑count for overlapping sub‑runs).

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top run:** `ETL_Nightly_2025‑08‑11T01:00–01:47`.
* **Spec:** `ETL_v12.bpmn`.
* **Performer:** `ETL_Runtime#TransformerRole:DataOps_2025`.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `WarehouseWrite` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **Γ\_time:** hull for SLA, union for cluster utilization.
* **Γ\_work:** sum compute minutes; attribute storage input and output once at the parent.

#### A.15.1:6.3 - Thermodynamic cycle (work as a path)

* **Run:** `Carnot_Cycle_Run#2025‑08‑09T13:00–13:06`.
* **Spec:** `Carnot_Cycle_Spec` (MethodDescription with Dynamics model).
* **Performer:** `LabRig_7#TransformerRole:ThermoLab`.
* **Work identity:** the **path in state-space** traced during the interval; outputs: heat and work tallies.
* **Γ\_time:** straightforward interval; **Γ\_work:** integrates energy exchange; no “steps” required.

### A.15.1:7 - Bias‑Annotation (as in E‑cluster)

* **Lenses tested:** `Prag`, `Arch`, `Did`, `Epist`.
* **Scope declaration:** Universal; temporal semantics and episode policy are **context‑local** via `U.BoundedContext`.
* **Rationale:** Gives FPF a clean, actionable notion of **occurrence** compatible with `U.RoleAssignment` and **Role Enactment** (A.2.1; A.15) and with 4D extensional thinking, so that costing, quality, and audit rest on **runs**, not on plans or recipes.

### A.15.1:8 - Conformance Checklist (normative)

**CC‑A15.1‑1 (Strict distinction).**
`U.Work` is a **dated run-time occurrence**. It is **not** a `U.Method` (semantic way), **not** a `U.MethodDescription` (description), **not** a `U.Role` or `U.RoleAssignment` (assignment), and **not** a `U.WorkPlan` (plan or schedule).

**CC‑A15.1‑2 (Required links).**
Every `U.Work` **MUST** reference:
(a) `enactsMethod -> U.Method` (the method enacted),
(b) `methodDescriptionRef -> U.MethodDescription` when the source episteme or editioned method description is live,
(c) `performedBy -> U.RoleAssignment` (the assigned performer in context), and
(d) `executedWithin -> U.System` or `executedWithin -> U.SubSystem` (the operational system or subsystem accountable for the occurrence).

**CC‑A15.1‑3 (Time window).**
Every `U.Work` **MUST** carry a closed interval `[t_start, t_end]` (or an explicitly marked open end for in-flight work) and, where relevant, location or asset.

**CC‑A15.1‑4 (Context anchoring and judgement).**
A `U.Work` **MUST** be judged inside a declared **`U.BoundedContext`** (the **judgement context**).

* By default, the judgement context is **the context of the referenced MethodDescription**.
* If `performedBy` references a `U.RoleAssignment` in a different context, there **MUST** exist an explicit **Bridge (`U.Alignment`)** or policy stating cross-context acceptance. Otherwise, the Work is **non-conformant** in that context.

**CC‑A15.1‑4b (State‑plane anchoring).**
Each `U.Work` **MUST** declare a `StatePlaneRef` for its Δ‑judgement.

**CC‑A15.1‑5 (RoleAssignment validity).**
The `performedBy` `U.RoleAssignment` timespan **MUST** cover the Work interval. If it does not, the Work is **invalid** or must be re-judged in a context that allows retroactive assignments.

**CC‑A15.1‑6 (Parameter binding).**
Parameters declared by the **MethodDescription** **MUST** have concrete values bound **at Work creation or start** and recorded with the Work. Defaults in the specification do not satisfy this requirement.

**CC‑A15.1‑7 (Capability check).**
All capability thresholds stated by the Method or MethodDescription **MUST** be checked against the **holder** in `performedBy` **at the time of execution** (or at defined checkpoints). Violations must be flagged on the Work outcome.

**CC‑A15.1‑8 (Acceptance criteria).**
Success and failure classes and quality grades **MUST** be determined by the acceptance criteria declared or referenced by the **MethodDescription** or **CG-Spec** **in the judgment context**. The verdict is recorded on the Work.

**CC‑A15.1‑9 (Resource honesty).**
All consumptions and costs (energy, materials, machine‑time, money, tool wear) **SHALL** be booked **only** to `U.Work` (not to Method, MethodDescription, Role, or Capability). Estimates may live in specs; **actuals** live in Work.

**CC‑A15.1‑10 (Mereology declared).**
If a Work has parts, the chosen **part relation(s)** must be declared (temporal‑part, episode‑part, operational‑part, concurrent‑part). Ambiguous mixtures are forbidden.

**CC‑A15.1‑11 (Γ\_time selection).**
For any roll‑up, the judgement context **MUST** declare which temporal coverage operator applies: **union** (utilization) or **convex hull** (lead time). Silent mixing is prohibited.

**CC‑A15.1‑12 (Γ\_work aggregation).**
Aggregation of resource ledgers across Work parts **MUST** specify an **overlap policy** (e.g., “attribute shared machine‑time to parent only”) to prevent double‑counting.

**CC‑A15.1‑13 (Identity & retries).**
A retry **MUST** be modeled as a **new Work** linked via `retryOf`. Interruptions that are treated as the **same run** must be modeled as **episodes** (`resumptionOf`) per a context‑declared **episode policy**.

**CC‑A15.1‑14 (Concurrency & ordering).**
Overlaps and precedences among Work **MUST** use interval relations (`overlaps`, `precedes`, `contains`, or `within`). Implicit "step order" claims are not admissible evidence.

**CC‑A15.1‑15 (Cross‑context evidence).**
If a Work is to be accepted in multiple contexts (e.g., regulatory + operational), either:
(a) re‑judge it in each context, or
(b) provide Bridges that map acceptance criteria, units, and roles; never assume cross-context identity by name.

**CC‑A15.1‑16 (Spec changes during run).**
If the MethodDescription version changes mid‑run, the Work **MUST** either:
(a) split into episodes bound to respective specs, or
(b) record an explicit **spec override** event in the judgement context. Silent substitution is forbidden.

**CC‑A15.1‑17 (Distributed performers).**
If multiple `U.RoleAssignment`s jointly perform the same top-level Work (e.g., multi-agent orchestration), the Work **MUST** either:
(a) designate a **lead `U.RoleAssignment`** and list others as **concurrent parts**, or
(b) be modeled as a **parent Work** with child Works per `U.RoleAssignment`.

**CC‑A15.1‑18 (Logs ≠ Work by themselves).**
Logs and telemetry are **evidence** for a Work; they **do not constitute** a Work unless bound to specification, performer, time window, and judgment context.

**CC‑A15.1‑19 (Affected referent).** Each `U.Work` **MUST** name at least one affected referent (e.g., `U.Asset`, product, batch, dataset, or document) via `affected -> {...}`.

**CC‑A15.1‑20 (State‑change witness).** Each `U.Work` **MUST** carry either (a) explicit **pre‑state**/**post‑state** anchors on the declared state‑plane or (b) a **Δ‑predicate** that can be evaluated on evidence. Trivial “no‑op” runs **MUST** be flagged as such.

**CC‑A15.1‑21 (World anchoring vs. record handling).** A run whose only effect is copying or reformatting records **does not** qualify as `U.Work` unless the judgment context declares those records to be the **product referent** (e.g., data-product manufacture).

**CC‑A15.1‑22 (System anchoring).** Each `U.Work` **MUST** declare `executedWithin -> U.System` or `executedWithin -> U.SubSystem`; if different from the asset of change, keep `affected` explicit.

**CC‑A15.1‑23 (Compositionality of Δ).** For composite Work, the parent effect **MUST** be the declared composition of child effects under the same overlap policy as `Γ_work`.

**CC‑A15.1‑24 (No new claims on publication views).** MVPK views for `U.Work` **SHALL NOT** add properties or claims beyond the declared work-occurrence claim; numeric or comparable content **MUST** include unit, scale, reference-plane, and **EditionId** pins; the term **"signature"** is banned on work-publication views.

**CC‑A15.1‑25 (No Γ leakage).** Publication views **MUST** reference Γ operators and policies by id when showing aggregates; they **MUST NOT** encode aggregation semantics in prose or imply defaults. Γ lives in Part B; views carry **pinned references** only.

**CC‑A15.1‑26 (No input-output re-listing).** Publication views **MUST NOT** restate method-description input and output lists; publish **presence pins** and source anchors only (per MVPK §5.4).

**CC‑A15.1‑27 (Lawful orders; return sets).** Any across-run comparison presented on a `U.Work` publication view **MUST** use a declared **ComparatorSet** (map-then-compare), **return sets** when order is partial, and **forbid** hidden scalarization or ordinal means.

**CC‑A15.1‑28 (Comparator and transport pins).** Any numeric or comparable acceptance or KPI on a `U.Work` publication view **MUST** pin `ComparatorSet.edition`, `CG-Spec.edition`, and, where conversions occur, `TransportRegistry.edition` with **Φ** or **Φ^plane** policy-ids; Bridge ids are mandatory for cross-context or cross-plane reuse; penalties affect the reliability relation only.

**CC‑A15.1‑29 (Telemetry hooks, when applicable).** If a Work instance feeds **G.11** or QD and OEE portfolios, it **SHALL** cite `PathId` or `PathSliceId` and the active **policy-id** in its evidence; illumination remains **report-only telemetry** unless CAL explicitly promotes it.

### A.15.1:9 - Temporal & Aggregation Semantics (normative operators & invariants)

#### A.15.1:9.1 - Temporal coverage `Γ_time`

* **Input:** a finite set `S` of Work instances or Work parts.
* **Output:** either (a) the **union** of their intervals, or (b) the **convex hull** `[min t_start, max t_end]`—**as declared by context** and KPI.
* **Invariants:**

  * **Idempotent:** `Γ_time(S ∪ S) = Γ_time(S)`
  * **Commutative:** order of elements irrelevant
  * **Monotone:** if `S ⊆ T` then coverage(S) ⊆ coverage(T) (for union) or hull(S) ⊆ hull(T) (for hull)
* **Usage guidance:**

  * Use **union** for **utilization and availability** (how much of the clock time the asset was actually busy).
  * Use **hull** for **lead time and cycle time** (elapsed from first touch to last release).
  * **Manager’s tip:** Write the choice near the KPI; many disputes are just a hidden union‑vs‑hull mismatch.

#### A.15.1:9.2 - Resource aggregation `Γ_work`

* **Input:** a finite set `S` of Work instances or parts with resource ledgers.
* **Output:** an **aggregated ledger** (materials, energy, machine‑time, money, tool wear) with explicit **overlap policy**.
* **Invariants:**

  * **Additivity on disjoint parts:** if intervals and resources are disjoint by policy, totals add.
  * **No double‑count:** overlapping costs must follow the declared policy (e.g., count once at parent).
  * **Traceability:** each aggregated figure must be reconcilable to contributing Work IDs.
* **Typical policies:**

  * **Parent‑attribution:** shared fixed costs at parent; variable costs at children.
  * **Pro‑rata by wall‑time:** split overlaps by relative durations.
  * **Driver‑based:** allocate by a declared driver (e.g., CPU share, weight, priority).

### A.15.1:10 - Cross-Context Checks (MethodDescription, RoleAssignment, and Work)

When a Work is recorded, perform these **three quick checks**:

1. **Method-description context check.** Does `methodDescriptionRef` refer to a MethodDescription **defined in** the judgement context, or bridged to it, when that source is live?

   * If **no**, the Work is **out‑of‑context**; either change context or add a Bridge.

1. **RoleAssignment context check.** Is `performedBy`'s `U.RoleAssignment` **valid in** the same context, or bridged?

   * If **no**, the Work is **unassigned** for that context; remedy via a valid `U.RoleAssignment` or a policy exception.

1. **Standard–Outcome Check.** Do the Work's inputs, outputs, and metrics satisfy the **acceptance criteria** from the spec **as interpreted in that context**?

   * If **no**, the Work **fails** or is “conditionally accepted” per context policy.

> **Manager’s mnemonic:** Context, assignment, Standard → **CAC**. Fail any → the Work is not acceptable *here* (perhaps acceptable elsewhere).

### A.15.1:11 - Anti‑patterns (and the right move)

* **“The log is the process.”** Dumping telemetry without binding (spec, performer, context) → **Not Work**. Create a Work, link the log as evidence.
* **Record-only transforms.** ETL or replication of records with no declared affected referent (product or dataset as product) -> **Not Work** in this context; either declare the dataset as the product referent or move it to `U.WorkPlan` or the relevant operations pattern.
* **Silent cross‑context acceptance.** “Ops accepted it, so audit accepts it.” → Add a **Bridge** or re‑judge in audit context.
* **Spec drift in mid‑run.** Swapping SOP v5→v6 without recording → Split into episodes or record override.
* **Budget on the method.** Charging costs to Method or Role → Book **only** to Work; keep estimates in specs.
* **Part ambiguity.** Mixing retries, episodes, and operational parts with no declared relation → Choose and declare the part relation.
* **Union-hull confusion.** Changing KPI coverage silently between reports -> declare `Γ_time` policy per KPI.
* **Double‑count in overlaps.** Summing child and parent resource ledgers → Declare and apply an overlap policy.

### A.15.1:12 - Migration notes (quick wins)

1. **Backfill links.** For existing logs, create Work records and attach `isExecutionOf` and `performedBy`.
2. **Name the context.** Pick the judgement context explicitly; add Bridges if multiple contexts must accept.
3. **Record the episode policy.** Decide when an interruption keeps identity or forces a new run.
4. **Choose Γ\_time per KPI.** Put “union” or “hull” in the KPI definition; stop arguing in meetings.
5. **Set an overlap policy.** Write one sentence on how shared costs are allocated; apply consistently.
6. **Pull plans out.** Move calendars to `U.WorkPlan`; let Work record actuals.
7. **Parameter blocks.** Make parameters explicit and bind them at start; root-cause analyses become easier.

### A.15.1:13 - Consequences

| Benefits                                                                                                                 | Trade-offs and mitigations                                                                 |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Auditable reality.** Costs, time, and quality attach to concrete runs; root‑cause analysis and accountability improve. | **More records.** You create Work instances; mitigate with templates and automation.       |
| **Sound roll-ups.** Γ\_time and Γ\_work turn roll-ups from hand-waving into declared policy; KPIs become comparable.     | **Policy discipline.** You must choose union or hull and an overlap policy; write it once. |
| **Cross‑context clarity.** CAC checks prevent silent model drift; bridges make acceptance explicit.                      | **Bridge upkeep.** Keep mappings short and focused; review at releases.                    |
| **4D extensional coherence.** Parts, overlaps, and retries stop double-counting and identity confusion.                  | **Learning curve.** Teach episode vs retry; include examples in onboarding.                |

### A.15.1:13a - SoTA Alignment

**SoTA alignment rule.** A source tradition counts here only when it preserves the local `U.Work` distinction: dated occurrence, role-assigned performer, enacted method, method-description source when live, time window, affected referent, resources, outcome, and evidence path.

| Source tradition | Local invariant adopted | Shortcut rejected |
| --- | --- | --- |
| 4D extensional and BORO-style occurrence modeling | Work identity is tied to occurrence extent plus execution anchors; parts, retries, resumptions, and overlaps are explicit. | Treating a method factor, diagram, or log entry as proof of a work occurrence. |
| Process mining, audit, and operations-management practice | Logs, telemetry, and event records evidence work only after they are bound to performer, method, time window, context, and affected referent. | Treating telemetry alone as `U.Work`. |
| Temporal-interval and aggregation practice | Roll-ups require declared `Γ_time`, `Γ_work`, and overlap policy; partial order and overlap are not hidden in step labels. | Mixing union, hull, parent cost, and child cost without a declared policy. |
| Provenance, observability, and quality-measurement practice | Work records carry evidence paths and currentness hooks without letting evidence, assurance, or gate claims replace the occurrence. | Using an evidence path, assurance statement, or gate result as if it were the performed work. |

### A.15.1:14 - Relations

* **Builds on:** A.1 Holonic Foundation; A.1.1 `U.BoundedContext`; **U.System**; A.2 `U.Role`; A.2.1 `U.RoleAssignment`; A.2.2 `U.Capability`; A.3.1 `U.Method`; A.3.2 `U.MethodDescription`.
* **Coordinates with:** A.15 Role-Method-Work Alignment (the "four-slot grammar"); B.1 Γ (aggregation) for resource and time operators; E-cluster lexical rules (L-PROC and L-FUNC).
* **Informs:** reporting and KPI patterns; assurance and evidence patterns (Work as the anchor for audits); scheduling patterns (`U.WorkPlan` -> `U.Work` deltas).

### A.15.1:15 - Didactic quick cards

* **What is Work?** *How it went this time* → dated, resourced, accountable.
* **Four-slot grammar:** Who? **RoleAssignment**. Can? **Capability**. How? **Method or MethodDescription**. Did? **Work**.
* **CAC checks:** **Context** (judgement), **assignment** (valid `U.RoleAssignment`), **Standard** (acceptance criteria).
* **Roll‑ups:** `Γ_time = union` (utilization) or `hull` (lead time); `Γ_work` with a declared overlap policy.
* **Episodes vs retries:** same run split vs new run; write the policy.
* **Resource honesty:** actuals booked **only** to Work; estimates live in specs.

### A.15.1:15a - P2W Performed-Work Use Relation

When `E.18.1` reaches performed work, `U.Work` carries the dated occurrence: performer, method-description source, parameters, resources, time window, pre-state, post-state, outputs, outcome, and audit trace.

A `U.Work` occurrence may cite a `U.WorkPlan` or `SlotFillingsPlanItem` as planned baseline. The performed-work record carries launch values, actuals, substitutions, variance, telemetry, and result-related records; comparator, transport, `PrincipleFrame`, evidence, assurance, and gate claims are separate live relations when the carry-through record names them.

### A.15.1:16 - Lowering, Repair, and Refresh Conditions

Lower a candidate `U.Work` claim when performer, enacted method, method-description source when live, time window, `executedWithin`, affected referent, parameter bindings, resources, outcome, or state-change witness cannot be named at the granularity required by the next work move. The admissible lowered record is a plan note, evidence note, source-gap note, source-restoration request, or method-description reference, not a backdated work occurrence.

Repair the work record when a subsequent source changes the work interval, performer, role assignment, enacted method, method-description edition, parameter binding, resource ledger, outcome, affected referent, state-plane anchor, pre-state or post-state anchor, overlap policy, or aggregation policy. Repair only the changed relation: do not rewrite the method when only evidence changed, do not rewrite evidence when only work time changed, and do not convert a plan or source-restoration request into work.

Refresh before cross-context acceptance, aggregation, comparison, result measurement, release reliance, gate use, evidence use, assurance use, QD or OEE archive use, or P2W carry-through use. If the claim being made after refresh is no longer performed work, use the governing pattern for that relation and keep only the returned `U.Work` reference here.

### A.15.1:End


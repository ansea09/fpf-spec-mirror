We adopt a **4D extensional** stance for occurrences: a Work is identified primarily by its **spatiotemporal extent** and its execution anchors (spec used, performer, parameterization). This avoids double‑counting and keeps aggregation sound. FPF adapts insights from BORO/constructive ontologies to Work while staying practical.

#### A.15.1:5.1 - Parts and wholes of Work (design‑neutral, run‑time facts)

* **Temporal‑part (`TemporalPartOf_work`).** A proper **time‑slice** of a Work (e.g., the first 10 minutes of a 2‑hour run). Useful for monitoring and SLAs.
* **Episode‑part (`EpisodeOf_work`).** A **resumption fragment** after an interruption (same run identity if policy deems it one episode; see 5.5).
* **Operational‑part (`OperationalPartOf_work`).** A **sub‑run** that enacts a **factor** of the Method/Spec (e.g., “incision” run within “appendectomy” run), possibly **overlapping** with others in time.
* **Parallel‑part (`ConcurrentPartOf_work`).** Two sub‑runs that **overlap** in their windows, coordinated by the same higher‑level run.

**Didactic rule:** **Method composition ≠ proof of Work decomposition.** Sub‑runs often map to method factors, but retries, batching, pipelining, and failures make the mapping non‑isomorphic.

#### A.15.1:5.2 - Key relations among Work

* **`precedes/happensBefore`** — strict partial order on Work windows.
* **`overlaps`** — intervals intersect but neither contains the other.
* **`contains/within`** — one Work’s window contains another’s.
* **`causedBy/causes`** — pragmatic causal links (e.g., a rework caused by a failed inspection run).
* **`retryOf`** — a new Work instance re‑attempting the same MethodDescription with revised parameters.
* **`resumptionOf`** — a Work episode that **continues** an interrupted run (policy decides identity; see 5.5).

These relations are **run‑time facts**, not design assumptions.

#### A.15.1:5.3 - Operators for roll‑ups (Γ\_time and Γ\_work)

* **Temporal coverage — `Γ_time(S)`**
  For a set `S` of Work parts, returns a **coverage interval set** (union of intervals) or, when required, the **convex hull** `[min t₀, max t₁]`. Use **union** for utilization; use **hull** for lead time.
  *Properties:* idempotent, commutative, monotone under set inclusion.

* **Resource aggregation — `Γ_work(S)`**
  For a set `S` of Work parts, returns the **aggregated resource ledger** (materials, energy, time, money) with de‑duplication rules for shared/overlapped parts (context‑declared).
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

For any Work with parts, the **effect of the whole** must be the **rules‑declared composition** of the effects of its parts plus any declared overheads/residuals. Composition must align with the overlap rules used by `Γ_work` (e.g., no double‑count of shared fixed costs, and consistent attribution of variable deltas).

### A.15.1:6 - Archetypal grounding (parallel domains)

#### A.15.1:6.1 - Surgical case (overlap and episodes)

* **Top run:** `Appendectomy_Case#2025‑08‑10T09:05–11:42`.
* **Spec:** `Appendectomy_v5` (MethodDescription).
* **Performer:** `OR_Team_A#SurgicalTeamRole:Hospital_2025` (RoleAssigning).
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** brief power dip 10:02–10:07 → **resumptionOf** same run (per hospital policy).
* **Γ\_time:** union for OR utilization; hull for patient lead time.
* **Γ\_work:** totals consumables and staff time once (no double‑count for overlapping sub‑runs).

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top run:** `ETL_Nightly_2025‑08‑11T01:00–01:47`.
* **Spec:** `ETL_v12.bpmn`.
* **Performer:** `ETL_Runtime#TransformerRole:DataOps_2025`.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `Load` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **Γ\_time:** hull for SLA, union for cluster utilization.
* **Γ\_work:** sum compute minutes; attribute storage I/O once at the parent.

#### A.15.1:6.3 - Thermodynamic cycle (work as a path)

* **Run:** `Carnot_Cycle_Run#2025‑08‑09T13:00–13:06`.
* **Spec:** `Carnot_Cycle_Spec` (MethodDescription with Dynamics model).
* **Performer:** `LabRig_7#TransformerRole:ThermoLab`.
* **Work identity:** the **path in state‑space** traced during the interval; outputs: heat/work tallies.
* **Γ\_time:** straightforward interval; **Γ\_work:** integrates energy exchange; no “steps” required.


### A.15.1:7 - Bias‑Annotation (as in E‑cluster)

* **Lenses tested:** `Prag`, `Arch`, `Did`, `Epist`.
* **Scope declaration:** Universal; temporal semantics and episode policy are **context‑local** via `U.BoundedContext`.
* **Rationale:** Gives FPF a clean, actionable notion of **occurrence** compatible with `U.RoleAssignment` / **Role Enactment** (A.2.1; A.15) and with 4D extensional thinking, so that costing, quality, and audit rest on **runs**, not on plans or recipes.

### A.15.1:8 - Conformance Checklist (normative)

**CC‑A15.1‑1 (Strict distinction).**
`U.Work` is a **dated run‑time occurrence**. It is **not** a `U.Method` (semantic way), **not** a `U.MethodDescription` (description), **not** a `U.Role/RoleAssigning` (assignment), and **not** a `U.WorkPlan` (plan/schedule).

**CC‑A15.1‑2 (Required links).**
Every `U.Work` **MUST** reference:
(a) `isExecutionOf → U.MethodDescription` (the spec followed; **edition pinned**),
(b) `performedBy → U.RoleAssignment` (the assigned performer in context), and
(c) `executedWithin → U.System/SubSystem` (the operational system accountable for the occurrence).

**CC‑A15.1‑3 (Time window).**
Every `U.Work` **MUST** carry a closed interval `[t_start, t_end]` (or an explicitly marked open end for in‑flight work) and, where relevant, location/asset.

**CC‑A15.1‑4 (Context anchoring & judgement).**
A `U.Work` **MUST** be judged inside a declared **`U.BoundedContext`** (the **judgement context**).

* By default, the judgement context is **the context of the referenced MethodDescription**.
* If `performedBy` references a RoleAssigning in a different context, there **MUST** exist an explicit **Bridge (`U.Alignment`)** or policy stating cross‑context acceptance. Otherwise, the Work is **non‑conformant** in that context.

**CC‑A15.1‑4b (State‑plane anchoring).**
Each `U.Work` **MUST** declare a `StatePlaneRef` for its Δ‑judgement.

**CC‑A15.1‑5 (RoleAssigning validity).**
The `performedBy` RoleAssigning’s `timespan` **MUST** cover the Work interval. If it does not, the Work is **invalid** or must be re‑judged in a context that allows retroactive assignments.

**CC‑A15.1‑6 (Parameter binding).**
Parameters declared by the **MethodDescription** **MUST** have concrete values bound **at Work creation/start** and recorded with the Work. Defaults in the spec do not satisfy this requirement.

**CC‑A15.1‑7 (Capability check).**
All capability thresholds stated by the Method/MethodDescription **MUST** be checked against the **holder** in `performedBy` **at the time of execution** (or at defined checkpoints). Violations must be flagged on the Work outcome.

**CC‑A15.1‑8 (Acceptance criteria).**
Success/failure and quality grades **MUST** be determined by the acceptance criteria declared (or referenced) by the **MethodDescription**/**CG‑Spec** **in the judgment context**. The verdict is recorded on the Work.

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
Overlaps and precedences among Work **MUST** use interval relations (`overlaps`, `precedes`, `contains/within`). Implicit “step order” claims are not admissible evidence.

**CC‑A15.1‑15 (Cross‑context evidence).**
If a Work is to be accepted in multiple contexts (e.g., regulatory + operational), either:
(a) re‑judge it in each context, or
(b) provide Bridges that map acceptance criteria/units/roles; never assume cross‑context identity by name.

**CC‑A15.1‑16 (Spec changes during run).**
If the MethodDescription version changes mid‑run, the Work **MUST** either:
(a) split into episodes bound to respective specs, or
(b) record an explicit **spec override** event in the judgement context. Silent substitution is forbidden.

**CC‑A15.1‑17 (Distributed performers).**
If multiple RoleAssignings jointly perform the same top‑level Work (e.g., multi‑agent orchestration), the Work **MUST** either:
(a) designate a **lead RoleAssigning** and list others as **concurrent parts**, or
(b) be modeled as a **parent Work** with child Works per RoleAssigning.

**CC‑A15.1‑18 (Logs ≠ Work by themselves).**
Logs/telemetry are **evidence** for a Work; they **do not constitute** a Work unless bound to (spec, performer, time window) and judged in a context.

**CC‑A15.1‑19 (Affected referent).** Each `U.Work` **MUST** name at least one affected referent (e.g., `U.Asset`, product/batch, dataset/document) via `affected → {…}`.

**CC‑A15.1‑20 (State‑change witness).** Each `U.Work` **MUST** carry either (a) explicit **pre‑state**/**post‑state** anchors on the declared state‑plane or (b) a **Δ‑predicate** that can be evaluated on evidence. Trivial “no‑op” runs **MUST** be flagged as such.

**CC‑A15.1‑21 (World anchoring vs. record‑handling).** A run whose only effect is copying/reformatting records **does not** qualify as `U.Work` unless the judgment context declares those records to be the **product referent** (e.g., data‑product manufacture).

**CC‑A15.1‑22 (System anchoring).** Each `U.Work` **MUST** declare `executedWithin → U.System/SubSystem`; if different from the asset of change, keep `affected` explicit.

**CC‑A15.1‑23 (Compositionality of Δ).** For composite Work, the parent effect **MUST** be the declared composition of child effects under the same overlap policy as `Γ_work`.

**CC‑A15.1‑24 (No new claims on faces).** MVPK faces for `U.Work` **SHALL NOT** add properties/claims beyond the intensional arrow; numeric/comparable content **MUST** include unit/scale/reference‑plane/**EditionId** pins; the term **“signature”** is banned on faces.

**CC‑A15.1‑25 (No Γ‑leakage).** Faces **MUST** reference Γ operators/policies by id when showing aggregates; they **MUST NOT** encode aggregation semantics in prose or imply defaults. Γ lives in Part B; faces carry **pinned references** only.

**CC‑A15.1‑26 (No I/O re‑listing).** Faces **MUST NOT** restate intensional I/O; publish **presence‑pins** and anchors only (per MVPK §5.4).

**CC‑A15.1‑27 (Lawful orders; return sets).** Any across‑run comparison presented on a `U.Work` face **MUST** use a declared **ComparatorSet** (map‑then‑compare), **return sets** when order is partial, and **forbid** hidden scalarization/ordinal means.

**CC‑A15.1‑28 (Comparator/Transport pins).** Any numeric/comparable acceptance or KPI on a `U.Work` face **MUST** pin `ComparatorSet.edition`, `CG‑Spec.edition`, and (where conversions occur) `TransportRegistry.edition` with **Φ/Φ^plane** policy‑ids; Bridge ids are mandatory for cross‑context/plane reuse; **penalties → R only**.

**CC‑A15.1‑29 (Telemetry hooks, when applicable).** If a Work instance feeds **G.11** or QD/OEE portfolios, it **SHALL** cite `PathId/PathSliceId` and the active **policy‑id** in its evidence; illumination remains **report‑only telemetry** unless CAL explicitly promotes it.

### A.15.1:9 - Temporal & Aggregation Semantics (normative operators & invariants)

#### A.15.1:9.1 - Temporal coverage `Γ_time`

* **Input:** a finite set `S` of Work instances or Work parts.
* **Output:** either (a) the **union** of their intervals, or (b) the **convex hull** `[min t_start, max t_end]`—**as declared by context** and KPI.
* **Invariants:**

  * **Idempotent:** `Γ_time(S ∪ S) = Γ_time(S)`
  * **Commutative:** order of elements irrelevant
  * **Monotone:** if `S ⊆ T` then coverage(S) ⊆ coverage(T) (for union) or hull(S) ⊆ hull(T) (for hull)
* **Usage guidance:**

  * Use **union** for **utilization/availability** (how much of the clock time the asset was actually busy).
  * Use **hull** for **lead/cycle time** (elapsed from first touch to last release).
  * **Manager’s tip:** Write the choice near the KPI; many disputes are just a hidden union‑vs‑hull mismatch.

#### A.15.1:9.2 - Resource aggregation `Γ_work`

* **Input:** a finite set `S` of Work instances or parts with resource ledgers.
* **Output:** an **aggregated ledger** (materials, energy, machine‑time, money, tool wear) with explicit **overlap policy**.
* **Invariants:**

  * **Additivity on disjoint parts:** if intervals/resources are disjoint by policy, totals add.
  * **No double‑count:** overlapping costs must follow the declared policy (e.g., count once at parent).
  * **Traceability:** each aggregated figure must be reconcilable to contributing Work IDs.
* **Typical policies:**

  * **Parent‑attribution:** shared fixed costs at parent; variable costs at children.
  * **Pro‑rata by wall‑time:** split overlaps by relative durations.
  * **Driver‑based:** allocate by a declared driver (e.g., CPU share, weight, priority).

### A.15.1:10 - Cross‑context checks (MethodDescription ↔ RoleAssigning ↔ Work)

When a Work is recorded, perform these **three quick checks**:

1. **Spec–Context Check.** Does `isExecutionOf` refer to a MethodDescription **defined in** the judgement context (or bridged to it)?

   * If **no**, the Work is **out‑of‑context**; either change context or add a Bridge.

1. **RoleAssigning–Context Check.** Is `performedBy`’s RoleAssigning **valid in** the same context (or bridged)?

   * If **no**, the Work is **unassigned** for that context; remedy via a valid RoleAssigning or a policy exception.

1. **Standard–Outcome Check.** Do the Work’s inputs/outputs and metrics satisfy the **acceptance criteria** from the spec **as interpreted in that context**?

   * If **no**, the Work **fails** or is “conditionally accepted” per context policy.

> **Manager’s mnemonic:** Context, assignment, Standard → **CAC**. Fail any → the Work is not acceptable *here* (perhaps acceptable elsewhere).


### A.15.1:11 - Anti‑patterns (and the right move)

* **“The log is the process.”** Dumping telemetry without binding (spec, performer, context) → **Not Work**. Create a Work, link the log as evidence.
* **Record‑only transforms.** ETL/replication of records with no declared affected referent (product/dataset as product) → **Not Work** in this context; either declare the dataset as the product referent or move it to `U.WorkPlan`/operations‑support.
* **Silent cross‑context acceptance.** “Ops accepted it, so audit accepts it.” → Add a **Bridge** or re‑judge in audit context.
* **Spec drift in mid‑run.** Swapping SOP v5→v6 without recording → Split into episodes or record override.
* **Budget on the method.** Charging costs to Method or Role → Book **only** to Work; keep estimates in specs.
* **Part ambiguity.** Mixing retries, episodes, and operational parts with no declared relation → Choose and declare the part relation.
* **Union/hull confusion.** Changing KPI coverage silently between reports → Declare `Γ_time` policy per KPI.
* **Double‑count in overlaps.** Summing child and parent resource ledgers → Declare and apply an overlap policy.


### A.15.1:12 - Migration notes (quick wins)

1. **Backfill links.** For existing logs, create Work records and attach `isExecutionOf` and `performedBy`.
2. **Name the context.** Pick the judgement context explicitly; add Bridges if multiple contexts must accept.
3. **Publish the episode policy.** Decide when an interruption keeps identity vs forces a new run.
4. **Choose Γ\_time per KPI.** Put “union” or “hull” in the KPI definition; stop arguing in meetings.
5. **Set an overlap policy.** Write one sentence on how shared costs are allocated; apply consistently.
6. **Pull plans out.** Move calendars to `U.WorkPlan`; let Work record actuals.
7. **Parameter blocks.** Make parameters explicit and bind them at start; your root‑cause analyses will get 10× easier.


### A.15.1:13 - Consequences

| Benefits                                                                                                                 | Trade‑offs / mitigations                                                                   |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Auditable reality.** Costs, time, and quality attach to concrete runs; root‑cause analysis and accountability improve. | **More records.** You create Work instances; mitigate with templates and automation.       |
| **Sound roll‑ups.** Γ\_time/Γ\_work turn roll‑ups from hand‑waving into declared policy; KPIs become comparable.         | **Policy discipline.** You must choose union vs hull and an overlap policy; write it once. |
| **Cross‑context clarity.** CAC checks prevent silent model drift; bridges make acceptance explicit.                      | **Bridge upkeep.** Keep mappings short and focused; review at releases.                    |
| **4D extensional coherence.** Parts/overlaps/retries stop double‑counting and identity confusion.                        | **Learning curve.** Teach episode vs retry; include examples in onboarding.                |


### A.15.1:14 - Relations

* **Builds on:** A.1 Holonic Foundation; A.1.1 `U.BoundedContext`; **U.System**; A.2 `U.Role`; A.2.1 `U.RoleAssignment`; A.2.2 `U.Capability`; A.3.1 `U.Method`; A.3.2 `U.MethodDescription`.
* **Coordinates with:** A.15 Role–Method–Work Alignment (the “four‑slot grammar”); B.1 Γ (aggregation) for resource/time operators; E‑cluster lexical rules (L‑PROC/L‑FUNC).
* **Informs:** Reporting/KPI patterns; Assurance/evidence patterns (Work as the anchor for audits); Scheduling patterns (`U.WorkPlan` ↔ `U.Work` deltas).


### A.15.1:15 - Didactic quick cards

* **What is Work?** *How it went this time* → dated, resourced, accountable.
* **Four‑slot grammar:** Who? **RoleAssigning**. Can? **Capability**. How? **Method/MethodDescription**. Did? **Work**.
* **CAC checks:** **Context** (judgement), **assignment** (valid RoleAssigning), **Standard** (acceptance criteria).
* **Roll‑ups:** `Γ_time = union` (utilization) or `hull` (lead time); `Γ_work` with a declared overlap policy.
* **Episodes vs retries:** same run split vs new run; write the policy.
* **Resource honesty:** actuals booked **only** to Work; estimates live in specs.

### A.15.1:End

## A.15.2 - U.WorkPlan

### A.15.2:1 - Context (plain‑language motivation)

Operations live on **time**. Even with perfect roles, abilities, and methods, nothing ships unless we **decide when and by whom** concrete runs **should** happen, under what **constraints** and **budgets**. Teams need a first‑class concept for **plans and schedules** that does **not** get confused with:

* the **semantic “way of doing”** (that is `U.Method`),
* the **written recipe** (that is `U.MethodDescription`),
* the **actual execution** (that is `U.Work`), or
* the **state laws** (that is `U.Dynamics`).

`U.WorkPlan` is that missing anchor.


### A.15.2:2 - Problem (what breaks without `WorkPlan`)

1. **“Workflow = schedule” conflation.** Flowcharts or code are used as calendars; resource clashes and SLA misses follow.
2. **Plan/run blur.** Gantt bars or Kanban tickets are reported as if the work already happened; audits and costing degrade.
3. **Spec/time leakage.** People and calendars creep into MethodDescriptions; reuse and staffing agility collapse.
4. **No variance model.** Without planned baselines, deviations in time, cost, and quality cannot be explained or improved.
5. **Structure entanglement.** BoM and org charts get baked into “process” views; plans become brittle and unmaintainable.


### A.15.2:3 - Forces (what we must balance)

| Force                              | Tension we resolve                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Universality vs. domain idioms** | One plan concept that fits hospitals, fabs, data centers, and research labs—while honoring local terms. |
| **Commitment vs. flexibility**     | Plans must be firm enough to coordinate, yet easy to update as reality changes.                         |
| **Assignment vs. assignment**     | Plans may name intended performers; the actual assignment must still be checked at run time.           |
| **Budgets vs. actuals**            | Plans carry targets and reservations; only Work carries actual spend.                                   |
| **Decomposition vs. mapping**      | Plan tasks decompose conveniently; they do not force a shape on actual Work runs.                       |


### A.15.2:4 - Solution — the `U.WorkPlan` as the time‑bound intention to execute Work

#### A.15.2:4.1 - Definition

**`U.WorkPlan`** is an **`U.Episteme`** that **declares intended `U.Work` occurrences** over a horizon, with **planned windows**, **dependencies**, **intended performers** (as **role kinds** or **proposed RoleAssignings**), **resource budgets/reservations**, and **acceptance targets**—**within a `U.BoundedContext`**.

> **Strict distinction (memory aid):**
> **Method** = *how in principle*. **MethodDescription** = *how it is written*.
> **WorkPlan** = *when, by whom in intent, under which constraints*.
> **Work** = *how it went this time*.

#### A.15.2:4.2 - Plan Items (what a `WorkPlan` is made of)

A `U.WorkPlan` **contains Plan Items** (think: scheduled tasks/ops), each of which typically states:

1. **Target Method/Spec** — the **Method** to be enacted and the **MethodDescription** intended for enactment.
2. **Planned window** — e.g., earliest start/latest finish, timebox, recurrence (cron‑like), blackout periods.
3. **Role requirements** — **role kinds** required (not people), optional **proposed RoleAssigning(s)** if pre‑assignment is allowed in the context.
4. **Capability thresholds** — minimal abilities required of the performer (checked at run time).
5. **Resource budgets/reservations** — planned energy/materials/machine slots/money; reservations on assets.
6. **Dependencies** — precedence/overlap permissions; gates/approvals.
7. **Acceptance targets** — quality windows/SLA targets to be judged when Work completes.
8. **Location/asset constraints** — where the run is expected to take place.
9. **Links to Service promises** (if any) — external commitments that this plan aims to satisfy.

> **Didactic guardrail:** **No logs or actuals** belong in a WorkPlan; **no step logic** or solver internals either—that’s the Method/Spec.

#### A.15.2:4.3 - Clear distinctions (lexical sanity for “schedule/process/workflow”)

| If you say…                                 | In FPF it is…                                        | Why                                               |
| ------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| “The **schedule** for tomorrow’s surgeries” | **`U.WorkPlan`**                                     | Calendar of intended runs (who/when constraints). |
| “The **workflow** for appendectomy”         | **`U.MethodDescription`** (and `U.Method`)                  | Recipe and semantic way, not a calendar.          |
| “The **process** already ran at 10:00”      | **`U.Work`**                                         | A dated run with resources and outcomes.          |
| “The **thermodynamic process** path”        | **`U.Work`** (occurrence) + **`U.Dynamics`** (model) | A realized trajectory plus its model, not a plan. |
| “The **plan** assigns Dr. Lee”              | **WorkPlan** naming an **intended** RoleAssigning      | assignment is still validated at run time.       |
| “The **budget** for Shift‑B”                | **WorkPlan** (planned ledger)                        | Actual costs land on **Work**, not on the plan.   |

> **L‑SCHED (lexical rule).** In this document, words like **schedule**, **calendar**, **rota**, **Gantt**, **plan** point to **`U.WorkPlan`** unless explicitly redefined by a bounded context glossary.

#### A.15.2:4.4 - Plan mereology (composition of plans ≠ composition of methods or runs)

Keep three separations crystal‑clear:

* **Method composition** (design‑time semantics) → produces **new Methods**.
* **Work composition** (run‑time occurrences) → produces **parent/child runs** with overlaps/episodes.
* **Plan mereology** (epistemic structure) → organizes **Plan Items** for coordination (phases, sprints, shifts), with **precedence** and **resource reservations**.

**Common relations among Plan Items:**

* **`Precedes_pl` / `DependsOn_pl`** — start/finish constraints and gates.
* **`MayOverlap_pl` / `MutuallyExclusive_pl`** — allowed overlaps vs exclusive windows.
* **`Refines_pl`** — a child plan item tightens windows/budgets of a parent.
* **`Alternative_pl`** — planned alternatives (e.g., backup rig, backup team).

**Didactic rule:** A Plan Item **does not force** an identical Work shape; mapping is via **fulfilment** and **variance** (see §6).

#### A.15.2:4.5 - How `WorkPlan` meets `Work` (fulfilment & variance)

When reality happens, each `U.Work` may:

* **Fulfil** a Plan Item — link `plannedAs → PlanItem`.
* **Partially fulfil** — multiple Work instances share one Plan Item (e.g., split run), or one Work fulfils several Plan Items (e.g., consolidated batch).
* **Deviate** — execute with method/spec substitution, different window, different performer (still valid or policy‑exception).
* **Be unplanned** — Work with no Plan Item (emergency, ad‑hoc); must be labeled as such.

**Variance dimensions** the plan expects to report on:

* **Schedule variance (Δt):** early/late vs planned window.
* **Cost variance (Δc):** actual resource spend vs budget.
* **Scope variance:** different Method/Spec than planned (with justification).
* **Quality variance:** acceptance verdict vs target.
* **Assignment variance:** intended vs actual RoleAssigning.

> **Manager’s view:** A plan that cannot report variance is a calendar picture, not a management tool.


### A.15.2:5 - What a good `WorkPlan` states (review checklist)

Use this as a human‑readable checklist (not a rigid schema):

1. **Horizon & cadence** (e.g., “W36 surgeries, daily ETL”).
2. **Plan Items** with: target Method/Spec, planned windows, dependencies.
3. **Role requirements** (kinds) and **intended assignments** (optional, context‑lawful).
4. **Capability thresholds** and **safety envelopes**.
5. **Resource budgets** and **reservations** on assets.
6. **Acceptance targets** (SLA/quality windows).
7. **Bridges** if plan spans **multiple contexts** (operations ↔ audit/regulatory).
8. **Baseline/version** and **change notes** (so variance is attributable).
9. **Policy pointers** (episode policy, overlap policy for Work roll‑ups if needed for KPIs).
10. **Exceptions path** (how ad‑hoc/emergency work is planned post‑factum).


### A.15.2:6 - Archetypal grounding (parallel domains)

#### A.15.2:6.1 - Hospital OR day plan (shift rota + cases)

* **WorkPlan:** `OR_DayPlan_2025‑08‑12`.
* **Plan Items:** `Case#1 Appendectomy`, `Case#2 Hernia`, with windows, Context assignments, and surgeon **role kinds**; anesthetist **intended RoleAssigning** provided.
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
* **Fulfilment:** Deployment Work passes ops targets; audit Work passes later—variance reported per context.


### A.15.2:7 - Bias‑Annotation (as in E‑cluster)

* **Lenses tested:** `Did`, `Prag`, `Arch`, `Epist`.
* **Scope declaration:** Universal; meanings of windows/budgets/permissions are **context‑local** via `U.BoundedContext`.
* **Rationale:** Elevates **planning/scheduling** to a first‑class episteme that coordinates Methods, RoleAssignings, and Work without conflation.

### A.15.2:End

## A.15.3 - SlotFillingsPlanItem

> **Tech-name:** `SlotFillingsPlanItem`
> **Plain-name:** planned slot-fillings baseline item (planned baseline)
> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A → A.15 (Work & WorkPlanning)
> **Builds on:** pattern template (E.8), `U.WorkPlan` (A.15.2), Work enactment discipline (A.15.1 / TGA), Context discipline (E.10.D1), `MechSuiteDescription` (A.6.7), conformance discipline (E.19), publication/view discipline (E.17; views are projections, not places of meaning)
> **Used by:** planned-baseline requirements from suites/kits; P2W (selection → WorkPlanning → WorkEnactment); Part G universalization
> **Purpose (one line):** provide a universal, context-explicit **planned baseline** that maps a slot-owner’s `SlotKind`s to **planned fillers**, to be consumed by Work enactment where launch values are finalized.

**Minting notes (informative)**
* **Mint vs reuse:** This pattern mints the kind name `SlotFillingsPlanItem`. It reuses existing Core terms and disciplines (e.g., `U.WorkPlan.PlanItem`, SlotKind/ValueKind/RefKind/refMode discipline, edition pinning, `U.BoundedContext`, and the P2W split between WorkPlanning and WorkEnactment).
* **`SlotFillingsPlanItem` (kind name):** keep the suffix `PlanItem` to preserve the WorkPlanning locus. Do not mint aliases like *SlotBinding…* (conflicts with the A.6.5 binding discipline) or *SlotValue…* (ambiguous owner/context).
* **Anchor names:** if any anchors in §4.2 are later materialized as formal field names, keep `…_ref` only for fields whose values are concrete RefKind handles, and keep `…_id` only for identifiers. Avoid introducing generic placeholders like `SpecRef/PolicyRef/GateRef` inside this pattern; prefer existing concrete ref kinds (or a dedicated DRR+LEX step).
* **Row vocabulary:** treat `SlotFillingRow` and `PlannedFiller` as *internal* names of this pattern unless/until a separate DRR+LEX step promotes them to shared tokens.

### A.15.3:1 - Problem frame

FPF frequently needs to make **reproducible, reviewable choices** about *what fills which conceptual slot* (spec refs, policy refs, mechanism-instance refs, time selectors, evidence hooks, etc.) **before** any Work is enacted. These choices must be visible as a planned baseline for a concrete P2W slice (CG-frame / path slice / publication scope), and must remain distinct from run-time “actuals” and gate decisions.

However, absent a universal WorkPlanning artifact for “architecture-by-planned-slot-filling”, authors tend to hide these choices inside mechanism prose, CG/CN specs, ad-hoc cards, or informal checklists—making Part G patterns difficult to universalize and making Work audit trails ambiguous.

`SlotFillingsPlanItem` addresses this by defining a **WorkPlan PlanItem kind** whose job is to state, in one place and with explicit context, a mapping:

> *(Target slot owner, slot kind) → planned filler (ByValue | ByRef(<concrete RefKind>), with edition pins when needed)*

and to do so in a form that can be cited by Work enactment and by suite/kit contract pins, without collapsing into “execution” or “decision logging”. 

### A.15.3:2 - Problem (what breaks without it)

Without an explicit `SlotFillingsPlanItem` baseline, at least six failure modes recur:

1. **Hidden slot ownership and meaning drift:** a planned filler is stated without making explicit *whose* slot set is being filled, allowing silent reinterpretation of `SlotKind`s across kits/suites.

2. **Plan/execution collapse:** plan documents get “backfilled” with run-time values, so there is no stable planned baseline and no clean variance trail. WorkPlan explicitly warns against this. 

3. **Implicit time (“latest”) and implicit recency:** planned claims about comparability or launch readiness omit an explicit `Γ_time`, which violates the time discipline (“no implicit recency”). 

4. **Edition ambiguity:** references to methods/policies/specs are not edition-pinned where reproducibility requires it, or the plan mutates the edition vector instead of citing pinned editions (edition changes are crossings, not “plan edits”). 
   A particularly harmful subtype is **edition-key backfill**: retroactively editing a previously used baseline so that an edition-key change looks like an innocent PlanItem edit (hiding the required GateCrossing witness and breaking audit traceability).

5. **Crossing invisibility:** cross-context/plane expectations (Bridge + policy ids) are not stated at plan time, so later gate crossings appear as “magic” rather than traceable expected constraints.

6. **G-pattern fragmentation:** each Part G pattern invents its own place to stash planned refs (method pick, comparator pick, QD archive config, etc.), blocking a clean “G.Core” universal layer and making modular reuse brittle.

### A.15.3:3 - Forces (what we must balance)

* **Strict distinction:** planned baseline is not a run-time witness; launch values are finalized only in Work enactment. 
* **Context must be explicit:** every normative claim/rule is context-bound; the PlanItem must carry its context rather than relying on file location or prose. 
* **Time must be explicit:** no implicit “latest”; any plan that will be cited by comparability/launch checks needs an explicit `Γ_time` selector/rule. 
* **SlotKind meaning is stable:** the plan may choose fillers, but must not reinterpret SlotKinds or smuggle new semantics into indices.
* **Derived indices must not become “places of meaning”:** projections like “planned spec refs” are useful, but must remain derivable from the authoritative rows.
* **Conceptual, not procedural:** no solver steps, no lints, no “data governance”; this is an epistemic object used by humans in review.
* **Supports universalization:** one PlanItem pattern must be usable across the whole of Part G, not just G.5.
* **Integrates with suites/kits:** suites may require a planned-baseline ref and may act as slot owners. 

| Force | Tension |
| --- | --- |
| Plan/run split | Plan must be citeable without containing run-time values. |
| Slot meaning stability | SlotKinds must not drift by implicit owner changes. |
| Edition honesty | Baselines must pin editions where meaning changes; avoid “latest”. |
| Suite/kit modularity | Suites define contracts; baselines choose fillers for a plan instance. |
| Auditability | A reader must reconstruct “what was planned” without chasing hidden defaults. |
| Extensibility | Allow suite-specialized variants without breaking universal core. |

### A.15.3:4 - Solution

#### A.15.3:4.1 Definition

A `SlotFillingsPlanItem` is a **kind of `U.WorkPlan.PlanItem`** whose content is a **planned slot-fillings ledger** for a *single* slot owner, within an explicit P2W context.

It is a **WorkPlanning baseline**, intended to be:

* produced/approved in WorkPlanning,
* **cited** by downstream Work enactment (as planned baseline),
* compared against actual fillings (variance recorded in Work, not by rewriting the plan). 

**Normative note (I/D/Spec vs views):** A `SlotFillingsPlanItem` is a Description-level planning episteme (a PlanItem). It MAY be projected into `U.View` (e.g., `TechCard(SlotFillingsPlanItemRef)`), but any view is strictly a projection and MUST NOT introduce additional claims or “shadow defaults”.

#### A.15.3:4.2 Core conceptual descriptors (not a data schema)

A conformant `SlotFillingsPlanItem` SHALL provide the following description (names are indicative; the semantics are normative):

1. **PlanItem core (from A.15.2)**
   The PlanItem MUST remain a planning artifact: it may include assumptions, dependencies, constraints, expected artifacts, and notes; it MUST NOT contain run-time logs/actuals. 

2. **Target slot owner**

   * `target_slot_owner_ref : <concrete …DescriptionRef>` (required)
     Identifies the **owner of the SlotKind set** being filled (e.g., a kit description or a suite description).
     The slot owner MUST be referenced as an **edition-addressable Description episteme** (a concrete `…DescriptionRef` such as `MechSuiteDescriptionRef`, `…KitDescriptionRef`, etc.),
     and MUST NOT be a mechanism `U.Mechanism.IntensionRef` (or any other intensional ref).
     A `MechSuiteDescription` MAY serve as a slot owner for this purpose.
     If the slot owner’s SlotKind interface is edition-sensitive (or expected to evolve), the reference MUST be edition-pinned (e.g., `target_slot_owner_ref.edition`) whenever the PlanItem is used as a reproducibility baseline.

3. **Described entity and grounding (for “whose measurements/choices?”)**

   * `described_entity_ref : <concrete RefKind>` (required)
     The referent is the *described entity* (C.2.3 role): the thing the planned baseline is **about**.
     It MUST NOT be silently conflated with a holon. (Example: a baseline can be about a width/measure while the grounding holon is a stool with that width.)
     Use a concrete RefKind of the described entity (e.g., `U.HolonRef`, `U.MeasureRef`, …). Do **not** mint a new generic `EntityRef` token inside this pattern.
   * `grounding_holon_ref? : U.HolonRef` (optional; required when the described entity is not itself a holon and a grounding holon is needed for plane/frame anchoring)
   * `reference_plane? : ReferencePlane` (optional; required when not unambiguously derivable from cited context artifacts such as CG-frame/spec pins)

4. **Explicit planning context** (no hidden context)

   * `bounded_context_ref : U.BoundedContextRef` (required)
   * `cg_frame_ref? : CGFrameRef` (recommended when the fillings feed CG legality/selection)
   * `path_slice_id? : PathSliceId` (recommended for P2W reproducibility)
   * `publication_scope_id? : PublicationScopeId` (recommended if the plan will be surfaced in publication-facing views)
     These anchors exist because context is mandatory for claims/rules in FPF-style authoring. 

5. **Explicit time selector** (no implicit recency)

   * exactly one of:

     * `Γ_time_selector : Γ_timeSelector` (ByValue), or
     * `Γ_time_rule_ref : Γ_timeRuleRef` (RefKind)
       This MUST be present whenever the plan is intended to support comparability/launch-related downstream checks. 

6. **Expected guard pins** (refs/expectations only; no gate decisions)

   * `expected_usm_guard_pins : [USM.CompareGuard | USM.LaunchGuard]` (ByValue; subset of `{USM.CompareGuard, USM.LaunchGuard}`)
     These lexemes are reserved for `USM.Guards` **pins** (gate-level surfaces), not for mechanism operator names.
     If `USM.LaunchGuard` is expected, the plan MUST include enough pins/refs to make that guard executable downstream (explicit `Γ_time_*`, pinned editions where needed, and evidence hook anchors).
     The PlanItem MUST NOT include outcomes for these guards and MUST NOT emulate gate decisions; it only records *expectations* and *required anchors*.

   * `guard_owner_gate_ref? : <concrete OperationalGateRefKind>` (refs only; required when `expected_usm_guard_pins` is non-empty unless unambiguously derivable)
     Identifies the gate that owns/aggregates `GuardFail` outcomes (via the `GuardOwnerGateSlot` discipline). This remains an expectation pin, not a decision log.
     (Use the concrete RefKind that addresses `OperationalGate(profile)` in A.21. If such a RefKind does not yet exist, treat this as a DRR+LEX item.)

7. **Planned evidence anchors (pin refs only)**

   * `planned_evidence_pin_refs? : [<concrete …PinRef>…]`
     These are anchors to *where* evidence will be placed or cited (typically SCR/RSCR pins; optionally other pin kinds explicitly allowed by the downstream guard regime),
     not the evidence itself.

8. **The planned slot-fillings ledger (authoritative rows)**

   * `planned_fillings : [SlotFillingRow+]` where:

     `SlotFillingRow := ⟨ slot_kind, planned_filler, edition_pin? ⟩`

     * `slot_kind : SlotKind`
       A SlotKind provided by the `target_slot_owner_ref` (the PlanItem MUST NOT reinterpret SlotKind meaning).
       Unless the slot owner explicitly declares the slot as multi-valued, each `slot_kind` SHALL appear **at most once** in `planned_fillings`.
     * `planned_filler : PlannedFiller` where:
       `PlannedFiller := ByValue(value) | ByRef(ref : <concrete RefKind>)`
       In `ByRef(…)`, the `ref` MUST be of a **concrete RefKind** (e.g., `…SpecRef`, `…PolicyRef`, `…MethodDescriptionRef`);
       the PlanItem MUST NOT use an untyped/generic “Ref” / “RefKind” placeholder.
       The chosen filler MUST conform to the SlotSpec discipline of the slot owner (A.6.5-style: `refMode ∈ {ByValue | <concrete RefKind>}`).
       Changes to planned fillers are described using the A.6.5 verb discipline: ByValue content change (`fill/assign/update`) vs ref retargeting (`retarget`) vs ref resolution (`resolve`), never by “renaming the slot”.
     * `edition_pin? : EditionId`
       Required only when reproducibility depends on an edition **and** the planned filler cannot carry an edition pin directly (preferred: `…DescriptionRef.edition` on the ref itself).
       If both the planned filler ref and the row provide edition pinning, they MUST agree (mismatch ⇒ nonconformant).
       ByValue rows SHOULD NOT carry edition pins unless the pinned edition is explicitly tied to a cited external artifact (e.g., a referenced rule/policy/method description).

9. **Derived indices (optional; never a second source of truth)**

   * `planned_spec_ref_index? : [<concrete …SpecRef>…]`
   * `planned_policy_ref_index? : [<concrete …PolicyRef>…]`
   * `planned_mechanism_instance_ref_index? : [<concrete …MechanismInstanceRef>…]`
     If any of these are present, they MUST be **derivable projections** of `planned_fillings`; any mismatch is nonconformant.
     (These are *categories* of refs extracted from the authoritative rows, not an invitation to introduce new generic `SpecRef/PolicyRef` token-kinds.)

10. **Expected crossing policy pins (refs only; no crossing witnesses)**

   * `expected_crossing_policy_refs? : [⟨bridge_card_ref, phi_policy_id, psi_policy_id?, phi_plane_policy_id?, reference_plane(src,tgt)⟩ …]`
     These communicate what the plan expects will be needed for crossings, without claiming that a crossing has occurred.
     `bridge_card_ref` is expected to pin a Bridge identity/channel (BridgeId + channel) and to be auditable via downstream CrossingSurface/UTS rows.
     This section states **Bridge-only** expectations; it MUST NOT introduce non-Bridge crossing mechanisms, and it MUST NOT embed CL/Φ/Ψ/Φ_plane tables (refs/policy-ids/pins only).

   * `expected_crossing_surface_refs? : [CrossingSurfaceRef…]` (optional)
     Permitted only when the plan is explicitly citing already-published CrossingSurface baselines (e.g., “fixed context constants”); otherwise, the PlanItem SHALL state only expected policy pins and allow the crossing witness to appear at the gate/work level.

11. **Notes (didactic, non-normative)**

* `planned_filling_notes?`
  Helpful narrative for reviewers; must not embed new claims that contradict the rows.

#### A.15.3:4.2.1 Canonical skeleton (Show)

The following compact pseudo-record illustrates the intended *canonical minimum*: explicit context + explicit time + a few authoritative rows.

```
SlotFillingsPlanItem := ⟨
  kind = SlotFillingsPlanItem,
  target_slot_owner_ref = CHRMechanismSuiteDescriptionRef@edition(E_suite),
  described_entity_ref = U.HolonRef(H:described-entity), // or another concrete RefKind per C.2.3
  grounding_holon_ref = U.HolonRef(H:grounding-holon)?,  // when the described entity is not itself a holon
  bounded_context_ref = U.BoundedContextRef(BC:context),
  cg_frame_ref = CGFrameRef(CG:frame),              // optional but typical for G.* legality/selection
  path_slice_id = PathSliceId(P2W:slice),           // optional but typical for reproducibility
  Γ_time_selector = point(t0),                      // no implicit “latest”
  expected_usm_guard_pins = {USM.CompareGuard, USM.LaunchGuard},
  planned_evidence_pin_refs = [RSCR.PinRef(RSCR:evidence-anchor)],
  planned_fillings = [
    ⟨ slot_kind = CNSpecSlot, planned_filler = ByRef(CNSpecRef(CN:…@edition(E_cn))) ⟩,
    ⟨ slot_kind = CGSpecSlot, planned_filler = ByRef(CGSpecRef(CG:…@edition(E_cg))) ⟩,
    ⟨ slot_kind = ScoringMethodDescriptionSlot,
      planned_filler = ByRef(ScoringMethodDescriptionRef(M:…@edition(E_m))) ⟩
  ]
⟩
```

#### A.15.3:4.3 Relation to Work enactment (planned baseline vs actuals)

* A `SlotFillingsPlanItem` is **not** a witness of `FinalizeLaunchValues`.
  Launch values (actuals) occur only in Work enactment, and their witness belongs in Work/audit surfaces, not in this PlanItem. 

* Deviation at execution time is allowed, but it must be recorded as **variance in Work**, and the plan must not be rewritten to match the execution. 
  When a Work enactment claims to follow a planned baseline, the Work MUST cite the `SlotFillingsPlanItem` in its Audit as the planned baseline reference, and MUST record any variance against it (rather than “backfilling” the plan).
  The baseline citation SHOULD be edition-addressable (i.e., the Work cites a stable PlanItem edition), so that later PlanItem revisions cannot erase what was actually planned.
  If the baseline needs to change (including any edition-pinned ref changes), author a **new PlanItem edition** (or a new PlanItem) and treat the difference as a planning change—not as a retroactive edit of the previously cited baseline.

#### A.15.3:4.4 Relation to suites/kits

* Any suite/kit that requires a “planned baseline” may require and cite a reference to a `SlotFillingsPlanItem` via its contract pins; `MechSuiteDescription` explicitly provides a place for such a requirement. 

#### A.15.3:4.5 - Variants

1. **Suite-specialized PlanItem (Refinement)**
   A suite may define `XSuiteSlotFillingsPlanItem ⊑ SlotFillingsPlanItem` with:

   * fixed `target_slot_owner_ref = XSuiteDescriptionRef`,
   * additional required rows (e.g., mandatory pinned `CGSpecRef`, `CNSpecRef`, suite-required mechanism instance refs),
   * additional required expected pins (guards, crossing policies).

2. **Minimal vs crossing-aware variants**

   * *Minimal:* includes only context + planned rows + time selector.
   * *Crossing-aware:* adds `expected_crossing_policy_ref[]` and explicit `reference_plane`.

3. **Evidence-gated variant**
   For workflows where `USM.LaunchGuard` is expected, require `planned_evidence_pin_refs[]` and explicitly pin the relevant edition set needed for the later guard.

#### A.15.3:4.6 - Non-goals

* Not a mechanism; it performs no operations and publishes no operator signatures.
* Not a `…Spec`; it is not an acceptance harness and does not replace CN-Spec or CG-Spec.
* Not a hiding place for acceptance thresholds: any threshold-like semantics MUST live in explicit Acceptance/Policy artifacts (and be referenced/pinned), not smuggled in as anonymous ByValue numbers.
* Not a gate log: it MUST NOT contain `GateDecision` / `DecisionLog`, and MUST NOT claim that a crossing occurred.
* Not a run-time witness: it MUST NOT contain `FinalizeLaunchValues` actuals.
* Not a publication surface: it may be projected to views, but it is not “the card” itself. Any view MUST be an explicit projection (e.g., `TechCard(PlanItemRef)`), and unchecked presentation drift is a known failure mode. 

#### A.15.3:4.7 - When to use

Use `SlotFillingsPlanItem` whenever:

* a workflow will be enacted through P2W and you need a **planned baseline** for what fills a suite/kit’s slots;
* you must pin editions/time policies explicitly (e.g., legality gates, comparator sets, transport registries);
* you are refactoring/authoring Part G patterns and want a uniform place to record selected refs/policies/mechanism instances;
* you expect a LaunchGate or any guard-based eligibility check to be meaningful and traceable.

#### A.15.3:4.8 - Implementation notes

**Informative authoring guidance (conceptual):**

1. Choose one `target_slot_owner_ref` per PlanItem. If multiple slot owners are involved, author multiple `SlotFillingsPlanItem`s (one per owner) to keep slot meaning unambiguous.
2. Fill rows by SlotKind, not by positional arguments or “index numbers”.
3. If any downstream reasoning may hinge on “now vs then”, supply `Γ_time_selector` or `Γ_time_rule_ref` explicitly.
4. Prefer edition-pinned references when the downstream step is intended to be reproducible across review cycles.
5. Use derived indices only as projections for reader convenience; never maintain them independently.
6. If a PlanItem has been cited as a baseline by a Work, do not “edit it in place” to match reality. Create a new PlanItem edition and let Work record variance and/or the required crossing witnesses.

### A.15.3:5 - Archetypal Grounding (Tell–Show–Show; System / Episteme)

#### A.15.3:5.1 - Archetype 1: CHR suite planned baseline for lawful characterization

**Tell.** A team plans a characterization workflow over a CG-frame that uses a CHR mechanism suite. The suite requires an explicit planned baseline reference.

**Show (failure without `SlotFillingsPlanItem`).** The “plan” is implicit: it says “use the latest CG-Spec and the current best comparator; compute scores and launch” without an explicit `Γ_time`, without edition pins, and without a stable mapping from SlotKinds to chosen fillers. Review later cannot distinguish: (i) what was planned, (ii) what was executed, and (iii) what changed via a crossing / edition-key shift.

**Show (repair with `SlotFillingsPlanItem`).** A conformant `SlotFillingsPlanItem`:
* targets `CHRMechanismSuiteDescriptionRef` as the slot owner (and pins its edition if used as a reproducibility baseline),
* pins `CNSpecRef` and `CGSpecRef` (editions pinned where reproducibility requires),
* pins a `ScoringMethodDescriptionRef.edition` (e.g., a monotone scoring family) and/or a set-valued method family (e.g., conformal-style set predictions),
* declares `Γ_time_selector = point(t0)` (no implicit “latest”),
* declares `expected_usm_guard_pins = {USM.CompareGuard, USM.LaunchGuard}`,
* includes evidence pin refs that will later be populated/used in Work enactment.

The resulting Work enactment cites this PlanItem as the planned baseline; any substitution (e.g., retargeting a method description ref) appears as Work variance (and, when relevant, as a crossing witness), not as a retroactive plan rewrite.

#### A.15.3:5.2 - Archetype 2: Archive/QD selection with edition-sensitive descriptors

**Tell.** A workflow plans to return an **archive** (quality-diversity style) rather than a single winner. The selection pipeline depends on descriptor maps and distance definitions that are edition-sensitive.

**Show (failure without `SlotFillingsPlanItem`).** Descriptor-map and distance-definition drift is discovered only after the fact: an “archive” is produced, but reviewers cannot reconstruct which descriptor edition and distance definition were assumed at planning time, and the published view/card becomes the de facto (and mutable) “source of truth”.

**Show (repair with `SlotFillingsPlanItem`).** A conformant `SlotFillingsPlanItem`:
* targets an archive-selection kit/suite as `target_slot_owner_ref`,
* pins `DescriptorMapDescriptionRef.edition` and `DistanceDefDescriptionRef.edition` (or their kit equivalents),
* states `expected_usm_guard_pins = {USM.CompareGuard}` (if no LaunchGate is expected yet),
* records expected crossing policy pins if descriptors are reused cross-context.

This prevents “silent” descriptor drift across iterations and makes Part G’s archive-related extensions composable rather than embedded in selector prose.

### A.15.3:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal**.

| Lens | Bias / limitation introduced by the pattern | Mitigation |
| --- | --- | --- |
| Gov | Baseline immutability and variance recording can be misread as bureaucracy rather than epistemic hygiene. | Keep the baseline minimal; use suite-specialized refinements only when a suite contract truly requires them. |
| Arch | Enforces a clean P2W seam and discourages “configuration hidden in mechanisms”. This can expose weakly-specified slot owners earlier. | Treat that friction as an architectural signal; refine the slot-owner interface rather than hiding choices in prose. |
| Onto/Epist | Strongly biases toward explicit context/time/edition pinning; exploratory reasoning may feel constrained. | Use minimal variants (context + rows + time selector) for exploration; graduate to pinned editions only when reproducibility is required. |
| Prag | Increases upfront authoring cost (explicit context, time, edition pins). | Use derived indices as projections for reader navigation; avoid duplicating content on views/cards. |
| Did | Biases against “one true card” habits by treating views as projections; may clash with existing documentation culture. | Provide a TechCard/PlainView projection explicitly, but keep the PlanItem as the semantic authority. |

### A.15.3:7 - Conformance Checklist

| ID          | Check (normative)                                                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CC-A15.3-01 | The object is a `U.WorkPlan.PlanItem` with `kind = SlotFillingsPlanItem`, and obeys WorkPlan guardrails (no logs/actuals, no step logic).                                                                           |
| CC-A15.3-02 | `target_slot_owner_ref` is present and identifies a real SlotKind owner (kit/suite); SlotKinds in rows are interpreted only within that owner.                                                                      |
| CC-A15.3-02a | If the PlanItem is used as a reproducibility baseline and the slot owner is edition-addressable, `target_slot_owner_ref` is edition-pinned (e.g., `…DescriptionRef.edition`).                                      |
| CC-A15.3-02b | `target_slot_owner_ref` is a **Description-level** ref (e.g., `MechSuiteDescriptionRef`, `…KitDescriptionRef`) and MUST NOT be an intensional ref (e.g., `U.Mechanism.IntensionRef`). |
| CC‑A15.3‑02c (single slot owner) | A `SlotFillingsPlanItem` targets exactly one slot owner via `target_slot_owner_ref`. If multiple slot owners are involved, they MUST be represented by multiple PlanItems (one per owner). |
| CC-A15.3-03 | `described_entity_ref` is present. If `grounding_holon_ref` and/or `reference_plane` are omitted, they must be unambiguously derivable from cited context artifacts (e.g., the pinned CG-frame/spec context).      |
| CC-A15.3-03a | `described_entity_ref` is a concrete RefKind (no generic “EntityRef” placeholder is introduced by this pattern). |
| CC-A15.3-04 | Context anchors are explicit at least to `bounded_context_ref`; if the fillings support legality/selection, then CG-frame/path-slice anchors are present.                                                           |
| CC-A15.3-05 | Time is explicit: the item includes `Γ_time_selector` or `Γ_time_rule_ref`; “latest/current” without explicit `Γ_time` is nonconformant.                                                                             |
| CC-A15.3-05a | Exactly one of `Γ_time_selector` and `Γ_time_rule_ref` is present (XOR); both-present or both-absent is nonconformant. |
| CC-A15.3-06 | `planned_fillings` is the authoritative source: each row is `⟨slot_kind, planned_filler, edition_pin?⟩`; each planned filler is explicit `ByValue` vs `ByRef(ref-of-concrete-RefKind)` and conforms to the slot owner’s SlotSpec discipline (no silent slot-meaning changes). |
| CC-A15.3-06a | Unless the slot owner declares a slot as multi-valued, `planned_fillings` contains **no duplicate** `slot_kind` rows (duplicate keys ⇒ nonconformant). |
| CC-A15.3-06b | If both a row and its `ByRef(…)` filler carry edition pinning, they MUST agree; mismatch ⇒ nonconformant. |
| CC-A15.3-07 | Any present “indices” (`planned_*_ref_index`) are derivable projections of `planned_fillings` and are not independently authored; mismatch ⇒ nonconformant.                                                         |
| CC-A15.3-08 | The PlanItem contains no `GateDecision` / `DecisionLog`, and makes no claim that a crossing occurred; only expected policy pins may be stated.                                                                      |
| CC-A15.3-09 | The PlanItem contains no `FinalizeLaunchValues` witness and no launch-time actuals; launch values are finalized only in Work enactment.                                                                             |
| CC-A15.3-10 | If `expected_usm_guard_pins` includes `USM.LaunchGuard`, the PlanItem contains sufficient pins/refs (explicit `Γ_time_*` + pinned editions + evidence pin anchors + `guard_owner_gate_ref` or an unambiguous derivation) to make downstream guard execution possible.     |
| CC-A15.3-10a | In this pattern, “evidence anchors” are expressed as pin refs (e.g., SCR/RSCR pins). Introducing a new generic `EvidenceHookRef` token requires an explicit DRR+LEX step; absent that, use concrete pin refs. |
| CC-A15.3-11 | The PlanItem does not claim to set or mutate the edition vector (`editions{…}` / edition_key). It may pin editions and may state *expected* edition-sensitive crossings, but edition changes themselves are crossings (gate/work-level witnesses). |
| CC-A15.3-12 | When used as a baseline for enactment, execution-time deviations are recorded as Work variance and the baseline PlanItem is not rewritten (“no backfill”); the Work Audit cites the PlanItem (preferably by edition-addressable ref) as the planned baseline reference.  |
| CC-A15.3-12a | Any change to edition-pinned refs that would alter the effective edition-key for legality/selection MUST NOT be retroactively applied to the already-cited baseline PlanItem. Treat it as (i) a new PlanItem edition for future enactments and (ii) variance and/or required crossing witnesses for the enactment that deviated. |
| CC-A15.3-13 | If `expected_crossing_policy_refs` is present, it contains **refs/policy-ids only** (BridgeCardRef + policy-id refs + plane ids); it MUST NOT embed CL/Φ/Ψ/Φ_plane tables or introduce non-Bridge transport edges. |
| CC‑A15.3‑13a (crossing surfaces are not witnesses) | `expected_crossing_surface_refs` (if present) is used only to cite already‑published, context‑constant CrossingSurface baselines; it MUST NOT be used to claim that a crossing occurred for this enactment, nor to substitute for gate/work‑level crossing witnesses. |
| CC‑A15.3‑14 (view projection discipline) | Any `U.View` projection of a `SlotFillingsPlanItem` (e.g., `TechCard(PlanItemRef)`, `PlainView(PlanItemRef)`) MUST be an explicit projection that introduces no additional claims, defaults, or rows beyond the PlanItem; any additional semantics on the view is nonconformant. |


### A.15.3:8 - Common Anti‑Patterns and How to Avoid Them

#### A.15.3:8.1 - Plan-as-execution

A plan document says: “Use the latest CG-Spec and the current best comparator; compute scores and launch.”
This is nonconformant because it omits explicit `Γ_time`, omits edition pins, collapses planning into execution, and provides no stable baseline for variance/audit.

#### A.15.3:8.2 - Anti-example: Edition-key change disguised as a plan edit (backfill)

A team executes Work while actually using `CGSpecRef@edition(E2)` (and/or `ComparatorSetRef@edition(E2)`), but the previously approved baseline PlanItem had pinned `@edition(E1)`.
Later, instead of recording variance and the required GateCrossing witness for the **edition-key change**, someone edits the baseline PlanItem “in place” to replace `E1 → E2`,
and then claims “no variance; we followed the plan”.

This is nonconformant because it:
* collapses planning into execution (retroactive baseline editing),
* hides an edition-key change that is crossing-relevant,
* destroys reproducibility and breaks Work/Audit traceability.

Correct handling: keep the old baseline intact; record variance in Work and, where applicable, require the gate/work-level crossing witness (UTS/CrossingSurface + policy-id pins),
or produce a new PlanItem edition as the new planned baseline for subsequent enactments.

### A.15.3:9 - Consequences

| Benefit | Trade‑off / Cost | Notes / Mitigation |
| --- | --- | --- |
| Improved modularity | Requires an explicit baseline artifact | Keep baselines minimal; specialise only when a suite truly needs it. |
| Audit clarity | More up‑front authoring work | The burden is intentional: it buys attributable variance and prevents “mystery defaults”. |
| Edition honesty | Forces authors to think about editions and time | Use editioned refs and time selectors by ref; keep actual `Γ_time` in Work evidence. |
| Controlled specialisation | Multiple PlanItem kinds may exist (core + suite‑specialised) | Use DRR to document why specialisation is warranted; keep the universal core stable. |

### A.15.3:10 - Rationale

This pattern exists to give WorkPlanning an explicit, citeable place to commit to “which artifacts will fill which slots” without collapsing into run-time state.

Keeping the baseline bound to exactly one slot owner makes SlotKind semantics checkable and prevents accidental cross-owner slot drift.

Treating indices as derived projections preserves a single source of truth (the rows) while still enabling human-friendly navigation or tooling acceleration.

Finally, by disallowing run-time witnesses (launch values, observed values, concrete `Γ_time`) the pattern enforces the plan/run split and keeps audit variance attributable to an explicit baseline rather than to shifting defaults.

### A.15.3:11 - SoTA‑Echoing (informative)

This pattern aligns with post‑2015 practice in multiple traditions while deliberately staying notationally/tool independent.

* **ISO/IEC/IEEE 12207:2017** — **Adopt** the separation between planning artifacts and execution artifacts plus baseline/change-control concepts; **Adapt** them into a lightweight, citeable PlanItem kind; **Reject** prescribing any specific process tooling as normative inside FPF.
* **ISO 26262:2018** — **Adopt** the emphasis on traceability, change impact visibility, and preventing retroactive “paper compliance”; **Adapt** it into baseline immutability + variance reporting; **Reject** treating safety certification structure as a required envelope for all contexts.
* **NIST SP 800-128 Rev.1 (2020)** — **Adopt** baseline management and deviation recording as an audit primitive; **Adapt** by expressing baselines as epistemic, context-bound references rather than machine configuration states; **Reject** security-tooling prescriptions as a dependency of the conceptual model.
* **Forsgren, Humble, Kim (2018), _Accelerate_** — **Adopt** the empirical lesson that explicit change tracking and small, attributable deltas improve reliability; **Adapt** by making the baseline the anchor for fulfilment/variance; **Reject** any “one true pipeline” or vendor-specific operational recipe.
* **Morris (2021), _Infrastructure as Code_ (2nd ed.)** — **Adopt** the desired-state vs observed-state distinction and the discipline of explicit declarations; **Adapt** by keeping declarations as plan-level epistemes rather than deployment manifests; **Reject** binding the model to any specific IaC syntax or platform.

### A.15.3:12 - Relations

* **Builds on / governed by:**
  * **A.15.2 `U.WorkPlan`** — container + PlanItem discipline; baseline citeability.
  * **A.6.5 slot discipline** — SlotKind/RefKind hygiene and binding-time separation.
  * **E.10.D1 Context discipline** — explicit context/edition; no implicit “latest”.
  * **E.18 / TGA** — keeps `FinalizeLaunchValues` strictly in WorkEnactment; pin/guard discipline.
* **E.17 / Publication discipline** — views are projections; no new semantics on cards.
* **Interacts with / complements:**
  * **A.6.7 `MechSuiteDescription`** — suites may require the presence of a planned baseline ref/pin without embedding planned fillers or launch values.
  * **A.15.1 Work / WorkEnactment discipline** — fulfilment and variance are recorded downstream against this baseline.
  * **C3.2-S-02 Time discipline** — time selection policy may be pinned by ref; run-time `Γ_time` stays in Work evidence.

### A.15.3:End

## A.17 - Canonical “Characteristic” (A.CHR‑NORM)

### A.17:1 - Context

To have reproducibility and explainability there is a need to **measure** various aspects of systems or knowledge artifacts. A dedicated measurement backbone (see **C.MM‑CHR**, Measurement & Metrics Characterization) already exists, prescribing the **CSLC discipline** – i.e. define a **Characteristic**, choose a **Scale** (with a **Unit** if applicable), record a **Level/Value**, and thus obtain a **Coordinate** on that scale, optionally mapping to a **Score** via a **ScoringMethod (USCM)**. However, historically multiple near-synonyms (“axis”, “dimension”, “property”, “feature”, "metric") have been used interchangeably for “what is being measured,” and often the _aspect itself_ gets conflated with _how it is expressed_ (units, ranges, labels). This pattern enters the FPF **Kernel lexicon** to **canonize a single term** for the measured aspect and enforce a clear separation between **what** is measured and **how** it is measured.

### A.17:2 - Problem

When measurement concepts are not kept rigorously distinct, several issues arise:

-   **Polysemy at the anchor.** Teams say “dimension” or “feature” but mean slightly different things, so the very trait being measured is ambiguous.
    
-   **Arity mistakes.** A relational quality (e.g. similarity between two items) might be treated as if it were an intrinsic property of one item, or vice versa, leading to logical errors.
    
-   **Expression conflation.** The aspect being measured is often mixed up with its expression – for example, using “scale” or “axis” to mean both the quality _and_ its unit or range. This leads to **unsafe arithmetic** (averaging ordinal ranks, comparing raw numbers from incompatible scales, etc.) because values get interpreted out of context.
    

In summary, projects lacking a canonical terminology for metrics risk miscommunication and pseudo-quantitative operations. Measurements of physical quantities, architectural attributes, or performance scores end up on **incommensurate rails** due to inconsistent naming and handling.

### A.17:3 - Forces

-   **F1 – Single anchor of meaning.** Any numeric value is meaningless unless one can ask “value of _what_?”. The measurement’s meaning must be anchored in a single clearly named aspect.
    
-   **F2 – Arity clarity.** Some characteristics apply to a single entity (e.g. its mass or length), while others inherently relate multiple entities (e.g. distance between two points, coupling between modules, agreement between judges). If arity isn’t explicit, claims and calculations become corrupted.
    
-   **F3 – Scale integrity.** Different kinds of scales permit different operations – e.g. you can average temperatures (ratio scale) but not ranks or grades (ordinal scale) without losing meaning. If one mixes values without regard to scale type or units, the result is nonsense (**pseudo-arithmetic**).
    
-   **F4 – Composition discipline.** In complex evaluations, multiple measurements may need to be combined. Without a disciplined approach, people might perform ad-hoc math on apples and oranges (adding scores from unrelated characteristics, etc.). A proper pattern must require any combination to go through a defined monotonic **ScoringMethod** (e.g. a weighted formula) instead of arbitrary aggregation.
    
-   **F5 – Transdisciplinarity.** The measurement framework should work for **any domain**. The same conceptual scaffold must serve physical science (e.g. lab temperature readings), software engineering (e.g. module cohesion ratings), and even subjective assessments (e.g. figure-skating scores) without bias. One vocabulary, many CG‑frames.
    
-   **F6 – Open-endedness.** As systems evolve, their performance or quality metrics also evolve. Rigid life-cycle stage labels (“Phase 1, Phase 2…”) don’t capture iterative improvement. The pattern should favor an **open-ended state-space** view (revisiting states via checklists, as in an RSG – **RoleStateGraph** with re-entry) over any fixed lifecycle with “terminal” stages.
    
### A.17:4 - Solution

**Establish “Characteristic” as the one canonical construct for “what is measured.”** In every FPF context, the _aspect or trait_ being measured MUST be referred to as a **Characteristic**. This term replaces “axis” or “dimension” in normative usage (those may appear _only_ as explanatory aliases in Plain register). By fixing a single name and schema, we cleanly separate a **Characteristic** from its **Scale** (and **Unit**), and from any observed **Value/Level** on that scale. The solution also differentiates single-entity vs multi-entity cases and binds all measurements to the standard CSLC sequence.

To enforce this solution, the following rules apply:

-   **A17-R1 (Canonical term).** In all normative models and specifications, the measured aspect **SHALL** be referred to as a **Characteristic**. (Legacy terms “Axis” or “Dimension” are retired from technical vocabulary – see Part J Lexicon Update.)
    
-   **A17-R2 (Entity vs. relation subtype).** Each Characteristic **MUST** declare its intended _arity_. An **Entity-Characteristic** applies to exactly one bearer (e.g. _Temperature_ of a reactor, _Evolvability_ of a software module), whereas a **Relation-Characteristic** applies to an ordered tuple of two or more bearers (e.g. _Distance_ between two sensors, _Coupling_ between modules, _Agreement_ among reviewers). The arity is part of the definition and **must be explicit** wherever it’s not obvious from naming.
    
-   **A17-R3 (Characteristic space).** Any set of defined Characteristics spans a multi-dimensional **CharacteristicSpace**. Movement or evolution is then described as trajectories through this space (with states revisited or refined over time), rather than as a linear lifecycle through preset phases. This ensures measurements feed into open-ended state modeling rather than locking into “end states.”
    
-   **A17-R4 (Lexical guardrails).** Normative text **SHALL** use only the canonical measurement terms: **Characteristic, Scale, Level, Value, Coordinate, Score, Normalization, Unit**. Synonyms like _axis_, _dimension_, _metric_, _grade_, _property_, etc., are **forbidden in formal usage**. (They may appear in narrative explanations or user-facing documentation _only if_ clearly defined as aliases for the canonical terms.) Authors **MUST** not use deprecated terms in identifiers or formal statements, and any didactic alias should be introduced with an explicit mapping to the official term. These lexical rules uphold clarity and are further detailed in **E.10 LEX‑BUNDLE**. 

- **A17-R5 (Symbol policy).** **Γ** reserved for holonic composition; **𝒢 : Coordinate→Score** for metric‑level ScoringMethod; **MUST NOT** be conflated; documents **SHALL NOT** reuse Γ for ScoringMethod. **If an ordered Scale is declared, polarity SHALL be fixed; 𝒢 MUST be monotone** w.r.t. that polarity.

- **A17-R6 (Declared polarity).** Every ordered Scale **SHALL** declare one of: **↑‑better**, **↓‑better**, or **non‑applicable** (for purely nominal scales). For interval/ratio scales, polarity fixes the intended order of comparison.

- **A17-R7 (Monotonicity against polarity).** If a template declares an **ordering polarity** on its Scale (↑ better / ↓ better), then **𝒢 MUST be monotone** w\.r.t. that polarity: higher‑is‑better (resp. lower‑is‑better) in coordinates **implies** ≥ (resp. ≤) in scores.

- **A17-R8 (Arity declaration).** Authors **SHALL** mark a Characteristic as **`U.EntityCharacteristic`** (applies to exactly one bearer) or **`U.RelationCharacteristic`** (applies to a relation of cardinality ≥ 2). Examples: *Cohesion* → entity‑level; *Coupling* → relation‑level.

- **A17-R9 (Relational scale anchors).** For relation‑level cases, the Scale’s admissible values **SHALL** be defined over the **tuple** domain (e.g., distances, similarities, inter‑role latencies). Ambiguity that re‑reads a relational Characteristic as unary is **forbidden**.

- **A17-R10 (Intension vs Description).** The **Characteristic** remains the **intensional object**; any rubric, catalogue of levels, or examples are **descriptions**. Keep the intensional Characteristic distinct from its descriptive episteme (cf. `U.Episteme` roles: Object–Concept–Symbol).

#### A.17:4.1 - CharacteristicSpace & Change Reasoning *(Normative/Clarifying)*

**R17 — CharacteristicSpace declaration.** When an agent reasons about **change**, it **SHALL** name the **CharacteristicSpace** (the set of Characteristics, with Scales, units, and topology assumptions) in which motion is considered.

**R18 — RSG framing, not lifecycle.** Change narratives **SHALL** be framed as movement on a **reachable‑states graph (RSG)** with **checklists** that certify state acquisition; **“lifecycle”** staging is **deprecated**. *(A.17 conforms to the open‑ended evolution stance of the Kernel.)*

**I7 — Vector interpretation.** A **U.Coordinate** vector may collect multiple coordinates for multi‑Characteristic reasoning; composition into a single Score, if desired, is an **explicit new 𝒢** on that vector.

### A.17:5 - Archetypal Grounding (System & Episteme Examples)

**In a physical system (`U.System`):** Consider a **Distance** Characteristic defined for a pair of physical objects. For example, two machines in a factory have a Distance of 3.5 meters between them. Here _Distance_ is a Relation-Characteristic (applies to the pair), with an associated Scale (e.g. a ratio scale in meters), and the measured 3.5 m is a **Coordinate** on that scale. If we instead look at an **Engine Temperature** Characteristic (unary), a particular engine might have a Temperature of 350 K at some moment – _Temperature_ (the Characteristic) is clearly separated from how it’s measured (Scale in Kelvin) and the reading (350, a Coordinate on that scale).

**In an epistemic context (`U.Episteme`):** Consider a **Formality** Characteristic to rate a documentation artifact’s rigor. We might define an ordinal Scale with named Levels such as _Informal_, _Semi-formal_, _Formal_. A given specification document can then be said to have _High Formality_ – meaning it occupies the “Formal” **Level** on the Formality Scale. Here _Formality_ (Characteristic) captures _what_ we measure about the document, while the tiered Scale (with qualitative levels) expresses _how_ we categorize it. Because we use an ordinal scale, we can rank documents by Formality, but we would not average “Semi-formal” and “Formal” (avoiding meaningless arithmetic on an ordinal metric). In another knowledge context example, one could define a Characteristic **Reliability** for a knowledge source with a percentage Scale from 0 to 100%. An article’s reliability might be 85% – which is only interpretable by knowing it refers to “Reliability” on a 0–100% Scale (i.e. a specific Coordinate on that Characteristic’s scale).

### A.17:6 - Bias-Annotation

This pattern is deliberately **domain-neutral** and introduces no bias toward any particular discipline or measurement type. By enforcing a uniform lexicon, A.17 actually mitigates bias: it prevents **disciplinary jargon** from creeping into core definitions (ensuring, for instance, that a software metric isn’t given a vague custom term when it’s fundamentally a Characteristic). The **Didactic lens** is strongly served: using one precise name per concept improves clarity for all audiences. There is a slight initial cost in re-labeling legacy terms (e.g. renaming “dimensions” to Characteristics), but this is offset by the long-term **Cognitive Elegance (P‑1)** – the framework becomes easier to learn and less prone to misinterpretation. No single domain’s terminology dominates, and the pattern explicitly supports both quantitative (physics-like) and qualitative (judgment-based) measurements, reflecting **Pragmatic neutrality**. The requirement of open-ended state-space thinking aligns with **P‑10 (Open-Ended Evolution)**, ensuring we don’t bake in lifecycle biases that assume development must terminate at a final stage. In summary, A.17 imposes a disciplined vocabulary that is broad enough for all fields and free of hidden assumptions, thereby avoiding subtle ontological or cultural biases in the measurement model.

### A.17:7 - Conformance Checklist

When authoring or reviewing FPF-compliant metrics, use the following checklist to ensure **Characteristic normalization** is applied:

1.  **Declared Characteristic:** Have you explicitly named a **Characteristic** for each aspect being measured, instead of using generic terms? (e.g. use _“Reliability”_ as a Characteristic name rather than saying “this dimension”).
    
2.  **Arity Explicit:** Is it clear whether the Characteristic is unary or relational? If a metric involves a relationship, are the participating entities (pair, tuple, etc.) identified in its definition?
    
3.  **Separate Scale/Unit:** For each Characteristic, have you defined the **Scale** (and **Unit**, if applicable) separately, rather than embedding units or ordinal terms in the name of the Characteristic? (e.g. _“Length (m)”_ should be captured as Characteristic = _Length_, Unit = _meter_).
    
4.  **Scale-appropriate operations:** Are you only performing comparisons or calculations that make sense for the declared scale type? (No averaging of ranks, no mixing of units – ensure **ordinal** Characteristics aren’t treated like numbers, and **interval/ratio** values respect zero and units.)
    
5.  **No implicit aggregation:** If multiple measurement readings are combined, is there a defined **ScoringMethod** (with monotonic logic) that produces a **Score**? Avoid any ad-hoc “overall score” that simply adds or averages raw values from different Characteristics.
    
6.  **Canonical terminology in use:** Are you using the terms _Characteristic_, _Scale_, _Level/Value_, _Coordinate_, _Score_, _ScoringMethod_, _Unit_ in all formal descriptions? Confirm that no deprecated synonyms (axis, dimension, etc.) appear in technical content or identifiers (they can appear in Plain explanations only with proper reference to the canonical term).
    
7.  **Open-ended progression:** (If applicable) When modeling progress or change using metrics, have you considered using a state-space of Characteristics rather than a fixed sequence of phases? This check is to encourage leveraging the open-ended nature of CharacteristicSpaces, especially in evolutionary or iterative processes.
    
_(Failure to satisfy the above indicates a violation of this pattern’s intent. The **LEX-BUNDLE** rules in E.10 provide automated checks for term usage, and MM-CHR templates enforce explicit Characteristic/Scale definitions.)_

### A.17:8 - Consequences

By instituting **Characteristic** as the single term and enforcing the CSLC structure, this pattern yields several positive outcomes:

-   **Unambiguous metrics:** Every measurement has a single, well-defined anchor of meaning – the Characteristic – eliminating guesswork about “what is this number about?”.
    
-   **Separation of concerns:** We cleanly separate _what_ is measured from _how_ it’s represented. The Characteristic names the quality of interest, while the Scale/Unit defines the expression. A raw value now **means nothing by itself** – it must be read as “X units on the Y scale of Z Characteristic,” which greatly reduces misinterpretation.
    
-   **Unary vs. relational clarity:** The explicit distinction between Entity-Characteristic and Relation-Characteristic ensures that relational properties (like “distance between A and B” or “consistency among experts”) aren’t mistakenly treated as inherent properties of a single object. This guards against logical errors and data modeling mistakes.
    
-   **Cross-domain comparability:** All measurements, regardless of domain, follow the same **CSLC** rails. This means a temperature in Kelvin and a reliability score in percent can each be traced through Characteristic → Scale → Coordinate. They can’t be directly compared unless designed to be, which is _good_: any composite scoring must be done via an explicit **SCP** mapping to a common **Score** scale. The pattern thus enables interoperability (through well-defined Score bridges) while preventing illegitimate comparisons.
    
-   **Consistent evolution framing:** By retiring the idea of a bespoke “lifecycle” for every process and instead viewing changes as movement in a CharacteristicSpace, the pattern aligns metric thinking with state-based reasoning (e.g. as used in dynamic models). There is no artificial “final state” for improvement – a system can always evolve to a new coordinate without violating a lifecycle Standard. This open-ended view encourages continuous improvement and refinement, echoing FPF’s emphasis on evolutionary development.
    

There are few downsides. One consequence is that modelers must learn the canonical terms and possibly refactor existing documentation (a short-term effort). Also, enforcing scale integrity means quick-and-dirty aggregate scores are not allowed unless justified via a SCP – this introduces a healthy “pause” to ensure composite metrics are well-founded. Overall, the benefits in clarity and correctness far outweigh the overhead. Teams gain a _lingua franca_ for metrics, and the risk of metric abuse (mixing apples and oranges) is significantly reduced.

### A.17:9 - Rationale

The Canonical Characteristic pattern is a direct response to recurring measurement pitfalls. By insisting on “one precise name per concept”, it upholds **Strict Distinction (A.7)**, ensuring that the framework never treats two different ideas as one. For instance, earlier practice might label both a requirement category and its score as “dimension,” causing confusion; with A.17, the _aspect_ is a Characteristic and its _score_ is separate, so each idea has its place. This clarity is pedagogically vital (**P‑2 Didactic Primacy**): readers and contributors immediately know what a term means and how to interpret any value associated with it.

The solution also draws on fundamentals of measurement theory (Stevens’ levels of measurement) to prevent misuse. By encoding scale types and unit handling into our patterns, we avoid the “pseudo-quantitative” fallacies – no more averaging things like _risk levels_ or adding up _grades_ as if they were true numbers. In effect, A.17 puts a safeguard around **P‑1 Cognitive Elegance and P‑7 Ontological Parsimony**: we use a minimal, universal set of measurement constructs, and we avoid bloating the conceptual space with domain-specific or redundant terms. One canonical set of terms also makes the framework more teachable and **composable across contexts**, since patterns and projects aren’t inventing new synonyms that others must decipher.

Importantly, distinguishing Entity vs Relation Characteristics future-proofs the reasoning model. It enforces a modeling rigor seen in domains like physics (where properties vs. relations are carefully distinguished) and brings it to architecture and knowledge domains. This rigor supports advanced reasoning in FPF – for example, **A.3.3 (Dynamics)** can treat system state variables as a well-defined set of Characteristics, and assurance patterns can trace **evidence metrics** unambiguously to the exact aspect measured. It also means any attempt to compare or combine metrics has to be explicit (via ScoringMethods), which inherently improves **transparency and auditability** (a key FPF goal).

Finally, retiring the “lifecycle” vocabulary in favor of state-space trajectories aligns with FPF’s **open-ended evolution** principle. It acknowledges that improvement is not a predefined path but a navigable space. This shift in mindset (from lifecycle stages to checklisted state transitions) removes an implicit bias that systems _ought_ to reach a “final” maturity stage – instead, it keeps the door open for perpetual refinement, which is philosophically aligned with continuous learning and adaptation.

In summary, A.17 is the linchpin that turns a loose collection of measurement practices into a **coherent, principle-driven system**. It rationalizes the language, thereby rationalizing thought: by speaking in one clear voice about measurements, FPF ensures that every number in the system can be trusted to answer “value of what, on what scale, relative to what context.” This rationale is reflected in improved model integrity and cross-domain trust in the meaning of metrics.

### A.17:10 - Relations

-   **Builds on / Elaborates:** _FPF Core Measurement Schema_ (as outlined in C.16). A.17 lifts the metric template concepts from C.16 into a kernel-level rule. It also reinforces **A.7 Strict Distinction**, by giving each measurement concept a unique name and forbidding overloaded terms.
    
-   **Constrains:** All other patterns that define or use metrics. For example, **A.3.3 `U.Dynamics`** (system dynamics) must name its state variables as Characteristics with proper scales (it cannot refer to them loosely as “KPIs” without context). Similarly, any **service-level targets / SLO clauses (A.2.3 `U.PromiseContent.acceptanceSpec`)** or **assurance calculations (B.3, D.3 patterns)** that involve measurements are governed by this canonical terminology (no unwarranted synonyms or unit confusion per ISO/IEC 80000, ISO/IEC 25024, QUDT, SOSA/SSN best practices). The pattern’s lexical rules are part of the **LEX-BUNDLE** (E.10) – any FPF-conformant context must adhere to these naming conventions.
    
-   **Coordinates with:** **A.18 (CSLC-KERNEL)**, which defines the minimal **Characteristic/Scale/Level/Coordinate** Standard in detail. A.17 provides the vocabulary and basic distinctions (what is a Characteristic, and its arity), while A.18 applies this to ensure each measurement template is well-formed. Also coordinates with **C.KD-CAL** and **C.CHR-CAL** (Knowledge Dynamics Calculus, Characterization Calculus) – those patterns use the Characteristic/Scale constructs to build domain-specific metrics (e.g. knowledge quality scores) and rely on A.17’s canon for consistency.
    
-   **Anticipates:** **E.10 Lexical Discipline** rules – A.17’s enforcement of a single term and controlled aliases is a concrete instance of the lexical uniformity mandated in E.10. It also paves the way for **F.7 Concept-Set Bridges** in Unification patterns, since external ontologies for quantities (ISO 80000, QUDT, etc.) can be mapped cleanly onto FPF Characteristics now that the term is fixed. In short, A.17 is a foundational lexicon pattern that a) ensures internal consistency and b) simplifies alignment with external standards for measurable properties.
    
### A.17:End

## A.18 - Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)

**Aliases (for narrative use only):** _“Axis”_ (≈ Characteristic), _“Point”_ (≈ Coordinate). _(These colloquial aliases may be used in Plain language **explanations**, but never in formal identifiers or normative text.)_

### A.18:1 - Problem Frame

We often need to **characterize some aspect** of a subject (be it a single artefact or a relationship between artefacts) in a rigorous way. Whether it’s recording a physical quantity, an architectural property, or a performance rating, the characterization must:

-   remain _domain-neutral_ (work for engineering metrics, subjective scores, etc.),
    
-   ensure that two measurements are **comparable if and only if** they share the same defined aspect and scale, and
    
-   accommodate both **ordered tiers** (qualitative levels like Low/Medium/High) and **numeric magnitudes** (continuous or interval values) without mixing them up.
    

In FPF’s kernel, the **CSLC pattern** (CG‑frame–Scale–Level–Coordinate) provides the minimal vocabulary and constraints to achieve this. It defines how one **Characteristic** ties to one **Scale**, and how any measured **value** can be treated as a **Coordinate** on that scale (with an optional named **Level** if the scale is discrete or tiered). The context here is the need for a _unified Standard_ so that every single measurement can be interpreted and compared on common grounds.

### A.18:2 - Problem

**Uninterpretable values.** A raw number or label means nothing without knowing **what aspect it measures** and **how it is measured**. The string “4”, the label “High”, or the real number 9.81 convey no insight unless we know **which Characteristic** they pertain to and the **Scale** that gives them meaning. In cross-disciplinary work this ambiguity is magnified: a “5” could be a risk rank (ordinal), a length in meters (ratio), or a satisfaction score (perhaps interval). Common failure modes include:

-   In **ordinal settings** (e.g. expertise levels _Novice < Skilled < Expert_), one can **rank** values but not meaningfully add or average them. Treating ordinal labels like numbers (e.g. averaging _Novice=1, Expert=3_) produces invalid results.
    
-   In **cardinal settings** (e.g. seconds, meters, degrees Kelvin), arithmetic operations do make sense – but only if units are respected and zero is meaningful (for ratio scales). If we strip away units or mix scales (seconds vs. minutes), we again get nonsense.
    

Without a strict Standard, one team might treat “High” and “Medium” as having a numeric gap, another might average **4** (on a 5-star scale) with **4** (as 4 seconds) because both are “4”. **Inconsistent practices make cross-domain reasoning impossible.** We need a kernel-level solution that _fixes_: (a) the **aspect being measured**, (b) the **scheme by which it’s measured**, and (c) the **type of scale structure** (ordinal vs. metric), _and_ that ensures each reported value is bound to that scheme. At the same time, the Standard should _not_ force artificial numeric detail where it isn’t applicable (e.g. we shouldn’t assign meaningless numbers to purely qualitative tiers just to satisfy a structure).

### A.18:3 - Forces

-   **F1 – Transdisciplinarity.** The pattern must uniformly handle measurements in _physical domains_ (e.g. length, time, temperature), _system attributes_ (e.g. a module’s coupling or reliability), and _human judgments_ (e.g. user satisfaction scores). It needs to be neither overly quantitative (alienating softer domains) nor overly qualitative (lacking precision for hard science).
    
-   **F2 – Comparability vs. freedom.** We want to compare “like with like” – e.g. two readings of the same Characteristic on the same Scale – with absolute confidence. At the same time, the system should allow **different Scales for the same Characteristic** when necessary (for example, one project might measure Quality on a 0–5 star scale, another on a 0–100 percentage scale). The pattern must permit such flexibility _without_ letting those differing scales be conflated.
    
-   **F3 – Ordinal vs. cardinal integrity.** The Standard should preserve the nature of the data: **order-only vs order+distance**. If something is ordinal (ranks, grades), the framework should prevent unwarranted numeric operations on it. If it’s cardinal (real-valued with units), the framework should enable arithmetic but still keep track of units and zero. In essence, it must protect ordinal data from “leaking” into interval arithmetic.
    
-   **F4 – Named tiers vs. continuous magnitudes.** In many domains, **named Levels** (tiers or grades) are useful – e.g. Technology Readiness Levels or bond credit ratings – whereas in others, a continuous scale is needed. The pattern should support **optional Level labels** (for tiered scales) _without forcing_ every scale to have such labels. In other words, Levels are an add-on for discrete/tiered scales, not a requirement for truly continuous measures.
    
-   **F5 – Method agnosticism.** The kernel Standard should say _what_ must be defined (Characteristic, Scale, etc.) but **not prescribe how measurements are obtained**. Whether a value comes from a sensor reading, a simulation, or an expert judgment is up to the respective patterns (e.g. Sys-CAL vs. KD-CAL). The pattern must not bake in any process or scoring methodology; it only ensures that once a measurement exists, it’s well-formed and comparable. This avoids locking in any particular assessment method.
    
### A.18:4 - Solution

**Adopt a minimal “one characteristic – one scale – one coordinate (value)” Standard for all measurements.** In the FPF kernel, any metric must bind **exactly one Characteristic to exactly one Scale**, and any observation produces **one Coordinate (value)** on that Scale (with an optional **Level** name if the scale has discrete tiers). We nickname this the **CSLC clause**:

> **Exactly one Characteristic + exactly one Scale ⇒ one Coordinate (value), with an optional Level.**

Concretely, the parts of this clause are defined as follows:

-   **Characteristic:** the aspect or feature being measured (the “CG‑frame” along which comparison is made). It answers “_What are we measuring?_” – e.g. _Distance, Temperature, Quality, Reliability_.
    
-   **Scale:** the organized set of possible values that the Characteristic can take, including the type of scale (_ordinal_, _interval_, or _ratio_), the measurement **Unit** (if applicable), and any bounds or structure. The Scale defines “_How do we measure it?_” – e.g. “meters on a linear scale from 0 up to 1000” or “ratings 1 through 5 with ordering only”.
    
-   **Coordinate:** a concrete measured value that locates the subject on the chosen scale. This could be a number (for a numeric scale) or a category label (for an ordinal scale). It answers “_What is the result?_” – e.g. 7.4 (meters), or _Expert_ (level).
    
-   **Level (optional):** a named **tier or category** on the scale, used only if the scale is tiered or discretized. For example, an ordinal scale might have Levels _Low, Medium, High_. A Level is essentially a human-friendly label for certain coordinates or ranges. On purely continuous scales, **Level** is not used.
    

Using this **CSLC structure**, every measurement is unambiguous and self-contained: the Characteristic tells us the context, the Scale tells us how to interpret the value, and the Coordinate is the outcome on that scale (with a Level label if appropriate). Notably, this pattern _forbids bundling multiple characteristics into one metric_ – each metric template is one-characteristic-per-template to keep semantics crisp. If something needs to assess multiple factors, it should be modeled as multiple CSLC metrics or a higher-level composite (see §8 below). This one-aspect-one-scale rule is what allows unambiguous comparison and prevents hidden complexity.

Finally, the solution ensures **tier optionality**: If a domain uses named Levels, we include them; if not, we don’t force it. For example, one can have a _Bug Severity_ Characteristic with Levels {Minor, Major, Critical} on an ordinal scale, whereas a _Length_ Characteristic would have a continuous scale (no predefined levels, just units). Both fit the pattern.

### A.18:5 - Archetypal Grounding (System & Episteme Examples)

**In a physical scenario (`U.System`):** Consider an athlete’s long jump. We define a Characteristic **Jump Distance** with a Scale “meters (m)” ranging from 0 upward (ratio scale with meters as the unit). When the athlete jumps and lands at 7.45 m, we record a **Coordinate** of _7.45 m_ for the Jump Distance Characteristic. Here, Jump Distance is the Characteristic, the meter-scale is the declared Scale, and _7.45 m_ is the value (Coordinate). Because this is a cardinal measurement, we can meaningfully say one jump is 1.5 m longer than another, etc. Now consider another metric in the system: **Battery Health** of a device, which might be categorized qualitatively. We could define an ordinal Scale with Levels like _Good, Fair, Poor_ for the Battery Health Characteristic. If a particular device is rated “Poor”, that is a Coordinate on the Battery Health scale (with _Poor_ as the Level name). No arithmetic is done on these labels, but we can order devices by health (Good > Fair > Poor). Both examples illustrate the one-characteristic-one-scale rule: the jump’s distance is not combined with any other aspect; the battery’s health is evaluated on its own defined scale.

**In a knowledge context (`U.Episteme`):** Consider measuring an author’s expertise in a certain domain. We introduce a Characteristic **Expertise Level** for a person, with an ordinal Scale defining tiers such as _Novice, Competent, Expert_. Alice might be assessed at _Expert_ level in software engineering – that’s a **Coordinate** on the Expertise Level scale for the Characteristic “Software Engineering Expertise”. Bob might be at _Competent_. We cannot average Alice’s and Bob’s levels, but we can say the scale is ordered (_Expert_ > _Competent_ > _Novice_). For a more quantitative episteme example, consider a Characteristic **Hypothesis Confidence** for a scientific claim, with a Scale 0–1 (or 0–100%) representing probability or confidence level (ratio scale). One hypothesis might have a confidence of 0.95, another 0.7; these are Coordinates on the Confidence scale. We can compare them numerically (0.95 is higher than 0.7, and 0.95 _implies_ a stronger belief), and we could even combine multiple confidence values through Bayesian formulas (if justified) – but crucially, we would only do so in a way that respects their scale (probabilities combined properly, not treated as arbitrary scores). The Expertise Level and Hypothesis Confidence examples show how the CSLC pattern accommodates both an ordinal qualitative measure and a continuous quantitative measure in the knowledge domain, each with one Characteristic and one defined Scale.

### A.18:6 - Bias-Annotation

The CSLC-Kernel pattern is crafted to be **maximally inclusive of different measurement types** while imposing just enough structure to ensure consistency. It does not privilege any particular domain or modality of measurement: a subjective 5-star rating is treated with the same formal rigor as a physical length in meters. In terms of the FPF principle lenses, this pattern consciously balances the **Architectural/Ontological** needs (clear structure for data) with the **Pragmatic/Didactic** needs (flexibility and clarity for users). There is little risk of cross-domain bias here because the pattern explicitly supports both extremes (ordinal and ratio, qualitative and quantitative). By remaining **method-agnostic**, it avoids bias toward certain validation techniques – e.g. it doesn’t assume every measurement comes from an instrument (it could come from expert judgment just as well). One might argue the pattern enforces a somewhat formal approach to what could be informal measures (forcing definition of scale and characteristic), but this formalism is lightweight and is precisely what makes the metric interpretable. In summary, A.18 embodies **neutrality**: it’s a container that fits any content as long as that content is well-labeled. It reinforces **P‑2 (Didactic Primacy)** by making all metrics self-explanatory in terms of what and how, and respects **P‑1 (Cognitive Elegance)** by using a minimal, uniform scheme. No cultural or disciplinary assumptions are baked in – an anthropologist’s “Cultural Significance” scale can live alongside an engineer’s “Voltage” scale with equal status. The pattern’s requirement for declaring polarity (“higher is better” vs “lower is better” vs target range) further avoids bias in interpretation – it prevents the assumption that “more is always better,” which might be untrue in many contexts (e.g. for error rates, lower is better). All these considerations ensure that A.18 introduces no hidden skew; it merely provides a fair playing field for all metrics.

### A.18:7 - Conformance Checklist

When defining a new metric template or using measurements, practitioners **SHALL** verify the following:

1.  **One characteristic, one scale:** Each metric **template** binds exactly **one Characteristic** to exactly **one Scale**. If you find a metric trying to cover multiple things at once, split it into separate metrics.
    
2.  **Polarity declared:** For any **ordered** Scale (ordinal/interval/ratio), the **polarity** (“higher‑is‑better”, “lower‑is‑better”, “targeted optimum (symmetric or asymmetric around a declared target)”) **SHALL** be declared at the **template** that binds a Characteristic to a Scale. State whether higher values are better, lower are better, or if an optimal range/target exists. (For example: \*“higher is better” for a performance score, \*“lower is better” for error count, or _“target 37 °C” for body temperature where deviation in either direction is worse_.) This ensures that anyone comparing two values knows which way is “up.”
    
3.  **Unit and level clarity:** If the Scale is quantitative, specify the **Unit** (e.g. _seconds, meters, %_) and make sure all values include or assume that unit. If the Scale has named Levels, list them clearly and use them consistently. Do **not** use the same label to mean different things on different scales, and avoid using unit terms in Characteristic names (the unit belongs with the scale).
    
4.  **Scale-appropriate operations only:** Only perform those comparisons or calculations that are valid for the given scale type. For a nominal scale, you can check equality but not order. For an ordinal scale, you can order or rank values but not do math like “A minus B.” For interval scales, addition/subtraction is OK (with unit conversion if needed), but ratio comparisons (A is twice B) might not make sense without a true zero. For ratio scales, all arithmetic operations are allowed _with proper attention to units_. This check prevents logical errors (e.g. averaging “High” (3) and “Medium” (2) and getting 2.5 — which is meaningless).
    
5.  **No bare numbers:** Never present a raw number or value without its context of Characteristic and Scale. If someone sees “42” in your output, they should _also_ see or know “42 of what, measured how.” A reader who is not aware of the metric’s template should not be left guessing what a given value signifies. In practice, this means labeling reports and data with the metric name or identifier so that values can be traced back to their meaning.
    
6.  **Template bridges for cross-metric comparison:** If you intend to compare or aggregate measurements from **different templates** (different Characteristics/Scales), ensure an explicit **ScoringMethod** or conversion is defined. For example, if you need to combine a “usability score” (0–5 stars) with a “security score” (0–100%), you might define a new **Score** that maps both onto a common 0–10 scale via monotonic functions. Without such a bridge, do not directly mix metrics – keep them separate in analysis. This guarantees that any cross-metric reading has a well-founded basis.
    
7.  **Level optionality respected:** If your Characteristic doesn’t naturally have tiers, don’t force it to have **Level** names (you can leave the Level concept unused). Conversely, if your Characteristic is commonly described in categories, it’s fine to define Levels for clarity. The key is to use the Level field intentionally: either not at all (for truly continuous measures) or in a fixed, **non-overlapping** way (for discrete categories). Do not use “Level” for something that behaves like a continuous value (it would be confusing to assign a label where a number would do, or vice versa).
8. **Comparability test:** Two Coordinates are comparable iff same Characteristic+Scale (incl. unit, polarity). Otherwise — Score‑level only after a declared SCP to a bounded range.

_(The above serve as normative checkpoints. Many of these are automatically supported by using the standard metric templates in software: e.g. the system will enforce one Characteristic per template, require a unit for ratio scales, etc. The **Lexical rules** from A.17/E.10 are assumed: use canonical names and notations for all parts of the metric.)_

### A.18:8 - Consequences

Adopting the minimal CSLC Standard in the kernel yields a number of benefits:

-   **Universal interpretability:** Every measurement is intrinsically self-describing. One cannot have a “mystery number” floating around; by design you must know it’s _X (Coordinate) on Y Scale of Z Characteristic_. This dramatically reduces miscommunication in reports and data exchange. An engineer and an analyst can share a metric knowing they interpret it the same way, because the context travels with the value. Level is optional when scale is tiered or discreet. 
    
-   **Safe comparison and aggregation:** Values can only be compared when they belong to the same Characteristic and Scale (or when an authorized SCP converts them). This prevents the common error of comparing apples to oranges. When cross-comparison is needed, the pattern funnels us into creating a proper normalization, which improves the soundness of composite scores. Essentially, it’s now impossible to accidentally average an uptime percentage with a user satisfaction rating, for example, without explicitly defining how to map one to the other.
    
-   **Flexibility across domains:** The pattern is **transdisciplinary**. It doesn’t matter if the measurement is temperature in Kelvin, length in inches, code complexity in “abstract points,” or user satisfaction on a five-level Likert scale – all are handled uniformly. This makes it easier to plug new patterns for new domains into FPF, since they don’t need special rules for their metrics; they just instantiate the CSLC template in their context.
    
-   **Ordinal and cardinal handled with equal rigor:** By explicitly classifying scales, the pattern gives ordinal data the respect it deserves (no pretending it’s numeric) and gives ratio data the formal context it needs (units, zero, etc.). This balance means both qualitative assessments and quantitative measurements live side by side, each with their constraints respected. Domains that lean heavily on categorical ratings benefit from the **Level** concept (with no pressure to assign fake numbers), and domains that use real measurements benefit from unit enforcement and type-aware computations.
    
-   **Clarity in multi-factor scoring:** The prohibition of implicit multi-characteristic measures means that any “overall” score or index has to be constructed out of known pieces. This tends to improve the transparency of complex scoring schemes. If an organization wants to create a single index from 5 different metrics, A.18 forces them to introduce a defined ScoringMethod function that combines those 5 Coordinates into one Score, with declared monotonicity and bounds. The consequence is that composite metrics become auditable and debatable (you can examine the weighting or formula) rather than opaque sums.
    
-   **Methodological neutrality (and innovation):** Because the kernel imposes no method for obtaining the values – only how to frame them once obtained – patterns and tool builders are free to innovate in how they measure things. The Standard just ensures that once they do, everyone else can understand and use the results correctly. This separation of concerns (what vs. how) accelerates multi-disciplinary collaboration: a social scientist’s observational scale can feed into a systems model without any confusion, as long as it’s couched in the CSLC terms.
    

On the downside, **users must do a bit more upfront work** to define their metrics. The pattern’s requirements (declare Characteristic, define Scale, etc.) mean one cannot simply say “we’ll track a risk score” without further detail. In practice, this is a _desirable_ trade-off: the extra effort (perhaps a few minutes to set up a metric template) prevents far greater confusion down the line. Another possible trade-off is **multiplicity of scales** – the pattern allows the same Characteristic to have multiple scales (in different contexts or versions), which might fragment data if not managed (e.g. two teams measuring “Performance” on different scales). However, it also provides the remedy: make the difference explicit and, if needed, build a conversion ScoringMethod. This explicitness is actually beneficial, as it highlights when “Performance (0–5)” is not directly comparable to “Performance (Percentage)”. In short, any fragmentation is out in the open and can be dealt with via alignment or bridging.

Overall, A.18’s consequences are overwhelmingly positive: **measurements become first-class, well-understood citizens of the model.** The cost is a slight increase in definition effort and discipline, which is a small price for coherence. Once this pattern is in place, higher-level patterns (in Parts B, C, D) that reason about metrics can rely on it. For example, trust calculations (Part D) can assume that any metric they consume has a known scale and meaning, and knowledge dynamics algorithms (Part B or C) can safely combine evidence knowing the comparisons are valid. The minimal CSLC Standard is thus a foundational enabler for robust, cross-domain assurance in FPF.

### A.18:9 - Rationale

The rationale behind A.18 is to enforce _semantic clarity_ at the data level, thereby solving a host of downstream problems. Without this pattern, one must constantly ask, “What does this number mean? Can I combine these two values?” – questions that have led to many project errors. By building the answers into the framework (“every number knows its unit, scale, and aspect”), we front-load the work and eliminate ambiguity. The solution directly addresses each force:

-   **Transdisciplinarity:** We include both ordinal and cardinal mechanisms so that no discipline’s metrics are left out. This was informed by observing multi-disciplinary teams: e.g., in a single project, a human factors specialist might rate usability (ordinal) while an engineer measures throughput (ratio). A.18 gives them a common language and prevents one from misusing the other’s data. It embodies the idea that _universal structure enables local freedom_: everyone’s metric can plug in, as long as they specify it properly.
    
-   **Comparability vs. freedom:** The pattern strikes a balance by tying comparability to explicit commonality. If two metrics truly measure the same thing in the same way, then of course you can compare them – they’ll share Characteristic and Scale. If they differ, the framework doesn’t stop you from defining them (freedom), but it does stop you from _conflating_ them inadvertently. The introduction of **polarity** declarations is a direct response to this tension: it adds a tiny burden (must declare “higher is better” etc.) but yields big pay-off in avoiding mis-ordered interpretations and enabling safe composite scoring (monotonic ScoringMethods).
    
-   **Ordinal vs. cardinal separation:** The rationale here is guided by measurement theory: we want to preserve information content. Treating ordinal data with only order operations preserves all its information; doing more (like adding them) injects false information. The pattern’s strictness on scale types forces modelers to be honest about what their data can and cannot do. This not only prevents errors but also encourages **best practices** (e.g. if you find you desperately want to average an ordinal score, perhaps you should refine it into an interval scale in your methodology). The outcome is a framework that respects both the **qualitative** and **quantitative** realms appropriately, aligning with **FPF’s Pillar of Pragmatism** – use formalism where it’s justified, but not beyond its limits.
    
-   **Optional Levels:** Requiring Levels in every case would have been too rigid (not everything has named tiers), but not supporting them would fail domains that rely on them (like maturity models or grading systems). The rationale for making Level _optional_ is to accommodate both. We saw in practice that many metrics naturally form tiers (e.g. technology readiness levels TRL 1–9) and giving them a slot in the model (instead of burying them in definitions) makes those metrics much easier to work with and integrate. Meanwhile, continuous metrics carry no baggage of unused fields. This design was checked against existing standards (like ISO 25024 for quality measures) to ensure we aren’t deviating from industry expectations: indeed, separating the concept (Characteristic) from the scheme (Scale) aligns well with standards, and including an optional categorization aligns with common practice in capability maturity models, etc.
    
-   **Method neutrality:** The decision to _not_ include any measuring procedures in A.18 (no specific formulas, no mandated evidence type) comes from the principle of separation of concerns. The kernel should provide the _what_ and _how (structurally)_, while patterns provide the _how (procedurally)_. This keeps the kernel lean (**P‑1 Cognitive Elegance**) and allows domain experts to implement whatever method is appropriate, merely committing to wrap their results in the CSLC form. By doing so, we avoid any bias toward empirical vs analytical, or manual vs automated measurements – FPF welcomes all, as long as they conform to the schema. This was rationalized by examining case studies: e.g., some reliability metrics come from formal proofs (analysis), others from testing (empirical) – the kernel can host both results identically, requiring only that each result says what it measured and on what scale.
    

In essence, A.18 is the _infrastructure of meaning_ for metrics. It may appear as a simple template, but it’s profoundly enabling. It forces clarity at creation time, so we don’t have to infer or debate meaning at usage time. The pattern’s strength lies in preventing errors that _don’t have to happen_. It encodes lessons from both metrology (the science of measurement) and everyday data science (where unit errors and mis-comparisons are infamous issues). The rationale is backed by these lessons: **fix the interpretation rules in the design, and you eliminate entire classes of confusion and mistakes.** By having this in the kernel, every mechanism – from knowledge scoring to system performance – benefits immediately, and their results become interoperable to a degree that would be impossible without a common structure.

### A.18:10 - Relations

-   **Extends/Uses:** **A.17 (CHR-NORM)** – A.18 explicitly builds on the canonical terminology established in A.17. It uses the term **Characteristic** as defined there (and no other synonyms) and carries forward the edict that “axis/dimension” be treated as mere narrative aliases. It also leverages the Entity-vs-Relation Characteristic distinction from A.17: Section 7.4 of this pattern references tests for disambiguating relational metrics. Essentially, A.17 provides the **lexical and conceptual groundwork** (what a Characteristic is, and the basic vocabulary), while A.18 provides the **structural and normative rules** for linking Characteristics to measurements.
    
-   **Core foundation for metrics:** This pattern underpins the **Measurement & Metrics Characterization spec (C.MM‑CHR)** – the pattern that implements metric storage and computation. In MM-CHR, every `U.DHCMethodRef` and `U.Measure` follows the CSLC format defined by A.18. By lifting CSLC rules to the kernel, we ensure all FPF patterns (like **KD-CAL** for knowledge dynamics, **Sys-CAL** for systems, or any custom CAL/CHR) share a common approach to metrics. A.18 also informs the design of **CHR-CAL (Characterisation Calculus)**, which generalizes measurable property templates: CHR-CAL relies on the one-Characteristic-per-metric assumption and the comparability rules set here to compose higher-level characterizations.
    
-   **Enables dynamic reasoning:** A.18’s insistence on well-defined Scales allows patterns like **A.3.3 `U.Dynamics`** (system dynamics models) to incorporate measurement dimensions as state variables without ambiguity. For example, a `stateSpace` in a dynamics model can be explicitly defined as a set of Characteristics (each with units and ranges), making simulations and traces dimensionally consistent. If A.18 were not in place, one model might treat “performance” as a 1–5 score and another as a probability – combining them would be incoherent. With A.18, such differences must be reconciled via a ScoringMethod or kept separate, preserving coherence in multi-model analyses.
    
-   **Coordinates with assurance patterns:** Many patterns in Part B and D (for trust, assurance, and ethics) involve **scores** and **metrics**. For instance, **B.3** (Assurance Levels) computes overall assurance from evidence scores; A.18 ensures those input scores are well-defined and comparable (e.g. all are 0–1 or all are percentages, with polarity noted). **D.4** (Trust-Aware Calculus) might combine trust metrics across domains – again, A.18 provides the common ground so that a “trust score” coming from an operational metric and one coming from a social rating can be normalized and compared meaningfully. In summary, any pattern that aggregates or uses measurements is constrained (in a positive way) by A.18’s rules. They “plug into” this framework.
    
-   **Constrained by lexical rules:** This pattern’s content is part of the formal lexicon governance. It works within **E.10 LEX-BUNDLE**, which means the terms _Characteristic, Scale, Coordinate, Level,_ etc., are controlled vocabulary. A.18 localizes some generic requirements from A.17 (for example, A.17 mandates polarity in principle; A.18 requires it be declared per template in practice). It also aligns with external standards: by having explicit scale types and units, it dovetails with ISO/IEC measurement terminology and allows straightforward mapping to frameworks like **ISO 80000 (quantities and units)** and **Stevens’s scale types**. This relation to standards is deliberate – it eases **F.9 (Alignment Bridge)** construction to external ontologies by having a clean internal schema (A.18 provides that schema). In effect, A.18 is where FPF’s internal consistency meets external compatibility, ensuring our measurement semantics can relate to those outside FPF when needed.

### A.18:End

## A.19 - CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)

### A.19:0 - Reading path for engineer-managers

> **Informative (navigation only).** This subsection is a didactic index for human readers. It introduces no new norms and does not change semantic ownership.

**When to use this path.** You need to review a CHR-enabled plan or audit, or coordinate engineering work across teams, without deep-diving every CHR mechanism up front.

**Step 1 — Measurement vocabulary: what is measured, and what “comparable” can mean.**

* **A.17** — canonizes the technical anchor **Characteristic** (and retires near-synonyms such as “axis/dimension/feature/property/metric” from normative Tech register).
* **A.18** — CSLC discipline (**Characteristic / Scale / Level / Coordinate**) as the metrology of interpretability, comparability, and lawful aggregation.
* **C.16 (MM‑CHR)** — the measurement substrate (`U.DHCMethodRef`, `U.Measure`, `U.Unit`, `U.EvidenceStub`) and the conservative baseline of **direct comparability** (“same template”). C.16 makes coordinates auditable; it does not define CHR mechanisms.

**Step 2 — Ontology and contract surfaces the CHR suite operates on.**

* This pattern **A.19** — `U.CharacteristicSpace` and the dynamics hook: the base ontology of measurable coordinates and their spaces.
* **A.19.CN** — CN‑frame / **CN‑Spec**: the contract surface for normalization and comparability routing, indicator policy, aggregation routing, and acceptance; it explicitly points to **C.16** for evidence/backing and to **G.0** for legality gates.

**Step 3 — Legality gates and mechanism shape (what to check when numbers appear).**

* **G.0 (CG‑Spec)** — the legality gate for numeric operations and comparisons (SCP, ComparatorSet, MinimalEvidence, Γ_fold, crossings/plane pins). CHR mechanisms cite CG‑Spec; they do not duplicate it.
* **A.6.1 / A.6.5** — the mechanism norm‑form (`U.Mechanism.Intension`) and slot discipline. Read once so the structure of each mechanism owner pattern (slots, operators, laws, admissibility guards, audit anchors) is predictable.

**Step 4 — The CHR suite boundary and the P2W seam.**

* **A.19.CHR (CHRMechanismSuite)** — focus on:
  * `A.19.CHR:4.1` (published objects),
  * `A.19.CHR:4.2.1` (CHR SlotKind lexicon),
  * `A.19.CHR:4.2.2` (canonical mechanism targets),
  * `A.19.CHR:4.5` (suite protocols — order/optionality live here, not in `mechanisms[]`),
  * `A.19.CHR:4.6–4.7.2` (P2W planned-baseline hook and the plan-item shape),
  * `A.19.CHR:7` (suite conformance checklist).
* **A.15.3** — `SlotFillingsPlanItem` (planned baseline discipline: planning vs enactment).
* **E.18 (E.TGA)** — how to express the actual pipeline/flow graph (including crossings) while keeping suite and plan artefacts refs‑only.

**Step 5 — The six CHR mechanism owner patterns (read one at a time).**

Each mechanism below owns its `U.Mechanism.Intension` card and assumes the measurement-lawfulness base from **A.17/A.18** and **C.16**.

1. **A.19.UNM** — normalization (CV→NCV, `≡_UNM`, `TransportRegistryΦ`).
2. **A.19.UINDM** — indicatorization (policy-bound indicator selection; no “NCV ⇒ indicator” shortcut).
3. **A.19.USCM** — scoring (SCP-first; no implicit UNM).
4. **A.19.ULSAM** — lawful aggregation (explicit `Γ_fold`; ordinals are not averaged).
5. **A.19.CPM** — comparison (set-valued outcomes; no silent scalarisation/totalisation).
6. **A.19.SelectorMechanism** — selection kernel (set-returning; dominance/portfolio defaults are policy-bound).

**Step 6 — Specialization and reuse.**

* **E.20** — how to use specializations of mechanisms (`⊑` / `⊑⁺`) without breaking SlotKind meaning or introducing hidden inputs; consult this whenever you see project‑ or domain‑specific variants of the CHR mechanisms.

**Fast review entry points.**

* If you are reviewing a plan: start from **A.19.CHR:4.6–4.7.2** (planned baseline hook + plan item shape) and **A.15.3** (what a planned baseline may/may not contain).
* If you are reviewing semantic drift: start from **A.19.CHR:4.2.2** (canonical targets), then use **E.10** (suffix discipline) and **F.18** (alias docking) to preserve public continuity while fixing terminology.
* If you are reviewing conformance: start from **A.19.CHR:7** (suite checklist), then consult the relevant **A.19.<MechId>** checklist(s) for mechanism-level conformance; use **E.19** for the review protocol.

**Non‑duplication note.** This pattern defines `U.CharacteristicSpace` and the typing hook `U.Dynamics.stateSpace`. It reuses the canonical measurement concepts (`U.Characteristic`, **CSLC** terms) from **A.17/A.18** and remains notation‑neutral about storage/IDs.  
This pattern is intentionally **not** a second semantic owner for CHR mechanisms: it may *use* CHR‑mechanism terms when talking about comparability and certification, but it does so strictly by *Tell + Cite* to the corresponding `A.19.<MechId>` mechanism‑owner patterns.

**Single‑owner rule (Normalization & CHR mechanisms referenced here).** This pattern **MUST NOT** be a second semantic owner for CHR‑mechanism vocabulary.
- **Normalization vocabulary + admissibility** (UNM artifacts: `UNM`, `NormalizationMethod`, `NormalizationMethodDescription`, `NormalizationMethodInstance`, **NCV**, **≡_UNM**, `NormalizationFix`; κ‑retirement; “map vs Map” lexical guard) are owned normatively by **A.19.UNM**.
- **Indicatorization vocabulary + admissibility** (UINDM artifacts: `IndicatorChoicePolicy`, `Indicator`, `IndicatorSet`, indicatorization as a policy step; “NCV ⇒ indicator” prohibition) are owned normatively by **A.19.UINDM**.
- **Other CHR mechanism vocabulary referenced here** (e.g., scoring / aggregation / comparison / selection terms) is owned normatively by the corresponding mechanism‑owner pattern in the `A.19.<MechId>` family (e.g., `A.19.USCM`, `A.19.ULSAM`, `A.19.CPM`, `A.19.SelectorMechanism`).
- **Evidence/calibration backing** for normalization is owned by **C.16 (MM‑CHR)**.
- **CN‑frame surface wiring** (how CN‑Spec references normalization/comparability by fields/refs) is owned by **A.19.CN (CN‑Spec)**.
- **Vocabulary extension rule.** If this pattern needs a new normalization / indicatorization / scoring / aggregation / comparison / selection term, it SHALL be introduced in the corresponding mechanism‑owner pattern first, then cited here (*Tell + Cite*). A.19 SHALL NOT mint new CHR‑mechanism vocabulary.

**Terminology pointer (informative; do not duplicate).** When A.19 uses normalization or indicatorization terms below, it uses them *by reference* to **A.19.UNM** / **A.19.UINDM** and **C.16**. This pattern only constrains how such artifacts are **cited** when doing state‑space comparability, embeddings, and certification.

**Reader map (informative).**
* If you need the **meaning** of `UNM`, `NCV`, `≡_UNM`, or `NormalizationFix` / `NormalizationFixSpec`: see **A.19.UNM**.  
* If you need the **meaning** of `IndicatorChoicePolicy` / indicatorization: see **A.19.UINDM**.  
* If you need the **CN‑Spec field/Ref wiring** (`CN_Spec.normalization`, `CN_Spec.comparability.*`): see **A.19.CN**.  
* If you need **evidence/calibration backing** for normalization or scoring legality: see **C.16 (MM‑CHR)**.  
* If you need **cross‑context alignment mechanics**: see **F.9 (Alignment Bridge)** and the `Transport` discipline (A.6.1).

### A.19:1 - Intent & Scope (Normative)

**Intent.** Establish a **kernel‑level state‑space type**—`U.CharacteristicSpace`—so that any holon’s **state changes** (e.g., a system’s condition or a role’s readiness) can be formalized as **trajectories in a space of declared Characteristics with chosen Scales**. For **epistemes**, state is governed by **ESG**; **F–G–R** are **assurance coordinates**, not a state space. This gives every `U.Dynamics` model a well‑typed `stateSpace` and enables formal state certification (using RoleStateGraph checklists) instead of narrative stage transitions.

**Scope.** Pattern A.19 **defines**:

-   the **type** `U.CharacteristicSpace` as a finite product of **slot value sets** (per A.18),
-   the **slot** construct for each factor (a pairing of a **Characteristic** with a chosen **Scale**),
    
-   minimal **structural overlays** (optional **order**, **topology**, **metric** hooks) that downstream patterns _may_ attach to a space, and
    
-   the **hook** `U.Dynamics.stateSpace : CharacteristicSpace` – i.e. the requirement that any dynamics model declare a CharacteristicSpace for its state space (typing only).
    

A.19 **does not** introduce any new measurement aspects, composite metrics, or **normalization semantics** (owned by **A.19.UNM**, with evidence/calibration under **C.16 (MM‑CHR)**), and it does not define how dynamics evolve over time or any predictive laws (see **A.3.3** for dynamics semantics). The focus here is purely on the _structure of state spaces_ and their comparability.

**Lexical guard (“map”).** Follow the normalization lexical discipline owned by **A.19.UNM**. In this pattern, lowercase **map** is used only in the mathematical sense, while capitalized **Map** retains its Part‑G suffix meaning (e.g., `DescriptorMap`). Do not mint new normalization terminology here.

**Lexical guard (“carrier”).** In kernel prose, **Carrier** (capitalized) names `U.Carrier` (a **symbol bearer**). Do **not** use “carrier” for set‑theoretic supports; prefer **ValueSet**/**underlying set**. A.19 therefore uses **ValueSet(slot)** for the set that supplies values to a slot.

### A.19:2 - Context (Informative)

FPF’s kernel already standardizes **what** is measured (a **Characteristic**, per A.17) and **how** it is measured (a **Scale** with units, via the **CSLC** Standard in A.18). We also have a measurement substrate (`U.DHCMethodRef`, `U.Measure`) to handle individual observations. What has been missing for modeling **dynamics** is a canonical “Context” in which **multiple Characteristics** can co-exist so that complex **states** (with many aspects) and their **trajectories** are well-typed and comparable. Without a formal CharacteristicSpace, teams either hard-code ad-hoc vectors (often with inconsistent assumptions) or fall back to informal lifecycle stories (“phases” or stages) that contradict the kernel’s open-ended, non-linear evolution paradigm. The Architectural patterns (A-cluster) expect that `U.Dynamics.stateSpace` will be a set of **declared Characteristics each with a declared Scale**. Pattern A.19 delivers exactly this capability, leveraging the CSLC measurement discipline without reinventing any arithmetic or unit-handling logic.

### A.19:3 - Problem (Informative)

-   **P1 — “Feature vector” drift.** In practice, teams often assemble state vectors or “feature” lists with implicit or mismatched units and scales. Without a formal space, one coordinate’s value can’t safely be compared or combined with another’s (e.g. mixing degrees Celsius with percentages). **CSLC** guarantees consistency **per Characteristic**, but a bundle of multiple “characteristics” remains under-specified if we lack a unified space definition.
    
-   **P2 — Lifecycle bias.** Absent a formal state space, system change tends to be described in terms of fixed **stages or phases** (design phases, maturity levels, etc.). This conflicts with FPF’s **open-ended** stance: in FPF a role’s state model (RSG) allows re-entry and refinement of states rather than one-way lifecycle stages with an “end.” We need a space model that treats evolution as continuous movement, not a one-directional sequence.
    
-   **P3 — Incoherence across CN‑frames.** Different modeling “CN‑frames” (architecture vs. epistemic vs. operational) often choose different sets of qualities to measure (different sets of characteristics). Later, however, we may need to **compose** these models or **project** one into another. Without a kernel notion of how one state space can be a **subspace** of or **embedded** in another, any integration of models will be ad hoc and error-prone.
    
-   **P4 — Relational measurements.** Some Characteristics are inherently **relational** (e.g. a _Coupling_ between two components, or _Distance_ between points). Naïvely forcing such traits into a single-object feature vector loses critical information (arity, symmetry). The kernel already distinguishes single-entity vs multi-entity Characteristics (A.17); we must preserve that distinction in the state space so that a relational metric isn’t treated as an intrinsic one by mistake.
    
-   **P5 — The geometry temptation.** When defining a state space, it’s tempting to assume or inject additional structure (ordering of states, topologies for continuity, metrics for distance) as if inherent. But the kernel must remain minimal and domain-neutral: it should not **smuggle in** analysis methods or domain-specific norms under the guise of geometry. Any such structure should be added explicitly by specialized patterns, not baked into the core definition of a space.
    

### A.19:4 - Forces (Informative)

-   **F1 – CSLC integrity at scale.** When combining multiple measurements into a state, we must uphold the **CSLC discipline** for each component: each coordinate has a defined Characteristic, Scale type, unit, and (if applicable) polarity. We need to do this without redefining or duplicating that single-characteristic integrity – the multi-dimensional space should simply enforce CSLC per slot.
    
-   **F2 – Transdisciplinarity & lexical clarity.** The state space framework must work for **quantitative physical metrics** (ratio scales, continuous units), **qualitative assessments** (ordinal scales, tiers), and mixtures thereof. It must not be biased toward one domain’s notion of measurement. At the same time, to avoid confusion, the **lexicon must remain canonical**: we use _Characteristic_ (not “axis/dimension”) as the formal term for a measured aspect, regardless of domain, per A.17’s naming convention.
    
-   **F3 – Arity and semantics.** Lifting various Characteristics into a unified space should not obscure their nature. If a Characteristic is defined as a relation (multi-entity property), the state space must represent it appropriately (e.g. as a coordinate that is a tuple or a symmetric relation) rather than flattening it into an unrelated scalar. Entity-specific vs relational properties must remain clear in the space’s structure.
    
-   **F4 – Minimal core, extensible further.** The kernel should provide only the **bare essentials**: a carrier for state with proper typing. It should be possible to impose additional structure like order, topology, or metrics _if and when needed_ by downstream theories, but these must be **optional overlays**. The core space definition should be minimalistic to allow broad use, yet capable of extension for advanced needs.
    
-   **F5 – Composability of spaces.** We need well-defined operations to **project** a state space to a subspace (dropping some Characteristics), **embed** one space into a larger space (mapping coordinates from one context to another), and take **products** of spaces (combining different state spaces into a joint space). These operations are crucial for composing sub-models, comparing alternatives, or aligning different “CN‑frames” (for example, linking an architectural model’s state space with a metrics model’s space). The approach must support such composition in a principled way.
    
-   **F6 – Alignment with RSG (state machines).** In FPF, formal **state certification** is done via checklists on RoleStateGraphs (A.2.5). Our state space concept must complement that: i.e. the **state** of a holon remains an **intensional** concept (defined by criteria), but those criteria are evaluated against the measurable **coordinates** in a CharacteristicSpace. The design must allow checklists to map observed coordinates to named states and enable re-certification as states evolve, rather than locking states into a static progression.
    

### A.19:5 - Solution

#### A.19:5.1 - `U.CharacteristicSpace`

##### A.19:5.1.1 - Type signature

Let **I** be a finite index set labeling a collection of **slots**. Each **slot** _i_ (for _i ∈ I_) is defined as a pair:

> **`slot_i = (Characteristic_i, Scale_i)`**,

where:

-   `Characteristic_i` is a `U.Characteristic` (with an explicit arity, i.e. either an entity-Characteristic or a relation-Characteristic as defined in A.17), and
    
-   `Scale_i` is a chosen **Scale** for that Characteristic (with a specified scale type and unit, per A.18 and the MM‑CHR rules).
    
Then a **CharacteristicSpace** (CS) is formally the Cartesian product of all slot **value sets**:

$$\mathbf{CS} = \prod_{i \in I} \mathrm{ValueSet}(\mathrm{slot}_i)\,.$$

In other words, a point (state) in the space consists of one coordinate value for each slot. A **state** _x_ in CS can be seen as a total function _x(i)_ that picks a value from each slot’s **ValueSet** (for every _i ∈ I_, _x(i) ∈ ValueSet(slot\_i)_). By kernel mandate, any `U.Dynamics.stateSpace` **SHALL** be bound to some instance of `CharacteristicSpace`, and all states or trajectories described by that dynamics model **MUST** lie within that space’s **value set**. (The actual dynamic **laws** and time progression are handled in A.3.3; A.19 only defines the state‑space container and its properties.)

##### A.19:5.1.2 - Slot discipline (invariants)

To ensure consistency and comparability, a CharacteristicSpace must obey the following invariants:

-   **A19-CS-1 (Exactly one per slot).** Each slot **binds exactly one** Characteristic to **exactly one** Scale (including a specific Unit or kind, if applicable). This mirrors the CSLC clause of “one aspect – one scale”: there are no ambiguous or compound mappings in a single slot. (If a Characteristic can be measured on multiple scales, only one is chosen for a given space; others would require separate slots or a different space.)
    
-   **A19-CS-2 (Named basis).** A CharacteristicSpace **SHALL** publish an ordered list of its slots as its **basis**. Each slot in the basis has a stable identifier (or key) that can be used in data structures or APIs. These basis names should be treated as technical identifiers (machine-readable tokens); any human-friendly alias or description for a slot should be provided only in the Plain register as a non-normative aid (per E.10). In short, the identity and order of slots in the space are explicit and stable.
 -   **A19-CS-2 (Named basis).** A CharacteristicSpace **SHALL** publish an ordered list of its slots as its **basis**. Each slot in the basis has a stable identifier (or key) that can be used in technical notations and interfaces. These basis names should be treated as stable technical tokens (identifier‑like); any human-friendly alias or description for a slot should be provided only in the Plain register as a non-normative aid (per E.10). In short, the identity and order of slots in the space are explicit and stable.
    
-   **A19-CS-3 (Immutability of meaning).** Once a space is in use, the meaning of each slot is fixed. A slot’s `(Characteristic, Scale)` pair **MUST NOT** be retroactively altered. If requirements change (e.g. a different scale or a revised definition of the Characteristic), one **MUST** define a new version of the space (or a new slot) rather than silently changing the existing one. When a space is versioned or a slot replaced, an explicit **embedding** (mapping from the old space to the new space) should be published to relate historical states to the new coordinates. This ensures past data remains interpretable and prevents semantic drift.
    
-   **A19-CS-4 (Arity preservation).** If a `Characteristic_i` is defined as a **relation** (multi-entity characteristic), then slot _i_ represents a relationship among multiple entities. The coordinate value at such a slot is a **tuple** (with the appropriate entity types) rather than a simple scalar. The slot’s declaration **SHALL** indicate the relation’s symmetry or directionality as part of its meaning (this should align with how the Characteristic was originally defined in its template). In essence, relational Characteristics retain their arity in the space, so that we don’t confuse, say, “Coupling between X and Y” with an intrinsic property of X or Y alone.
 
 -  **A19-CS-5 (No hidden normalizations or aggregations).** A CharacteristicSpace itself carries **no implicit normalizations or formulas** for combining coordinates. It is a _descriptive_ structure, not a scoring mechanism. Any computation that combines or transforms coordinates (e.g., **normalizing**, **indicatorizing**, **scoring**, **Γ‑folding**, **comparing**, or **selecting**) must be defined outside the core space—typically as an explicit **CHR mechanism step** and cited from its designated mechanism‑owner pattern (`A.19.UNM`, `A.19.UINDM`, `A.19.USCM`, `A.19.ULSAM`, `A.19.CPM`, `A.19.SelectorMechanism`).  
   *Normalization semantics and admissibility* are owned by **A.19.UNM**; *evidence/calibration backing* is owned by **C.16 (MM‑CHR)**.  
   In particular, any handling of **polarity** (which way “better” is), weighting, or cross-slot aggregation happens in those external mechanisms/policies, not inside the space definition. The space provides the raw coordinates; the logic to interpret or aggregate them is added by domain‑specific layers with explicit disclosure of how it’s done.

 - **A19-CS-6 (Slot meta completeness).** Where applicable, each slot **SHALL** declare `admissible_domain` and **missingness semantics** (e.g., codes for *missing*, *censored*, *not-applicable*), consistent with the Characteristic’s Scale and with MM‑CHR. This prevents silent domain drift and clarifies how absent values participate in predicates and comparisons.

##### A.19:5.1.3 - Minimal structure hooks (optional overlays)

By default, a CharacteristicSpace has no assumed ordering or metric structure – it is just a Cartesian product of value sets. However, a space **MAY** declare certain structural attributes _as opt-in metadata_ (i.e. informative annotations that patterns can rely on, but not enforced by the kernel). These optional **overlays** include:

-   **Product topology.** A **topology** on the space, typically the product topology when slots that are quantitative (interval or ratio scales) need continuity considerations. Declaring a topology is useful if continuity or convergence arguments are relevant (e.g. to say a sequence of states approaches a limit state). By default, without declaration, no topological structure is assumed on the space.
    
_Lexical note:_ Here **“distance metric”** strictly means a mathematical distance function (or a generalized distance such as a **pseudometric** or **quasi‑metric**) on the state space. This is **not** to be confused with *metrics* as performance measures in MM‑CHR. In the **Tech** register, avoid the noun **metric**; refer to **`U.DHCMethod`/`U.DHCMethodRef`** for measurement templates (see **C.16**). Any distance overlay on a CharacteristicSpace must not conflict with scale semantics; it is an additional analysis structure, not a redefinition of measurement meaning.

These overlays are entirely **optional** and have no effect on the core meaning of the space – they exist only to support particular needs (like making **dominance**, **continuity**, or **distance** reasoning possible) in models that require them. If needed, they should be added deliberately by an architectural theory rather than assumed. This way, any ordering or metric properties of states are made **explicit** instead of relying on hidden or default arithmetic. _(Rationale:_ The CSLC and MM‑CHR rules already govern what operations are allowed on each scale; A.19’s approach is to let higher-level theories layer on an order, topology, or metric when appropriate, so nothing is taken for granted tacitly in multi-dimensional arithmetic._)_

##### A.19:5.1.4 - Dynamics hook (typing only)

Any model of change or dynamics in FPF must declare the state space it operates over. Formally, `U.Dynamics.stateSpace` **SHALL** be specified as a reference to a `CharacteristicSpace`. This creates a typing obligation: the dynamic model can only produce states (and trajectories of states) that lie in the given space. All predicates or predictions in such a dynamics model are understood to **quantify over** sequences of points in that CharacteristicSpace (with time semantics governed by A.3.3’s time base and laws). **Note:** A.19 defines only the structure of the state space; it deliberately **does not** fix any time axis or dynamic law. Those remain the responsibility of the dynamics pattern (A.3.3). A.19 simply ensures there is a well-defined space in which states live, so that dynamics are decoupled from any narrative “stage” and instead treat evolution as movement through this space.

##### A.19:5.1.5 - Lexical discipline (Normative)

In all **normative references, definitions, and identifiers** related to this pattern, the specification uses the canonical measurement terminology: **Characteristic**, **Scale**, **Level**, **Coordinate**, **CharacteristicSpace**, **slot**, **basis**. Legacy terms like “axis”, “dimension”, or “point” are **forbidden** in Technical/Formal registers of the spec (per A.17’s lexical rules). They may appear _at most once_ in explanatory **Plain** language as mapped aliases to aid understanding (and if used, must be explicitly identified as equivalent to the official terms). In this pattern, we consistently use “slot” or “basis element” (never “axis”) to refer to a component of a space, and “Characteristic” (never “dimension”) to refer to the measured aspect. This lexical discipline ensures clarity and consistency across the framework (see A.17 and C.16 L-rules for the formal policy on terminology).

##### A.19:5.1.6 - Quotients & NormalizationFix (Normative)

**Owner note.** `≡_UNM` and `NormalizationFix` are defined in **A.19.UNM**. This section constrains only how they are **cited** when used in state‑space reasoning.

**Design rule — read invariants, not labels.** Any checklist, acceptance predicate, or comparability claim over a CharacteristicSpace **SHALL** be evaluated on **quotients by ≡_UNM** (or on explicitly **Normalization‑fixed** charts), not on raw labels.
**Design rule — read invariants, not labels.** Any checklist, acceptance predicate, or comparability claim that depends on representation choice (chart, unit, reference plane, or normalization route) **SHALL** be evaluated on **quotients by ≡_UNM** (or on explicitly **Normalization‑fixed** charts), not on raw labels.

*Minimal obligations:*
1) **Name the quotient or fix.** If a checklist predicates over a **normalization‑variant** property, it **MUST** name the **NormalizationFix** (including the referenced **UNM** and the relevant `NormalizationMethodInstance`(s), by reference) and thus the **≡_UNM** class.
2) **Declare NormalizationMethod class.** Every normalization used **MUST** name its method‑class token and validity window **as defined in A.19.UNM** (do not restate the class taxonomy here).
3) **Join/equality only on invariants.** Equality checks and joins across spaces **MUST** target invariant forms (the **≡_UNM** quotient or a declared **Normalization‑fixed** representation), never raw un‑fixed coordinates.

##### A.19:5.1.7 - Metric discipline & calibration (Normative)

Use the **weakest safe structure** required by the argument (pre‑order → semi‑metric → metric). 
* **If a distance overlay is declared**, any acceptance predicate or KPI defined over a CharacteristicSpace **SHALL be non‑expansive** (Lipschitz ≤ 1) w.r.t. the published `d` on the **declared domain** (raw coordinates or NCVs, as specified), or else state an explicit margin that absorbs any expansion.
* **If only an order overlay is declared**, any acceptance predicate/KPI **SHALL be isotone** w.r.t. the declared product order.

*Minimal obligations:*
1) **Publish the metric (if used).** If a distance overlay is used, the space **MUST** publish the distance function `d` (including any weights/parameters) and its declared domain of applicability.
2) **Bound expansion.** Any acceptance predicate/KPI that relies on `d` **MUST** be shown **non‑expansive** (Lipschitz ≤ 1); otherwise an explicit **expansion bound** and compensating **margin** **MUST** be stated.
3) **State error & commutation.** If a metric is used together with **NormalizationFix**, the specification **MUST** state (a) the maximum tolerated measurement/calibration error and (b) whether `d` **commutes** with the **NormalizationFix** (or provide a disclaimer and additional guard if it does not).

#### A.19:5.2 - State Spaces & Comparability

> **Memory hook:** _We compare **only what lies in the same space** (or is translated into a common space via a declared mapping), and we only certify a holon’s **state** based on **observable coordinates** in that space (using a defined checklist). Anything else is just storytelling._

To make state-space reasoning practical across different contexts and models, this section provides the key **operators and criteria** related to CharacteristicSpaces:

1.  **Space operations** – how to derive a **Subspace**, establish an **Embedding**, or form a **Product** of spaces. These enable us to restrict a space to fewer slots, to map one space into another (with unit conversions, etc.), or to combine spaces (e.g. for composite models).
    
2.  **Comparability regimes** – two allowable ways to compare states: (a) **coordinatewise**, which requires strict sameness of space and units; or (b) **normalization-based**, which uses declared transformations to reconcile differences. We define when each applies and how to apply it properly.
    
3.  **RSG integration** – how formal **state certification** (via checklists in a Role’s state graph) ties into the CharacteristicSpace: ensuring that whenever we declare a system “Ready” or “Degraded”, it’s based on snapshot coordinates in a space. We also outline how to push or pull state definitions along space embeddings (so different contexts can translate states).
    
4.  **Archetypal examples** – “worked mini-schemas” illustrating typical usage in complementary CN‑frames (Operational, Assurance, Alignment). These examples show minimal models mixing entity and relational slots, how data might be structured, and how cross-context alignment works in practice.
    

> **Terminology note:** We often denote a CharacteristicSpace abstractly as **CS**. Formally, one can describe a CS as a tuple `⟨I, basis⟩` where _I_ is the index set of slots and _basis_ is the set (or ordered list) of `slot_i` pairs. When a CharacteristicSpace is attached to a specific **Role** in a specific **Context** (see A.2, A.2.5), we may call it an **RCS** (Role CharacteristicSpace) – essentially the state space for that role’s state machine within that bounded context. Individual **states** of a role live in an RSG (RoleStateGraph, A.2.5), and a **StateAssertion** is a certified claim that at a given time window, the holon’s RCS coordinates satisfy the checklist for a particular state.

##### A.19:5.2.1 - CS Operators (notation-neutral, context-local)

To support model composition, we define operations on CharacteristicSpaces in a notation-independent way (so these can be implemented in any tooling or notation). All these operations are assumed to occur **within a single context** (within one `U.BoundedContext`) unless otherwise noted:

###### A.19:5.2.1.1 - Subspace – **Projection** `π_S : CS → CS|_S`.
Given a CharacteristicSpace CS with basis _I_ (slots) and a chosen subset of slot indices $S \subseteq I$, one can form the **subspace** $CS|_S$ which includes only the slots in _S_ and omits all others. The projection map `π_S` takes any state _x_ in the original space and **projects** it onto the coordinates indexed by _S_, effectively discarding the other coordinates. This operation is straightforward: if $S = \{i_1, i_2, … \}$, then $CS|_S$ has those slots, and any state in $CS|_S$ corresponds to a state in CS with the other coordinates ignored. 
**Properties:** Projection is **idempotent** (`π_S ∘ π_S = π_S`) and, if an order or other structure is defined solely on the subspace’s slots, `π_S` preserves that structure (e.g. it will reflect any order that depends only on slots in _S_).

###### A.19:5.2.1.2 Embedding – **Injection** `ι : CS₁ ↪ CS₂`.
An **embedding** is a structure-preserving **injection** from one space CS₁ into another space CS₂. It consists of two parts: (a) an injective **slot correspondence** from CS₁ to CS₂, and (b) (only where needed) cited **normalization instances** that make the correspondence semantically safe. Formally, let CS₁ have basis _I₁_ and CS₂ have _I₂_. An embedding declares an injective function _m: I₁ → I₂_ that identifies each slot of CS₁ with a corresponding slot in CS₂. 

For each slot _i ∈ I₁_ where the scale/unit differs from the target slot _m(i)_ in CS₂, the embedding **MUST cite** a `NormalizationMethodInstanceId` (per **A.19.UNM**) that re‑expresses values from `ValueSet(slot_i)` into `ValueSet(slot_{m(i)})` within the declared invariants and validity window. The embedding does **not** define normalization semantics; it only references the required instances.

Intuitively, an embedding says: “Any coordinate tuple from CS₁ can be interpreted as a coordinate tuple in CS₂, possibly after converting units or re‑scaling, and without losing any information except what the declared **NormalizationMethods** intentionally **coarse‑grain**.” If there is no loss at all (**NormalizationMethods** are identity or strict conversions), the embedding is essentially an inclusion of one space into a larger one; if there is some information loss (e.g., converting a fine‑grained scale to a coarse one), that loss is explicit in the **NormalizationMethodDescription**. **Locality:** 

Embeddings are defined **within a single `U.BoundedContext`** (i.e., both CS₁ and CS₂ are in the same context). Using an embedding across contexts requires an **Alignment Bridge** (see F.9) and **MUST** be declared via the relevant mechanism’s **A.6.1 Transport** clause (BridgeId + channel + `ReferencePlane(src,tgt)` + any `CL^plane`; no implicit crossings).  

**Normalization declaration duties (MUST):** Each cited `NormalizationMethodInstanceId` **MUST** satisfy the declaration/admissibility obligations owned by **A.19.UNM** (incl. method‑class token and validity window). If such normalization artifacts are used for gating or assurance, their evidence/calibration backing and waiver rules are governed by **C.16 (MM‑CHR)**. In other words, you cannot assume one context’s space fits into another’s without an explicit Bridge; any attempt to do so must treat it as a cross‑context alignment with potential loss.

###### A.19:5.2.1.3 Product – **Combination** `CS₁ ⊗ CS₂ = CS⊗`.
The **product** of two spaces CS₁ and CS₂ is a new space **CS⊗** that effectively contains all slots of CS₁ and all slots of CS₂. If CS₁ has index set _I₁_ and basis slots {slot₁…} and CS₂ has _I₂_, then $CS⊗$ has index set $I\_⊗ = I₁ ⊎ I₂$ (disjoint union) with each slot’s definition carried over from its original space. In practical terms, any state in the product space is a pair _(x₁, x₂)_ where _x₁_ is a state of CS₁ and _x₂_ is a state of CS₂ (assuming the two spaces pertain to possibly different aspects or roles). **Use cases:** Product spaces allow modeling **multi-role scenarios** or bundling an entity’s state with some environmental or contextual state. For example, one might take a space of internal capability metrics and ⊗ with a space of external conditions to form a combined space for “readiness under conditions.” **Note:** When combining scores or coordinates from a product space, one must be mindful of scale incommensurability. Cross‑slot aggregation **SHALL** proceed only via a declared **Γ‑fold** (B.1) and, where needed, explicitly declared **NormalizationMethods**; naïve arithmetic is forbidden. The product operation itself doesn’t perform any aggregation; it only sets the stage.

##### A.19:5.2.2 - Comparability of **States** (two admissible regimes)

A **state label** like "Ready", "Authorized", "Degraded", etc., in an RSG is an intensional category (defined by a checklist of conditions – see A.2.5). Determining whether the **states of two holons** are comparable (e.g. whether one is “better” or “worse” than the other in some multi-criteria sense) depends on **where** their state coordinates live and **how** we map those coordinates to a common basis. There are two admissible comparability regimes in FPF:

###### A.19:5.2.2.1 Coordinatewise comparability (`≼_coord`)

Two states can be compared **coordinatewise** only under strict conditions. Essentially, we require the states to be expressed in the **same measurement space**, with the **same units and scales**, and using the **same state definitions**. Formally, coordinatewise comparison is allowed **only if all of the following hold**:

-   **Same space.** The two holders’ state snapshots lie in the **exact same CharacteristicSpace** (and, if relevant, the same RCS attached to a Role in a given Context). It’s not enough that they have similarly named characteristics; they must share the actual defined space (same slots with same definitions).
    
-   **Scale congruence.** For each slot being compared, the scale type, unit, and polarity orientation are **identical**. For example, if comparing temperature readings, both must be on the same scale (say, °C on a ratio scale with “higher = hotter” orientation). No unit mismatches or differing interpretations can be present.
    
-   **State-definition congruence.** The states or status labels themselves must be defined in terms of the **same checklist criteria applied in the same space**. In other words, if we are comparing whether one system is “Ready” and another is “Ready”, both instances of “Ready” must derive from the same formal definition (same thresholds, same checklist logic) over those coordinates. If one context’s "Ready" means something different, you cannot assume they correspond.
    
When these conditions are met, one can define a **coordinatewise preorder** over states. Common patterns include:

- **Dominance:** For a given set of “higher is better” slots, we say state *x* **≼<sub>coord</sub>** state *y* if and only if for *every relevant slot a*, the coordinate $a(x) \le a(y)$ (**after orienting all slots to the declared polarity for that slot**). In other words, *y* is as good or better on all enforced criteria. This defines a Pareto-like ordering (often partial, not total).

-   **Threshold band inclusion:** If states are defined by meeting certain thresholds (e.g. State _Y_ means all metrics above specific levels), then we might say _x_ **≼<sub>coord</sub>** _y_ if _x_ meets every threshold that defines _y_’s state. For instance, if state _y_ = “High Performance” requires speed > 100 and accuracy > 90%, then _x_ is “no less than y” if _x_ also exceeds those thresholds.
    
By default, **no comparability** is assumed unless proven. If any of the above congruence conditions fails, one must **not** fall back to ad-hoc comparisons (like matching by name or normalizing without declaration). Either switch to a **normalization-based regime** or declare the states **incomparable**.

###### A.19:5.2.2.2 Normalization‑based comparability (`≼_normalization`)

When two state vectors do not meet the strict conditions for coordinatewise comparison (e.g. they come from different spaces, or the “same” Characteristics are measured on different scales/units), the only sanctioned way to compare them is: **normalize, then compare**.

Concretely: if we have state _x_ in CS₁ and state _y_ in CS₂, a normalization‑based comparison is permitted only if the model can cite a set of `NormalizationMethodInstanceId`(s) under a chosen **UNM** (per **A.19.UNM**) that lands the relevant coordinates of _x_ into CS₂ (or lands both into a declared common target space). The result is understood as **NCVs** (or an `≡_UNM` quotient class) per A.19.UNM.

**Comparability rule (normalize‑then‑compare).** We say _x_ **≼<sub>normalization</sub>** _y_ only if, after applying the cited normalization instances to produce a representation of _x_ in CS₂ (or a common target), the mapped state can be compared **coordinatewise** under `≼_coord`. In other words, we never compare raw _x_ and _y_; we compare *after landing in a common, well‑typed space*.

If the normalization crosses context boundaries (i.e., CS₁ and CS₂ are in different bounded contexts), then by FPF policy this mapping MUST be treated as a formal **Alignment Bridge** (F.9) with an associated **congruence‑loss (CL)** level and MUST be declared via the relevant mechanism’s **A.6.1 Transport** (BridgeId + channel + `ReferencePlane(src,tgt)`; no implicit crossings). In such cases, any conclusions drawn carry an assurance penalty per **B.3** (`Φ(CL)`).

**Auditability.** Each cited `NormalizationMethodInstanceId` used for comparison SHOULD be transparent via its referenced description/edition (per **A.19.UNM**). Evidence/calibration backing and waiver discipline are owned by **C.16 (MM‑CHR)**. The key here is that **no comparison is magic** – if values differ in scale or context, the normalization route and its limitations must be explicit.

> **Mnemonic:** _“Never compare before you **land** both points in the **same** well-typed space.”_ In other words, always map measurements to a common basis (same CharacteristicSpace and units) before attempting to say one state is ≥ or ≤ another. Directly comparing raw numbers from different scales or contexts is not allowed.

##### A.19:5.2.3 - RSG touch-points — **State certification via CS**

To connect the abstract concept of a **space of metrics** with the operational concept of **states** (like “Ready” or “Degraded”) in a Role’s lifecycle, we introduce a **certifier** function that evaluates state predicates against coordinates: 

certify(Role, Context): Snapshot( RCS[Role,Context], Window )  ──→  {StateAssertion}

This is a conceptual sketch: given a **snapshot** of all relevant coordinates for a Role (in its RCS) over some time window, the certifier produces a set of **StateAssertions** that are deemed true in that window. Each StateAssertion claims that the holder is in a particular state (e.g. “Ready”) during the window, backed by evidence.

**5.2.3.1 From CS snapshot to StateAssertion (design → run).** Each possible state _s_ in a Role’s RSG has an associated **Checklist** _(s)_ – a design-time artifact (see A.2.5 §8.1) which is a predicate defined over the RCS’s coordinates (and possibly other contextual observables). For example, a state “Degraded” might have a checklist like “\[temperature < 50 °C\] AND \[pressure > 5 bar\] for 10 minutes”. When the system is running, we take an **Observation** of the current coordinates (a snapshot of the RCS at a given time or over a time window) and evaluate the checklist. A **StateAssertion**(holder, _s_, Window) is then a record that the checklist for state _s_ has been satisfied by the observed data in that interval. In other words, it’s a certified evaluation that “state _s_ holds true for this holon at this time.” Only observable, measurable facts go into these predicates (no subjective judgments), and each assertion is traceable to the specific evidence (observations) that support it. The Role’s **Green-Gate Law** (A.2.5 §8.4) then says that a Role can proceed with an enactment (e.g. performing work) if and only if there is a **StateAssertion** showing the holon to be in an **enactable** state at that time. This connects measurement to action: you can only act if you have evidence you’re in the right state to act. 
**Evidence kind & window.** Every StateAssertion **SHALL** record `evidence_kind ∈ {observation, prediction}`, the **window** `[t_from, t_to]`, and, if `prediction`, the **horizon Δt** relative to the observation base. Use of `prediction` in enactment gates is permitted **only** under the DYN/TIME constraints captured in **CC‑A19.17–A19.18**; otherwise a **fresh observation** is required.

**5.2.3.2 Translating state definitions across embeddings.** If we have an **embedding** ι: RCS₁ ↪ RCS₂ (for example, RCS₁ is a subspace or a different version of RCS₂), we might want to reuse or compare state definitions between the two. There are two directions to consider:
* **Pulling a checklist** (reuse state criteria from a larger space in a smaller space): Given a checklist defined on RCS₂ (the larger or target space), we can **pull it back** via the normalization map **N** of the embedding to get a predicate on RCS₁. This derived checklist (**Checklist₂ ∘ N**) lets us apply the RCS₂’s state definition to a holon that only has RCS₁ measurements. This is useful when a consumer context wants to evaluate whether a producer (with fewer characteristics or different units) meets the consumer’s state definitions. Essentially, the consumer asks: “If I map the producer’s metrics into my space, does it satisfy my state criteria _s_?”
 * **Pushing an assertion** (honor a producer’s certified state in a larger space): If a holon has a StateAssertion for state s’ in RCS₁, can we treat it as evidence for state s in RCS₂? This is only valid under a strict condition: the checklist for state s in the larger space, when composed with the normalization mapping **N**, must logically imply the checklist s’ in the smaller space (or vice versa, depending on which state corresponds to which). In practice, this often requires a proof of refinement: that meeting state s (in big space) guarantees state s’ (in small space), or that state s’ (in small) is sufficient for state s (in big space) given the normalization translations. If that condition is met (or a policy waiver is granted in lieu of proof), then an assertion in the smaller space can be **pushed up** to count as an assertion in the larger space. This mechanism allows, for example, a component’s certified state to satisfy a system-level state requirement, provided the relationship is formally established.
  
**5.2.3.3 Certification interface (pointer).** Operational interface examples and minimal data stubs are **informative** and live in **A.19.CN** (“Certification Interface Example”). Pattern A.19 only constrains **conceptual** obligations; no storage/ID scheme is mandated here.
  
_(In summary, embeddings not only allow numeric comparability, but also allow **state definitions** and **certifications** to be systematically translated between contexts, ensuring consistency in how we interpret “Ready”, “Failed”, etc., across different models.)_

##### A.19:5.2.4 - Cross-context comparability & assurance hooks

When comparing states or metrics **across different bounded contexts** (different “context of meaning”), additional rules apply to maintain semantic integrity:

###### A.19:5.2.4.1 Direction & loss (Bridges).
Suppose we want to claim that “Holon X in Context B is in state _Ready_ as defined in Context A.” This requires an explicit **Alignment Bridge** declaration that maps the RCS of _(Role, Context B)_ to the RCS of _(Role, Context A)_ (or maps State B to State A). Such a Bridge (see F.9) will specify the correspondence of Characteristics (and the necessary **NormalizationMethods under UNM**) and a **congruence‑loss (CL)** level indicating how much fidelity is lost in translation. Critically, these Bridges are **one-directional** mappings unless explicitly made bidirectional. Just because we can interpret B’s state as an A-state does not mean we can go the other way without another mapping. The Bridge makes the mapping and any loss explicit. Without a declared Bridge, cross-context state comparisons or substitutions are not valid – there is no implicit global state space. The statement above, for instance, would only hold if we have something like “Bridge B→A (with defined NormalizationMethods) such that X@B can be viewed in A’s terms.” The **direction matters**: “B satisfies A’s Ready” does **not** imply the converse unless another bridge (A→B) is defined.
    
###### A.19:5.2.4.2 Confidence penalties for mapped comparisons.
Whenever a **normalization-based comparison** crosses Contexts (via a Bridge), assurance **MUST** apply the penalty **Φ(CL)** as **defined in B.3** (CL is **ordinal** there). For episteme‑specific compositions, **B.1.3** instantiates the same policy. This pattern does **not** restate the scale or Φ; it defers to **B.3**. For example, a safety argument that relies on a cross-context comparison might need to downgrade its certainty or include an extra safety margin.  This penalty **MUST** be declared as part of the assurance argument for the comparison (stating the Bridge used and its CL), so that the Φ(CL) discount can be reasoned and applied. No implementation‑level storage format or identifier is mandated by this pattern.
    
###### A.19:5.2.4.3 Declare “incomparable” when appropriate.
If for some critical Characteristic there is **no valid NormalizationMethod** to translate measurements between two contexts (e.g. the scale types are fundamentally different, or the measurement’s meaning doesn’t carry over), then the framework insists that we declare the states or metrics **incomparable** rather than attempting any fudge. No comparison should ever default to “close enough by name” or other heuristics. For instance, if one context measures “User Satisfaction” qualitatively and another quantitatively, and no monotonic mapping can be justified, one must simply say a user satisfaction state in context A cannot be compared to one in context B. Mark it incomparable and avoid any misleading conclusions. This rule guards against the natural temptation to compare things just because they have the same label or general intent, when in fact their measurement basis is different.

##### A.19:5.2.5 - Certification pipeline (Minimal, Normative)

Canonical evaluation chain (notation‑neutral):

`raw coords → Normalize (UNM.NormalizationMethodInstance) → Quotient / NormalizationFix → (optional) Indicatorization (via IndicatorChoicePolicy) → (optional) Order/Distance overlay → Evaluate Checklist → StateAssertion → Green‑Gate`

**Strict distinction.** Steps may be **co‑implemented**, but are **logically distinct** and **MUST** be referenceable in assertions (**NormalizationMethodInstance/UNM** name or formula, overlay kind). A gate is **invalid** if any required step lacks a current, valid referent (e.g., expired **NormalizationMethodInstance** edition).

#### A.19:5.3 - Operator library (notation‑neutral)

**Spaces:** `Sub` (projection), `Emb` (embedding), `Prod` (product), `Quot` (quotient by declared equivalence), `NormalizationFix` (fix to a named chart/edition).

**States/criteria transport:** `Pull` (pull checklist via embedding/NormalizationMethodInstance), `Push` (push assertion along embedding with proof/waiver), `Indicatorize` (apply **IndicatorChoicePolicy** to select Indicators), `Align_B` (cross‑context alignment via Bridge with CL), `Fold_Γ` (admissible aggregation/accumulation per B.1, with WLNK/MONO constraints).

**OP‑1 (Normative).** If `Align_B` is used in **gating**, the **Bridge used** and its **CL** **MUST** be declared in the assurance argument; the corresponding Φ(CL) penalty is applied per B.3. Silent cross‑context reuse is forbidden. (A.19 does not mandate any storage/ID scheme.)

### A.19:6 - Conformance Checklist (normative) — **CC‑A19**

**Formality anchors & operational segregation (normative).** A.19 aligns with **C.2.3 Unified Formality Characteristic (F)**. The legacy tier labels **T0/T1/T2 are deprecated**; speak **F** directly and treat operations separately (see **E.10** for registers).
— **F-Surface (recommended F ≥ F3).** Obligations are **declarability** and **arguability**: the author can **name** the CharacteristicSpace (basis/slots as *(Characteristic, Scale)* pairs), **state** the comparability regime (coordinatewise or normalization-based), and **express** a state’s checklist in observable coordinates. No storage formats, IDs, or operational provenance are required.
— **F-Predicates (F ≥ F4 when predicate-like).** As above, plus **explicit slot/NormalizationMethod names** and **stated overlays** (order/metric). When acceptance conditions are written as **typed predicates over coordinates**, declare **F ≥ F4**. Remains **notation-neutral** and **storage-agnostic**.
— **Operational bindings (not part of F).** When automatic checking/assurance is required, use **A.19.CN / C.16 / B.3** for IDs, validity windows, waivers, and logs. These raise **R/TA** in the trust calculus and **do not change F** unless the **expression form** changes (see C.2.3 orthogonality).

The following checklist summarizes the normative requirements introduced by Pattern A.19. An implementation or model **conforms** to A.19 if and only if all these conditions are met:

**Spaces & mappings**  
**CC‑A19.1.** Any defined **Subspace**, **Embedding**, or **Product** of CharacteristicSpaces **MUST** explicitly list the involved slots and their metadata (scale type, unit, polarity). No comparability or merging is allowed purely by matching names or assuming correspondence – it must be declared.  
**CC‑A19.2.** Every **Embedding** `ι: CS₁ ↦ CS₂` **MUST** cite a well‑defined `NormalizationMethodInstance` (per **A.19.UNM**) for each slot where `CS₁`’s slot differs in scale/unit from `CS₂`’s. The cited instances MUST satisfy the admissibility/declaration obligations owned by **A.19.UNM** (incl. monotonicity w.r.t. polarity, validity window, and method‑class token) and, when used for gating/assurance, MUST be evidence‑backed per **C.16**. (Identity suffices where scales are identical.)
**CC‑A19.2a.** **Scale‑class guard (by reference).** The scale‑class requirements for admissible normalizations are owned by **A.19.UNM** (and must remain CSLC‑consistent per **A.18**). This checklist item is satisfied by citing a `NormalizationMethodInstance` whose declared class token meets those requirements; do not restate the taxonomy here.

**Comparability**  
**CC‑A19.3.** **Coordinatewise comparability** (`≼_coord`) is **permitted only** when the states being compared share the **same CharacteristicSpace**, with **identical scale metadata** on each compared slot, and using the **same state definition criteria**. If these conditions aren’t fully satisfied, an implementation **MUST NOT** attempt direct coordinatewise comparison; it should either apply a **normalization‑based** method or report the items as **incomparable**.
**CC‑A19.3a.** Use of **Indicators** in any checklist/assertion **MUST** cite an **IndicatorChoicePolicy** (edition). Treating any **NCV** as an Indicator **without** a declared policy is **forbidden**.

**CC‑A19.4.** **Normalization‑based comparability** (`≼_normalization`) **MUST** be done by first normalizing all relevant coordinates of the source state into the target state’s space via declared admissible `NormalizationMethodInstance`(s) (see **A.19.UNM**), and **only then** comparing in that common space. In other words, two states can be compared under `≼_normalization` only by producing an image of one in the other’s space (`N(x)`) and using `≼_coord` on the result. No implicit or “on the fly” conversions are permitted.
**CC‑A19.5.** Any cross-context state comparison or substitution **MUST** cite a corresponding **Alignment Bridge** (F.9) with an explicit **CL (congruence-loss) level**. If such a Bridge is used in an assurance or decision-making context, the model **MUST** apply the appropriate confidence reduction (`Φ(CL)` penalty per B.3) to reflect the loss. Cross-context comparisons without a Bridge (i.e. assuming equivalence by name or convention) are **forbidden**.

**Certification & enactment**  
**CC‑A19.6.** Every **StateAssertion** **MUST** identify at least: the specific **state** being asserted (by name), the associated **checklist** or criteria set (by name), and the observation **window**. Furthermore, if the evaluation involved cross‑space mapping, it **MUST** **declare** which **NormalizationMethod(s)** or **Bridge** were applied. This ensures the decision can be examined in review; A.19 does not mandate any storage/ID scheme.

**CC‑A19.7.** The **Green-Gate enactment rule** (A.2.5) **SHALL** be enforced: a transformative action (`U.Work`) by a RoleAssignment is only allowed if there exists a **contemporaneous** StateAssertion showing the holon in a state that is marked **enactable**. If a StateAssertion has been translated from another context or space, it is valid for gating **only** if it was obtained through declared Embeddings/Bridges (no untracked inferences). This ensures no work is done under an unverified or mis-mapped state condition.  
**CC‑A19.8.** All **Checklist** definitions for states **MUST** be formulated in terms of **observable predicates** on the RCS (and known context events) – no hidden workflows or implicit time sequencing inside a checklist. A checklist should read like a static predicate (even if it’s about a duration of some condition). If temporal order or multi-step processes are involved in achieving a state, those must be modeled via explicit **Methods/Work** or via an aggregation logic (e.g., using the Γ (Gamma) patterns in B.1 for process sequencing), rather than being baked into the state’s definition. **Use of Indicators in any checklist MUST cite an IndicatorChoicePolicy edition; treating any NCV as an Indicator without policy is forbidden.**

**Anti‑drift**  
**CC‑A19.9.** If a **NormalizationMethod/UNM** or a **state checklist** is updated or calibrated differently in a new version, previous StateAssertions **MUST NOT** be retroactively modified. One must close out or mark the old assertions with their valid time window and start issuing new assertions under the updated definitions. In other words, historical records remain as they were (tied to the definitions at that time), and any change in criteria results in a _new context or version_ for future assertions. This prevents retroactive truth-changing and maintains integrity of historical data.  
**CC‑A19.10.** If any **critical slot** in a comparison lacks an **admissible** `NormalizationMethodInstanceId` (per **A.19.UNM**) to translate that slot between the relevant spaces (within the declared validity window), then the comparison **MUST** be reported as **incomparable**. The model must not attempt unofficial workarounds (e.g., name‑matching, silent dropping of the slot, or ad‑hoc coercions). This rule applies even if all other slots have admissible normalization instances, unless a policy explicitly accepts the loss via a declared Bridge with stated limitations.

**Quotients & Normalization‑fix (QNT)**
**CC‑A19.11.** Equality checks and joins across spaces **MUST** target invariant forms (on a **quotient** or declared **NormalizationFixed** chart), not raw coordinates.
**CC‑A19.12.** If a checklist predicates on a normalization‑variant property, it **MUST** name the **NormalizationFix** (which UNM.NormalizationMethod or chart is assumed).
**CC‑A19.13.** All used **method‑class tokens** for cited `NormalizationMethodInstanceId`(s) **MUST** be named in the bounded context’s glossary (per the taxonomy owned by **A.19.UNM**). Do not restate the class taxonomy here.

**Metric discipline & calibration (MET)**
**CC‑A19.14.** If a distance overlay is used, acceptance predicates/KPIs over a CS **SHALL** be **non‑expansive** (Lipschitz ≤ 1) w.r.t. the published `d` on the declared domain (raw coordinates or NCVs), or declare a compensating margin; otherwise they **SHALL** be isotone w.r.t. the declared product order.
**CC‑A19.15.** Any distance used in state/acceptance checks **MUST** carry max tolerated error and, where claimed, a **Lipschitz bound** for the **NormalizationMethod** composition in use.
**CC‑A19.16.** Cross‑CN‑frame inputs **SHALL** name the **normalization transform** and its **validity window**; expired transforms are invalid for gating unless waived explicitly.

**Dynamics & time (DYN/TIME)**
**CC‑A19.17.** Every temporal guard **MUST** specify the window `[t_from, t_to]` and `evidence_kind ∈ {observation, prediction}`; if `prediction` is used for gating, the conditions in **§ 5.2.3.1 (Evidence kind & window)** **MUST** hold.
**CC‑A19.18.** Any dynamics map `Φ_{Δt}` used in comparison/gating **MUST** be **non‑expansive** (Lipschitz ≤ 1) under the declared distance overlay **and** commute with **NormalizationFix**; otherwise **observation** is required.

**Certification (CERT)**
**CC‑A19.19.** StateAssertions **MUST** **state** the current **NormalizationMethod/UNM** and overlay artifacts used (by name or formula) and the `evidence_kind`; assertions relying on **expired** NormalizationMethod/UNM are **invalid** for gating unless an explicit **Waiver SpeechAct** is **declared** per policy. (A.19 imposes no requirement on IDs or storage.)
**CC‑A19.20.** The certification pipeline steps (**Normalize (UNM.NormalizationMethod); Quot/Fix_normalization; overlay; evaluate; assert**) are **logically distinct** and **MUST** be reconstructable in argument/review; collapsing steps without clearly stated referents violates A.19. (No specific persistence format is implied.)

**Operators (OP)**
**CC‑A19.21.** Use of `Align_B` in gating **MUST** **declare** the **Bridge** used and propagate **CL** into assurance (B.3). Cross‑context comparison without a Bridge is **forbidden**. (No requirement to store an ID is imposed by A.19.)

### A.19:7 - Anti‑patterns → safe rewrites

_The following are common modeling mistakes (“anti-patterns”) related to measurement spaces, and how to correct them:_

-   **“Same label ⇒ comparable.”**  
    ✗ _Assuming_ **Ready@contextA ≥ Ready@contextB** _just because both states are called "Ready"._  
  ✓ **Explicitly normalize and bridge contexts:** Define an Alignment **Bridge (B→A)** and appropriate **NormalizationMethods** for the underlying metrics. Then compare by first translating one state’s coordinates (compute **N(x)** as NCVs in the target space) and using `≼_coord` on the result.
    
-   **“Compare before landing.”**  
    ✗ Comparing values directly across different scales, e.g. _Drift\_A = 5°C vs Drift\_B = 5°F_ as if they were the same.  
  ✓ **Normalize to common units first:** e.g., apply the Fahrenheit‑to‑Celsius **NormalizationMethod** _m_(T_F) = (T_F − 32) × 5/9 to convert all data to °C, **then** compare the drift values. Always **normalize into one space** before comparing magnitudes.
    
-   **“Checklist = workflow.”**  
    ✗ Defining a state’s checklist with an implied sequence: _“State ‘Ready’ requires doing Step 1 then Step 2…”_  
    ✓ **Keep checklists declarative:** A **Checklist** should represent a state of the system (a condition) – essentially **state evidence** – not a sequence of actions. If order or process matters, model that explicitly via a **MethodDescription** or by using a **Γ** (Gamma) aggregator for process logic. In other words, state = “Ready” might require conditions A and B to be true (regardless of how you got there), whereas the procedure to get ready (do Step1 then Step2) should be a separate method or playbook.
    
-   **“Retro-fix past assertions.”**  
    ✗ Going back to edit or reinterpret old StateAssertions after changing a threshold or NormalizationMethod (e.g. “We updated the criteria, let’s ‘fix’ last quarter’s records to match”).  
    ✓ **Never alter historical assertions:** **Leave history as‑is.** If criteria change, issue new assertions under the new criteria going forward, and if needed, explicitly **version** the **NormalizationMethod/UNM** or checklist. Past assertions remain valid for the old version and their time; new ones apply henceforth. This ensures auditability and avoids erasing or rewriting what was true under earlier standards.

### A.19:End

## A.19.CN - CN‑frame (comparability & normalization)

> **Scope.** This CN‑frame Algebra & Normalization Discipline **extends A.19** by fixing the **governance Standard** for CN‑frames, defining a **conformance checklist** and **regression harness**, and providing **didactic one‑pagers** and **anti‑patterns** so teams can introduce CN‑frames without tool lock‑in. The mandatory pattern structure and authoring discipline from **Part E** (Style Guide, Tell‑Show‑Show, checklists, DRR, guard‑rails) are applied throughout.
>
> **Single‑owner boundary (cite, don’t duplicate).** A.19.CN owns the **CN‑frame governance surface** (`CN‑Spec`, registry, bridges, checklist/harness). It does **not** own any CHR‑mechanism **intensions**, term cards, or method taxonomies. Those are owned by the corresponding mechanism patterns (**A.19.UNM / A.19.UINDM / A.19.USCM / A.19.ULSAM / A.19.CPM / A.19.SelectorMechanism**)**. Evidence/backing is owned by **C.16**; legality gates are owned by **G.0**. Therefore A.19.CN specifies *where the references live*, *what must be cite‑able for audit*, and *how governance changes trigger regression* — not mechanism semantics.
>
> **Reader map (fast navigation).**
> - “What does `NormalizationMethodId/…InstanceId/≡_UNM/NormalizationFix` mean?” → **A.19.UNM**.
> - “What is an Indicator / `IndicatorChoicePolicy` and why NCV ≠ Indicator?” → **A.19.UINDM**.
> - “Why can we trust a normalization / where does calibration or evidence live?” → **C.16 (MM‑CHR)**.
> - “What is lawful to compare/aggregate / what is `MinimalEvidence`?” → **G.0 (CG‑Spec)**.

### A.19.CN:1 - Context

A.19 established a substrate‑neutral picture:

* a **CN‑frame** = *(Context‑local)* **CharacteristicSpace (CS)** + **chart** (coordinate patch + units) + a referenced **Normalization mechanism (UNM)** pinned from `CN‑Spec.normalization`. Any semantics of admissibility, invariants, and `≡_UNM` is owned by the UNM owner (see **A.19.UNM**);
* **operators** (subspace, product, pullback/pushforward) and **comparability** (coordinatewise vs **normalization‑based (normalize‑then‑compare)**);
* **RSG touch‑points**: role readiness (**RSG** states) are **certified** against CS via **checklists** over observable characteristics;
* **entity/relational mixtures** across CN‑frames via minimal schemas and bridges.

**Terminology guard.** *CN‑frame* is the **lens** (I); *CN‑Spec* is the **governance card** (S) that fixes admissible charts/normalization *references*/comparability/Γ‑fold for that lens **in one `U.BoundedContext`**; *CN‑Description* is the didactic surface (D) with worked examples and anti‑patterns. Mechanism‑level term cards (e.g., `NormalizationMethod`, `NormalizationMethodInstance`, `NCV`, `≡_UNM`, `IndicatorChoicePolicy`) are owned by the corresponding **A.19.<MechId>** patterns and are only **cited** here.

**Lexical guard (map/Map, by reference).** Follow the lexical discipline owned by **A.19.UNM**: avoid introducing new normalization tokens that use “map/Map/mapping” (because `…Map` is a Part‑G method‑type kind). In normalization contexts prefer **normalize / transform / re‑parameterize**. Legacy tokens (including retired κ‑notation) are handled via **alias docking** (F.18); A.19.CN applies this rule and does not redefine it.

A.19.CN makes this *operational and auditable*.

### A.19.CN:2 - Problem

Absent a governance layer, four failure modes recur:

1. **Chartless numbers.** Measures move between teams without units, reference states, or declared normalization → **illusory comparability**.
2. **Hidden normalization flips.** Re‑parameterisations (e.g., normalising by batch size) silently alter meaning; trend lines lie.
3. **CN‑frame sprawl.** Every initiative mints a new “dashboard dimension”; semantics diverge; assurance collapses.
4. **Un‑bridgeable reports.** Cross‑team roll‑ups average **incongruent** CN‑frames, violating the **weakest‑link (WLNK)** discipline from Γ and B.3.

### A.19.CN:3 - Forces

| Force                         | Tension we must balance                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| **Universality vs nuance**    | One Standard for robotics, safety, finance — yet leave each context’s idioms intact. |
| **Speed vs audit**            | Light ceremony for on‑ramp; hard guarantees for assurance and SoD.                   |
| **Local truth vs federation** | Keep CN‑frames meaning‑local; still enable **explicit** bridging across Contexts.          |
| **Minimalism vs safety**      | Few mandatory slots; enough structure to forbid silent normalization drift.                  |  


### A.19.CN:4 - Solution — **The CN‑Spec** (CN‑Spec) + **Registry** + **Bridges**

#### A.19.CN:4.1 - The **CN‑Spec** (comparability & normalization specification per CN‑frame, in one `U.BoundedContext`)

A **CN‑frame** is governed by a compact, notation‑free card:

```
CN‑Spec {
  name              : CN‑frameName                  // local to Context
  context           : U.BoundedContext              // edition/version included
  cs_basis          : [{
    slot_id         : <tech-token>,                 // stable slot id (basis name)
    characteristic  : <U.Characteristic>,          // per A.17 / A.18
    scale           : { type: nominal|ordinal|interval|ratio, unit?: <U.Unit>, bounds?: <… > },
    polarity        : up|down|target-range,        // comparison orientation
    // if needed: missingness?, admissible_domain? (MM‑CHR‑consistent metadata)
  }]
  chart             : { reference_state, coordinate_patch, measurement_protocol_ref }
  normalization     : {
   UNM_id?,                                      // reference to the UNM mechanism; canonical Intension: A.19.UNM
   methods: [NormalizationMethodId],              // UNM-owned tokens; semantics live in A.19.UNM
   instances?: [NormalizationMethodInstanceId],   // UNM-owned tokens; evidence/backing lives in C.16
   method_descriptions: [NormalizationMethodDescriptionRef], // refs only; semantics/corpus live with the semantic owner
   admissible_reparameterizations,                // UNM-owned declarations (opaque here; see A.19.UNM)
   invariants,                                    // UNM-owned invariant tokens (opaque here; see A.19.UNM)
   fix?: <NormalizationFixSpec>                   // UNM-owned fix spec (opaque here; see A.19.UNM)
   }
  comparability     : { mode ∈ {coordinatewise, normalization-based}, minimal_evidence }  // `minimal_evidence` is a gate reference (default: CG‑Spec.MinimalEvidence; see G.0/C.16)
  indicator_policy? : { IndicatorChoicePolicyRef, scope, edition }  // policy ref only; semantics owned by A.19.UINDM
  acceptance        : { checklist_for_admission, window, evidence_anchors } // gates RSG state checks
  aggregation       : { Γ_fold, WLNK/COMM/LOC/MONO choices, time_policy }   // fold tokens only; semantics owned by B.3/G.0 (and the folding mechanism card, if cited)
  alignment?        : { bridges_to_other_contexts, CL_levels, loss_notes }  // optional
  lifecycle         : { owner_role, DRR_links, deprecation_plan }
}
```

**Reading:** *A CN‑frame is a context‑local lens with declared characteristics and a chart to read them. `CN‑Spec` pins the **references and governance choices** needed to make admission, comparability, and safe roll‑ups auditable: the UNM reference for normalization‑based comparability, an optional `IndicatorChoicePolicyRef`, an explicit `Γ_fold`, and the admission checklist. Any mechanism semantics (e.g., what `≡_UNM` means, or what counts as an Indicator) is owned by the corresponding mechanism pattern and is only cited from here.*

**Ownership note.** CN‑Spec stores only the **governance surface** (references and declarations). The semantics and term cards for `NormalizationMethod*`, `≡_UNM`, `NCV`, `IndicatorChoicePolicy`, and any other CHR‑mechanism vocabulary are owned by the corresponding mechanism patterns (e.g., **A.19.UNM**, **A.19.UINDM**) and evidence backing lives in **C.16**. (Kernel reminder: per **A19‑CS‑5**, `U.CharacteristicSpace` carries no hidden normalizations or aggregations.) In A.6.1 terms, `UNM_id` points to a canonical **`U.Mechanism.Intension`** card; the CN‑Spec **references** that mechanism and does **not** introduce implicit **Transport**.

**L‑CN‑Spec‑NORM‑IDs (by reference).** When CN‑Spec (or its audit trail) needs stable normalization tokens, use **NormalizationMethodId**/**NormalizationMethodInstanceId** as specified by the UNM owner (A.19.UNM). Avoid generic “map” nouns and retired κ‑notation (see the **A.19.UNM** lexical guard); preserve legacy tokens only via **F.18 alias docking**. If you introduce reference‑typed fields, obey **A.6.5** (`*Ref` reserved for reference fields; `*Slot` reserved for SlotKinds).

#### A.19.CN:4.2 - **CN‑frame Registry** (per Context)

Each `U.BoundedContext` keeps a **CN‑frame Registry** (VR):

* **canonical names** and **editions**;
* **SoD hooks** (who can edit CN‑Spec, who can certify admission);
* **deprecation map** (what replaces what, when).

#### A.19.CN:4.3 - **Bridges** (across contexts)

Cross‑context reuse occurs **only** via explicit **Alignment Bridges** (F.9) between CN‑Specs:

```
Bridge CN‑frameA@Context1  →  CN‑frameB@Context2
  channel: {Scope|Kind}                 // F.9 (and A.6.1 Transport)
  planes: ReferencePlane(src,tgt)       // C.2.1 (must be recorded)
  CL: {3|2|1|0}
  CL_plane?: {3|2|1|0}                  // only when planes differ
  kept_characteristics: [… ]
  lost_characteristics: [… ]
  transform: {pullback | pushforward | re-scaling | re-binning | … }  // illustrative; use the operator vocabulary owned by A.19/F.9
  extra_guards: {additional evidence / reviewer role / waiver speech-act}
```

**CL policy (reference).** **CL levels and the penalty Φ(CL) are defined in B.3** (CL is **ordinal**; do not average). In A.6.1 terms, any cross‑context (or cross‑plane) reuse is declared **only** via a mechanism’s **Transport** clause: **name the BridgeId and channel** (`Scope|Kind`) and **record** `ReferencePlane(src,tgt)`; if planes differ, declare the `CL^plane` regime. **Transport is declarative** (it does not introduce a `U.Transfer` edge and does not restate CL ladders or Φ tables). When both scope and *describedEntity* change, apply the **two‑bridge rule** (Scope bridge + **KindBridge (CL^k)**). Penalties from scope/kind/plane **route to `R/R_eff` only** (never to **F/G**). This CN‑Spec may **add operational guards** per level (e.g., “extra reviewer at CL=1”, “waiver at CL=2”), but it **does not redefine** the scale or Φ. For episteme‑specific frames, see also **B.1.3**.

### A.19.CN:5 - Conformance Checklist (normative)

> **Pass these and your CN‑frames are fit for assurance and cross‑team composition.**

**CC‑A19.D1‑1 (Local scope).** Every CN‑frame **MUST** live inside a declared `U.BoundedContext` (with edition). Names are **local**; same label in another Context ≠ same CN‑frame.

**CC‑A19.D1‑2 (Units & polarity).** Each characteristic in `cs_basis` **MUST** declare **unit/scale** and **polarity** (↑ better / ↓ better / target range). No unlabeled magnitudes.

**CC‑A19.D1‑3 (Chart).** `chart` **MUST** name the **reference state**, **coordinate patch** and **measurement protocol** (`U.MethodDescription`) to make numbers reproducible.

**CC‑A19.D1‑4 (Normalization references, not redefinition).** `normalization` **MUST** (i) cite the UNM mechanism (`UNM_id?`) and (ii) provide the normalization references required by the UNM owner (methods / invariants / fix, and instances when used) so that any normalization‑based comparison is auditable. This pattern does not define what a “NormalizationMethod” is — it requires that CN‑Spec can point to the owner that does.

**CC‑A19.D1‑5 (Comparability mode).** `comparability.mode` **MUST** be either **coordinatewise** (same chart & units) or **normalization‑based** (“normalize‑then‑compare” via the declared **UNM**). Mixed/implicit modes are prohibited. The semantics of `≡_UNM` (and what counts as “same class”) is owned by the UNM mechanism card (A.19.UNM); CN‑Spec only pins the references needed to audit the choice.

**CC‑A19.D1‑6 (Admission checklist).** `acceptance.checklist_for_admission` **MUST** be observable and time‑bounded; each datum admitted to the CN‑frame **SHALL** cite a **StateAssertion** or equivalent `U.Evaluation`.

**CC‑A19.D1‑7 (Aggregation discipline).** `aggregation.Γ_fold` **MUST** specify WLNK/COMM/LOC/MONO choices and the **time policy** (e.g., average of rates vs integral of counts). **No free‑hand averages.** The legality/semantics of folding is owned by **B.3/G.0** (and, when a folding mechanism is cited, by its mechanism owner); CN‑Spec only stores the governance pins.

**CC‑A19.D1‑8 (Bridge‑only reuse).** Cross‑context consumption **MUST** cite a **Bridge** with: (i) `channel ∈ {Scope|Kind}`, (ii) recorded `ReferencePlane(src,tgt)`, (iii) CL (and `CL^plane` when planes differ), and (iv) **loss notes**; coordinate‑by‑name without a Bridge **fails**. If the data participate in **gating/assurance**, apply **Φ(CL) per B.3**; this CN‑Spec does not restate Φ.

**CC‑A19.D1‑9 (SoD & roles).** Editing CN‑Spec and admitting data **MUST** be performed by **different** roles (⊥ enforced): `CN‑frameStewardRole ⊥ CN‑frameCertifierRole` inside the same context.

**CC‑A19.D1‑10 (Lifecycle & DRR).** Every CN‑Spec **MUST** carry an **owner role**, a **deprecation plan**, and links to **DRR** entries for rationale and changes (Part E.9).

**CC‑A19.D1‑11 (Anchors & lanes for comparability).** Any **admission** into a CN‑frame that is later **used for comparison/aggregation** **SHALL** cite the corresponding **A.10 EvidenceRole** anchors for each characteristic, with **assuranceUse lane** tags {TA, VA, LA} and **validity windows** (where applicable), so that the **SCR** can report lane‑separated contributions and freshness (B.3). Absence of anchors for a required characteristic renders items **incomparable**.

**CC‑A19.D1‑12 (Notation independence).** CN‑Spec content **MUST NOT** depend on a tool or file format; semantics precede notation (E.5.2 Notational Independence).

**CC‑A19.D1‑13 (Lexical guard‑rails).** characteristic names and role labels **MUST** follow the Part E lexical discipline (registers, twin labels; no overloaded “process/service/function”).

### A.19.CN:6 - Consequences (informative)

| Benefit                           | Why it matters                                                                                                        |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Auditable comparability**       | Chart + declared normalization (UNM + NormalizationMethods) make “same number” meaningful; silent re‑basings become explicit, reviewable choices.                   |
| **Safe roll‑ups**                 | Γ‑folds with WLNK/COMM/LOC/MONO stop optimistic averaging and preserve invariants.                                    |
| **Pluralism without incoherence** | Bridges with CL and loss notes allow federation without pretending to global sameness.                                |
| **RSG‑ready**                     | Admission checklists let **RSG** states reference **CN‑frame‑backed** facts (e.g., *Ready* requires characteristics within bounds). |

### A.19.CN:7 - Rationale (informative)

The CN‑Spec aligns A.19.CN with **Part E**: it packages Tell‑Show‑Show, Conformance Checklists, and DRR‑backed change, while honouring **DevOps Lexical Firewall**, **Unidirectional Dependency**, and **Notational Independence** so that semantics never depend on tooling.  It also operationalises B.3 **Trust & Assurance** by making CL penalties and WLNK folds first‑class.


### A.19.CN:8 - Archetypal Grounding *(Tell‑Show‑Show)*

> **Same slots, three arenas; no tooling implied.** The examples below use plain-language normalization descriptions as placeholders; any normative use must cite UNM-owned ids/refs (A.19.UNM) and evidence pins (C.16), not invent new terminology here.

#### A.19.CN:8.1 - **Industrial line** — *Weld‑quality CN‑frame* (`AssemblyLine_2026`)

* `cs_basis`: *BeadWidth\[mm] (target 6.0±0.2)*, *Porosity\[ppm] (↓)*, *SeamRate\[1/min] (↑ until limit)*
* `chart`: reference jig, fixture ID, torch type; `MethodDescription#Weld_MIG_v3`
* `normalization`: affine rescale on gray‑level calibration → invariant = physical porosity
* `comparability`: **normalization‑based (UNM)** (calibration tables applied)
* `aggregation`: WLNK on quality (min‑bound), COMM on counts, time = per‑shift histograms
* **RSG hook**: `WelderRole.Ready` requires *Porosity ≤ 500 ppm* & *BeadWidth within ±0.2 mm* admitted by this CN‑frame.

#### A.19.CN:8.2 - **Software/SRE line** — *Latency CN‑frame* (`SRE_Prod_Cluster_EU_2026`)

* `cs_basis`: *P50Latency\[ms] (↓)*, *P99Latency\[ms] (↓)*, *Load\[req/s]*
* `chart`: client vantage, trace sampler v4; `MethodDescription#HTTP_probe_v4`
* `normalization`: monotone time‑warp compensation for collector skew; invariant = percentile order
* `comparability`: **normalization‑based (UNM)** with declared normalization
* `aggregation`: MONO on latency (max of mins), WLNK across services
* **RSG hook**: `DeployerRole.Active` gated if **P99** < declared SLO over the admission window.

#### A.19.CN:8.3 - **Clinical/episteme line** — *Trial‑outcome CN‑frame* (`Cardio_2026`)

* cs_basis:
  - slot_id: ΔBP
    characteristic: BloodPressureChange
    scale: { type: ratio, unit: mmHg }
    polarity: down
  - slot_id: AdverseRate
    characteristic: AdverseEventRate
    scale: { type: ratio, unit: "%" }
    polarity: down
  - slot_id: Age
    characteristic: Age
    scale: { type: ratio, unit: years }
    polarity: neutral
* `chart`: cohort definition; `MethodDescription#TrialProtocol_v5`
* `normalization`: case‑mix adjustment (propensity score); invariant = adjusted ΔBP
* `comparability`: **normalization‑based (UNM)** (post‑adjustment)
* `aggregation`: LOC on subcohorts; WLNK on safety outcomes
* **RSG hook**: `EvidenceRole.Validated` admission requires CN‑frame acceptance; **Assurance** pulls CL from any Bridge used.

#### A.19.CN:8.4 - Worked mini-schemas (entity/relational mixtures across CN‑frames, informative)

To illustrate how CharacteristicSpace is used in practice, below are simplified schema snippets for three typical **CN‑frames**: an **Operations** view (run-time state and action gating), an **Assurance** view (evidence and cross-context comparison), and an **Alignment** view (design-time consistency across contexts). These examples mix entity-based and relational Characteristics and demonstrate how normalization and bridge *references* may appear in a model.

**Didactic-only note (no data governance).** The “schema/table” shapes below are purely explanatory: they show which **references must be cite-able** for audit and reproducibility. They are **not** storage requirements, do not prescribe file formats, and do not define the semantics of `NormalizationMethod*` tokens (see A.19.UNM / C.16).

##### A.19.CN:8.4.1 - Operations CN‑frame — Run-time gating & enactment

_Entity graph view:_

Holder (System) ── playsRoleOf ──> Role@Context ── has ──> RCS (slots…)
RSG (Role@Context) ── owns ──> State (◉ status)
Checklist (of State) ── testedBy ──> Evaluation ── yields ──> StateAssertion
Work ── performedBy ──> RoleAssignment
Work ── isExecutionOf ──> MethodDescription

In the above, a **Holder** (a system instance) plays a **Role** in some Context, which has an attached **RCS** (a set of slots defining its characteristic space). That Role’s **RSG** owns various possible **State** entries (each state could be, e.g., Ready, Waiting, Degraded, etc.). Each State has a **Checklist** which is **tested by** an Evaluation process, resulting in a **StateAssertion** (pass/fail) at runtime. Meanwhile, **Work** instances (concrete operations) are performed by the RoleAssignment and correspond to some MethodDescription (procedure). The “gate” for Work is that a StateAssertion for an enactable state must exist.

_Relational stub:_ (illustrating how information might be recorded)

| Table | Key Columns (essential) |
| --- | --- |
| **ROLE\_ASSIGNMENT** | `RA_ID` (PK); `HOLDER_ID`; `ROLE_ID`; `CONTEXT_ID`; `WINDOW_FROM`, `WINDOW_TO` |
| **RCS\_SNAPSHOT** | `SNAP_ID` (PK); `RA_ID` (FK to ROLE\_ASSIGNMENT); `WINDOW_FROM`, `WINDOW_TO`; `CHAR_ID`; `VALUE`; `UNIT`; `SCALE_TYPE` |
| **RSG\_STATE** | `STATE_ID` (PK); `ROLE_ID`; `CONTEXT_ID`; `NAME`; `ENACTABLE` (bool) |
| **CHECKLIST** | `CHK_ID` (PK); `STATE_ID` (FK to RSG\_STATE); `PREDICATE_TYPE`; `PREDICATE_SPEC` |
| **STATE\_ASSERTION** | `SA_ID` (PK); `RA_ID` (FK); `STATE_ID` (FK); `CHK_ID` (FK); `WINDOW_FROM`, `WINDOW_TO`; `VERDICT` (pass/fail); `NORMALIZATION_INSTANCE_ID`?; `BRIDGE_ID`? |  
| **WORK** | `WORK_ID` (PK); `RA_ID` (FK); `METHODDESC_ID` (FK to MethodDescription); `WINDOW_FROM`, `WINDOW_TO`; _(other fields like results or references)_ |

In this schema: an RCS snapshot table might log individual coordinate values (`VALUE`) for each Characteristic (`CHAR_ID`) in a given RoleAssignment, with their units and scale type noted (to ensure we know what the number means). The StateAssertion ties a RoleAssignment to a state checklist and says whether it passed, including references to any **NormalizationMethodInstance** or **Bridge** if cross-context or cross-scale comparisons were involved. The gate logic for enactment can then be a query like: “Is Work W admissible now?” – which joins through ROLE\_ASSIGNMENT to find the latest StateAssertion for that RA where `ENACTABLE=true` and `VERDICT=pass`.

##### A.19.CN:8.4.2 - Assurance CN‑frame — Evidence freshness & mapped comparisons

_Entity graph view:_

NormalizationMethodInstance ── appliesTo ──> Characteristic   (each instance is a scale‑appropriate, monotone transform within UNM)
Bridge (ContextB → ContextA)   (Alignment Bridge between contexts, with CL and loss notes)
StateAssertion ── uses ──> {NormalizationMethodInstance, Bridge}   (if a state comparison crossed contexts)

This view highlights that in the assurance context, we keep track of how we mapped or compared states:

* A **NormalizationMethodInstance** reference records that an admitted comparison/assertion relied on a declared normalization instance. The admissibility conditions, monotonicity constraints and evidence semantics are owned by **A.19.UNM** and **C.16**.
* A **Bridge** between Context B and Context A (for corresponding roles or states) carries a CL rating and possibly notes on what is “lost in translation.”
* A **StateAssertion** may **use** a NormalizationMethodInstance or a Bridge, meaning that assertion was reached by translating data via that instance or comparing across that bridge.

_Relational stub:_

| Table                | Key Columns (essential)                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **NORMALIZATION\_METHOD** | `NORMALIZATION_METHOD_ID` (PK); `KIND` (token; see A.19.UNM); `DESCRIPTION_REF` |
| **NORMALIZATION\_INSTANCE** | `NORMALIZATION_INSTANCE_ID` (PK); `NORMALIZATION_METHOD_ID` (FK); `SRC_CHAR_ID`; `TGT_CHAR_ID`; `FORMULA_SPEC|LUT_REF` (illustrative); `VALIDITY_WINDOW` (illustrative); `EVIDENCE_REF` (pin/ref; see C.16) |
| **BRIDGE**           | `BRIDGE_ID` (PK); `FROM_ROLE@CTX`; `TO_ROLE@CTX`; `CL` (congruence-loss level, e.g. 0–3); `NOTES` (description of losses/adjustments) |
| **ASSURANCE\_EVENT** | `AE_ID` (PK); `SA_ID` (FK to StateAssertion); `EFFECT` (enum: penalty\_applied, evidence\_refreshed, etc.); `DETAILS`                 |

In this stub, **NORMALIZATION\_INSTANCE** records a mapping instance that has to be accounted for when reconstructing an assertion or comparison. The exact meaning of `FORMULA_SPEC`/`VALIDITY_WINDOW`/evidence pins is owned by the UNM and evidence patterns (A.19.UNM / C.16); the point here is that the instance is **referenceable** so audits can follow it. The Bridge table enumerates official Bridges between contexts (for example, bridging a “Ready” state in an engineering context to “Ready” in an operations context, with CL indicating how fully comparable they are). An ASSURANCE\_EVENT log could record when a penalty was applied due to a low-CL Bridge or when an assertion was refreshed or invalidated due to new evidence or time lapse.

##### A.19.CN:8.4.3 Alignment CN‑frame — Design-time reuse of states across Contexts

_Entity graph view:_

Checklist(ContextA.State)   ← pull(N) —   Checklist’(ContextB.State’)   (pull a checklist via **NormalizationMethodInstance** N)
Refinement π : RSG(Role' ≤ Role)   (RSG refinement mapping, e.g. Role' is a subtype of Role)

This view covers how _design-time_ alignment happens:

-   A **Checklist’** for a state in Context B can be **pulled** via a **NormalizationMethodInstance** into Context A to become a derived Checklist for a state in Context A. This is effectively what we described in the pull operation: using another context’s criteria in your own space.
    
-   A **Refinement π** is shown between RSGs indicating Role’ is a specialized role of Role (e.g. a sub-role or a scenario-specific role) and how their states relate (Role’ might have extra states or more granular distinctions). This refinement should maintain that for each state in Role’ that maps to a state in Role, the entails/implication relation holds for enactability.
    

_Relational stub:_ (illustrating how information might be recorded)

| Table               | Key Columns                                                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RSG\_REFINEMENT** | `MAP_ID` (PK); `ROLEPRIME_ID` (FK to Role' in Context B); `ROLE_ID` (FK to Role in Context A); `STATEPRIME_ID` (FK to state in Role' RSG); `STATE_ID` (FK to state in Role RSG); `ENTAILS` (bool) |
| **CHECKLIST\_PULL** | `PULL_ID` (PK); `SRC_STATE_ID`; `TGT_STATE_ID`; `NORMALIZATION_INSTANCE_ID` (FK to NormalizationMethodInstance used); `VERSION`? /\* and perhaps timestamp \*/                                     |

In this stub, RSG\_REFINEMENT maps states of a sub-role to states of a super-role, with an `ENTAILS` flag indicating if being in the sub-state guarantees being in the super-state. **Every refinement mapping should ensure at least one enactable state in the sub-role corresponds to an enactable state in the super-role** (or else the sub-role would allow something the super-role doesn’t – that’s an alignment lint check). The CHECKLIST\_PULL table records that a state from one context has had its checklist pulled into another context via a **NormalizationMethodInstance** (identified by `NORMALIZATION_INSTANCE_ID`). This is a design artifact saying “State X in context A is defined by applying normalization instance N to State Y in context B’s criteria.” A version or validity field might ensure we know which edition of the checklist or normalization instance was used.


### A.19.CN:9 - Anti‑patterns (and the fix)

| Anti‑pattern            | Symptom                                   | Why it hurts                 | Fix (CN‑Spec slot)                           |
| ----------------------- | ----------------------------------------- | ---------------------------- | --------------------------------------- |
| **Chartless number**    | “Latency = 120”                           | No unit/vantage → untestable | Fill `cs_basis` + `chart`                          |
| **Normalization smuggling**     | Quiet “per‑unit” normalisation mid‑stream | Trend reversal               | Declare UNM normalization references (`NormalizationMethodId` / `NormalizationMethodInstanceId`) + named invariants (see A.19.UNM)        |
| **Bridge‑by‑name**      | Reusing labels across Contexts               | False comparability          | Author **Bridge** with CL + loss        |
| **Free‑hand averaging** | Arithmetic mean on bounded risks          | Violates WLNK                | Declare `Γ_fold` with WLNK              |
| **CN‑frame sprawl**        | Ten nearly‑identical CN‑frames               | Cognitive debt               | Use Registry + DRR; prefer reuse        |
| **Role conflation**     | Same person edits CN‑Spec & certifies data     | SoD breach                   | Enforce `CN‑frameSteward ⊥ CN‑frameCertifier` |

### A.19.CN:10 - Didactic quick cards (one‑liners teams reuse)

1. **Numbers travel with their Context.** Always cite `Context@Edition`.
2. **If the normalization is not declared, the trend is fiction.**
3. **WLNK beats wishful means.** Use weakest‑link folds for safety.
4. **Admit → Assert → Act.** (CN‑frame admission → RSG StateAssertion → Method step).
5. **Bridge or bust.** Cross‑context = Bridge with CL and loss notes.
6. **Steward writes, Certifier admits.** (SoD by design.)
7. **Charts are recipes.** Name the `MethodDescription` that made the number.
8. **Deprecate in the open.** CN‑frame cards carry DRR & retirement plans.
9. **Keep characteristics few, meanings sharp.** Prefer ≤ 7 characteristics per CN‑frame.
10. **No tooling names in Core.** Semantics first; notation later.
11. **Use method/instance IDs; avoid generic “map” nouns.** Prefer `NormalizationMethodId`/`NormalizationMethodInstanceId` (see the **A.19.UNM** lexical guard).

### A.19.CN:11 - SCR / RSCR Harness (acceptance & regression)

> **These are concept‑level checks; notation‑agnostic.**

#### A.19.CN:11.1 - **SCR — Acceptance (first introduction)**

* **SCR‑A19.4‑S01 (Completeness).** **CN‑Spec has **all** mandatory slots; `cs_basis` include **unit/scale/polarity**; `chart` references a `MethodDescription`.
* **SCR‑A19.4‑S02 (Normalization clarity).** `normalization` cites the UNM mechanism (`UNM_id?`) and provides the normalization references required by the UNM owner (methods / invariants / fix, and instances when used). If instances are referenced in assurance logs, their evidence/backing and validity constraints are handled by the owning evidence pattern (C.16), not by A.19.CN.
* **SCR‑A19.4‑S03 (Comparability test).** Provide one worked example showing **coordinatewise** or **normalization‑based** comparison end‑to‑end (with Evidence Graph Ref).
* **SCR‑A19.4‑S04 (Γ‑fold audit).** Aggregation rule spells out WLNK/COMM/LOC/MONO choices; reviewer reconstructs result on a toy set.
* **SCR‑A19.4‑S05 (SoD).** Distinct `RoleAssignments` for `CN‑frameStewardRole` and `CN‑frameCertifierRole` exist; windows do not overlap.
* **SCR‑A19.4‑S06 (describedEntity & anchors surfaced).** For each CN‑Spec characteristic used in the worked example, cite the corresponding CHR Characteristic name and the evidence anchor(s) (A.10) that make the reading observable in this Context.

#### A.19.CN:11.2 - **RSCR — Regression (on change)**

* **RSCR‑A19.4‑R01 (UNM edit).** On changing `normalization` (UNM/NormalizationMethod), flag **all** downstream Bridges for CL re‑assessment; re‑run example comparisons.
* **RSCR‑A19.4‑R02 (Slot surgery/Basis surgery).** Adding/removing/renaming slot/basis requires a **new edition**; old data remain valid **for their edition**.
* **RSCR‑A19.4‑R03 (Chart drift).** Updating measurement protocol bumps edition; **historic Work** keeps old edition link.
* **RSCR‑A19.4‑R04 (Fold change).** Any change to `Γ_fold` invalidates cached roll‑ups; re‑compute or mark as superseded.
* **RSCR‑A19.4‑R05 (Bridge health).** After either side’s edition change, **re‑validate** Bridge CL and loss notes before accepting Cross‑context data.
* **RSCR‑A19.4‑R06 (Deprecation rule).** On deprecating a CN‑frame, Registry lists its successor; bridges re‑targeted or retired.

### A.19.CN:12 - Interaction summary (wiring to the rest of the kernel)

* **A.2 / A.2.5 (Roles / RSG).** RSG **checklists** quote **CN‑Spec.acceptance**; enactment gates rely on **admitted** CN‑frame data.
* **B.1 (Γ‑algebra).** CN‑Spec’s `Γ_fold` instantiates Γ\_ctx/Γ\_time/WLNK/MONO choices explicitly.
* **B.3 (Assurance).** Bridge CL enters the **R** term; WLNK protects safety roll‑ups.
* **C.6 / C.7 (LOG‑CAL / CHR‑CAL).** Units, scales, and measurement templates come from CHR; proofs about folds live in LOG‑CAL.

### A.19.CN:13 - Minimal CN‑Spec template (copy/paste, informational)

**Template note (refs-only).** This template shows *slot placement* for governance. Token semantics for normalization belong to the UNM owner (A.19.UNM); indicatorization semantics belong to the indicatorization owner (e.g., A.19.UINDM); evidence/backing semantics belong to C.16; legality/evidence gates belong to G.0.

```
CN‑frame: <Name>      Context: <Context/Edition>
characteristics:
  - <CharacteristicName> : <Unit/Scale>  [Polarity: up|down|target-range]
Chart:
  reference_state: <text>
  coordinate_patch: <domain/subset>
  measurement_protocol_ref: <MethodDescriptionId>
Normalization:
  UNM: <UNMId?>
  methods: [<NormalizationMethodId>… ]
  method_descriptions: [<NormalizationMethodDescriptionRef>… ]
  invariants: [<property>… ]           # what ≡_UNM preserves (token semantics: see A.19.UNM)
  fix?: <NormalizationFixSpec>          # canonical representative of the ≡_UNM class (token semantics: see A.19.UNM)
Indicators (optional):
  policy_ref: <IndicatorChoicePolicyRef>
  resulting_indicators: [<IndicatorId>… ] // selection is policy‑defined; NCVs alone do not make an Indicator (see A.19.UINDM)
Comparability:
  mode: coordinatewise | normalization-based
  minimal_evidence: <what must be observed to compare>  # legality/evidence gate surface (see G.0/C.16)
Aggregation:
  fold: <Γ_fold expr>   time_policy: <window, statistic>
  WLNK/COMM/LOC/MONO: <declared choices>
Acceptance:
  checklist: [<observable criterion>… ]
  window: <ISO 8601 interval>
  evidence_anchors: [<Observation/Evaluation ids>… ]
Alignment (optional):
  bridges: [<BridgeId, CL, kept/lost characteristics, extra guards>… ]
Lifecycle:
  owner_role: <Role>
  DRR_links: [<DRR ids>… ]
  deprecation_plan: <short note>
```

**Implementation note (non‑normative): conceptual audit fields.** (For implementation completeness only; not part of the CN‑Spec normative surface.) The goal is *auditability*: any implementation should be able to cite the relevant refs (CN‑Spec edition, evidence anchors, UNM instance refs, Bridge ids) when producing a `StateAssertion`. The normative semantics of normalization and evidence/backing are owned by the corresponding mechanism and evidence patterns (e.g., A.19.UNM and C.16). A.19.CN does not prescribe storage formats.

### A.19.CN:Close

A.19.CN gives A.19 some **teeth**: a *CN‑Spec* you can put on one page, a **Registry** that stops sprawl, **Bridges** that carry explicit loss, and a **checklist + harness** that make comparability **auditable**. It obeys the **mandatory pattern structure** of Part E (style, checklists, DRR, guard‑rails) while remaining tool‑agnostic and context‑local.

### A.19.CN:End

## A.19.CHR - CHRMechanismSuite

> **Type:** Architectural (A)  
> **Status:** Stable

**PatternId:** A.19.CHR
**Name:** `CHRMechanismSuite`
**Pattern class:** specialization of **A.6.7** (`MechSuiteDescription`) for the CHR (characterization) core.

**Introduces / fixes canonical objects and kinds**

* **`CHRMechanismSuiteDescription`** (object; kind: `MechSuiteDescription`): the canonical CHR suite description instance (cited downstream via `MechSuiteDescriptionRef`, edition-addressable when used as a reproducibility baseline).
* **`CHRMechanismSuiteSlotFillingsPlanItem`** (kind; `⊑ SlotFillingsPlanItem`): a suite-specialized plan item kind used as the **planned baseline** for P2W integration of the CHR suite (selection → WorkPlanning → WorkEnactment).

**Depends on**

* A.6.7 `MechSuiteDescription` (Kernel)
* A.15.3 `SlotFillingsPlanItem` (WorkPlanning)
* A.6.1 `U.Mechanism.Intension` (mechanism norm-form)
* A.6.5 slot discipline (`SlotSpec := ⟨SlotKind, ValueKind, refMode⟩`; `SlotIndex` is a projection)
* A.19 `CN‑Spec` (contract surface)
* G.0 `CG‑Spec` (legality gate for numeric operations)
* E.TGA / E.18 (P2W + crossings + UTS/Path pins)
* E.10 lexical/ontological rules (strict distinction, suffix discipline, minimal specificity)
* E.19 conformance style (checklist obligations)

**Non-goals**

* No “data governance”, no implementation tooling, no “machine readability” requirements.
* Not a packaging/bundling mechanism (that remains **G.10**).
* Not a replacement for `MechFamilyDescription` (that remains “many implementations of **one** mechanism intension”).

### A.19.CHR:1 - Problem frame

Part G (and adjacent patterns that operate on measurable slot coordinates, e.g. Q-bundles) repeatedly needs the same *lawful characterization core*:
normalization, indicatorization, scoring, lawful aggregation, comparison, and selection under explicit legality constraints.

In the current corpus, many G patterns interleave:

* universal CHR legality mechanics (CN‑Spec/CG‑Spec citation, set-return semantics, tri-state uncertainty handling, penalties routing),
* CG-frame and crossing obligations (ReferencePlane, Bridge-only transport visibility, edition-sensitive pins), and
* discipline/method/generator specifics (method families, candidate/criteria emitters, packaging concerns),

inside one construct. This mixing makes it hard to universalize Part G, causes drift in defaults and guard semantics, and encourages “hidden tails”
(implicit UNM/UINDM/ULSAM or implicit slot filling outside WorkPlanning).

At the same time, the P2W split requires a uniform *planned baseline* object:
selection can choose refs/policies, WorkPlanning can record planned slot fillings, and WorkEnactment can witness `FinalizeLaunchValues`.
Without a canonical planned-baseline artifact, teams tend to “smuggle” launch values into planning prose or into mechanism descriptions,
which breaks auditability and makes crossings and edition sensitivity non-obvious.

### A.19.CHR:2 - Problem

This pattern applies when a workflow (especially in Part G) needs lawful characterization over measurable slots/coordinates (e.g., in Q‑bundles), including normalization, indicatorization, scoring, aggregation, comparison, and selection.

### A.19.CHR:3 - Forces

* **No implicit crossings.** Any cross‑context / cross‑plane reuse must be expressed via Bridge-only Transport and visible crossing surfaces (UTS/Path pins).
* **CN‑Spec / CG‑Spec must remain the contract center.** Mechanisms cite them; mechanisms do not duplicate them.
* **Strict separation of layers.** Universal CHR core vs discipline/method specializations vs generators vs packaging.
* **SlotKind invariance.** Specialization ladders must preserve SlotKind meaning and only refine ValueKind / strengthen guards/laws.
* **No silent scalarization / totalization.** Partial orders must remain set‑valued; any numeric summary is report‑only unless explicitly declared as a lawful comparator/policy.
* **P2W split.** Planned slot filling belongs to WorkPlanning; launch values belong to WorkEnactment.

### A.19.CHR:4 - Solution

This pattern defines a single, canonical **CHR mechanism suite** as a *description object* (not a mechanism, not a pack), so that:

1. the CHR core is reusable across all Part‑G patterns (not only G.5),
2. legality is centralized via **contract pins** (`CN‑Spec`, `CG‑Spec`) and **Transport discipline**,
3. P2W integration is made explicit by requiring a standard **planned slot fillings** artifact in `WorkPlanning`, while keeping **FinalizeLaunchValues** exclusively in `WorkEnactment`.

Core idea:
`CHRMechanismSuiteDescription := {UNM, UINDM, USCM, ULSAM, CPM, SelectorMechanism} + SuiteObligations + SuiteContractPins + SuiteProtocols (+ audit obligations)`.

#### A.19.CHR:4.0 - Ownership map and implementability guard

**Tell.** CHR mechanisms are only implementable if each described artefact has a single semantic owner. In FPF, “owner” means a concrete container that can be cited and patched: a `PatternId` (or `PatternId:SectionPath`) for text, a `PatternScopeId = G.x:Ext.*` for wiring modules, or a `DRRId` (E.9) for a decision/rationale record.

**Where lives what (single‑owner routing; cite, don’t duplicate):**

* **see `A.19.CHR:4.2.2` for canonical targets**.
* **CHR suite boundary (membership + obligations + protocols):** `A.19.CHR` (`mechanisms[]` declares `…IntensionRef`; `suite_protocols` declares order/optionality).
* **Planned baseline binding (instances/editions/policy pins):** `A.15.3` + `A.19.CHR:4.7.2` (refs/pins only; no launch values).
* **SoTA harvesting & method claims:** `G.2` (pack owner) and downstream authoring kits (`G.3`, `G.4`) — not this suite.
* **Wiring modules for method/discipline/generator specifics:** `G.*:Extensions` as `GPatternExtension` blocks (`PatternScopeId = G.x:Ext.<…>`), with explicit `SemanticOwnerPatternId`.
* **RSCR trigger catalogue and trigger alias maps:** `G.Core` (single‑writer).
* **Lexical alias docking (token drift without breaking public references):** `F.18`.
* **Project‑level specialization and transduction graphs:** project patterns (`P.*`) for `⊑/⊑⁺` specializations; `E.18 (E.TGA)` for flow graphs citing planned baseline instance refs.

#### A.19.CHR:4.1 - Objects published by this pattern

##### A.19.CHR:4.1.1 - `CHRMechanismSuiteDescription`

A concrete `MechSuiteDescription` instance whose role is to:

* enumerate the canonical CHR mechanisms (as `U.Mechanism.IntensionRef`s),
* declare suite‑level obligations/invariants,
* declare suite‑level contract pins (refs only),
* declare admissible suite protocols (Uses pipelines),
* require a standard planned baseline artifact (`CHRMechanismSuiteSlotFillingsPlanItem`) on P2W paths.

**Note (non-normative, disambiguation).** Kernel A.6.7 already uses `CHRMechanismSuiteDescription` as an illustrative *example* of a `MechSuiteDescription`. This pattern fixes the same-named object as the **canonical** CHR suite instance and supplies its P2W hook plus conformance envelope.

##### A.19.CHR:4.1.2 - `CHRMechanismSuiteSlotFillingsPlanItem`

A `SlotFillingsPlanItem` specialization used in WorkPlanning to fix the **planned baseline** of:

* pinned `CN‑Spec` / `CG‑Spec` refs (and editions where required),
* chosen mechanism instances / method descriptions / comparator specs (refs only),
* time selector / time rule pins for “no implicit latest”,
* expected guards (Launch/Compare pins) and expected crossing policy pins,
* and context identifiers needed for audit traceability (CG‑frame, path slice, publication scope).

It is explicitly **not** a mechanism, not an admissibility gate, and not a witness of execution.

#### A.19.CHR:4.2 - Canonical mechanism membership

**Tell.** `CHRMechanismSuiteDescription.mechanisms` MUST contain the following six mechanism intensions (each published as `U.Mechanism.Intension` per their owner patterns) and MUST treat them as **distinct mechanisms** (not “implementations of one”):

1. `UNM` — Unified Normalization Mechanism
2. `UINDM` — Unified Indicatorization Mechanism
3. `USCM` — Unified Scoring Mechanism
4. `ULSAM` — Unified Lawful Scale Aggregation Mechanism
5. `CPM` — Unified Comparison Mechanism
6. `SelectorMechanism` — universal set‑returning selection kernel

**Show.**

```
CHRMechanismSuiteDescription.mechanisms :=
  [ UNM.IntensionRef,
    UINDM.IntensionRef,
    USCM.IntensionRef,
    ULSAM.IntensionRef,
    CPM.IntensionRef,
    SelectorMechanism.IntensionRef ]
```

**Membership semantics note (normative).**
`mechanisms` denotes a duplicates-free **set**; order carries no semantics. Any intended ordering is expressed only in `suite_protocols`.

**Rationale.** This suite is unified by **contract surfaces** and legality discipline (CN‑Spec + CG‑Spec + Transport), not by a single BaseType.

#### A.19.CHR:4.2.1 - CHR SlotKind Lexicon (suite‑wide minimum)

**Tell.** To prevent SlotKind drift across the CHR ladder and across SoTA wiring layers, CHR mechanism intensions SHOULD use the SlotKind tokens from this lexicon whenever they refer to the corresponding semantic roles. New SlotKinds MAY be introduced, but only by first extending this lexicon (suite‑owned), then citing the new SlotKind from the affected mechanism card.

**Lexicon (minimum).** Tokens below are **SlotKind** names (not types). Concrete `ValueKind` / `RefKind` constraints are defined by the owning mechanism card and by A.6.5, A.19, G.0.

- **Core contract slots**
  - `CharacteristicSpaceSlot`
  - `CNSpecSlot`
  - `CGSpecSlot`
  - `ContextSlot`

- **Indicatorization**
  - `IndicatorChoicePolicySlot`
  - `IndicatorSetSlot`
  - `JustificationSlot`

- **Scoring**
  - `InputProfileSlot`
  - `ScoreProfileSlot`

- **Aggregation**
  - `MeasureSetSlot`
  - `GammaFoldSlot`
  - `GammaTimeRuleSlot` *(optional)*
  - `AggregatedMeasureSlot`
  - `ContributorSetSlot` *(optional)*

- **Comparison**
  - `LeftProfileSlot`
  - `RightProfileSlot`
  - `ComparatorSpecSlot`
  - `ComparisonResultSlot`

- **Selection**
  - `CandidateSetSlot`
  - `CriteriaSlot`
  - `TaskSignatureSlot` *(optional)*
  - `SelectionSlot`

- **Evidence / legality (optional, policy‑bound)**
  - `MinimalEvidenceSlot` *(optional)*

**Note.** This lexicon is intentionally small and role‑based: it constrains naming, not method semantics. Method/discipline specifics belong in SoTA packs (G.2) and wiring‑only `GPatternExtension` modules, not in the suite core.

#### A.19.CHR:4.2.2 - Canonical Intension targets (no dangling refs)

**Tell.** Each `…IntensionRef` enumerated in `CHRMechanismSuiteDescription.mechanisms` SHALL resolve to a canonical `U.Mechanism.Intension` publication under the mechanism’s own single semantic owner pattern (for CHR: the corresponding `A.19.<MechId>` mechanism-profile pattern). Draft stubs are allowed; dangling refs are not. 

**Canonical targets (normative anchors).**

- `UNM.IntensionRef` → `A.19.UNM`
- `UINDM.IntensionRef` → `A.19.UINDM`
- `USCM.IntensionRef` → `A.19.USCM`
- `ULSAM.IntensionRef` → `A.19.ULSAM`
- `CPM.IntensionRef` → `A.19.CPM`
- `SelectorMechanism.IntensionRef` → `A.19.SelectorMechanism`

#### A.19.CHR:4.3 - Suite obligations

`CHRMechanismSuiteDescription.suite_obligations` MUST be written using the **canonical obligation vocabulary** from A.6.7:4.2 and MUST include the following clauses (duplicates-free set semantics; order carries no meaning):

`{ bridge_only_crossings,
   two_bridge_rule_for_described_entity_change,
   transport_declarative_only,
   penalties_route_to_r_eff_only,
   guard_decision_tristate(pass|degrade|abstain),
   unknown_never_coerces_to_pass,
   gate_decision_separation,
   guard_lexeme_reservations,
   cg_spec_cite_required_for_numeric_ops,
   no_silent_scalarisation_of_partial_orders,
   no_silent_totalisation,
   no_thresholds_in_suite_core,
   crossing_visibility_required,
   planned_slot_filling_in_work_planning_only,
   finalize_launch_values_in_work_enactment_only,
   implementation_export_discipline_when_cited }`.

##### A.19.CHR:4.3.1 - Crossings, visibility, and penalties

* **`bridge_only_crossings`:** all cross-context / cross-plane reuse is Bridge-only (no implicit crossings).
* **`two_bridge_rule_for_described_entity_change`:** any described-entity (kind/identity) change (`CL^k`) is explicit and satisfies the two-bridge rule.
* **`transport_declarative_only`:** the suite does not embed CL/Φ/Ψ/Φ_plane tables and does not introduce transfer edges; it requires only refs/pins/anchors whose realization is mediated by E.TGA / gate surfaces.
* **`penalties_route_to_r_eff_only`:** CL/Φ/Ψ/Φ_plane penalties route to `R/R_eff` only; `F/G` are invariant under penalty routing.
* **`crossing_visibility_required`:** any GateCrossing relevant to suite use publishes a `CrossingSurface` (E.18) and can be cited as an audit anchor (including LaunchGate and `edition_key` changes of pinned `editions{…}` vectors).

##### A.19.CHR:4.3.2 - Guards and gate separation

* **Guard decision tristate:** mechanism‑level guards return
  `GuardDecision := {pass | degrade | abstain}`.
* **Unknown never coerces to pass:** unknown/insufficient evidence MUST map to `degrade` or `abstain`, not to `pass`.
* **Gate decision separation:** mechanisms and suite objects MUST NOT publish `GateDecision` nor `DecisionLog`. `block` is gate‑only (OperationalGate(profile)).
* **Guard lexeme reservations:** `USM.CompareGuard` / `USM.LaunchGuard` are gate‑level pins; mechanism predicates use suffixes `…Admissibility` / `…Eligibility`.

##### A.19.CHR:4.3.3 - Numeric legality and order semantics

* **CG‑Spec citation required:** any numeric scoring/aggregation/comparison MUST cite CG‑Spec (SCP + ComparatorSet + MinimalEvidence + Γ_fold + Φ/CL pins), and MUST NOT embed a “shadow CG‑Spec” inside mechanisms/suite.
* **No silent scalarisation of partial orders:** partial order comparisons remain set‑valued; any scalar summary is report‑only unless explicitly declared as a lawful comparator/policy.
* **No silent totalisation:** absence of totality MUST NOT be hidden by “tie‑breakers” or implicit weights.

##### A.19.CHR:4.3.4 - P2W discipline

* **Planned slot filling in WorkPlanning only.**
* **FinalizeLaunchValues in WorkEnactment only.**
* Suite and plan objects MUST NOT contain launch‑value witnesses.

##### A.19.CHR:4.3.5 - Thresholds and defaults

* **`no_thresholds_in_suite_core`:** acceptance thresholds live in AcceptanceClauses / TaskSignature / GateProfile, not in CHR suite core.
* **Default discipline (no competing defaults):** the suite MUST NOT introduce competing defaults. If a default is used (e.g., portfolio mode), it MUST be cited from its single declared source (typically a TaskSignature or an explicit policy-id), and all other mentions are citations.

##### A.19.CHR:4.3.6 - Implementation export discipline (when cited)

* Suite MAY cite implementations (CAL/LOG/CHR) as refs, but:

  * LOG/CHR do not export Γ,
  * CAL exports exactly one Γ,
  * imports are acyclic.

##### A.19.CHR:4.3.7 - Routed claim mini-register (A.6.B)

**Intent.** `CHRMechanismSuite` is a contract-like architectural boundary (suite obligations + P2W hook). To avoid “contract soup”, the load-bearing statements below are routed as atomic claims per **A.6.B** and can be cited by IDs instead of being paraphrased across downstream patterns and MVPK faces.

| ID | Quadrant | Statement (atomic; verbatim) | Canonical location |
|---|---|---|---|
| **L-A67CHR-01** | L | `CHRMechanismSuiteDescription.mechanisms` denotes a duplicates-free set; order carries no semantics. | A.19.CHR:4.2 (Membership semantics note) |
| **L-A67CHR-02** | L | A “planned baseline” is a WorkPlanning artefact that records planned fillers and pins for a P2W path slice. | A.19.CHR:4.1.2 / 4.6 |
| **L-A67CHR-03** | L | A planned baseline is not an execution witness and contains no launch values. | A.19.CHR:4.1.2 / 4.6 |
| **A-A67CHR-01** | A | A suite protocol is *suite-closed* iff every `ProtocolStep.mechanism` is a member of `CHRMechanismSuiteDescription.mechanisms`. | A.19.CHR:4.5 (WF‑MS‑2) |
| **A-A67CHR-02** | A | A P2W path slice is CHR-suite-ready for enactment iff a planned baseline of kind `CHRMechanismSuiteSlotFillingsPlanItem` exists for that slice, sets `target_slot_owner_ref` to an edition-addressable `MechSuiteDescriptionRef` whose referent is `CHRMechanismSuiteDescription`, and pins `CNSpecRef` and `CGSpecRef`. | A.19.CHR:4.6 |
| **D-A67CHR-01** | D | Suite authors SHALL publish `CHRMechanismSuiteDescription` as a `MechSuiteDescription` instance. | A.19.CHR:7.1 (CC‑A67CHR‑1) |
| **D-A67CHR-02** | D | Suite authors SHALL NOT encode `CHRMechanismSuiteDescription` as a `MechFamilyDescription`. | A.19.CHR:7.1 (CC‑A67CHR‑1) |
| **D-A67CHR-03** | D | Suite authors SHALL enumerate exactly `{UNM, UINDM, USCM, ULSAM, CPM, SelectorMechanism}` as `U.Mechanism.IntensionRef`s in `CHRMechanismSuiteDescription.mechanisms`. | A.19.CHR:4.2 / 7.1 (CC‑A67CHR‑2) |
| **D-A67CHR-04** | D | Suite authors SHALL keep `CHRMechanismSuiteDescription.suite_contract_pins` refs-only. | A.19.CHR:4.4 / 7.1 (CC‑A67CHR‑3) |
| **D-A67CHR-05** | D | Suite authors SHALL NOT embed CL/Φ/Ψ/Φ_plane tables or introduce transport edges in suite- or plan-level artefacts. | A.19.CHR:4.3.1 / 4.4 / 7.2 (CC‑A67CHR‑13) |
| **D-A67CHR-06** | D | WorkPlanning authors SHALL publish one `CHRMechanismSuiteSlotFillingsPlanItem` per P2W path slice that uses the CHR suite. | A.19.CHR:4.6 / 7.2 (CC‑A67CHR‑10) |
| **D-A67CHR-07** | D | WorkPlanning authors SHALL ensure a `CHRMechanismSuiteSlotFillingsPlanItem` contains planned pins/fillers only. | A.19.CHR:7.2 (CC‑A67CHR‑11) |
| **D-A67CHR-08** | D | WorkPlanning authors SHALL NOT include launch values, execution witnesses, gate decisions, or decision logs in a `CHRMechanismSuiteSlotFillingsPlanItem`. | A.19.CHR:7.2 (CC‑A67CHR‑11) |
| **D-A67CHR-09** | D | MVPK face authors SHALL ensure any claimful face that publishes edition pins or comparability/launch claims also publishes the required BridgeCard + UTS row anchors and the applicable USM guard pin with `GuardOwnerGateSlot`. | A.19.CHR:7.3 (CC‑A67CHR‑16) |
| **E-A67CHR-01** | E | Evidence carrier for the planned baseline is the `CHRMechanismSuiteSlotFillingsPlanItem` instance and its citation from downstream `U.Work.Audit` as the baseline for the path slice. | A.19.CHR:7.2 (CC‑A67CHR‑14) |
| **E-A67CHR-02** | E | Evidence carrier for launch values and `FinalizeLaunchValues` is `U.WorkEnactment` (and its audit/evidence carriers), not the planned baseline artefact. | A.19.CHR:4.6 / 7.2 |

#### A.19.CHR:4.4 - Suite contract pins

`CHRMechanismSuiteDescription.suite_contract_pins` MUST be refs‑only and MUST include:

1. **Required spec refs:** `{CNSpecRef, CGSpecRef}` (as required pins, not copied content).
2. **Required planned baseline:** `required_planned_baseline_ref := CHRMechanismSuiteSlotFillingsPlanItem` (kind‑level requirement: “P2W path MUST publish a planned baseline artifact of this kind”).
3. **Required edition pins / policy pins (when applicable):**

   * `editions{CG‑Spec, ComparatorSet, UNM.TransportRegistryΦ, …}` when the chosen protocol path is edition‑sensitive,
   * policy‑id pins for Φ/Ψ/Φ_plane when crossings are expected.

**Tell (discipline).** Contract pins are **anchors**; they do not embed tables (CL ladders, Φ registries) and do not introduce transport edges.

#### A.19.CHR:4.5 - Suite protocols

`CHRMechanismSuiteDescription.suite_protocols` (if present) MUST follow the A.6.7 `SuiteProtocol` structure and MUST be closed over suite membership (WF‑MS‑2): every `ProtocolStep.mechanism` is a member of `CHRMechanismSuiteDescription.mechanisms`.


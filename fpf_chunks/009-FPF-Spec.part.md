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
> **Purpose (one line):** provide a universal, context-explicit **planned baseline** that maps a slot-bearing description's `SlotKind`s to **planned fillers**, to be consumed by Work enactment where launch values are finalized.

**Minting notes (informative)**
* **Mint vs reuse:** This pattern mints the kind name `SlotFillingsPlanItem`. It reuses existing Core terms and disciplines (e.g., `U.WorkPlan.PlanItem`, SlotKind/ValueKind/RefKind/refMode discipline, edition pinning, `U.BoundedContext`, and the P2W split between WorkPlanning and WorkEnactment).
* **`SlotFillingsPlanItem` (kind name):** keep the suffix `PlanItem` to preserve the WorkPlanning placement. Do not mint aliases like *SlotBinding…* (conflicts with the A.6.5 binding discipline) or *SlotValue…* (ambiguous slot-bearing description or context).
* **Anchor names:** if any anchors in §4.2 are later materialized as formal field names, keep `…_ref` only for fields whose values are concrete RefKind handles, and keep `…_id` only for identifiers. Avoid introducing generic placeholders like `SpecRef/PolicyRef/GateRef` inside this pattern; prefer existing concrete ref kinds (or a dedicated DRR+LEX step).
* **Row vocabulary:** treat `SlotFillingRow` and `PlannedFiller` as *internal* names of this pattern unless/until a separate DRR+LEX step promotes them to shared tokens.

### A.15.3:1 - Problem frame

FPF frequently needs to make **reproducible, reviewable choices** about *what fills which conceptual slot* (spec refs, policy refs, mechanism-instance refs, time selectors, evidence hooks, etc.) **before** any Work is enacted. These choices must be visible as a planned baseline for a concrete P2W slice (CG-frame, path slice, or publication scope), and must remain distinct from run-time “actuals” and gate decisions.

However, absent a universal WorkPlanning plan item for architecture-by-planned-slot-filling, authors tend to hide these choices inside mechanism prose, CG/CN specs, ad-hoc cards, or informal checklists—making Part G patterns difficult to universalize and making Work audit trails ambiguous.

`SlotFillingsPlanItem` addresses this by defining a **WorkPlan PlanItem kind** whose job is to state, in one place and with explicit context, a mapping:

> *(Target slot-bearing description, slot kind) → planned filler (ByValue | ByRef(<concrete RefKind>), with edition pins when needed)*

and to do so in a form that can be cited by Work enactment and by suite/kit spec pins, without collapsing into “execution” or “decision logging”.

### A.15.3:2 - Problem (what breaks without it)

Without an explicit `SlotFillingsPlanItem` baseline, at least six failure modes recur:

1. **Hidden slot-bearing-description reference and meaning drift:** a planned filler is stated without making explicit *whose* slot set is being filled, allowing silent reinterpretation of `SlotKind`s across kits/suites.

2. **Plan/execution collapse:** plan documents get “backfilled” with run-time values, so there is no stable planned baseline and no clean variance trail. WorkPlan explicitly warns against this.

3. **Implicit time (“latest”) and implicit recency:** planned claims about comparability or launch readiness omit an explicit `Γ_time`, which violates the time discipline (“no implicit recency”).

4. **Edition ambiguity:** references to methods/policies/specs are not edition-pinned where reproducibility requires it, or the plan mutates the edition vector instead of citing pinned editions (edition changes are crossings, not “plan edits”).
   A particularly harmful subtype is **edition-key backfill**: retroactively editing a previously used baseline so that an edition-key change looks like an innocent PlanItem edit (hiding the required GateCrossing witness and breaking audit traceability).

5. **Crossing invisibility:** cross-context or cross-plane expectations (Bridge + policy ids) are not stated at plan time, so later gate crossings appear as “magic” rather than traceable expected constraints.

6. **G-pattern fragmentation:** each Part G pattern invents its own place to stash planned refs (method pick, comparator pick, QD archive config, etc.), blocking a clean “G.Core” universal layer and making modular reuse brittle.

### A.15.3:3 - Forces (what we must balance)

* **Strict distinction:** planned baseline is not a run-time witness; launch values are finalized only in Work enactment.
* **Context must be explicit:** every normative claim/rule is context-bound; the PlanItem must carry its context rather than relying on file location or prose.
* **Time must be explicit:** no implicit “latest”; any plan that will be cited by comparability/launch checks needs an explicit `Γ_time` selector/rule.
* **SlotKind meaning is stable:** the plan may choose fillers, but must not reinterpret SlotKinds or smuggle new semantics into indices.
* **Derived indices must not become “places of meaning”:** projections like “planned spec refs” are useful, but must remain derivable from the authoritative rows.
* **Conceptual, not procedural:** no solver steps, no lints, no “data governance”; this is an epistemic object used by humans in review.
* **Supports universalization:** one PlanItem pattern must be usable across the whole of Part G, not just G.5.
* **Integrates with suites/kits:** suites may require a planned-baseline ref and may act as slot-bearing descriptions.

| Force | Tension |
| --- | --- |
| Plan/run split | Plan must be citeable without containing run-time values. |
| Slot meaning stability | SlotKinds must not drift by implicit slot-bearing-description changes. |
| Edition honesty | Baselines must pin editions where meaning changes; avoid “latest”. |
| Suite/kit modularity | Suite descriptions define slot interfaces and obligations; baselines choose fillers for a plan instance. |
| Auditability | A reader must reconstruct “what was planned” without chasing hidden defaults. |
| Extensibility | Allow suite-specialized variants without breaking universal core. |

### A.15.3:4 - Solution

#### A.15.3:4.1 Definition

A `SlotFillingsPlanItem` is a **kind of `U.WorkPlan.PlanItem`** whose content is a **planned slot-fillings ledger** for a *single* slot-bearing description, within an explicit P2W context.

It is a **WorkPlanning baseline**, intended to be:

* produced/approved in WorkPlanning,
* **cited** by downstream Work enactment (as planned baseline),
* compared against actual fillings (variance recorded in Work, not by rewriting the plan).

**Normative note (I/D/Spec vs views):** A `SlotFillingsPlanItem` is a Description-level planning episteme (a PlanItem). It MAY be projected into `U.View` (e.g., `TechCard(SlotFillingsPlanItemRef)`), but any view is strictly a projection and MUST NOT introduce additional claims or “shadow defaults”.

#### A.15.3:4.2 Core conceptual descriptors (not a data schema)

A conformant `SlotFillingsPlanItem` SHALL provide the following description (names are indicative; the semantics are normative):

1. **PlanItem core (from A.15.2)**
   The PlanItem MUST remain a WorkPlanning plan item: it may include assumptions, dependencies, constraints, expected publications or records, and notes; it MUST NOT contain run-time logs/actuals.

2. **Target slot-bearing description**

   * `target_slot_bearing_description_ref : <concrete …DescriptionRef>` (required)
     Identifies the **Description episteme whose SlotKind set is being filled** (e.g., a kit description or a suite description).
     The slot-bearing description MUST be referenced as an **edition-addressable Description episteme** (a concrete `…DescriptionRef` such as `MechSuiteDescriptionRef`, `…KitDescriptionRef`, etc.),
     and MUST NOT be a mechanism `U.Mechanism.IntensionRef` (or any other intensional ref).
     A `MechSuiteDescription` MAY serve as a slot-bearing description for this purpose.
     If the slot-bearing description’s SlotKind interface is edition-sensitive (or expected to evolve), the reference MUST be edition-pinned (e.g., `target_slot_bearing_description_ref.edition`) whenever the PlanItem is used as a reproducibility baseline.

3. **Described entity and grounding (for “whose measurements/choices?”)**

   * `described_entity_ref : <concrete RefKind>` (required)
     The referent is the *described entity* (C.2.3 role): the thing the planned baseline is **about**.
     It MUST NOT be silently conflated with a holon. (Example: a baseline can be about a width/measure while the grounding holon is a stool with that width.)
     Use a concrete RefKind of the described entity (e.g., `U.HolonRef`, `U.MeasureRef`, …). Do **not** mint a new generic `EntityRef` token inside this pattern.
   * `grounding_holon_ref? : U.HolonRef` (optional; required when the described entity is not itself a holon and a grounding holon is needed for plane/frame anchoring)
   * `reference_plane? : ReferencePlane` (optional; required when not unambiguously derivable from cited context publications or records such as CG-frame/spec pins)

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
       A SlotKind provided by the `target_slot_bearing_description_ref` (the PlanItem MUST NOT reinterpret SlotKind meaning).
       Unless the slot-bearing description explicitly declares the slot as multi-valued, each `slot_kind` SHALL appear **at most once** in `planned_fillings`.
     * `planned_filler : PlannedFiller` where:
       `PlannedFiller := ByValue(value) | ByRef(ref : <concrete RefKind>)`
       In `ByRef(…)`, the `ref` MUST be of a **concrete RefKind** (e.g., `…SpecRef`, `…PolicyRef`, `…MethodDescriptionRef`);
       the PlanItem MUST NOT use an untyped/generic “Ref” / “RefKind” placeholder.
       The chosen filler MUST conform to the SlotSpec discipline of the slot-bearing description (A.6.5-style: `refMode ∈ {ByValue | <concrete RefKind>}`).
       Changes to planned fillers are described using the A.6.5 verb discipline: ByValue content change (`fill/assign/update`) vs ref retargeting (`retarget`) vs ref resolution (`resolve`), never by “renaming the slot”.
     * `edition_pin? : EditionId`
       Required only when reproducibility depends on an edition **and** the planned filler cannot carry an edition pin directly (preferred: `…DescriptionRef.edition` on the ref itself).
       If both the planned filler ref and the row provide edition pinning, they MUST agree (mismatch ⇒ nonconformant).
       ByValue rows SHOULD NOT carry edition pins unless the pinned edition is explicitly tied to a cited external publication or record (e.g., a referenced rule, policy, or method description).

9. **Derived indices (optional; never a second canonical source)**

   * `planned_spec_ref_index? : [<concrete …SpecRef>…]`
   * `planned_policy_ref_index? : [<concrete …PolicyRef>…]`
   * `planned_mechanism_instance_ref_index? : [<concrete …MechanismInstanceRef>…]`
     If any of these are present, they MUST be **derivable projections** of `planned_fillings`; any mismatch is nonconformant.
     (These are *categories* of refs extracted from the authoritative rows, not an invitation to introduce new generic `SpecRef/PolicyRef` token-kinds.)

10. **Expected crossing policy pins (refs only; no crossing witnesses)**

   * `expected_crossing_policy_refs? : [⟨bridge_card_ref, phi_policy_id, psi_policy_id?, phi_plane_policy_id?, reference_plane(src,tgt)⟩ …]`
     These communicate what the plan expects will be needed for crossings, without claiming that a crossing has occurred.
     `bridge_card_ref` is expected to pin a Bridge identity/channel (BridgeId + channel) and to be auditable via downstream CrossingBundle/UTS rows.
     This section states **Bridge-only** expectations; it MUST NOT introduce non-Bridge crossing mechanisms, and it MUST NOT embed CL/Φ/Ψ/Φ_plane tables (refs/policy-ids/pins only).

   * `expected_crossing_bundle_refs? : [CrossingBundleRef…]` (optional)
     Permitted only when the plan is explicitly citing already-published CrossingBundle baselines (e.g., “fixed context constants”); otherwise, the PlanItem SHALL state only expected policy pins and allow the crossing witness to appear at the gate/work level.

11. **Notes (didactic, non-normative)**

* `planned_filling_notes?`
  Helpful narrative for reviewers; must not embed new claims that contradict the rows.

#### A.15.3:4.2.1 Canonical skeleton (Show)

The following compact pseudo-record illustrates the intended *canonical minimum*: explicit context + explicit time + a few authoritative rows.

```
SlotFillingsPlanItem := ⟨
  kind = SlotFillingsPlanItem,
  target_slot_bearing_description_ref = CHRMechanismSuiteDescriptionRef@edition(E_suite),
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

* Any suite/kit that requires a “planned baseline” may require and cite a reference to a `SlotFillingsPlanItem` via its spec pins; `MechSuiteDescription` explicitly provides a place for such a requirement.

#### A.15.3:4.5 - Variants

1. **Suite-specialized PlanItem (Refinement)**
   A suite may define `XSuiteSlotFillingsPlanItem ⊑ SlotFillingsPlanItem` with:

   * fixed `target_slot_bearing_description_ref = XSuiteDescriptionRef`,
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
* Not a hiding place for acceptance thresholds: any threshold-like semantics MUST live in explicit Acceptance or Policy records (and be referenced/pinned), not smuggled in as anonymous ByValue numbers.
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

1. Choose one `target_slot_bearing_description_ref` per PlanItem. If multiple slot-bearing descriptions are involved, author multiple `SlotFillingsPlanItem`s (one per slot-bearing description) to keep slot meaning unambiguous.
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
* targets `CHRMechanismSuiteDescriptionRef` as the slot-bearing description (and pins its edition if used as a reproducibility baseline),
* pins `CNSpecRef` and `CGSpecRef` (editions pinned where reproducibility requires),
* pins a `ScoringMethodDescriptionRef.edition` (e.g., a monotone scoring family) and/or a set-valued method family (e.g., conformal-style set predictions),
* declares `Γ_time_selector = point(t0)` (no implicit “latest”),
* declares `expected_usm_guard_pins = {USM.CompareGuard, USM.LaunchGuard}`,
* includes evidence pin refs that will later be populated/used in Work enactment.

The resulting Work enactment cites this PlanItem as the planned baseline; any substitution (e.g., retargeting a method description ref) appears as Work variance (and, when relevant, as a crossing witness), not as a retroactive plan rewrite.

#### A.15.3:5.2 - Archetype 2: Archive/QD selection with edition-sensitive descriptors

**Tell.** A workflow plans to return an **archive** (quality-diversity style) rather than a single winner. The selection pipeline depends on descriptor maps and distance definitions that are edition-sensitive.

**Show (failure without `SlotFillingsPlanItem`).** Descriptor-map and distance-definition drift is discovered only after the fact: an "archive" is produced, but reviewers cannot reconstruct which descriptor edition and distance definition were assumed at planning time, and the published view/card becomes the de facto mutable canonical source.

**Show (repair with `SlotFillingsPlanItem`).** A conformant `SlotFillingsPlanItem`:
* targets an archive-selection kit/suite as `target_slot_bearing_description_ref`,
* pins `DescriptorMapDescriptionRef.edition` and `DistanceDefDescriptionRef.edition` (or their kit equivalents),
* states `expected_usm_guard_pins = {USM.CompareGuard}` (if no LaunchGate is expected yet),
* records expected crossing policy pins if descriptors are reused cross-context.

This prevents “silent” descriptor drift across iterations and makes Part G’s archive-related extensions composable rather than embedded in selector prose.

### A.15.3:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal**.

| Lens | Bias / limitation introduced by the pattern | Mitigation |
| --- | --- | --- |
| Gov | Baseline immutability and variance recording can be misread as bureaucracy rather than epistemic hygiene. | Keep the baseline minimal; use suite-specialized refinements only when a suite description truly requires them. |
| Arch | Enforces a clean P2W seam and discourages “configuration hidden in mechanisms”. This can expose underspecified slot-maintenance assignments earlier. | Treat that friction as an architectural signal; refine the slot-maintenance interface rather than hiding choices in prose. |
| Onto/Epist | Biases toward explicit context/time/edition pinning; exploratory reasoning may feel constrained. | Use minimal variants (context + rows + time selector) for exploration; graduate to pinned editions only when reproducibility is required. |
| Prag | Increases upfront authoring cost (explicit context, time, edition pins). | Use derived indices as projections for reader navigation; avoid duplicating content on views/cards. |
| Did | Biases against “one true card” habits by treating views as projections; may clash with existing documentation culture. | Provide a TechCard/PlainView projection explicitly, but keep the PlanItem as the governing work-plan record. |

### A.15.3:7 - Conformance Checklist

| ID          | Check (normative)                                                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CC-A15.3-01 | The object is a `U.WorkPlan.PlanItem` with `kind = SlotFillingsPlanItem`, and obeys WorkPlan guardrails (no logs/actuals, no step logic).                                                                           |
| CC-A15.3-02 | `target_slot_bearing_description_ref` is present and identifies a real slot-bearing description (kit/suite); SlotKinds in rows are interpreted only within that slot-bearing description.                                                                      |
| CC-A15.3-02a | If the PlanItem is used as a reproducibility baseline and the slot-bearing description is edition-addressable, `target_slot_bearing_description_ref` is edition-pinned (e.g., `…DescriptionRef.edition`).                                      |
| CC-A15.3-02b | `target_slot_bearing_description_ref` is a **Description-level** ref (e.g., `MechSuiteDescriptionRef`, `…KitDescriptionRef`) and MUST NOT be an intensional ref (e.g., `U.Mechanism.IntensionRef`). |
| CC‑A15.3‑02c (single slot-bearing description) | A `SlotFillingsPlanItem` targets exactly one slot-bearing description via `target_slot_bearing_description_ref`. If multiple slot-bearing descriptions are involved, they MUST be represented by multiple PlanItems (one per slot-bearing description). |
| CC-A15.3-03 | `described_entity_ref` is present. If `grounding_holon_ref` and/or `reference_plane` are omitted, they must be unambiguously derivable from cited context publications or records (e.g., the pinned CG-frame/spec context).      |
| CC-A15.3-03a | `described_entity_ref` is a concrete RefKind (no generic “EntityRef” placeholder is introduced by this pattern). |
| CC-A15.3-04 | Context anchors are explicit at least to `bounded_context_ref`; if the fillings support legality/selection, then CG-frame/path-slice anchors are present.                                                           |
| CC-A15.3-05 | Time is explicit: the item includes `Γ_time_selector` or `Γ_time_rule_ref`; “latest/current” without explicit `Γ_time` is nonconformant.                                                                             |
| CC-A15.3-05a | Exactly one of `Γ_time_selector` and `Γ_time_rule_ref` is present (XOR); both-present or both-absent is nonconformant. |
| CC-A15.3-06 | `planned_fillings` is the authoritative source: each row is `⟨slot_kind, planned_filler, edition_pin?⟩`; each planned filler is explicit `ByValue` vs `ByRef(ref-of-concrete-RefKind)` and conforms to the slot-bearing description’s SlotSpec discipline (no silent slot-meaning changes). |
| CC-A15.3-06a | Unless the slot-bearing description declares a slot as multi-valued, `planned_fillings` contains **no duplicate** `slot_kind` rows (duplicate keys ⇒ nonconformant). |
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
| CC‑A15.3‑13a (crossing bundles are not witnesses) | `expected_crossing_bundle_refs` (if present) is used only to cite already‑published, context‑constant CrossingBundle baselines; it MUST NOT be used to claim that a crossing occurred for this enactment, nor to substitute for gate/work‑level crossing witnesses. |
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

Correct handling: keep the old baseline intact; record variance in Work and, where applicable, require the gate/work-level crossing witness (UTS/CrossingBundle + policy-id pins),
or produce a new PlanItem edition as the new planned baseline for subsequent enactments.

### A.15.3:9 - Consequences

| Benefit | Trade‑off / Cost | Notes / Mitigation |
| --- | --- | --- |
| Improved modularity | Requires an explicit baseline plan item | Keep baselines minimal; specialise only when a suite truly needs it. |
| Audit clarity | More up-front authoring work | The authoring workload is intentional: it buys attributable variance and prevents “mystery defaults”. |
| Edition honesty | Forces authors to think about editions and time | Use editioned refs and time selectors by ref; keep actual `Γ_time` in Work evidence. |
| Controlled specialisation | Multiple PlanItem kinds may exist (core + suite‑specialised) | Use DRR to document why specialisation is warranted; keep the universal core stable. |

### A.15.3:10 - Rationale

This pattern exists to give WorkPlanning an explicit, citeable place to commit to “which planned values or references will fill which slots” without collapsing into run-time state.

Keeping the baseline bound to exactly one slot-bearing description makes SlotKind semantics checkable and prevents accidental cross-slot-bearing-description drift.

Treating indices as derived projections preserves the canonical row source while still enabling human-friendly navigation or tooling acceleration.

Finally, by disallowing run-time witnesses (launch values, observed values, concrete `Γ_time`) the pattern enforces the plan/run split and keeps audit variance attributable to an explicit baseline rather than to shifting defaults.

### A.15.3:11 - SoTA‑Echoing (informative)

This pattern aligns with post‑2015 practice in multiple traditions while deliberately staying notationally/tool independent.

* **ISO/IEC/IEEE 12207:2017** — **Adopt** the separation between planning documents, execution records, and baseline/change-control concepts; **Adapt** them into a lightweight, citeable PlanItem kind; **Reject** prescribing any specific process tooling as normative inside FPF.
* **ISO 26262:2018** — **Adopt** the emphasis on traceability, change impact visibility, and preventing retroactive “paper compliance”; **Adapt** it into baseline immutability + variance reporting; **Reject** treating safety certification structure as a required envelope for all contexts.
* **NIST SP 800-128 Rev.1 (2020)** — **Adopt** baseline management and deviation recording as an audit primitive; **Adapt** by expressing baselines as epistemic, context-bound references rather than machine configuration states; **Reject** security-tooling prescriptions as a dependency of the conceptual model.
* **Forsgren, Humble, Kim (2018), _Accelerate_** — **Adopt** the empirical lesson that explicit change tracking and small, attributable deltas improve reliability; **Adapt** by making the baseline the anchor for fulfilment/variance; **Reject** any “one true pipeline” or vendor-specific operational recipe.
* **Morris (2021), _Infrastructure as Code_ (2nd ed.)** — **Adopt** the desired-state vs observed-state distinction and the discipline of explicit declarations; **Adapt** by keeping declarations as plan-level epistemes rather than deployment manifests; **Reject** binding the model to any specific IaC syntax or platform.

### A.15.3:12 - Relations

* **Builds on and is governed by:**
  * **A.15.2 `U.WorkPlan`** — container + PlanItem discipline; baseline citeability.
  * **A.6.5 slot discipline** — SlotKind/RefKind hygiene and binding-time separation.
  * **E.10.D1 Context discipline** — explicit context/edition; no implicit “latest”.
  * **E.18 and TGA** — keeps `FinalizeLaunchValues` strictly in WorkEnactment; pin and guard discipline.
* **E.17 publication discipline** — views are projections; no new semantics on cards.
* **Interacts with and complements:**
  * **A.6.7 `MechSuiteDescription`** — suites may require the presence of a planned baseline ref/pin without embedding planned fillers or launch values.
  * **A.15.1 Work / WorkEnactment discipline** — fulfilment and variance are recorded downstream against this baseline.
  * **C3.2-S-02 Time discipline** — time selection policy may be pinned by ref; run-time `Γ_time` stays in Work evidence.

### A.15.3:End

## A.15.4 - Work-Relevant Source Restoration

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** This A.15 cluster member tells an engineer-manager which exact project-side FPF kind and reference must be recovered before an encountered episteme, episteme publication, display, credential view, generated explanation, copied statement, provenance mark, dashboard tile, schema wording, API wording, or composed source chain may support a work claim or reliance claim.

**Use this when.** Use this pattern when a visible item is about to guide a work move, reliance move, or work-relevant P2W claim by appearance, and the acting user must recover the exact project-side FPF kind and reference before proceeding.

**First output.** One compact restoration note: encountered item; live work claim, reliance claim, or P2W load or position; governing FPF pattern; exact project-side FPF kind and reference needed; admissible next project move now; and blocked overread.

**What goes wrong if missed.** Teams treat a visible dashboard, credential view, copied approval, generated explanation, provenance mark, schema wording, API wording, publication, display, or cue as if it already carried approval, permission, gate passage, evidence, engineering justification, performed work, release permission, role support, or status support. Work then proceeds or stops on appearance while the governing FPF pattern and exact project-side FPF kind and reference that actually carry the claim or effect are missing, stale, revoked, or contradicted.

**Governed object in plain terms.** One source-restoration relation for one live work claim, reliance claim, or P2W load or position: encountered item, live claim or effect, governing FPF pattern, exact project-side FPF kind and reference needed, admissible next project move now, and blocked overread. It is not a new `authoritySourceRef` target, evidence source, gate record, engineering justification object, work occurrence, or generic publication kind.

**Governing move in plain terms.** Recover or name the governing FPF pattern and exact project-side FPF kind and reference before allowing the encountered item to guide work or reliance. When that support is absent or insufficient, narrow the move, reopen or refresh the source, run only a bounded reversible probe under a work plan, or block the unsupported claim or effect.

**Recognition block vs assurance block.** Read **At a glance**, **Use this when**, **First output**, **What goes wrong if missed**, **Governed object**, **Governing move**, **Working action path**, **Not this pattern when**, and **What this buys** as the primary recognition block. Read the field tables, lookup table, lint cues, stress cases, conformance checklist, SoTA alignment, and relations below as assurance and support blocks that tighten the same source-restoration claim; they do not widen this pattern into an evidence, gate, engineering-justification, speech-act, commitment, boundary, or work-occurrence pattern.

**Working action path.**
1. Name the encountered item kind and publication position without treating its appearance as source support.
2. Name the live work claim, reliance claim, or P2W load or position and the claim or effect that would be carried.
3. Recover the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect.
4. Choose the lightest admissible project move now: proceed inside recovered support, narrow the move, run a bounded reversible probe under `U.WorkPlan`, reopen or refresh the source, ask the accountable role assignment to expose or repair the missing source episteme, publication, register entry, or project record, or block only the unsupported claim or effect.
5. Return to `A.15` only when the remaining live question is `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation.

**Not this pattern when.** Stay in A.15 when the live problem is only `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation. Stay in E.17 when the live problem is only publication-face exposure or multi-view publication. Stay in A.10, B.3, A.20, A.21, A.2.8, A.2.9, A.6, or A.15.1 when evidence, currentness, engineering justification, gate validity, constraint validity, commitment, speech act, boundary claim, or work occurrence already governs the live claim or effect directly.

**What this buys.** The acting engineer-manager can keep work moving at the lightest admissible level: proceed inside recovered support, narrow the move, run a bounded reversible probe under a work plan, reopen the needed exact project-side FPF kind and reference, ask the role assignment accountable for that source to expose or repair it, or block only the unsupported claim or effect while preserving narrower admissible use.

### A.15.4:1 - Problem Frame

Dashboards, credential views, generated explanations, copied approvals, provenance labels, green tiles, schema wording, API wording, and composed source chains often look ready for action before the governing FPF pattern and exact project-side FPF kind and reference that make the action or reliance admissible have been recovered. The practical problem is not to classify the item in FPF; the problem is to decide what an engineer-manager may do in the project now without turning appearance into approval, gate passage, evidence, assurance, performed work, or release permission.

**Plain recognition line.** Let the visible cue point to the support; do not let it become the support that permits the work or reliance move.

### A.15.4:2 - Cluster Boundary


A.15 remains the kernel for separating `U.Role`, holder and context, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and actual `U.Work`. A.15.4 starts only when an encountered item begins to support a work claim or reliance claim and the team must recover the exact project-side FPF kind and reference that carries that support. If the governing FPF pattern and project-side reference are already known, use them directly and keep A.15.4 as the bounded restoration step.

### A.15.4:3 - Work-Relevant Source Restoration

##### Core stress-case rule
**Ordinary source-restoration note.** In ordinary use, do not build a source dossier. The first useful note is:

`encountered item; live work claim or reliance claim; governing FPF pattern; exact project-side FPF kind and reference needed; admissible next project move now; blocked overread`

The encountered item may be a tile, credential view, approval-looking memo, generated explanation, copied review, provenance mark, API wording, functional-description publication, or composed source chain. The pattern asks whether the exact work claim or reliance claim is currently supported, not whether the item is impressive, fluent, or easy to read.

**Conditional source-support field set.** Use the fuller fields below only when release, safety, compliance, role, status, gate, assurance, contested source, external reliance, cross-context reuse, currentness, revocation, generated source support, or copied source support is live. These fields are local restoration aids, not a new record kind.

| Field | Working question |
| --- | --- |
| subject or actor | Who or what would perform the work, rely on the item, hold the status, or be affected by the claim? |
| role | Which `U.RoleAssignment` or role-context reading is live? |
| action or work target | Which selected method, method of work, `U.WorkPlan`, planned work, actual `U.Work`, work result, release move, reliance move, status, or effect is being guided? |
| resource or claim target | Which resource, claim, gate, credential, status, evidence, approval, or source finding with authority-reference relation is supposedly affected? |
| context | Which bounded context, environment, project slice, interface setting, protocol setting, or relying situation makes the claim live? |
| policy or gate version | Which policy, gate profile, constraint version, method version, or register edition is supposed to govern the claim? |
| time window | During which window is the support claimed to hold? |
| currentness or revocation status | Is the supporting source current, stale, revoked, superseded, expired, contradicted, or unknown? |
| issuer or source | Which issuer, exact project-side FPF kind and reference, register source, status source, speech act, gate decision, evidence path, or work-occurrence record carries the support? |
| verifier or relying context | Who is checking or relying on the claim, and in which context? |
| evidence or attestation path | Which `A.10` evidence, provenance, or attestation path, if any, supports the claim without itself becoming approval, gate passage, assurance, or work occurrence? |
| sourceSupportPosture | Which `E.17:5.1b` posture applies to the encountered item and required claim or use? |
| unsupported effect | Which requested work claim, reliance claim, or downstream effect remains unsupported and must be narrowed, repaired, reopened, probed, or blocked? |


Start with the A.15.4 working action path above when the encountered item is about to guide a work move, reliance move, or work-relevant claim. If the live issue is only evidence, currentness, gate validity, constraint validity, engineering justification, commitment, speech act, boundary wording, admissibility wording, credential proof, status proof, explanation, comparison, or carrier and front-end behavior, apply that governing FPF pattern and exact project-side FPF kind and reference directly; use A.15.4 only when that source must be restored before role, method, plan, work, work result, result measurement, or another work move or reliance move can proceed.

**Authority-looking source-backed work or reliance case.** Use A.15.4 when an approval-, permission-, gate-, command-, credential-, delegation-, revocation-, status-, provenance-, dashboard-, copied-review-, generated-explanation-, schema-, API-, or composed-chain case is about to be used as a work cue, reliance basis, release reliance basis, execution-evidence basis, approval claim basis, approval effect basis, role claim basis, status claim basis, or next work-relevant move. The recognition moment is that an encountered publication, display, credential view, wording, or explanation looks like permission, prohibition, readiness, or evidence for starting work; the governed question is still the live work claim, reliance claim, or P2W load or position plus the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect being read from, or through, the wording, display, publication face, carrier, or source-finding cue. It is not the wording alone. A.15.4 does not change the governed object of `A.15`; it governs only the source-restoration step before the encountered case can support work or reliance.

Here "authority-looking case" is only a recognition phrase for the encountered situation; it is not a `U.*` kind, not a profile, not a score, and not a new evidence source, governing pattern, or `authoritySourceRef` target. The source-backed object that permits, forbids, records, or supports the work may instead be a `GateDecision`, `SpeechAct`, `Commitment`, `RoleAssignment`, credential record, status record, `A.6.B`-governed claim, `A.10` evidence path, or `B.3` assurance claim. Use `E.17:5.1c` for the shared meanings of `orientation use`, `reliance use`, work claim, reliance claim, operative claim, unsupported downstream use, and `reopen trigger`; use `E.17:5.1d` when the primary live question may belong to another governing FPF pattern with its exact project-side FPF kind and reference.

The central behaviour is: name the live work claim, reliance claim, or P2W load or position; name the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect; keep the `U.Episteme` or `U.EpistemePublication` distinct from publication form, MVPK face, carrier, rendering, and source-finding cue; choose the minimum sufficient next move; recover only the exact project-side FPF kind and reference needed for that move; and do not raise the claim beyond that recovered support. If the named project record states the governing FPF relation, use that recorded relation directly rather than inferring support from wording.

**Positive repaired path.** An encountered `U.Episteme` publication, publication form, MVPK face, carrier, rendering, or source-finding cue may guide work or reliance only to the support carried by the recovered exact project-side FPF kind and reference, actor or role, live work claim, reliance claim, or P2W load or position, affected work target, context, window, and source-supported claim or effect. The repaired outcome is the smallest admissible work or reliance statement plus the unsupported work claim or reliance claim still blocked.


Load posture by governing FPF pattern and exact project-side FPF kind and reference:

| Work or reliance posture | Use when | Minimum useful record |
| --- | --- | --- |
| Orientation or source-finding note | The encountered item is only a publication face, carrier, rendering, cue, search handle, learning aid, or reversible local probe trigger. | `encountered item; required claim or effect not yet supported; source to reopen; stop condition`. |
| Routine reliance note | The team needs ordinary bounded reliance without release, safety, compliance, delegated status, contested source, or cross-context reuse. | Live work claim, reliance claim, or P2W load or position; required claim or effect; actor or role; affected work target, context, and window; visible source ref; and reopen condition. |
| Load-bearing reliance path | The required claim or effect is external-impact, irreversible, release-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, revoked, status-bearing, generated-source-mediated, copied-source-mediated, provenance-mediated, contested, or cross-context. | Exact project-side FPF kind and reference with the live `A.10`, `A.6`, `B.3`, `A.2.9`, `A.2.8`, `A.21`, `A.20`, or `A.15.1` support fields needed for that claim or effect. |

A small A.15.4 restoration note is enough for the first posture:

| Field | Value |
| --- | --- |
| live work claim, reliance claim, or P2W load or position | Name the live work claim, reliance claim, P2W load, or P2W position exactly: method-family selection, selected method, method of work, work plan, planned work, actual `U.Work`, work result, result-measurement, release reliance decision, or non-work reliance claim. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record; actual execution becomes `U.Work` only after it occurs and is recorded under `A.15.1`; work-result measurement belongs with the evidence or result-measurement source. This row is a local restoration label unless it cites an existing FPF kind or governing FPF relation. |
| governing FPF pattern and exact project-side FPF kind and reference | Approval, permission, gate passage, role or status currentness, work occurrence, evidence support, assurance claim, boundary claim, or other exact claim or effect needed before that load, position, or claim can be treated as supported. The governing relation must be carried by the named FPF pattern and recovered project-side reference, not by a new `A.15.4` kind. |
| actor or role | Who would act or rely. |
| affected work target, context, and window | Release, service, person, role holder, work item, claim, tenant, environment, physical batch, construction element, machine state, or validity window affected by that class or claim. |
| claim-bearing episteme or episteme publication | The claim-bearing FPF kind is `U.Episteme` or a species such as `U.EpistemePublication`; if the encountered item is only a publication form, MVPK face, carrier, rendering, `PublicationUnit`, dashboard tile, copied text, credential view, generated explanation, API wording, or cue, name that exact kind separately. |
| exact project-side FPF kind and reference needed or safe next move | Source `U.Episteme`, source `U.EpistemePublication`, register entry, or exact project-side FPF kind and reference to reopen; status to refresh; reversible probe; role assignment accountable for exposing or repairing the missing source; or narrower admissible use. |
| stop or reopen condition | What blocks the work claim or reliance claim and what would reopen it. |

**Borrowed episteme/publication discipline.** A.15.4 borrows the `C.2.1`, `E.17`, and `A.16.0` distinction rather than minting a new generic `U.*` kind. The claim-bearing FPF kind here is `U.Episteme`; `U.EpistemePublication` is used only when that episteme is available as a published episteme with MVPK-face references. Publication forms, MVPK faces, carriers, renderings, `PublicationUnit` instances, and source-finding cues are separate kinds or roles in the case. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record such as `SlotFillingsPlanItem`; launch values and finalization values remain their own project records, decision logs remain gate or decision records, execution evidence remains evidence, and actual work occurrences remain `A.15.1` or `U.Work` matters.

When the required exact project-side FPF kind and reference is incomplete, choose one admissible degraded-operation move after naming the live work claim, reliance claim, or P2W load or position and the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect; pick the lightest move that preserves practical work and source recoverability:

1. Use the encountered item only for orientation or source-finding.
2. Reopen the required source `U.Episteme`, source `U.EpistemePublication`, register entry, or exact project-side FPF kind and reference, or refresh status or currentness.
3. Narrow actor or role, requested operation or work class, affected target, context, and window until the recovered source really covers the move.
4. Run a bounded reversible probe under an explicit `U.WorkPlan` when no external-impact reliance is being made.
5. Ask the role assignment accountable for the issuer, gate decision, evidence path, role record, status record, or boundary claim set to expose or repair the missing source.
6. Repair the `U.WorkPlan`, `U.MethodDescription`, dashboard label, source link, or boundary wording that made the overread plausible.
7. Proceed only inside the recovered scope and window.
8. Block only the work claim or reliance claim that lacks source support.

##### Repair assignment rule

**Broken-source repair assignment.** If the required exact project-side FPF kind and reference is unavailable to the acting user, assign only prospective repair work, request work, decision work, work-plan work, or source-gap work to the role assignment accountable for the issuer record, gate decision, evidence path, role record, status record, or boundary claim set. The acting user records the blocked work claim or reliance claim and the missing source relation to expose or repair, then proceeds only with the safe narrowed move available under recovered support. The repair request or source-gap note is not past evidence, approval, gate passage, performed `U.Work`, release permission, or assurance.


An encountered item may be a `U.Episteme`, a `U.EpistemePublication`, a publication form, an MVPK face, a carrier, a rendering, a `PublicationUnit`, or only a source-finding cue. Name that kind before using it. Do not treat a file, display, dashboard tile, model card, credential view, generated text, `PublicationUnit`, publication face, or carrier as the source claim, effect, work occurrence, gate decision, role record, status record, evidence relation, or assurance claim by presentation alone. If the encountered item exposes an exact project-side FPF kind and reference, use the exposed `GateDecision`, `SpeechAct`, evidence path, credential source, status source, work-occurrence record, or other exact FPF source directly; do not infer that support from the display face itself.

**Adversarial misuse guard.** Do not let release pressure, delegated pressure, compliance pressure, unsourced green-dashboard pressure, copied wording, or generated wording convert a cue into work support or reliance support. A properly designed dashboard tile may guide release when it is a current view of the relevant `GateDecision` plus evidence path and currentness path; pressure or color alone does not replace that source.


##### Exact project-side FPF kind and reference lookup table

Exact project-side FPF kinds and references by required claim or effect kind:


- cue-only orientation: use only for attention or source-finding; stay with `A.16` or `A.16.1` for pre-articulation cues or `A.6.A` for `A.6.A`-governed invitation. Cue-only orientation is not work guidance, work plan, gate passage, approval, work occurrence evidence, or assurance.

- issuing, approval, authorization, delegation, or revocation act: cite `A.2.9` `U.SpeechAct` or `SpeechActRef`, including act type, actor, role, affected work target or claim target, judgement context, window, carrier reference, evidence reference when currentness matters, and instituted effects if claimed; because `U.SpeechAct <: U.Work`, the same act can satisfy dated work-occurrence evidence only for that communicative act itself. It does not evidence the deployment, release, repair, inspection, or other operational work that the act approved, ordered, or described;
- role or status reliance: cite `A.2.1` or `U.RoleAssignment`, a status-changing `U.SpeechAct`, a governing context-state record, a credential proof or status result under `A.10`, or an `A.21` `GateDecision` when the status is gate-governed; do not infer a status kind from a label;
- deontic permission, obligation, prohibition, or recommendation-as-duty: cite `A.2.8` `U.Commitment` and the instituting `SpeechActRef` when provenance matters; if "permission" means admissibility predicate, gate passage, authorization act, role effect, status effect, credential status, cue, or advice, use `A.6.B`, `A.21`, `A.2.9`, `A.2.1`, `A.10`, `A.16`, or `A.6.A` according to the actual claim or effect kind instead;
- boundary, policy, API, schema, "allowed", "authorized", "approved", "recommended", or "guaranteed" wording: split the statement through `A.6` or `A.6.B`; use `A.6.C`, `A.2.3`, `A.2.8`, and `A.2.9` for agreement-like guarantee, SLA, or promise wording before work use or reliance use;
- gate decision or gate passage: cite `A.21` `OperationalGate(profile)`, `GateDecision`, `GateDecisionRationale`, `DecisionLogRef`, gate profile, gate version, check set, scope, window, and replay or freshness pins;
- constraint or flow-validity witness: cite `A.20` `ConstraintValidity` status, witness, `GateCheckRef.aspect = ConstraintValidity`, path, window, sentinel, and pins as applicable; this is not identical to a gate decision;
- release, deployment, or rollback work occurred: cite `A.15.1` dated `U.Work` occurrence and the `A.10` evidence carrier path; a gate decision or command-like cue is not execution evidence;
- evidence, provenance, authenticity, currentness, copied-source, or generated-source support: apply `A.10`; evidence support does not approve, permit, execute, pass a gate, or raise assurance by itself;
- assurance, readiness, safety, compliance, trust, release confidence, `R`, `F`, `G`, or `CL` increase: apply `B.3`;
- generated explanation: use `E.17.EFP` for explanation faithfulness or source-finding relation, then require `A.10` claim-bound source support for every operative claim that will be relied on.
- approval claim or effect split: if approval means someone approved something, cite `A.2.9` `U.SpeechAct` or `SpeechActRef`; if the approval institutes a deontic binding, cite `A.2.8` `U.Commitment` and the instituting act; if it means a gate passed, cite `A.21` `GateDecision` or `DecisionLogRef`; if it is being used as evidence that release or other work occurred, cite `A.15.1` dated `U.Work` plus `A.10`; if it is only approval wording in boundary, API, policy, or schema prose, split through `A.6` or `A.6.B`; if it is evidence of approval, apply `A.10`; if it is confidence because something was approved, use `B.3` only when a typed assurance claim is live.
- permission claim or effect split: if permission is a deontic relation, cite `A.2.8` `U.Commitment` and the instituting source; if it is an admissibility predicate, cite the `A.6.B` `A-*` claim; if it means gate passage, cite `A.21`; if it means an authorization act, cite `A.2.9`; if it changes or depends on role or status, cite `A.2.1` or status-changing support; if it means credential status, use `A.10`; if it is only a UI label, badge, dashboard display, or permission-looking wording, treat it as orientation or source-finding until the required exact project-side FPF kind and reference is recovered.
- authorization claim or effect split: if authorization means a speech act authorizing, cite `A.2.9`; if it means a policy or admissibility predicate over subject, requested policy operation or work class, affected resource or work target, context, and policy version, split through `A.6.B`; if it means gate decision or gate passage, cite `A.21`; if it means access proof, credential proof, status proof, or currentness, use `A.10`; if it means role assignment, role effect, or status effect, cite `A.2.1` or status-changing support; if it is being used to say execution happened, do not use authorization as evidence of execution, cite `A.15.1` dated `U.Work` plus `A.10` instead.


Return products for loop closure:

| Governing source relation used | Return product for this A.15.4 restoration | What the return product does not hide |
| --- | --- | --- |
| `A.6` or `A.6.B` | Typed claim IDs (`L-*`, `A-*`, `D-*`, and `E-*`) plus the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect. | Raw wording is not work support or reliance support. |
| `A.10` | Claim-bound evidence path, freshness posture, currentness posture, and admissible or non-admissible use for the attempted claim. | Evidence support is not approval, permission, gate passage, work occurrence, or assurance. |
| `B.3` | Typed assurance claim, no-assurance-use disposition, or rejected/downgraded assurance claim. | Assurance wording is not a generic trust label. |
| `A.21` | `OperationalGate(profile)`, `GateDecision`, `DecisionLogRef`, gate profile, gate version, scope, window, and replay or freshness pins. | Gate passage is not execution evidence or assurance. |
| `A.20` | `ConstraintValidity` status, witness, path, window, sentinel, and pins where live. | Constraint validity is not the gate decision itself. |
| `A.2.9` | `SpeechActRef` with act type, actor, role, affected work target or claim target, judgement context, window, and instituted effects if claimed. | A speech act is not deontic binding, gate passage, or operational work occurrence by itself; as work-occurrence evidence it supports only the communicative act that occurred. |
| `A.2.8` | `U.Commitment` deontic relation with accountable role, agent, content, object, window, and instituting source when needed. | Commitment is not proof that work occurred. |
| `A.15.1` | Dated `U.Work` occurrence plus evidence carrier path when relied on. | Work occurrence is not permission or assurance. |
| `E.17.EFP` | Explanation class, source-finding relation, and faithfulness relation over the source `U.Episteme` or source `U.EpistemePublication`. | Explanation is not operative source support without A.10 claim-bound evidence. |


Load-bearing work or reliance - especially external-impact, irreversible, release-bearing, role-bearing, status-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, contested, or assurance-bearing claim or effect - is admissible only for the actor, role, live work claim, reliance claim, P2W load, P2W position, affected work target or claim target, audience, scope, environment, version, policy context, operational mode, and time window for which required FPF-governed project support is recoverable. Cue-only, source-finding, learning, and bounded reversible probes stay lightweight and do not require a full source dossier.

Quick dispositions:


| Encountered case | First `A.15.4` disposition |
| --- | --- |
| Source-backed release dashboard tile | If the tile is a current dashboard view of `A.21` `GateDecision` or `DecisionLogRef` plus release target or work target, environment, scope, window, gate profile, gate version, and `A.10` evidence path, it may support gate-passage reliance for that release and environment. |
| Unsourced or stale release dashboard tile | Display or source-finding only until the current `GateDecision` or `DecisionLogRef`, release target or work target, scope, window, gate profile, gate version, and `A.10` evidence path are recoverable; use `B.3` only if an assurance claim is live. |
| Copied review summary or copied approval | Copied wording and copied-currentness posture at most; approval, authorization, permission, commitment, or work occurrence needs the original `A.2.9` `SpeechActRef`, `A.21` decision, `A.2.8` commitment, or `A.15.1` work source plus `A.10` evidence. |
| Delegation chain with forwarded approval | Each link names delegator, delegatee, delegated operation or work class, affected target, scope, window, source permitting delegation, subdelegation allowance if any, revocation state, currentness state, and evidence path. A forwarded approval is not delegated authority by copy alone. |
| Role, revocation, or status display | Resolve to role assignment, status-changing speech act, context-state record, credential proof or status result, or gate decision with freshness or revocation support; visual status cannot defeat a higher-priority revocation or supersession source. |
| Conflicting sources | Do not resolve by color, visual salience, copied wording, or apparent recency. Name source order, governing decision source, freshness policy, and supersession rule; the work claim, reliance claim, or effect is contested until resolved, while source-finding and bounded reversible probes remain available. |
| Credential badge or register-backed status view | Use the display as a publication of a credential source or status source, not the source itself. Find the governing status register or issuer, trust anchor, holder binding or subject binding, verifier context, relying context, proof or status result, revocation, freshness, and validity window. If the governing register entry itself creates or changes role, status, permission, duty, or gate state in the bounded context, cite that exact register or status-source entry and the `A.2.1`, `A.2.8`, `A.2.9`, `A.6.B`, or `A.21` source it depends on. Otherwise rely only on credential-currentness for that holder and context. |

| Rollback command-like cue | Treat as cue or `A.6.A`-governed invitation unless exact command, authorization, work occurrence, execution result, or gate support is recoverable. |
| Generated explanation says "authorized" | Explanation may help find sources; it does not issue, approve, revoke, commit, authorize, pass a gate, evidence execution, or raise assurance. A citation or source mention inside the explanation supports work use or reliance use only when the cited carrier supports that exact relied-on claim in the relying context under `A.10`. |

| Extracted source, rewrite, representation shift, explanation, then gate or release claim | Reopen the most directly claim-bearing exact project-side FPF kind and reference at the first lossy or non-commutative transform step; the gate claim or release claim waits for required transform, evidence, explanation, gate, or assurance support. |
| Repeated green-tile failures without recoverable source support | Treat recurrence as upstream source-system repair work: expose decision refs, fix dashboard semantics, add source links and currentness, revise boundary wording, or add review cues so the acting user is not repeatedly forced to reconstruct missing source support. |


##### Worked dashboard/approval examples

Worked dashboard and approval slice:

A release dashboard shows a green approval-looking tile for `Release-2026.05.08-prod`. If the tile is a current view of the relevant `GateDecisionRef` plus evidence path and currentness path, it may support bounded gate-passage reliance for that release target and window. Execution or deployment still requires an `A.15.1` work-occurrence source if the claim is that deployment happened. If the gate source is missing or stale, treat the tile as orientation and source-finding until the team can name the live release-work load, live release-work position, governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect, and exact project-side FPF kind and reference that carries the gate decision, evidence path, and currentness path.

| Step | Required move |
| --- | --- |
| Required project claim or effect kind | Release reliance, gate passage, compliance proof, assurance increase, evidence support, or currentness support. |
| Gate decision source | Cite the current `A.21` `GateDecision` or `DecisionLogRef`, gate profile, gate version, release target or work target, scope, window, and replay or freshness pins. Without that source, the tile is not release permission or gate passage. |
| Constraint or flow-validity source | Cite `A.20` `ConstraintValidity` status or witness only when the claim is about constraint or flow validity, not about the gate decision itself. |
| Evidence and currentness source | Use `A.10` for the dashboard query, carrier integrity, evidence refs, time, window, freshness stance, revocation stance, verifier context, relying context, and rival explanation such as stale display or copied status. |
| Assurance source | Use `B.3` only if the tile is being used to raise readiness, compliance, trust, safety, release confidence, `R`, `F`, `G`, or `CL`; otherwise no assurance tuple is live. |
| Admissible repaired use | With the decision and evidence path recovered, rely on gate passage only for the named release target or work target, environment, gate profile, gate version, time, and window; a claim that deployment happened still needs an `A.15.1` work-occurrence source. |
| Blocked overreads | The dashboard color does not create approval, permission, compliance proof, rollback success, work occurrence, or assurance by display. |

Approval memo green path:

An approval memo may support an approval claim when it exposes the `A.2.9` `SpeechActRef`, actor, role, affected release target or work target, judgement context, time, window, carrier refs, evidence refs, and instituted effect being claimed. That supports the bounded approval claim or effect only. It does not prove that release, deployment, rollback, or other work occurred; that execution claim still needs the dated `A.15.1` work-occurrence source plus any `A.10` evidence path required for the relying context.

Credential/status green path:

A credential or status response may support holder reliance, status reliance, or currentness reliance only inside the issuer or governing status register, holder binding or subject binding, verifier context, relying context, proof result or status result, revocation stance, freshness stance, and validity window that it exposes. It does not by itself support release, work occurrence, gate passage, engineering justification, evidence for underlying operational facts, or contextual permission; those uses require the exact project-side FPF kind and reference that governs that claim or effect.

Role prompts:

| Role in the situation | Prompt |
| --- | --- |
| Acting user | What can I safely do next without turning the encountered episteme or episteme publication into unsupported work support or reliance support? |
| Release engineer | Which `A.21` gate decision, decision log, release target, work target, and `A.15.1` work occurrence are separate here? |
| Issuer, gate, evidence, or role source | What source, status, decision ref, or evidence path must be exposed or repaired? |
| Auditor/reviewer | Which evidence path, decision ref, speech-act ref, commitment, work occurrence, or assurance claim must be recoverable? |
| Boundary author | Which words need typed claim IDs before they can guide work or reliance? |
| Manager | Is repeated ambiguity a source-system repair item rather than another manual check for the acting user? |
| LLM/tool user | Which exact project-side FPF kind and reference does the explanation help find, and which operative claims still need `A.10` support? |
| Security or compliance source | Which revocation, currentness, proof, status, source order, or supersession source must be exposed? |
| Model or data source | Which intended use, evaluation condition, version, window, limitation, and evidence path bound the model or data documentation? |
| Assurance reviewer | Which named claim is actually receiving an assurance posture, with what assurance tuple, evidence path, limitations, and reopen condition? |
Search aliases for A.15.4 include: approval, approval-looking display, authorization, authorization-looking display, permission, permission display, allowed wording, green dashboard, release tile, release readiness, model card, datasheet, data card, provenance, provenance mark, attestation, attestation label, credential, credential badge, generated explanation, copied review, copied approval, review summary, compliance-looking mark, delegation, delegation display, revocation, revocation status, gate passed, gate passage, rollback successful, rollback cue, and assurance label. These are search handles only; decide the carrying exact project-side FPF kind and reference and governing FPF pattern or source relation from the live work question or reliance question, not from the displayed word or carrier name or source name.

Work and reliance disposition map for authority-looking cases:

| Live question | Start in | First useful output |
| --- | --- | --- |
| Can this encountered episteme publication, publication face, carrier, rendering, or cue guide work or reliance? | `A.15.4` | Candidate next `U.WorkPlanning`, `U.Work`, or reliance move, governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect, minimum admissible next move, and exact project-side FPF kind and reference needed. |
| Is the problem boundary, policy, API, schema, or connector wording? | `A.6` or `A.6.B` | Typed `L-*`, `A-*`, `D-*`, and `E-*` claims before the work claim or reliance claim is used. |
| Is the problem evidence, currentness, provenance, credential status, generated-source support, copied-source support, or source-chain recovery? | `A.10` | Claim-bound evidence path, currentness path, and admissible or non-admissible use. |
| Is the problem assurance, readiness, safety, compliance, trust, release confidence, `R`, `F`, `G`, or `CL` posture? | `B.3` | Typed assurance claim, no-assurance-use disposition, or downgraded or rejected assurance use. |

Display guidance for bounded status: a visible status meant to guide work should expose source type, exact ref or link, freshness, window, scope, unsupported work claim, unsupported reliance claim, and unsupported effect. For example, prefer `Gate check passed; GateDecisionRef; release target; environment; window; not compliance proof, rollback success, or assurance increase` over a bare approval-looking label.

Incident-learning fields for authority-looking overread: encountered episteme or episteme publication, live work claim, reliance claim, P2W load, or P2W position, governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect, actor, role, affected work target or claim target, context, window, missing or stale source `U.Episteme`, source `U.EpistemePublication`, register entry, or exact project-side FPF kind and reference; governing FPF relation or role assignment accountable for exposing or repairing that missing source, plausible overread, safe disposition used now, and upstream repair item for the source, dashboard, explanation, credential view, boundary wording, publication face, or carrier.

Contestability and redress path: when an authority-looking case affects person or team status, access, assignment, responsibility, release blockage, compliance posture, or safety-impacting work, name the review path or redress path before the work claim or reliance claim hardens. The path should name the disputed source or claim, the role assignment accountable for refreshing or correcting that source, the evidence path or status path to reopen, the safe interim disposition, and the time and window for review.


Lintable overread cues:

| Lint signal | Exact governing exit |
| --- | --- |
| `approved`, `authorized`, `allowed`, `recommended`, or `guaranteed` in boundary, API, schema, or policy wording | Split through `A.6` or `A.6.B` into `L-*`, `A-*`, `D-*`, and `E-*`; use `A.6.C`, `A.2.8`, and `A.2.9` for agreement-like wording where live. |
| Dashboard tile, status color, or release tile used as release evidence or gate passage | Require `A.21` `GateDecision` or `DecisionLogRef` plus `A.10` evidence path and currentness path. |
| Credential screenshot or badge used as permission, authorization, role support, or status support | Require `A.10` issuer, holder, verifier, status, currentness, and relying-context support, then exact `A.2.8`, `A.2.9`, `A.2.1`, `A.6.B`, or `A.21` source for the required permission, authorization, role, status, gate claim, or gate effect. |
| Generated explanation uses `authorized`, `approved`, or similar wording | Use `E.17.EFP` for explanation relation and source-finding relation and `A.10` claim-bound source support; issue, approval, gate, and commitment claims still need `A.2.9`, `A.21`, or `A.2.8`. |
| Model card, datasheet, label, or note cited as readiness, safety, compliance, or release confidence | Require a typed `B.3` assurance claim, intended-use match, evaluation condition, limitations, and `A.10` evidence path. |
| Provenance or attestation label cited as truth, safety, release, or permission | Require `A.10` bounded provenance claim or process claim plus separate evidence for truth, safety, release, permission, or assurance. |
| Evidence, assurance, gate, or work-occurrence words without the exact project-side FPF kind and reference that carries that claim or effect | Recover the `A.10`, `B.3`, `A.21`, or `A.15.1` support fields respectively before the work claim or reliance claim is used. |

Stress cases for practice:

| Case | Expected A.15.4 disposition |
| --- | --- |
| Green release dashboard tile with no `GateDecisionRef`. | Source-finding only; recover `A.21` decision or decision log plus `A.10` evidence before gate-passage reliance. |
| Copied approval from last month. | Recover original `A.2.9` `SpeechActRef`, currentness, freshness, and any live `A.2.8` commitment or `A.21` gate source. |
| Credential badge screenshot after revocation. | Treat as contested credential-currentness; use `A.10` issuer, holder, verifier, status, and revocation path and do not infer permission. |
| Generated explanation says `authorized by policy`. | Use `E.17.EFP` for explanation and source-finding and `A.10` claim-bound support; issuing, gate, and commitment claims still need their own sources. |
| Boundary wording says `guaranteed approved for production`. | Split through `A.6` or `A.6.B`; if agreement-like or promise-bearing, unpack through `A.6.C`, `A.2.8`, and `A.2.9`. |
| Dashboard says green while decision log says blocked. | Treat as conflicting sources; name source order, governing decision source, freshness policy, and supersession rule before the work claim or reliance claim is used. |

### A.15.4:4 - Conformance Checklist

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A15.4-1 (Work-relevant source restoration)** | Before an authority-looking case guides work or reliance, a conforming `A.15.4` use SHALL produce the ordinary source-restoration note: encountered item, live work or reliance claim, P2W load or position, governing FPF pattern, exact project-side FPF kind and reference needed, admissible next project move now, and blocked overread. It SHALL identify the neighboring FPF pattern and exact project-side FPF kind and reference that actually carry the requested approval, permission, status, evidence, gate, assurance, or work-occurrence support; if that source is absent or stale, mark only the unsupported reliance as orientation-only, contested, reopened, or blocked. Fuller source-support fields open only when the live use, dispute, or reliance case requires them. Any new repair request, future decision request, prospective work-plan entry, or explicit source-gap note is prospective and SHALL NOT be used as retroactive evidence, approval, gate passage, performed `U.Work`, release permission, or assurance. A conforming `A.15.4` use SHALL NOT absorb evidence, assurance, boundary wording, gate decision, role or status, commitment, speech-act, or work-occurrence semantics from `A.10`, `B.3`, `A.6`, `A.2.1`, `A.2.8`, `A.2.9`, `A.20`, `A.21`, or `A.15.1`. | Prevents displays, badges, copied text, generated explanations, and composed chains from becoming authority by appearance while keeping ordinary use cheap. |
| **CC-A15.4-2 (P2W publication use boundary)** | A principle scheme, functional diagram, scenario, screen, or explanation that makes a P2W chain readable SHALL NOT be used as performed `U.Work`, work authority, evidence, gate passage, engineering justification, or release permission by publication alone. | The project use names the exact `A.15` object it supports: method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, or result measurement; unsupported claims require their own exact project-side FPF kinds and references. |

### A.15.4:5 - Common Anti-Patterns and How to Avoid Them

- **Authority-looking case as source, work overread, role overread, or status overread.** Do not treat a dashboard tile, credential display, copied approval, generated explanation, provenance label, command-like cue, or composed source chain as approval, permission, gate passage, role currentness, status currentness, work occurrence, evidence, or assurance by appearance. First name the live work claim, reliance claim, P2W load, or P2W position, then recover the governing FPF pattern and exact project-side FPF kind and reference that actually carry the requested approval, permission, status, evidence, gate, assurance, or work-occurrence support, or block only that unsupported reliance.

### A.15.4:6 - SoTA Alignment

**SoTA alignment rule.** Read the row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and relations of this pattern.

| Claim need | Source idea and current source | Current source reference | Local FPF invariant and practical local test | Adopted invariant, adapted invariant, and rejected shortcut |
| --- | --- | --- | --- | --- |
| Dynamic authorization or policy-response displays need exact operation, target, context, and window support. | Dynamic authorization practice separates subject, requested operation, affected target, context, and window before a relying move is allowed. | NIST Zero Trust and dynamic authorization practice; Cedar policy language; Zanzibar-style relation authorization; source maturity = current standards, specifications, and widely used technical practice. | The restoration note names the live work claim, reliance claim, P2W load, or P2W position, the affected work target or claim target, policy version, context, and time window before treating a visible allow response, deny response, or policy response as support. | **Adopt, adapt, reject.** Adopt bounded currentness and source-support invariants; adapt them through exact FPF project records; reject treating policy-looking output as permission or work authority by display. |
| Credential or register-backed status needs issuer, holder, verifier, status, currentness, and relying-context support. | Credential and status practice separates issuer, holder binding or subject binding, verifier context, relying context, proof result or status result, governing register entry, revocation, freshness, and validity window. | W3C Verifiable Credentials and digital identity or register-backed status practice; source maturity = current specifications and technical practice. | A credential view or status tile can support only the holder claim, status claim, or currentness claim whose issuer, register, proof result or status result, revocation, freshness, and relying context are recoverable. | **Adopt, adapt, reject.** Adopt status-currentness separation; reject reading a badge, screenshot, or register excerpt as role, status, permission, gate passage, or work support without the governing FPF pattern and exact project-side FPF kind and reference. |
| Provenance and attestation marks need source support and process support without becoming truth, release, or work evidence. | Provenance and attestation practice separates origin support, process support, build claim, supply-chain claim, and verification metadata from truth of downstream claims or release permission. | C2PA content provenance; SLSA and in-toto attestations; source maturity = current standards, specifications, and widely used practice. | A provenance or attestation mark remains source support or process support until `A.10`, `B.3`, `A.20`, `A.21`, `A.15.1`, or another exact source relation carries the downstream claim. | **Adopt, adapt, reject.** Adopt source traceability and process traceability; reject provenance-mark-as-truth, release permission, gate passage, assurance, or work occurrence. |
| Change, gate, release, and approval displays need decision, schedule, and executed-work separation. | Release and change practice separates approval acts, authorization acts, gate decisions, planned schedules, and executed work. | ITIL 4 Change Enablement and current release or change practice; source maturity = current practitioner guidance plus mature service practice. | A dashboard or approval-looking display must expose the `GateDecision`, `SpeechAct`, `Commitment`, `U.WorkPlan`, or `A.15.1` work-occurrence source that carries the exact claim or effect. | **Adopt, adapt, reject.** Adopt decision, schedule, and executed-work separation; reject a green tile, copied approval, or generated explanation as rollout, release, or work support by appearance. |

**Digital-identity and provenance boundary.** The W3C Verifiable Credentials, C2PA, SLSA, in-toto, Cedar-style, Zanzibar-style, NIST, and ITIL sources are used for currentness, status, provenance, authorization-support fields, and change-practice fields. They do not turn a visible credential, provenance label, attestation, policy response, register excerpt, or dashboard state into work occurrence, gate passage, permission, assurance, release, or project claim support without the exact project-side FPF kind and reference required by `A.15.4`, `A.15`, `A.10`, `B.3`, `A.20`, or `A.21`.

The nearest recovery anchors are the worked dashboard and approval examples, `CC-A15.4-1`, `CC-A15.4-2`, `A.10`, `B.3`, `A.20`, `A.21`, `A.2.8`, `A.2.9`, and `A.15.1`. If a SoTA row cannot be recovered through those local checks, do not let the source citation stand in for the local `A.15.4` rule.

### A.15.4:7 - Relations

* **Cluster relation:** `A.15.4` is a cluster member under `A.15` for work-relevant source restoration; it does not replace the A.15 role, method, plan, and work kernel.
* **Uses:** `E.17:5.1b` and `E.17:5.1c` source-support and use vocabulary, `E.17.EFP` for generated-explanation faithfulness and source-finding, `A.6`, `A.6.B`, and `A.6.C` for boundary, policy, API, and schema wording, `A.10` for evidence, currentness, provenance, and credential status, `B.3` for engineering justification claims, `A.20` for constraint validity, `A.21` for gate decisions, `A.2.8` for commitments, `A.2.9` for speech acts, and `A.15.1` for dated `U.Work` occurrences.
* **Returns to:** `A.15` when the remaining live question is role, method, plan, and work alignment rather than source restoration.

### A.15.4:7a - C.29 MLA relation

> If a mathematical lens appears in work-relevant source restoration, use `C.29` only to state why the lens helps expose or bound an encountered item such as a visible item, generated wording, dashboard cue, copied phrase, publication form, MVPK face, carrier, rendering, `PublicationUnit`, or source-finding cue. `A.15.4` still governs the exact source item, visible item, restoration or reopen condition, reliance support, and whether that item can support work. Method choice, plans, and performed work return to `A.15` and `A.15.1`; lens adequacy does not turn a cue, rendering, or diagnostic phrase into source support.

### A.15.4:End
## A.16 - Language-State Transduction Coordination

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state move coordination.

**Start here when.** Your first honest content is a cue, not yet a claim, requirement, method, or work record, and you need to name the next admissible move without pretending that one downstream governing pattern has already taken over.

**First output.** A small typed move note or early preservation-to-routing note that names the source publication form, target publication form, target governing pattern, and MVPK face where that face matters.

**Typical next governing patterns.** `A.16.1` for early preservation, `B.4.1` for route publication, `B.5.2.0` for cue-derived abductive prompting, receiving endpoint governing patterns such as `A.6.P`, `A.6.A`, and `A.6.Q`, and `A.16.2` when the right move is reopen/backoff/respecify/retire.

**Common neighboring-pattern mistakes.** If history itself must be published as an accountable trajectory, use `A.16.0`; if you are already doing slot-explicit semantic repair, apply `A.6.P`, `A.6.Q`, or `A.6.A`; if the publication target is a graph publication in itself, use `E.18`.

### A.16:1 - Problem frame
Once positions in the declared language-state `U.CharacteristicSpace` chart from `C.2.2a` are explicit, teams still need admissible move kinds for how governed `U.Episteme` publications change, narrow, reopen, or hand off across that chart. Those moves must not collapse into a second formality-only climb, a generic one-pass process story, or an invisible sequence of governing pattern replacements.

A single local move note is often enough. Only some cases need a full trajectory account. The coordination pattern therefore has to stand independently while still remaining compatible with `A.16.0` when lineage, branch structure, loss notes, or handoff history become governance-relevant.

### A.16:2 - Problem
Without a dedicated coordination pattern, authors either misuse `F0-F9`, force every cue into anomaly/problem language too early, let reopen and backoff happen informally with no explicit guards, or over-wrap every local move in a meta-account that should have remained optional.

### A.16:3 - Forces
| Force | Tension |
|---|---|
| **Coordination vs duplication** | Coordinate moves over the declared language-state chart without recreating `A.19` or `E.18`. |
| **Local sufficiency vs history visibility** | Let a typed local move note stand independently, while still supporting richer history publication when that history matters. |
| **Early capture vs endpoint discipline** | Admit low-articulation governed `U.Episteme` publications without losing endpoint-classification discipline. |
| **Forward development vs admissible retreat** | Support formalization and operationalization, but also reopening, sketch-backoff, respecification, and admissible retirement. |

### A.16:4 - Solution
`A.16` governs only admissible move kinds, their guards, and docking rules for how governed `U.Episteme` publications may be related across declared language-state positions. It does **not** govern `F`, does **not** define the trajectory-account semantics itself, and does **not** define a rival graph calculus beside `E.18`.

A conforming move may be published as a local move note without any `U.LanguageStateTransductionTrajectory` wrapper. `A.16.0` is used only when lineage, branch structure, loss notes, supersession, retirement, bridge-sensitive history, or governing pattern handoff has governance value that should be published as an account.

Observation itself is a precursor condition typically published through `B.4.1`. `A.16` move kinds begin once a cue is deliberately noticed, stabilized, route-published, reopened, formalized, operationalized, respecified, or retired under explicit move discipline.

#### A.16:4.1 - Governed move family
| Move | What it does | Typical source condition | Typical publication effect |
|---|---|---|---|
| `notice` | marks that a low-articulation cue is being deliberately preserved | low or unstable articulation | cue preservation becomes explicit enough for early publication work |
| `stabilize` | makes the local shape steadier without forcing route or endpoint choice | cue already noticed | cue nucleus, anchors, or witness structure become steadier |
| `route` | publishes downstream route plurality or a selected route through an explicit route-bearing form | stabilized cue exists | `RoutedCueSet` or equivalent route-bearing publication makes route state explicit |
| `projection` | publishes route-bounded partialization without pretending full endpoint governance | route is explicit and one aspect is being foregrounded | a typed route-bounded publication form is emitted on an existing MVPK face, with loss notes and reopen conditions |
| `formalize` | increases explicit symbolic or normal-form structure | articulation threshold is met | a publication form with higher articulation or closure is published; new evidence-generation crossings stay visible if required |
| `operationalize` | turns a selected line toward method, work, or gate use | method, work, or gate-facing line exists | operational hooks become explicit; work crossings stay visible if new world-facing work is required |
| `reopen` | relaxes closure while preserving the current family if possible | route or frame no longer holds cleanly | closure drops and rivals re-open |
| `sketchBackoff` | moves to an exploratory cue-bearing publication form | endpoint-bound, method-facing, work-facing, or gate-facing publication form over-commits the current publication | exploratory cue-bearing form becomes admissible again |
| `respecify` | keeps the broad family but revises framing scaffold, facet-profile reading, or route specification | current framing remains plausible but is stated wrongly | a new framing scaffold or route specification replaces the old one while continuity stays explicit |
| `retire` | declares that a cue, route-bearing publication, or branch is no longer current or no longer worth preserving | better-supported successor exists, supporting grounds have collapsed, or authority has been withdrawn entirely | retirement or withdrawal becomes explicit together with successor or no-successor note |

`A.16` governs these **move names**, not the publication forms that may result from them. `U.PreArticulationCuePack`, `RoutedCueSet`, `U.AbductivePrompt`, and endpoint-pattern-governed `U.EpistemePublication` forms are governed publication forms; they are not move kinds.

Here `projection` remains the move name, but its reading is tightened: it is route-bounded partialization. The resulting publication must be a **typed publication form** rendered on an existing MVPK face. Naming only the face is insufficient; naming only an untyped placeholder is insufficient.

`respecify` is intentionally narrower than semantic repair. In `A.16`, it may change framing scaffold, route specification, or facet-profile reading while preserving the broad family. Slot-explicit semantic rewrite and endpoint-local lexical repair remain with receiving governing patterns such as `A.6.P`, `A.6.Q`, and `A.6.A`.

#### A.16:4.2 - Guard discipline
Move guards are stated over named facets from `C.2.LS`, together with witnesses, scope, and `GammaTime` selectors where needed. In practice this means explicit reference to `AE` (`C.2.4`), `CD` (`C.2.5`), `LanguageStateAnchoringMode` (`C.2.6`), and `LanguageStateRepresentationFactorBundle` (`C.2.7`), either facetwise or through one published facet profile. No move may be justified by vague prose such as "the idea matured" without naming what changed in articulation, closure, anchoring, representation, or route state.

#### A.16:4.3 - Docking discipline
After `route`, `projection`, `formalize`, or `operationalize`, the next admissible publication shall keep three layers distinct:

- the **publication form** now being issued (for example `U.PreArticulationCuePack`, `RoutedCueSet`, `U.AbductivePrompt`, or a named `U.EpistemePublication` form governed by a receiving endpoint pattern);
- the **governing pattern** that governs that form (`A.16.1`, `B.4.1`, `B.5.2.0`, `A.6.P`, `A.6.A`, `A.6.Q`, `B.5.2`, `A.15`, `C.25`, or another named governing pattern);
- the **MVPK face**, when rendering matters, that carries that publication.

Naming only the governing pattern is insufficient because governing patterns are not forms. Naming only the face is insufficient because faces are not forms. An admissible move note states the pattern-governed publication form first, then the governing pattern, then the face if the face matters.

#### A.16:4.4 - Effect-free versus work-requiring moves
Some `formalize` and `operationalize` moves are effect-free epistemic rewrites or moves to publication forms with higher articulation or closure over already available grounds. Others require new measurements, experiments, instrumentation, execution, or other `U.Work`. When the latter happens, the move note shall expose the crossing or handoff explicitly; `A.16` does not pretend that world-facing work occurred inside the language layer.

#### A.16:4.5 - Move-note threshold and path publication discipline
A typed local move note is sufficient when a small move or short move chain can be kept reconstructible without publishing extra lineage machinery.

Use `A.16.0` only when at least one of the following is load-bearing:

- derivation, supersession, fork, merge, or retirement structure;
- a multi-move history whose compression would hide governing pattern or authority changes;
- visible loss notes or reopen conditions spanning more than one move;
- responsibility handoff or bridge/viewpoint entry that depends on upstream history.

If the history itself must be published as a graph publication, reuse `E.18`. `A.16` governs move admissibility; `A.16.0` packages trajectory accounts; `E.18` governs graph publication of paths.

### A.16:5 - Archetypal Grounding
**Tell.** A language-state move is not "the episteme became better". It is a typed transduction: articulation rose, closure narrowed, route plurality was published, one route was foregrounded, a framing scaffold was replaced, or a branch was admissibly retired.

**Show (System).** An operator alert note about a disturbance may go `notice -> stabilize -> route -> operationalize`, then later `reopen` when counter-evidence arrives, or `retire` one branch when a better-supported successor line takes over.

**Show (Episteme).** An inquiry cue pack about a felt or trace-anchored discrepancy cue may go `notice -> stabilize -> route -> projection -> formalize`, or `reopen -> sketchBackoff -> respecify` if the chosen framing over-commits.

### A.16:6 - Bias-Annotation
The pattern biases authors toward explicit move-typing and away from folk stories such as "it naturally matured". That bias is intentional.

### A.16:7 - Conformance Checklist
- `CC-A.16-1` `A.16` **MUST NOT** redefine `F` or publish a second formality-only climb.
- `CC-A.16-2` A conforming move note **MAY** stand alone; `A.16.0` **SHALL NOT** be treated as mandatory wrapper syntax for every move.
- `CC-A.16-3` Every move kind **SHALL** name its preconditions and postconditions over explicit language-state facets, route state, or authority state.
- `CC-A.16-4` Publication form, governing pattern, and MVPK face **SHALL NOT** be collapsed into one unnamed target.
- `CC-A.16-5` Multi-route state inside one governed member **SHALL NOT** be confused with lineage fork across several successor members.
- `CC-A.16-6` `respecify` **SHALL NOT** be used to hide slot-explicit semantic repair that belongs to later repair governing patterns.
- `CC-A.16-7` Retreat or retirement **SHALL** preserve, withdraw, or discard prior witnesses and authority explicitly.
- `CC-A.16-8` Published path structures **SHOULD** reuse `E.18` when a graph publication is needed.
- `CC-A.16-9` `AuthorityState` and `EndpointAdmissionProfile` reuse **SHALL NOT** be treated as new governing patterns, new route-bearing forms, or substitutes for gate or work state.
- `CC-A.16-10` A summarized multi-move publication **SHALL** keep intermediate governing pattern transitions reconstructible; otherwise the case must reopen or publish richer history.

### A.16:8 - Common Anti-Patterns and How to Avoid Them
- **Trajectory-wrapper inflation.** Do not wrap every local move in `A.16.0`. Publish a local move note unless history has lineage governance value.
- **Governing-pattern-as-form collapse.** Do not write as if `A.6.P`, `B.5.2`, or `A.15` were publication forms. Name the pattern-governed form and the governing pattern separately.
- **Form-face collapse.** Do not treat an MVPK face as if it were the publication form itself. Name both when both matter.
- **Irreversible maturity story.** Reopen, sketch-backoff, respecify, and retirement are admissible moves, not failures of the trajectory discipline.
- **Silent branch retirement.** Do not let one route or branch disappear without a retirement or supersession note.
- **Route/fork confusion.** Several live routes in one `RoutedCueSet` are not yet a lineage fork.

### A.16:9 - Consequences
The benefit is a clear governing pattern for language-state transductions and an admissible place for both tightening and retreat without governing pattern blur. The trade-off is more explicit move bookkeeping.

### A.16:10 - Rationale
This separation keeps `C.2.3` as the sole governing pattern of formality while `C.2.2a` / `A.19` define position semantics, `A.16.0` packages only the history that deserves publication as an account, and `A.16` defines move admissibility.

### A.16:11 - SoTA-Echoing
**Claim 1.** Best-known current incident-response, exploratory design, and inquiry practice treats advance, backoff, reopening, and retirement as governed transitions rather than as one irreversible maturity climb.

**Practice source, local alignment, and adoption decision.** Contemporary incident review, exploratory design, and inquiry practice after 2015 keeps rollback, reopen, and retirement explicit because otherwise later readers over-credit earlier low-articulation forms. This pattern **adopts** explicit retreat and retirement, **adapts** them to typed publication forms, route states, and authority states, and **rejects** the still-popular shortcut where every change is narrated as one-way maturation.

**Claim 2.** Best-known current provenance, path-publication, and model-evaluation practice distinguishes a local transition note from a heavier published history account.

**Practice source, local alignment, and adoption decision.** Contemporary provenance and evaluation practice separates lightweight transition marking from heavier account publication when branch structure, loss notes, or handoff history become governance-relevant. This pattern **adopts** that separation, **adapts** it through the `A.16` / `A.16.0` / `E.18` split, and **rejects** both extremes: wrapping every move in a mandatory trajectory wrapper and compressing a governance-relevant move history into one vague maturity sentence.

**Local stance.** The load-bearing SoTA claim for this pattern is narrow: admissible language-state movement needs typed move notes, explicit authority effects, and explicit retreat/retirement options, but it does not need a mandatory formality climb or a mandatory wrapper around every move.

### A.16:12 - Relations
- Builds on: `C.2.2a`, `C.2.LS`, `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `A.18`, `A.19`.
- Coordinates with: `A.16.0`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `A.6.P`, `A.6.A`, `A.6.Q`, `E.18`.
- Constrains: language-state move publication and docking.

### A.16:13 - Admissible Move Matrix

#### A.16:13.1 - Typical publication consequences
| Move | Typical source publication state | Typical resulting publication state or form | What must become explicit |
|---|---|---|---|
| `notice` | observation trace, low-articulation cue, provisional note | preservation-worthiness of the cue becomes explicit | why the cue counts as worth preserving |
| `stabilize` | low-articulation preserved cue | `U.PreArticulationCuePack` or equivalent early preservation form becomes admissible | cue nucleus, anchors, witnesses, and preservation rationale |
| `route` | cue pack or stabilized note | `RoutedCueSet` or equivalent route-bearing publication becomes admissible | route plurality, selected route if any, route rationale, route authority state |
| `projection` | routed cue or selected route | a typed route-bounded publication form rendered on an existing MVPK face | what is foregrounded, what is omitted, and how reopen remains admissible |
| `formalize` | explicit but not yet formal-enough publication | a named `U.EpistemePublication` form with higher articulation or closure governed by a later formal pattern becomes admissible | new symbolic or slot structure and governing-pattern entry |
| `operationalize` | method-facing, work-facing, or gate-facing publication | a method-facing, work-facing, or gate-facing `U.EpistemePublication` form governed by a later method, work, or gate pattern becomes admissible | hook governing pattern, guard, authority basis, and work crossing if any |
| `reopen` | route-bearing or endpoint-bound publication | same family with reduced closure | which rivals reopen and what authority falls |
| `sketchBackoff` | over-rigid form | exploratory cue-bearing form such as `U.PreArticulationCuePack` or `RoutedCueSet` | withdrawn authority and retained witnesses |
| `respecify` | plausible family under wrong framing scaffold | same family with revised framing scaffold or route specification | replaced framing commitments and invariants that stay fixed |
| `retire` | cue pack, route-bearing publication, or branch | retired / withdrawn state with successor or no-successor note | why continuation stopped and what now carries authority |

#### A.16:13.2 - Invariance reminder
An admissible move may change articulation, closure, representation, route, authority, or publication form, but it shall not silently rewrite governing pattern boundaries. A move is not permission to retype a cue into any convenient governing pattern.

### A.16:14 - Worked Move Notes

#### A.16:14.1 - Incident-control move note
An operator alert note about a production disturbance may move:

`notice -> stabilize -> route -> operationalize`

The alert note does not need to become an anomaly statement immediately. It may first become a cue pack, then a routed cue set, and only then a typed operational form under the receiving governing pattern.

#### A.16:14.2 - Inquiry move note
An inquiry cue pack about a model-vs-observation discrepancy may move:

`notice -> stabilize -> route -> projection -> formalize`

Later, if the selected framing over-commits, the admissible continuation may be:

`reopen -> sketchBackoff -> respecify`

#### A.16:14.3 - Retired branch
A routed cue set may initially keep both evaluative and abductive routes live. If later review shows the evaluative branch was unsupported, the admissible continuation is not silent disappearance but explicit retirement of that branch, while the abductive branch remains current.

#### A.16:14.4 - False-maturity leap to reject
The following is not admissible:

`notice -> gate decision`

unless explicit intermediate publication and governing pattern transitions justify it. The trajectory discipline exists precisely to block such invisible leaps.

### A.16:15 - Authoring and Review Guidance

#### A.16:15.1 - Author prompt
When naming a move, the author should say:

- what the source publication form is,
- what the target publication form is,
- which governing pattern governs the target form,
- which MVPK face matters if rendering matters,
- which facet or route-state change justifies the move,
- what authority effect follows,
- and what remains invariant.

#### A.16:15.2 - Review prompt
A reviewer should ask:

- is the move a real transduction or just rhetorical relabeling?
- does the move preserve witnesses and route provenance appropriately?
- is route plurality being confused with lineage fork?
- did a receiving governing pattern silently absorb the publication too early?
- if retreat or retirement occurred, was the authority drop made explicit?

#### A.16:15.3 - Integration reminder
When path publication becomes important as a graph publication in itself, move semantics stay in `A.16`, the optional history package stays in `A.16.0`, and the path publication still belongs to `E.18`.

### A.16:16 - Migration and Boundary Notes

#### A.16:16.1 - Migration from old formality-only climb talk
Older prose that narrates a cue as moving from "informal to formal" should be unpacked into the relevant `A.16` move plus the relevant facet, route-state, and authority changes. A single-factor maturity story is not enough.

#### A.16:16.2 - Boundary reminder
If authors find themselves using `A.16` to justify measurement admissibility, bridge substitution, endpoint ontology, or slot-explicit semantic repair, they have crossed out of this governing pattern's scope.

### A.16:17 - Move Package Discipline

Publish moves as small typed transduction notes rather than as narrative adjectives.

#### A.16:17.1 - Minimal move note
A conforming move note should name:

- the **source publication form**,
- the **target publication form**,
- the **target governing pattern**,
- the **move kind**,
- the **facet or route-state changes** that justify the move,
- the **authority effect**,
- and the **witnesses or traces** that preserve continuity.

If those fields already make the move reconstructible, the note does not need `A.16.0`.

#### A.16:17.2 - Source and target must both be typed
"The episteme was refined" is insufficient. `A.16` requires a typed source publication form and a typed target publication form so governing pattern boundaries stay visible.

#### A.16:17.3 - Witness continuity
Keep continuity explicit when anchors, contrasts, traces, or exemplars survive. If continuity breaks, state the break directly rather than smoothing it over in maturity prose.

### A.16:18 - Authority, Route Plurality, and Fork Rules

The pattern is not just about movement; it is about admissible movement under explicit authority boundaries.

#### A.16:18.1 - Multi-route state versus lineage fork
A **multi-route state** means one governed member still keeps several downstream directions live inside one publication such as `RoutedCueSet`.

A **lineage fork** means separate successor members have already been published, each with distinct authority, losses, and future handoff semantics.

The first is plurality inside one member. The second is explicit branching of lineage. Reviewers shall not treat them as the same lineage relation.

#### A.16:18.2 - Four route / authority states
A governed publication after route work is usually in one of four states:

- **open plurality** - several downstream directions remain live;
- **selected-route-before-endpoint-publication** - one route is preferred, but the `U.EpistemePublication` is still an early or seam publication form;
- **endpoint-pattern-publication-issued** - a named endpoint pattern now governs the relevant `U.EpistemePublication` form and responsibility handoff;
- **retired / withdrawn** - the publication or branch is no longer current and survives only as historical continuity.

Confusing these states is one of the main causes of premature endpoint language.

#### A.16:18.3 - `AuthorityState` extraction note
The four states above may be reused as `AuthorityState`, an extracted shared profile for corridor coordination and review.

That extraction does **not** create a new governing pattern. It reuses the state vocabulary already pattern-governed here for later cross-references in `B.4.1`, `B.5.2.0`, `A.6.P`, `A.6.Q`, `A.6.A`, and `A.15`.

`AuthorityState` names authority posture after route work. It does not replace `routeDecision`, `selectedRoute`, `routeAuthorityState`, route-bearing publication governance, gate state, or work-execution state. Any `endpoint-pattern-publication-issued` state still names the downstream governing pattern and governed `U.EpistemePublication` form explicitly.

#### A.16:18.4 - Authority may rise, stay bounded, fall, or retire
A move may:

- **raise authority**, as when a routed cue becomes an admissible `U.EpistemePublication` form governed by a named endpoint pattern;
- **keep authority bounded**, as when a route-bearing publication clarifies one route without claiming endpoint governance;
- **lower authority**, as when reopening or sketch-backoff withdraws prior closure or route force;
- **retire authority**, as when a branch or publication is explicitly withdrawn from current use.

The authority effect should be named as carefully as the move kind itself.

#### A.16:18.5 - Boundary to governing pattern replacement
`A.16` never authorizes a silent governing pattern replacement. If a route crosses into `A.6.P`, `B.5.2`, `A.15`, `C.25`, or another endpoint governing pattern, that governing pattern and the pattern-governed publication form must be named explicitly. `A.16` coordinates the crossing; it does not absorb the destination governing pattern's semantics.

#### A.16:18.6 - `EndpointAdmissionProfile` extraction note
The corridor can reuse an `EndpointAdmissionProfile` as a declarative pattern-derived profile for admissible handoff from language-state publications to receiving governing patterns.

That profile is stated over already pattern-governed conditions: declared language-state positions in `C.2.2a`, facet readings in `C.2.LS` and `C.2.4`-`C.2.7`, explicit route state in `B.4.1`, prompt-readiness in `B.5.2.0`, and witness or grounding conditions that are already visible in the publication chain.

`EndpointAdmissionProfile` decides whether handoff is admissible; it does not govern the downstream publication form itself. A relation-like skeleton may therefore be admitted toward `A.6.P`; an explicit open question with rival-set may be admitted toward `B.5.2.0`; evaluative or `A.6.A`-inviting publication content may be admitted toward `A.6.Q` or `A.6.A`; executable docking may be admitted toward `A.15`.

No admission result makes a receiving governing pattern optional. Tone, style, or mere apparent explicitness is never sufficient by itself; the relevant governing pattern conditions still have to be named and met.

### A.16:19 - Worked Failure and Recovery Cases

#### A.16:19.1 - Premature endpoint capture
A low-articulation cue is observed and quickly described as if it were already a requirement. Under `A.16`, this is rejected because the move history is missing: the publication should first be noticed, stabilized, and route-published. The recovery is not to defend the over-committing label, but to reopen and publish the earlier route-bearing form.

#### A.16:19.2 - Silent route drift
A note begins as evaluative pressure but later starts driving work planning. If this shift is not published, the route drift remains invisible. `A.16` requires either a new route-bearing publication, an explicit operationalization note, or an explicit handoff to a receiving governing pattern.

#### A.16:19.3 - admissible retreat after over-formalization
A note is formalized too early into a relation-like shape, but later review shows the anchors are still unstable. The correct continuation is not to leave the relation form in place and quietly reinterpret it. The correct continuation is `reopen -> sketchBackoff`, preserving what still holds and lowering the authority of what no longer does.

#### A.16:19.4 - Silent branch disappearance
A route-bearing publication originally kept two candidate routes live. Later text talks only as if one route ever existed. Reviewers should treat that as silent branch laundering unless the abandoned route was explicitly retired, merged, or shown never to have become a distinct branch.

#### A.16:19.5 - Form-governing pattern-face collapse
A note says only `the move publishes a Tech face` or `the move enters A.6.P` and never names the actual publication form. That wording is non-conforming because it collapses three different layers into one phrase. The repair is to name the publication form first, then the governing pattern, then the MVPK face if the face matters for rendering or review.

### A.16:20 - Multi-Move Composition and Path Publication

#### A.16:20.1 - Compound move rule
Many published histories are short move chains such as `notice -> stabilize -> route -> projection` into `U.AbductivePrompt`, or `endpoint-pattern-publication-issued -> reopen -> sketchBackoff -> route`. A conforming publication may summarize such a chain only if the intermediate governing pattern transitions remain reconstructible.

#### A.16:20.2 - Move-by-move authority reading
Read authority move by move. A later move to higher closure state, route authority state, or endpoint authority claim does not retroactively authorize earlier lower-articulation forms, and later retreat or retirement does not erase the fact that the later route or endpoint authority state once existed.

#### A.16:20.3 - `A.16.0` threshold
When a move history acquires lineage governance value, publish it through `A.16.0` rather than overloading one local move note with hidden lineage structure.

#### A.16:20.4 - `E.18` threshold
When the history must be published as a path publication in a graph sense, reuse `E.18`. `A.16` still governs move semantics.

### A.16:21 - Comparative Move Rules and Boundary Tests

#### A.16:21.1 - Comparing move histories
Move histories may be compared across contexts only if the compared moves are typed by publication form, governing pattern, and authority effect. Comparing one context's `route -> projection` chain to another context's `cue -> requirement` leap as though they were the same "formalization speed" is a category mistake.

#### A.16:21.2 - No maturity-climb compression
A multi-move path shall not be redescribed as one generic climb in maturity, rigor, or readiness. The admissible comparison is over move kinds, facet shifts, route states, governing pattern crossings, and authority effects.

#### A.16:21.3 - Boundary test for silent path laundering
If a endpoint claim depends on prior move publications that are not visible anywhere in the publication chain, reviewers should assume silent path laundering until the missing move records are supplied. `A.16` exists precisely to prevent such invisible transitions.

### A.16:22 - Review Matrix for Integration Integrity

A reviewer can test an `A.16` move or move chain with six questions:

1. **Are the source publication form and target publication form typed?** If not, the move is too vague.
2. **Are governing pattern and face kept distinct from the form?** If not, the move collapses layers.
3. **Is the authority effect explicit?** If not, receiving governing pattern boundaries will drift.
4. **Is route plurality being confused with lineage fork?** If yes, the history is being misread.
5. **Are intermediate move publications suppressed in a way that changes the reading?** If yes, the chain is over-compressed.
6. **Has `A.16` started to impersonate a receiving governing pattern or a trajectory wrapper?** If yes, the relevant receiving governing pattern or `A.16.0` threshold needs to be named explicitly.

This matrix keeps the integration layer narrow while still making its move semantics inspectable.
### A.16:End

## A.16.0 - `U.LanguageStateTransductionTrajectory` - Optional trajectory-account normal form over the language-state `U.CharacteristicSpace`

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state transduction trajectory.

**Builds on.**
`C.2.2a`, `A.16`, `A.19`, `E.17`, `E.18`, `E.10`, `F.18`.

**Used by.**
`A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `A.6.P`, `A.6.Q`, `A.6.A`, `F.9.1`, `E.17.1`.

### A.16.0:1 - Problem frame
In engineering, inquiry, operator, and management practice, teams sometimes need more than a local move note. When branch structure, supersession, retirement, handoff, bridge-sensitive loss, or multi-step governing pattern change matters, readers need one place where the history of successive governed `U.Episteme` publications is made explicit.

Cue packs, routed cue sets, abductive prompts, typed route-bounded projection publications, partial normal forms, and endpoint-bound records are publication forms that may appear in that history. They are not the raw disturbances, telemetry traces, model outputs, bodily tensions, or carrier documents that ground it.

What must remain intelligible is therefore not a myth that one unchanged `U.Episteme` publication literally `moves`. What must remain intelligible is a lineage of successive governed `U.Episteme` publications, together with the load-bearing links among them, when that history itself has governance value.

### A.16.0:2 - Problem
Without an explicit trajectory-account pattern for those heavier cases:

1. history is mistaken for generic one-pass process story rather than for governed transduction over a declared language-state `U.CharacteristicSpace`;
2. early seam publications are confused with `U.EpistemePublication` forms governed by endpoint patterns;
3. forks, merges, route retirement, supersession, and route-sensitive loss become implicit and unverifiable;
4. every local move is either over-wrapped in ad hoc history prose or under-wrapped in a way that hides handoff and authority change;
5. bridge and viewpoint docking inherit under-described upstream history.

### A.16.0:3 - Forces
| Force | Tension |
| --- | --- |
| **History value vs wrapper inflation** | Publish lineage only when it matters, without making trajectory accounts mandatory around every admissible move. |
| **Lineage fidelity vs readable publication** | Trajectory history must stay branch-aware without becoming unreadable bookkeeping. |
| **Seam usefulness vs endpoint discipline** | Upstream publications must be useful while remaining visibly upstream of endpoint governance. |
| **Account clarity vs governing pattern boundaries** | The trajectory pattern must explain heavy-history cases without taking over `A.19`, `A.16`, `E.17`, `E.18`, or endpoint semantics. |
| **Local transduction vs bridge entry** | The same trajectory may later cross viewpoint or context boundaries, but that crossing does not redefine the local trajectory governing pattern. |

### A.16.0:4 - Solution
`U.LanguageStateTransductionTrajectory` is the **optional** trajectory-account normal form that records how successive governed `U.Episteme` publications are linked across position claims in the declared language-state `U.CharacteristicSpace` chart named in `C.2.2a`.

It does **not** define position semantics, move admissibility, or publication-face ontology by itself. Those remain with `C.2.2a` / `A.19`, `A.16`, and `E.17` / `E.18` respectively.

It answers the question: `when history itself matters, which governed publication is current, which members precede or branch from it, which admissible moves relate them, which publication forms carry them, what was lost, and who now governs the next responsibility?`

#### A.16.0:4.1 - Ontological subject and role lanes
In this cluster, keep six roles distinct:

- **current governed member** - the current `U.Episteme` publication under language-state governance;
- **lineage links** - explicit `derivedFrom`, `supersedes`, `forkedFrom`, `mergedFrom`, and retirement / no-successor links among governed members;
- **grounds / witnesses** - service disturbances, model-vs-observation discrepancies, traces, model outputs, bodily tensions, contrasts, or exemplars that justify the history;
- **publication forms** - cue packs, routed cue sets, prompt forms, typed route-bounded projection publications, partial normal forms, and records governed by endpoint patterns through which lineage members are published;
- **publication faces** - the existing MVPK faces on which those publication forms are rendered when face typing matters;
- **carriers** - documents, console notes, cards, trace files, or model outputs or carriers that hold or render those publications.

A multi-route state inside one current governed member is **not** yet a lineage fork. It becomes a fork only when distinct successor members are published and given distinct authority, losses, or handoff semantics.

A trajectory step may add a new lineage member, revise the current member, or relate several members through fork, merge, supersession, or retirement. It does **not** mean that the source phenomenon itself has moved through the language-state chart.

#### A.16.0:4.2 - Position-account discipline
The position read by this pattern is the slot-explicit claim defined in `C.2.2a`: a partial coordinate publication in the declared language-state `U.CharacteristicSpace`, where each basis slot publishes a `ValueSet(slot)`, interval, or other admissible set-valued claim.

Early seam publications may leave some slots unknown or wide. That uncertainty is admissible only if it is explicit. A trajectory account therefore records the position claims of the current lineage member and, when needed, of the predecessor or sibling members that justify the move reading.

#### A.16.0:4.3 - Use threshold and core trajectory record
A single local `A.16` move note is sufficient when no load-bearing branch, loss, handoff, or supersession structure needs publication.

Use `U.LanguageStateTransductionTrajectory` when at least one of the following is load-bearing:

- derivation, supersession, fork, merge, or retirement structure;
- multi-step loss notes or reopen conditions that would be hidden by a compressed move note;
- responsibility handoff whose legitimacy depends on upstream history;
- bridge or viewpoint entry that depends on upstream route, loss, or lineage structure.

A conforming trajectory account then keeps at least the following explicit:

- the current governed member;
- predecessor, sibling, or ancestor references when the current reading depends on lineage structure;
- the lineage link kind (`derivedFrom`, `supersedes`, `forkedFrom`, `mergedFrom`, `retiredWithSuccessor`, `retiredWithoutSuccessor`, or another explicitly typed link);
- the current position claim and any load-bearing predecessor position claims;
- the typed move or move sequence that relates them;
- the publication form currently carrying the governed member and, if it matters, the MVPK face carrying that form;
- the next intended governing pattern or handoff state;
- any loss note, reopen condition, branch-specific authority note, or bridge-sensitive note that matters.

#### A.16.0:4.4 - Recorded move-family discipline
`U.LanguageStateTransductionTrajectory` records the governed `A.16` move family: `notice`, `stabilize`, `route`, `projection`, `formalize`, `operationalize`, `reopen`, `sketchBackoff`, `respecify`, and `retire`.

The point is not that every account uses every move. The point is that forward movement, retreat, reframing, and explicit retirement belong to one governed family when that history is worth publishing.

Detailed move guards remain with `A.16`. `A.16.0` records their use; it does not govern them.

#### A.16.0:4.5 - Seam publication and face discipline
A trajectory account may refer to seam publications that remain upstream of endpoint governance. In the current cluster these include:

- `U.PreArticulationCuePack`;
- `RoutedCueSet`;
- `U.AbductivePrompt`;
- partial normal forms already typed elsewhere;
- other explicitly typed upstream publications that preserve non-endpoint status.

These are not a rival publication-face sequence. They are typed publication forms rendered, when necessary, on existing MVPK faces under `E.17`.

Untyped placeholders such as "route-bounded publication face" are non-conformant in a trajectory account unless the text also names the actual publication form and, separately, the MVPK face if face typing matters.

#### A.16.0:4.6 - Endpoint docking and responsibility handoff
A trajectory does not need to terminate in order to be useful. What matters is a visible docking milestone or responsibility handoff into a governing pattern that is allowed to take the next pattern-governed declaration.

Typical docking governing patterns include:

- `A.6.P` for relation repair forms;
- `A.6.A` for invitation forms;
- `A.6.Q` for evaluative repair forms;
- `B.5.2` for later abductive work;
- `A.15` for method-facing or work-facing forms;
- `C.25` for endpoint bundle structures.

A trajectory account should therefore name not only the docking governing pattern but also the pattern-governed publication or record that now carries the next pattern-governed declaration. Naming only the governing pattern under-publishes the handoff.

After such a handoff, monitoring, maintenance, revisit, or later re-entry may continue through new lineage members or later trajectories. The pattern therefore distinguishes `lineage continuity` from `current governing pattern responsibility`.

#### A.16.0:4.7 - Effect-free moves versus work-requiring crossings
Some `formalize` and `operationalize` steps are effect-free epistemic transformations: rewriting, slot-explicit articulation, route-bounded partialization, view retargeting, or normal-form repair over already available grounds.

Other steps require new measurements, experiments, instrumentation, execution, or other `U.Work`. When that happens, the trajectory account shall publish the crossing or handoff explicitly rather than pretending that world-facing work occurred inside the language layer. `A.16.0` records that the crossing was required; the relevant work, gate, or endpoint governing pattern records the world step itself.

#### A.16.0:4.8 - Relation to `A.16` and `E.18`
`U.LanguageStateTransductionTrajectory` is not an `E.18` path publication, and `A.16.0` does **not** govern the semantics of language-state movement.

- `A.19` plus `C.2.2a` govern the declared characteristic-space reading of positions;
- `A.16` governs move kinds and move guards;
- `E.17` / `E.18` govern publication-face discipline and graph publication of paths;
- endpoint patterns govern endpoint-local `U.EpistemePublication` forms and declarations.

`A.16.0` standardizes only the heavier history package for cases where that package is itself worth publication.

#### A.16.0:4.9 - Bridge and viewpoint entry
A trajectory may later cross a viewpoint or context boundary. When that happens:

- bridge substitution licence remains with `F.9`;
- stance overlays remain with `F.9.1`;
- viewpoint reuse remains with `E.17.1`;
- endpoint-local semantics remain with their named endpoint patterns and governed publication forms.

`A.16.0` only makes those entry points explicit so that later attachments do not float without an upstream history account.

### A.16.0:5 - Archetypal Grounding
**Tell.** A language-state trajectory account is not `we kept refining the note`. It is an optional, lineage-aware account of successive `U.Episteme` publications, with declared position claims, move kinds, publication forms, losses, and next governing patterns.

**Show (System).** A service disturbance is a system-side phenomenon, not the trajectory subject. It grounds an alerting episteme lineage. One stabilized cue pack may first keep two routes live in one `RoutedCueSet`; only later, if two distinct successor publications are actually issued, does the lineage fork.

**Show (Episteme).** A model-vs-observation discrepancy is a witness-lane tension, not the occupant itself. Once preserved as a cue pack, the governed lineage may project into a typed prompt publication on one branch and later formalize on another, or it may reopen and retire one branch if the provisional route proves unsupported.

### A.16.0:6 - Bias-Annotation
The pattern biases authors toward lineage-aware history accounts rather than stage stories about one magically maturing `U.Episteme` publication. That bias is intentional when branch, loss, or handoff semantics matter. The counter-bias is equally intentional: do **not** publish a trajectory account when a local move note already suffices.

### A.16.0:7 - Conformance Checklist
- `CC-A.16.0-1` `U.LanguageStateTransductionTrajectory` **SHALL NOT** be treated as mandatory wrapper syntax around every `A.16` move.
- `CC-A.16.0-2` A language-state trajectory account **SHALL** identify the current governed `U.Episteme` publication and **SHALL NOT** collapse grounds, publication forms, publication faces, carriers, and governed members into one unnamed moving thing.
- `CC-A.16.0-3` Position claims used in the trajectory **SHALL** be published as slot-explicit claims in the declared language-state `U.CharacteristicSpace`, not as folk stage labels.
- `CC-A.16.0-4` Fork, merge, supersession, derivation, and retirement **SHALL** be made explicit whenever the account depends on them.
- `CC-A.16.0-5` Publication form and MVPK face **SHALL NOT** be collapsed, and untyped seam placeholders **SHALL NOT** substitute for typed publication forms.
- `CC-A.16.0-6` `projection` **SHALL** be read as route-bounded partialization with visible loss notes and an admissible reopen path.
- `CC-A.16.0-7` Work-requiring `formalize` or `operationalize` steps **SHALL** expose the relevant crossing or handoff rather than pretending that `U.Work` occurred inside the language layer.
- `CC-A.16.0-8` When graph publication of paths is needed, authors **SHOULD** reuse `E.18` rather than inventing a rival path calculus here.

### A.16.0:8 - Common Anti-Patterns and How to Avoid Them
- **Meta-wrapper inflation.** Treat `A.16.0` as obligatory around every move. Repair by publishing a local `A.16` move note unless history itself has governance value.
- **One-publication myth.** Treat one frozen episteme as literally moving unchanged. Repair by publishing lineage members and their links.
- **Governing-pattern/form collapse.** Treat receiving governing patterns as if they were publication forms. Repair by naming the pattern-governed form and the governing pattern separately.
- **Form/face collapse.** Treat seam publications as if they minted a second MVPK face family. Repair by naming form and face separately.
- **Multi-route/fork collapse.** Treat several live routes in one governed member as if they were already several successor members.
- **Hidden work crossing.** Describe operationalization as purely linguistic when it actually required new world-facing work. Repair by publishing the crossing explicitly.

### A.16.0:9 - Consequences
The benefit is that heavy-history language-state movement becomes lineage-aware, reviewable, and dockable without premature endpoint capture or metonymic collapse. The trade-off is more explicit publication of position claims, lineage links, move kinds, loss notes, and handoffs when history is worth publishing.

### A.16.0:10 - Rationale
Language-state work needs one explicit trajectory-account normal form for the subset of cases where history itself matters. Without that account, readers have to reconstruct lineage, branch structure, retirement, and handoff semantics from fragments. With it overused, every local move becomes over-wrapped. The pattern exists to hold the middle line.

### A.16.0:11 - SoTA-Echoing
The pattern matches contemporary practice in exploratory inquiry, operator-centered incident work, model probing, and structured design iteration: admissible progress sometimes requires visible intermediate publications, branch-aware history, disciplined retreat, and explicit handoffs rather than hidden jumps from cue to endpoint.

### A.16.0:12 - Relations
- Builds on: `C.2.2a`, `A.16`, `A.19`, `E.17`, `E.18`.
- Coordinates with: `C.2.LS`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `B.5.2`, `A.6.P`, `A.6.Q`, `A.6.A`, `F.9`, `F.9.1`, `E.17.1`.
- Constrains: trajectory-account publication, branch visibility, seam publication reading, docking visibility, and anti-pipeline language across the cluster.

### A.16.0:13 - Worked trajectories

#### A.16.0:13.1 - Multi-route state before fork
A routed operator cue may first publish one governed member with both intervention and inquiry routes live inside one `RoutedCueSet`. That is still one member in a multi-route state. Only if separate successor publications are later issued for those two continuations does the lineage fork.

#### A.16.0:13.2 - Inquiry trajectory with fork
An inquiry cue pack centered on a felt or trace-anchored discrepancy cue may first publish one governed member, then fork into:

- `notice -> stabilize -> route -> projection -> formalize`, with a cue-derived prompt publication carrying the explanatory branch, and
- `notice -> stabilize -> route -> projection -> operationalize`

if one branch supports explanatory work while another supports immediate probe or control work. The branches remain admissible only if the fork is visible and each branch keeps distinct loss notes and handoff conditions.

#### A.16.0:13.3 - Operator trajectory with retirement
An operator alert note about a service disturbance may move:

`notice -> stabilize -> route -> projection -> operationalize`

If one route later proves unsupported, the admissible continuation may include explicit retirement of that branch rather than silent disappearance. The retirement does not erase the prior branch; it withdraws authority and preserves continuity explicitly.

#### A.16.0:13.4 - Bridge-sensitive trajectory
A route-bearing comparative note may move through a seam publication and only later dock to a bridge overlay or viewpoint bundle. The bridge or viewpoint attachment does not replace the trajectory account; it annotates or re-expresses a lineage that already exists.

### A.16.0:14 - Trajectory publication package discipline
A publishable trajectory account should normally identify:

- the current governed `U.Episteme` publication;
- predecessor, sibling, or ancestor references when they are load-bearing;
- the lineage link kind;
- the current position claim and any load-bearing predecessor position claims;
- the move or move sequence being asserted;
- the current publication form and, if relevant, the MVPK face carrying it;
- the grounds or witnesses that make the history necessary;
- the next route, docking governing pattern, or retirement state;
- the losses, open rivals, or reopen conditions that matter for continuation.

If these are missing, the publication is usually only plain sequence prose, not a conforming trajectory account.

### A.16.0:15 - Review guidance
A reviewer should ask:

1. Is the author really describing history over the declared language-state `U.CharacteristicSpace`, or only narrating progress informally?
2. Is the current governed member distinct from the grounds, publication form, publication face, and carrier?
3. Is this history heavy enough to justify `A.16.0`, or would a local `A.16` move note have sufficed?
4. Are multi-route state and lineage fork being kept distinct?
5. Are derivation, supersession, fork, merge, or retirement links visible where the reading depends on them?
6. Is the current publication a seam publication or already a `U.EpistemePublication` form governed by a named endpoint pattern?
7. If `formalize` or `operationalize` required world-facing work, is the crossing or handoff explicit?

### A.16.0:16 - Boundary notes
`A.16.0` does not replace `C.2.2a` / `A.19` position semantics, `A.16` move guards, `A.16.1` cue-pack semantics, `A.16.2` retreat / retirement semantics, `B.4.1` seam entry routing, `B.5.2.0` abductive prompt species, `E.17` face typing, `E.18` path publication, or any endpoint-local repair logic.

Its job is narrower and architectural: to make the heavier trajectory account visible only where lineage, branch, loss, retreat, retirement, and handoff need to be published as one intelligible package.
### A.16.0:End

## A.16.1 - `U.PreArticulationCuePack`

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Pre-articulation cue pack.

**Start here when.** Your first honest content is a preserve-worthy cue nucleus that should not yet be forced into a claim, route decision, method, or work record.

**First output.** One `U.PreArticulationCuePack` with an explicit cue nucleus, preservation rationale, primary witness or anchor when one is load-bearing, and any early lane candidates or route-candidate hints that are already visible.

**Typical next governing patterns.** `B.4.1` when route plurality or route authority becomes publishable, `B.5.2.0` for cue-derived abductive prompting, `A.6.P`, `A.6.A`, or `A.6.Q` once endpoint articulation threshold is actually met, and `A.16.2` when reopening or retirement becomes the truthful move.

**Common neighboring-pattern mistakes.** Do not publish a cue pack as a selected-route decision, anomaly statement, evaluative ascription, `A.6.A`-governed invitation, or work record; if route authority is already explicit, use `B.4.1`; if endpoint semantics are already stable, apply the receiving governing pattern and its named publication form; if backoff or retirement is the active problem pressure, use `A.16.2`.

### A.16.1:1 - Problem frame
Early governed `U.Episteme` publications can be worth preserving before route publication, prompt publication, relation repair, evaluative repair, `A.6.A`-governed invitation repair, method work, or endpoint governance through receiving governing patterns. `U.PreArticulationCuePack` therefore exists as the earliest durable seam publication form for such pre-threshold cue content.

The cue pack is deliberately earlier than `RoutedCueSet`. It may carry early directional hints, but it is not yet the governing form for route selection, route authority, or route rationale.

### A.16.1:2 - Problem
Without an explicit cue-pack publication form, such epistemes either disappear, are prematurely forced into `AnomalyStatement` or `Characteristic`, or leak into prose as vague cue or signal language, loose evaluative talk, fit-talk, premature work-possibility pressure, or premature reliance-possibility pressure.

### A.16.1:3 - Forces
| Force | Tension |
|---|---|
| **Low-articulation shape vs publishability** | Preserve early cues without pretending they are already late `U.EpistemePublication` forms governed by endpoint patterns. |
| **Pre-route preservation vs later routing** | Let cue preservation stand independently before route publication is justified. |
| **Carrier awareness vs stack duplication** | Respect traces, bodies, and model states without creating a second carrier stack beside `A.7`. |
| **Plurality vs auditability** | Allow several plausible continuations without collapsing the cue pack into a route record. |

### A.16.1:4 - Solution
`U.PreArticulationCuePack` is a typed publishable episteme form that serves as the earliest durable seam publication form inside the language-state cluster. It is not a claim, not a characteristic, not a method, not work, and not a route record. When rendered, it appears on an ordinary MVPK face; cue-pack status is a property of the publication form, not a rival face kind.

A cue pack may exist before any route is selected and even before route-candidate hints can yet be named clearly. When route plurality or route authority becomes explicit enough to publish, the successor publication is governed by `B.4.1` and `RoutedCueSet`.

#### A.16.1:4.1 - Core shape
A conforming cue pack may publish:

- `cueNucleus`
- `preservationRationale?`
- `laneCandidates?`
- `routeCandidateHints?`
- `valenceProfile?`
- `languageStateClosureDegreeRef?`
- `languageStateFacetProfileRef?`
- `detector?`
- `primaryAnchor?`
- `candidateAnchors?`
- `primaryWitnessRef?`
- `witnessRefs?`
- `exemplars?`
- `contrasts?`
- `traceRefs?`
- `embodimentRefs?`
- `modelStateRefs?`
- `scope?`
- `GammaTime?`

`cueNucleus` names the minimal preserved core: what exactly is being kept visible rather than lost in carrier noise or premature endpoint wording.

`primaryWitnessRef` and `primaryAnchor` provide explicit triage when one witness or anchor is load-bearing for preservation. Secondary witnesses, anchors, traces, embodiment refs, and model-state refs may enrich the pack without displacing that primary nucleus.

`laneCandidates` and `routeCandidateHints` are early directional hints only. They are **not** selected route, route rationale, or route authority state. Those belong to `RoutedCueSet` under `B.4.1`.

The cue pack governs none of the facets it references. `primaryAnchor`, `candidateAnchors`, contrasts, and exemplars commonly support `AE` under `C.2.4`; `languageStateClosureDegreeRef` docks to `C.2.5`; anchoring and representation-factor refs dock to `C.2.6` and `C.2.7`; `languageStateFacetProfileRef` may bundle them through `C.2.LS`.

In this cluster, a cue is a salient epistemic nucleus extracted from witnesses, traces, felt tensions, model outputs, work-possibility hints, reliance-possibility hints, contrasts, or other grounds and made preservable as a pack. A raw signal-like trace counts as a cue only when that salience and preservability have been made explicit; otherwise it remains evidence, not yet a cue.

#### A.16.1:4.2 - Governance boundary
A cue pack may preserve:

- a cue nucleus,
- preservation rationale,
- primary and candidate anchors,
- primary and secondary witnesses,
- contrasts and exemplars,
- early directional plurality or route-candidate hints.

A cue pack shall not silently serve as:

- a route decision record,
- a selected-route publication,
- a finished anomaly statement,
- a finished evaluative ascription,
- a finished `A.6.A`-governed invitation,
- a method step,
- a work occurrence.

#### A.16.1:4.3 - Transition discipline
A cue pack may admissibly feed:

- `B.4.1` once route plurality or route selection deserves explicit publication;
- `B.5.2.0` after a cue-derived abductive prompt is formed;
- `A.6.P` only once articulation threshold and relation-like shape are met;
- `A.16.2` when prior stabilization must be reopened, backed off, respecified, or retired.

### A.16.1:5 - Archetypal Grounding
**Tell.** A cue pack says "there is a preserve-worthy cue nucleus here" without falsely claiming that a later route or endpoint form already exists.

**Show (System).** A console alert with traces and tension indicators may be worth preserving as a cue pack before anyone can honestly publish route selection, gate logic, or work execution.

**Show (Episteme).** A researcher's stabilized felt or trace-anchored discrepancy cue with exemplars and contrasts can be published as a cue pack before it becomes a routed cue set, an abductive prompt, or an anomaly statement.

### A.16.1:6 - Bias-Annotation
This pattern biases authors toward preserving low-articulation meaningful cues instead of discarding them or disguising them as later publication forms with higher closure state, route authority state, or endpoint authority claim. The counter-bias is deliberate as well: a cue pack must still name what is being preserved and why.

### A.16.1:7 - Conformance Checklist
- `CC-A.16.1-1` A cue pack **SHALL NOT** be presented as a claim, characteristic, method, work occurrence, or route-decision record.
- `CC-A.16.1-2` A cue pack **SHALL** make `cueNucleus` explicit.
- `CC-A.16.1-3` When preservation depends on privileged grounding, `primaryWitnessRef` or `primaryAnchor` **SHALL** be explicit.
- `CC-A.16.1-4` `laneCandidates` and `routeCandidateHints` **MAY** be published early, but `selectedRoute`, `routeRationale`, and route authority state **SHALL NOT** be smuggled into the cue pack.
- `CC-A.16.1-5` If route-candidate hints are not yet nameable, publication is still admissible only when `preservationRationale` and grounding make the preservation need explicit.
- `CC-A.16.1-6` Language-state, anchoring, and representation-factor details **MAY** be referenced, but their governing patterns remain `C.2.LS`, `C.2.4`, `C.2.5`, `C.2.6`, and `C.2.7`.
- `CC-A.16.1-7` A cue pack **SHALL NOT** silently inherit endpoint authority that belongs to receiving governing patterns.

### A.16.1:8 - Common Anti-Patterns and How to Avoid Them
- **Cue as claim.** Do not promote the pack into a proposition without a later admissible move.
- **Cue as route record.** Do not let `selectedRoute`, route rationale, or route authority hide inside cue-pack prose.
- **Cue without nucleus.** Do not publish only refs and carriers while leaving the preserved core unnamed.
- **Cue without triage.** Do not pretend all witnesses or anchors are equally load-bearing when one clearly carries the preservation need.
- **Cue as carrier zoo.** Do not make `U.PreArticulationCuePack` a replacement for `A.7` carrier discipline.

### A.16.1:9 - Consequences
The benefit is an admissible preservation form for early cues and a cleaner seam into routing and receiving endpoint patterns. The trade-off is one more explicit publication form that must be named and maintained.

### A.16.1:10 - Rationale
`U.PreArticulationCuePack` is the earliest durable seam publication in the cluster. It keeps pre-threshold cues visible before route selection and without overloading `A.6.P`, `B.4.1`, or `B.5.2`.

### A.16.1:11 - SoTA-Echoing
The pattern fits early cue capture in design, embodied cognition, incident triage, model interpretation, and focusing-like practice, where low-articulation but real cues need preservation before route or endpoint choice.

### A.16.1:12 - Relations
- Builds on: `C.2.2a`, `A.16`, `C.2.LS`, `A.7`.
- Coordinates with: `A.16.0`, `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `B.4.1`, `B.5.2.0`, `A.6.A`, `A.6.Q`, `A.16.2`.
- Constrains: publication of pre-threshold cues.

### A.16.1:13 - Worked Examples and Invalid Publications

#### A.16.1:13.1 - Operator cue pack
A valid operator-facing cue pack might preserve:

- one cue nucleus around a disturbance/work-or-intervention possibility tension,
- a primary witness trace,
- candidate anchors from recent operator work step and system response,
- lane candidates toward intervention, inquiry, and rollback,
- but no selected route and no final gate decision.

This is admissible because it preserves early significance without pretending the cue is already a route record, a gate, method, or work record.

#### A.16.1:13.2 - Inquiry cue pack
An inquiry cue pack may preserve exemplars, contrasts, a felt or trace-anchored discrepancy cue nucleus, and candidate anchor fragments. This is admissible even when the publication is still below both route publication and `A.6.P` threshold.

#### A.16.1:13.3 - Invalid publication to reject
It is invalid to publish a cue pack and then cite it as if it were already an anomaly statement, a routed cue set, an explanatory bundle, or a control obligation. The cue pack is only the preservation form.

### A.16.1:14 - Authoring and Review Guidance

#### A.16.1:14.1 - Author prompt
A cue pack should answer four questions:

- what exactly is being preserved?
- why is it worth preserving now rather than losing it?
- which witness or anchor currently carries the primary load?
- which downstream directions, if any, are already visible without pretending that a route has been selected?

#### A.16.1:14.2 - Review prompt
A reviewer should check:

- whether the pack has a clear cue nucleus;
- whether primary witness or primary anchor triage is explicit when needed;
- whether it is being abused as a shadow claim or shadow route record;
- whether route language is still an early directional hint rather than route selection.

#### A.16.1:14.3 - Carrier reminder
The cue pack may cite traces, embodiment, and model-state refs, but it should not try to replace `A.7` carrier discipline.

### A.16.1:15 - Migration and Extension Notes

#### A.16.1:15.1 - Migration from vague cue / signal language
Older prose often says merely "there is a signal" or "something suggests a work move". A conforming migration first asks whether the source is truly signal-like in the narrow telemetry or trace sense, or whether the load-bearing phenomenon is a broader cue nucleus, work-possibility hint, reliance-possibility hint, contrast, or figure-against-background shift. It then turns the passage into a cue pack with explicit cue nucleus, primary witness or anchor, and route-candidate hints only if those hints are already visible.

#### A.16.1:15.2 - Local extension rule
Contexts may add local cue-pack fields only if they remain preservation aids rather than covert route-decision or endpoint semantics.

#### A.16.1:15.3 - Boundary reminder
If a cue pack begins to carry route decision, stable endpoint authority, relation slots, method semantics, work semantics, or other later-pattern authority or signature conditions, the publication is ready to exit this governing pattern.

### A.16.1:16 - Cue-Pack Package Discipline

A cue pack is useful only if it preserves enough structure to justify route publication or prompt formation without pretending that a receiving endpoint pattern already governs the publication.

#### A.16.1:16.1 - Minimal preservation package
A robust cue pack should make visible:

- the **cue nucleus** being preserved,
- the **preservation rationale**,
- the **primary witness or primary anchor** when one is load-bearing,
- the **candidate anchors / contrasts / exemplars** that keep the nucleus non-arbitrary,
- the **secondary witnesses or carriers** that support it,
- and the **lane candidates or route-candidate hints**, if such directional hints are already visible.

This is what turns early cues into an admissible preservation form.

#### A.16.1:16.2 - Route-candidate hints are optional, not forbidden
A cue pack is not an archive of low-articulation cues, but it also need not wait until route-candidate hints are fully articulate. If route-candidate hints are already visible, publish them. If they are not yet visible, publication may still be admissible when the cue nucleus, grounding, and preservation rationale make clear why the cue should not be lost.

#### A.16.1:16.3 - Valence is not endpoint semantics
Valence, urgency, discomfort, promise, or attraction may explain why a cue is preserved. They do not by themselves establish `A.6.A`-governed invitation, evaluative, abductive, or route authority.

### A.16.1:17 - Cue-Pack Continuations and Non-Continuations

#### A.16.1:17.1 - Admissible continuations
A cue pack may continue admissibly into:

- a routed cue set,
- a cue-derived abductive prompt,
- a later lexical-repair family once articulation threshold is met,
- or a retreat / retirement move when prior stabilization over-committed or no longer deserves current publication.

#### A.16.1:17.2 - Non-continuations
A cue pack should not be used directly as:

- a stable proposition,
- a route decision,
- a deontic commitment,
- a work occurrence,
- or a measurement-bearing quality endpoint.

Those are not just later stages of the same text. They are different governing forms with different authority/signature conditions.

#### A.16.1:17.3 - Multi-direction state versus lineage fork
Several lane candidates or several low-articulation route-candidate hints may live inside one cue pack. That is still one governed publication.

A fork happens only after distinct successor publications are actually issued, each with distinct authority or handoff consequences. Reviewers should not treat pre-route plurality inside one cue pack as if it were already a forked lineage.

#### A.16.1:17.4 - Split and merge cases
One cue pack may later split into several route-bearing continuations if its preserved cue nucleus actually contains several tensions. Several cue packs may also merge if later stabilization reveals that they were fragments of one more coherent cue complex. Both cases are admissible if the continuity and later route consequences are published explicitly.

### A.16.1:18 - Worked Cue Complexes and Review Tests

#### A.16.1:18.1 - Mixed-source cue complex
A cue pack may combine trace refs, embodiment refs, model-state refs, and exemplar fragments. This is admissible provided the pack still identifies what unifies those grounds into one cue nucleus rather than using the pack as an unstructured container for unrelated fragments.

#### A.16.1:18.2 - Review test for under-specified packs
A reviewer may ask: if all candidate anchors and witnesses were removed, would anything remain that justifies preserving this pack at all? If the answer is still unclear what is being preserved, the pack is under-specified and should be rewritten, retired, or not published yet.

#### A.16.1:18.3 - Review test for covert endpoint capture
A reviewer should also ask whether any sentence in the pack would become false if the receiving endpoint pattern and its governed publication form were denied. If yes, the cue pack is already carrying endpoint semantics and needs either an explicit move out of `A.16.1` or a rewrite back into preservation language.

### A.16.1:19 - Cue-Pack Continuation and Comparative Preservation Rule

#### A.16.1:19.1 - Continuation visibility
A cue pack should make it visible whether the preserved cue nucleus is being kept open, route-published later, split, merged, or retired.

#### A.16.1:19.2 - Preservation worthiness test
Keep a cue pack only when its nucleus would likely be lost or distorted without it. If the same cue already lives stably in a receiving governing form with a more closed state, route authority state, or endpoint authority claim, the cue pack has become redundant.

#### A.16.1:19.3 - Comparative preservation rule
Compare cue packs only when nuclei, primary witness choice, primary anchor choice, and any early directional hints are explicit. Emotional intensity, rhetorical urgency, or author confidence are not admissible comparison proxies.

### A.16.1:20 - Witness and Carrier Triage

#### A.16.1:20.1 - Witness priority rule
Not all witnesses play the same role. Authors should distinguish the witness that anchors the cue nucleus from secondary witnesses that only enrich or corroborate it. Without that distinction, cue packs become hard to route because everything in the pack starts looking equally load-bearing.

#### A.16.1:20.2 - Carrier overload boundary
A cue pack may cite traces, embodiment, model-state refs, or document fragments, but it should not absorb their full carrier semantics. When carrier analysis itself becomes central, `A.7` or another carrier governing pattern should be cited explicitly rather than silently embedded into the pack.

#### A.16.1:20.3 - Early directional plurality rule
Plural lane candidates or plural route-candidate hints are not a flaw. If the same cue nucleus pulls toward several receiving governing patterns, the pack should keep that plurality visible until `B.4.1` narrows it into explicit route publication. The error is not plurality; the error is hiding plurality under a single convenient gloss.

### A.16.1:21 - Review Matrix and Migration Tests

A reviewer can test a cue pack with four questions:

1. **What exactly is being preserved?** If the nucleus is unclear, the pack is under-specified.
2. **Why this pack rather than a receiving governing form with a more closed state, route authority state, or endpoint authority claim?** If the answer is only habit, the pack may be redundant.
3. **Which witness or anchor is primary?** If none can be named where triage matters, the pack may be storage rather than preservation.
4. **Which downstream directions remain live, if any?** If the publication hides them, later routing will be distorted.

Migration from legacy signal language should therefore reconstruct not just a vague "signal", but the preserved cue nucleus, its primary witness or anchor, and any directional hints that are already honestly visible.
### A.16.1:End

## A.16.2 - Reopen / SketchBackoff / Respecify

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Admissible reopen / backoff / respecification.

### A.16.2:1 - Problem frame
A governed history across the language-state chart must support admissible retreat as well as tightening. When a route, publication form, or framing scaffold over-commits, teams need a first-class way to reopen, back off, respecify, or retire a branch without pretending nothing changed.

### A.16.2:2 - Problem
Without an explicit retreat pattern, teams treat reopening as failure, hide regressions, silently mutate endpoint-bound or route-bearing forms back into exploratory cue-bearing publication forms with no audit trail, or let obsolete branches disappear without any visible withdrawal note.

### A.16.2:3 - Forces
| Force | Tension |
|---|---|
| **Reversibility vs trust** | Allow backoff without making the trajectory discipline look arbitrary. |
| **Explicit retreat vs clutter** | Name retreat and retirement without drowning the model in bookkeeping. |
| **Witness retention vs honest revision** | Keep what remains valid while explicitly discarding what no longer holds. |
| **Framing revision vs repair-pattern boundary** | Allow route-specification or framing-scaffold revision without letting `A.16.2` swallow slot-explicit semantic repair from receiving governing patterns. |

### A.16.2:4 - Solution
This pattern defines the retreat, reframing, and retirement side of the `A.16` move family.

#### A.16.2:4.1 - Move family
| Move | When to use it | What remains stable | What may change |
|---|---|---|---|
| `reopen` | the current family is still right, but closure was over-committed | family and major orientation | closure, rival set, guards |
| `sketchBackoff` | the current publication form overstates articulation or stability | witnesses, traces, some anchors | publication form, articulation-explicitness value, route certainty |
| `respecify` | the family remains plausible, but the framing scaffold, route specification, or facet-profile reading is wrong | broad domain, witness base, and major family commitments | framing scaffold, route specification, facet-profile reading |
| `retire` | a cue, route-bearing publication, or branch is no longer current or no longer worth preserving | historical continuity and any cited witnesses that still matter | currentness, authority, successor/no-successor status |

`respecify` is intentionally narrower than semantic repair. Slot-explicit semantic rewrite, bearer repair, or endpoint-local lexical precision remains with receiving governing patterns such as `A.6.P`, `A.6.Q`, and `A.6.A`.

#### A.16.2:4.2 - Required publication note
Every retreat or retirement move shall name:

- source publication form,
- source articulation / closure / route-authority state,
- trigger or counter-evidence,
- target family or target publication form,
- retained witnesses,
- withdrawn assumptions, route claims, or authority,
- and whether a successor now exists or the branch is retired without successor.

#### A.16.2:4.3 - Authority discipline
A retreat or retirement move shall not silently preserve operational, gate, commitment, or route authority if the retreat target form no longer supports that authority.

### A.16.2:5 - Archetypal Grounding
**Tell.** Backoff is not regression; it is an admissible transduction when the current publication form over-commits. Retirement is not erasure; it is admissible withdrawal when continuation no longer deserves current authority.

**Show (System).** A rollback cue may reopen a prior decision path instead of pretending the original operationalization still holds, or retire one branch once a better-supported successor line has taken over.

**Show (Episteme).** A formalized hypothesis may sketch-backoff to a cue pack when its framing collapses under new exemplars, or it may respecify its route specification while leaving slot-explicit semantic repair to receiving governing patterns.

### A.16.2:6 - Bias-Annotation
The pattern pushes against false linear progress narratives. The cost is that teams must expose when closure or route authority is being relaxed, reframed, or retired.

### A.16.2:7 - Conformance Checklist
- `CC-A.16.2-1` Retreat or retirement moves **SHALL** cite the trigger or counter-evidence that justifies them.
- `CC-A.16.2-2` A retreat or retirement move **SHALL NOT** silently preserve endpoint authority if the target form no longer supports it.
- `CC-A.16.2-3` Reopen / backoff / respecify / retire moves **SHOULD** preserve witnesses and trace links whenever still valid.
- `CC-A.16.2-4` The target articulation, closure, and route-authority state **SHALL** be explicit when the move substantively changes any of them.
- `CC-A.16.2-5` `respecify` **SHALL NOT** be used to smuggle slot-explicit semantic repair out of receiving governing patterns.

### A.16.2:8 - Common Anti-Patterns and How to Avoid Them
- **Shame-driven concealment.** Teams hide the retreat. Publish the move.
- **Silent downgrade.** The publication loses closure state, route authority state, or endpoint authority claim but no one updates the route or authority state.
- **Retreat as erasure.** Earlier witnesses disappear even though they remain valid.
- **Respecify as silent repair.** `respecify` is used to hide a real semantic rewrite that belongs to later repair governing patterns.
- **Silent branch disappearance.** A branch stops mattering, but no retirement or supersession note is published.

### A.16.2:9 - Consequences
The benefit is explicit reversibility, reframing, and retirement handling. The trade-off is more explicit transition records and more explicit governance notes.

### A.16.2:10 - Rationale
Language-state history is not one-way tightening. Without retreat and retirement discipline, `A.6.P` and endpoint forms would encode only one-way progress and would hide the real cost of over-commitment.

### A.16.2:11 - SoTA-Echoing
This fits iterative design, incident response, scientific reframing, embodied inquiry, and exploratory model work where recovery from over-commitment and honest branch retirement are part of competent practice.

### A.16.2:12 - Relations
- Builds on: `A.16`, `C.2.5`.
- Coordinates with: `C.2.2a`, `A.16.0`, `A.16.1`, `B.4.1`, `B.5.2`, `A.6.P`, `A.6.A`, `A.6.Q`.
- Constrains: admissible retreat, respecification, and retirement paths.

### A.16.2:13 - Worked Retreat Trajectories

#### A.16.2:13.1 - Reopen within the same family
A routed evaluative note may remain within the same family but move from high closure to lower closure when a rival frame reopens. This is `reopen`, not `sketchBackoff`.

#### A.16.2:13.2 - Sketch-backoff to cue pack
An over-specified `A.6.A`-governed invitation may later prove premature. The admissible retreat is:

`actionInvitation -> sketchBackoff -> U.PreArticulationCuePack`

with explicit withdrawal of route authority that no longer holds.

#### A.16.2:13.3 - Respecify without repair-pattern drift
A route-bearing publication may keep the same broad family but replace one framing scaffold or route specification with another. That is `respecify`, not silent editing, and not slot-explicit semantic repair.

#### A.16.2:13.4 - Retire an obsolete branch
A route-bearing branch may later become obsolete because another branch now carries the governing pattern and witness support for the current use. The admissible continuation is explicit `retire`, not silent disappearance.

### A.16.2:14 - Authoring and Review Guidance

#### A.16.2:14.1 - Author prompt
A retreat or retirement note should say:

- what proved over-committed or no longer current,
- what remains valid,
- what authority is withdrawn,
- what publication form now becomes appropriate,
- and whether any successor carries the continuity forward.

#### A.16.2:14.2 - Review prompt
A reviewer should ensure that retreat does not become silent erasure. Valid witnesses should survive unless explicitly discarded with reason, and retired branches should either name a successor or say clearly that none exists.

#### A.16.2:14.3 - Boundary reminder
Retreat is an admissible move, not a rhetorical excuse to avoid publishing mistakes. The value of the pattern depends on making the retreat or retirement visible.

### A.16.2:15 - Migration Notes

#### A.16.2:15.1 - Migration from regression language
Older language often talks about "going backwards" or "regressing". The preferred migration is to name whether the change is reopen, sketch-backoff, respecify, or retire, and what boundary or authority consequence follows.

#### A.16.2:15.2 - Integration reminder
When retreat affects receiving governing patterns such as `A.6.P`, `A.6.A`, `A.6.Q`, or `A.15`, those governing patterns should be updated explicitly rather than left to drift on stale authority.

### A.16.2:16 - Retreat Package Discipline

A retreat is trustworthy only when it makes visible what changed, what survived, and what authority no longer holds.

#### A.16.2:16.1 - Minimal retreat note
A retreat note should make explicit:

- the **source form and authority-reference relation state**,
- the **triggering mismatch or counter-evidence**,
- the **move kind**,
- the **target form or target family**,
- the **retained witnesses**,
- the **withdrawn assumptions or route claims**,
- the **required downstream updates** for any affected receiving governing pattern,
- and the **successor / no-successor status** if a branch is retired.

#### A.16.2:16.2 - Retreat is not erasure
Retreat preserves continuity: a high-closure formulation or formulation with endpoint authority claim was adopted, then shown to over-commit in stated respects, and therefore backed off or withdrawn admissibly.

#### A.16.2:16.3 - Partial retreat
Some retreats withdraw only one route claim, scope assumption, framing scaffold, or operational hook. In those cases name the surviving core rather than resetting everything.

### A.16.2:17 - Retained vs Withdrawn Authority

#### A.16.2:17.1 - Reopen
`reopen` usually preserves the family and much of the surrounding structure while withdrawing closure. It reintroduces rival possibilities without claiming that the entire earlier publication was inadmissible.

#### A.16.2:17.2 - Sketch-backoff
`sketchBackoff` withdraws closure state, route authority state, or endpoint authority claim more sharply. It typically preserves witnesses, exemplars, or cue anchors while withdrawing the over-committing publication form and any authority that depended on that form.

#### A.16.2:17.3 - Respecify
`respecify` keeps the broad family but changes framing scaffold, route specification, or facet-profile reading. It is neither pure retreat nor silent edit: it preserves enough of the prior publication to justify continuity, but it does not authorize semantic slot repair that belongs to receiving governing patterns.

#### A.16.2:17.4 - Retire
`retire` ends current authority for a cue, route-bearing publication, or branch while preserving historical continuity. It may point to a better-supported successor or explicitly state that no successor currently exists.

### A.16.2:18 - Worked Recovery Cases

#### A.16.2:18.1 - Reopening a routed evaluative note
An evaluative note may have reached a high closure state under one route, but new contrasts reopen a serious rival. `reopen` is admissible when the bearer, family, and witness base remain largely intact but the closure claim must be relaxed.

#### A.16.2:18.2 - Sketch-backoff from prompt to cue pack
An abductive prompt may later prove over-committed because its open question was formulated before the cue anchors had stabilized. The admissible recovery is to sketch-backoff to `U.PreArticulationCuePack`, preserving the cue carriers while withdrawing prompt authority.

#### A.16.2:18.3 - Respecifying a route specification
A route-bearing publication may keep the same general direction but replace one route specification with another when later review shows that the original framing selected the wrong governing pattern family. The point of `respecify` is to make that replacement visible without pretending the earlier route specification never existed.

#### A.16.2:18.4 - Retiring a route branch
A route-bearing branch may later be withdrawn because better-supported grounds, clearer closure, or a more adequate successor publication now carry the work. `retire` keeps that withdrawal visible instead of letting the branch vanish into later prose.

### A.16.2:19 - Review Matrix for Retreat Integrity

A reviewer can test retreat integrity with five questions:

1. **Was the trigger explicit?** If not, the retreat risks becoming retrospective narrative repair.
2. **Was authority updated?** If the earlier publication with named authority-reference relation, evidence-support class, or gate/admission basis no longer applies, any dependent route-bearing publication, gate decision, or endpoint authority claim must have been revised.
3. **Did valid witnesses survive?** If all earlier grounding disappeared without reason, the retreat probably became erasure.
4. **Was the move kind correctly named?** Reopen, sketch-backoff, respecify, and retire solve different problems; confusing them obscures what actually changed.
5. **If a branch was retired, was successor / no-successor status explicit?** If not, retirement may be hiding silent laundering.

The matrix is intentionally small: `A.16.2` should keep retreat legible, not surround it with decorative procedure.

### A.16.2:20 - Required Downstream Repairs

#### A.16.2:20.1 - Stale downstream publication/work-target rule
A retreat or retirement often leaves stale downstream publications or work targets behind: prompts, `A.6.A`-governed invitations, evaluative notes, requirement candidates, or work hooks that were admissible only under the prior state with higher closure state, route authority state, or endpoint authority claim. A conforming retreat should therefore name which downstream publications or work targets remain valid, which must be revised, and which must be withdrawn.

#### A.16.2:20.2 - Narrow retreat propagation
Retreat propagation should be as narrow as truth permits. If only one framing scaffold failed, then only the downstream publications or work targets that depend on that scaffold need revision. Over-broad rollback is wasteful; under-broad rollback leaves false authority in circulation.

#### A.16.2:20.3 - Retreat timestamping and witness continuity
Where several revisions exist, the retreat note should make clear which earlier publication it revises and which witness set still carries continuity across the revision. Without that linkage, readers may not know whether two nearby texts are alternative drafts or a genuine retreat sequence.

### A.16.2:21 - Comparative Retreat Rule

#### A.16.2:21.1 - Retreat kinds are not interchangeable
`reopen`, `sketchBackoff`, `respecify`, and `retire` solve different problems. Comparing them as if they all meant "we stepped back" erases the specific authority change each one makes.

#### A.16.2:21.2 - Honest recovery over softening prose
A context may prefer softening language such as "refined further" or "adjusted slightly" even when a real retreat or retirement occurred. `A.16.2` rejects that habit. If authority fell, closure dropped, framing was withdrawn, or a branch was retired, the move should be named directly.

#### A.16.2:21.3 - Boundary to silent editing
If a publication is simply rewritten and no continuity or authority story is preserved, that is editing, not `A.16.2`. Retreat is a reviewable move only when the earlier high-closure form or form with endpoint authority claim remains part of the visible history.

### A.16.2:22 - Review Addendum for Retreat Integrity

Add three checks to the base retreat matrix:

- **Were downstream dependencies updated?**
- **Was the propagation scope truthful?**
- **Does the revised history remain legible?**

These checks keep `A.16.2` tied to explicit recovery and retirement rather than narrative smoothing.
### A.16.2:End


## A.17 - Canonical “Characteristic” (A.CHR‑NORM)

### A.17:1 - Context

To have reproducibility and explainability there is a need to **measure** various aspects of systems or knowledge epistemes or publications. A dedicated measurement backbone (see **C.MM‑CHR**, Measurement & Metrics Characterization) already exists, prescribing the **CSLC discipline** – i.e. define a **Characteristic**, choose a **Scale** (with a **Unit** if applicable), record a **Level/Value**, and thus obtain a **Coordinate** on that scale, optionally mapping to a **Score** via a **ScoringMethod (USCM)**. However, historically multiple near-synonyms (“axis”, “dimension”, “property”, “feature”, "metric") have been used interchangeably for “what is being measured,” and often the _aspect itself_ gets conflated with _how it is expressed_ (units, ranges, labels). This pattern enters the FPF **Kernel lexicon** to **canonize a single term** for the measured aspect and enforce a clear separation between **what** is measured and **how** it is measured.

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

-   **F6 – Open-endedness.** As systems evolve, their performance or quality metrics also evolve. Rigid stage labels (“Phase 1, Phase 2…”) don’t capture iterative improvement. The pattern should favor an **open-ended state-space** view (revisiting states via checklists, as in an RSG – **RoleStateGraph** with re-entry) over any fixed stage sequence with “terminal” stages.

### A.17:4 - Solution

**Establish “Characteristic” as the one canonical construct for “what is measured.”** In every FPF context, the _aspect or trait_ being measured MUST be referred to as a **Characteristic**. This term replaces “axis” or “dimension” in normative usage (those may appear _only_ as explanatory aliases in Plain register). By fixing a single name and schema, we cleanly separate a **Characteristic** from its **Scale** (and **Unit**), and from any observed **Value/Level** on that scale. The solution also differentiates single-entity vs multi-entity cases and binds all measurements to the standard CSLC sequence.

To enforce this solution, the following rules apply:

-   **A17-R1 (Canonical term).** In all normative models and specifications, the measured aspect **SHALL** be referred to as a **Characteristic**. (Legacy terms “Axis” or “Dimension” are retired from technical vocabulary – see Part J Lexicon Update.)

-   **A17-R2 (Entity vs. relation subtype).** Each Characteristic **MUST** declare its intended _arity_. An **Entity-Characteristic** applies to exactly one bearer (e.g. _Temperature_ of a reactor, _Evolvability_ of a software module), whereas a **Relation-Characteristic** applies to an ordered tuple of two or more bearers (e.g. _Distance_ between two sensors, _Coupling_ between modules, _Agreement_ among reviewers). The arity is part of the definition and **must be explicit** wherever it’s not obvious from naming.

-   **A17-R3 (Characteristic space).** Any set of defined Characteristics spans a multi-dimensional **CharacteristicSpace**. Movement or evolution is then described as trajectories through this space (with states revisited or refined over time), rather than as a linear stage sequence through preset phases. This ensures measurements feed into open-ended state modeling rather than locking into “end states.”

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

**In an epistemic context (`U.Episteme`):** Consider a **Formality** Characteristic to rate a documentation episteme's rigor. We might define an ordinal Scale with named Levels such as _Informal_, _Semi-formal_, _Formal_. A given specification document can then be said to have _High Formality_ – meaning it occupies the “Formal” **Level** on the Formality Scale. Here _Formality_ (Characteristic) captures _what_ we measure about the document, while the tiered Scale (with qualitative levels) expresses _how_ we categorize it. Because we use an ordinal scale, we can rank documents by Formality, but we would not average “Semi-formal” and “Formal” (avoiding meaningless arithmetic on an ordinal metric). In another knowledge context example, one could define a Characteristic **Reliability** for a knowledge source with a percentage Scale from 0 to 100%. An article’s reliability might be 85% – which is only interpretable by knowing it refers to “Reliability” on a 0–100% Scale (i.e. a specific Coordinate on that Characteristic’s scale).

### A.17:6 - Bias-Annotation

This pattern is deliberately **domain-neutral** and introduces no bias toward any particular discipline or measurement type. By enforcing a uniform lexicon, A.17 actually mitigates bias: it prevents **disciplinary jargon** from creeping into core definitions (ensuring, for instance, that a software metric isn’t given a vague custom term when it’s fundamentally a Characteristic). The **Didactic lens** is served: using one precise name per concept improves clarity for all audiences. There is a slight initial cost in re-labeling legacy terms (e.g. renaming “dimensions” to Characteristics), but this is offset by the long-term **Cognitive Elegance (P‑1)** – the framework becomes easier to learn and less prone to misinterpretation. No single domain’s terminology dominates, and the pattern explicitly supports both quantitative (physics-like) and qualitative (judgment-based) measurements, reflecting **Pragmatic neutrality**. The requirement of open-ended state-space thinking aligns with **P‑10 (Open-Ended Evolution)**, ensuring we don’t bake in lifecycle biases that assume development must terminate at a final stage. In summary, A.17 imposes a disciplined vocabulary that is broad enough for all fields and free of hidden assumptions, thereby avoiding subtle ontological or cultural biases in the measurement model.

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

-   **Consistent evolution framing:** By retiring the idea of a bespoke fixed stage sequence for every process and instead viewing changes as movement in a CharacteristicSpace, the pattern aligns metric thinking with state-based reasoning (e.g. as used in dynamic models). There is no artificial “final state” for improvement – a system can always evolve to a new coordinate without violating a declared state model. This open-ended view encourages continuous improvement and refinement, echoing FPF’s emphasis on evolutionary development.


There are few downsides. One consequence is that modelers must learn the canonical terms and possibly refactor existing documentation (a short-term effort). Also, enforcing scale integrity means quick-and-dirty aggregate scores are not allowed unless justified via a SCP – this introduces a healthy “pause” to ensure composite metrics are well-founded. Overall, the benefits in clarity and correctness far outweigh the overhead. Teams gain a _lingua franca_ for metrics, and the risk of metric abuse (mixing apples and oranges) is significantly reduced.

### A.17:9 - Rationale

The Canonical Characteristic pattern is a direct response to recurring measurement pitfalls. By insisting on “one precise name per concept”, it upholds **Strict Distinction (A.7)**, ensuring that the framework never treats two different ideas as one. For instance, earlier practice might label both a requirement category and its score as “dimension,” causing confusion; with A.17, the _aspect_ is a Characteristic and its _score_ is separate, so each idea has its place. This clarity is pedagogically vital (**P‑2 Didactic Primacy**): readers and contributors immediately know what a term means and how to interpret any value associated with it.

The solution also draws on fundamentals of measurement theory (Stevens’ levels of measurement) to prevent misuse. By encoding scale types and unit handling into our patterns, we avoid the “pseudo-quantitative” fallacies – no more averaging things like _risk levels_ or adding up _grades_ as if they were true numbers. In effect, A.17 puts a safeguard around **P‑1 Cognitive Elegance and P‑7 Ontological Parsimony**: we use a minimal, universal set of measurement constructs, and we avoid bloating the conceptual space with domain-specific or redundant terms. One canonical set of terms also makes the framework more teachable and **composable across contexts**, since patterns and projects aren’t inventing new synonyms that others must decipher.

Importantly, distinguishing Entity vs Relation Characteristics future-proofs the reasoning model. It enforces a modeling rigor seen in domains like physics (where properties vs. relations are carefully distinguished) and brings it to architecture and knowledge domains. This rigor supports advanced reasoning in FPF – for example, **A.3.3 (Dynamics)** can treat system state variables as a well-defined set of Characteristics, and assurance patterns can trace **evidence metrics** unambiguously to the exact aspect measured. It also means any attempt to compare or combine metrics has to be explicit (via ScoringMethods), which inherently improves **transparency and auditability** (a key FPF goal).

Finally, retiring fixed-stage vocabulary in favor of state-space trajectories aligns with FPF’s **open-ended evolution** principle. It acknowledges that improvement is not a predefined path but a navigable space. This shift in mindset (from fixed stages to checklisted state transitions) removes an implicit bias that systems _ought_ to reach a “final” maturity stage – instead, it keeps the door open for perpetual refinement, which is philosophically aligned with continuous learning and adaptation.

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

We often need to **characterize some aspect** of a subject, whether the subject is one entity or a relationship between entities. Whether it’s recording a physical quantity, an architectural property, or a performance rating, the characterization must:

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


Using this **CSLC structure**, every measurement is unambiguous and self-contained: the Characteristic tells us the context, the Scale tells us how to interpret the value, and the Coordinate is the outcome on that scale (with a Level label if appropriate). Notably, this pattern _forbids bundling multiple characteristics into one metric_ – each metric template is one-characteristic-per-template to keep semantics crisp. If something needs to assess multiple factors, it should be modeled as multiple CSLC metrics or an explicit composite over several CSLC metrics (see §8 below). This one-aspect-one-scale rule is what allows unambiguous comparison and prevents hidden complexity.

Finally, the solution ensures **tier optionality**: If a domain uses named Levels, we include them; if not, we don’t force it. For example, one can have a _Bug Severity_ Characteristic with Levels {Minor, Major, Critical} on an ordinal scale, whereas a _Length_ Characteristic would have a continuous scale (no predefined levels, just units). Both fit the pattern.

#### A.18:4.1 - Characteristic-space support must stay declared

- When one front, archive, shortlist, or derived tradition view is discussed in one space, declare the object kind and the relevant characteristic space explicitly.
- Use one `SpaceRef` only when the text truly needs to recover which space or typed feature family is carrying the comparison.
- One declared space does not imply that every neighboring line must use the same space.
- Different declared spaces may coexist for the same family when they answer different comparison questions, but the active one must stay recoverable.
- If one atlas-like reading uses several declared spaces over the same palette, front, archive, or shortlist family, say which `SpaceRef` is active in the current reading rather than letting the atlas label hide that choice.
- If one outcome surface is materially different from one representation or search surface, keep that difference explicit rather than calling both simply `space`.
- `OutcomeMapRef` is warranted only when the text needs one declared map from the current set surface into one outcome or effect surface.
- When `OutcomeMapRef` is cited for one atlas-like or cross-scale reading, keep the source set surface and the projected outcome surface visible together so the map stays support for the view rather than a replacement default.

### A.18:5 - Archetypal Grounding (System & Episteme Examples)

**In a physical scenario (`U.System`):** Consider an athlete’s long jump. We define a Characteristic **Jump Distance** with a Scale “meters (m)” ranging from 0 upward (ratio scale with meters as the unit). When the athlete jumps and lands at 7.45 m, we record a **Coordinate** of _7.45 m_ for the Jump Distance Characteristic. Here, Jump Distance is the Characteristic, the meter-scale is the declared Scale, and _7.45 m_ is the value (Coordinate). Because this is a cardinal measurement, we can meaningfully say one jump is 1.5 m longer than another, etc. Now consider another metric in the system: **Battery Health** of a device, which might be categorized qualitatively. We could define an ordinal Scale with Levels like _Good, Fair, Poor_ for the Battery Health Characteristic. If a particular device is rated “Poor”, that is a Coordinate on the Battery Health scale (with _Poor_ as the Level name). No arithmetic is done on these labels, but we can order devices by health (Good > Fair > Poor). Both examples illustrate the one-characteristic-one-scale rule: the jump’s distance is not combined with any other aspect; the battery’s health is evaluated on its own defined scale.

**In a knowledge context (`U.Episteme`):** Consider measuring an author’s expertise in a certain domain. We introduce a Characteristic **Expertise Level** for a person, with an ordinal Scale defining tiers such as _Novice, Competent, Expert_. Alice might be assessed at _Expert_ level in software engineering – that’s a **Coordinate** on the Expertise Level scale for the Characteristic “Software Engineering Expertise”. Bob might be at _Competent_. We cannot average Alice’s and Bob’s levels, but we can say the scale is ordered (_Expert_ > _Competent_ > _Novice_). For a more quantitative episteme example, consider a Characteristic **Hypothesis Confidence** for a scientific claim, with a Scale 0–1 (or 0–100%) representing probability or confidence level (ratio scale). One hypothesis might have a confidence of 0.95, another 0.7; these are Coordinates on the Confidence scale. We can compare them numerically (0.95 is higher than 0.7, and 0.95 _implies_ higher confidence), and we could even combine multiple confidence values through Bayesian formulas (if justified) – but crucially, we would only do so in a way that respects their scale (probabilities combined properly, not treated as arbitrary scores). The Expertise Level and Hypothesis Confidence examples show how the CSLC pattern accommodates both an ordinal qualitative measure and a continuous quantitative measure in the knowledge domain, each with one Characteristic and one defined Scale.

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

Overall, A.18’s consequences are overwhelmingly positive: **measurements become first-class, well-understood citizens of the model.** The cost is a slight increase in definition effort and discipline, which is a small price for coherence. Once this pattern is in place, neighboring patterns in Parts B, C, and D that reason about metrics can rely on it. For example, trust calculations (Part D) can assume that any metric they consume has a known scale and meaning, and knowledge dynamics algorithms (Part B or C) can safely combine evidence knowing the comparisons are valid. The minimal CSLC Standard is thus a foundational enabler for robust, cross-domain assurance in FPF.

### A.18:9 - Rationale

The rationale behind A.18 is to enforce _semantic clarity_ at the data level, thereby solving many downstream problems. Without this pattern, one must constantly ask, “What does this number mean? Can I combine these two values?” – questions that have led to many project errors. By building the answers into the framework (“every number knows its unit, scale, and aspect”), we front-load the work and eliminate ambiguity. The solution directly addresses each force:

-   **Transdisciplinarity:** We include both ordinal and cardinal mechanisms so that no discipline’s metrics are left out. This was informed by observing multi-disciplinary teams: e.g., in a single project, a human factors specialist might rate usability (ordinal) while an engineer measures throughput (ratio). A.18 gives them a common language and prevents one from misusing the other’s data. It embodies the idea that _universal structure enables local freedom_: everyone’s metric can plug in, as long as they specify it properly.

-   **Comparability vs. freedom:** The pattern strikes a balance by tying comparability to explicit commonality. If two metrics truly measure the same `U.Characteristic` on the same Scale by the same measurement procedure, then of course you can compare them. If they differ, the framework doesn’t stop you from defining them (freedom), but it does stop you from _conflating_ them inadvertently. The introduction of **polarity** declarations is a direct response to this tension: it adds a small declaration requirement (must declare “higher is better” etc.) but yields big pay-off in avoiding mis-ordered interpretations and enabling safe composite scoring (monotonic ScoringMethods).

-   **Ordinal vs. cardinal separation:** The rationale here is guided by measurement theory: we want to preserve information content. Treating ordinal data with only order operations preserves all its information; doing more (like adding them) injects false information. The pattern’s strictness on scale types forces modelers to be honest about what their data can and cannot do. This not only prevents errors but also encourages **best practices** (e.g. if you find you desperately want to average an ordinal score, perhaps you should refine it into an interval scale in your methodology). The outcome is a framework that respects both the **qualitative** and **quantitative** realms appropriately, aligning with **FPF’s Pillar of Pragmatism** – use formalism where it’s justified, but not beyond its limits.

-   **Optional Levels:** Requiring Levels in every case would have been too rigid (not everything has named tiers), but not supporting them would fail domains that rely on them (like maturity models or grading systems). The rationale for making Level _optional_ is to accommodate both. We saw in practice that many metrics naturally form tiers (e.g. technology readiness levels TRL 1–9) and giving them a slot in the model (instead of burying them in definitions) makes those metrics much easier to work with and integrate. Meanwhile, continuous metrics carry no baggage of unused fields. This design was checked against existing standards (like ISO 25024 for quality measures) to ensure we aren’t deviating from industry expectations: indeed, separating the concept (Characteristic) from the scheme (Scale) aligns well with standards, and including an optional categorization aligns with common practice in capability maturity models, etc.

-   **Method neutrality:** The decision to _not_ include any measuring procedures in A.18 (no specific formulas, no mandated evidence type) comes from the principle of separation of concerns. The kernel should provide the _what_ and _how (structurally)_, while neighboring measurement or method patterns provide method-side constraints and evidence expectations. This keeps the kernel lean (**P‑1 Cognitive Elegance**) and allows domain experts to implement whatever method is appropriate, merely committing to wrap their results in the CSLC form. By doing so, we avoid any bias toward empirical vs analytical, or manual vs automated measurements – FPF welcomes all, as long as they conform to the schema. This was rationalized by examining case studies: e.g., some reliability metrics come from formal proofs (analysis), others from testing (empirical) – the kernel can carry both result kinds identically, requiring only that each result says what it measured and on what scale.


In essence, A.18 is the _infrastructure of meaning_ for metrics. It may appear as a simple template, but it’s profoundly enabling. It forces clarity at creation time, so we don’t have to infer or debate meaning at usage time. The pattern’s practical payoff lies in preventing errors that _don’t have to happen_. It encodes lessons from both metrology (the science of measurement) and everyday data science (where unit errors and mis-comparisons are infamous issues). The rationale is backed by these lessons: **fix the interpretation rules in the design, and you eliminate entire classes of confusion and mistakes.** By having this in the kernel, every mechanism – from knowledge scoring to system performance – benefits immediately, and their results become interoperable to a degree that would be impossible without a common structure.

### A.18:10 - Relations

-   **Extends/Uses:** **A.17 (CHR-NORM)** – A.18 explicitly builds on the canonical terminology established in A.17. It uses the term **Characteristic** as defined there (and no other synonyms) and carries forward the edict that “axis/dimension” be treated as mere narrative aliases. It also leverages the Entity-vs-Relation Characteristic distinction from A.17: Section 7.4 of this pattern references tests for disambiguating relational metrics. Essentially, A.17 provides the **lexical and conceptual groundwork** (what a Characteristic is, and the basic vocabulary), while A.18 provides the **structural and normative rules** for linking Characteristics to measurements.

-   **Core foundation for metrics:** This pattern underpins the **Measurement & Metrics Characterization spec (C.MM‑CHR)** – the pattern that implements metric storage and computation. In MM-CHR, every `U.DHCMethodRef` and `U.Measure` follows the CSLC format defined by A.18. By lifting CSLC rules to the kernel, we ensure all FPF patterns (like **KD-CAL** for knowledge dynamics, **Sys-CAL** for systems, or any custom CAL/CHR) share a common approach to metrics. A.18 also informs the design of **CHR-CAL (Characterisation Calculus)**, which generalizes measurable property templates: CHR-CAL relies on the one-Characteristic-per-metric assumption and the comparability rules set here to compose composite characterizations.

-   **Enables dynamic reasoning:** A.18’s insistence on well-defined Scales allows patterns like **A.3.3 `U.Dynamics`** (system dynamics models) to incorporate measurement dimensions as state variables without ambiguity. For example, a `stateSpace` in a dynamics model can be explicitly defined as a set of Characteristics (each with units and ranges), making simulations and traces dimensionally consistent. If A.18 were not in place, one model might treat “performance” as a 1–5 score and another as a probability – combining them would be incoherent. With A.18, such differences must be reconciled via a ScoringMethod or kept separate, preserving coherence in multi-model analyses.

-   **Coordinates with assurance patterns:** Many patterns in Part B and D (for trust, assurance, and ethics) involve **scores** and **metrics**. For instance, **B.3** (Assurance Levels) computes overall assurance from evidence scores; A.18 ensures those input scores are well-defined and comparable (e.g. all are 0–1 or all are percentages, with polarity noted). **D.4** (Trust-Aware Calculus) might combine trust metrics across domains – again, A.18 provides the common ground so that a “trust score” coming from an operational metric and one coming from a social rating can be normalized and compared meaningfully. In summary, any pattern that aggregates or uses measurements is constrained (in a positive way) by A.18’s rules. They “plug into” this framework.


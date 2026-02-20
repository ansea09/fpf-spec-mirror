If `suite_protocols` is present, it SHALL include at least one protocol that is equivalent to the canonical **suite-closed** pipeline below (with `fold_Γ` explicitly optional).

**Show (canonical suite-closed protocol).**

```
normalize (UNM) →
indicatorize (UINDM) →
score (USCM) →
fold_Γ? (ULSAM) →
compare (CPM) →
select (SelectorMechanism)
```

**Tell.**

* The `fold_Γ` step is optional (explicitly optional, not implicit inside `score/compare/select`).
* `suite_protocols` encodes a pipeline/Uses contour between mechanisms; it does **not** define a specialisation ladder (`⊑/⊑⁺`). Specialisations live in `A.6.1:4.2.1` (and in project `P.*` extensions).
* Any publish/telemetry step is **outside** `suite_protocols` (to preserve WF‑MS‑2 closure) and is routed through established publication patterns (G.10 and/or PTM), not as “hidden tails” inside CHR mechanisms.

#### A.19.CHR:4.6 - P2W hook: mandatory planned baseline

**Tell.** Any P2W path that uses `CHRMechanismSuiteDescription` MUST include a `WorkPlanning` artifact:

an instance of kind `CHRMechanismSuiteSlotFillingsPlanItem` (where `CHRMechanismSuiteSlotFillingsPlanItem ⊑ SlotFillingsPlanItem`)

that acts as the **planned baseline** for all suite‑level pinned refs/editions/policies used downstream.

This is the mandatory bridge between:

* *selection* (G.* set‑return choice of candidates/policies), and
* *WorkEnactment* (FinalizeLaunchValues witness + gate execution + logs).

#### A.19.CHR:4.7 - Canonical concept card fragments

##### A.19.CHR:4.7.1 - `CHRMechanismSuiteDescription` as a concrete `MechSuiteDescription`

**Show (canonical skeleton; refs only).**

```
CHRMechanismSuiteDescription := ⟨
  mech_suite_id        : MechSuiteId,
  mechanisms           : [UNM.IntensionRef, UINDM.IntensionRef, USCM.IntensionRef,
                          ULSAM.IntensionRef, CPM.IntensionRef, SelectorMechanism.IntensionRef],

  suite_obligations    : SuiteObligations {
                          bridge_only_crossings,
                          two_bridge_rule_for_described_entity_change,
                          transport_declarative_only,
                          penalties_route_to_r_eff_only,
                          guard_decision_tristate(pass|degrade|abstain),
                          unknown_never_coerces_to_pass,
                          gate_decision_separation,
                          guard_lexeme_reservations,
                          no_thresholds_in_suite_core,
                          cg_spec_cite_required_for_numeric_ops,
                          no_silent_scalarisation_of_partial_orders,
                          no_silent_totalisation,
                          crossing_visibility_required,
                          planned_slot_filling_in_work_planning_only,
                          finalize_launch_values_in_work_enactment_only,
                          implementation_export_discipline_when_cited
                        },

  suite_contract_pins  : SuiteContractPins {
                          required_spec_refs := {CNSpecRef, CGSpecRef},
                          required_planned_baseline_ref := CHRMechanismSuiteSlotFillingsPlanItem,
                          required_edition_pins? := …,
                          required_policy_id_pins? := …
                        },

  suite_protocols?     : SuiteProtocol[*],            // includes the canonical pipeline
  suite_notes?         : …,                            // didactic boundaries + anti-patterns
  suite_audit_obligations? : …                         // UTS+Path pins, crossings visibility, guard ownership
⟩
```

##### A.19.CHR:4.7.2 - `CHRMechanismSuiteSlotFillingsPlanItem` as a `SlotFillingsPlanItem`

**Tell.** This plan item fixes the planned baseline for suite contract pins and for chosen mechanism/policy refs, within an explicit P2W context.

**Required fields (minimum; aligns with A.15.3 naming)**

* `target_slot_owner_ref` MUST be edition-addressable and MUST reference the `CHRMechanismSuiteDescription` instance (kind: `MechSuiteDescription`) via a `MechSuiteDescriptionRef@edition(…)` (the suite is the slot owner for this planned baseline).
* MUST include explicit context anchors:
  * `described_entity_ref` (a concrete RefKind per C.2.3),
  * `bounded_context_ref`,
  * `cg_frame_ref`,
  * `reference_plane` (unless unambiguously derivable from cited context artefacts; see A.15.3 context-derivability rule),
  * `path_slice_id`,
  * `publication_scope_id`,
  * `Γ_time_selector` (ByValue) or `Γ_time_rule_ref` (ByRef) — no implicit “latest”.
* MAY include `expected_usm_guard_pins ⊆ {USM.CompareGuard, USM.LaunchGuard}` (planned expectation only; not execution).
  If `expected_usm_guard_pins` is present and non-empty, the PlanItem MUST also pin (or make unambiguously derivable) `guard_owner_gate_ref` required for later aggregation of `GuardFail` events (A.15.3 guard-owner rule).
* MUST include planned fillings for (at least) the suite contract pins, expressed as `planned_fillings` rows keyed by the corresponding SlotKind tokens:
  * `CNSpecSlot` filled by `ByRef(CNSpecRef@edition(…))` (edition‑pinned where required),
  * `CGSpecSlot` filled by `ByRef(CGSpecRef@edition(…))` (edition‑pinned where required),
    and (when applicable) the chosen method/comparator/mechanism refs as planned fillers (e.g., `ScoringMethodDescriptionSlot`, `ComparatorSpecSlot`, …).
* When crossings are expected, MUST include `expected_crossing_policy_refs` (refs only):
  `⟨bridge_card_ref, phi_policy_id, psi_policy_id?, phi_plane_policy_id?, reference_plane(src,tgt)⟩ …`,
  and SHOULD include the corresponding `expected_crossing_surface_refs` (refs only) so crossing visibility has an explicit anchor.

**Prohibitions**

* MUST NOT contain `GateDecision` / `DecisionLog`.
* MUST NOT contain `FinalizeLaunchValues` witnesses or launch values.
* MUST NOT embed CL/Φ/Φ_plane tables; only refs/pins.

#### A.19.CHR:4.8 - Examples

##### A.19.CHR:4.8.1 - Example — normalization-based comparability with explicit Uses chain

**Show.**

* `CHRMechanismSuiteDescription` is referenced by a G‑pattern (e.g., method selection, parity selection, or lawful publish pipeline).
* WorkPlanning publishes `CHRMechanismSuiteSlotFillingsPlanItem` with:

  * pinned `CNSpecRef(ed=…)`, `CGSpecRef(ed=…)`,
  * pinned `ComparatorSpecRef(ed=…)` (from `CG‑Spec.ComparatorSet`),
  * pinned `ScoringMethodDescriptionRef(ed=…)` (e.g., a monotone scoring method),
  * explicit `Γ_timeSelector` (“point at …”, no implicit “latest”),
  * `ExpectedUSMGuards = {USM.CompareGuard, USM.LaunchGuard}`,
  * expected crossing policy pins for any cross‑context step.

The executed protocol (by E.TGA/P2W) is:
Suite-closed protocol:
`UNM → UINDM → USCM → CPM → SelectorMechanism`.
Downstream continuation (outside `suite_protocols`): publication/telemetry via `G.10` and/or `PTM`.

**SoTA note (illustrative, non-normative).** A `ScoringMethodDescription` here can represent a post‑2015 monotone model family (e.g., monotone lattice / constrained monotone learning) or a set‑valued scoring family (e.g., conformalized score intervals), as long as legality remains SCP‑bound and uncertainty is handled via tri‑state guards rather than being suppressed into a scalar.

##### A.19.CHR:4.8.2 - Example — archive portfolio mode with report-only illumination

**Show.**

* The same CHR suite is used, but the selected `SelectorMechanism` specialization (via G.* extension) returns an **Archive** portfolio.
* WorkPlanning plan item additionally pins:

  * `DescriptorMapRef@edition(…)` and `DistanceDefRef@edition(…)` (QD/illumination configuration),
  * an explicit policy ref that states illumination is **report‑only** by default,
  * a separate CAL policy‑id if illumination is ever promoted into dominance (never implicit).

**SoTA note (illustrative, non-normative).** Archive semantics align naturally with quality‑diversity families that matured after 2015 (MAP‑Elites‑class extensions, CMA‑ME‑class, etc.), while the pattern’s “promotion only via policy‑id” prevents an implicit collapse of diversity telemetry into dominance.

#### A.19.CHR:4.9 - Evolution rules

* **Kernel-first stability.** This suite is intentionally minimal. Adding a new core CHR mechanism to this kernel suite is a suite-version change and MUST be accompanied by alias docking (F.18) so existing references remain citeable. For exploratory or domain‑specific extra stages, prefer a suite variant (e.g., `A.19.CHR+` / `A.19.CHR.Extended`) or project‑level specializations (patterns P.\*) instead of mutating the kernel.
* **Mechanism specializations are not wiring.** Domain/project variants are expressed via A.6.1 (`⊑/⊑⁺`) under their semantic owner (typically a project pattern `P.*`), not by editing suite membership. The suite binds to `…IntensionRef`; the planned baseline (A.19.CHR:4.7.2 under A.15.3) chooses concrete instances/specializations.
* **Protocols evolve within the suite boundary.** Adding/changing suite protocols (A.19.CHR:4.5) is allowed as long as each protocol remains suite‑closed and does not import publish/telemetry as a mandatory step. If a protocol introduces a new required stage not present in membership, treat it as a suite variant rather than a protocol edit.
* **SoTA harvesting updates methods, not the kernel.** Updates from SoTA harvesting/synthesis (G.2) are carried via edition‑pinned `MethodDescriptionRef` / `ComparatorSpecRef` selections and wiring modules (`G.x:Ext.*`), keeping the kernel Intension set stable. If a SoTA update requires changing a mechanism’s signature/laws, the change happens in the owning A.6.1 card and MUST emit RSCR triggers from `G.Core`.
* **New mechanism families (outside CHR).** Introduce new mechanism kinds as new pattens in their mechanism suite pattern cluster. If they require suite‑level composition and P2W binding, add a new suite pattern `A.6.7.<FamilyKey>` plus a suite‑specific planned baseline specialization of A.15.3, mirroring the ownership routing of this pattern.

#### A.19.CHR:5.1 - `U.System` vignette (Tell–Show–Show)

**Tell.** A system-level decision must select a portfolio of options when measurable evidence comes from multiple slices (test rigs, simulations, field trials). Measurements are multi-scale and not always comparable without explicit normalization, and some evidence is missing or stale. The team needs lawful comparison and selection without forcing a single scalar “fitness”.

**Show.** The system’s P2W path cites `CHRMechanismSuiteDescription` and publishes `CHRMechanismSuiteSlotFillingsPlanItem` as the planned baseline:
`CNSpecRef(ed=…)`, `CGSpecRef(ed=…)`, chosen `ComparatorSpecRef(ed=…)`, chosen `ScoringMethodDescriptionRef(ed=…)`, explicit `Γ_timeSelector` (point or window), and expected guard pins.
WorkEnactment witnesses `FinalizeLaunchValues` and runs `UNM → UINDM → USCM → CPM → SelectorMechanism`, returning a set-valued portfolio (Pareto or Archive), while any cross-context reuse is surfaced by Bridge-only crossings and audit pins.

**Show.** If the team instead embeds normalization inside scoring (“we always normalize to [0,1]”) or collapses a partial order into a single weighted sum, the suite protocol explicitness and “no silent scalarization/totalization” obligations make the violation legible at review time, and the planned baseline cannot honestly pin the missing UNM/ULSAM steps.

#### A.19.CHR:5.2 - `U.Episteme` vignette (Tell–Show–Show)

**Tell.** A research episteme compares methodological claims across traditions where some evaluation scales are ordinal (rank-based) and others are interval or ratio. The group wants to select a method family for a task while keeping uncertainty explicit and avoiding illicit aggregation (e.g., averaging ranks).

**Show.** The episteme’s planned baseline pins `CNSpecRef` (comparability mode and indicator policy) and `CGSpecRef` (SCP, ComparatorSet, MinimalEvidence, Γ_fold). The suite runs `UINDM` to select indicators, `USCM` to compute lawful score measures under SCP, `ULSAM` only when Γ_fold is explicitly selected, and `CPM` to compare without scalarizing partial orders. The selector returns a portfolio rather than forcing a single winner.

**Show.** If a draft evaluation writes “take the mean rank and pick the minimum”, the pattern’s legality discipline forces the author either to (a) re-express the step as a lawful comparator declared in CG‑Spec, or (b) keep the result as report-only telemetry, not a dominance driver.

### A.19.CHR:6 - Bias-Annotation

**Lenses tested:** `Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`. **Scope:** Universal for any Part‑G (and adjacent) use of the CHR characterization core via `CHRMechanismSuiteDescription` and the corresponding P2W planned-baseline artifact.

* **Gov.** Bias toward fail-closed legality and explicit auditability (Bridge-only crossings, pinned spec refs, guard–gate separation). Mitigation: the tri-state `GuardDecision` allows uncertainty to degrade or abstain without forcing gate-level blocking; exploration can still proceed via explicit SoS‑LOG policy branches.
* **Arch.** Bias toward explicit node-level composition (E.TGA) and explicit P2W artifacts (`SlotFillingsPlanItem`). Mitigation: the suite fixes only the universal core; discipline-specific generators and extensions remain separate mechanisms connected by `Uses`, keeping the suite compact.
* **Onto/Epist.** Bias toward a strict separation of contracts (CN‑Spec/CG‑Spec), mechanisms (A.6.1), and planning epistemes (A.15.3). Mitigation: specialization is explicitly supported (`⊑/⊑⁺`) and does not require inventing new top-level constructs; method diversity is expressed via MethodDescription refs and ComparatorSpec refs.
* **Prag.** Bias toward conservative uncertainty handling (unknown does not coerce to pass) may reduce decisiveness. Mitigation: “probe-only” and “sandbox” behaviors are permitted as explicit, audited degrade modes (policy-id + branch-id), not as silent coercions.
* **Did.** Bias toward explicit terminology and pins increases authoring surface area. Mitigation: this pattern provides a canonical protocol and a single planned-baseline kind so authors can reuse a stable template rather than re-inventing local prose conventions.

### A.19.CHR:7 - Conformance Checklist

A work product set is conformant to **A.19.CHR** iff all applicable items below hold. Where useful, checklist items cite routed claim IDs from **A.19.CHR:4.3.7** to reduce paraphrase drift.

#### A.19.CHR:7.1 - Suite object checks

**CC‑A67CHR‑1 (Correct kind and level).**
A conforming `CHRMechanismSuiteDescription` SHALL be a `MechSuiteDescription` instance and SHALL NOT be encoded as a `MechFamilyDescription`.

**CC‑A67CHR‑1a (Stable citation handle).**
A conforming `CHRMechanismSuiteDescription` SHALL include a stable `mech_suite_id` suitable for downstream planning and `U.Work.Audit` citation.

**CC‑A67CHR‑2 (Canonical membership).**
A conforming `CHRMechanismSuiteDescription` SHALL enumerate exactly the six CHR mechanisms (UNM, UINDM, USCM, ULSAM, CPM, SelectorMechanism) as `U.Mechanism.IntensionRef`s.

**CC‑A67CHR‑2a (Membership set semantics).**
A conforming `CHRMechanismSuiteDescription.mechanisms` SHALL be duplicates-free and SHALL NOT treat order as semantic (WF‑MS‑1).

**CC‑A67CHR‑2b (No dangling IntensionRefs).**
Each `U.Mechanism.IntensionRef` enumerated in `CHRMechanismSuiteDescription.mechanisms` SHALL resolve to a canonical `U.Mechanism.Intension` publication under the single semantic owner pattern (draft stubs allowed; dangling refs are not). See `A.19.CHR:4.2.2`.

**CC‑A67CHR‑3 (Contract surfaces are pins, not copies).**
A conforming `CHRMechanismSuiteDescription` SHALL cite `CN‑Spec` and `CG‑Spec` as required spec refs and SHALL NOT duplicate them as “shadow specs”.

**CC‑A67CHR‑3a (Planned-baseline requirement is pinned).**
A conforming `CHRMechanismSuiteDescription` SHALL set
`suite_contract_pins.required_planned_baseline_ref = CHRMechanismSuiteSlotFillingsPlanItem`
so the P2W seam is enforced by the suite contract surface (not by ad hoc prose).

**CC‑A67CHR‑4 (Crossing discipline is complete).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL include, at minimum:
`bridge_only_crossings`,
`two_bridge_rule_for_described_entity_change`,
`transport_declarative_only`,
`penalties_route_to_r_eff_only`,
`guard_decision_tristate(pass|degrade|abstain)`,
`unknown_never_coerces_to_pass`,
`gate_decision_separation`,
`guard_lexeme_reservations`,
`cg_spec_cite_required_for_numeric_ops`,
`no_silent_scalarisation_of_partial_orders`,
`no_silent_totalisation`,
`no_thresholds_in_suite_core`,
`crossing_visibility_required`,
`planned_slot_filling_in_work_planning_only`,
`finalize_launch_values_in_work_enactment_only`,
`implementation_export_discipline_when_cited`.

**CC‑A67CHR‑5 (Guard/gate separation).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL:
1) enforce tri‑state guard decisions (`pass|degrade|abstain`),
2) enforce `unknown_never_coerces_to_pass`,
3) enforce guard–gate separation (no `GateDecision` / `DecisionLog` at mechanism/suite level; `block` remains gate‑only), and
4) enforce guard lexeme reservations (`USM.CompareGuard` / `USM.LaunchGuard` are gate-level pins; mechanism predicates use `…Admissibility/…Eligibility`).

**CC‑A67CHR‑6 (No hidden scalarization/totalization).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL include explicit bans on silent scalarization of partial orders and silent totalization.

**CC‑A67CHR‑7 (No thresholds in core + single-source defaults).**
A conforming `CHRMechanismSuiteDescription.suite_obligations` SHALL include `no_thresholds_in_suite_core`.
If any suite protocol relies on defaults (e.g., portfolio mode), the artefacts SHALL cite those defaults from their single declared source (typically a TaskSignature or explicit policy-id), and SHALL NOT introduce competing defaults in the suite.

**CC‑A67CHR‑8 (Protocol explicitness + closure).**
If `suite_protocols` is present, a conforming `CHRMechanismSuiteDescription` SHALL:
1) express any dependence as an explicit protocol step (no hidden invocation of UNM/UINDM/ULSAM inside score/compare/select), and
2) satisfy WF‑MS‑2 (protocol closure): every protocol step cites a mechanism that is a member of the suite.

**CC‑A67CHR‑8a (Canonical protocol is available when protocols are published).**
If `suite_protocols` is present, a conforming `CHRMechanismSuiteDescription` SHALL include at least one protocol equivalent to:
`normalize (UNM) → indicatorize (UINDM) → score (USCM) → fold_Γ? (ULSAM) → compare (CPM) → select (SelectorMechanism)`,
where `fold_Γ` is explicitly optional.
Any publish/telemetry continuation is routed externally (e.g., via G.10 and/or PTM) and MUST NOT be encoded as a `ProtocolStep` inside `suite_protocols` (to preserve WF‑MS‑2 closure).

**CC‑A67CHR‑9 (Packaging separation).**
If protocols include `publish/telemetry`, it is routed through G.10 and/or PTM; the suite does not act as a pack/shipping artifact.

#### A.19.CHR:7.2 - Planned baseline checks

**CC‑A67CHR‑10 (Planned baseline exists on P2W paths).**
For each P2W path slice that uses the suite, Authors SHALL provide a `CHRMechanismSuiteSlotFillingsPlanItem` in WorkPlanning.

**CC‑A67CHR‑10a (Correct slot owner).**
A conforming `CHRMechanismSuiteSlotFillingsPlanItem` SHALL set `target_slot_owner_ref = CHRMechanismSuiteDescriptionRef` (edition-addressable when used as a reproducibility baseline).

**CC‑A67CHR‑11 (Plan item is baseline, not execution).**
The plan item contains planned fillers and pins only; it does not contain launch values, execution witnesses, gate decisions, or logs.

**CC‑A67CHR‑11a (Minimum P2W context anchors).**
A conforming `CHRMechanismSuiteSlotFillingsPlanItem` SHALL include, at minimum:
`described_entity_ref`, `bounded_context_ref`, `cg_frame_ref`, `path_slice_id`, `publication_scope_id`, and an explicit time selector (`Γ_time_selector` ByValue or `Γ_time_rule_ref` ByRef),
and SHALL either include `reference_plane` or make it unambiguously derivable from the cited context artefacts.

**CC‑A67CHR‑11b (Planned guard pins and guard ownership).**
If `expected_usm_guard_pins` is present in a `CHRMechanismSuiteSlotFillingsPlanItem`, it SHALL satisfy
`expected_usm_guard_pins ⊆ {USM.CompareGuard, USM.LaunchGuard}`.
If `expected_usm_guard_pins` is present and non-empty, the plan item SHALL also pin (or make unambiguously derivable) `guard_owner_gate_ref` required for later aggregation of `GuardFail` events (per the A.15.3 guard-owner rule).

**CC‑A67CHR‑11c (Planned contract pins are present).**
A conforming `CHRMechanismSuiteSlotFillingsPlanItem` SHALL include planned fillings (refs/pins; no copied content) for, at minimum, SlotKinds `CNSpecSlot` and `CGSpecSlot` (filled by edition‑pinned `CNSpecRef` / `CGSpecRef` where required by the chosen protocol).

**CC‑A67CHR‑12 (Edition/time explicitness).**
The plan item includes explicit time selector/rule (no implicit “latest”) and includes edition pins where the protocol is edition‑sensitive.
Edition pins MAY be carried via edition-addressable refs in `planned_fillings` and/or via per-row `SlotFillingRow.edition_pin` (A.15.3 edition-pin rule); they MUST remain pins/anchors, not copied artefacts.

**CC‑A67CHR‑13 (Crossing pins are refs-only).**
Expected crossings are expressed via Bridge/policy refs and ReferencePlane pins; no embedded CL/Φ tables.
If expected crossings are listed, `expected_crossing_surface_refs` SHOULD be provided (or be unambiguously derivable) so crossing visibility has an explicit audit anchor.

**CC‑A67CHR‑14 (Audit traceability).**
The plan item is citeable from downstream `U.Work.Audit` as the planned baseline, and deviations (retarget/substitute/assign/update) require a variance trace.

#### A.19.CHR:7.3 - MVPK face checks (when projected)

**CC‑A67CHR‑15 (Views do not add meaning).**
Any `TechCard(…)` / `PlainView(…)` projection of the plan item does not introduce new assertions beyond the plan item.

**CC‑A67CHR‑16 (Fail-closed pins on claimful faces).**
If a face publishes edition pins or claims comparability/launch, it MUST also publish the required BridgeCard + UTS row anchors and the appropriate USM guard pin with `GuardOwnerGateSlot`; otherwise, it is nonconformant (fail‑closed).

### A.19.CHR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Avoid / repair |
|---|---|---|
| Using `MechFamilyDescription` as a suite container | Collapses “many implementations of one mechanism” into “many mechanisms”, mixing levels and breaking reuse contracts | Use `MechSuiteDescription` for multi-mechanism sets; use `MechFamilyDescription` only for multiple implementations of a single `U.Mechanism.Intension` |
| Embedding a second CG‑Spec or CL/Φ/Φ_plane tables inside the suite or plan item | Duplicates the contract center and creates drift between planning, gates, and audit | Publish refs and pins only (`CGSpecRef`, `BridgeCardRef`, policy-id pins); keep tables in their canonical registries and cite them |
| Implicit UNM/UINDM/ULSAM “inside” score/compare/select | Breaks auditability and violates the suite protocol explicitness obligation | Make dependencies explicit as protocol steps (`Uses`) and cite the chosen mechanism instances in the planned baseline and audit pins |
| Hidden thresholds or weights in CHR core | Moves acceptance criteria into the wrong layer, defeating “single source of defaults” and traceability | Keep thresholds in AcceptanceClauses, TaskSignature, or GateProfile; if a policy is needed, mint a policy-id and cite it explicitly |
| Scalarizing partial orders “for convenience” | Violates set-return semantics and hides incomparability | Keep comparisons set-valued via CPM and selectors portfolio-returning; any scalar summary must be declared as report-only telemetry or as an explicit lawful comparator |
| Treating planned baseline as a launch witness | Smuggles execution facts into planning and blurs P2W separation | Record planned slot fillings in WorkPlanning; witness `FinalizeLaunchValues` only in WorkEnactment and cite the plan item as baseline with variance traces |
| Using `CompareGuard` / `LaunchGuard` as mechanism lexemes | Collides with reserved gate-level pins and blurs guard vs gate responsibilities | In mechanisms use `…Eligibility` / `…Admissibility`; reserve `USM.CompareGuard` and `USM.LaunchGuard` for gate-visible pins |

### A.19.CHR:9 - Consequences

| Consequence | Upside | Cost / risk | Mitigation |
|---|---|---|---|
| One canonical CHR core anchor for Part G | Universalization becomes structurally simpler: G patterns cite one suite and specialize via `⊑/⊑⁺` or `Uses` | Up-front refactoring effort | Use the suite as a non-invasive anchor: keep existing method/generator constructs but route them through stable SlotKinds and planned baselines |
| Explicit P2W planned baseline | Eliminates hidden slot filling and improves auditability of editions, time selectors, and crossings | Adds a planning artifact per path slice | Keep the plan item minimal (refs and pins only) and project it to views for readability when needed |
| Tri-state guard semantics | Avoids false precision and prevents unknown from silently passing | More conservative behavior can yield larger portfolios or more abstentions | Use explicit SoS‑LOG degrade branches for probe-only exploration while preserving traceability |
| Contract pins, not copied contract content | Reduces drift and keeps CN‑Spec/CG‑Spec as real centers of gravity | Requires discipline in authoring and review | Enforce “refs-only” at suite/plan level and use conformance items CC‑A67CHR‑3 and CC‑A67CHR‑13 to keep the surface clean |

### A.19.CHR:10 - Rationale

This pattern deliberately fixes the CHR core as a **description object** rather than a new “meta-mechanism” so that:

1. **Level separation stays clean.** The suite is a D-episteme that enumerates mechanisms and obligations; the mechanisms remain `U.Mechanism.Intension` nodes with their own SlotSpecs, laws, guards, transport and audit. This prevents a “god object” that re-implements A.6.1 inside a new container.

2. **Contracts remain centralized.** CN‑Spec and CG‑Spec already define the contract surfaces for comparability, normalization, indicatorization policy, and numeric legality. The suite requires those specs as pins and forbids duplicating them, making “one center of gravity” operational rather than rhetorical.

3. **P2W integration becomes explicit without turning planning into execution.** A planned-baseline `SlotFillingsPlanItem` is the minimal, reusable way to record “what will fill which slots under which CG-frame and path slice” while preserving the rule that only WorkEnactment witnesses launch values.

4. **Uncertainty handling is made safe by construction.** Tri-state guard decisions are a minimal contract that supports lawful abstention and degradation while keeping gate decisions and decision logs in their proper place (OperationalGate(profile)).

In short: *contracts are cited, not copied; plans are declared, not executed; and legality is a first-class surface, not a hidden tail.*

### A.19.CHR:11 - SoTA-Echoing

This pattern aligns with several post‑2015 practice lines while adapting them to FPF’s concept-first, contract-pinned discipline.

| Practice line (post‑2015) | Primary source | What is adopted here | Adoption status |
|---|---|---|---|
| Architecture description standards emphasize explicit viewpoints, explicit views, and view consistency rules. | ISO/IEC/IEEE 42010:2022 | “Views are projections of existing content” is mirrored by MVPK faces that do not add meaning beyond the underlying episteme. | **Adopt/Adapt:** adopt the viewpoint discipline; adapt terminology to FPF’s `U.View` projections. |
| Selective classification work formalizes abstention/deferral under uncertainty as a first-class outcome. | Geifman & El‑Yaniv (SelectiveNet, 2019) | A first-class “abstain/defer” outcome is mirrored by tri-state `GuardDecision` where unknown does not coerce to pass. | **Adapt:** integrate abstention into guard outputs while keeping gate decisions/logs gate-only (SoS‑LOG for degrade branches). |
| Quality-diversity research treats diverse portfolios/archives as first-class outputs rather than forcing a single optimum. | Pugh, Soros, Stanley (Quality Diversity, 2016) | Treating portfolios/archives as primary outputs aligns with set-return selection and Archive mode, with illumination treated as report-only unless promoted by policy-id. | **Adapt:** preserve legality pins and forbid hidden scalarization/totalization; allow promotion only via explicit policy-id. |
| Open-endedness research emphasizes continual portfolio maintenance and explicit task/environment generation separate from the selector kernel. | Wang et al. (POET, 2019) | The separation “universal core vs generators via Uses” mirrors the need to keep method/task generation separate from the selector kernel. | **Adapt:** add explicit edition pins and crossing visibility pins so maintenance remains auditable across contexts/planes. |

**Terminology drift and deltas.** Many contemporary sources speak in terms of “pipelines” and “provenance”. FPF’s delta is the explicit separation of (a) planned baseline in WorkPlanning, (b) execution witnesses in WorkEnactment, and (c) audit pins that remain conceptual anchors rather than tooling formats. Where external practice sometimes relies on implicit transfer assumptions, FPF requires cross-context reuse to be explicit as Bridge-only transport with visible pins (`BridgeId`, `CL` or `CL^k`, and the relevant Φ/Ψ/Φ_plane policy-ids), with penalties routed to `R_eff` only.

### A.19.CHR:12 - Relations

#### A.19.CHR:12.1 - Builds on

* **A.6.7 `MechSuiteDescription`** (the base suite description kind and obligations surface)
* **A.15.3 `SlotFillingsPlanItem`** (planned baseline in WorkPlanning)
* **A.6.1 `U.Mechanism.Intension`** and **A.6.5 slot discipline** (SlotSpecs in signatures; SlotIndex as projection)
* **A.19 CN‑Spec** and **G.0 CG‑Spec** (contract surfaces and legality gate)
* **E.TGA / E.18** (P2W, crossings, UTS and Path pins)
* **E.10** (lexical and ontological discipline) and **E.19** (conformance style)

#### A.19.CHR:12.2 - Coordinates with

* **G.5** (selector semantics, set-return defaults, archive semantics and report-only illumination discipline)
* **G.10** and **PTM** (publication and telemetry as external steps, not suite internals)
* **A.21 OperationalGate(profile)** and **USM.Guards** (gate-level decisions and reserved guard pins)
* **C.23 SoS‑LOG** (explicit degrade branches such as probe-only and sandbox)

#### A.19.CHR:12.3 - Constrains and informs

* Constrains Part G universalization: G patterns should reference this suite for the universal CHR node set and express method and generator specifics only as (a) explicit specializations (`⊑/⊑⁺`) or (b) separate provider mechanisms connected via `Uses`.
* Informs other kits and suites: any kit or suite that materially participates in selection should provide an analogous `…SlotFillingsPlanItem` planned baseline, so that the P2W seam remains uniform and auditable.

#### A.19.CHR:12.4 - Notes for Part‑G

**Tell.** This pattern is intended as a universal core anchor for the Part‑G:

* G patterns not mixing universal CHR legality mechanics with CG-frame specifics, discipline-specific method content, and packaging concerns in one construct.
* Instead, they cite `CHRMechanismSuiteDescription` (universal node set and obligations) and keep specifics in explicit specializations or separate `Uses` providers.
* P2W integration is performed uniformly via `CHRMechanismSuiteSlotFillingsPlanItem` planned baselines, preserving the rule that only WorkEnactment witnesses launch values.

### A.19.CHR:End

## A.19.UNM - Unified Normalization Mechanism (UNM)

> **Type:** Architectural (A)  
> **Status:** Stable  
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A / CN‑Spec cluster (A.19) / CHR mechanism owner patterns 
> **Semantic owner note (Phase‑3 canonicalization):** This pattern is the designated **single semantic owner** of the *meaning* of `UNM.IntensionRef` (per `E.20`). The canonical publication anchor for `UNM.IntensionRef` remains `A.19.UNM`, while `A.6.1` remains the owner of the `U.Mechanism.Intension` **template**.  
> **Non‑ownership note:** The `CN_Spec` surface itself (incl. `CN_Spec.normalization` and `CN_Spec.comparability`) remains owned by `A.19.CN`; this pattern specifies only UNM’s stable semantic surface and how UNM **consumes/interprets** the CN‑frame routing fields (no shadow CN‑spec).  
> **ID‑continuity:** legacy UNM mentions remain valid via *Tell + Cite* stubs (e.g., cite `A.19.UNM:4.1`).  
> **Canonicalization hook (Phase‑3):** Any other location that mentions UNM (including legacy “card fragments”) SHALL be reduced to *Tell + Cite* and SHALL NOT restate `SlotIndex / OperationAlgebra / LawSet / AdmissibilityConditions / Applicability / Transport / Γ_timePolicy / PlaneRegime / Audit`. This is the usability+didactic guard against “scattered semantics”.
**If someone says “we normalized”, ask (in this order):**
1) Which **`UNM_id`** (if applicable) and which **`NormalizationMethodInstanceId`** (and its validity window) was used?  
2) Which **`NormalizationInvariant[*]`** were declared (i.e., *what is preserved*)?  
3) Where are the **evidence pins** and any **transport / plane** pins (Bridge/CL/ReferencePlane + `UNM.TransportRegistryΦ/Phi` if invoked)?

**Mental model.** UNM **re‑parameterizes** a raw coordinate value (`CV`) into an `NCV` *under declared invariants* and exposes `≡_UNM` so downstream steps can be stated as “compare on invariants” *explicitly* (and audited).


### A.19.UNM:0 - At a glance — didactic, informative

**Intent.** Provide a single, explicit normalization mechanism for **coordinate values** in a `U.CharacteristicSpace`, so that **comparability** and downstream characterization steps can be stated as “**normalize-then-compare**” (governance), rather than as hidden arithmetic inside scoring/selection.

**Where it sits.**
- **CN-frame governance surface:** `CN_Spec.normalization` + `CN_Spec.comparability.mode` route whether comparison is `coordinatewise` or `normalization-based`.  
- **CHR suite role:** stage `normalize` (first-stage, when enabled by the suite protocol / comparability routing).

**Key outputs.**
- `NCV` (NormalizedCharacteristicValue) values for coordinates.
- A declared congruence `≡_UNM` (equivalence) induced by a chosen normalization method instance.
- Optionally, an explicit representative selection policy (`NormalizationFixSpec`, aka “NormalizationFix” in prose) when quotient objects must be presented as concrete chart items.

**Two IDs (do not conflate).**
- `UNM_id?` selects the **UNM mechanism instance** used by this CN‑frame (a `U.Mechanism` instance of type UNM; routing/governance level).
- `NormalizationMethodInstanceId` selects the **normalization method instance** applied to specific coordinate(s), with its validity window and evidence pins (method/application level).

**Minimum declaration set (didactic).**
- In `CN_Spec.comparability`: set `mode`, and (when UNM participates in acceptance/comparison) set `minimal_evidence`.
- In `CN_Spec.normalization`: declare `UNM_id?`, `methods`, `instances`, `method_descriptions`, `invariants`, and (if representatives are required) `fix`.
- In Audit: cite the chosen `NormalizationMethodInstanceId`, `NormalizationMethodDescriptionRef.edition`, declared invariants, validity window, evidence pins, and any Bridge/CL/ReferencePlane pins (plus the edition pin `UNM.TransportRegistryΦ/Phi` when transport is invoked).

**Non-goals.**
- Not indicator selection (that is **UINDM**).
- Not scoring, aggregation, comparison, selection (USCM / ULSAM / CPM / SelectorMechanism).
- Not a data governance system: UNM is a concept-level mechanism with explicit semantic ownership and auditability.

**Single-owner note (Phase‑3 canonicalization).**
This pattern is intended to become the **single semantic owner** of the canonical `U.Mechanism.Intension` for `UNM.IntensionRef`. Other locations that currently carry UNM “card fragments” should be reduced to **Tell + Cite** stubs pointing here, preserving public IDs/anchors.

### A.19.UNM:1 - Problem frame

FPF needs a disciplined way to talk about **measurable slots** (coordinates/scales) such that engineers can reason about:
- **What it means** to compare values across charts/slices/contexts, and
- **Where the “meaning-preserving” transformations live**, so comparisons are lawful and explainable.

In practice, teams routinely face a mismatch between:
- values that look comparable (“they’re numbers”), and  
- values that are not comparable without normalization (different units, scale types, reference planes, context semantics, or validity windows).

FPF’s CHR family explicitly separates stages (normalize → indicatorize → score → fold → compare → select). UNM is the *normalization* stage, and its job is to make “compare-on-invariants” explicit and auditable.

### A.19.UNM:2 - Problem

Without an explicit UNM owner pattern:

1) **Normalization drifts into hidden places.** It gets embedded inside scoring, comparison, or selection, making legality and governance non-local.

2) **Comparability becomes rhetorical.** People say “we normalize” but cannot answer:  
   *Which method? Which invariants? Which validity window? Which evidence? Which transport/plane regime?*

3) **Cross-context and cross-plane slips become invisible.** Teams “reuse” normalizations across contexts without explicit Bridge/CL/ReferencePlane discipline.

4) **Engineers cannot reconstruct the mechanism.** When UNM semantics are scattered, the pattern structure (problem/forces/solution) is lost, hurting didactic use by engineering managers.

### A.19.UNM:3 - Forces

| Force | Tension |
|---|---|
| **Evolvability vs Usability** | Stable mechanism surface ↔ method families evolve; single place to read ↔ modular wiring. |
| **Semantic precision vs Cognitive load** | Formal invariants/quotients ↔ a mechanism description that engineers can act on. |
| **Single-owner discipline vs Cross-cutting reality** | UNM touches CN/CG/transport/planes ↔ avoid “shadow specs” and duplicate centers of gravity. |
| **Trustworthiness vs Overreach** | “Normalization is legitimate” must be evidence-backed ↔ UNM must not pretend to define measurement meaning itself. |
| **Locality vs Reuse** | Normalization is context-local ↔ reuse requires explicit transport declarations (Bridge-only). |
| **Fail-closed safety vs Convenience** | Unknown/insufficient evidence must not coerce ↔ teams want “a number anyway”. |

### A.19.UNM:4 - Solution

UNM is a `U.Mechanism` that normalizes coordinate values using declared method classes, producing:
- normalized values (`NCV`),
- an induced congruence `≡_UNM`,
- and (when needed) a representative policy (`NormalizationFix`) for quotient objects.

UNM is **not** a bag of algorithms. It is a **canonical semantic surface**:
- **Routing** lives in `CN_Spec.normalization` and `CN_Spec.comparability.mode`.
- **Evidence/calibration legitimacy** lives in `C.16 (MM‑CHR)`.
- **Method families** can be supplied by SoTA packs and wired via extensions, without mutating UNM’s surface.

#### A.19.UNM:4.0 - Vocabulary (normative)

**NormalizationMethodId.** A stable token naming a normalization method *kind*, used in `CN_Spec.normalization.methods`.

**NormalizationMethod.** The method *kind* (class) that defines:
1) the **invariants** it preserves (`NormalizationInvariant[*]`),  
2) its **closure rules** (composition, and inverses where defined), and  
3) its **validity rules** (scope / context / time window constraints).

**NormalizationMethodDescription.** An editioned epistemic description of a normalization method (bounds, validity region/window, scope constraints, and evidence links owned by `C.16`).  
**NormalizationMethodDescriptionRef.** A ref to an editioned `NormalizationMethodDescription`, used in `CN_Spec.normalization.method_descriptions`.

**NormalizationMethodInstanceId.** A stable token naming a concrete, declared application of a normalization method to specific coordinate(s)/slot(s) in a host `U.CharacteristicSpace`, with a named validity window and (when required) evidence pins. Used in `CN_Spec.normalization.instances`.

**NormalizationMethodInstance.** The instance binding itself (conceptual); referenced in specs/logs/gates by `NormalizationMethodInstanceId`.

**CV (CoordinateValue).** A raw coordinate value for a **named measurable slot** in a chart: conceptually `⟨slot_id, raw_value⟩` (plus any chart/slice scoping needed by the host). UNM re‑parameterizes `CV → NCV` under declared invariants and validity constraints.

**NCV (NormalizedCharacteristicValue).** A normalized **value** for a coordinate (UNM does **not** “normalize characteristics”; it normalizes coordinate values under declared invariants).

**`≡_UNM` (UNM‑congruence).** A context‑local equivalence relation induced by a chosen `NormalizationMethodInstance`.
Two charts (or chart items/views) are `≡_UNM` iff they are related by a finite chain of admissible transformations that preserve the declared invariants.

**NormalizationInvariant.** A named invariant (e.g., unit alignment, polarity, reference plane) declared in `CN_Spec.normalization.invariants` and/or the selected `NormalizationMethodDescription`. Preserving the declared `NormalizationInvariant[*]` is the core admissibility claim for a normalization method instance.

**NormalizationFixSpec.** A declared policy selecting a canonical representative of a `≡_UNM` equivalence class when downstream consumers require a concrete chart item/view. Bound via `CN_Spec.normalization.fix` (otherwise keep quotient objects abstract).
**UNM_id.** An optional identifier in `CN_Spec.normalization.UNM_id?` selecting the UNM **mechanism instance** used by this CN‑frame. This is routing/governance; it is distinct from `NormalizationMethodInstanceId` (method/application).
**ValidityWindow.** A named validity window attached to a `NormalizationMethodInstanceId`, bounding where/when the instance is admissible (no implicit “latest”).

**`UNM.TransportRegistryΦ`.** An editioned anchor (single‑writer under UNM authoring) that enumerates the declared transport/plane pins and Φ‑penalties used when normalizations are reused across contexts/planes. Referenced via edition pins in suite/flow contracts; never re‑authored downstream.  
**Alias:** `UNM.TransportRegistryPhi` is an ASCII‑safe alias token (dock via `F.18`); it is **not** a competing head.

**Lexical guard (strict distinction).** Avoid the word **`map`** / **`mapping`** for UNM transforms (especially `Map`), because `Map` is a specialized FPF term and creates ontology drift. Prefer “normalization”, “re‑parameterization”, “transform under invariants”.
Legacy κ‑notation for normalization is retired; do not re‑introduce it.

#### A.19.UNM:4.1 - UNM as a `U.Mechanism.Intension` (normative)

**Scope note.** This Mechanism.Intension is authored to the `U.Mechanism.Intension` **shape** owned by `A.6.1`. It defines only UNM’s stable *semantic surface*. It does **not** bind project pins (editions/policy‑ids), which belong to the P2W seam (`A.15.3` + `A.19.CHR`), and it does **not** emit `GateDecision`/`GateLog`. It may emit tri‑state `GuardDecision` and Audit pins.

**IntensionHeader**
- `IntensionId`: `UNM`
- `IntensionRef`: `UNM.IntensionRef`
- `Name`: Unified Normalization Mechanism
- `Status`: Stable
- `Version`: `v1.0`
- `SuiteRole`: CHR.normalize (when enabled by CN/CHR routing)

**Imports (cite, don’t duplicate)**
- `A.6.1` (shape: `U.Mechanism.Intension`, specialization discipline)  
- `A.6.5` (slot discipline; SlotIndex is a projection)
- `A.19.CHR:4.2` (CHR suite boundary / membership)
- `A.19.CHR:4.2.1` (CHR SlotKind Lexicon)
- `A.19.CHR:4.5` (suite protocols: ordering/optionality; suite closure)
- `A.19.CN` (CN-frame routing: `normalization`, `comparability.mode`)
- `G.0` (CG-frame legality gates where required downstream)
- `C.16` (evidence carriers; calibration/validity for normalization legitimacy)
- `A.17/A.18` (measurement meaning & scale lawfulness; not redefined here)

**SubjectBlock**
- `SubjectKind`: `NormalizationMethod classes` (with induced `≡_UNM` over charts/views)
- `BaseType`: chart/`U.CharacteristicSpace` family in a CN‑frame (one `U.BoundedContext`), where normalization acts on coordinate values (`CV`) for measurable slots (UNM normalizes **values**, not characteristics)
- `SliceSet`: `U.ContextSliceSet` (context is explicit; no implicit “global normalization”)
- `ExtentRule`: “coordinate values admitted for normalization within the declared context and the method instance validity window”
- `ResultKinds`:
  - `NormalizedCharacteristicValue (NCV)`
  - `UNM‑congruence (≡_UNM)`
  - optional quotient objects and/or `Normalization‑fixed` representatives (via `NormalizationFixSpec`)

**SlotIndex (derived projection; minimum)**
- `CharacteristicSpaceSlot : ⟨ValueKind = U.CharacteristicSpace, refMode = U.CharacteristicSpaceRef⟩`
- `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`
- `ContextSlot : ⟨ValueKind = U.BoundedContext, refMode = U.BoundedContextRef⟩`

UNM‑specific slots (must be alias‑docked into the CHR SlotKind lexicon if used across the suite):
- `NormalizationMethodInstanceSlot : ⟨ValueKind = NormalizationMethodInstanceId, refMode = ByValue⟩`
- `NormalizationMethodDescriptionSlot? : ⟨ValueKind = NormalizationMethodDescription, refMode = NormalizationMethodDescriptionRef⟩`
- `NormalizationInvariantSetSlot? : ⟨ValueKind = NormalizationInvariant[*], refMode = ByValue⟩`
- `NormalizationMethodInstancePairSlot? : ⟨ValueKind = NormalizationMethodInstanceId[2], refMode = ByValue⟩`  *(used only by `compose`; roles = {inner, outer})*
- `CoordinateValueSlot : ⟨ValueKind = CV, refMode = ByValue⟩`
- `NCVSlot : ⟨ValueKind = NCV, refMode = ByValue⟩`
- `UNMCongruenceSlot : ⟨ValueKind = UNM‑congruence (≡_UNM), refMode = ByValue⟩`
- `NormalizationFixSlot? : ⟨ValueKind = NormalizationFixSpec, refMode = ByValue⟩`

**Authoring note (didactic).** `NormalizationMethodDescriptionSlot`, `NormalizationInvariantSetSlot`, and `NormalizationFixSlot` are typically *resolved/derived* from `CN_Spec.normalization.{method_descriptions,invariants,fix}` plus the selected `NormalizationMethodInstanceId`. They are listed here because they participate in eligibility/audit semantics — not because every operation takes them as explicit inputs.

**Note (transport anchor, not a SlotKind).** When transport/plane reuse is invoked, Audit MUST cite the edition pin key `UNM.TransportRegistryΦ` (aka `UNM.TransportRegistryPhi`) in the editions vector (see Transport/Audit), rather than introducing an ad‑hoc `…Ref` kind.

**OperationAlgebra (conceptual)**
1) `apply`
- Preconditions: `UNM_Eligibility(…) ∈ {pass, degrade}` (fail‑closed; `abstain` ⇒ no NCV output).
- Inputs: `NormalizationMethodInstanceSlot`, `CoordinateValueSlot`, `CharacteristicSpaceSlot`, `CNSpecSlot`, `ContextSlot`
- Outputs: `NCVSlot` (+ availability of `UNMCongruenceSlot` for the same method instance)

2) `compose`
- Purpose: build a composed method (only when explicitly declared lawful).
- Inputs: `NormalizationMethodInstancePairSlot` (roles = {inner, outer}), `ContextSlot`
- Output: `NormalizationMethodInstanceSlot` (new composed `NormalizationMethodInstanceId`), with an explicit validity window and evidence pins.

3) `quotient(≡_UNM)`
- Inputs: `CharacteristicSpaceSlot` (or chart view), `NormalizationMethodInstanceSlot`
- Output: quotient object under `UNMCongruenceSlot`  
  (When a concrete representative is required, `NormalizationFixSlot` (`NormalizationFixSpec`) must be declared and used.)

**LawSet (UNM laws; identifiers are stable)**
- **UNM‑L0 (Values, not characteristics).** UNM produces `NCV` as a **value** under declared invariants; it does not redefine the underlying characteristic meaning (measurement meaning remains owned by A.17/A.18 and evidence by C.16).
- **UNM‑L1 (Declared method class gate).** A normalization method instance is admissible only if its method is declared in the allowed method class set: `{ratio:scale, interval:affine, ordinal:monotone, nominal:categorical, tabular:LUT(+uncertainty)}`.
- **UNM‑L1a (Method semantics live in the method).** `NormalizationMethod` defines invariants, closure (composition / inverses where defined), and validity rules. UNM consumes these declarations; it does not invent “extra” legality.
- **UNM‑L2 (Congruence is first-class).** Each chosen method instance induces `≡_UNM` over charts/views; equality/comparability decisions that rely on normalization are defined on the quotient (or on a declared fix), not on raw labels.
- **UNM‑L2a (Context-local by default).** `≡_UNM` is context‑local; cross‑context reuse requires explicit transport declarations (Bridge-only).
- **UNM‑L3 (Fail‑closed).** If admissibility/evidence is insufficient (or required inputs are missing/stale), UNM does not silently coerce; it yields `abstain` or `degrade` (tri‑state guard discipline) and may surface an explicit freshness/work request (see A.19.UNM:4.5).  
  *Didactic reading:* `abstain` ⇒ no lawful NCV/comparability for this slice; `degrade` ⇒ NCV may be produced but must be treated as policy‑gated and auditable (never “quietly good enough”).
- **UNM‑L4 (No implicit indicatorization).** `NCV` does not imply “indicator”; indicator status is a separate policy step (UINDM).
- **UNM‑L5 (Bridge‑only transport).** Cross‑context reuse of normalization requires explicit Bridge-only transport declarations (Bridge id + channel + `ReferencePlane(src,tgt)`); describedEntity changes require a KindBridge (`CL^k`) and the two‑bridge rule. Penalties route to the **R‑lane only** (never to F/G; if scalarized, into `R_eff`).
- **UNM‑L6 (Time explicitness).** Validity windows are named; no implicit “latest”.
- **UNM‑L7 (Auditability).** The applied method instance, invariants, validity window, evidence pins, and any transport/plane declarations must be auditable as refs/pins.
- **UNM‑L8 (No shadow writers).** When UNM publishes/updates editioned anchors used downstream (e.g., `UNM.TransportRegistryΦ`), other patterns and faces treat them as **ref‑only** (single‑writer discipline; no competing centers of gravity).
- **UNM‑L9 (No publish/telemetry ops).** UNM defines no publish/telemetry step. Any publication/telemetry is out of suite closure and does not mutate UNM semantics (`NCV`, `≡_UNM`, quotient/fix); only Audit pins are produced here.

**AdmissibilityConditions**
Definition (UNM‑Eligibility):
`UNM_Eligibility(NormalizationMethodInstanceSlot, CoordinateValueSlot, CharacteristicSpaceSlot, CNSpecSlot, ContextSlot) → GuardDecision`
where `GuardDecision ∈ {pass | degrade | abstain}` and follows this predicate semantics:
- **pass** iff all of the following hold:
  - (**CN‑frame binding**) the selected `NormalizationMethodInstanceId` is declared in `CN_Spec.normalization.instances` (or an equivalent declared surface), its method kind is included in `CN_Spec.normalization.methods`, and (if present) it satisfies `normalization.admissible_reparameterizations`;
  - (**Target coordinate binding**) the input `CV`’s `slot_id` belongs to the method instance’s declared bound coordinate set;
  - (**Scale‑regime compatibility**) the method kind is compatible with the coordinate’s regime (`ratio:scale | interval:affine | ordinal:monotone | nominal:categorical | tabular:LUT(+uncertainty)`) and preserves the declared `NormalizationInvariant[*]` (from `CN_Spec.normalization.invariants` and/or the method description);
  - (**Validity window**) the method instance’s validity window covers the active slice/time policy (no implicit “latest”);
  - (**Evidence sufficiency when routed into governance**) when `comparability.mode = normalization-based` (or downstream uses `NCV` in gated decisions), the method instance’s evidence pins satisfy `CN_Spec.comparability.minimal_evidence` (structure typically gated by `G.0`; evidence semantics owned by `C.16`).
- **degrade** iff all non‑evidence conditions above hold, but the evidence check does not pass and the declared failure behavior permits producing a policy‑gated degraded `NCV` rather than abstaining.
- **abstain** otherwise (including missing binding, coordinate mismatch, out‑of‑window validity, or evidence failure when the declared failure behavior is abstain).

**Applicability**
UNM is applicable when:
- `CN_Spec.comparability.mode = normalization-based`, or
- a declared downstream step requires “compare-on-invariants” and thus requires explicit normalization.
UNM is typically skipped when `comparability.mode = coordinatewise` (unless an explicit downstream step requires a declared quotient/fix anyway).

**Transport**
- **Bridge-only.** Any cross-context use must be expressed via explicit Bridge pins and recorded in Audit.
- If the describedEntity changes, a KindBridge (`CL^k`) must be declared (two‑bridge rule).
- If transport/plane reuse is invoked, the edition pin key `UNM.TransportRegistryΦ` (aka `UNM.TransportRegistryPhi`) MUST be cited explicitly (in addition to Bridge/CL/ReferencePlane pins); penalties remain R‑lane only.

**Γ_timePolicy**
- Default: `point` (no implicit “latest”).
- If normalization relies on time windows, the validity window is part of the method instance and must be declared.

**PlaneRegime**
- Normalized values live on the episteme ReferencePlane by default.
- Plane crossings require explicit `CL^plane` and are audited; penalties route to `R_eff` only.

**Audit**
Audit records MUST include:
- `CNSpecRef.edition` + `comparability.mode`
- (when present) `CN_Spec.normalization.UNM_id` (the selected UNM mechanism instance id for this CN‑frame)
- chosen `NormalizationMethodInstanceId`, its validity window, and any `NormalizationMethodDescriptionRef.edition`
- declared `NormalizationInvariant[*]` and `NormalizationFixSpec` (if used)
- any declared admissible re‑parameterizations (if present in `CN‑Spec.normalization`)
- all evidence pins (as declared by the instance) and their scope ids
- any Bridge/CL/ReferencePlane pins if transport or plane crossings are invoked, plus the edition pin key `UNM.TransportRegistryΦ/Phi`
- any emitted `FreshnessRequest` / work request identifiers (when applicable; see A.19.UNM:4.5)

#### A.19.UNM:4.2 - CN-frame wiring: `normalization` and comparability routing (normative-by-reference)

**Tell.** CN-frame does not “do normalization”; it **routes** normalization.  
- `comparability.mode ∈ {coordinatewise, normalization-based}` governs whether comparisons are done directly or “normalize-then-compare”.  
- `normalization.UNM_id?` selects the UNM mechanism instance used by this CN-frame.  
- `normalization.methods / instances / method_descriptions / invariants / fix` provide the declared surface that UNM consumes.  
(If present) `normalization.admissible_reparameterizations` constrain which re‑parameterizations count as “admissible” under the declared invariants.  
(See CN-frame definition in `A.19.CN`; `A.19.CN` remains the semantic owner of the CN-frame surface. This section only states the UNM consumption/interpretation constraints and does not introduce a shadow spec.)

#### A.19.UNM:4.3 - Evidence and calibration are owned by MM‑CHR (normative-by-reference)

UNM does not claim “this normalization is legitimate” by decree.  
Instead, legitimacy is routed through evidence carriers and calibration/validity artifacts owned by `C.16 (MM‑CHR)` and referenced from the chosen `NormalizationMethodInstance`.

#### A.19.UNM:4.4 - Didactic rule: quotients or fixes, never “labels” (normative)

When UNM is used to support comparability/acceptance:
- Think in **invariants and equivalence classes** (quotients), not in labels.  
- If a concrete representative is needed, declare a `NormalizationFix` explicitly.  
Do not silently treat an arbitrary representative as canonical.

#### A.19.UNM:4.5 - P2W / TGA integration note (normative-by-reference)

When UNM is used inside transduction flows/graphs (e.g., `E.18 (E.TGA)`):
- UNM occurs **before** selection/decision steps.
- If required measurements are **missing or stale**, UNM does not “guess a number”; it surfaces an explicit **freshness/work request** that must be planned in `U.WorkPlanning` and executed in `U.WorkEnactment`.
- In TGA terms, transport/plane reuse is surfaced as explicit calibration/transport artifacts pinned to `TransportRegistry^Φ` (editioned as `UNM.TransportRegistryΦ`; penalties stay R‑lane only).
- Editioned anchors referenced by faces downstream (e.g., `UNM.TransportRegistryΦ`, and legality anchors when applicable) remain **single‑writer**: downstream consumers cite them as refs and do not re‑author them.

### A.19.UNM:5 - Archetypal Grounding (Tell–Show–Show)

**Tell.** UNM is the conceptual “front gate” that turns “raw coordinate values” into “values comparable under declared invariants”, by:
1) choosing an admissible normalization method instance (with evidence and validity window),  
2) applying it to produce NCVs,  
3) exposing `≡_UNM` and (optionally) quotient/fix structure so downstream mechanisms can remain lawful and explicit.

**Show (System).** A team compares alternatives using `normalization-based` comparability:
- CN-Spec declares:
  - `comparability.mode = normalization-based`
  - `normalization.invariants = {unit-alignment, polarity}`
  - a method instance `M_unitScale` with validity window `VW_2026Q1` and evidence pins.
- UNM applies `M_unitScale` to each coordinate value, producing NCVs.
- CPM compares the NCV-profiles (not raw profiles).
- If evidence pins are missing for a slice, UNM returns `GuardDecision = abstain`, preventing “fake comparability”.

**Show (Episteme).** Quotient thinking:
- Two chart items `x` and `y` are different raw values (different units or reference planes).
- Under a chosen normalization method instance, `x ≡_UNM y` holds.
- Comparability claims are made over `[x]_{≡_UNM}` and `[y]_{≡_UNM}` (equivalence classes).
- If reporting needs a single representative, a declared `NormalizationFix` selects it; otherwise, do not pretend a representative is canonical.

**Show (P2W / TGA).** Missing/stale inputs:
- A selector (or comparator) requires comparability under `normalization-based` mode.
- UNM finds that a required coordinate value is missing/stale for the current slice and the instance validity window.
- UNM returns `GuardDecision = abstain` (fail‑closed) **and** emits a `FreshnessRequest` that must be handled via planned baseline + enactment (UNM does not silently proceed).

### A.19.UNM:6 - Bias‑Annotation

Common cognitive traps around normalization:
- **Normalization-as-truth bias:** treating NCVs as “objective” instead of “objective under declared invariants and validity window”.
- **Hidden-steps bias:** assuming normalization “happened somewhere” and skipping explicit routing/pins.
- **Unit-blindness:** treating numeric sameness as semantic sameness.
- **Proxy legitimacy:** assuming a popular method is legitimate without evidence pins or validity region.

Mitigation: enforce explicit `NormalizationMethodInstance` + validity window + evidence pins; and keep `≡_UNM`/quotient semantics explicit.

### A.19.UNM:7 - Conformance Checklist

- [ ] **Template compliance:** canonical E.8 sections 1–13 present in order; pattern ends with `### A.19.UNM:End`.
- [ ] **Terminology:** uses `NormalizationMethodId`, `NormalizationMethodInstanceId`, `NormalizationMethodDescription(Ref)`, `CV`, `NCV`, `≡_UNM`, `NormalizationInvariant[*]`, `NormalizationFixSpec`; avoids “map” wording (esp. `Map`); κ‑notation is retired.
- [ ] **CN routing:** uses `CN_Spec.comparability.mode` and the `CN_Spec.normalization` surface; does not embed “shadow CN-spec”.
- [ ] **Fail-closed:** eligibility is tri-state and never coerces unknown to pass.
- [ ] **Legality classes declared:** method class is one of `{ratio:scale, interval:affine, ordinal:monotone, nominal:categorical, tabular:LUT(+uncertainty)}` and the instance’s validity window is named.
- [ ] **No indicator conflation:** does not treat NCV as automatically implying indicator status.
- [ ] **Transport discipline:** cross-context/plane reuse is Bridge-only, explicit, audited; penalties route to `R`/`R_eff` only.
- [ ] **Quotient/fix discipline:** if a representative is required, `NormalizationFix` is declared; otherwise quotient semantics remain abstract.
- [ ] **Auditability:** method instance, validity window, evidence pins, and transport/plane policies are recorded as refs/pins.
- [ ] **No shadow writers:** if editioned transport/calibration anchors are used (e.g., `UNM.TransportRegistryΦ`), downstream consumers treat them as ref‑only (single‑writer discipline).
- [ ] **P2W awareness (when used in flows):** missing/stale inputs lead to explicit `FreshnessRequest` emissions (planned via P2W), not silent coercion.
- [ ] **SlotKind discipline:** SlotKind tokens reuse the CHR SlotKind lexicon where applicable; UNM‑specific SlotKinds are docked into the suite lexicon before use (no ad‑hoc drift).
- [ ] **TransportRegistry key discipline:** `UNM.TransportRegistryΦ` (alias `UNM.TransportRegistryPhi`) is referenced as an edition pin key (and audited) / `TransportRegistry^Φ` in TGA terms, not introduced as a new `…Ref` kind.

### A.19.UNM:8 - Common Anti‑Patterns and How to Avoid Them

1) **Hidden normalization inside scoring or selection**  
   Avoid by routing via `CN_Spec.comparability.mode` and explicit UNM use.

2) **“NCV ⇒ indicator” shortcut**  
   Avoid by treating indicatorization as UINDM policy, not a byproduct of normalization.

3) **“We normalized” without declaring invariants**  
   Avoid by naming `NormalizationInvariant[*]` and exposing `≡_UNM`.

4) **Cross-context reuse without transport declaration**  
   Avoid by Bridge-only transport and auditing Bridge/CL/ReferencePlane pins.

5) **Choosing a representative implicitly**  
   Avoid by either keeping quotient objects abstract or declaring `NormalizationFix`.

6) **Using “map/mapping/Map” language as if it were harmless**  
   Avoid by using “normalization / re‑parameterization under invariants” and by keeping `Map` for its specialized FPF meaning.

7) **Treating UNM outputs as globally comparable across contexts/planes**  
   Avoid by Bridge-only transport declarations + audited ReferencePlane/CL pins; otherwise stay context-local and fail‑closed.

8) **Re‑authoring editioned transport/calibration anchors downstream**  
   Avoid by treating `UNM.TransportRegistryΦ` (and similar anchors) as single‑writer artifacts: downstream is ref‑only.

### A.19.UNM:9 - Consequences

**Benefits**
- Makes “normalize-then-compare” a first-class governance choice.
- Centralizes semantic ownership, improving usability and reducing drift.
- Supports evolvability: method families can evolve via packs/extensions without mutating the mechanism surface.
- Prevents silent illegality (unit/scale/plane errors) by fail-closed guards.

**Costs**
- Requires explicit declarations (method instance, invariants, validity window, evidence pins).
- Some workflows must learn quotient/fix thinking (a conceptual overhead).

### A.19.UNM:10 - Rationale

UNM is designed as a **minimal canonical semantic surface**:
- Enough structure to prevent illegal comparisons and hidden transformations.
- Explicit routing in CN-frame so normalization is governance, not an algorithmic trick.
- Evidence/calibration are delegated to MM‑CHR to avoid redefining measurement meaning.
- Bridge-only transport prevents accidental “global normalization” across contexts.

This balances evolvability (methods evolve) with didactic usability (one place to read what UNM is).

### A.19.UNM:11 - SoTA‑Echoing (post‑2015 practice alignment)

UNM does not prescribe algorithms, but it is designed to **host** SoTA normalization families via `NormalizationMethodDescriptionRef` + evidence pins (typically shipped as `G.2` SoTA packs and wired via `GPatternExtension` modules, not as mutations of UNM’s surface). Examples of post‑2015 method families that often appear as evidence-backed normalization candidates (domain-dependent):
- **SoTA ≠ popular.** Method families enter UNM through `G.2` claim structures + edition pins + evidence pins; “widely used” is not a validity claim by itself.
- **Calibration of probabilistic coordinates** (e.g., temperature scaling; multiclass calibration families such as Dirichlet calibration).  
  *Typical citations:* Guo et al., 2017; Kull et al., 2019.
- **Shift-/validity-region-aware normalization** where “validity window/region” is explicit and shift detection enters as *evidence*, not as hidden branching.  
  *Typical citations:* Lipton et al., 2018 (shift estimation); Ovadia et al., 2019 (uncertainty under shift) — as evidence motifs.
- **Order-preserving transforms** for ordinal regimes (normalization constrained to monotone transforms; legality forbids arithmetic).  
  *Typical citations:* modern monotonic modeling toolkits (post‑2017) used as *method families*, not as silent arithmetic.
- **Set-valued / uncertainty-aware normalization outputs** where uncertainty is preserved as a first-class outcome (tri‑state guards + set-valued artifacts, rather than coerced point values).  
  *Typical citations:* conformal-style families (post‑2018+) used as evidence/uncertainty carriers.

SoTA is connected as **wiring** (packs/extensions) while UNM’s surface remains stable.

### A.19.UNM:12 - Relations

**Builds on / cites**
- `E.8` (pattern template)
- `E.20` (single‑owner discipline for mechanism‑intension content)
- `A.15.3` (P2W planned baseline seam, when UNM is used in flows)
- `F.18` (alias docking / token continuity, when renaming or retiring legacy UNM tokens)
- `A.6.1` (U.Mechanism.Intension shape; specialization discipline)
- `A.19.CHR` (CHR suite boundary; slot lexicon; suite protocols)
- `A.19.CN` (CN_Spec normalization + comparability routing)
- `C.16` (MM‑CHR evidence/calibration carriers)
- `G.0` (CG-frame legality gates used downstream)
- `G.2` (SoTA synthesis packs as the method‑family ingress; wiring‑only integration)
- `E.18 (E.TGA)` (when UNM is used in transduction flows/graphs; P2W freshness/work routing)
- `B.3` (congruence/quotient intuition, when referenced)

**Used by**
- CHR suite protocols (normalize stage), when `comparability.mode` requires normalization-based comparability.

### A.19.UNM:End

## A.19.UINDM - Unified Indicatorization Mechanism (UINDM)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A / CN‑Spec cluster (A.19) / CHR mechanism owner patterns (Phase‑3)
> **Source:** FPF / CHR Phase‑3 mechanism owner patterns
> **Modified:** 2026‑01‑19
>
> **Semantic owner note (Phase‑3 canonicalization):** this pattern is the **designated single semantic owner** of the canonical `U.Mechanism.Intension` for `UINDM.IntensionRef` (CHR suite stage `indicatorize`). This matches the “single‑owner route map” discipline: mechanism‑intension semantics live in `A.19.<MechId>.
> `A.6.1` remains the owner of the **template** of `U.Mechanism.Intension`.
>
> **Canonicalization hook (ID‑continuity‑safe):** any other appearances of the UINDM intension (e.g., a legacy grounding stub in `A.6.1` or suite prose in `A.19.CHR`) SHALL be reduced to a **Tell + Cite** stub pointing to **`A.19.UINDM:4.1`**, while preserving the original section headings and their public `PatternId:SectionPath` IDs for continuity (alias‑dock legacy tokens rather than deleting them).
> Such stubs MUST NOT restate SlotIndex / LawSet / Admissibility content (no “second center of gravity” via near‑duplicate prose).

### A.19.UINDM:0 - At a glance (didactic, informative)

* **Suite stage:** `indicatorize` (ordering lives only in `A.19.CHR:suite_protocols`).
* **Inputs (conceptual):** host `U.CharacteristicSpaceRef` + `CNSpecRef` + `IndicatorChoicePolicyRef` + `U.BoundedContextRef`,
  with optional `CGSpecRef` (+ optional `MinimalEvidenceRef` override) when the chosen policy is evidence‑gated.
* **Output:** `IndicatorSetSlot` = a set of `U.CharacteristicRef` (chosen coordinates), not measurements.
* **Non‑goals:** does **not** normalize, score, compare, aggregate, threshold, publish, or emit telemetry; it only selects a subset under explicit policy.
* **P2W seam:** concrete edition/policy pins are bound in planned baseline artefacts (`A.15.3` + `A.19.CHR:4.7.2`); executions only record effective refs/pins in `Audit`.
* **Failure mode:** tri‑state guard (`pass|degrade|abstain`); unknown never coerces to `pass`.
* **Quick rule of thumb:** if `CN‑Spec.indicator_policy` is absent → `IndicatorizeEligibility = abstain` (fail‑closed); if the selected policy is evidence‑gated → `CGSpecRef` MUST be available and the effective MinimalEvidence MUST be explicit (override or `CG‑Spec.MinimalEvidence`).

### A.19.UINDM:1 - Problem frame

FPF’s Characterization (CHR) suite treats indicatorization as a **distinct mechanism boundary** within the CHR suite (authoritative membership: `A.19.CHR:4.2`).
Suite membership is a **set** (order has no semantics); any intended ordering is expressed only via `suite_protocols` (`A.19.CHR:4.5`), under the suite obligations (`A.19.CHR:4.3`).

Within the canonical suite‑closed protocol, UINDM appears as the `indicatorize` stage (after `normalize`, before `score/compare/select`; optional stages remain explicitly optional per `suite_protocols`).

UINDM’s job is concept‑level and contract‑bound: it selects an **indicator subset** over an existing `U.CharacteristicSpace` under `CN‑Spec.indicator_policy`, using the suite‑wide SlotKind lexicon to prevent SlotKind drift across the CHR ladder and across SoTA wiring layers.
A “subspace view” (if needed) is treated as a **derived artefact** from the chosen set (see `A.19.UINDM:4.2`), not as an extra mandatory output of the kernel signature.

### A.19.UINDM:2 - Problem

Engineering teams routinely need to decide “which characteristics count as indicators” for a CN‑frame—before they can score, compare, aggregate, or select. If indicatorization is not given a **first‑class mechanism boundary**, several failure modes emerge:

* **Hidden indicatorization:** downstream mechanisms (scoring/comparison/selection) implicitly decide which characteristics matter, making the CHR pipeline opaque and hard to audit. 
* **NCV conflation:** measurability (or “having an NCV”) is treated as sufficient to be an indicator, collapsing the crucial distinction between “measurable characteristic” and “indicator chosen under policy.” 
* **Drift and non‑determinism:** indicator sets vary between teams and contexts without stable edition pins, making comparisons and decisions irreproducible. 
* **Silent evidence coercion:** missing/unknown evidence is implicitly treated as acceptable (“pass”) or collapsed to an empty set, degrading decision quality without visibility. 

### A.19.UINDM:3 - Forces

1. **Policy primacy vs method freedom.** Indicatorization must be governed by explicit `IndicatorChoicePolicy`, while still allowing multiple method families (e.g., theory‑first, invariance‑driven, evidence‑gated) to be wired later without mutating the mechanism’s signature.

2. **Selection‑only vs “semantic alchemy.”** UINDM must not smuggle normalization, scaling, polarity flips, aggregation, or scoring inside “indicator choice.” It is a selection mechanism over the host basis, not a transformation mechanism. 

3. **Context locality vs cross‑context reuse.** Indicatorization is slice‑bound; cross‑context indicatorization is permitted only when an explicit `Transport` clause (Bridge+CL/ReferencePlane) is present—otherwise implicit crossings destroy semantic precision. 

4. **Auditability vs authoring overhead.** Engineer‑managers need to see *why* an indicator set was chosen and *which editions/policies* were in effect, but FPF stays conceptual (no data governance, no tool‑enforced metadata). Audit obligations must therefore be minimal yet decisive. 

5. **Evolvability vs didactic usability.** CHR mechanisms must remain evolvable (stable slot lexicon; method specifics in SoTA packs / wiring), while the spec must remain teachable: a reader should find UINDM’s purpose, boundary, laws, guard behavior, and audit obligations in one place.

6. **Fail‑closed discipline.** Unknown/insufficient evidence must never be coerced into “pass”; tri‑state guards (`pass|degrade|abstain`) are required to preserve correctness under uncertainty. 

7. **P2W separation and gate/guard separation.** UINDM must expose eligibility and audit pins without turning into (i) a WorkPlanning baseline binder or (ii) a legality gate:
   planned slot fillings belong to P2W artefacts (WorkPlanning), while GateDecision/GateLog live in gate patterns / WorkEnactment (suite protocols remain mechanism‑steps only).

### A.19.UINDM:4 - Solution

UINDM is the **canonical indicatorization mechanism** in the CHR suite. It defines:

* a stable **mechanism boundary** (“indicatorize” is a stage with its own operation and eligibility predicate),
* a stable **SlotKind surface** (via the suite lexicon),
* a strict **selection‑only law set** (no implicit UNM; no unit/scale/polarity changes),
* a **tri‑state admissibility guard** (fail‑closed on missing policy, legality, or evidence), and
* an **audit minimum** (edition pins + crossing policy ids when transport occurs).

UINDM also preserves the CHR suite obligations by construction: it does not embed GateDecision/GateLog, it does not perform publish/telemetry steps, and it keeps Transport declarative (refs/pins only).

Method semantics (“how to pick indicators”) remain out of suite core: they belong in SoTA packs (`G.2`) and wiring‑only extension modules (`GPatternExtension` blocks), while UINDM remains the stable contract surface.

#### A.19.UINDM:4.1 - Mechanism.Intension (normative)

This is the canonical `U.Mechanism.Intension` for `UINDM.IntensionRef` and is intended to be cited by CHR suite artifacts and by any wiring layers.

* **Scope note:** this intension is an **instance** authored to the `U.Mechanism.Intension` shape owned by `A.6.1`. It defines only the mechanism’s semantic surface (slots/ops/laws/guards/audit). It does **not** bind project‑specific pins (P2W), and it does **not** emit GateDecision/GateLog; it emits `Audit` pins and a tri‑state guard only.
* **IntensionHeader:** `id = UINDM`, `version = 1.0.0`, `status = stable`.
* **IntensionRef:** `UINDM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).
* **Tell.** Policy‑bound indicatorization: select an indicator subset over an existing `U.CharacteristicSpace` under `CN‑Spec.indicator_policy`.
* **Purpose:** freeze a policy‑bound indicator subset early so downstream CHR mechanisms can assume a declared indicator profile (or explicitly `degrade/abstain`) rather than silently “choosing indicators” inside scoring/comparison/selection.
* **Imports:** `A.19.CN (CN‑Spec.indicator_policy)`, `A.6.5 (slot discipline)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`, and (when evidence‑gated) `G.0 (CG‑Spec.MinimalEvidence)`.
* **SubjectBlock:**

  * **SubjectKind:** `Indicatorization`.
  * **BaseType:** `U.CharacteristicSpace`.
  * **SliceSet:** `U.ContextSliceSet`.
  * **ExtentRule:** indicatorization ranges over the host basis `CNSpecSlot.cs_basis` (within `CNSpecSlot.chart`) for the active Context slice; it never enlarges the host basis.
  * **ResultKind?:** `U.Set`.
* **SlotIndex** (derived projection from `SlotSpecs` / guard SlotSpecs; uses `A.19.CHR:4.2.1` SlotKind tokens; no independent semantics):

  * `CharacteristicSpaceSlot : ⟨ValueKind = U.CharacteristicSpace, refMode = CharacteristicSpaceRef⟩`,
  * `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`,
  * `IndicatorChoicePolicySlot : ⟨ValueKind = IndicatorChoicePolicy, refMode = IndicatorChoicePolicyRef⟩`,
  * `ContextSlot : ⟨ValueKind = U.BoundedContext, refMode = U.BoundedContextRef⟩`,
  * `CGSpecSlot? : ⟨ValueKind = CG‑Spec, refMode = CGSpecRef⟩` (optional; REQUIRED iff the chosen `IndicatorChoicePolicy` is evidence‑gated),
  * `MinimalEvidenceSlot? : ⟨ValueKind = MinimalEvidence, refMode = MinimalEvidenceRef⟩` (optional override; if evidence‑gated and omitted, the effective MinimalEvidence is `CGSpecSlot.MinimalEvidence`),
  * `IndicatorSetSlot : ⟨ValueKind = U.Set (of U.CharacteristicRef), refMode = ByValue⟩`.
* **OperationAlgebra** (suite stage = `indicatorize`, per `A.19.CHR:4.5`; canonical stage‑op = `Indicatorize`):

  * `Indicatorize(CharacteristicSpaceSlot, CNSpecSlot, IndicatorChoicePolicySlot, ContextSlot, CGSpecSlot?, MinimalEvidenceSlot?) → IndicatorSetSlot`.
* **LawSet** (CHR‑lawful indicatorization):

  1. **Selection‑only:** `Indicatorize` MUST NOT alter units/scales/polarities; it only selects a subset (no implicit `UNM`).
  2. **Host‑basis restriction:** the resulting set MUST be a subset of the declared host basis (as constrained by `CNSpecSlot.cs_basis` / `CNSpecSlot.chart`).
  3. **No implicit NCV⇒indicator:** measurability/NCV is not sufficient; indicators exist only via `IndicatorChoicePolicySlot` (cites `A.19.CN` `indicator_policy`).
  4. **Edition‑determinism (with slice locality):** for fixed editions of all **ByRef** inputs (`CharacteristicSpaceRef`, `CNSpecRef`, `IndicatorChoicePolicyRef`, and—when evidence‑gated—`CGSpecRef` plus optional `MinimalEvidenceRef`) and a fixed active Context slice, the `IndicatorSetSlot` result is stable.
  5. **No silent evidence coercion:** if evidence is insufficient/unknown under the chosen policy, the result MUST NOT be “silently emptied” nor silently treated as “pass”; use tri‑state guards.
* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing legality/evidence):

  * `IndicatorizeEligibility(CharacteristicSpaceSlot, CNSpecSlot, IndicatorChoicePolicySlot, ContextSlot, CGSpecSlot?, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `CNSpecSlot.indicator_policy` is present, (ii) `IndicatorChoicePolicySlot` is consistent with that policy reference (same `…PolicyRef` + edition pins), and (iii) `CharacteristicSpaceSlot` matches the host basis implied by `CNSpecSlot` (within the active chart and Context slice).
  * If the chosen `IndicatorChoicePolicy` is evidence‑gated:
    (i) `CGSpecSlot` MUST be present,
    (ii) define `EffectiveMinimalEvidence := (MinimalEvidenceSlot if present, else CGSpecSlot.MinimalEvidence)`,
    and (iii) insufficient/unknown evidence MUST yield `degrade` or `abstain` per the **effective** failure‑behavior policy (never a silent `pass`).
  * If the chosen `IndicatorChoicePolicy` is **not** evidence‑gated, absence of `MinimalEvidenceSlot` MUST NOT affect eligibility; no accidental “always‑evidence‑gated” behavior is permitted.
* **Applicability:**
  * Intended to be used before any scoring/comparison/selection that assumes an indicator profile, while remaining a distinct step (no hidden indicatorization inside downstream mechanisms).
  * Cross‑context indicatorization is allowed only via an explicit `Transport` clause.
  * Pin‑binding note: choosing concrete policy editions/pins is a planned baseline concern (P2W); UINDM only consumes those refs and records the effective ones in `Audit`.
* **Transport:** declarative Bridge+CL/ReferencePlane only (refs/pins; do not restate CL ladders or Φ tables here); penalties route to **`R_eff` only**.
* **Γ_timePolicy:** `point` by default (no implicit “latest”).
* **PlaneRegime:** values live on the episteme `ReferencePlane` (the `IndicatorSetSlot` is a set of references into the host basis); UINDM does not introduce plane shifts.
  When the indicatorization outcome is used across planes, apply **CL^plane** by explicit policy and route penalties → **`R_eff` only**.
* **Audit:**

  * MUST record: `CharacteristicSpaceRef.edition`, `CNSpecRef.edition`, `IndicatorChoicePolicyRef.edition`.
  * When evidence‑gated, MUST record: `CGSpecRef.edition` and effective MinimalEvidence (`MinimalEvidenceRef` when provided; otherwise `CGSpecSlot.MinimalEvidence`).
  * SHOULD record: the realized `GuardDecision` (`pass|degrade|abstain`) and, when non‑`pass`, the policy‑bound failure behavior reference that justified it.
  * SHOULD record: a stable description of `IndicatorSetSlot` (or an id reference to a **citable** indicator‑set artefact), and any Bridge/CL/ReferencePlane ids when `Transport` was invoked.

#### A.19.UINDM:4.2 - Interpretation notes (informative)

* **IndicatorSet is a set of references, not values.** `IndicatorSetSlot` contains `U.CharacteristicRef` tokens; it does not compute measurements. The move from “chosen indicators” to “measured indicator profile” is performed downstream (e.g., via scoring/comparison), not by UINDM. 

* **Subspace views are derived, not mandatory.** If a project needs an explicit subspace view, treat it as a derived artefact `CS|_S` where `S = IndicatorSetSlot` over the host `CS = CharacteristicSpaceSlot`. Do not add a new mandatory output to the kernel signature; model a first‑class subspace artefact via `⊑⁺` only when it is genuinely needed.

* **Justification is optional and externalized.** The CHR SlotKind lexicon includes `JustificationSlot`, but the canonical UINDM intension does not require it.
  If a project needs a first‑class justification output, treat it as an **extension** (`⊑⁺`) rather than by mutating the base `Indicatorize` signature,
  and model the justification as an episteme artefact (e.g., `JustificationSlot : ⟨ValueKind = U.Episteme, refMode = U.EpistemeRef⟩`).

* **Evidence‑gated indicatorization is explicit.** Evidence gating is *not* default: it is activated only when the chosen `IndicatorChoicePolicy` is evidence‑gated, in which case `CGSpecSlot` and `MinimalEvidenceSlot` become required inputs to avoid “silent passes.” 

### A.19.UINDM:5 - Archetypal Grounding (informative)

#### A.19.UINDM:5.1 - Tell

Think of UINDM as a **policy‑bound projection**:

* Input: “the whole declared characteristic basis of a CN‑frame (in this context slice) + an explicit indicator choice policy”
* Output: “the subset of characteristic references that are allowed to count as indicators for downstream CHR steps”

The key didactic boundary is: **UINDM chooses coordinates; it does not alter coordinates.**

#### A.19.UINDM:5.2 - Show (U.System) — cross‑unit engineering dashboard

A program manager maintains a `U.CharacteristicSpace` for manufacturing sites, including ~30 characteristics (quality, safety, cost, throughput, sustainability).

* The CN‑Spec’s `indicator_policy` for the “weekly executive dashboard” selects a subset:
  `{DefectRate, IncidentRate, UnitCost, LeadTime, EnergyPerUnit, OnTimeDelivery}`.
* UINDM runs `Indicatorize(...)` and outputs `IndicatorSetSlot =` those references.
* One site lacks reliable incident reporting for the last week. The indicator policy is evidence‑gated; `IndicatorizeEligibility` returns `degrade` (not `pass`), and the audit records the effective MinimalEvidence and the edition pins used.

Downstream mechanisms can now be held to the invariant: **they may only score/compare/select using the declared indicator profile (or explicitly abstain/degrade).** This avoids “dashboard drift” where different teams silently score on different subsets.

#### A.19.UINDM:5.3 - Show (U.Episteme) — robust evaluation across environments

A research lead wants indicators for model robustness under distribution shift (different hospitals, sensors, geographies).

* The host characteristic basis includes many candidate metrics (accuracy slices, calibration, subgroup error, OOD detection quality).
* The indicator choice policy is “invariance‑driven”: prefer indicators whose semantics remain stable under environment changes; deprioritize proxy metrics known to be environment‑sensitive.
* UINDM returns an indicator set used by the scoring and comparison stages; uncertain indicators are handled via tri‑state guarding rather than coerced to zero or silently dropped.

### A.19.UINDM:6 - Bias-Annotation (informative)

* **Gov (governance).** Bias toward explicit policy surfaces (`IndicatorChoicePolicyRef`, edition pins, auditable outcomes) rather than tacit “expert choice.” Risk: perceived extra work. Mitigation: keep the mechanism minimal (selection‑only) and push method detail into wiring modules.

* **Arch (architecture).** Bias toward stable interfaces: SlotKind tokens come from the suite lexicon and evidence gates are explicit inputs. Risk: reduced “quick hacks.” Mitigation: allow `⊑⁺` extensions for richer outputs (e.g., justification) without mutating the kernel signature.

* **Onto/Epist.** Bias toward a strict distinction between “measurable characteristic” and “indicator under policy.” Risk: teams accustomed to “everything measurable is an indicator” may resist. Mitigation: embed this as an explicit LawSet clause (“No implicit NCV⇒indicator”). 

* **Prag (pragmatics).** Bias toward fail‑closed guards and traceability under uncertainty. Risk: more `abstain/degrade` outcomes early. Mitigation: couple `degrade` with explicit downstream behaviors (policy‑bound) rather than silent coercions.

* **Did (didactics).** Bias toward “one place to learn the mechanism”: the problem/forces/solution narrative is co‑located with the canonical Mechanism.Intension.

### A.19.UINDM:7 - Conformance Checklist

A UINDM publication / usage is conformant if it satisfies:

1. **Mechanism.Intension completeness.** The mechanism publication includes the full intension shape (header/imports/subject/slot index/op algebra/laws/admissibility/applicability/transport/time/plane/audit), and uses the tri‑state guard form. SlotIndex is treated as a **derived** projection. (See `CC‑UM.0/CC‑UM.1/CC‑UM.9`.) 

2. **SlotKind discipline.** SlotKind tokens match the CHR SlotKind lexicon for the roles used (`CharacteristicSpaceSlot`, `CNSpecSlot`, `IndicatorChoicePolicySlot`, `ContextSlot`, etc.). New SlotKinds, if any, are introduced by first extending the suite lexicon, not ad‑hoc in the mechanism. 

3. **Selection‑only behavior.** `Indicatorize` does not alter units/scales/polarities, does not perform implicit normalization, and does not enlarge the host basis. 

4. **No NCV shortcut.** “Measurable/NCV” is not treated as sufficient for indicatorhood; indicatorhood arises only via `IndicatorChoicePolicySlot` consistent with `CN‑Spec.indicator_policy`. 

5. **Evidence gating is explicit.** When the chosen `IndicatorChoicePolicy` is evidence‑gated, `CGSpecSlot` is present and the effective MinimalEvidence is explicit and auditable
   (`MinimalEvidenceSlot` when provided; otherwise `CGSpecSlot.MinimalEvidence`); insufficient/unknown evidence must yield `degrade/abstain` per the effective failure‑behavior policy, never a silent `pass`.

6. **Cross‑context indicatorization is explicit.** Any cross‑context use names the relevant Bridge/CL/ReferencePlane and routes penalties to `R_eff` only (Bridge‑only transport + R‑only routing). (See `CC‑UM.3/CC‑UM.4`.) 

7. **Gate/guard separation + lexeme discipline.** UINDM uses `…Eligibility` returning `GuardDecision ∈ {pass|degrade|abstain}` and does not embed GateDecision/GateLog in suite steps.
   Reserved gate‑lexemes (e.g., `…Guard`) are not used for mechanism‑level predicates; the mechanism stays at the guard/admissibility layer.

8. **P2W seam is preserved.** Planned slot fillings / edition pin‑bindings are not authored inside this mechanism intension; they are bound in WorkPlanning artefacts (P2W) and surfaced at run‑time only via `Audit` refs/pins.

9. **Specialization discipline (if extended).** Any specialization of UINDM (`⊑/⊑⁺`) MUST follow the multi‑level specialization discipline (`A.6.1:4.2.1`, `CC‑UM.8`): SlotKind invariance for inherited ops, no new mandatory inputs to the inherited `Indicatorize` op, and any extra outputs (e.g., justification/subspace artefacts) expressed only via `⊑⁺`.

### A.19.UINDM:8 - Common Anti‑Patterns and How to Avoid Them

* **“NCV ⇒ indicator.”** Treating all measurable characteristics as indicators. Violates “No implicit NCV⇒indicator.” 

* **Indicatorization hidden in scoring.** A scoring method silently ignores some characteristics or introduces an implicit “feature selection” without an explicit indicator set.

* **Silent emptying.** When evidence is insufficient, returning an empty indicator set (or treating missing evidence as “pass”) without a tri‑state guard decision. 

* **Cross‑context reuse without Transport.** Reusing an indicator set across contexts without naming Bridge/CL/ReferencePlane, thereby hiding penalties and violating crossing visibility. 

* **Smuggling plan‑binding into the mechanism.** Binding concrete edition pins / planned slot fillings (“launch values”) inside the UINDM description instead of using the P2W seam (WorkPlanning) and recording only effective refs/pins in `Audit`.

* **GateDecision leakage.** Emitting or implying GateDecision/GateLog as part of the `indicatorize` step (gate decisions are separated from suite steps; keep UINDM at guard+audit level).

### A.19.UINDM:9 - Consequences

**Benefits**

* Makes “which characteristics count as indicators” explicit, auditable, and policy‑bound.
* Prevents downstream semantic drift by freezing an indicator subset early in the CHR pipeline.
* Improves reproducibility via edition‑determinism (fixed editions ⇒ stable result). 
* Preserves evolvability: new indicator selection method families can be added via wiring (packs/extensions) without changing the mechanism’s intension.

**Costs / trade‑offs**

* Adds an explicit step (and explicit policy work) before scoring/comparison.
* Strict fail‑closed behavior can increase early `degrade/abstain` outcomes until evidence and policies are properly specified.

### A.19.UINDM:10 - Rationale

Indicatorization is separated because it is a different kind of commitment than scoring or comparison:

* Indicatorization commits to **which coordinates are allowed to matter** under policy.
* Scoring/aggregation/comparison commit to **how** allowed coordinates are transformed, folded, or ordered under legality gates.

By making indicatorization selection‑only, UINDM avoids “semantic alchemy” (changing meanings while claiming to merely “pick indicators”) and supports the CHR suite’s broader discipline: explicit contracts, explicit crossings, and explicit handling of uncertainty via tri‑state guards. 

### A.19.UINDM:11 - SoTA-Echoing

**SoTA vs popular note.** This section records alignment to post‑2015 evidence‑backed practice. It is **not** a mandate to use fashionable methods; method semantics stay in SoTA packs (`G.2`) and wiring modules, while this pattern fixes the stable mechanism boundary.

**Pack note (Phase‑3):** this pattern does not currently cite a UINDM‑specific `G.2` SoTA pack/ClaimSheet. If/when such a pack is introduced, replace the bibliographic pointers below with the pack’s `ClaimSheetId` citations, keeping the mechanism semantics unchanged.

#### A.19.UINDM:11.1 - SoTA alignment map (normative)

| SoTA practice pointer (post‑2015+) | Primary source (post‑2015+) | Where it connects to UINDM | Adoption status |
| --- | --- | --- | --- |
| Prefer indicators stable under environment shift (avoid spurious proxies) | IRM / invariant prediction line ([arXiv][1]) | Expressed as **policy freedom** (`IndicatorChoicePolicySlot`) + explicit `Transport` + fail‑closed eligibility; method details stay out of the kernel | Adapt |
| Treat “why these indicators” as a first‑class artefact, not tribal knowledge | Model Cards documentation discipline ([ACM Digital Library][2]) | Expressed as minimal but decisive `Audit` + optional `⊑⁺` justification output (without mutating the kernel signature) | Adapt |
| Keep architectural commitments traceable and single‑owner (avoid “second centers of gravity”) | ISO/IEC/IEEE 42010:2022 “Systems and software engineering — Architecture description” | Expressed as the explicit semantic‑owner hook + “Tell + Cite” stubs elsewhere (no competing semantics) | Adopt |

**Notes per row (SoTA‑Echoing; not method mandates).**
1. *Invariance under shift.* UINDM does not “implement IRM”; it merely makes room for invariance‑driven indicator policies to be wired while keeping the kernel selection‑only.
2. *Justification discipline.* UINDM keeps justification optional at the kernel level; if a justification artefact is required, add it via `⊑⁺` so the base signature stays stable.
3. *Single‑owner traceability.* The ISO architecture‑description discipline is used here only to motivate “one semantic owner + Tell/Cite stubs”; it does not add new Part‑A contract surfaces.

### A.19.UINDM:12 - Relations

* **Builds on**

  * `A.19.CN` (CN‑Spec, specifically `indicator_policy`). 
  * `A.6.1` / `CC‑UM.*` (mechanism intension shape and authoring checks). 
  * `A.19.CHR:4.2.1` (CHR SlotKind lexicon). 
* **Used by**

  * `A.19.CHR` (suite membership and suite protocols; UINDM is the `indicatorize` stage). 
* **Coordinates with**

  * `G.0` (CG‑Spec / MinimalEvidence) when indicator choice is evidence‑gated. 
  * `E.20` (single‑owner discipline) and `F.18` (alias docking) for Phase‑3 canonicalization and ID continuity.
[1]: https://arxiv.org/abs/1907.02893 "Invariant Risk Minimization"
[2]: https://dl.acm.org/doi/10.1145/3287560.3287596 "Model Cards for Model Reporting"

### A.19.UINDM:End

## A.19.USCM - Unified Scoring Mechanism, USCM

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A / CN‑Spec cluster (A.19) / CHR mechanism owner patterns (Phase‑3)
> **Source:** FPF / CHR Phase‑3 mechanism owner patterns
> **Modified:** 2026‑01‑20
>
> **Semantic owner note, Phase‑3 canonicalization:** this pattern is the **designated single semantic owner** of the canonical `U.Mechanism.Intension` for `USCM.IntensionRef` (CHR suite stage `score`). This matches the single‑owner discipline: mechanism‑intension semantics of characterisation mechanisms live in an explicitly designated mechanism‑owner pattern (`E.20`).
> `A.6.1` remains the owner of the **template** of `U.Mechanism.Intension`; this pattern owns the **USCM‑specific** slots, operations, laws, admissibility, applicability, transport, plane, and audit obligations for that template (single‑owner at the instance‑semantics level).
>
> **Canonicalization hook, ID‑continuity‑safe:** any other appearances of the USCM intension (e.g., a legacy grounding stub in `A.6.1` or suite prose in `A.19.CHR`) SHALL be reduced to a **Tell + Cite** stub pointing to **`A.19.USCM:4.1`**, while preserving the original section headings and their public `PatternId:SectionPath` IDs for continuity (alias‑dock legacy tokens rather than deleting them).
> Such stubs MUST NOT restate SlotIndex, OperationAlgebra, LawSet, Admissibility, or Audit content (no “second center of gravity” via near‑duplicate prose).

### A.19.USCM:0 - At a glance — didactic, informative

* **Suite stage:** `score` (ordering lives only in `A.19.CHR:4.5` / `suite_protocols`; suite membership is a set in `A.19.CHR:4.2`).
* **Inputs, conceptual:** an admitted measure profile (`InputProfileSlot`) + `CNSpecRef` + `CGSpecRef` + `ScoringMethodDescriptionRef` + active `U.BoundedContextRef`, with optional `MinimalEvidenceRef` override.
* **Output:** `ScoreProfileSlot` = a set of score measures (vector scores are first‑class; a scalar score is allowed only if explicitly declared).
* **Non‑goals:** does **not** normalize (UNM), aggregate (ULSAM), compare (CPM), select (SelectorMechanism), threshold, publish, or emit telemetry; it is a scoring step with explicit legality and evidence surfaces.
* **P2W seam:** concrete edition/policy pin bindings (including `ScoringMethodDescriptionRef@edition(…)` when USCM is used) are chosen in planned baseline artefacts (`A.15.3` + `A.19.CHR:4.7.2`); executions only record effective refs/pins in `Audit`.
* **Failure mode:** tri‑state guard (`pass|degrade|abstain`); unknown never coerces to `pass`, and MUST NOT be coerced to `0/false`.
* **Quick rule of thumb:** if `CGSpecSlot.SCP` is missing → `ScoreEligibility = abstain` (fail‑closed); if `ScoringMethodDescriptionSlot` is missing → `ScoreEligibility = abstain` (no implicit scoring method); if `CN‑Spec.comparability` requires normalization‑based comparability → normalization MUST be explicit in choreography (Uses/pins), never hidden inside `Score`.

### A.19.USCM:1 - Problem frame

FPF’s Characterization (CHR) suite treats scoring as a **distinct mechanism boundary** within the CHR suite (authoritative membership: `A.19.CHR:4.2`). Suite membership is a **set** (order has no semantics); any intended ordering is expressed only via `suite_protocols` (`A.19.CHR:4.5`), under the suite obligations (`A.19.CHR:4.3`).

Within the canonical suite‑closed protocol, USCM appears as the `score` stage (after `normalize` and `indicatorize`, before comparison and selection). USCM’s surface is legality‑first: it produces **score measures** from admitted profiles while remaining constrained by the legality gate (`CG‑Spec.SCP`) and by scale‑lawfulness (CSLC).

USCM exists to keep a strict distinction between:

* **normalization** (UNM),
* **indicatorization** (UINDM),
* **scoring** (USCM),
* **aggregation/folding** (ULSAM), and
* **comparison/ordering/selection** (CPM + SelectorMechanism),

so that each commitment has a single place to live, can be audited, and can evolve without smuggling extra semantics into adjacent steps.

### A.19.USCM:2 - Problem

Engineering teams often need to convert an admitted (indicator or NCV) profile into one or more **score measures** for downstream comparison and selection. If scoring is not given a **first‑class mechanism boundary** with explicit legality and evidence surfaces, the following failure modes are common:

* **Illicit arithmetic by convenience:** teams apply weighted sums, averages, or nonlinear transforms across mixed scale kinds without an explicit legality profile, creating scores that are not CSLC‑lawful.
* **Hidden normalization:** scoring implementations silently normalize, align, or flip polarities, collapsing the distinction between “normalize” and “score” and making downstream reasoning non‑reproducible.
* **Silent scalarization:** multi‑criteria realities (vector scores, partial‑order comparability) are reduced to a single scalar via hidden tie‑breakers, producing an apparent total order that is not justified.
* **Unknown coercion:** missing or insufficient evidence is coerced into `0/false` or treated as “good enough,” yielding scores that look precise while being epistemically unsafe.
* **Drift and non‑auditability:** different teams score “the same thing” differently because legality constraints and effective policies (editions, evidence rules, crossings) are not explicit and not recorded.

### A.19.USCM:3 - Forces

1. **Legality discipline vs operational pressure.** Scoring is where “just compute a number” pressure is strongest, but legality must remain explicit and checkable: SCP and CSLC constraints must bound permissible transforms.

2. **Method diversity vs stable contract surface.** Scoring methods evolve rapidly; USCM’s signature must remain stable so method families can be wired through SoTA packs and extensions without mutating the mechanism boundary.

3. **Vector reality vs scalar simplicity.** Many situations require multiple score dimensions. A single scalar score may be convenient but must be an explicit, declared commitment, not a hidden reduction.

4. **Uncertainty vs decisiveness.** Teams need decisions under uncertainty; the framework must prevent epistemic overconfidence. Tri‑state admissibility guards preserve correctness without forcing silent coercions.

5. **Strict distinction across CHR steps.** USCM must not absorb UNM, ULSAM, or CPM semantics “for convenience,” or the suite becomes opaque and non‑teachable.

6. **Evolvability vs didactic usability.** Interfaces must remain evolvable (stable SlotKind surface; method semantics externalized), while the spec remains teachable: a reader must find USCM’s purpose, boundary, laws, guard behavior, and audit minimum in one place.

7. **P2W separation and gate/guard separation.** Planned baseline binding (editions/policy ids) belongs to WorkPlanning artefacts; gate decisions and logs live in gate patterns / WorkEnactment. USCM must expose eligibility + audit pins without turning into a gate or a planner.

### A.19.USCM:4 - Solution

USCM is the **canonical scoring mechanism** in the CHR suite. It defines:

* a stable **mechanism boundary** (`score` is its own stage with a canonical `Score` operation and a tri‑state eligibility predicate),
* a stable **SlotKind surface** (via the suite lexicon),
* a legality‑first **LawSet** anchored in `CG‑Spec.SCP` and CSLC,
* an explicit **anti‑smuggling rule** (no implicit normalization), and
* an **audit minimum** (edition pins and effective evidence policy, plus crossings when transport occurs).

USCM preserves the suite obligations by construction: it does not embed GateDecision/GateLog, it does not perform publish/telemetry steps, and it keeps Transport declarative (refs/pins only) with penalties routed to `R_eff` only.

Method semantics (“how to score”) remain out of suite core: they belong in SoTA packs (`G.2`) and wiring‑only extension modules (`GPatternExtension` blocks), while USCM remains the stable conceptual contract surface.

#### A.19.USCM:4.1 - Mechanism.Intension

This is the canonical `U.Mechanism.Intension` for `USCM.IntensionRef` and is intended to be cited by CHR suite artifacts and by any wiring layers.

* **Scope note:** this intension is an **instance** authored to the `U.Mechanism.Intension` shape owned by `A.6.1`. It defines only the mechanism’s semantic surface (slots/ops/laws/guards/audit). It does **not** bind project‑specific pins (P2W), and it does **not** emit GateDecision/GateLog; it emits `Audit` pins and a tri‑state guard only.

* **IntensionHeader:** `id = USCM`, `version = 1.0.0`, `status = stable`.

* **IntensionRef:** `USCM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).

* **SignatureManifest (optional; importability):** if a USCM publication is intended to be imported/reused, it SHOULD publish a `SignatureManifest` (A.6.0 / A.6.1; `CC‑A.6.0‑18`, `CC‑UM.1`) consistent with `IntensionHeader`/`Imports`, explicitly exposing the stable SlotKind surface (including `ScoringMethodDescriptionSlot`) and any declared scalarization commitment.

* **Tell.** **SCP‑first** scoring: produce score measures from admitted profiles without violating CSLC / scale legality.

* **Purpose:** **SCP‑first** scoring: produce score measures from admitted profiles without violating CSLC / scale legality.

* **Imports:** `G.0 (CG‑Spec.SCP, CG‑Spec.MinimalEvidence)`, `A.18 (CSLC)`, `C.16 (ScoringMethod disclosure + polarity/monotonicity discipline)`, `A.19.CN (comparability.mode + normalization routing)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **SubjectBlock:**

  * **SubjectKind:** `Scoring`.
  * **BaseType:** `U.Measure`.
  * **SliceSet:** `U.ContextSliceSet`.
  * **ExtentRule:** scoring ranges over admitted (indicator/NCV) profiles in the active context slice, routed by `CN‑Spec.comparability` and legality‑gated by `CG‑Spec.SCP`.
  * **ResultKind?:** `U.Set` (of `U.Measure`).

* **SlotIndex** (derived projection from `SlotSpecs` / guard SlotSpecs; uses `A.19.CHR:4.2.1` SlotKind tokens where applicable; any new SlotKind tokens introduced here MUST be suite‑docked into the lexicon by the suite owner to avoid drift):

  * `InputProfileSlot : ⟨ValueKind = U.Set (of U.Measure), refMode = ByValue⟩`,
  * `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`,
  * `CGSpecSlot : ⟨ValueKind = CG‑Spec, refMode = CGSpecRef⟩`,
  * `ScoringMethodDescriptionSlot : ⟨ValueKind = ScoringMethodDescription, refMode = ScoringMethodDescriptionRef⟩` (SlotKind token; when reproducibility matters it is edition‑pinned via the P2W baseline; if the suite lexicon does not yet contain this token, it SHALL be docked into the lexicon by the suite owner rather than introduced ad‑hoc),
  * `ContextSlot : ⟨ValueKind = U.BoundedContext, refMode = U.BoundedContextRef⟩`,
  * `MinimalEvidenceSlot? : ⟨ValueKind = MinimalEvidence, refMode = MinimalEvidenceRef⟩` (optional override; otherwise cite `CGSpecSlot.MinimalEvidence`),
  * `ScoreProfileSlot : ⟨ValueKind = U.Set (of U.Measure), refMode = ByValue⟩`.

* **OperationAlgebra** (suite stage = `score`, per `A.19.CHR:4.5`; canonical stage‑op = `Score`):

  * `Score(InputProfileSlot, CNSpecSlot, CGSpecSlot, ScoringMethodDescriptionSlot, ContextSlot, MinimalEvidenceSlot?) → ScoreProfileSlot`.

* **LawSet** (minimum; legality‑first, no hidden scalarization):

  1. **SCP+CSLC legality:** any numeric transform used to produce `ScoreProfileSlot` MUST be admissible under `CGSpecSlot.SCP` and CSLC‑lawful (cites `G.0` + `A.18`).
  2. **ScoringMethod is explicit (no hidden defaults):** `Score` MUST cite `ScoringMethodDescriptionSlot` (edition‑pinned via P2W when reproducibility matters; see `A.19.CHR:4.7.2`). If a score is issued, the scoring method **𝒢** (Coordinate→Score) MUST be disclosed as required by `C.16` (bounded codomain; monotonicity consistent with template polarity). USCM MUST NOT rely on an implicit “default scoring method”.
  3. **No implicit normalization:** `Score` MUST NOT silently perform UNM; if `CNSpecSlot.comparability` requires normalization‑based comparability, the normalization step MUST be explicit in choreography (Uses/pins), not hidden in `Score`.
  4. **Vector scores allowed; scalarization must be explicit:** producing a single scalar score is allowed only if explicitly declared (e.g., by fixing `ScoreProfileSlot` cardinality to 1 and citing the lawful transform); partial‑order semantics MUST NOT be silently reduced to a scalar “tie‑breaker”.
  5. **Unknown is not coerced:** unknown / insufficient evidence MUST NOT be mapped to `0`/`false`; use tri‑state guards and explicit failure behavior.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing legality/evidence):

  * `ScoreEligibility(InputProfileSlot, CNSpecSlot, CGSpecSlot, ScoringMethodDescriptionSlot, ContextSlot, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `CGSpecSlot.SCP` is present, (ii) `ScoringMethodDescriptionSlot` is present (no implicit scoring method), (iii) evidence passes `MinimalEvidenceSlot?` or `CGSpecSlot.MinimalEvidence`, and (iv) `CN‑Spec.comparability` routing is satisfied (incl. explicit UNM when needed).
  * If `MinimalEvidenceSlot` is absent, the guard MUST evaluate evidence against `CGSpecSlot.MinimalEvidence` (by explicit rule), and MUST NOT return `pass` when evidence is missing/unknown.
  * If `ScoringMethodDescriptionSlot` is missing or unpinned/ambiguous under the active planned baseline, the guard MUST return `abstain` (fail‑closed), not “assume a default”.

* **Applicability:**

  * Intended to be used after indicatorization (when indicator profiles are used) and before comparison/selection.
  * Applicable only when legality/evidence surfaces are present via `CGSpecSlot` (fail‑closed otherwise).
  * Applicable only when a scoring method is explicitly declared via `ScoringMethodDescriptionSlot` (edition‑pinned when reproducibility matters). A “do nothing / identity scoring” intent (if ever needed) MUST still be declared as an explicit scoring method description, not as an implicit default.

* **Transport:** Bridge+CL/ReferencePlane only; penalties route to **`R_eff` only**.

* **Γ_timePolicy:** `point` by default (no implicit “latest”).

* **PlaneRegime:** values live on **episteme ReferencePlane**; on plane crossings apply **CL^plane** policy; penalties → **`R_eff` only**.

* **Audit:**

  * MUST record: `CNSpecRef.edition`, `CGSpecRef.edition`, `ScoringMethodDescriptionRef.edition`.
  * MUST record the **effective evidence policy**:
    * if `MinimalEvidenceSlot?` is present → record `MinimalEvidenceRef` as effective;
    * otherwise → cite `CGSpecSlot.MinimalEvidence` as effective.
  * SHOULD record the realized `GuardDecision` for `ScoreEligibility`, and (when `degrade`/`abstain`) the referenced failure behavior / downstream handling policy id (e.g., SoS‑LOG branch id) when such a policy is in scope.
  * SHOULD record: a stable description of `ScoreProfileSlot`, any Bridge/CL/ReferencePlane ids when `Transport` was invoked, and (when normalization‑based comparability was required) an explicit ref/pin that the upstream UNM step was applied (no provenance gaps for “normalized input” claims).

#### A.19.USCM:4.2 - Interpretation notes — informative

* **A score profile is a set of measures.** `ScoreProfileSlot` is a `U.Set (of U.Measure)`. Treat this as “vector scoring by default.” If a project truly needs a single scalar score, declare that explicitly (per LawSet item 3), rather than assuming scalarity.
* **A score profile is a set of measures.** `ScoreProfileSlot` is a `U.Set (of U.Measure)`. Treat this as “vector scoring by default.” If a project truly needs a single scalar score, declare that explicitly (per LawSet item 4), rather than assuming scalarity.

* **USCM does not order; it scores.** USCM produces score measures. Any ordering, dominance, or set‑valued comparison is performed by CPM and SelectorMechanism (and any optional aggregation is made explicit via ULSAM). Treating the score as “the decision” is a category error in CHR terms.

* **ScoringMethod is explicit (no hidden defaults).** USCM requires `ScoringMethodDescriptionSlot`: the scoring method is a first‑class, auditable choice (typically pinned in planned baseline). This keeps “how we score” evolvable (wired via method packs) without making it implicit or accidental.

* **No implicit UNM is a boundary guard.** This discourages convenience implementations that “just normalize inside scoring.” USCM forbids that: if comparability requires normalization‑based routing, the UNM step is explicit in choreography (Uses/pins) and visible in audit surfaces.

* **Evidence policy is explicit and auditable.** `MinimalEvidenceSlot?` is an optional override; otherwise the effective policy is `CGSpecSlot.MinimalEvidence`. Failures do not disappear; they must show up as `degrade/abstain` and be traceable.

* **Crossings are declarative and penalize `R_eff` only.** When scoring spans contexts or planes, USCM names Bridge+CL/ReferencePlane policies and routes penalties to `R_eff` only, keeping correctness separate from convenience.

### A.19.USCM:5 - Archetypal Grounding — informative

#### A.19.USCM:5.1 - Tell

Think of USCM as **legality‑gated scoring**:

* Input: “an admitted profile of measures, in this context slice, plus CN/CG contract surfaces”
* Output: “a set of score measures that downstream steps may compare/select on”

The key didactic boundary is: **USCM is allowed to transform measures only within the legality surface (SCP+CSLC), and it must not hide normalization, aggregation, or ordering.**

#### A.19.USCM:5.2 - Show — U.System

A program manager evaluates competing rollout plans for a product launch.

* The admitted profile includes measures like `{Cost, LeadTime, Reliability, RiskExposure, CarbonPerUnit}`.
* The CG‑Spec’s `SCP` admits only scale‑lawful transforms (e.g., monotone transforms on ratio/interval measures, explicit unit alignment rules, and prohibited operations on ordinal measures).
* USCM runs `Score(...)` and outputs a score profile such as `{UtilityScore, RiskScore}` rather than forcing a single number.
* A plan lacks sufficient evidence for `RiskExposure` in this context slice; `ScoreEligibility` returns `degrade`, and the audit records the effective MinimalEvidence policy and the editions of `CNSpecRef` and `CGSpecRef`.

Downstream steps can now compare and select with an explicit audit trail, instead of pretending that “the score was objective.”

#### A.19.USCM:5.3 - Show — U.Episteme

A research lead compares several model families for deployment across heterogeneous environments.

* Indicators include calibration and robustness metrics; scoring is done using a calibrated probabilistic score plus uncertainty‑aware score dimensions.
* A post‑2015 practice example is to keep monotonicity and interpretability constraints explicit (e.g., monotone additive models or monotone deep lattice style models) and to treat uncertainty as first‑class (e.g., conformal set‑valued scoring that yields intervals rather than point scores).
* USCM produces a score profile that can remain vector‑valued and uncertainty‑aware, and it refuses to coerce “unknown” into a point score. Comparisons and selections occur downstream using set‑valued semantics where appropriate.

### A.19.USCM:6 - Bias-Annotation — informative

* **Gov (governance).** Bias toward explicit legality and evidence surfaces (`CGSpecRef`, `SCP`, `MinimalEvidence`) rather than “standard practice” arithmetic. Risk: perceived overhead. Mitigation: keep the kernel signature small and push method specifics into SoTA packs and wiring modules.

* **Arch (architecture).** Bias toward stable interfaces and strict step boundaries (no implicit UNM; no hidden scalarization). Risk: reduced room for ad‑hoc shortcuts. Mitigation: allow richer scoring method families via wiring, without mutating the USCM intension.

* **Onto/Epist.** Bias toward treating scores as measures with declared semantics, not as “the truth.” Risk: teams accustomed to one‑number rankings may resist. Mitigation: treat scalarization as an explicit, auditable commitment, not as the default.

* **Prag (pragmatics).** Bias toward fail‑closed guards and traceability under uncertainty. Risk: more `degrade/abstain` outcomes early. Mitigation: couple `degrade` with explicit downstream behavior policies, rather than silent coercion.

* **Did (didactics).** Bias toward “one place to learn the mechanism”: the problem/forces/solution narrative is co‑located with the canonical Mechanism.Intension.

### A.19.USCM:7 - Conformance Checklist

A USCM publication / usage is conformant if it satisfies:

1. **Mechanism.Intension completeness.** The publication includes the full intension shape (header/imports/subject/slot index/op algebra/laws/admissibility/applicability/transport/time/plane/audit), and uses the tri‑state guard form. SlotIndex is treated as a **derived** projection. (See `CC‑UM.*`.)

2. **SlotKind discipline.** SlotKind tokens match the CHR SlotKind lexicon for the roles used (`InputProfileSlot`, `CNSpecSlot`, `CGSpecSlot`, `ContextSlot`, `MinimalEvidenceSlot`, `ScoringMethodDescriptionSlot`, `ScoreProfileSlot`). If `ScoringMethodDescriptionSlot` (or any other required token) is missing from the suite lexicon, it SHALL be suite‑docked there (alias docking acceptable) rather than introduced ad‑hoc in the mechanism.

3. **SCP+CSLC legality is enforced.** Any numeric transform used to produce score measures is admissible under `CGSpecSlot.SCP` and CSLC‑lawful; illicit operations (especially “convenient arithmetic” over non‑lawful scales) are excluded.

4. **ScoringMethod is explicit and auditable.** `Score` cites `ScoringMethodDescriptionSlot` (edition‑pinned when reproducibility matters). No implicit “default scoring method” is assumed. The disclosed method respects polarity/monotonicity discipline (cf. `C.16`).

5. **No implicit normalization.** `Score` does not silently perform UNM. If `CN‑Spec.comparability` requires normalization‑based routing, the normalization step is explicit in choreography (Uses/pins) and auditable.

6. **No hidden scalarization.** Vector scores are permitted. A scalar score is produced only when explicitly declared, and partial‑order semantics are not reduced to a scalar tie‑breaker.

7. **Unknown and evidence handling is explicit.** Unknown / insufficient evidence is not coerced to `0/false`. Eligibility uses `GuardDecision ∈ {pass|degrade|abstain}` and evaluates evidence against the effective policy (`MinimalEvidenceSlot` override or `CGSpecSlot.MinimalEvidence`).

8. **P2W seam is preserved.** Planned slot fillings / edition pin bindings are not authored inside the mechanism intension; they are bound in WorkPlanning artefacts (P2W) and surfaced at run‑time only via `Audit` refs/pins.

9. **Transport and plane discipline.** Cross‑context and cross‑plane use is declarative (Bridge+CL/ReferencePlane; `CL^plane` for plane crossings) and routes penalties to `R_eff` only. Audit records crossings when invoked.

10. **Specialization discipline, if extended.** Any specialization of USCM (`⊑/⊑⁺`) follows the multi‑level specialization discipline (`A.6.1:4.2.1`, `CC‑UM.8`): SlotKind invariance for inherited ops, no new mandatory inputs to the inherited `Score` op, and any extra outputs or ops expressed only via `⊑⁺`.

### A.19.USCM:8 - Common Anti‑Patterns and How to Avoid Them

* **Hidden normalization inside scoring.** Scoring silently normalizes or aligns measures. Avoid by making UNM explicit in choreography and keeping USCM’s `Score` legality‑only.

* **Weighted sum across mixed or non‑lawful scales.** Treating “weights + sum” as universal. Avoid by requiring SCP+CSLC admissibility; if it’s not lawful, it’s not admissible.

* **Silent scalarization.** Collapsing vector scores or partial orders into a single “overall score” via an untracked tie‑breaker. Avoid by leaving vector scores intact, and making scalarization an explicit declared commitment.

* **Implicit scoring method (“we just use the standard formula”).** The scoring method is assumed rather than declared and pinned. Avoid by requiring `ScoringMethodDescriptionSlot` and edition pinning in planned baseline; treat “identity scoring” (if ever needed) as an explicit method description, not a hidden default.

* **Unknown → 0 coercion.** Treating missing evidence as zero, false, or “good enough.” Avoid by tri‑state guards and explicit failure behavior, with auditable effective evidence policy.

* **Shadow CG‑Spec.** Hard‑coding legality rules inside a scoring method description instead of citing `CGSpecSlot.SCP`. Avoid by keeping legality in CG‑Spec and treating method details as wiring.

* **Telemetry or publish leakage.** Treating scoring as a reporting step. Avoid by keeping publish/telemetry outside suite closure (e.g., routed via appropriate post‑suite mechanisms).

* **SlotKind drift.** Renaming or re‑purposing slots across specializations or across mechanisms. Avoid by using the suite SlotKind lexicon and the `⊑/⊑⁺` discipline.

### A.19.USCM:9 - Consequences

**Benefits**

* Makes scoring a first‑class, legality‑gated CHR step, reducing illicit arithmetic and silent assumptions.
* Improves auditability and reproducibility via explicit edition pins and explicit evidence policy selection (override vs default).
* Preserves evolvability: scoring method families can change via SoTA wiring without changing the USCM intension.
* Supports correctness under uncertainty via tri‑state guards and explicit unknown handling.

**Costs / trade‑offs**

* Requires explicit CG‑Spec legality surfaces (SCP) and explicit evidence policies to achieve `pass`; this can feel slower than “just compute a score.”
* Vector scores can be less immediately comfortable than a single number; downstream comparison/selection must be explicit about how vector scores are used.

### A.19.USCM:10 - Rationale

Scoring is a frequent source of semantic precision loss: it is easy to smuggle normalization, illegal arithmetic, implicit thresholds, and uncertainty coercion into “a simple scoring function.” USCM prevents that by forcing a clean boundary:

* **Legality first:** all transforms are justified by `CG‑Spec.SCP` and CSLC.
* **No hidden steps:** normalization is explicit (UNM), aggregation is explicit (ULSAM), ordering is explicit (CPM/SelectorMechanism).
* **Uncertainty is visible:** admissibility is tri‑state; unknown is not coerced.
* **Audit is minimal yet decisive:** effective editions and effective evidence policy are always traceable.

This increases both evolvability (stable interface, externalized method semantics) and didactic usability (a single place to learn USCM’s boundary and obligations).

### A.19.USCM:11 - SoTA-Echoing

**SoTA vs popular note.** This section records alignment to post‑2015 evidence‑backed practice. It is **not** a mandate to use fashionable methods; method semantics stay in SoTA packs (`G.2`) and wiring modules, while this pattern fixes the stable mechanism boundary.

**Pack note, Phase‑3:** this pattern does not currently cite a USCM‑specific `G.2` SoTA pack or ClaimSheet. If/when such a pack is introduced, `ScoringMethodDescriptionSlot` SHOULD be wired to `ScoringMethodDescriptionRef(ed=…)` entries owned by that pack’s ClaimSheets, keeping the USCM mechanism semantics unchanged.

#### A.19.USCM:11.1 - SoTA alignment map

| SoTA practice pointer, post‑2015+                                             | Primary source examples, post‑2015+                                                                                                               | Where it connects to USCM                                                                                                                                        | Adoption status |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Prefer monotone and interpretable scoring surfaces where appropriate          | Explainable additive and monotone model lines, e.g., Lou et al. 2016; Nori et al. 2019; monotone deep lattice style models, e.g., You et al. 2017 | Expressed as **legality‑bounded transform freedom** via `CGSpecSlot.SCP` and explicit scalarization rules; method details stay out of the kernel                 | Adapt           |
| Treat probabilistic scores as measures requiring calibration, not raw outputs | Calibration practice, e.g., temperature scaling (Guo et al. 2017) and successors                                                                  | Expressed as “score is a measure on an explicit scale,” bounded by SCP+CSLC and evidence gating; calibration itself is wired as method semantics, not kernel law | Adapt           |
| Keep uncertainty explicit and allow set‑valued scoring when appropriate       | Modern conformal prediction practice, e.g., Romano et al. 2019; Barber et al. 2021                                                                | Expressed as “vector scores allowed; unknown not coerced; no hidden scalarization,” enabling downstream set‑valued comparison/selection                          | Adapt           |
| Keep architectural commitments traceable and single‑owner                     | ISO/IEC/IEEE 42010:2022 architecture description discipline                                                                                       | Expressed as explicit semantic ownership and Tell+Cite stubs elsewhere (no competing semantics)                                                                  | Adopt           |

**Notes per row**

1. USCM does not “implement a particular scoring model”; it preserves a stable, legality‑gated surface on which such models can be wired.
2. Calibration is treated as a lawful transform family that must live within SCP+CSLC; the kernel does not mandate a specific calibration method.
3. Set‑valued scoring aligns with USCM’s “vector first, scalar by declaration” law, and is naturally consumed by CPM/SelectorMechanism without forcing a spurious total order.
4. Single‑owner traceability is used here to keep the spec teachable and non‑duplicative; it does not add new contract surfaces.

### A.19.USCM:12 - Relations

* **Builds on**

  * `A.6.1` / `CC‑UM.*` (mechanism intension shape and authoring checks).
  * `A.19.CHR:4.2.1` (CHR SlotKind lexicon).
  * `G.0` (CG‑Spec, specifically `SCP` and `MinimalEvidence`).
  * `A.18` (CSLC legality discipline).
  * `C.16` (ScoringMethod disclosure; polarity/monotonicity discipline for score mappings).
  * `A.15.3` + `A.19.CHR:4.7.2` (P2W planned baseline seam for edition/policy pin bindings; cited as seam, not duplicated in Intension).
  * `A.19.CN` (CN‑Spec, specifically `comparability` routing and normalization‑based comparability expectations).
* **Used by**

  * `A.19.CHR` (suite membership and suite protocols; USCM is the `score` stage).
  * Downstream CHR stages that require score measures as inputs (e.g., `CPM`, `SelectorMechanism`).
  * `E.18 (E.TGA)` when USCM instances are used as transduction nodes; the selected `ScoringMethodDescriptionRef@edition(…)` and other pins live in planned baselines (P2W), while executions surface effective refs/pins via `Audit`.
* **Coordinates with**

  * `UNM` when `CN‑Spec.comparability` requires normalization‑based comparability (explicit choreography, no hidden UNM).
  * `ULSAM` when folding/aggregation is needed as a distinct, explicit step.
  * `G.2` and `GPatternExtension` wiring modules for post‑2015 method families, without mutating the USCM kernel.
  * `E.20` (single‑owner discipline) and `F.18` (alias docking) for Phase‑3 canonicalization and ID continuity.

### A.19.USCM:End

## A.19.ULSAM - Unified Lawful Scale Aggregation Mechanism (ULSAM)

> **Type:** Architectural (A)  
> **Status:** Stable  
> **Normativity:** Normative (unless explicitly marked informative)  
> **Placement:** Part A / CN‑Spec cluster (A.19) / CHR mechanism owner patterns (Phase‑3)  
> **Source:** FPF / CHR Phase‑3 mechanism owner patterns  
> **Modified:** 2026-01-20

**Semantic owner note (Phase‑3 canonicalization):** this pattern is the **designated single semantic owner** of the canonical `U.Mechanism.Intension` for `ULSAM.IntensionRef` (CHR suite stage `fold_Γ?`). This matches the “single‑owner route map” discipline: mechanism‑intension semantics live either in an explicitly designated mechanism‑owner pattern (`E.20`).
`A.6.1` remains the owner of the **template** of `U.Mechanism.Intension` and the `U.MechAuthoring` discipline; this pattern owns the **ULSAM‑specific** slots/ops/laws/admissibility/audit obligations for that template (single‑owner at the instance‑semantics level).

**ID continuity note.** When migrating away from any legacy “card location”, preserve public anchors: keep the legacy section heading/ID as a **Tell + Cite stub** (or dock aliases via `F.18`) rather than deleting or silently renaming it.

**Canonicalization hook (ID‑continuity‑safe):** any other appearances of ULSAM intension content (e.g., a legacy grounding stub in `A.6.1` or suite prose in `A.19.CHR`) SHALL be reduced to a **Tell + Cite** stub pointing to **`A.19.ULSAM:4.1`**, while preserving the original section headings and their public `PatternId:SectionPath` IDs for continuity (alias‑dock legacy tokens rather than deleting them).
Such stubs MUST NOT restate SlotIndex / OperationAlgebra / LawSet / Admissibility content (no “second center of gravity” via near‑duplicate prose).
* **ID‑continuity‑safe:** if content is moved from an earlier location, preserve the earlier heading and its IDs as a stub that cites `A.19.ULSAM:4.1`.
* **Alias‑dock, don’t break:** if any legacy tokens exist, dock them via `F.18` + E.10 rules; do not silently replace tokens “by смысл”.
* **No shadow semantics:** derived summaries MAY be informative, but MUST NOT restate SlotIndex / OperationAlgebra / LawSet / Admissibility; they may only summarise and cite.

### A.19.ULSAM:0 - At a glance (didactic, informative)

* **Suite stage:** `fold_Γ?` (ordering lives only in `A.19.CHR:suite_protocols`; `mechanisms[]` membership is a set, not an order).
* **Input surface:** `MeasureSetSlot` + `{CNSpecSlot, CGSpecSlot}` + `GammaFoldSlot` + `ContextSlot` (+ optional `MinimalEvidenceSlot?` override).
* **Output surface:** `AggregatedMeasureSlot` (+ optional `ContributorSetSlot?` as an explanation surface).
* **Non‑goals:** no scoring, no comparison, no selection, no “method catalog”, no hidden defaults, no hidden thresholds.
* **P2W seam:** edition/policy binding for `ΓFoldRef` / `MinimalEvidenceRef` is selected in planned baseline (A.15.3 + CHR P2W hook), not invented at run time.
* **Failure mode:** tri‑state guard `GuardDecision := {pass|degrade|abstain}`; unknown/insufficient evidence never coerces to “pass”.
* **Rule of thumb:** if you are about to “average/sum/roll up”, you probably need an explicit ULSAM `Fold_Γ` stage (or a justified decision to *not* fold).

**What this mechanism is.** `ULSAM` is the CHR mechanism that makes **aggregation explicit**: it performs an explicit **Γ‑fold** over a set of **admitted measures**, producing an **aggregated measure** (and optionally a contributor surface) under **declared legality**.

**What this mechanism is not.**
- It is **not** a scoring method (that is `USCM`).
- It is **not** a comparison mechanism (that is `CPM`).
- It is **not** a selection mechanism (that is `SelectorMechanism`).
- It is **not** a “method catalog”: method specifics belong to SoTA packs and wiring (`G.*:Ext.*`), not here.
- It is **not** a place to hide defaults (“implementation default fold”) or hidden thresholds.

**When you need ULSAM.**
- You want to “roll up” multiple measures into one measure (e.g., an overall reliability/assurance coordinate, a single aggregated risk measure, an aggregate score coordinate).
- You need the fold to be **auditable** (what contributed; what was excluded by evidence/legality).
- You need the fold to be **scale-lawful** (no ordinal arithmetic; no illegal mixing of units).
- You need the fold to be **policy-bound and edition-stable** (replayability and pin traceability).

**Where it sits in CHR.**
- In the CHR suite protocol, ULSAM corresponds to the optional stage `fold_Γ?` (i.e., **explicitly optional** and never hidden inside `score/compare/select`).

**60‑second script for engineer-managers.**
> “If you’re about to average, sum, or otherwise compress multiple measures into one, stop. Ask: (i) do we have a declared Γ‑fold policy and SCP legality, (ii) are the measures admissible and scale-compatible, (iii) what do we do if evidence is missing? If you cannot answer with explicit pins/refs, you are not folding — you are smuggling an assumption. Use ULSAM’s `Fold_Γ`, record the effective Γ‑fold and contributor set, and keep the fold as an explicit step.”

### A.19.ULSAM:1 - Problem frame (normative)

Within CHR, teams frequently need an **explicit aggregation step** (Γ‑fold) to produce an aggregated measure that is later consumed by comparison and/or selection. Without a dedicated mechanism boundary, aggregation tends to:
- leak into scoring (“the score function also averages everything”),
- leak into selection (“the selector silently computes a scalar”),
- become an “implementation default” rather than a declared policy,
- violate scale legality (especially via ordinal arithmetic or unit-mixing),
- become unauditable (“what exactly got folded, and under what evidence posture?”).

### A.19.ULSAM:2 - Problem (normative)

How do we define an aggregation step that:
1) is **explicit** (separate from scoring/comparison/selection),  
2) is **scale-lawful** and legality-gated (`CSLC` + `CG‑Spec.SCP`),  
3) is **Γ‑fold-policy-bound** (`CG‑Spec.Γ_fold` or explicit override),  
4) is **evidence-gated** with tri‑state guards (no `unknown → 0/false` coercions),  
5) is **auditable** (editions, effective fold, contributor surface),  
6) preserves **kernel stability** while allowing SoTA evolution via wiring,  
7) remains **didactically readable** (one owner pattern; no scavenger hunt).

### A.19.ULSAM:3 - Forces (normative)

- **Lawfulness vs convenience.** The most “convenient” aggregation (e.g., weighted sums) is often illegal across scales/units; lawful folds require explicit constraints.
- **Explicitness vs brevity.** A single scalar is short to discuss, but expensive in hidden assumptions.
- **Kernel stability vs method evolution.** Aggregation methods evolve; the kernel must not.
- **Evidence gating vs “always return a number.”** The mechanism must support abstain/degrade rather than coercion.
- **Optional stage vs pipeline clarity.** `fold_Γ?` is optional in CHR protocols; optionality must be explicit (not implicit “sometimes scoring folds”).
- **Auditability vs minimal overhead.** Recording contributor sets and effective pins adds overhead but prevents semantic drift.
- **Cross-context reuse vs locality.** Cross-context folds must respect Transport discipline (Bridge+CL/ReferencePlane) and penalty routing to `R_eff`.
- **P2W separation and gate/guard separation.** ULSAM must expose eligibility and audit pins without turning into (i) a WorkPlanning baseline binder or (ii) a legality gate: planned slot fillings belong to P2W artefacts (WorkPlanning), while GateDecision/GateLog live in gate patterns / WorkEnactment (suite protocols remain mechanism‑steps only).

### A.19.ULSAM:4 - Solution (normative)

ULSAM is the **canonical scale‑aggregation mechanism** in the CHR suite. It defines:
* a stable **mechanism boundary** (`fold_Γ?` is a stage with its own operation and eligibility predicate),
* a stable **SlotKind surface** (via the suite lexicon),
* a **tri‑state admissibility guard** (fail‑closed on missing legality/evidence),
* and an **audit minimum** (edition pins + effective Γ‑fold identity + crossing policy ids when transport occurs).

Method semantics (“which aggregation family to use”) remain out of suite core: they belong in SoTA packs (`G.2`) and wiring‑only extension modules (`GPatternExtension` blocks), while ULSAM remains the stable contract surface.

#### A.19.ULSAM:4.1 - Mechanism.Intension (canonical; normative)

Archetypal Grounding — **Mechanism.Intension** (normative).

This is the canonical `U.Mechanism.Intension` for `ULSAM.IntensionRef` and is intended to be cited by CHR suite artifacts and by any wiring layers.

* **Scope note:** this intension is an **instance** authored to the `U.Mechanism.Intension` shape owned by `A.6.1`. It defines only the mechanism’s semantic surface (slots/ops/laws/guards/audit). It does **not** bind project‑specific pins (P2W), and it does **not** emit GateDecision/GateLog or publish/telemetry steps; it emits `Audit` pins and a tri‑state guard only.

* **IntensionHeader:** `id = ULSAM`, `version = 1.0.0`, `status = stable`.
* **IntensionRef:** `ULSAM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).
* **Tell.** Explicit **Γ‑fold** over admitted measures — no hidden aggregation inside scoring/comparison/selection.
* **Purpose:** explicit **Γ‑fold** (and, when declared, time‑fold) over admitted measures — no hidden aggregation inside scoring/selection.
* **Imports:** `G.0 (CG‑Spec.Γ_fold, CG‑Spec.SCP, CG‑Spec.MinimalEvidence)`, `A.18 (CSLC)`, `A.19.CN (CN‑Spec.acceptance + aggregation routing)`, `A.6.5 (slot discipline)`, `B.3 (Γ‑fold defaults for R_eff, incl. WLNK)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **SubjectBlock:**
  * **SubjectKind:** `ScaleAggregation` (Γ‑fold).
  * **BaseType:** `U.Measure`.
  * **SliceSet:** `U.ContextSliceSet`.
  * **ExtentRule:** aggregation ranges over **admitted** measure sets in the active context slice (admission routed by `CNSpecSlot.acceptance`); legality is delegated to `CG‑Spec.Γ_fold` and `CG‑Spec.SCP`.
  * **ResultKind?:** `U.Measure`.

* **SlotIndex** (derived projection from `SlotSpecs` / guard SlotSpecs; uses `A.19.CHR:4.2.1` SlotKind tokens; no independent semantics):
  * `MeasureSetSlot : ⟨ValueKind = U.Set (of U.Measure), refMode = ByValue⟩`,
  * `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`,
  * `CGSpecSlot : ⟨ValueKind = CG‑Spec, refMode = CGSpecRef⟩`,
  * `GammaFoldSlot : ⟨ValueKind = ΓFold, refMode = ΓFoldRef⟩`,
  * `ContextSlot : ⟨ValueKind = U.BoundedContext, refMode = U.BoundedContextRef⟩`,
  * `MinimalEvidenceSlot? : ⟨ValueKind = MinimalEvidence, refMode = MinimalEvidenceRef⟩` (optional override; otherwise cite `CGSpecSlot.MinimalEvidence`),
  * `AggregatedMeasureSlot : ⟨ValueKind = U.Measure, refMode = ByValue⟩`,
  * `ContributorSetSlot? : ⟨ValueKind = U.Set (of U.Measure), refMode = ByValue⟩` (optional but recommended for auditability).

* **OperationAlgebra** (suite stage = `fold_Γ?`, per `A.19.CHR:4.5`; canonical stage‑op = `Fold_Γ`):
  * `Fold_Γ(MeasureSetSlot, CNSpecSlot, CGSpecSlot, GammaFoldSlot, ContextSlot, MinimalEvidenceSlot?) → (AggregatedMeasureSlot, ContributorSetSlot?)`.

* **LawSet** (minimum; explicit, scale‑lawful folding only):
  1. **No hidden aggregation:** any Γ‑fold MUST be explicit as `Fold_Γ` (no folding hidden inside `Score/Compare/Select`).
  2. **Scale‑lawfulness:** aggregation MUST be CSLC‑lawful and admissible under `CGSpecSlot.SCP`; ordinal arithmetic (e.g., means on ordinal ranks) is forbidden unless explicitly allowed by the relevant CSLC fragment.
  3. **Γ‑fold legality:** `GammaFoldSlot` MUST resolve to either `CGSpecSlot.Γ_fold` or an explicitly pinned override (CAL policy) — never an implicit “implementation default”.
  4. **Evidence‑gated folding:** if evidence is insufficient/unknown, folding MUST follow tri‑state guard behavior and MUST NOT silently coerce.
  5. **Contributor accountability (when produced):** when `ContributorSetSlot?` is produced, it MUST be a subset of the admitted portion of `MeasureSetSlot`, and `AggregatedMeasureSlot` MUST be the result of applying the effective Γ‑fold to that contributor subset (no “hidden contributors”).
  6. **No implicit UNM:** ULSAM MUST NOT silently normalize/rescale to “force comparability.” If establishing a compare‑on‑invariants surface requires UNM for the measures being folded, UNM MUST appear as an explicit stage (Uses + pins) upstream; ULSAM itself remains folding‑only.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing legality/evidence):
  * `FoldEligibility_Γ(MeasureSetSlot, CNSpecSlot, CGSpecSlot, GammaFoldSlot, ContextSlot, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `CGSpecSlot` provides the legality surface (`SCP` and `Γ_fold`), (ii) `GammaFoldSlot` is admissible under `CGSpecSlot.Γ_fold` routing (or explicit override), and (iii) the measure set is admitted (per `CNSpecSlot.acceptance`) and scale‑compatible for the intended fold.
  * Define `EffectiveMinimalEvidence := (MinimalEvidenceSlot if present, else CGSpecSlot.MinimalEvidence)`; the guard MUST evaluate evidence against `EffectiveMinimalEvidence`.
  * If evidence is missing/unknown under `EffectiveMinimalEvidence`, the guard MUST NOT return `pass` (return `degrade` or `abstain` per the effective failure behavior; record the basis in Audit).

* **Applicability:**
  * Intended to be used only when a fold is explicitly required (and never as a hidden sub‑step of scoring/comparison/selection).
  * Applicable only when `CGSpecSlot` provides the legality surface (`Γ_fold` and `SCP`) (fail‑closed otherwise).
  * If comparability routing for the measures being folded is UNM‑based, applicability presumes an explicit upstream UNM stage; ULSAM does not “make measures comparable” by itself.

* **Transport:** Bridge+CL/ReferencePlane only; penalties route to **`R_eff` only**.
* **Γ_timePolicy:** `point` by default; time‑fold requires explicit windowing policy (if an explicit operator is needed, introduce `FoldTime_Γ` as an `⊑⁺` extension using `GammaTimeRuleSlot` from the CHR SlotKind Lexicon).
* **PlaneRegime:** values live on **episteme ReferencePlane**; on plane crossings apply **CL^plane** policy; penalties → **`R_eff` only**.

* **Audit:**
  * MUST record: `CNSpecRef.edition`, `CGSpecRef.edition`, and the effective Γ‑fold (`ΓFoldRef`).
  * If `GammaFoldSlot` resolves via an explicit override, SHOULD record the override’s `policy-id` (or its stable ref) alongside `ΓFoldRef`.
  * When `MinimalEvidenceSlot?` is present, MUST record `MinimalEvidenceRef`; otherwise MUST cite `CGSpecSlot.MinimalEvidence` as the effective evidence policy.
  * When `ContributorSetSlot?` is produced, SHOULD record it (or an id reference) as an auditable explanation surface.
  * SHOULD record: any explicit UNM invocation ids/pins when folding presumes a compare‑on‑invariants surface established by UNM.
  * SHOULD record: any Bridge/CL/ReferencePlane ids when `Transport` was invoked.
  * SHOULD record: the evaluated `GuardDecision` (especially when not `pass`) and, when applicable, the effective evidence policy / failure behavior reference used to justify `degrade|abstain`.

#### A.19.ULSAM:4.2 - Interpretation notes (didactic, informative)

- **Γ‑fold is a declared contract surface, not an implementation choice.** In FPF terms, “how we fold” is a **policy-level commitment**: `GammaFoldSlot` MUST be resolvable to `CGSpecSlot.Γ_fold` routing or an explicit pinned override. If you cannot cite it, you do not have a fold — you have a hidden default.
- **ULSAM is not normalization.** ULSAM does not establish comparability by itself: it does not normalize, rescale, or “align units” as a hidden convenience. If a compare‑on‑invariants surface is required, invoke UNM explicitly upstream and cite the effective pins in Audit.
- **Prefer vector semantics when possible.** If you do not strictly need one aggregated measure, keep measures separate and let `CPM` + `SelectorMechanism` operate on a partial order (set-return semantics). A fold is a lossy compression; treat it as such.
- **Contributor surfaces are not “nice-to-have” in practice.** `ContributorSetSlot?` is optional in the signature, but operationally it is the simplest way to prevent “mystery rollups” and to preserve an explanation surface.
- **Time-fold is a specialization, not a loophole.** The base ULSAM declares `Γ_timePolicy` and allows time-fold only via explicit windowing policy. If a project needs an explicit `FoldTime_Γ` operator, introduce it as an `⊑⁺` extension consistent with `A.6.1:4.2.1` (no mutation of inherited ops; no SlotKind drift).
  - Use the suite lexicon token `GammaTimeRuleSlot` for the additional windowing rule input; do not overload `ContextSlot` or `GammaFoldSlot` to smuggle time semantics.

### A.19.ULSAM:5 - Archetypal grounding (didactic, informative)

#### A.19.ULSAM:5.1 - Tell

- In CHR, ULSAM exists to keep the stage `fold_Γ?` **explicit**: if a pipeline wants folding, it invokes `ULSAM.Fold_Γ`; otherwise it skips the stage. Folding MUST NOT be smuggled into `USCM.Score`, `CPM.Compare`, or `SelectorMechanism.Select`.
- In `U.System` decision contexts: ULSAM is where you explicitly fold multiple admitted measures (e.g., multiple risk coordinates) into an aggregated measure **only when the contract declares that fold**.
- In `U.Episteme` contexts: ULSAM is where you explicitly fold an evidential or measurement set into an aggregated coordinate (e.g., an assurance measure), typically using a conservative Γ‑fold (e.g., weakest-link) when folding reliability-like quantities.

#### A.19.ULSAM:5.2 - Show

**Scenario A (manager-facing): “roll up” a multi-metric readiness into one reliability-like coordinate.**
1. A CHR pipeline produces a set of admitted measures (post-`USCM` or directly from characteristic measures):  
   `MeasureSetSlot = {m₁, m₂, …, m_k}`.
2. The team wants a single “readiness” measure `m_ready` to be used as an input to later comparison/selection.  
   The temptation is to “just average” or “just do weighted sum”.
3. ULSAM forces three explicit questions before folding:
   - **Legality:** Is the fold admissible under `CGSpecSlot.SCP` (units/scale) and `CGSpecSlot.Γ_fold` (declared fold kinds)?
   - **Evidence:** Is the evidence posture sufficient under `MinimalEvidence`? If not, do we `degrade` or `abstain`?
   - **Policy identity:** What is the identity of the fold (which ΓFoldRef, which edition)?
4. Only then, the pipeline performs:  
   `Fold_Γ(MeasureSetSlot, CNSpecSlot, CGSpecSlot, GammaFoldSlot, ContextSlot, MinimalEvidenceSlot?) → (AggregatedMeasureSlot, ContributorSetSlot?)`.  
   The audit records `ΓFoldRef` and (optionally) the contributor surface.

**Scenario B (engineer-facing): cross-context aggregation with explicit Transport discipline.**
- A project tries to fold measures that originate from different contexts. ULSAM does not “make it fine”; it requires Transport to be explicit (Bridge+CL/ReferencePlane) and routes penalties to `R_eff` only. If the project cannot cite Bridge ids and the effective congruence policy, folding is non-admissible (fail-closed by guard).

### A.19.ULSAM:6 - Bias-Annotation (informative)

This pattern intentionally biases CHR authoring toward **explicit aggregation boundaries** and against “scalarization by convenience”.

* **Gov (governance).** Bias toward auditable folds (editions, effective ΓFoldRef, contributor surfaces). Risk: perceived overhead. Mitigation: keep the signature stable and move method specifics to SoTA wiring.
* **Arch (architecture).** Bias toward keeping `fold_Γ` a distinct stage (no leakage into score/compare/select). Risk: longer pipelines. Mitigation: the stage is explicitly optional (`fold_Γ?`) and can be omitted when not required.
* **Onto/Epist (ontology/epistemology).** Bias toward scale-lawful aggregation (no illegal ordinal arithmetic; SCP-bound). Risk: forbids many informal “single-number” habits. Mitigation: use partial orders and set-return selection unless a lawful fold is truly needed.
* **Prag (practice).** Bias toward policy-bound defaults (no “implementation default Γ‑fold”). Risk: teams must name policies. Mitigation: provide conservative defaults in `CG‑Spec.Γ_fold` and keep overrides explicit.
* **Did (didactic).** Bias toward one-owner readability (this pattern is the owner; no scavenger hunt). Risk: duplication temptation elsewhere. Mitigation: enforce Tell+Cite canonicalization.

### A.19.ULSAM:7 - Conformance Checklist (normative)

| ID | Requirement |
|----|-------------|
| **CC‑A19ULSAM‑0** | **MechAuthoring discipline:** the canonical ULSAM Mechanism.Intension in `A.19.ULSAM:4.1` MUST satisfy `A.6.1` `U.MechAuthoring` and the relevant `CC‑UM.*` checks; this pattern does not override the `U.Mechanism.Intension` shape. |
| **CC‑A19ULSAM‑1** | **Single owner:** the canonical ULSAM `U.Mechanism.Intension` MUST be owned by `A.19.ULSAM:4.1`. Any other ULSAM “card” text MUST be reduced to Tell+Cite referencing this owner section. |
| **CC‑A19ULSAM‑2** | **No hidden aggregation:** any Γ‑fold MUST be explicit as `ULSAM.Fold_Γ` (no folding hidden inside `Score/Compare/Select`, including inside `USCM/CPM/SelectorMechanism`). |
| **CC‑A19ULSAM‑3** | **Scale-lawfulness:** a conformant ULSAM fold MUST be CSLC-lawful and admissible under `CGSpecSlot.SCP`. Ordinal arithmetic is forbidden unless explicitly allowed by the relevant CSLC fragment. |
| **CC‑A19ULSAM‑4** | **Γ‑fold legality:** a conformant ULSAM publication MUST ensure `GammaFoldSlot` resolves to `CGSpecSlot.Γ_fold` or an explicitly pinned override (CAL policy). “Implementation default fold” is non-conformant. |
| **CC‑A19ULSAM‑5** | **Evidence gating:** a conformant ULSAM publication MUST guard folding via `FoldEligibility_Γ` with `GuardDecision ∈ {pass|degrade|abstain}`; missing/unknown evidence MUST NOT yield `pass`. If `MinimalEvidenceSlot?` is absent, the guard MUST evaluate against `CGSpecSlot.MinimalEvidence`. |
| **CC‑A19ULSAM‑6** | **SlotKind discipline:** SlotKind tokens used in the ULSAM intension MUST come from the CHR SlotKind Lexicon (`A.19.CHR:4.2.1`). New SlotKinds require lexicon extension first. |
| **CC‑A19ULSAM‑7** | **Audit surface:** Audit MUST record `CNSpecRef.edition`, `CGSpecRef.edition`, and the effective `ΓFoldRef`; and MUST record `MinimalEvidenceRef` when overridden (else cite `CGSpecSlot.MinimalEvidence`). |
| **CC‑A19ULSAM‑8** | **Contributor accountability:** when `ContributorSetSlot?` is produced, it SHOULD be recorded (or referenced by stable id) as an explanation surface for what contributed after legality/evidence gating. |
| **CC‑A19ULSAM‑9** | **P2W separation:** planned baseline artefacts MUST bind `ΓFoldRef`/`MinimalEvidenceRef`/editions (A.15.3 + CHR P2W hook); these bindings MUST NOT be invented as run-time decisions inside the suite protocol. |
| **CC‑A19ULSAM‑10** | **Gate/guard separation:** ULSAM MUST NOT embed GateDecision/GateLog or publish/telemetry operations in the `fold_Γ?` stage; admissibility is via `FoldEligibility_Γ` (tri‑state) and run‑time observability via `Audit` pins only. |
| **CC‑A19ULSAM‑11** | **No implicit UNM:** ULSAM MUST NOT silently normalize/rescale to force comparability. When a compare‑on‑invariants surface is required, UNM MUST be invoked explicitly upstream and SHOULD be cited via stable ids/pins in `Audit`. |

### A.19.ULSAM:8 - Common anti-patterns (didactic, informative)

| Anti-pattern | Symptom | Why it fails in FPF | How to avoid |
|---|---|---|---|
| Hidden rollup inside scoring | “Our score already averages everything.” | Violates the “no hidden aggregation” law and hides Γ‑fold identity. | Keep `USCM.Score` scoring-only; use `ULSAM.Fold_Γ` as an explicit stage. |
| Averaging ordinals | Means on ranks/levels, or unitless mixing | Illegal under CSLC/SCP unless explicitly allowed. | Keep ordinal outputs as ordinal; compare via CPM; if folding is required, use an ordinal-legal fold explicitly declared by Γ_fold policy. |
| Implementation default Γ‑fold | “If not specified, we use X.” | Breaks replayability and violates Γ‑fold legality. | Require `GammaFoldSlot` to resolve to `CGSpecSlot.Γ_fold` or pinned override. |
| Coercing unknown to a number | “Missing metric becomes 0.” | Violates tri-state guard discipline; silently changes meaning. | Use `FoldEligibility_Γ` with `{pass|degrade|abstain}` and record the effective evidence policy. |
| Cross-context folding without Transport | Folding measures from different contexts “as-is” | Violates Bridge-only discipline and penalty routing to `R_eff`. | Make Transport explicit (Bridge+CL/ReferencePlane) and record ids in Audit. |
| Treating fold_Γ as mandatory | Always folding even when not needed | Unnecessary lossy compression; reduces set-return semantics. | Keep `fold_Γ?` explicitly optional in protocols; prefer vector+CPM+Selector when possible. |

### A.19.ULSAM:9 - Consequences (didactic, informative)

| Benefits | Costs / trade-offs |
|---|---|
| Clear separation of concerns: folding is explicit and auditable. | Adds an explicit step; authors must name Γ‑fold policies. |
| Prevents illegal “single-number” shortcuts (ordinal means, unit mixing). | Some familiar heuristics become non-conformant. |
| Improves evolvability: folding methods evolve via wiring, while the kernel signature stays stable. | Requires discipline to keep method specifics out of kernel prose. |
| Supports evidence-aware aggregation via tri-state guards. | Guard + Audit expectations may feel heavier than ad-hoc aggregation. |

### A.19.ULSAM:10 - Rationale (didactic, informative)

Aggregation is a **semantic commitment**: it changes a set/vector of measures into a single measure, and therefore changes what later comparison/selection can legitimately claim. In CHR, that commitment must be explicit, legality-gated, and auditable.

Keeping ULSAM as its own mechanism preserves:
- the strict boundary between **method choice** (SoTA packs) and **kernel signature** (Mechanism.Intension),
- the strict boundary between **planned baseline** (pins chosen in WorkPlanning) and **run-time audit** (what actually executed),
- and the engineer-facing clarity that “we folded here, not everywhere”.

### A.19.ULSAM:11 - Known uses (didactic, informative)

- CHR suite optional stage `fold_Γ?` (explicitly optional; never hidden).
- Folding trust/assurance-like quantities (conservative Γ‑folds such as WLNK as declared defaults under trust policy).
- Any project that requires an auditable “roll-up” measure prior to lawful comparison/selection.
- In transduction graphs (E.18 / TGA): ULSAM appears as a mechanism instance node whose `ΓFoldRef` / `MinimalEvidenceRef` are bound in planned baseline (P2W), while Audit records the effective pins used at run time.

### A.19.ULSAM:12 - Builds on / Relates to

**Builds on (cite, don’t duplicate).**
- `A.6.1` (`U.Mechanism.Intension` shape; `U.MechAuthoring`; CC‑UM discipline).
- `A.6.5` (slot discipline; SlotIndex as a projection).
- `A.19.CHR` (CHR suite boundary; stage `fold_Γ?`; CHR SlotKind Lexicon).
- `G.0` (`CG‑Spec.Γ_fold`, `CG‑Spec.SCP`, `CG‑Spec.MinimalEvidence`; legality gate).
- `A.18` (CSLC).
- `B.3` (Γ‑fold defaults for `R_eff`, including WLNK; trust skeleton).

**Relates to (coordination, not ownership).**
- `A.19.CN` (`CN‑Spec`), via `CNSpecSlot.acceptance` gating in admissibility.
- `A.19.UINDM` / `USCM` / `CPM` / `SelectorMechanism` as adjacent CHR stages (Uses contour; no semantic ownership transfer).
- Part G SoTA packs and wiring (`G.2` + `G.*:Ext.*`) for method family selection and edition/policy binding.

### A.19.ULSAM:13 - SoTA-Echoing (informative; not a center of gravity)

SoTA here is treated as **method-family material to be wired** (ideally curated as `G.2` claim sheets and connected via `G.*:Ext.*` wiring), not as kernel semantics. ULSAM’s contribution is the stable boundary: explicit, legal, auditable folding.

**SoTA vs popular note.** This section records alignment to post‑2015 evidence‑backed practice. It is **not** a mandate to use fashionable methods; method semantics stay in SoTA packs (`G.2`) and wiring modules, while this pattern fixes the stable mechanism boundary.

**Pack note (Phase‑3):** this pattern does not currently cite a ULSAM‑specific `G.2` SoTA pack/ClaimSheet. If/when such a pack is introduced, replace the bibliographic pointers below with the pack’s `ClaimSheetId` citations, keeping the mechanism semantics unchanged.

| SoTA practice pointer (post‑2015+) | Primary source | Where it connects | Adoption status |
|---|---|---|---|
| Permutation‑invariant set aggregation as a *method family* (set → summary) | Zaheer et al., “Deep Sets” (2017) [1] | Candidate `ΓFold` families can include permutation‑invariant folds; ULSAM keeps them legality‑gated and policy‑pinned. | **Adapt** (keep legality/pins explicit; do not treat learned folds as implicit defaults). |
| Attention-based permutation‑invariant set aggregation as a *method family* | Lee et al., “Set Transformer” (2019) [4] | Alternative learnable set folds (pooling by attention); still requires explicit policy binding and legality gating. | **Adapt** (publish as method family in SoTA pack; pin editions/policies; keep kernel unchanged). |
| Robust aggregation under uncertainty/outliers as a *policy-selectable fold family* | Rahimian & Mehrotra, “Distributionally Robust Optimization: A Review” (2019) [2] | Treat “worst‑case / risk‑aware” folds as explicit Γ‑fold options (policy-bound), not as hidden safety margins. | **Adapt** (policy‑bound and SCP/CSLC‑gated). |
| Single‑owner discipline for architectural statements | ISO/IEC/IEEE 42010:2022 [3] | Supports the “one semantic owner” rule: ULSAM intension content lives here; other places cite. | **Adopt** (principle-level; applied to FPF pattern ownership). |

**Reminder.** “SoTA” means best known methods; it is not a synonym for “popular right now”. SoTA material should be curated and versioned in SoTA packs and connected via wiring modules, not embedded into kernel mechanism signatures.

[1]: https://arxiv.org/abs/1703.06114 "Zaheer et al., Deep Sets, 2017"
[2]: https://arxiv.org/abs/1908.05659 "Rahimian & Mehrotra, Distributionally Robust Optimization: A Review, 2019"
[3]: https://www.iso.org/standard/74393.html "ISO/IEC/IEEE 42010:2022 — Systems and software engineering — Architecture description"
[4]: https://arxiv.org/abs/1810.00825 "Lee et al., Set Transformer, 2019"

### A.19.ULSAM:End

## A.19.CPM - Unified Comparison Mechanism (CPM)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A / CN‑Spec cluster (A.19) / CHR mechanism owner patterns (Phase‑3)
> **Source:** FPF / CHR Phase‑3 mechanism owner patterns
> **Modified:** 2026‑01‑20
>
> **Semantic owner note, Phase‑3 canonicalization:** this pattern is the **designated single semantic owner** of the canonical `U.Mechanism.Intension` for `CPM.IntensionRef` (CHR suite stage `compare`). This matches the single‑owner discipline: mechanism‑intension semantics live in an explicitly designated mechanism‑owner pattern (`E.20`).
> `A.6.1` remains the owner of the **template** of `U.Mechanism.Intension`; this pattern owns the **CPM‑specific constraints** over the (suite‑owned) SlotKind surface — operations, laws, admissibility, applicability, transport, plane, and audit obligations for that template (single‑owner at the instance‑semantics level, not a second schema, and not the owner of the CHR SlotKind lexicon).
>
> **Canonicalization hook, ID‑continuity‑safe:** any other appearances of the CPM intension (e.g., suite prose in `A.19.CHR`) SHALL be reduced to a **Tell + Cite** stub pointing to **`A.19.CPM:4.1`**, while preserving the original section headings and their public `PatternId:SectionPath` IDs for continuity (alias‑dock legacy tokens rather than deleting them).
> Such stubs MUST NOT restate SlotIndex, OperationAlgebra, LawSet, AdmissibilityConditions, Applicability, Transport, Γ_timePolicy, PlaneRegime, or Audit content (no “second center of gravity” via near‑duplicate prose).

### A.19.CPM:0 - At a glance (didactic, informative)

CPM is the CHR comparison kernel: it compares two admitted profiles under an explicit, legality‑gated comparator and returns a **set‑valued** comparison outcome.

**One-screen purpose (manager-first).** CPM answers: “Given two admitted profiles and an explicit comparator, what relation holds under the declared legality frame?” It does **not** answer: “Which one should we pick?” (selection) nor “What is the score?” (scoring).

**Manager quick checklist (before you trust a comparison):**
* **Comparator is explicit:** do we have a `ComparatorSpecRef`, and is it admitted by `CG‑Spec.ComparatorSet`?
* **Legality is declared:** do we cite `CG‑Spec` (and `SCP` when numeric ops exist) and treat violations as `degrade|abstain`?
* **Evidence is not faked:** are missing/unknown inputs routed to `degrade|abstain` under the effective MinimalEvidence policy (never to `pass`)?
* **Partiality is preserved:** are we willing to accept incomparability/ties as first‑class outcomes (set‑valued result), rather than forcing a winner?

* **Suite stage:** `compare` (pipeline order lives in `A.19.CHR:4.5`, not in the `mechanisms[]` enumeration).
* **Input (conceptual):** left profile, right profile, `CN‑Spec`, `CG‑Spec`, an explicit `ComparatorSpec`, context slice; optional explicit `MinimalEvidence` override.
* **Output (conceptual):** `ComparisonResultSlot` as a **set of relation/poset tokens** (not a single scalar, and not an embedded selection decision).
* **P2W seam:** concrete `ComparatorSpecRef.edition` and any policy ids are bound **only** in planned baseline artefacts (A.15.3 + `A.19.CHR:4.7.2`). CPM’s kernel does **not** bind project‑specific pins; executions record the **effective** refs/pins in `Audit`.
* **Reproducible comparisons:** for parity/benchmark style runs that require a stable run package + report surface (editions, windows, parity pins), route packaging through `G.9` (Parity / Benchmark Harness). CPM stays kernel‑only.
* **What CPM does not do (strict distinction):**

  * does **not** normalize (`UNM`);
  * does **not** choose indicators (`UINDM`);
  * does **not** score (`USCM`);
  * does **not** fold/aggregate (`ULSAM`);
  * does **not** select (“pick best”) — that is `SelectorMechanism`.
* **Core safety commitments:** legality gate via `CG‑Spec.ComparatorSet` + `CG‑Spec.SCP` + CSLC; tri‑state admissibility (`pass|degrade|abstain`); unknown never coerces to “pass” or to a fabricated outcome; no silent scalarization/totalization.
* **Where method details live:** in editions of `ComparatorSpec` and their SoTA wiring (Part G packs/extensions), not inside CPM’s kernel semantics.
* **Quick rule of thumb:** if you need **numbers**, that’s `USCM`; if you need a **decision/portfolio**, that’s `SelectorMechanism`. CPM’s job is only: **compare → relation tokens**.

### A.19.CPM:1 - Problem frame

FPF’s Characterization (CHR) suite treats comparison as a **distinct** mechanism stage (`compare`) with suite‑wide obligations that forbid hidden scalarization/totalization, require tri‑state guards, and enforce legality surfaces for numeric operations. Comparison must therefore be described as:

* a **mechanism** (in the `U.Mechanism.Intension` sense, per `A.6.1` / slot discipline `A.6.5`),
* that is **suite‑conformant** (per CHR obligations and protocol closure in `A.19.CHR`),
* and **contract‑surface‑respecting** (comparability and admission are routed via `CN‑Spec` and legality is gated via `CG‑Spec` rather than re‑invented locally).

Within suite protocols, CPM appears as the explicit `compare` stage: it consumes admitted left/right profiles (scores and/or folded measures **when** those upstream stages are present) and produces a lawful, auditable **comparison relation** that downstream selection can consume without CPM smuggling selection or scoring semantics into “comparison”.

### A.19.CPM:2 - Problem

Engineering teams frequently need to compare two options (designs, methods, vendors, trajectories, hypotheses, etc.) across multiple measures and under incomplete evidence. Without a canonical comparison mechanism, teams predictably fall into one or more of these failure modes:

* **Hidden scalarization:** forcing a single number (or a single winner) from multi‑criteria reality, erasing incomparability and ties.
* **Silent totalization:** inventing an implied total order by convenience tie‑breakers or implicit thresholds, even when only a partial order is warranted.
* **Illegal arithmetic:** comparing across measures using operations that are not scale‑lawful (CSLC‑violating) or not admitted by the declared legality frame.
* **Comparator drift:** “the comparator” exists only as prose or code intuition; different teams compare “the same thing” differently because the comparator spec is not explicit and edition‑pinned.
* **Unknown coercion:** missing/unknown evidence is coerced into an outcome (e.g., “treat missing as equal”, “treat unknown as worse”), producing comparisons that look decisive but are epistemically unsafe.
* **Cross‑context leakage:** comparing across contexts/planes without explicit bridges, CL routing, or penalties discipline, producing misleading outcomes that ignore transport costs and reference plane constraints.

CPM exists to make the comparison act explicit, legality‑gated, set‑valued, and auditable—so downstream selection can remain a separate, policy‑bound step.

### A.19.CPM:3 - Forces

1. **Usability vs correctness:** engineers want a “simple compare” function; correctness demands explicit legality, explicit comparator choice, and explicit handling of incomparability/unknown.
2. **Total order convenience vs partial order truth:** total orders simplify downstream selection; partial orders are often the faithful representation (especially in multi‑criteria settings).
3. **Evolvability vs stability:** comparator methods evolve (SoTA churn); kernel semantics and slot surfaces must remain stable and wiring‑friendly.
4. **Auditability vs speed-of-discussion:** teams want fast decisions; FPF requires audit pins and explicit edition/policy references for reproducibility.
5. **Cross‑context reasoning vs transport discipline:** comparisons across contexts are valuable, but they require bridge‑only crossings and explicit penalty routing, not implicit “normalization by hand”.
6. **Avoiding “second centers of gravity”:** mechanism semantics must have a single owner; otherwise the suite, `A.6.1` archetypes, and Part‑G wiring drift apart.

### A.19.CPM:4 - Solution

CPM is specified as a canonical `U.Mechanism.Intension` whose core commitments are:

* **Comparator legality is declared and gated** (`CG‑Spec.ComparatorSet`, and `CG‑Spec.SCP` when numeric operations are involved; scale lawfulness via CSLC).
* **Results are set‑valued relation/poset tokens**; partial orders remain partial; no silent scalarization or totalization.
* **Admissibility is tri‑state and fail‑closed** on missing legality/evidence; unknown never coerces into a fabricated outcome.
* **Comparison remains distinct from selection**; CPM produces relation outcomes; `SelectorMechanism` consumes them.

This pattern defines (single‑owner, wiring‑friendly):
1. a **stable mechanism boundary** for lawful comparison: `Compare(...) → ComparisonResultSlot` plus a tri‑state `CompareEligibility` guard;
2. a **stable SlotKind surface** (by suite lexicon tokens) that downstream selection and Part‑G wiring can rely on without SlotKind drift;
3. a **legality/evidence responsibility split**: legality is gated by `CG‑Spec` (and CSLC), while admission/comparability routing is cited from `CN‑Spec`;
4. a minimal **audit contract**: what pins/editions MUST be recorded to make a comparison replay‑grade;
5. explicit **P2W separation**: planned baseline binds editions/policies; CPM records effective bindings in `Audit`.

#### A.19.CPM:4.1 - Mechanism.Intension (canonical; normative)

This is the canonical `U.Mechanism.Intension` for `CPM.IntensionRef`. It is intended to be cited by CHR suite artifacts and by any wiring layers.

* **Scope note:** this intension is an **instance** authored to the `U.Mechanism.Intension` shape (`A.6.1`). It does **not** publish/telemetry, does **not** publish `GateDecision` nor `DecisionLog` surfaces (gate‑only), and does **not** embed selection. It emits `Audit` pins and a tri‑state guard only (per suite obligations).
  * **P2W separation:** this intension does **not** bind project‑specific pins (editions, policy‑ids, bridge ids, etc.). Binding lives in planned baseline artefacts (A.15.3 + `A.19.CHR:4.7.2`); executions record effective refs/pins in `Audit`.

* **IntensionHeader:** `id = CPM`, `version = 1.0.0`, `status = stable`.

* **IntensionRef:** `CPM.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).

* **SignatureManifest (optional; importability):** if a CPM publication is intended for reuse beyond the CHR suite, author SHOULD publish a `SignatureManifest` that records (i) the declared `Compare` stage‑op signature, (ii) the SlotKind surface (by lexicon tokens), and (iii) the explicit set‑valued output commitment (no silent scalarization/totalization).

* **Tell.** Lawful comparison producing **set‑valued** parity / poset outcomes (not a single scalar).

* **Purpose:** lawful comparison producing **set‑valued** parity / poset outcomes (not a single scalar).

* **Imports:** `G.0 (CG‑Spec.ComparatorSet, CG‑Spec.SCP, CG‑Spec.MinimalEvidence)`, `A.18 (CSLC)`, `A.19.CN (comparability routing)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **SubjectBlock:**

  * **SubjectKind:** `Comparison`.
  * **BaseType:** CHR‑typed measures in a CG‑Frame (see `CG‑Spec.ComparatorSet`).
  * **SliceSet:** `U.ContextSliceSet`.
  * **ExtentRule:** comparison ranges over admitted left/right profiles under the active context slice, using a declared comparator from `CG‑Spec.ComparatorSet`.
  * **ResultKind?:** `U.Set` (relation/poset token set; set‑valued by default).

* **SlotIndex** (derived projection from `SlotSpecs` / guard SlotSpecs; uses `A.19.CHR:4.2.1` SlotKind tokens; no independent semantics):

  * `LeftProfileSlot : ⟨ValueKind = U.Set (of U.Measure), refMode = ByValue⟩`,
  * `RightProfileSlot : ⟨ValueKind = U.Set (of U.Measure), refMode = ByValue⟩`,
  * `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`,
  * `CGSpecSlot : ⟨ValueKind = CG‑Spec, refMode = CGSpecRef⟩`,
  * `ComparatorSpecSlot : ⟨ValueKind = ComparatorSpec, refMode = ComparatorSpecRef⟩`,
  * `ContextSlot : ⟨ValueKind = U.BoundedContext, refMode = U.BoundedContextRef⟩`,
  * `MinimalEvidenceSlot? : ⟨ValueKind = MinimalEvidence, refMode = MinimalEvidenceRef⟩` (optional override; otherwise cite `CGSpecSlot.MinimalEvidence`),
  * `ComparisonResultSlot : ⟨ValueKind = U.Set (relation/poset tokens), refMode = ByValue⟩`.

* **OperationAlgebra** (suite stage = `compare`, per `A.19.CHR:4.5`; canonical stage‑op = `Compare`):

  * `Compare(LeftProfileSlot, RightProfileSlot, CNSpecSlot, CGSpecSlot, ComparatorSpecSlot, ContextSlot, MinimalEvidenceSlot?) → ComparisonResultSlot`.

* **LawSet** (minimum; set‑valued comparison, no hidden scalarization):

  1. **ComparatorSet gate:** `ComparatorSpecSlot` MUST be an element of `CGSpecSlot.ComparatorSet` (legality gate; cite `G.0`).
  2. **Set‑valued semantics:** `ComparisonResultSlot` is set‑valued (parity/poset tokens); partial orders remain partial — no silent totalization/scalarization.
  3. **CSLC+SCP legality:** any numeric ops implied by the comparator MUST be admissible under `CGSpecSlot.SCP` and CSLC‑lawful (cite `G.0` + `A.18`).
  4. **Unknown is not coerced:** missing/unknown evidence MUST NOT be mapped to a comparison outcome; use tri‑state guards.
  5. **No hidden thresholds/tie‑breakers:** any thresholds, epsilons, priority orders, or tie‑break logic MUST live in the declared `ComparatorSpecSlot` (or in `CNSpecSlot.acceptance` as explicit acceptance clauses), edition‑pinned and auditable; CPM MUST NOT smuggle constants.
  6. **No implicit UNM:** CPM MUST NOT perform normalization/alignment internally. If `CNSpecSlot.comparability` routes comparison through normalization‑based invariants, `CompareEligibility` MUST treat “inputs are already normalized to the declared invariants” as a precondition for `pass` (otherwise `degrade|abstain` per policy). Any UNM dependence MUST be explicit upstream and auditable.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing legality/evidence):

  * `CompareEligibility(LeftProfileSlot, RightProfileSlot, CNSpecSlot, CGSpecSlot, ComparatorSpecSlot, ContextSlot, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires: (i) `ComparatorSpecSlot ∈ CGSpecSlot.ComparatorSet`, (ii) any comparator‑implied numeric ops are admissible under `CGSpecSlot.SCP` and CSLC‑lawful for the effective measure scales, (iii) both profiles are admitted/comparable under `CNSpecSlot.comparability` and `CNSpecSlot.acceptance` for the given `ContextSlot`, and (iv) evidence satisfies the **effective** MinimalEvidence policy (explicit override via `MinimalEvidenceSlot?`, otherwise `CGSpecSlot.MinimalEvidence`).
  * If `CNSpecSlot.comparability` is normalization‑based (compare‑on‑invariants), `pass` additionally requires that the inputs are already in the required invariants/normalization regime; CPM MUST NOT “make them comparable” by silent normalization.
  * If `MinimalEvidenceSlot` is absent, the guard MUST evaluate evidence against `CGSpecSlot.MinimalEvidence` (by explicit rule), and MUST NOT return `pass` when evidence is missing/unknown **or** fails the effective MinimalEvidence gate.

* **Applicability:**

  * Intended to be used as the CHR stage `compare`: it may follow indicatorization/scoring and optional folding **when those stages are present**, and it precedes selection wherever selection occurs; MUST remain distinct from selection (no embedded “pick best”).
  * Applicable only when legality/evidence surfaces are present via `CGSpecSlot` (fail‑closed otherwise).
  * When used inside the CHR suite, stage ordering/optionality is determined only by `A.19.CHR:4.5 (suite_protocols)`; CPM does not infer order from `mechanisms[]`.

* **Transport:** Bridge+CL/ReferencePlane only; penalties route to **`R_eff` only**.

* **Γ_timePolicy:** `point` by default (no implicit “latest”).

* **PlaneRegime:** values live on **episteme ReferencePlane**; on plane crossings apply **CL^plane** policy; penalties → **`R_eff` only**.

* **Audit:**

  * MUST record: `CNSpecRef.edition`, `CGSpecRef.edition`, and the effective comparator (`ComparatorSpecRef`).
  * When `MinimalEvidenceSlot?` is present, MUST record `MinimalEvidenceRef`; otherwise MUST cite `CGSpecSlot.MinimalEvidence` as the effective evidence policy.
  * SHOULD record: the realized `GuardDecision` for `CompareEligibility`, and (when `degrade`/`abstain`) any referenced failure‑behavior / downstream‑handling policy ids (e.g., a SoS‑LOG branch id) when such policies are in scope.
  * If `CNSpecSlot.comparability` routes comparison through normalization‑based invariants, Audit MUST record the effective upstream normalization dependency (e.g., the relevant UNM intension/edition or other explicit normalization witness), or explicitly record that the comparison abstained/degraded due to missing normalization admissibility.
  * SHOULD record: a stable description of `ComparisonResultSlot` and any Bridge/CL/ReferencePlane ids when `Transport` was invoked.

#### A.19.CPM:4.2 - Interpretation notes — informative

* **Set‑valued output is the default, not a loophole.** “Set‑valued” means CPM preserves incomparability/ties/partiality as first‑class outcomes; it does not authorize silent post‑processing into a scalar or a single winner.
* **Total orders are allowed only if declared by the comparator.** If a `ComparatorSpec` defines a total order, CPM still outputs a (singleton) set of relation tokens; the totalization is a property of the declared comparator, not an implicit kernel default.
* **Normalization is not smuggled into comparison.** If `CN‑Spec.comparability` routes comparison through normalization‑based invariants, that dependence must be represented explicitly via the suite protocol and/or explicit Uses contours (CPM consumes admitted profiles; it does not silently normalize them).
* **Thresholds and tie‑breakers are never “kernel constants.”** If thresholds exist, they belong to explicit policies/specs (e.g., `ComparatorSpec`, `AcceptanceClauses`), edition‑pinned and auditable; not to hidden constants inside CPM.

### A.19.CPM:5 - Archetypal Grounding — informative

#### A.19.CPM:5.1 - Tell

Think of CPM as an **auditable relation‑builder**:

* Input: “two admitted profiles + an explicit comparator spec + declared legality/evidence surfaces”
* Output: “a **set‑valued** relation outcome that preserves incomparability and uncertainty”

The key didactic boundary is: **CPM compares; it does not decide.**

#### A.19.CPM:5.2 - Show (U.System) — comparing two supplier options without faking a total order

A program manager compares Supplier‑A vs Supplier‑B for a safety‑critical component. The team tracks a profile of measures (cost, lead time, defect rate, assurance, sustainability), but not all measures are strictly comparable across regions (different reporting regimes, different units).

* The project has a declared `CN‑Spec` (admission + comparability routing) and a declared `CG‑Spec` that lists lawful comparators in `ComparatorSet` and evidence rules in `MinimalEvidence`.
* The comparator chosen is explicit: `ComparatorSpecSlot = ParetoDominanceComparatorSpecRef@edition` (declared in `CG‑Spec.ComparatorSet`).
* CPM runs `Compare(...)`.

  * If Supplier‑A is better in cost but worse in defect rate and incomparable on assurance due to missing evidence, CPM does **not** invent “A wins” or “A loses”.
  * The guard returns `degrade` or `abstain` (per evidence policy), and the `ComparisonResultSlot` preserves the partial nature of the relation.
* The downstream `SelectorMechanism` can then return a portfolio (e.g., keep both suppliers in the candidate set) rather than forcing a single winner by hidden tie‑break rules.

#### A.19.CPM:5.3 - Show (U.Episteme) — uncertainty‑aware comparison with set‑valued outcomes

A research lead compares two proposed methods for a system component. Both methods have performance estimates with uncertainty bounds (e.g., distributions or prediction intervals). The team uses a SoTA uncertainty quantification package (post‑2015 conformal families are a common example) to avoid overstating confidence.

* `USCM` produces score profiles that are interval‑valued (or otherwise uncertainty‑annotated) rather than point estimates.
* The chosen comparator is uncertainty‑aware and declared as a `ComparatorSpec` (edition‑pinned) in `CG‑Spec.ComparatorSet`.
* CPM compares the two profiles and returns a set of relation tokens (e.g., “not worse”, “incomparable under evidence”, “abstain”), rather than forcing a numeric margin.
* The audit records the effective comparator edition and evidence policy, so later readers can reproduce *why* a comparison abstained or degraded (instead of mistaking “missing evidence” for “equality”).

### A.19.CPM:6 - Bias-Annotation — informative

CPM is a comparison *kernel*; it does not remove bias by itself, but it prevents the most common bias‑amplifying failure modes (hidden thresholds, hidden tie‑breakers, unknown coercion).

Typical bias risks and mitigations:

* **Comparator choice encodes value judgments.** Weights, priority orders, thresholds, and “tie‑break” conventions can encode organizational bias. CPM forces these to live in explicit, edition‑pinned `ComparatorSpec`/policy artifacts rather than in invisible code or informal reasoning.
* **Missing evidence is rarely random.** If evidence is systematically missing for certain contexts/groups, naive “unknown → worse” is a bias amplifier. CPM’s tri‑state guard avoids coercion; but teams must still define policy‑bound failure behavior and be explicit when abstention is acceptable.
* **Cross‑context comparisons can embed structural unfairness.** CPM enforces bridge‑only transport and penalty routing (`R_eff` only), making “comparisons across worlds” explicit instead of silently assuming commensurability.
* **Overconfidence via scalarization.** Collapsing partial orders into scalars often overstates certainty and hides tradeoffs. CPM makes set‑valued outcomes first‑class, so the human/managerial decision can remain honest about tradeoffs.

### A.19.CPM:7 - Conformance Checklist

A CPM publication / usage is conformant if it satisfies the checks below (these complement `CC‑UM.*` and the CHR suite obligations in `A.19.CHR:4.3`):

| Check Id | Requirement (normative) | Notes (didactic / evidence) |
| :--- | :--- | :--- |
| **CC‑A19CPM‑0** | **Mechanism.Intension completeness.** The publication includes the full intension shape (header/imports/subject/slot index/op algebra/laws/admissibility/applicability/transport/time/plane/audit) and uses tri‑state guards. | SlotIndex is **derived**; see `A.6.5` + `CC‑UM.*`. |
| **CC‑A19CPM‑1** | **Single owner.** The canonical CPM intension is owned here (`A.19.CPM:4.1`); other mentions are **Tell + Cite** stubs only. | Prevents “two near‑identical cards” drift. |
| **CC‑A19CPM‑2** | **Suite stage alignment.** `Compare` is the canonical stage‑op for CHR stage `compare`; ordering/optionality is taken only from `A.19.CHR:4.5`. | Never infer order from `mechanisms[]`. |
| **CC‑A19CPM‑3** | **SlotKind discipline.** SlotKind tokens follow the suite lexicon (`A.19.CHR:4.2.1`). | No SlotKind drift across specializations/wiring. |
| **CC‑A19CPM‑4** | **Comparator legality gate.** `ComparatorSpecSlot ∈ CGSpecSlot.ComparatorSet` is enforced (fail‑closed otherwise). | Legality is declared, not improvised. |
| **CC‑A19CPM‑5** | **Scale legality.** Any numeric operations implied by the comparator are admissible under `CGSpecSlot.SCP` and CSLC‑lawful. | “Weighted sum” etc must be explicitly lawful. |
| **CC‑A19CPM‑6** | **Set‑valued semantics.** Outputs remain set‑valued; no silent scalarization or totalization is introduced. | Incomparability/ties are first‑class outcomes. |
| **CC‑A19CPM‑7** | **Tri‑state admissibility (fail‑closed).** `CompareEligibility(...) → {pass|degrade|abstain}` exists and does not return `pass` on missing legality/evidence. | Unknown never coerces to `pass`. |
| **CC‑A19CPM‑8** | **MinimalEvidence defaulting is explicit.** If `MinimalEvidenceSlot?` is absent, the effective evidence policy is `CGSpecSlot.MinimalEvidence` by explicit rule. | Avoid “implicit evidence policy.” |
| **CC‑A19CPM‑9** | **Gate/guard separation + lexeme discipline.** CPM does not publish `GateDecision` nor `DecisionLog`; mechanism predicates use `…Eligibility` (not reserved gate `…Guard`). | Aligns with suite obligations (`gate_decision_separation`, `guard_lexeme_reservations`). |
| **CC‑A19CPM‑10** | **Transport / plane discipline.** Crossings are Bridge+CL/ReferencePlane only; penalties route to `R_eff` only; plane crossings use `CL^plane` when needed. | Keep cross‑world comparisons explicit. |
| **CC‑A19CPM‑11** | **Audit completeness.** Audit records `CNSpecRef.edition`, `CGSpecRef.edition`, effective `ComparatorSpecRef@edition`, and the effective evidence policy (override or cited default). | SHOULD record GuardDecision + crossing ids. |
| **CC‑A19CPM‑12** | **P2W separation.** Editions/policy‑ids are bound only in planned baseline artefacts; CPM records effective refs/pins in Audit and does not bind them. | Planned baseline = A.15.3 + suite PlanItem. |
| **CC‑A19CPM‑13** | **No implicit UNM.** CPM never performs silent normalization; normalization‑based comparability requires explicit upstream UNM witness (or `abstain/degrade`). | Keeps “compare‑on‑invariants” explicit. |

### A.19.CPM:8 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern: “Comparison returns a score.”**
  *Symptom:* `Compare(x,y)` returns a numeric margin or a single rank position.
  *Avoid:* keep numeric scoring in `USCM`; CPM returns relation tokens (set‑valued). If a numeric comparator is desired, it must be an explicit `ComparatorSpec` and still yields relation tokens as the kernel output.

* **Anti‑pattern: “CPM picks the winner.”**
  *Symptom:* comparison logic embeds winner selection or portfolio truncation.
  *Avoid:* CPM only compares; selection is `SelectorMechanism`, which consumes comparison outcomes and remains policy‑bound.

* **Anti‑pattern: “Comparator by prose / by code default.”**
  *Symptom:* comparator choice is implicit (e.g., “we usually do lexicographic by safety then cost”), not edition‑pinned.
  *Avoid:* require an explicit `ComparatorSpecRef` from `CG‑Spec.ComparatorSet` and record it in Audit.

* **Anti‑pattern: “GateDecision leakage.”**
  *Symptom:* the `compare` step emits/assumes `GateDecision`/GateLog/DecisionLog artifacts as part of suite closure, or uses reserved gate‑lexemes (`…Guard`) for mechanism‑level predicates.
  *Avoid:* keep CPM at guard+audit level (`…Eligibility → GuardDecision ∈ {pass|degrade|abstain}`); route gate decisions to their proper owners and keep publish/telemetry outside suite closure.

* **Anti‑pattern: “SlotKind drift.”**
  *Symptom:* renaming/re‑purposing `LeftProfileSlot/RightProfileSlot/ComparatorSpecSlot/ComparisonResultSlot` across specializations or across CHR layers.
  *Avoid:* use the suite SlotKind lexicon (`A.19.CHR:4.2.1`) and keep SlotIndex as a derived projection.

* **Anti‑pattern: “Smuggling plan‑binding into CPM.”**
  *Symptom:* hard‑coding comparator editions, policy ids, or “launch values” inside the CPM intension/pattern prose.
  *Avoid:* bind editions/policies only in P2W planned baseline artefacts; keep CPM refs‑only and record effective bindings in `Audit`.

* **Anti‑pattern: “Tie‑breakers as hidden constants.”**
  *Symptom:* forced total order via untracked thresholds, epsilons, or “if equal then compare cost” logic.
  *Avoid:* make tie‑break policy part of explicit comparator/acceptance policies; pin editions; audit.

* **Anti‑pattern: “Unknown coerces to outcome.”**
  *Symptom:* missing evidence treated as equal/zero/worse, producing decisive comparisons from absent information.
  *Avoid:* tri‑state guard; fail‑closed on missing evidence; explicit failure behavior via evidence policy.

* **Anti‑pattern: “Cross‑context compare without transport.”**
  *Symptom:* comparing profiles across contexts/planes without Bridge+CL/ReferencePlane discipline.
  *Avoid:* use transport mechanisms and crossing pins; penalties route to `R_eff` only; audit crossing ids.

### A.19.CPM:9 - Consequences

* **Improved usability (didactic):** CPM gives a single, engineer‑readable place to learn “what lawful comparison means” and what it does *not* mean.
* **Higher auditability:** comparison outcomes can be traced to comparator edition, legality surfaces, and evidence policies.
* **Reduced semantic drift:** teams cannot silently shift from Pareto to lexicographic to “weighted sum” without changing explicit comparator specs and pins.
* **Explicit tradeoffs:** set‑valued outcomes force downstream reasoning to acknowledge incomparability and uncertainty rather than hiding them.
* **Cost:** downstream consumers (notably selection) must handle sets, abstentions, and partial orders explicitly. This is intentional: it moves complexity from hidden heuristics into explicit policy‑bound mechanisms.

### A.19.CPM:10 - Rationale

1. **Set‑valued by design:** partial orders are common in multi‑criteria settings; pretending they are total creates false certainty and brittle decisions.
2. **ComparatorSet gating:** declaring what comparisons are legal (and under what scale/evidence rules) prevents “algorithm by convenience”.
3. **Tri‑state guards:** explicit `pass|degrade|abstain` preserves epistemic honesty: unknown is not silently converted into an outcome.
4. **Strict distinction:** separating compare from score and select prevents hidden semantic coupling and improves evolvability (methods change via wiring; kernel stays stable).
5. **Single‑owner canonicalization:** keeping one semantic owner eliminates “multiple near‑identical cards” that drift apart and destroy usability.

### A.19.CPM:11 - SoTA-Echoing

**SoTA vs popular note.** This section records alignment to post‑2015 evidence‑backed practice. It is **not** a mandate to use fashionable methods; method semantics stay in SoTA packs (`G.2`) and wiring modules, while this pattern fixes the stable CPM mechanism boundary.

**Pack note (Phase‑3).** If/when a CPM‑specific `G.2` SoTA pack/ClaimSheet is introduced, prefer citing the pack’s `ClaimSheetId`(s) over raw bibliographic pointers below, keeping CPM’s kernel semantics unchanged.

| SoTA practice pointer (post‑2015)                                                                                                   | How it connects to CPM                                                                                                                                           | Adoption status in FPF                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Fair ranking / constrained ranking** (e.g., Zehlike et al., 2017; Biega et al., 2018)                                             | Reinforces the “no hidden tie‑breaks/thresholds” stance: fairness constraints belong in explicit comparator/acceptance policies, not as silent kernel constants. | Integrate via `ComparatorSpec` editions in `CG‑Spec.ComparatorSet` + policy pins; CPM remains unchanged.              |
| **Uncertainty‑aware / set‑valued inference** (e.g., Romano et al., 2019; Barber et al., 2021)                                       | Supports “comparison may abstain” and “set‑valued outcomes are honest”: uncertain profiles should not be coerced into point‑comparisons.                         | Model as comparator families (or supporting method families) packaged in `G.2`; wired into declared `ComparatorSpec`. |
| **Differentiable sorting / learned comparators** (e.g., Grover et al., 2019; Blondel et al., 2020)                                  | When comparators are learned, explicit comparator specs and edition pins become even more critical for auditability and drift control.                           | Treated as method implementations behind `ComparatorSpec` (wiring‑only in Part G); CPM kernel stays stable.           |
| **Robust multi‑criteria decision support under partial orders** (modern robust outranking / preference‑learning variants post‑2015) | Emphasizes preserving incomparability and explicitly encoding thresholds/preferences as declared artifacts.                                                      | Packaged as comparator families; legality and evidence remain gated by `CG‑Spec`.                                     |

### A.19.CPM:12 - Relations

**Builds on / cites (non‑exhaustive):**

* `A.6.1` (shape of `U.Mechanism.Intension`; specialization discipline)
* `A.6.5` (slot discipline; SlotIndex as derived projection)
* `A.19.CHR` (suite membership + obligations + `suite_protocols`; CHR SlotKind lexicon)
* `A.15.3` + `A.19.CHR:4.7.2` (P2W planned baseline binding; CPM remains refs‑only w.r.t. pin binding)
* `A.19.CN` (CN‑Spec comparability routing + acceptance/admission surfaces)
* `G.0` (CG‑Spec: `ComparatorSet`, `SCP`, `MinimalEvidence`, CL/ReferencePlane framing)
* `A.18` (CSLC scale lawfulness)
* `E.10` (lexical/ontological authoring rules; kind suffix discipline)
* `E.19` (checks; authoring discipline)
* `E.20` (single‑owner discipline)
* `F.18` (alias docking; ID continuity)
* `E.18 (E.TGA)` (project transduction graphs consume CPM instances; CPM does not create a parallel “card deck”)

**Relates to (typical neighbors in CHR Uses contour):**

* `UNM.IntensionRef`, `UINDM.IntensionRef`, `USCM.IntensionRef`, `ULSAM.IntensionRef`, and `SelectorMechanism.IntensionRef` (downstream consumer of CPM results).
* `G.5` (selection conformance), `G.9` (parity / benchmark harness), `G.10`/PTM (publish/telemetry outside suite closure).

### A.19.CPM:End

## A.19.SelectorMechanism - Unified Selection Kernel, SelectorMechanism

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A / CN‑Spec cluster (A.19) / CHR mechanism owner patterns (Phase‑3)
> **Source:** FPF / CHR Phase‑3 mechanism owner patterns
> **Modified:** 2026‑01‑20
>
> **Semantic owner note (Phase‑3 canonicalization):** this pattern is the **designated single semantic owner** of the canonical `U.Mechanism.Intension` for `SelectorMechanism.IntensionRef` (CHR suite stage `select`). This matches the “single‑owner route map” discipline (`E.20:4.2`): mechanism‑intension semantics live in an explicitly designated mechanism‑owner pattern.
> `A.6.1` remains the owner of the **template** of `U.Mechanism.Intension` and the `U.MechAuthoring` discipline; this pattern owns the **SelectorMechanism‑specific** slots/ops/laws/admissibility/applicability/transport/plane/time/audit obligations for that template (single‑owner at the instance‑semantics level).
>
> **ID continuity note.** When migrating away from any legacy “card location”, preserve public anchors: keep the legacy section heading/ID as a **Tell + Cite stub** (or dock aliases via `F.18`) rather than deleting or silently renaming it.
>
> **Canonicalization hook (ID‑continuity‑safe):** any other appearances of the SelectorMechanism intension content (e.g., a legacy grounding stub in `A.6.1` or suite prose in `A.19.CHR`) SHALL be reduced to a **Tell + Cite** stub pointing to **`A.19.SelectorMechanism:4.1`**, while preserving the original section headings and their public `PatternId:SectionPath` IDs for continuity (alias‑dock legacy tokens rather than deleting them).
> Such stubs MUST NOT restate SlotIndex / OperationAlgebra / LawSet / Admissibility / Audit content (no “second center of gravity” via near‑duplicate prose).
> * **ID‑continuity‑safe:** if content is moved from an earlier location, preserve the earlier heading and its IDs as a stub that cites `A.19.SelectorMechanism:4.1`.
> * **Alias‑dock, don’t break:** if any legacy tokens exist (e.g., a historical `UNSELM` name token), dock them via `F.18` + E.10 rules; do not mint a competing head.
> * **No shadow semantics:** derived summaries MAY be informative, but MUST NOT restate SlotIndex / OperationAlgebra / LawSet / Admissibility / Audit; they may only summarise and cite.

### A.19.SelectorMechanism:0 - At a glance — didactic, informative

* **What it is:** a universal **set‑returning** selection kernel: it takes candidates, lawful comparison outcomes, and explicit criteria, and returns a **portfolio set**, not a forced single winner.
* **What it is not:** it is not a hidden scoring model, not a comparator, not a gate, and not a telemetry or publishing step.
* **Why it exists:** to prevent three recurring failure modes: **hidden thresholds**, **silent scalarization**, and **winner‑take‑all defaults** under partial orders and uncertain evidence.
* **How it evolves:** method semantics and SoTA algorithm families connect via `G.2` packs and wiring modules; the kernel signature stays stable and teachable.
* **Suite stage:** `select` (ordering lives only in `A.19.CHR:4.5` / `suite_protocols`; suite membership is a set in `A.19.CHR:4.2`).
* **Inputs (conceptual):** `CandidateSetSlot` + `ComparisonResultSlot` (lawful relation/poset tokens, typically produced by `CPM`) + `CriteriaSlot` + `CNSpecSlot` + `CGSpecSlot` + `ContextSlot` (+ `TaskSignatureSlot?`, + `MinimalEvidenceSlot?` override).
* **Output (conceptual):** `SelectionSlot` = portfolio set (a singleton is allowed **only** when explicitly demanded by criteria or by an explicitly declared upstream total order).
* **Non‑goals:** does **not** normalize (UNM), indicatorize (UINDM), score (USCM), fold (ULSAM), compare (CPM), define acceptance thresholds, publish, or emit telemetry; it is a selection step over already‑lawful inputs.
* **P2W seam:** concrete edition/policy pin bindings (e.g., `TaskSignatureRef@edition(…)`, `CGSpecRef@edition(…)`, evidence overrides) are chosen in planned baseline artefacts (`A.15.3` + `A.19.CHR:4.7.2`); executions only record effective refs/pins in `Audit`.
* **TGA use:** when used as a node type in `E.18 (E.TGA)`, selector instances are chosen in planned baseline artefacts (P2W); this pattern owns the intension that those instances cite.
* **Failure mode:** tri‑state guard (`pass|degrade|abstain`); missing/unknown evidence never coerces to `pass`.
* **Mental model:** `SelectEligibility` gates the step; `Select` applies explicit criteria to set‑valued comparison outcomes; the result is a portfolio set whose “single winner” behavior must be explicit.

---

### A.19.SelectorMechanism:1 - Problem frame

FPF’s Characterization (CHR) suite treats selection as a **distinct mechanism boundary** within the suite (authoritative membership: `A.19.CHR:4.2`).
Suite membership is a **set**; order has no semantics. Any intended ordering is expressed only via `suite_protocols` (`A.19.CHR:4.5`), under suite obligations (`A.19.CHR:4.3`).

Within the suite‑closed protocol, `SelectorMechanism` appears as the `select` stage (after lawful comparison; optional stages remain explicitly optional per `suite_protocols`). The kernel’s role is concept‑level and contract‑bound:

* consume **lawful** comparison outcomes without collapsing them into a hidden scalar,
* apply **explicit** criteria and policy routing, and
* return a **set/portfolio** result whose defaults are policy‑bound and auditable.

The kernel uses the CHR suite SlotKind lexicon (`A.19.CHR:4.2.1`) to prevent SlotKind drift across specializations and across SoTA wiring layers.

---

### A.19.SelectorMechanism:2 - Problem

Engineering teams regularly need to make “a selection decision” under conditions that are normal in real projects:

* comparisons are partial, multi‑criteria, or set‑valued,
* evidence is incomplete or policy‑gated, and
* different stakeholders ask for different “best” notions.

If selection is not a first‑class mechanism boundary with stable semantics, the same high‑risk drift happens repeatedly:

* **Silent winner forcing:** partial orders get collapsed to a single winner by ad‑hoc tie‑breakers or hidden weights.
* **Hidden thresholds and constants:** thresholds, weights, dominance regimes, and “default portfolio modes” get smuggled into implementations and become invisible in discussion and audit.
* **Scalarization by convenience:** set‑valued comparison outcomes get replaced by a scalar “score summary” that is treated as decision‑relevant without being declared as such.
* **Evidence coercion:** missing or unknown evidence gets treated as “good enough” (implicit pass) rather than routing to explicit `degrade` or `abstain`.
* **Boundary erosion:** selection quietly performs comparison, scoring, aggregation, or publishing, making the CHR pipeline opaque and hard to reason about.

---

### A.19.SelectorMechanism:3 - Forces

1. **Set‑valued reality vs single‑winner convenience.** Many lawful comparisons are partial orders. The kernel must preserve set‑valued semantics while still allowing single‑winner outcomes when explicitly requested by criteria.

2. **Policy primacy vs method freedom.** Criteria and defaults must be explicit and policy‑bound, while multiple method families and decision styles must remain add‑able without mutating the kernel.

3. **No hidden thresholds vs usability pressure.** Engineers often want “just pick one.” If the spec does not constrain this, hidden thresholds and tie‑breakers become de facto policy.

4. **Evidence discipline vs delivery pressure.** Under uncertainty, teams default to coercion (unknown → pass). The kernel must enforce tri‑state eligibility and fail‑closed discipline.

5. **Auditability vs conceptual minimalism.** FPF stays conceptual. Audit obligations must be minimal yet decisive: editions and effective policy routing must be visible without introducing tool‑level governance.

6. **Evolvability vs didactic usability.** The kernel must be stable enough to support SoTA wiring and specialization ladders, but also teachable: one place to learn the boundary, laws, guard behavior, and audit minimum.

7. **P2W separation and gate/guard separation.** Planned binding of fillers and pins lives in WorkPlanning (P2W). Selection must not mutate into a gate pattern: no `GateDecision` or decision logs inside the mechanism boundary.

8. **No competing defaults.** If defaults exist (for portfolio mode, dominance regime, archive policies), they must be cited from their declared single sources, not replicated or re‑declared inside the kernel (`A.19.CHR:4.3.5`).

---

### A.19.SelectorMechanism:4 - Solution

`SelectorMechanism` is the canonical **selection kernel** for CHR and for selector specializations. It provides:

* a stable mechanism boundary for `select`,
* a stable SlotKind surface (via the CHR lexicon),
* a minimum law set that preserves set‑valued semantics and forbids hidden thresholds and hidden scalarization,
* a tri‑state admissibility guard that is fail‑closed under missing legality or evidence,
* an audit minimum that records effective editions and policy routing.

Method semantics and SoTA algorithm families do not live inside the kernel: they connect via `G.2` SoTA packs and wiring modules, and via lawful specializations `⊑/⊑⁺` that obey the ladder discipline (`A.6.1:4.2.1`).

#### A.19.SelectorMechanism:4.1 - Mechanism.Intension — normative core

Archetypal Grounding — **Mechanism.Intension** (normative).

* **Scope note:** this intension is an **instance** authored to the `U.Mechanism.Intension` shape owned by `A.6.1`. It defines only the mechanism’s semantic surface (slots/ops/laws/guards/audit). It does **not** bind project‑specific pins (P2W), and it does **not** emit GateDecision/GateLog; it emits `Audit` pins and a tri‑state guard only.
* **Canonicality note:** this is the canonical `U.Mechanism.Intension` for `SelectorMechanism.IntensionRef` and is intended to be cited by CHR suite artefacts and by any wiring layers; other mentions are **Tell + Cite** only.

* **IntensionHeader:** `id = SelectorMechanism`, `version = 1.0.0`, `status = stable`.

* **IntensionRef:** `SelectorMechanism.IntensionRef` (canonical target for the suite member named in `A.19.CHR:4.2`).

* **Tell.** Universal set‑returning selection kernel over candidates and criteria; defaults remain policy‑bound; **no hidden thresholds**.

* **Purpose:** universal set‑returning selection kernel over candidates and criteria; defaults remain policy‑bound; **no hidden thresholds**.

* **Imports:** `A.6.1:4.2.1 (multi-level specialisation ladders)`, `A.6.5 (slot discipline; SlotIndex as projection)`, `A.19.CN (CN‑Spec contract surface)`, `C.22 (TaskSignature as a policy routing surface when used)`, `G.5 (selector conformance and default routing)`, `G.0 (CG‑Spec legality and evidence gates)`, `A.19.CHR:4.2.1 (CHR SlotKind Lexicon)`.

* **SubjectBlock:**

  * **SubjectKind:** `Selection`.
  * **BaseType:** `U.Set (candidates) + U.RelationTokenSet (lawful comparison outcomes)`.
  * **SliceSet:** `U.ContextSliceSet`.
  * **ExtentRule:** selection ranges over admitted candidates in the active context slice, constrained by explicit criteria/policies and by lawful comparison outcomes.
  * **ResultKind?:** `U.Set`.

* **SlotIndex:** derived projection from `SlotSpecs` (and any guard‑only SlotSpecs) per slot discipline; uses `A.19.CHR:4.2.1` SlotKind tokens; has no independent semantics.

  * `CandidateSetSlot : ⟨ValueKind = U.Set (candidates), refMode = ByValue⟩`.
  * `ComparisonResultSlot : ⟨ValueKind = U.Set (relation/poset tokens), refMode = ByValue⟩`.
  * `CriteriaSlot : ⟨ValueKind = U.Set (selection criteria / clauses, incl. explicit tie‑breakers; **acceptance thresholds are not criteria** and remain owned by the cited acceptance surfaces and applied only via `SelectEligibility`), refMode = ByValue⟩`.
  * `TaskSignatureSlot? : ⟨ValueKind = TaskSignature, refMode = TaskSignatureRef⟩` optional; when present, SHOULD be the single routing surface for selector defaults (e.g., portfolio mode / dominance regime), but it does not replace `CNSpecSlot` / `CGSpecSlot` contract surfaces.
  * `CNSpecSlot : ⟨ValueKind = CN‑Spec, refMode = CNSpecRef⟩`.
  * `CGSpecSlot : ⟨ValueKind = CG‑Spec, refMode = CGSpecRef⟩`.
  * `ContextSlot : ⟨ValueKind = U.BoundedContext, refMode = U.BoundedContextRef⟩`.
  * `MinimalEvidenceSlot? : ⟨ValueKind = MinimalEvidence, refMode = MinimalEvidenceRef⟩` optional override; otherwise the effective evidence policy is `CGSpecSlot.MinimalEvidence`.
  * `SelectionSlot : ⟨ValueKind = U.Set (portfolio), refMode = ByValue⟩`.

* **OperationAlgebra** suite stage = `select`, per `A.19.CHR:4.5`; canonical stage op = `Select`

  * `Select(CandidateSetSlot, ComparisonResultSlot, CriteriaSlot, CNSpecSlot, CGSpecSlot, ContextSlot, TaskSignatureSlot?, MinimalEvidenceSlot?) → SelectionSlot`.

* **LawSet** (minimum): the selection kernel is set‑returning and policy‑bound

  1. **Set‑returning by default:** a conformant `Select` MUST return a set/portfolio by default. It MUST NOT silently collapse partial orders or incomparabilities to a single winner; if a singleton outcome is required, it MUST be an explicit criterion (or a declared upstream total order).
  2. **No hidden thresholds/constants:** a conformant publication MUST NOT smuggle thresholds, weights, dominance rules, or tie‑breakers. Selection‑level commitments MUST be explicit in `CriteriaSlot` and/or in explicit policy routing surfaced by `TaskSignatureSlot`. Admissibility/acceptance thresholds are applied only via `SelectEligibility` using `CNSpecSlot.acceptance` and the effective evidence policy (`MinimalEvidenceSlot?` or `CGSpecSlot.MinimalEvidence`).
  3. **No hidden scalarization:** a conformant publication MUST consume `ComparisonResultSlot` as set‑valued/partial when it is set‑valued/partial. Scalar summaries (if produced at all) are report‑only unless explicitly promoted by policy outside suite closure.
  4. **Evidence gating is explicit:** when selection depends on evidence, it MUST cite either `MinimalEvidenceSlot` (override) or the effective policy `CGSpecSlot.MinimalEvidence`, and it MUST route the operation through tri‑state guards (no unknown coercion). Any candidate‑level ineligibility handling MUST be explicit (criteria and/or upstream outputs) and auditable (no silent dropping); the kernel MUST NOT invent new evidence thresholds.
  5. **No competing defaults:** portfolio/dominance defaults (when relevant) MUST be sourced from their declared single owners (typically via `TaskSignatureSlot` routing and/or the selector conformance/default surfaces in `G.5`), and MUST NOT be re‑declared inside the kernel.

* **AdmissibilityConditions** (tri‑state guard; fail‑closed on missing legality or evidence)

  * `SelectEligibility(CandidateSetSlot, ComparisonResultSlot, CriteriaSlot, CNSpecSlot, CGSpecSlot, ContextSlot, TaskSignatureSlot?, MinimalEvidenceSlot?) → GuardDecision ∈ {pass|degrade|abstain}`.
  * `pass` requires at minimum: (i) `ComparisonResultSlot` is compatible with `CandidateSetSlot` (same candidate universe), (ii) all selection criteria and any tie‑breakers are explicit (via `CriteriaSlot` and/or `TaskSignatureSlot`), (iii) admissibility/acceptance gates (`CNSpecSlot.acceptance`, evidence) do not fail, and (iv) `CNSpecSlot` and `CGSpecSlot` are coherent for the comparison tokens being consumed (no mixed contract surfaces).
  * If `MinimalEvidenceSlot` is absent, `SelectEligibility` MUST evaluate evidence against `CGSpecSlot.MinimalEvidence` by explicit rule, and missing/unknown evidence MUST NOT yield `pass`.
  * `degrade` is permitted only when an explicit, auditable failure behavior exists (policy‑bound), e.g., “exclude ineligible candidates” or “sandbox/probe‑only”; `abstain` is used when selection cannot proceed lawfully under the declared criteria/policies.

* **Applicability:**

  * Intended as the last stage of CHR selection after lawful comparison, producing a portfolio‑valued result.
  * Cross‑context selection is allowed only via explicit Transport (Bridge+CL/ReferencePlane) and cannot bypass CG‑Spec legality.

* **Transport:** declarative‑only: no embedded CL/Φ/Ψ tables and no new transport edges; crossings are via cited Bridge+CL/ReferencePlane surfaces; penalties route to **`R_eff` only**.

* **Γ_timePolicy:** `point` by default, no implicit latest.

* **PlaneRegime:** declarative‑only; does not introduce plane crossings. If selection spans planes, it MUST cite the applicable **ReferencePlane** and **CL^plane** policy; penalties route to **`R_eff` only**.

* **Audit:**

  * Must record: `CNSpecRef.edition`, `CGSpecRef.edition`.
  * If `TaskSignatureSlot?` is present, must record `TaskSignatureRef.edition`.
  * If `MinimalEvidenceSlot?` is present, must record `MinimalEvidenceRef`; otherwise must cite `CGSpecSlot.MinimalEvidence` as the effective evidence policy.
  * SHOULD record: the realized `GuardDecision` (`pass|degrade|abstain`) and, when non‑`pass`, the policy‑bound failure behavior reference that justified it.
  * SHOULD record: a stable identity for `CandidateSetSlot` and `ComparisonResultSlot` **or** a citable upstream `Audit` anchor that already fixes these identities; the goal is traceability without duplicating upstream semantics.
  * MUST record: a stable identity for `SelectionSlot`.
  * SHOULD record: a stable description (or citable reference) for the effective selection criteria surface (e.g., criteria artefact ids when criteria are reference‑backed; `TaskSignatureRef` when used).
  * SHOULD record: the realized routing‑relevant selector defaults (e.g., portfolio mode / dominance regime) **when** they are not fully determined by a referenced `TaskSignatureRef` or an explicit CAL policy surface; the point is auditability, not re‑declaring defaults.
  * SHOULD record: any Bridge/CL/ReferencePlane ids when `Transport` was invoked.

#### A.19.SelectorMechanism:4.2 - Boundary and layering rules

1. **Selection consumes upstream CHR products, it does not invent them.** `ComparisonResultSlot` is an input: the kernel MUST NOT perform normalization (UNM), indicatorization (UINDM), scoring (USCM), folding (ULSAM), or comparison (CPM) inside `Select`. If a scalar “overall score” is desired, it must be declared upstream as a lawful scoring and/or comparator choice, not invented inside selection.

2. **Threshold discipline (acceptance ≠ selection).** Acceptance/admission thresholds are not selection criteria: they live in `AcceptanceClauses` / `TaskSignature` / `GateProfile` surfaces per `A.19.CHR:4.3.5` and are applied only via `SelectEligibility`. Selection‑level tie‑breakers and portfolio constraints MAY exist, but MUST be explicit and auditable (typically as criteria artefacts or explicit policy routing), never as unnamed constants.

3. **Report‑only summaries inside suite closure.** Any scalar summaries, illumination metrics, or auxiliary “why not chosen” telemetry are report‑only unless explicitly promoted by policy, and MUST NOT be used as hidden dominance rules (`A.19.CHR:4.3.3`).
   Publishing and telemetry remain outside suite closure and are routed via established publication surfaces (e.g., `G.10` and/or `PTM`), not as hidden tails inside selection.

4. **Specializations are explicit and disciplined.** Any refinement or extension of `SelectorMechanism` must follow `A.6.1:4.2.1`:

   * SlotKind invariance for inherited operations,
   * no new mandatory inputs to inherited `Select`,
   * added capabilities appear as new operations or as `⊑⁺` extensions.

5. **P2W seam is preserved.** Planned bindings for `TaskSignatureRef@edition`, `CGSpecRef@edition`, evidence policy overrides, and other pins live in WorkPlanning (P2W). Execution visibility is via `Audit`, not by mutating plan objects at run time.

---

### A.19.SelectorMechanism:5 - Archetypal Grounding — informative

#### A.19.SelectorMechanism:5.1 - Tell

When comparisons are partial or set‑valued, selection must not pretend there is a single “best” by default. `SelectorMechanism` makes selection explicit, policy‑bound, and auditable: it returns a **set** unless criteria explicitly demand otherwise.

#### A.19.SelectorMechanism:5.2 - Show, U.System example

**Scenario.** A platform team must pick a set of deployment options for a subsystem under multiple criteria: latency, cost, and regulatory risk. Comparisons are multi‑criteria and do not induce a total order.

* `CandidateSetSlot` = `{OptionA, OptionB, OptionC}`
* `ComparisonResultSlot` includes tokens such as:

  * `OptionA ≼ OptionB` on latency,
  * `OptionB ≼ OptionA` on cost,
  * `OptionC` incomparable with both on risk evidence (missing attestations).
* `CriteriaSlot` contains explicit clauses:

  * “return all non‑dominated candidates under ParetoOnly,”
  * “candidates missing required evidence must not pass.”
* `MinimalEvidenceSlot?` is absent, so evidence is evaluated against `CGSpecSlot.MinimalEvidence`.

**Outcome.**

* `SelectEligibility` returns `degrade` (or `abstain`, depending on the declared failure behavior) **because** `OptionC` fails evidence gating; selection excludes `OptionC` under an explicit policy route rather than coercing unknowns.
* `SelectionSlot` returns `{OptionA, OptionB}` as a portfolio set, rather than forcing a single winner.
* `Audit` records `CGSpecRef.edition`, the effective evidence policy, and the stable identity of the selected portfolio.

#### A.19.SelectorMechanism:5.3 - Show, U.Episteme example

**Scenario.** A methods group selects a portfolio of analysis methods for a task. Candidates are method family refs. The group wants diversity in the portfolio, but does not want diversity metrics to silently become dominance criteria.

* `CandidateSetSlot` = `{Family1, Family2, Family3, Family4}`
* `ComparisonResultSlot` is produced by lawful comparison on declared indicators and evidence gates.
* `TaskSignatureSlot` is present and is the single routing surface for policy defaults:

  * portfolio mode and dominance regime,
  * budgeting/telemetry hooks (when used).
* `CriteriaSlot` declares that diversity signals are telemetry unless explicitly promoted by policy.

**Outcome.**

* `SelectionSlot` returns a portfolio set; any archive‑style behavior is a specialization and policy choice, not a hidden kernel default.
* `Audit` records `TaskSignatureRef.edition`, enabling reproducibility and post‑hoc explanation without embedding tool tokens into the kernel.

---

### A.19.SelectorMechanism:6 - Bias-Annotation — informative

This pattern intentionally biases selection authoring toward explicitness and legality.

* **Governance bias.** Bias toward explicit criteria and policy routing surfaces rather than implicit constants. Risk: perceived overhead. Mitigation: keep criteria artifacts minimal, and centralize defaults via `TaskSignatureSlot` when used.
* **Architecture bias.** Bias toward set‑return semantics and against forced total orders. Risk: consumers may expect a single winner. Mitigation: make single‑winner selection an explicit criterion or a declared comparator outcome, not an implicit kernel behavior.
* **Epistemic bias.** Bias toward fail‑closed evidence handling and against unknown coercion. Risk: more `degrade/abstain` early. Mitigation: improve evidence pins and policy clarity; do not relax the kernel.
* **Practice bias.** Bias against embedding telemetry and publishing into selection. Risk: teams want a one‑stop “select and report.” Mitigation: keep reporting in post‑suite routing patterns and record only minimal audit pins here.
* **Didactic bias.** Bias toward one semantic owner and “Tell + Cite” elsewhere. Risk: refactoring work. Mitigation: the result is a spec that can be read and taught without scavenger hunts.

---

### A.19.SelectorMechanism:7 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑A19SelectorMechanism‑0** | **MechAuthoring discipline:** the canonical SelectorMechanism `Mechanism.Intension` in `A.19.SelectorMechanism:4.1` MUST satisfy `A.6.1` `U.MechAuthoring` and the relevant `CC‑UM.*` checks; this pattern does not override the `U.Mechanism.Intension` shape. |
| **CC‑A19SelectorMechanism‑1** | **Single owner:** the canonical SelectorMechanism `U.Mechanism.Intension` MUST be owned by `A.19.SelectorMechanism:4.1`. Any other SelectorMechanism “card” text MUST be reduced to Tell+Cite referencing this owner section. |
| **CC‑A19SelectorMechanism‑2** | **Set‑return default:** a conformant `Select` MUST be set‑returning by default; it MUST NOT silently collapse partial orders or incomparabilities to a single winner. |
| **CC‑A19SelectorMechanism‑3** | **No hidden thresholds/constants:** a conformant SelectorMechanism publication MUST NOT smuggle thresholds, weights, dominance rules, tie‑breakers, or default portfolio modes. Selection‑level commitments MUST be explicit in `CriteriaSlot` and/or explicit policy routing (e.g., via `TaskSignatureSlot`). Acceptance thresholds remain owned by `AcceptanceClauses` / `TaskSignature` / `GateProfile` surfaces and MUST be applied only via `SelectEligibility`. |
| **CC‑A19SelectorMechanism‑4** | **No hidden scalarization:** if `ComparisonResultSlot` is set‑valued or partial, a conformant publication MUST consume it as such; scalar summaries are report‑only unless explicitly promoted by policy outside suite closure. |
| **CC‑A19SelectorMechanism‑5** | **Evidence gating:** a conformant publication MUST guard selection via `SelectEligibility` with `GuardDecision ∈ {pass|degrade|abstain}`; missing/unknown evidence MUST NOT yield `pass`. If `MinimalEvidenceSlot?` is absent, the guard MUST evaluate against `CGSpecSlot.MinimalEvidence`. Any candidate‑level filtering triggered by evidence MUST be explicit and auditable, not silent. |
| **CC‑A19SelectorMechanism‑6** | **SlotKind discipline:** SlotKind tokens used in the SelectorMechanism intension MUST come from the CHR SlotKind lexicon (`A.19.CHR:4.2.1`). New SlotKinds require lexicon extension first. |
| **CC‑A19SelectorMechanism‑7** | **Transport discipline:** cross‑context and cross‑plane selection MUST be explicit via Bridge+CL/ReferencePlane; penalties route to `R_eff` only, and crossings MUST be auditable. |
| **CC‑A19SelectorMechanism‑8** | **Audit surface:** Audit MUST record `CNSpecRef.edition`, `CGSpecRef.edition`, and the effective evidence policy (record `MinimalEvidenceRef` when overridden; else cite `CGSpecSlot.MinimalEvidence`); MUST record `TaskSignatureRef.edition` when `TaskSignatureSlot?` is used; and MUST record a stable identity for the resulting `SelectionSlot`. |
| **CC‑A19SelectorMechanism‑9** | **P2W separation:** planned baseline artefacts MUST bind editions and policy pins (A.15.3 + CHR P2W hook); these bindings MUST NOT be invented as run-time decisions inside the suite protocol. |
| **CC‑A19SelectorMechanism‑10** | **Specialization ladder discipline:** any `⊑/⊑⁺` specialization of SelectorMechanism MUST satisfy `A.6.1:4.2.1`, especially SlotKind invariance and “no new mandatory inputs” to inherited `Select`. |
| **CC‑A19SelectorMechanism‑11** | **Guard + gate separation:** `SelectorMechanism` MUST NOT publish `GateDecision`/`DecisionLog`; the mechanism‑level guard is `SelectEligibility` returning `GuardDecision := {pass|degrade|abstain}` and follows guard lexeme reservations (`A.19.CHR:4.3.2`). |
| GateDecision leakage         | `Select` emits `GateDecision` or writes a decision log                          | Keep gate decisions in gate patterns; selection uses `SelectEligibility` + `Audit` pins only                                                       |

---

### A.19.SelectorMechanism:8 - Common Anti-Patterns and How to Avoid Them — informative

| Anti-pattern                 | What it looks like                                                              | Remedy                                                                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Forced single winner         | `Select` always returns exactly one candidate even under incomparability        | Return a portfolio by default; if single winner is required, make it explicit in `CriteriaSlot` and ensure the induced order is lawful and declared |
| Hidden tie-breakers          | “If incomparable, pick lower cost” without declaring that as policy             | Move tie-breakers into explicit criteria or into declared comparator policies; never embed inside the kernel                                        |
| Scalarization by convenience | Replace set-valued comparison with a scalar “summary score” treated as decisive | Keep summaries report-only unless explicitly declared as lawful comparator outputs                                                                  |
| Unknown coerced to pass      | Missing evidence treated as acceptable                                          | Use tri-state `SelectEligibility`; unknown maps to `degrade` or `abstain`                                                                           |
| Selection does comparison    | Selection stage recomputes scoring or comparison internally                     | Keep comparisons upstream; `SelectorMechanism` consumes `ComparisonResultSlot`                                                                      |
| Publish inside selection     | Selection stage emits publish/telemetry as part of the suite step               | Keep publishing and telemetry outside suite closure; record minimal pins in `Audit`                                                                 |

---

### A.19.SelectorMechanism:9 - Consequences

**Benefits**

* Preserves correctness under partial orders by making set‑valued outcomes first‑class.
* Eliminates a major source of decision drift: hidden thresholds, hidden weights, and silent scalarization.
* Improves auditability and teachability: one owner location for selection semantics and its guards.
* Supports evolvability: new method families and selection styles can be wired without changing the kernel signature.

**Costs / trade-offs**

* Portfolio results can require explicit downstream handling when a single decision is needed.
* Strict evidence discipline increases early `degrade/abstain` until criteria and evidence policies are explicit.
* Teams must invest in explicit criteria artifacts instead of relying on implicit conventions.

---

### A.19.SelectorMechanism:10 - Rationale

Selection is where many systems accidentally convert lawful but nuanced information into an unjustified scalar decision. Making selection a separate, explicit mechanism boundary achieves two things that matter for engineering management:

1. **Technical integrity:** it enforces legality and evidence discipline at the decision boundary without smuggling heuristics.
2. **Organizational clarity:** it makes defaults and thresholds discussable, reviewable, and maintainable as explicit policy surfaces.

The set‑returning default is not a “preference for portfolios”; it is a correctness safeguard when the order is not total. Single‑winner outcomes remain possible, but only by explicit criteria or declared lawful comparators.

---

### A.19.SelectorMechanism:11 - SoTA-Echoing

**SoTA vs popular note.** This section records alignment to post‑2015 evidence‑backed practice. It is not a mandate to use fashionable methods; method semantics stay in SoTA packs (`G.2`) and wiring modules, while this pattern fixes the stable selection boundary.

**Pack note, Phase‑3:** this pattern does not currently cite a SelectorMechanism‑specific `G.2` pack or ClaimSheet. If and when such packs are introduced, they should connect via `CriteriaSlot` and `TaskSignatureSlot` routing, keeping kernel semantics unchanged.

#### A.19.SelectorMechanism:11.1 - SoTA alignment map (normative)

| SoTA practice pointer, post‑2015+                                                                               | Primary source examples, post‑2015+                                                                           | Where it connects to SelectorMechanism                                                                             | Adoption status |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------- |
| Treat the Pareto set or portfolio as a first-class output under multi-criteria partial orders                   | Quality Diversity as a decision framing, e.g., Pugh et al. 2016; Vassiliades et al. 2018                      | Expressed as set‑return default and explicit portfolio criteria; method details live in specializations and wiring | Adapt           |
| Use archive-based portfolios where diversity is part of the result, but do not silently promote it to dominance | Modern QD and archive practices post‑2015, including map-elites descendants and archive insertion policies    | Expressed as policy‑bound criteria and report‑only telemetry unless explicitly promoted                            | Adapt           |
| Pair environments and methods in open-ended or co-evolutionary settings without breaking kernel semantics       | Open-ended environment-method pairing, e.g., Wang et al. 2019 and successors                                  | Expressed as candidate and criteria structuring plus lawful specializations; kernel unchanged                      | Adapt           |
| Include an explicit abstain or reject option under uncertainty rather than forcing a decision                   | Selective prediction and rejection-option practice, e.g., Geifman and El‑Yaniv 2017; follow-on selective nets | Expressed as tri-state `SelectEligibility` with fail-closed discipline                                             | Adopt           |
| Keep architecture commitments traceable and single-owner                                                        | ISO/IEC/IEEE 42010:2022 architecture description discipline                                                   | Expressed as explicit semantic ownership and Tell+Cite stubs elsewhere                                             | Adopt           |

**Notes per row** (1–2 sentences; *why* adopt/adapt/reject):
* **Portfolio-as-output (QD framing):** adopt the *decision framing* (portfolio as a first-class result) while keeping concrete QD/portfolio algorithms out of the kernel; they belong in `G.2` packs and wiring modules, preserving evolvability.
* **Archive portfolios (diversity as result):** adapt archive thinking by keeping diversity/illumination signals report‑only unless an explicit CAL/policy promotes them to dominance; this prevents silent scalarization and preserves single‑owner defaults (typically `G.5`/CAL).
* **Open‑ended environment–method pairing:** keep the kernel unchanged; open‑ended pairing is expressed by shaping candidates/criteria (and, when needed, lawful specializations `⊑/⊑⁺`) with explicit edition pins and transfer/validity rules in planned baseline, not by mutating `Select`.
* **Reject/abstain under uncertainty:** adopt the rejection‑option stance as a tri‑state guard with fail‑closed semantics; explicit abstain is preferable to forced choice under missing legality/evidence.
* **Single‑owner architecture discipline:** adopt single‑owner + Tell‑and‑Cite to keep the spec teachable and reviewable; this directly reduces drift and “second centers of gravity”.

---

### A.19.SelectorMechanism:12 - Relations

* **Builds on**

  * `A.6.1` and `CC‑UM.*` for the mechanism intension shape and specialization ladder discipline.
  * `A.19.CHR` for suite membership, suite protocol closure, SlotKind lexicon, and threshold and default discipline.
  * `G.0` for `CG‑Spec` legality and evidence surfaces.
  * `A.19.CN` for `CN‑Spec` contract surfaces used as explicit inputs.
  * `C.22` for `TaskSignature` as a policy routing surface when used.
  * `A.6.5` for slot discipline (SlotIndex as projection; SlotKind invariance).
  * `A.15.3` + `A.19.CHR:4.7.2` for the P2W planned baseline seam for edition/policy pin bindings (cited as seam, not duplicated in Intension).
* **Used by**

  * `A.19.CHR` as the canonical `select` stage in CHR pipelines.
  * `G.5` as the primary conformance and specialization context for selector-based method dispatch and portfolio policies.
  * `E.18 (E.TGA)` when selector instances are used as transduction graph nodes; planned pins live in P2W, effective pins surface via `Audit`.
* **Coordinates with**

  * `CPM` and other lawful comparison stages as producers of `ComparisonResultSlot`.
  * `ULSAM` and other lawful aggregation stages that must remain explicit rather than hidden inside selection.
  * `E.20` single-owner discipline and `F.18` alias docking for Phase‑3 canonicalization and ID continuity.

### A.19.SelectorMechanism:End

## A.20 - U.Flow.ConstraintValidity — Eulerian

**Tech‑name.** `U.Flow.ConstraintValidity` (`U.Flow` genus)
**Plain‑name.** Flow constraint validity (Eulerian interpretation)
**Type / Status.** Architectural pattern — **normative** for flows hosted by E.TGA (E.18) under the Eulerian operational interpretation

### A.20:0 - Intention

**One‑liner** Defines cross‑cutting **ConstraintValidity** rules for all `U.Flow` instances. `U.TransductionFlow` inherits these rules and may refine **CV class specializations** for transduction‑specific semantics (species‑binding only; genus rules remain unchanged). The CV core is **kind‑agnostic** and assumes an **open‑world** catalogue of node **species**; the enumeration of node **kinds** in E.TGA is a **minimal roles baseline**.
**Operational interpretation.** **Eulerian** stance: **flow = valuation** over `U.Transfer`; **CV is attached to transformations (steps)** and evaluated **before any GateFit**; edges carry **assurance‑only operations**; no token‑passing semantics are assumed.

### A.20:1 - Problem frame

E.TGA makes *nodes = morphisms* and enforces a *single edge kind* (`U.Transfer`). **GateFit** checks aggregate only in `OperationalGate(profile)` with the activation predicate **CV ⇒ GF**: until aggregated **ConstraintValidity = pass**, all **GateFit** checks return **abstain**. Equivalently, while **ConstraintValidity ≠ pass**, any GateFit‑oriented explanation **does not apply**. To keep flows comparable and auditable, this pattern delimits **internal step constraints** (CV) from **external gate fit** (GF), preventing any second ladder of processes beside the graph.

### A.20:2 - Problem

Without a clear CV core:

* internal step laws (domains/ranges, invariants, units coherence, Lipschitz/stability) bleed into gate **profile**;
* plane or comparator declarations sneak into mechanisms;
* freshness and design/run concerns appear inside mechanisms;
* reproducibility suffers because transfers start carrying hidden semantics beyond `⟨L,P,E⃗,D⟩`.

Under this pattern, CV is evaluated **inside** transformations. **If** a check declares planes/units/comparators or depends on an active `GateProfile`, **then** it is treated as **GateFit at gates** and the CV explanation **does not apply**.

### A.20:3 - Forces

* **Separation of concerns.** Internal mechanism laws vs. external profile fit.
* **Auditability.** MVPK faces include pins/references only; no new numeric claims; editions and Γ are pinned where applicable.
* **Graph discipline.** One edge kind; all crossings mediated by gates; SquareLaw on every crossing.
* **Reproducible valuation.** Flow = valuation over `U.Transfer`, with slice‑local refresh bounded by sentinels.
* **LEX hygiene.** ASCII Tech labels, twin Tech/Plain registers, registered tokens.

### A.20:4 - Solution

#### A.20:4.1 - Intent & Scope

**Intent.** Establish the **ConstraintValidity core** for the **`U.Flow` genus**: the normative set of **internal step constraints** and how they are surfaced and aggregated, **independent of GateFit profiles** (publication follows MVPK without adding new numeric claims). Where CV speaks about admissibility, phrase criteria **counterfactually**: *“If the admissibility conditions hold, then the CV explanation applies; otherwise this explanation does not apply.”* Avoid duty verbs unless stating the **normative** CC minima.

**Scope (genus).** CV covers **intra‑step** properties checkable from the transformation’s own signature/mechanism. The canonical CV classes are **genus‑level and non‑exhaustive**:
`MechanismUnitsCoherence`, `LawSetInvariants`, `AdmissibilityConditionsSatisfaction`, `LipschitzBounds`, `TypeDomainRange`, and—only for **`StructuralReinterpretation`**—`ReinterpretationEquivalence` (correspondence/reversibility witness).

**Species binding (`U.TransductionFlow`).** The above classes bind to `U.Transduction(kind ∈ {Signature, Mechanism, Work, Check, StructuralReinterpretation})` with **`OperationalGate = kind=Check`**; no additional CV classes are introduced here (species‑specific semantics reside in A.31 and A.45).

**Out‑of‑scope (CV):** declaring/translating `ReferencePlane/Units/ComparatorSet`; CSLC comparability; Freshness; Role/Channel; Regulated‑X; `DesignRunTagConsistency` — all reside in **GateFit** (A.21).

#### A.20:4.2 - Intensional object(s)

**Genus.** `U.Flow` leaves step‑kinds abstract; CV/GF separation applies to any lawful instantiation.
**Species (`U.TransductionFlow`).** `U.Transduction(kind) ∈ {Signature, Mechanism, Work, Check, StructuralReinterpretation}`; this set of **kinds** is a **minimum roles baseline** defined in E.TGA. The **species** space (e.g., `UNM.Authoring/Usage`, `SelectionAndTuning`, `WorkPlanning`, `EvaluatingAndRefreshing`, …) is **open‑world** and non‑exhaustive. `OperationalGate = U.Transduction(kind=Check)`. `StructuralReinterpretation` is **projection‑preserving** (no mutation of `⟨L,P,E⃗,D⟩`) and may retarget **describedEntity** under CC‑TGA‑06‑EX; see also A.45.

**`AdmissibilityConditionsSatisfaction`** — **If** the declared admissibility conditions hold on the step’s inputs and context, **then** the CV explanation **applies**; **otherwise** this explanation **does not apply**.
**`LipschitzBounds`** — **If** inputs vary within the stated domain \(X\) and perturbations/noise \(≤ ε\), **then** the step’s estimate remains within **δ** of the reference; **otherwise** this explanation **does not apply**.
**`MechanismUnitsCoherence / TypeDomainRange`** — **If** units/types/domains match the mechanism’s signature and closed‑world assumptions for the step, **then** the CV explanation **applies**; **otherwise** this explanation **does not apply**.

**Terminology & bindings (normative)**
* **Status/witness lexicon (E.10 discipline).** In CV scope, publications use **Status/Witness** terminology; **GateDecision…** lexemes belong to GateFit (A.21) and do **not** apply to CV.
* **describedEntity = KindBridge.** Any CV mention of “describedEntity” SHALL be read via **`KindBridge (CL^k)`** on **UTS** (A.27 / C.3.3). CV **does not** declare or translate planes/units/comparators.
* **retargeting/witness binding.** For `U.Transduction(kind=StructuralReinterpretation)`, the CV class **`ReinterpretationEquivalence`** SHALL surface **`CV.WitnessRef := ReinterpWitness`** over the addressed `PathSliceId`; the UTS **`SquareLaw‑retargeting` witness** is referenced from MVPK/UTS and **linked** from the CV witness without duplication.
* **`ReinterpWitness` record (normative).**  
  `ReinterpWitness := { PathSliceId, PublicationScopeId, mapping:{kind: iso|optic, laws: PutGet/GetPut}, commutingSquares:[TransferId], definedOn: PathSliceId, properties:{invertible?:bool, idempotent?:bool}, UTS.RowId, NoHiddenScalarization:true }`.

#### A.20:4.3 - MVPK Faces (PlainView - TechCard - InteropCard - AssuranceLane)

Minimum pins on faces that surface CV outcomes (**Lean surfacing** allowed by profile but without weakening checks):

* **CtxState pins.** `⟨L,P,E⃗,D⟩` on ports/tokens; raw `U.Transfer` preserves them.
* **Path pins.** `PathId` and `PathSliceId` appear where slice‑local refresh or reinterpretation witnesses are relevant (valuation semantics per A.22).
* **CV pins.** `CV.Status ∈ {abstain, pass, degrade, block}`, `CV.WitnessRef?` (refs only).
* **Edition pins.** If a face cites `CG‑Spec`, `ComparatorSet`, or `UNM.TransportRegistryΦ`, the face **includes** the compatibility surface **as per A.27 (BridgeCard + UTS row, with `CL/CL^plane`)** for downstream consumption. A.20 references this requirement; it does not introduce or modify Bridge/UTS formats.
* **Face scope.** Each face includes `PublicationScopeId` with an **MVPK profile** (Min/Lite/SetReady/Max) — no new surface kinds.
* **Register discipline.** Tech names ASCII; twin labels; required LEX tokens follow E.10 (e.g., `SentinelId`, `PathSliceId`, `SliceRefresh`).

> **No new numeric claims.** Faces add pins and references; they do **not** introduce fresh computed scalars beyond what the mechanism already entails (MVPK functoriality).

**Publication lexeme (per‑check).** Each surfaced CV check is referenced as  
`GateCheckRef := { aspect=ConstraintValidity, kind, edition, scope }` with `scope ∈ {lane|locus|subflow|profile}`. This adds no execution steps and introduces no numeric claims on faces; it records what CV classes were considered and under which editions.

#### A.20:4.4 - GateChecks (table) — CV only

**Activation predicate (in E.TGA).** *Until aggregated `CV = pass`, all GateFit checks return `abstain` (CV⇒GF).*
**Role/Channel Fit guard (GateFit scope).** GateFit checks that involve roles SHALL use **Kernel `U.Role` tokens** (domain = `U.System`) and SHALL NOT consume `TypicalEnactorRoleName` strings from alias tables.

| Check class (A.20)                                                                                | aspect | Mandatory | Allowed | Forbidden |
| ------------------------------------------------------------------------------------------------- | -----: | :-------: | :-----: | :-------: |
| MechanismUnitsCoherence                                                                           |     CV |     ✓     |    —    |     —     |
| LawSetInvariants                                                                                  |     CV |     ✓     |    —    |     —     |
| AdmissibilityConditionsSatisfaction                                                               |     CV |     ✓     |    —    |     —     |
| LipschitzBounds / stability                                                                       |     CV |     ✓     |    —    |     —     |
| TypeDomainRange                                                                                   |     CV |     ✓     |    —    |     —     |
| ReinterpretationEquivalence (StructuralReinterpretation only; witness present)                    |     CV |     ✓     |    —    |     —     |
| Any `ReferencePlaneCrossing`, CSLC, Freshness, Role/Channel, Regulated‑X, DesignRunTagConsistency |     GF |     —     |    —    |     ✓     |

CV **must not** declare/translate `Units/ReferencePlane/ComparatorSet`; crossings and CSLC comparability live only in A.21.

#### A.20:4.5 - SWP matrix (single‑writer discipline)

* **Writes (faces).** `CV.Status` (and optional `CV.WitnessRef`) only.
* **Reads (ref‑only).** Any `CG‑Spec/ComparatorSet/TransportRegistryΦ` editions (when referenced); UNM remains single writer as per CC‑TGA‑24.

#### A.20:4.6 - CtxState & GateCrossing

* **Crossings only at `OperationalGate(profile)`** (plane/unit/context) with a **strict exception** for **`StructuralReinterpretation`**: a **projection‑only retargeting** MAY occur without a gate **iff** `⟨L,P,E⃗,D⟩` is preserved, **KindBridge (`CL^k`)** and a **SquareLaw‑retargeting witness** are present on MVPK/UTS, and the action is **PathSlice‑local** (`PathSliceId` pinned).
* **Projection vs describedEntity (normative reduction).** “Projection” denotes a change of **MVPK published view** that is point‑wise identity on the intensional transformation; “describedEntity” is the **Kind‑channel** on UTS evidenced by a `CL^k` row. “No unit/plane change” holds iff `P` is equal on both sides and **no `CL^plane`** is emitted for the step.
* **Projection/describedEntity normalization (normative).** In the context of `StructuralReinterpretation`, the terms **projection** and **describedEntity** are read **via UTS**: projection = change of **published view coordinates** only; describedEntity = **Kind‑channel** change under `CL^k`. A **“no unit/plane change”** test SHALL verify that `ReferencePlane(src)=ReferencePlane(tgt)` and `CL^plane` is absent (or `= ⊤`), otherwise the step is a gated crossing.
* **Assurance operations on edges.** `ConstrainTo/CalibrateTo/CiteEvidence/AttributeTo` reside on `U.Transfer` and do **not** alter `⟨L,P,E⃗,D⟩`; plane/unit changes occur only at gates; Φ/`CL^plane` penalties route in **R‑lane**. describedEntity/kind transitions are surfaced as **`KindBridge (CL^k)`** on **UTS** (see A.27 / C.3.3). describedEntity/kind transitions use **KindBridge (`CL^k`)** (A.27/E.TGA); under CC‑TGA‑06‑EX this appears without a gate and remains PathSlice‑local.

**Terminology binding (TGA‑specific, normative)**
* **Status/witness lexicon (E.10 discipline).** In CV scope, publications use **Status/Witness** terminology; **GateDecision…** lexemes belong to GateFit (A.21) and do **not** apply to CV.
* **describedEntity = KindBridge.** Any CV mention of “describedEntity” SHALL be read via **`KindBridge (CL^k)`** on **UTS** (A.27 / C.3.3). CV **does not** declare or translate planes/units/comparators.
* **retargeting/witness binding.** For `U.Transduction(kind=StructuralReinterpretation)`, the CV class **`ReinterpretationEquivalence`** SHALL surface **`CV.WitnessRef := ReinterpWitness`** over the addressed `PathSliceId`; the UTS **`SquareLaw‑retargeting` witness** is referenced from MVPK/UTS and **linked** from the CV witness without duplication.
* **`ReinterpWitness` record (normative).**  

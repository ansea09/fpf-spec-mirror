  **Avoid:** keep set‑valued semantics unless a total order is explicitly declared by a comparator/policy.

* **Anti-pattern:** Competing defaults scattered across multiple patterns.  
  **Avoid:** Default Ownership Index; delegate duplicate statements to the single owner.

* **Anti-pattern:** Local trigger tokens without canonical mapping.  
  **Avoid:** provide/cite a `TriggerAliasMap` with namespace‑qualified aliases.

* **Anti-pattern:** Breaking public CC ids during dedup.  
  **Avoid:** convert to delegation items; preserve IDs.


### G.Core:9 - Consequences

* **Positive:** Part‑G‑wide invariants become single-owned; refactors become safer and easier to audit.
* **Positive:** RSCR becomes reason-code driven (typed triggers), improving traceability and preventing semantic drift.
* **Positive:** Default conflicts become detectable and resolvable via single-owner discipline.
* **Negative:** Adds an extra authoring step (linkage sections and CoreRef CC item) to each `G.x`.
* **Negative:** Requires careful governance of the trigger catalogue to avoid excessive fragmentation.

### G.Core:10 - Rationale

Universalization of Part G requires a stable “gravity center” for invariants, otherwise each pattern becomes a competing source of truth. Delegation-first routing prevents duplication and makes ownership explicit, while typed triggers and default ownership turn historically prose-driven drift into checkable, id-based structure.

### G.Core:11 - SoTA alignment (informative)

Although FPF is conceptual (not a data governance framework), `G.Core` aligns Part‑G authoring with modern best practice patterns seen across post‑2015 work:

* **Selective prediction / abstention** informs tri‑state guard discipline: abstaining or degrading is a first-class outcome, not an error coerced into a scalar.
* **Set-valued / conformal methods** motivate set-return semantics: when comparability is partial or uncertainty is structural, returning sets/regions is often the SoTA-friendly representation.
* **Multiobjective optimization and quality-diversity** reinforce portfolio/Archive semantics instead of forced “best single scalar”.
* **Monotone constrained modelling** (where used) supports “legality-first” scoring/aggregation: constraints and admissibility precede optimization, mirroring CG‑Spec gate discipline.
* **Schema evolution and contract testing** motivate id-stable conformance points and typed trigger catalogues: stable identifiers + regression hooks are the practical mechanism for safe refactoring.

### G.Core:12 - Relations

* **Builds on:**

  * `E.8` pattern template and section discipline
  * `E.10` lexical/ontological rules (strict distinction; twin naming; kind‑suffix discipline)
  * `E.18` CrossingSurface (crossing visibility surface)
  * `E.19` conformance discipline
  * `A.6.7` SuiteObligations + suite protocol pins (routing surface)
  * `A.15.3` SlotFillingsPlanItem (planned baseline anchor)
  * `A.19` CN‑Spec contract surface
  * `G.0` CG‑Spec legality gate
  * `A.19.CHR` CHR suite boundary and “contract surfaces are pins, not copies” discipline
  * `C.23` SoS‑LOG (tri‑state branches; sandbox/probe‑only)
  * `F.17` UTS (identifier registry; alias/deprecation discipline)
  * `F.15` RSCR (regression/conformance loop)

* **Used by:**

  * `G.0…G.13` patterns (each adds `Builds on: G.Core`, linkage section, CoreRef CC item)

* **Constrains:**

  * Part‑G authoring: no shadow specs, no silent scalarization, tri‑state guards, penalties routing, typed RSCR causes, single-owner defaults, and ID‑continuity refactors.

### G.Core:End

## G.0 - Frame Standard and Comparability Governance — CG‑Spec

**Tag.** Architectural pattern (foundational Standard; constrains G.1–G.5)
**Stage.** *design-time* contract surface (establishes comparison legality & evidence minima; constrains run-time gates)
**Primary output.** `CG‑Spec` — a notation-independent legality gate for a `CG‑Frame`, published to UTS (with explicit edition pins for downstream reproducibility and RSCR).
**Primary hooks.** `USM.ScopeSlice(G)`, `describedEntity`, `SCP`, `MinimalEvidence`, `CNSpecRef`, `Γ‑fold`, `Φ(CL)` / `Φ_plane` policy pins, `UTS` publication (Name Cards + edition pins).
**Non-duplication note.** Universal Part‑G invariants are owned by `G.Core` and are satisfied here **only via delegation** (`CC‑G0‑CoreRef` → `CC‑GCORE‑*`). Single‑owner contract-surface discipline (CN/CG) is enforced via `CC‑GCORE‑CN‑CG‑1` (no shadow specs; no competing defaults).

### G.0:1 - Problem frame

A team defines or evolves a `CG‑Frame` (e.g., a frame for creativity measurement, decision quality, architecture trade‑offs, or portfolio selection). Downstream mechanisms (G.1–G.5 and beyond) must compare, aggregate, and publish CHR‑typed observations in ways that are:

* lawful with respect to measurement legality (scale/unit/polarity constraints),
* auditable with explicit evidence minima and provenance,
* reproducible via pinned editions and explicit policy ids,
* portable only via explicit crossings (bridges and reference-plane moves), never via implicit semantic leakage.

`CG‑Spec` is the single design-time object that fixes *what comparisons and aggregations are lawful in this frame*, under which pinned assumptions and minimal evidence requirements, so that run-time selection and publication can be audited without inventing new “local legality gates”.

Didactic subtitle: **Design-time rules for safe, auditable comparison.**

### G.0:2 - Problem

Without a single, frame-level legality standard:

* comparisons and aggregations drift into *implicit assumptions* (hidden scalarisation; silent totalisation of partial orders),
* numeric gates run on “whatever is available” rather than declared evidence minima and lane/carrier requirements,
* cross-context reuse happens without explicit crossing visibility and stated losses,
* selection outcomes become hard to audit because legality, evidence minima, and penalty routing are not pinned and traceable.

### G.0:3 - Forces

* **Pluralism vs. comparability.** Multiple traditions must co-exist while allowing lawful comparison where justified.
* **Expressiveness vs. safety.** Rich comparator sets and aggregators vs. measurement legality constraints.
* **Locality vs. portability.** Context-local semantics first; portability only via explicit bridges and explicit losses.
* **Assurance vs. agility.** Evidence minima must be strong enough to matter, light enough to adopt.
* **Design-time vs. run-time.** Keep legality standards and templates design-time; run-time only cites and applies them.

### G.0:4 - Solution — CG‑Spec as the design-time legality gate

`CG‑Spec` is a **notation-independent** UTS-published object that, for a given `CG‑Frame`, defines:

* the **ComparatorSet** (explicit, finite, typed) permitted in this frame,
* the **ScaleComplianceProfile** (SCP) that constrains lawful operations per characteristic,
* **MinimalEvidence** requirements per characteristic (lanes, carriers, freshness windows, crossing allowances, failure behavior),
* the frame’s **penalty and trust folding wiring** (by explicit policy ids and edition pins),
* **AcceptanceStubs** as design-time templates (thresholds remain owned by CAL, not by CG‑Spec),
* optional method-family hooks (e.g., illumination/QD or explore↔exploit guards) *as wiring only*, with semantics owned by the corresponding patterns.

`CG‑Spec` constrains downstream gate checks by being *referenced and pinned*; it is not itself an admissibility mechanism.

#### G.0:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; single-owner routing)

**GCoreLinkageManifest (normative; size-controlled via profiles/sets).**

Effective obligations/pins/triggers are computed by union expansion of the referenced ids (per `G.Core:4.2`).
Profiles/sets + explicit deltas; `Nil‑elision` applies.

* `CoreConformanceProfileIds :=`
  * `GCoreConformanceProfileId.PartG.AuthoringBase`
  * `GCoreConformanceProfileId.PartG.TriStateGuard`
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
* `CorePinSetIds :=`
  * `GCorePinSetId.PartG.AuthoringMinimal`
  * `GCorePinSetId.PartG.CrossingVisibilityPins`
* `CorePinsRequired :=` *(delta over PinSets)*
  * `UTSRowId[]`
  * `ReferenceMap`
  * `ComparatorSetRef.edition`
  * `SCPRef.edition`
  * `ΓFoldRef.edition?`
  * `MinimalEvidenceRef.edition?`
  * `FailureBehaviorPolicyId?`
* `DefaultsConsumed := {DefaultId.GammaFoldForR_eff}` *(owner: `CC‑G5.4` per `G.Core.DefaultOwnershipIndex`)*
* `RSCRTriggerSetIds := {GCoreTriggerSetId.CGSpecGate}`
* `RSCRTriggerKindIds :=` *(delta over TriggerSets)*
  * `RSCRTriggerKindId.EvidenceSurfaceEdit`
  * `RSCRTriggerKindId.TokenizationOrNameChange`
  * `RSCRTriggerKindId.DefaultOwnerChange`
* `TriggerAliasMapRef := ∅`

#### G.0:4.2 - CG‑Spec object model (normative)

`CG‑Spec` is authored per `CG‑Frame`. It SHALL:

* be **published to UTS** as a notation-independent object,
* reference CHR characteristics by id (measurement semantics remain owned by CHR packs),
* constrain what comparisons and aggregations are lawful in this frame via explicit comparator specs and SCP bindings,
* declare minimal evidence gates per characteristic, including explicit failure behavior wiring,
* cite `CN‑Spec` for normalization/comparability policies (no duplication and no shadow specs),
* publish edition pins and policy ids so downstream selection, parity, shipping, and refresh can be reproducible and RSCR-aware.

#### G.0:4.3 - CG‑Spec conceptual model (normative)

```
CG‑Spec :=
⟨
  UTS.id, Edition,
  Context, Purpose, Audience,

  Scope := USM.ScopeSlice(G) ⊕ Boundary{TaskKinds, ObjectKinds},

  describedEntity := ⟨GroundingHolon, ReferencePlane ∈ {world|concept|episteme}⟩,
  WorldRegime? ∈ {prep|live},          // only refines ReferencePlane=world; introduces no new planes

  ReferenceMap := minimal map{term/id → UTS|CHR|SoTA-pack refs},

  CNSpecRef := ⟨A.19 ref, CNSpecRef.edition⟩,          // CN‑Spec is the contract surface (single-owner)

  Characteristics := [CHR.Characteristic.id…],          // pointers only; authored in G.3 CHR pack

  // Edition-addressable segments (pins MUST be exposed)
  ComparatorSet := ⟨ComparatorSetId, ComparatorSetRef.edition, [ComparatorSpec…]⟩,
  SCP := ⟨SCPId, SCPRef.edition, map Characteristic.id → SCPEntry⟩,
  MinimalEvidence := ⟨MinEvId, MinimalEvidenceRef.edition?, map Characteristic.id → MinEvidenceEntry⟩,  // min pin: CGSpecRef.edition

  Γ‑fold := ⟨GammaFoldId, ΓFoldRef.edition,
             defaultRef := DefaultId.GammaFoldForR_eff,
             override? := ⟨overrideRef, proof_refs, boundary_notes⟩
           ⟩,

  // Penalty routing and plane policies are by explicit policy ids.
  // Semantics (tri-state, penalties→R_eff-only, crossing visibility, set-return) are owned by G.Core.
  CL‑Routing := ⟨policy_id, map Bridge.CL → penalty_spec⟩,
  Φ := ⟨phi_policy_id, phi_table_ref?, psi_policy_id?, phi_plane_policy_id?⟩,

  AcceptanceStubs := [AcceptanceStubId…],     // templates only; thresholds remain owned by CAL (G.4)

  // Optional hooks are wiring-only; semantics live in owners.
  E/E‑LOG Guard? := ⟨policy_id, pins…⟩,
  Illumination? := ⟨
    Q_refs ⊆ Characteristics, D_refs ⊆ Characteristics,
    DescriptorMapRef.edition?, DistanceDefRef.edition?, DHCMethodRef.edition?,
    InsertionPolicyRef?, PromotionPolicyId?
  ⟩,

  RSCR := ⟨
  RSCRTestId[]?,             // SHOULD cover: illegal_op_refusals; unit/scale legality checks; freshness windows; // partial-order scalarisation refusals; threshold semantics; CL→R_eff routing;
                            // and refusal of degrade.order on unit mismatches (MM‑CHR).
    RSCRTriggerKindId[]
  ⟩,

  Naming := UTS Name Cards (twin labels + lifecycle + bridge notes),
  Lifecycle := ⟨owner, DRR link, refresh cadence, decay/aging, deprecations⟩,
  Provenance := ⟨carrier types, SoTA-pack refs, DRR/SCR linkage⟩
⟩
```

**Local typing notes (non-exhaustive; normative intent but no shadow specs).**

* `ComparatorSpec` MUST be typed against SCP/CHR constraints. Examples of lawful comparators are frame-local choices and are authored here (e.g., dominance where lawful; lexicographic over typed traits; medoid/median for ordinal where lawful; explicit weighted sums only where legality is proven and units are aligned).
* `MinimalEvidenceEntry` MUST declare: lane requirements, evidence carriers, freshness window (if any), and explicit failure behavior wiring. The semantics of `{pass|degrade|abstain}` and `degrade(mode=…)` are delegated to `G.Core`.

#### G.0:4.4 - Interfaces (normative)

| Interface          | Consumes                             | Produces / constrains                                                      |
| ------------------ | ------------------------------------ | -------------------------------------------------------------------------- |
| **G.0‑1 Charter**  | CG‑Frame brief, USM scope signals    | `CG‑Spec.Scope`, `describedEntity`, `ReferenceMap`                         |
| **G.0‑2 SCP**      | CHR pack refs (G.3), legality proofs | `CG‑Spec.SCP` + bindings to lawful operators/aggregators                   |
| **G.0‑3 Evidence** | SoTA inputs (G.2), carriers (A.10)   | `CG‑Spec.MinimalEvidence`, `Γ‑fold` segment pins, `CL‑Routing`, `Φ` ids    |
| **G.0‑4 Publish**  | All above                            | Versioned `CG‑Spec@UTS` + Name Cards, lifecycle, RSCR tests/trigger kinds  |
| **G.0‑5 Expose_CrossingHooks** | `CG‑Spec` + crossing/plane/policy pins | GateCrossing inputs for `GateChecks` (`E.18/A.21`): plane checks, lane purity, lexical SD pins |
| **→ G.1**          | `CG‑Spec`                            | Generator guardrails (Comparator/SCP/MinEv pins); degrade/abstain wiring   |
| **→ G.2**          | `CG‑Spec`                            | Harvesting inclusion/exclusion and crossing policy constraints             |
| **→ G.3**          | `CG‑Spec`                            | Required CHR characteristics/scales/operators to exist                     |
| **→ G.4**          | `CG‑Spec`                            | Acceptance templates; evidence minima; Γ‑fold override proof hooks         |
| **→ G.5**          | `CG‑Spec`                            | Eligibility gates and explainability pins (Path/UTS/policy ids)            |
| **→ G.6**          | `CG‑Spec`                            | EvidenceGraph/SCR pinning surface (policy ids + Path/PathSlice discipline) |

#### G.0:4.5 - Authoring workflow for CG‑Spec (informative)

1. **Charter the frame.** Declare `Context`, `Scope`, `describedEntity`, boundary examples/non-examples, and `ReferenceMap`.
2. **Draft ComparatorSet and SCP.** Enumerate permitted comparator forms and bind each to CHR characteristics and legality constraints (scale/unit/polarity discipline). Attach guard bindings as explicit references/pins.
3. **Bind Characteristics.** Ensure every compared quantity is a CHR characteristic id (reuse/mint via UTS discipline).
4. **Declare MinimalEvidence.** For each characteristic: required lanes/carriers, freshness window, crossing allowances (if any), and explicit failure behavior wiring (tri-state semantics delegated to `G.Core`).
5. **Pin trust folding and penalties.** Cite the single owner for `DefaultId.GammaFoldForR_eff` unless explicitly overridden with proof refs; publish `Φ`/CL policy ids explicitly.
6. **Publish and register regression tests.** Publish `CG‑Spec@UTS` with edition-pinned segments; register RSCR tests for the frame’s legality surfaces and evidence minima.
7. **Lifecycle and refresh readiness.** Declare refresh cadence and deprecations with lexical continuity notes; ensure RSCR trigger kinds are emitted as canonical ids.

#### G.0:4.6 - Extensions (pattern-scoped; non-core)

All blocks below are `GPatternExtension` modules (PatternScopeId; not new PatternIds). They store wiring only and cite semantic owners.

**GPatternExtension: ContractSurfaces**

* **PatternScopeId:** `G.0:Ext.ContractSurfaces`
* **GPatternExtensionId:** `ContractSurfaces`
* **GPatternExtensionKind:** `InteropSpecific`
* **SemanticOwnerPatternId:** `A.19`
* **Uses:** `{A.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CNSpecRef.edition` (and any CN-side policy ids referenced by `CG‑Spec` fields)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.LegalitySurfaceEdit}`
* **Notes (wiring-only):** `CG‑Spec` SHALL cite CN‑Spec; it SHALL NOT restate normalization/comparability semantics.

**GPatternExtension: BridgeAndCLWiring**

* **PatternScopeId:** `G.0:Ext.BridgeAndCLWiring`
* **GPatternExtensionId:** `BridgeAndCLWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **SemanticOwnerPatternId:** `F.9`
* **Uses:** `{F.9, G.7}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `BridgeCardId/BridgeId` (when crossings are permitted)
  * `CL` / `CL^k` and `Φ`/`Φ_plane` policy ids (when penalties are in play)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (wiring-only):** Crossing semantics and penalty routing are delegated to `G.Core`; this module only lists the required pins used by `CG‑Spec` entries.

**GPatternExtension: SoTAPaletteInputs**

* **PatternScopeId:** `G.0:Ext.SoTAPaletteInputs`
* **GPatternExtensionId:** `SoTAPaletteInputs`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **SemanticOwnerPatternId:** `G.2`
* **Uses:** `{G.2}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `SoTA-Pack@CG‑Frame` refs used to justify comparator admissibility, evidence minima, and crossing allowances (e.g., claim sheets, operator inventory, bridge matrix ids)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring-only):** Any SoTA palette/tradition semantics are owned by `G.2`. `G.0` only requires that `CG‑Spec` entries cite the needed SoTA artefacts for auditability.

**GPatternExtension: QDAndExplorationHooks**

* **PatternScopeId:** `G.0:Ext.QDAndExplorationHooks`
* **GPatternExtensionId:** `QDAndExplorationHooks`
* **GPatternExtensionKind:** `MethodSpecific`
* **SemanticOwnerPatternId:** `C.18`
* **Uses:** `{C.18, C.19, C.23}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `InsertionPolicyRef?`
  * `FailureBehaviorPolicyId` / SoS‑LOG branch policy id when `degrade(mode=…)` is used
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring-only):** `CG‑Spec` may declare optional QD/exploration hooks; semantics remain owned by the referenced method patterns.

### G.0:5 - Archetypal Grounding — Tell–Show–Show; System / Episteme

#### G.0:5.1 - Archetype 1: System comparability under mixed evidence and unit constraints

**Tell.** Two labs compare energy efficiency results of a physical system where measurements use different rigs and units, and some evidence is missing.

**Show (failure without CG‑Spec).** The team averages an ordinal safety rating, mixes units (“kWh” vs “MJ”), and silently treats missing lanes as zeros. Cross-lab reuse happens without explicit bridge/loss notes, so selection becomes a black box.

**Show (repair with CG‑Spec).** A conformant `CG‑Spec`:

* pins the lawful comparator(s) (e.g., unit-aligned ratio comparisons only; ordinal comparisons are order-only),
* declares `MinimalEvidence` lanes/carriers and freshness windows per characteristic,
* declares explicit failure behavior wiring (tri-state semantics delegated to `G.Core`),
* exposes crossing pins (bridge ids + CL/policy ids) when reuse across rigs is attempted,
* publishes the pinned editions so parity/refresh can detect drift.

#### G.0:5.2 - Archetype 2: Epistemic comparability for portfolio selection across traditions

**Tell.** A team selects an R&D portfolio using multiple evaluation traditions: safety assurance, cost models, and readiness heuristics.

**Show (failure without CG‑Spec).** The team collapses partial orders into a single score, hides the threshold policy in code, and cannot explain why cross-tradition penalties changed between runs.

**Show (repair with CG‑Spec).** A conformant `CG‑Spec`:

* defines a comparator portfolio (e.g., Pareto dominance + explicit lexicographic tiebreaks where lawful),
* pins `CNSpecRef.edition` and the editioned segments (`ComparatorSetRef.edition`, `SCPRef.edition`, `MinimalEvidenceRef.edition`),
* makes `AcceptanceStubs` explicit as templates while locating thresholds in CAL (G.4),
* ensures RSCR triggers are emitted when comparator or policy pins change.

### G.0:6 - Bias-Annotation

`CG‑Spec` can encode (and therefore amplify) biases if authored carelessly:

* **Tradition favoritism.** Comparator choices may privilege a tradition’s evidence style; mitigation: require explicit evidence minima and explicit crossing costs, and keep cross-tradition aggregation gated by explicit justifications.
* **Metric gaming and Goodhart effects.** Overemphasis on a single scalar can lead to gaming; mitigation: preserve set-return semantics and require explicit, auditable scalarisations when they are lawful and intended.
* **Hidden thresholds and opaque safety policy.** Embedding acceptance thresholds in prose or code hides value judgments; mitigation: keep thresholds in CAL acceptance clauses and pin policy ids.
* **Scope creep.** Comparisons leak across describedEntity or reference planes; mitigation: require explicit `describedEntity` and `ReferencePlane` pins and treat plane moves as explicit crossing events.

### G.0:7 - Conformance Checklist (normative)

| ConformanceId | Statement |
| --- | --- |
| **CC‑G0‑CoreRef** | `G.0` is conformant only if the applicable core obligations listed in `G.0:4.1` are satisfied (delegation to `CC‑GCORE‑*`; no shadow specs, no competing defaults, typed RSCR triggers, explicit pins). |
| CC‑G0‑01 | `CG‑Spec` is published as a notation-independent UTS object with explicit `Edition`, `Context`, `Scope`, `describedEntity`, and a minimum `ReferenceMap`. |
| CC‑G0‑02 | `CNSpecRef.edition` is present and is treated as an external contract surface reference (no local redefinition of CN semantics). *(Delegation target: `CC‑GCORE‑CN‑CG‑1`.)* |
| CC‑G0‑03 | `ComparatorSet` is explicit and finite; each comparator is typed and bound to `SCP` and referenced CHR characteristics; **anything not enumerated MUST be treated as illegal/abstain by default** (no implicit comparator defaults). |
| CC‑G0‑04 | `SCP` declares, per characteristic, the lawful operation regime needed for each referenced comparator (scale/unit/polarity constraints and any required proofs/refs). |
| CC‑G0‑05 | `MinimalEvidence` is declared per characteristic and includes explicit lane/carrier requirements, freshness window references (if any), and explicit failure behavior wiring (tri-state semantics delegated). If freshness windows are used, a stable window id (e.g., `PathSliceId`) MUST be pinned for audit. |
| CC‑G0‑06 | `Γ‑fold` is present as an edition-pinned segment and either (i) cites `DefaultId.GammaFoldForR_eff` (single owner) or (ii) provides an explicit override with proof refs. |
| CC‑G0‑07 | If crossing penalties are used, `CL‑Routing` and `Φ` policy ids are explicit and auditable (policy ids are exposed as pins/refs) **and are required pins for downstream SCR publication on penalised claims** (see `G.6`). |
| CC‑G0‑08 | `AcceptanceStubs` in `CG‑Spec` are templates only; any context-local thresholds/acceptance policies are owned by CAL acceptance artefacts (G.4) and are cited, not duplicated. |
| CC‑G0‑09 | RSCR tests/triggers for edits to legality surfaces and evidence minima are present and use canonical `RSCRTriggerKindId`s. The RSCR test set SHOULD cover at least: illegal_op_refusals; unit/scale legality checks; freshness windows; partial-order scalarisation refusals; threshold semantics; CL→`R_eff` routing; refusal of `degrade.order` on unit mismatches (MM‑CHR). |
| CC‑G0‑10 | `Lifecycle` is declared: owner, DRR link, refresh cadence, decay/aging policy, and deprecations. Deprecations preserve lexical continuity (Δ-discipline; delegated to `CC‑GCORE‑ID‑*`). |
| CC‑G0‑11 | *(Conditional)* If `Illumination` / QD hooks are present, `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and any `InsertionPolicyRef` / promotion policy ids are pinned (or explicitly marked absent) and are recorded in provenance/audit pins. |
| CC‑G0‑12 | *(Conditional)* If freshness windows influence gating/selection, they are published and enforced, and the relevant window ids (`PathSliceId` or equivalent) are recorded in SCR/audit pins. |
| CC‑G0‑13 | **Pre-flight numeric gates.** Any numeric comparison/aggregation declared in `ComparatorSet` has associated `GateChecks` for unit legality, scale legality, pinned SOP/editions, and declared comparability assumptions; failing any check yields `refuse` or `abstain` (tri-state semantics delegated). |
| CC‑G0‑14 | **GateCrossing hook exposure.** Exports provide `Expose_CrossingHooks` inputs so `GateChecks` (`E.18/A.21`) can validate plane consistency, crossing intent, lane purity, and lexical SD; failures MUST block publication. |
| **CC‑G0‑Φ** | `Φ(CL)` (and `Φ_plane`, if used) is monotone, bounded, and table-backed; policy ids are published; construction preserves `R_eff ≥ 0`. |
| **CC‑G0‑Unknowns** | *Delegated.* Unknown handling MUST follow the tri-state guard semantics `{pass|degrade|abstain}` with no silent coercions. (See `CC‑GCORE‑GUARD‑1`.) |
| **CC‑G0‑CSLC** | Scale/unit/polarity legality MUST be proven before any aggregation; illegal arithmetic on ordinal/nominal values is nonconformant. (Ownered by the relevant legality patterns; `G.0` only binds and cites.) |
### G.0:8 - Common Anti-Patterns and How to Avoid Them

* **Anti-pattern: shadow legality gates in downstream code.** Avoid by requiring downstream to cite `CG‑Spec` segments by id+edition.
* **Anti-pattern: “one number to rule them all”.** Avoid by preserving set-return outputs when only partial orders are lawful; any scalarisation must be explicit, typed, and justified.
* **Anti-pattern: thresholds inside CG‑Spec or CHR.** Avoid by keeping thresholds and acceptance logic in CAL and citing from `CG‑Spec` only via stubs/templates.
* **Anti-pattern: implicit crossings.** Avoid by requiring explicit bridge ids, CL/policy ids, and reference-plane pins.

### G.0:9 - Consequences

* **Lawful comparability.** The frame declares exactly what can be compared/aggregated and under what constraints.
* **Auditable selection.** Downstream selectors can justify outcomes via pinned legality surfaces and explicit evidence minima.
* **Explicit portability costs.** Cross-context reuse becomes deliberate and costed via visible crossings and penalties.
* **Lower drift under evolution.** Edition pinning + typed RSCR triggers makes comparability drift detectable and refreshable.

### G.0:10 - Rationale

`CG‑Spec` centralises frame-level comparability constraints so that:

* CHR authorship (G.3) remains about *measurement meaning* rather than implicit thresholds,
* CAL (G.4) owns context-local acceptance/threshold policies and proof ledgers,
* selectors and dispatchers (G.5) remain policy-governed and auditable rather than encoding hidden legality assumptions,
* refresh (G.11) can treat legality edits and pin changes as explicit causes with canonical trigger ids.

### G.0:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice in evaluation and governance by:

* treating “abstain / defer” as a first-class outcome rather than forcing a single brittle scalar (cf. selective prediction / abstention and set-valued reporting practices),
* preserving multiobjective / partial-order outputs as sets (Pareto / archive thinking) rather than silently collapsing to a scalar,
* emphasising reproducibility via explicit versioning/pinning of evaluation surfaces (editions) and explicit policy identifiers,
* making evidence minima explicit and auditable (a conceptual analogue of modern reproducibility/robustness checklists and evaluation protocols),
* keeping method-family specifics modular (e.g., QD/archives, open-ended exploration budgets) via explicit wiring to owner patterns rather than embedding method semantics into the universal legality gate.

### G.0:12 - Relations

**Builds on:** `G.Core`, `A.19 (CN‑Spec)`, `A.10 (evidence carriers)`, `A.17–A.19 / C.16 (MM‑CHR legality)`, `A.18 (CSLC)`, `B.3 (trust / Γ‑fold family)`, `F.* (contexts, bridges, CL, UTS)`, `E.10 (lexical rules)`, `E.5.* (notation independence discipline)`.
**Used by:** `G.1` (generator guards), `G.2` (harvesting constraints), `G.3` (required CHR), `G.4` (acceptance templates / proof hooks), `G.5` (eligibility gates), `G.6` (evidence/pin surfaces), and downstream parity/shipping/refresh where `CG‑Spec` is pinned.
**Publishes to:** `UTS` (Name Cards + editioned `CG‑Spec` segments).

### G.0:End

## G.1 - CG‑Frame‑Ready Generator

**Tag.** architectural pattern; *generator chassis* (design‑time kit / authoring scaffold)  
**Status.** stable (Phase‑2 universalisation)  
**Normativity.** normative, except sections explicitly marked *informative*  
**Stage.** *design‑time* authoring of a generator‑kit with a *run‑time* execution façade (policy‑governed; edition‑aware)  
**Primary output.** the **six‑card chassis** `M1…M6` published as a **complete, reusable CG‑Frame kit**, plus a versioned **kit manifest** `CGKitId` that binds the six cards as a single reusable unit (view‑friendly inventory + wiring surface)  
**Primary hooks.** see **§12 Relations** (notably `G.Core`, `G.0`, `G.2`, `G.5`, `G.10`, `G.11`)  
**Working‑model first (informative).** prefer working models and didactic micro‑examples; escalate to formal harnesses only when risk warrants (per E.8).  
**Non‑duplication note.** universal Part‑G invariants (tri‑state guard, set‑return, penalties→`R_eff`‑only, crossing visibility, typed RSCR triggers, default ownership, P2W split, linkage discipline, shipping boundary) are **single‑owner in `G.Core`** and are **only cited** here.

### G.1:1 - Problem frame

You are authoring a **CG‑Frame** and want a **repeatable scaffold** that connects:

* a declared **scope anchor** (`CG‑FrameContext`, `describedEntity`, contract surfaces),
* a **local SoTA set** (scoped and provenance‑anchored),
* a **variant pool** (candidate ideas / decision options / method variants),
* a **shortlist** (a set/portfolio outcome, not a forced singleton),
* **publication‑ready bindings** into Part‑F artefacts (UTS rows, Name Cards, RSCR tests, worked examples),
* and **refresh readiness** (telemetry hooks + RSCR wiring) without redefining refresh or shipping.

This pattern is intentionally **a chassis**, not a method specification:

* harvesting semantics live in `G.2`,
* selection/dispatch semantics live in `G.5`,
* CHR/CAL payload semantics live in `G.3` / `G.4`,
* shipping ownership lives in `G.10`,
* refresh orchestration ownership lives in `G.11`.

### G.1:2 - Problem

Without a chassis, CG‑Frame authoring tends to fail in repeatable ways:

* **SoTA is not locally scoped**: inputs are “in the air”, not a reconstructible set.
* **Generation is ad‑hoc**: variant candidates are emitted without a stable trace of why/when/how.
* **Selection is opaque**: eligibility/acceptance and assurance are not pinned to explicit surfaces.
* **Outputs don’t land in reusable surfaces**: no clean hand‑off into UTS / RoleDescription / Concept‑Sets / RSCR.
* **No kit‑level snapshot**: the scaffold lacks a versioned manifest, so downstream can’t reliably cite “which chassis edition” was used.
* **Refresh is unplanned**: there is no canonical wiring from edits/telemetry/decay to RSCR causes along the P2W path.

### G.1:3 - Forces

* **Breadth vs. precision:** harvest wide enough to avoid local dogma, but keep the artefact actionable.
* **Generativity vs. assurance:** encourage novelty while keeping evidence, legality, and trust inspectable.
* **Local meaning vs. portability:** keep meaning local by default; crossing must be explicit and auditable.
* **Expressiveness vs. parsimony:** resist inventing new types/slots; prefer reuse and explicit wiring.
* **Stability vs. evolution:** keep stable IDs and pins while allowing SoTA, policies, and editions to evolve.
* **Didactic clarity vs. normative minimalism:** authors need a concrete scaffold, but universal invariants must not be duplicated outside `G.Core`.

### G.1:4 - Solution

#### G.1:4.1 - G.Core linkage (normative)

```
// Canonical form: see G.Core (Nil‑elision + Expansion rule for profiles/sets/pin‑sets).
GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.TriStateGuard,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
    GCoreConformanceProfileId.PartG.ShippingBoundary
  },

  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },

  // Prefer sets; use deltas for pattern‑specific additions.
  RSCRTriggerSetIds := { GCoreTriggerSetId.SoTAHarvestSynthesis },
  RSCRTriggerKindIds := { RSCRTriggerKindId.BaselineBindingEdit },

  // Pattern‑owned kit identifiers (the “six cards”).
  CorePinsRequired := {
    SoTAPaletteDescriptionId,
    SoTA_SetId,
    VariantPoolId,
    ShortlistId,
    CGFrameLibraryId,
    RefreshReadinessCardId,
    CGKitId,

    // Local pointer-map surface for vocabulary + observables-to-CHR anchoring.
    // (May cite `G.0:CG‑Spec.ReferenceMap`; do not duplicate semantics.)
    ReferenceMap,

    // RSCR regression tests used by the chassis (if any).
    RSCRTestId[]?,

    // When the chassis is bound into WorkPlanning (P2W): planned baseline refs.
    SlotFillingsPlanItemRef[]?
  },

  // Consumed defaults (single‑owner; this pattern only cites owners via `G.Core.DefaultOwnershipIndex`).
  DefaultsConsumed := {
    DefaultId.GammaFoldForR_eff,   // owner: CC‑G5.4
    DefaultId.PortfolioMode,       // owner: CC‑G5.23
    DefaultId.DominanceRegime      // owner: CC‑G5.28
  }
⟩
```

**Routing rule (normative):** the semantics of `CC‑GCORE‑*`, `RSCRTriggerKindId.*`, and `DefaultId.*` are **single‑owner** in their canonical owners (primarily `G.Core`, and for the defaults above the owners listed in `G.Core.DefaultOwnershipIndex`). `G.1` MUST NOT restate or redefine those semantics.

#### G.1:4.2 - Six‑module generator chassis (normative)

**Core artefact:** `CGFrameReadyGeneratorKit := ⟨M1, M2, M3, M4, M5, M6⟩`, where each `Mi` is a **card** with an explicit I/O surface and stable identifiers.
`CGKitId` identifies the versioned **kit manifest** (`CG‑Kit@CG‑Frame`) that lists the six card ids and the minimal wiring pins needed to treat the chassis as a reusable unit (this is **not** a shipping pack; shipping remains owned by `G.10`).

The chassis is *view‑friendly*: it is an inventory of “what exists and how it is wired”, not a second specification of CN/CG/CHR/CAL/selection semantics.

##### M1 — CG‑FrameContext Card (scope anchor)

**Owns (kit surface):**

* `CG‑FrameContext` and its **binding pins**:

  * `describedEntity := ⟨GroundingHolon, ReferencePlane⟩` *(pin set: `PartG.AuthoringMinimal`)*
  * `CNSpecRef.edition`, `CGSpecRef.edition` *(pin set: `PartG.AuthoringMinimal`)*
  * `ReferenceMap` *(cite `G.0:CG‑Spec.ReferenceMap`; do not duplicate semantics)*
  * any declared crossing/policy pins *(pin set: `PartG.CrossingVisibilityPins`)*

**Purpose:** provide the *single scope anchor* used by all downstream cards.

**Notes:** any contract/legality content is **cited** via `A.19 (CN‑Spec)` and `G.0 (CG‑Spec)` (delegation target: `CC‑GCORE‑CN‑CG‑1` via `CC‑G1‑CoreRef`); this card does not introduce a local “mini‑spec”.

##### M2 — SoTA_Set@CG‑Frame (harvester output card)

**Owns (kit surface):**

* `SoTAPaletteDescriptionId` and `SoTA_SetId` bound to `CG‑FrameContext`
* explicit provenance anchors for the set (via `A.10`), and any published UTS stubs/rows when applicable

**Semantic owner:** harvesting discipline and SoTA‑pack payload are owned by `G.2`.
In `G.1`, M2 is a *slot in the chassis* and a wiring surface; it does not redefine the harvesting method.

##### M3 — VariantPool (candidate inventory + emitter trace)

**Owns (kit surface):**

* `VariantPoolId` bound to `CG‑FrameContext`
* per‑candidate minimal traceability fields (emitter identity, `EmitterPolicyRef` (policy‑id/ref; owner‑defined), method/generator refs when declared, edition pins, provenance anchors)
* optional, per‑candidate **assurance preview pointers** (e.g., `PathSliceId?` and/or `SCRId?` when early assurance is recorded) and optional **QD/Open‑Ended scaffolding stubs** (only when introduced by explicit `GPatternExtension` blocks)

**Guardrails (via G.Core):**

* tri‑state eligibility handling, penalties routing, crossing visibility, and set‑return constraints are not defined here; they are enforced via `G.Core` conformance.

**Semantic owner of method payload:** method‑specific emitter semantics live in `Extensions` (e.g., `C.17`, `C.18`, `C.19`).
M3 MUST remain method‑agnostic in its core definition: it is an inventory surface, not an algorithm spec.

##### M4 — Shortlist (selector/assurer output)

**Owns (kit surface):**

* `ShortlistId` bound to `CG‑FrameContext`
* a portfolio/set of selected candidates plus rationale/assurance surfaces (`SCRId` required; `DRRId` optional; cite `PathId/PathSliceId` when applicable)
* optional **front/archive metadata** needed for reproducibility when used: ε‑front parameters and/or archive snapshot hooks, with ownership routed via `G.5` / `C.18` / `C.19` (no local semantics in `G.1`)

**Semantic owner:** selection/dispatch semantics are owned by `G.5`.
M4 MUST preserve *set‑return semantics* (as routed by `G.Core`) and MUST NOT hard‑code a forced singleton outcome.

##### M5 — CG‑FrameLibrary (published bindings index)

**Owns (kit surface):**

* `CGFrameLibraryId` bound to `CG‑FrameContext`
* an index of referenced CG‑Frame artefacts ready for reuse:

  * CHR/CAL/LOG bundles (by their ids; semantics owned by `G.3`, `G.4`, `G.8`)
  * published identifiers (UTS rows, Name Cards) per Part‑F owners
  * additional Part‑F binding surfaces (e.g., RoleDescription templates, Concept‑Set rows) by owner‑ids only
  * RSCR test identifiers (e.g., from `F.15`) and worked examples (where applicable)

**Boundary:** M5 is a **kit/library surface**, not shipping. If a shipped pack is needed, ownership is `G.10`.

##### M6 — RefreshReadiness Card (telemetry hooks + wiring)

**Owns (kit surface):**

* `RefreshReadinessCardId` bound to `CGFrameLibraryId` (and thus to `CG‑FrameContext`)
* `CGKitId` (the versioned kit manifest) binding `M1…M6` into a single reusable unit; it MUST enumerate the card ids and MAY carry references to deprecations/edition bumps minted by the canonical owners
* declared telemetry hooks (what signals are observed, with what pins)
* declared RSCR wiring: which `RSCRTriggerKindId` are relevant (canonical ids), with minimal required payload pins (including `SlotFillingsPlanItemRef[]` when the chassis is bound into WorkPlanning)

**Boundary:** orchestration semantics are owned by `G.11`.
M6 prepares *refresh‑readiness metadata* and wiring stubs; it does not define scheduling/priority heuristics.

#### G.1:4.3 - Minimal I/O surface (normative)

| Module | Consumes                                                                    | Produces                                                                               |
| ------ | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| M1     | CG‑Frame brief + `describedEntity` + `CNSpecRef/CGSpecRef` (edition‑pinned) | `CG‑FrameContext` + context pins                                                       |
| M2     | discovery inputs + inclusion criteria *(via G.2)*                           | `SoTA_SetId` (+ provenance anchors; optional UTS stubs/rows)                           |
| M3     | `SoTA_SetId` + local constraints + emitter policy pins *(via Extensions)*   | `VariantPoolId` (+ candidate trace/provenance; optional method payload via Extensions) |
| M4     | `VariantPoolId` + acceptance/eligibility surfaces *(via G.4/G.5)*           | `ShortlistId` (portfolio/set) + rationale refs                                         |
| M5     | `ShortlistId` + CHR/CAL/LOG bundle refs + UTS/Name refs                     | `CGFrameLibraryId` (library index; publish‑ready bindings)                             |
| M6     | telemetry inputs + freshness/decay policy pins + RSCR tests                 | `CGKitId` + `RefreshReadinessCardId` (wiring to `G.11`; no orchestration ownership)    |

#### G.1:4.4 - Extensions (pattern‑scoped; non‑core)

All method/discipline/generator specifics MUST be expressed as `GPatternExtension` blocks.

> Guard: `G.1:Ext.*` are **PatternScopeId** values (internal, pattern‑scoped), not new patterns and not new `PatternId`.

##### GPatternExtension — `G.1:Ext.HarvesterWiring`

**PatternScopeId:** `G.1:Ext.HarvesterWiring`
**GPatternExtensionId:** `HarvesterWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**SemanticOwnerPatternId:** `G.2`
**Uses:** `{G.2}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoTAPaletteDescriptionId`
* `SoTA_SetId`
* `ClaimSheetId[]` / `BridgeMatrixId` *(as referenced by the chosen G.2 pack form)*
* `CNSpecRef.edition`, `CGSpecRef.edition` *(already required via `GCorePinSetId.PartG.AuthoringMinimal`)*
**RSCRTriggerSetIds:** `{GCoreTriggerSetId.SoTAHarvestSynthesis}`
**Notes (wiring‑only):** harvesting semantics (living review funnels, inclusion policy families, SoS indicator families, etc.) are defined by `G.2` and are not duplicated in `G.1`.

##### GPatternExtension — `G.1:Ext.ShortlistWiring`

**PatternScopeId:** `G.1:Ext.ShortlistWiring`
**GPatternExtensionId:** `ShortlistWiring`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `G.5`
**Uses:** `{G.5, G.4}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ShortlistId`
* `SCRId` *(assurance/rationale surface by id; semantics owned by the selector/assurance owners)*
* `DRRId?` *(when a decision‑rationale artefact is minted; otherwise omitted)*
* `TaskSignatureRef?` *(if selection is task‑templated; otherwise omitted)*
* `AcceptanceClauseId[]` *(as referenced from `G.4` outputs)*
* any explicit selector policy pins *(policy‑id/ref; owner‑defined)* when not defaulted (default ownership is routed via `G.Core.DefaultOwnershipIndex`)

**Notes (wiring‑only):** `G.1` does not redefine selection: it binds M4’s output surface to the `G.5` selector/dispatcher kernel.

##### GPatternExtension — `G.1:Ext.CreativityCHR`

**PatternScopeId:** `G.1:Ext.CreativityCHR`
**GPatternExtensionId:** `CreativityCHR`
**GPatternExtensionKind:** `DisciplineSpecific`
**SemanticOwnerPatternId:** `C.17`
**Uses:** `{C.17, G.3}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `CHRPackId?` *(if creativity characteristics are published/typed)*
* edition/policy pins required by the chosen creativity characteristic set (owned by `C.17`)

**Notes (wiring‑only):** `G.1` only records which creativity characteristics are used for M3/M4 wiring; legality/typing lives in the CHR owners.

##### GPatternExtension — `G.1:Ext.NQD`

**PatternScopeId:** `G.1:Ext.NQD`
**GPatternExtensionId:** `NQD`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `C.18`
**Uses:** `{C.18, C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `InsertionPolicyRef` *(policy id / ref, as defined by the owner)*
* `TaskSignatureRef?` *(when QD is enabled via TaskSignature flags/traits rather than by an external switch)*
* `DHCMethodRef.edition?` *(when illumination/coverage summaries are pinned to a method)*
* `EmitterPolicyRef` *(policy‑id/ref; points to the exploration governance owner, e.g., `C.19` when E/E‑LOG is used)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (wiring‑only):** QD/QD‑adjacent algorithm families and their parameterisations belong to `C.18/C.19`; `G.1` only fixes the pins needed to make the VariantPool and Shortlist reproducible.

##### GPatternExtension — `G.1:Ext.OpenEndedFamilyWiring`

**PatternScopeId:** `G.1:Ext.OpenEndedFamilyWiring`
**GPatternExtensionId:** `OpenEndedFamilyWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**SemanticOwnerPatternId:** `G.2` *(family semantics live in SoTA cards; this block only wires pins; selector‑side wiring is owned by `G.5`.)*
**Uses:** `{G.2, G.5, C.19, C.23}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GeneratorFamilyId[]`
* `TransferRulesRef.edition` *(mandatory when Open‑Ended is enabled)*
* `EnvironmentValidityRegionRef?`
* `CoEvoCouplerRef[]?`
* `SoSLogBranchId[]?` *(when validity of generated tasks is gated by explicit branches)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (wiring‑only):** this block enables portfolios of `{Environment, MethodFamily}` pairs without redefining generator semantics in `G.1`; it should cite/align with the selector‑side wiring in `G.5:Ext.OpenEndedFamilyWiring`.

##### GPatternExtension — `G.1:Ext.RefreshWiring`

**PatternScopeId:** `G.1:Ext.RefreshWiring`
**GPatternExtensionId:** `RefreshWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**SemanticOwnerPatternId:** `G.11`
**Uses:** `{G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `RefreshReadinessCardId`
* `RSCRTestId[]`
* canonical `RSCRTriggerKindId[]` emitted/recorded (aliases only as labels, if any)
**RSCRTriggerSetIds:** `{GCoreTriggerSetId.RefreshOrchestration}`
**Notes (wiring‑only):** M6 declares readiness and wiring; orchestration semantics (queueing, prioritisation, cadence) are owned by `G.11`.

##### GPatternExtension — `G.1:Ext.ShippingWiring`

**PatternScopeId:** `G.1:Ext.ShippingWiring`  
**GPatternExtensionId:** `ShippingWiring`  
**GPatternExtensionKind:** `GeneratorSpecific`  
**SemanticOwnerPatternId:** `G.10`  
**Uses:** `{G.10}`  
**⊑/⊑⁺:** `∅`  
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `CGFrameLibraryId`
* `SoTAPaletteDescriptionId`, `SoTA_SetId`
* `CHRPackId?`, `CALPackId?`, `SoS‑LOGBundleId?`, `ParityReportId?` *(as present in the library index)*
* `EvidenceGraphId?`, `BridgeMatrixId?`, `BridgeCalibrationTableId?` *(when cited by the shipped artefacts)*
* `UTSRowId[]?` *(when any public ids are minted/published)*
* `SlotFillingsPlanItemRef[]?` *(when planned baseline is bound by id into the shipment surface)*
**Notes (wiring‑only):** this block does not define shipping; it only records the minimum wiring from the chassis/library index to `G.10` when shipping is performed.

### G.1:5 - Archetypal Grounding — Tell–Show–Show (informative)

**Tell.** Use the six‑card chassis to make a CG‑Frame authoring effort reproducible: a scoped SoTA set, a traceable candidate pool, a set‑return shortlist, a publishable library index, and refresh readiness—without redefining contract/legality/selection/refresh owners.

**Show A (R&D multi‑criteria decisions; post‑2015 SoTA workflow).**

* **M1:** define `CG‑FrameContext` for “R&D decision options”, pin `CNSpecRef/CGSpecRef` editions, and publish `describedEntity` + `ReferencePlane`.
* **M2:** build `SoTA_SetId` via `G.2` using a living‑review style funnel (e.g., PRISMA‑like trace + update cadence) and publish UTS stubs for reusable constructs.
* **M3:** emit a `VariantPoolId` where each candidate cites its emitter policy and provenance; if QD is used, wire `DescriptorMapRef.edition` and `DistanceDefRef.edition` via `G.1:Ext.NQD`.
* **M4:** produce `ShortlistId` as a portfolio set via `G.5`, with acceptance predicates sourced from `G.4`.
* **M5:** publish a `CGFrameLibraryId` indexing the chosen CHR/CAL/LOG bundles and UTS rows; register RSCR tests.
* **M6:** declare refresh readiness (telemetry pins + canonical RSCR trigger kinds) and wire to `G.11`.

**Show B (clinical operations; safety‑first acceptability).**

* **M1:** scope a CG‑Frame around dose adjustment decisions; pin legality and evidence minima explicitly.
* **M2:** harvest SoTA models and safety constraints as a reconstructible set (owned by `G.2`).
* **M3:** generate policy‑constrained candidate protocols; emitter trace and evidence pins are mandatory.
* **M4:** shortlist remains a set; “choose one” is deferred to explicit policy, not silently baked into the generator.
* **M5/M6:** publish and wire refresh (decay events, policy changes, and evidence updates retrigger along the P2W path).

### G.1:6 - Bias‑Annotation (informative)

* **Recency bias:** “newest paper wins” (mitigate with explicit inclusion criteria and update cadence in `G.2` wiring).
* **Novelty bias:** over‑rewarding novelty at the expense of legality/assurance (mitigate by making acceptance and assurance pins explicit and owned).
* **Algorithmic favoritism:** baking a preferred generator into “the chassis” (mitigate by keeping M3 method‑agnostic and pushing methods into Extensions).
* **Scalarisation bias:** collapsing portfolios/partial orders into a single score (mitigate by set‑return discipline routed via `G.Core`).
* **Hidden‑crossing bias:** implicit reuse across contexts (mitigate by explicit crossing pins and Bridge‑only routing via `G.Core`).

### G.1:7 - Conformance Checklist (normative)

| ConformanceId     | Statement   |
| ----------------- | ----------- |
| **CC‑G1‑CoreRef** | The pattern MUST satisfy the **effective** `CoreConformanceIds` implied by `G.1:4.1` (`GCoreConformanceProfileId` expansion + deltas), per `G.Core` expansion rules.   |
| CC‑G1‑01          | The deliverable MUST include all six cards `M1…M6` with stable ids **and** a versioned kit manifest `CGKitId`, including at minimum: `{CGKitId, CG‑FrameContext, SoTAPaletteDescriptionId, SoTA_SetId, VariantPoolId, ShortlistId, CGFrameLibraryId, RefreshReadinessCardId}`.  |
| CC‑G1‑02          | `M1` MUST bind the kit to a single `CG‑FrameContext` and MUST expose the required pins from `GCorePinSetId.PartG.AuthoringMinimal` (including `describedEntity` and `CNSpecRef/CGSpecRef` editions). `M1` MUST also expose (or explicitly cite) a `ReferenceMap` surface and MUST NOT restate its semantics (cite `G.0:CG‑Spec.ReferenceMap`).  |
| CC‑G1‑03          | `M2` MUST be wired to `G.2` (or explicitly cite the `G.2` owner artefacts) and MUST be reconstructible as a scoped set, including `SoTAPaletteDescriptionId` + `SoTA_SetId` (not free‑floating prose). Provenance MUST be anchored via `A.10` for the emitted set.  |
| CC‑G1‑04          | `M3` MUST record emitter provenance as a wiring surface, including `EmitterPolicyRef` (policy‑id/ref), edition pins, and provenance anchors (via `A.10`). Any method‑specific fields MUST be introduced only via `GPatternExtension` blocks.   |
| CC‑G1‑05          | `M4` MUST be wired to `G.5` (or explicitly cite `G.5` owner artefacts) and MUST preserve set/portfolio outcomes. `SCRId` MUST be present (or explicitly cited to the owner surface) so assurance is id‑addressable; `DRRId` SHOULD be present when a decision‑rationale artefact is minted.   |
| CC‑G1‑06          | `M5` MUST publish a library/index surface that points to referenced CHR/CAL/LOG artefacts and to any minted public ids (`UTSRowId[]`, Name Cards) via the canonical owners (Part F), without introducing shadow specs (delegation target: `CC‑GCORE‑CN‑CG‑1` via `CC‑G1‑CoreRef`).    |
| CC‑G1‑07          | `M6` MUST publish `CGKitId` and expose refresh‑readiness wiring: canonical `RSCRTriggerKindId[]` applicability + minimal payload pins (including `SlotFillingsPlanItemRef[]` when applicable) and RSCR test ids; orchestration semantics MUST be cited to `G.11`.  |
| CC‑G1‑08          | Any method/discipline/generator specificity in `G.1` MUST be located in `G.1:4.4` as `GPatternExtension` blocks with `PatternScopeId`, `GPatternExtensionKind`, and `SemanticOwnerPatternId` (or `owner TBD` only for Phase‑3 seeds). If QD/illumination or Open‑Ended generator families are declared, the corresponding extension blocks MUST be present and MUST carry the owner‑required edition/policy pins. |


### G.1:8 - Common Anti‑Patterns and How to Avoid Them (informative)

* **Anti‑pattern: “Shadow CN/CG spec inside the chassis.”**
  *Avoid:* keep CN/CG as cited contract surfaces; use pins and owner references only.

* **Anti‑pattern: “Chassis hard‑codes a favourite algorithm.”**
  *Avoid:* keep M3 core method‑agnostic; add algorithm families only via Extensions with explicit owner patterns and edition pins.

* **Anti‑pattern: “Shortlist = one winner.”**
  *Avoid:* preserve set/portfolio returns; any singleton choice must be an explicit downstream decision rule (policy‑bound).

* **Anti‑pattern: “Refresh plan described as prose triggers.”**
  *Avoid:* record canonical `RSCRTriggerKindId` and payload pins; aliases only as labels and only if docked.

* **Anti‑pattern: “Packaging implies shipping ownership.”**
  *Avoid:* treat M5 as a library index; treat M6 as readiness wiring; ship only via `G.10`.

### G.1:9 - Consequences (informative)

* **Repeatable authoring:** CG‑Frame work becomes reconstructible: what exists, what it depends on, and how it is refreshed.
* **Method pluralism with discipline:** multiple generator/selector families can coexist without turning the chassis into a shadow method spec.
* **Better reuse:** outputs land directly in published artefacts (UTS/Name/RSCR‑ready) rather than remaining local notes.
* **Lower refactor cost:** method changes localise to Extensions; core invariants remain stable and single‑owner.

### G.1:10 - Rationale (informative)

* **Why six cards?** It matches the minimal decomposition needed to keep scope, harvesting, generation, selection, publication, and refresh **explicitly separable** (and thus auditable and evolvable).
* **Why “kit/index” rather than “pack”?** A CG‑Frame authoring effort must stay modular; shipping is a separate ownership boundary (`G.10`).
* **Why push method content into Extensions?** It prevents conflating (i) universal invariants, (ii) frame‑specific kit surfaces, and (iii) method/generator families—supporting Phase‑2 universalisation goals.
* **Why working‑model first?** Many CG‑Frames fail due to premature formalism; a chassis with didactic micro‑examples improves correctness of pins, names, and boundaries before deep formalisation.

### G.1:11 - SoTA‑Echoing (informative)

This chassis is designed to stay compatible with modern (post‑2015) practice without confusing “SoTA” with “currently popular”:

* **Evidence synthesis:** living systematic review workflows (e.g., PRISMA‑style traceability and update cadence) map naturally to M2 wiring owned by `G.2`.
* **Quality‑Diversity and archives:** modern QD families (MAP‑Elites‑class, CMA‑ME‑class, and related archive‑based exploration) fit as M3/M4 extensions (`C.18`/`C.19`) because they require explicit descriptor/distance/insertion pins and preserve set‑valued outcomes.
* **Open‑ended exploration:** post‑2015 open‑endedness systems (POET‑class, paired/adversarial environment generation lines, and modern curriculum‑generation approaches) fit when treated as generator‑family wiring (owned elsewhere) rather than as chassis semantics.
* **Set‑valued decision outputs:** modern multi‑objective and set‑valued evaluation practices align with the `G.Core` set‑return discipline, preventing hidden scalarisation.
* **Governed traceability:** contemporary reproducibility and accountability norms (mechanism disclosure, provenance anchors, and audit trails) are supported via pinned policies/editions and explicit module boundaries, without introducing data‑governance machinery.

### G.1:12 - Relations

**Builds on:** `G.Core`, `E.8`, `E.10`, `E.19`.
**Uses:** `A.10 (Provenance Anchors)`, `A.15.3 (SlotFillingsPlanItem)`, `A.19 (CN‑Spec)`, `G.0 (CG‑Spec)`, `G.2 (SoTA Synthesis Pack)`, `G.3 (CHR Pack@CG‑Frame)`, `G.4 (CAL Pack@CG‑Frame)`, `G.5 (Selector & Dispatch)`, `G.10 (Shipping)`, `G.11 (Refresh Orchestration)`, and (via Extensions) `C.17/C.18/C.19`.
**Publishes to / consumes from:** Part‑F publication surfaces (UTS, naming, RSCR tests, Role/Concept artefacts) as cited by their owners.

### G.1:End

## G.2 - SoTA Harvester & Synthesis

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative *(unless explicitly marked informative)*
>
> **Purpose.** Provide a repeatable, auditable way to **discover**, **triage**, and **synthesize** state‑of‑the‑art (SoTA) across competing `Tradition` lineages *before* minting CHR/CAL/LOG assets for a `CG‑Frame`.
> The primary output is a **`SoTA Synthesis Pack@CG‑Frame`** that feeds:
>
> * naming/publication (UTS),
> * CHR authoring (G.3),
> * CAL authoring (G.4),
> * method/generator registries and dispatch (G.5).
>
> **Scope note.** This pattern **owns** the harvesting + synthesis *generator* in Part G. Shipping ownership is in **G.10**, refresh orchestration ownership is in **G.11**.
>
> **Terminology note (normative).** In normative clauses below, **`Tradition`** refers to the *Tech* token `Tradition` (a plural lineage with internally coherent commitments). Plain “tradition” is allowed only as a 1:1 synonym.

### G.2:1 - Problem frame

A team extends FPF into a new `CG‑Frame`. The relevant literature is typically:

* **plural** (multiple `Tradition` lineages with incompatible commitments),
* **context‑sensitive** (results depend on `U.BoundedContext` and declared `describedEntity`),
* **method‑heterogeneous** (different evidence styles, operator sets, and validity regions),
* **time‑sensitive** (rapid drift post‑2015; frequent benchmark/protocol shifts).

Downstream Part‑G work (CHR/CAL/selection/shipping/refresh) depends on the team producing **consumable, citation‑ready artefacts** without collapsing semantic boundaries across contexts or planes.

### G.2:2 - Problem

How can we systematically assemble a SoTA view that is:

1. **pluralist but comparable** (plurality preserved; comparability is achieved only via explicit crossings),
2. **evidence‑addressable** (claims cite auditable evidence surfaces and anchors),
3. **actionable** (produces inventories and cards that G.3/G.4/G.5 can consume),
4. **refreshable** (editions/policies/windows are pinned so RSCR/refresh can re‑audit and re‑run without semantic drift)?

### G.2:3 - Forces

* **Pluralism vs. consolidation.** Consolidation is valuable, but unqualified fusion destroys meaning.
* **Breadth vs. load‑bearing depth.** Too broad becomes shallow; too deep misses rival lineages.
* **Recency vs. stability.** Freshness matters, yet durable “backbone” claims must be identified and kept visible.
* **Pedagogy vs. rigour.** Outputs must be teachable enough to support review, while remaining audit‑ready.
* **Authoring vs. operations.** This pattern lives in the authoring plane; operational runs and decisions belong to Work planes and to owner patterns.

### G.2:4 - Solution

#### G.2:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; routing hub)

**GCoreLinkageManifest (normative).**
*(Canonical form, Nil‑elision, and Expansion rule are defined in `G.Core`.)*

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
  },
  RSCRTriggerSetIds := {GCoreTriggerSetId.SoTAHarvestSynthesis},
  CorePinSetIds := {GCorePinSetId.PartG.CrossingVisibilityPins},

  CorePinsRequired := {
    // Scope pins (G.2‑specific)
    CG-FrameContext,
    Tradition[],
    describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
    SoTA_SetId,
    SoTAPaletteDescriptionId,

    // Evidence / provenance pins (G.2‑specific)
    CorpusLedgerId,
    FlowRecordId,
    EvidenceAnchorRef[],
    EvidenceGraphId?,

    // Crossing / synthesis pins (delta beyond CorePinSetIds; only when used)
    GammaEpistSynthId[]?,

    // Edition / policy pins (only when used)
    HarvestPolicyRef?,
    DistanceDefRef.edition?,
    InclusionCriteriaId?,
    ScreeningRubricId?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := ∅
⟩`

*(RSCR payload pins: `ClaimSheetId[]`, `SoTA_SetId`, `SoTAPaletteDescriptionId`, `BridgeMatrixId?`, `GammaEpistSynthId[]?`, `UTSRowId[]?`, `DistanceDefRef.edition?`, `HarvestPolicyRef?`, `InclusionCriteriaId?`, `ScreeningRubricId?`, `PathId/PathSliceId?` when path‑citable evidence or a stable freshness window is pinned.)*

**Pattern‑local default rules (owned by this pattern; not a Part‑G‑wide `DefaultId`).**

`FamilyCoverageFloorK := 3` *(unless explicitly overridden by `HarvestPolicyRef` and recorded in `FlowRecord`)* 

#### G.2:4.2 - Kit: `SoTA Synthesis Pack@CG‑Frame` (pattern‑owned surface)

A conforming `G.2` publication produces a **notation‑independent pack** whose internal organisation is free, but whose exported **named components / views** are stable and citable:

Each named component is addressable via a stable **pack‑local identifier** (e.g., `CorpusLedgerId`, `ClaimSheetId`, `FlowRecordId`) for citation and RSCR scoping. If any component is minted/evolved as a **public id**, it is published and cited via `UTSRowId[]` per `CC‑GCORE‑UTS‑1` (delegation).

0. **`SoTA_Set@CG‑Frame`** *(export view; “M2 output” consumed downstream)*  
   A read‑optimised view over the harvested candidate set that downstream generator/selector work treats as the “harvester output set”.  
   **Constraint (normative):** `SoTA_Set@CG‑Frame` **MUST** be reconstructible from pack components by id (no “hidden extra set”).

1. **`G.2a CorpusLedger`**
   Ledger of candidate sources with Context and triage status (e.g., include / park / retire) and explicit rationale hooks.

2. **`G.2b ClaimSheets[Tradition]`**
   Typed Claim Sheets per `Tradition`, each with:

* explicit home context and `describedEntity`,
* explicit evidence anchors/citations (A.10 and/or EvidenceGraph refs when available),
* explicit freshness window notes and risk/trust cues *(cite `B.3` owners when using trust/decay language)*.

3. **`G.2c OperatorAndObjectInventory`**
   Inventory of candidate CHR terms (characteristics/scales/coordinates) and candidate CAL operators/flows *as stubs* for downstream authoring.

4. **`G.2d BridgeMatrix`**
   A citable alignment/divergence surface across `Tradition`×`Tradition`, with explicit losses and row scopes.
   If any row asserts **cross‑source / cross‑`Tradition` substitution or fusion**, the pack **MUST** attach a `GammaEpistSynthId` record (alias: **`G.2‑F`**) per `G.2:Ext.GammaEpistSynthesis` (no silent fusion).

5. **`G.2e MicroExamples`**
   Worked micro‑examples for load‑bearing claims, each citing A.10 carriers, declaring context + `describedEntity`, and annotating assurance type(s) (`TA`/`VA`/`LA`, where applicable).

6. **`G.2f UTSProposals`**
   Draft Name Cards + Minimal Definitional Sheets (MDS) + alias proposals (incl. concept‑set linkage where applicable), with the required publication pins.

7. **`G.2g describedEntity Map`**
   Map from key terms/claims/public ids to `GroundingHolon`, `ReferencePlane`, and minimal reference cues for later CHR/CAL authoring.

8. **`G.2h PRISMA Flow Record`**
   A screening/eligibility trail for how sources entered the pack (method‑profile is allowed; see Extensions).  
   *(Name is historical; the artefact remains notation‑independent.)*

9. **`G.2i SoSIndicatorFamilies`**
   Indicator *families* as variants (windows/constraints/assumptions) **with explicit Acceptance branches per variant** (branch ids/labels only; threshold semantics belong to CAL owners).

10. **`G.2j MethodFamilyCards`**
    Candidate method families with a shared signature and a plurality of implementations, each with validity regions, cost/complexity notes, and known failure modes.
    When the pack targets downstream registry/dispatch, MethodFamily cards **SHOULD** include wiring stubs needed by `G.5` (eligibility predicate refs, assurance profile cues, and the pack ids that justify the family).

11. **`G.2k GeneratorFamilyCards`** *(if applicable)*
    Candidate generator families for environment/task generation with declared validity regions and transfer hooks.

12. **`G.2l Annexes`** *(optional; owner‑routed; see Extensions)*
    For example: QD/NQD annexes, discipline‑specific indicator annexes, interop forms.

**SoTAPaletteDescription** *(export view; required downstream)*  
A view‑friendly description object (pack‑local `SoTAPaletteDescriptionId`) that binds together:
* the `SoTA_Set@CG‑Frame` view,
* `ClaimSheetId[]`, `OperatorAndObjectInventory`, `BridgeMatrixId?`,
* `SoSIndicatorFamilies` (with variant/branch structure),
* `MethodFamilyCards` / `GeneratorFamilyCards?`,
* `MicroExamples`, `UTSProposals`,
* and the `describedEntity Map` for citation and later CHR/CAL authoring.  
**Note (normative intent):** this is the primary “consumable surface” for `G.3/G.4/G.5`; it prevents downstream patterns from scraping free prose.

**Editorial template: 1‑page “SoTA Sheet” per Tradition (informative).**  
When authoring `ClaimSheets[Tradition]`, teams often benefit from a single‑page template: scope + claims + evidence anchors + validity region + failure modes + freshness window + cross‑Tradition reuse notes + pointers to micro‑examples.

#### G.2:4.3 - Harvester loop (conceptual choreography; pattern‑owned)

A conforming `G.2` work product is built by iterating the following conceptual loop until the declared gates are satisfied:

1. **Declare scope and plurality.**
   Declare `CG-FrameContext`, the initial `Tradition` set, and the `describedEntity` surface for each intended claim region. Record these declarations in the pack pins (not as implicit assumptions).

2. **Discover and triage sources (ledger‑first).**
   Populate `CorpusLedger` via:

* seed sources,
* expansion via citation chaining and keyword family exploration,
* pruning using load‑bearing relevance tests tied to the declared CG‑Frame scope.

3. **Distill claims per `Tradition`.**
   For each `Tradition`, author a Claim Sheet that preserves internal commitments and cites evidence anchors. Do not fuse cross‑`Tradition` claims at this stage.

4. **Inventory operators/objects for downstream authoring.**
   Extract candidate measurement terms and operator stubs for later CHR/CAL authoring (without asserting legality or thresholds locally).

5. **Build alignment/divergence surfaces.**
   Where reuse across `Tradition` is desired, author Bridge‑backed alignment records and explicit loss notes in `BridgeMatrix`. Any consolidation is explicitly marked as requiring alignment proof.

6. **(Alias: G.2‑F) Produce Γ_epist synthesis records when fusion/substitution is asserted.**
   If a work product asserts cross‑source / cross‑`Tradition` fusion or substitution (beyond mere “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records per `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit object alignment refs + assurance tuple refs), and it **MUST** keep penalties routed to `R_eff` only by delegation (`CC‑GCORE‑PEN‑1`).

7. **Publish teachable micro‑groundings.**
   Attach worked micro‑examples to load‑bearing claims, each tied to A.10 carriers and declaring context + `describedEntity`.

8. **Apply gates and record repairs.**
   Enforce `FamilyCoverageFloorK` (and any optional diversity‑by‑distance gate). If a gate fails, the pack **MUST**:
   * record the failure and the repair iteration in `FlowRecord` and `CorpusLedger`,
   * pin the updated `HarvestPolicyRef` / criteria ids (if changed),
   * iterate the loop rather than silently weakening the gate.

9. **Emit hand‑off manifests and export views.**
   Produce explicit manifests to:

* `G.3` (CHR authoring),
* `G.4` (CAL authoring),
* `G.5` (registry/dispatch),
  so that downstream work can cite pack components by id rather than re‑authoring them.
   The pack **MUST** also export `SoTA_Set@CG‑Frame` and `SoTAPaletteDescription` as the default downstream consumption surfaces (ids pinned).

#### G.2:4.4 - Interfaces (minimal I/O Standard)

| Interface         | Consumes                                                      | Produces                                                                    |
| ----------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **G.2‑1 Harvest** | `CG-FrameContext`, initial `Tradition[]`, `HarvestPolicyRef?`  | `SoTA Synthesis Pack@CG‑Frame` (G.2a–G.2l)                                  |
| **G.2‑2 Extend**  | existing Pack + new sources/anchors + updated policy pins     | updated Pack + RSCR‑relevant trigger emissions (canonical kinds)            |
| **G.2‑3 HandOff** | Pack                                                          | `CHR‑handoff` (to G.3), `CAL‑handoff` (to G.4), `Registry‑handoff` (to G.5) |

*Note:* Orchestration of re‑runs is owned by `G.11`; this pattern only defines what a conforming (re)harvest produces and what pins it must expose.

#### G.2:4.5 - Extensions (pattern‑scoped; non‑core)

`Extensions` are pattern‑scoped modules. They do not introduce Part‑G‑wide norms; they provide wiring/pins and cite semantic owners.

###### G.2:4.5.1 - GPatternExtension: GammaEpistSynthesis

**PatternScopeId:** `G.2:Ext.GammaEpistSynthesis`  
**GPatternExtensionId:** `GammaEpistSynthesis`  
**GPatternExtensionKind:** `GeneratorSpecific`  
**SemanticOwnerPatternId:** `G.2` *(this pattern owns synthesis semantics; module exists for modularity + later extraction)*  
**Uses:** `{G.Core, B.3, F.9, G.6}` *(penalty routing + trust/decay cues + bridges/CL + evidence path citation when used)*  
**⊑/⊑⁺:** `∅`  
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GammaEpistSynthId[]` *(pack‑local ids of synthesis records; emitted iff fusion/substitution is asserted)*  
* `EvidenceAnchorRef[]` *(provenance union; A.10 carriers)*  
* `BridgeMatrixId` and `BridgeCardId[]` *(explicit object alignment references when crossing is involved)*  
* `CL/CL^plane` + `Φ/Ψ/Φ_plane policy-ids` *(ids only; semantics routed via owners; penalties → `R_eff` only by delegation)*  
* `PathId/PathSliceId?` *(only when citing via `G.6`)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`

**Notes (normative intent; duplication‑avoidant):**
* `Γ_epist^synth` is an auditable record that binds: (i) provenance union, (ii) explicit object alignment refs, (iii) assurance tuple refs (via existing owners) for each asserted fusion/substitution.  
* This module **does not** redefine `Γ‑fold`, `Φ`, or penalty semantics; it only requires the pins/refs needed for replayability and auditability (see `G.Core` delegations).

###### G.2:4.5.2 - GPatternExtension: HarvestProtocols

**PatternScopeId:** `G.2:Ext.HarvestProtocols`
**GPatternExtensionId:** `HarvestProtocols`
**GPatternExtensionKind:** `Phase3Seed`
**SemanticOwnerPatternId:** `owner TBD` *(Phase‑3 seed: harvesting protocol taxonomy not yet extracted into a dedicated owner)*
**Uses:** `{B.3, A.10}` *(for freshness/decay and provenance anchors, when protocol requires them explicitly)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `HarvestPolicyRef` *(declares the chosen protocol family and its parameters)*
* `FlowRecordId` *(protocol‑specific profile id or rubric id may be attached here)*
* `InclusionCriteriaId` / `ScreeningRubricId` *(ids only; semantics remain local to the protocol family)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (wiring‑only):**
* This module binds a declared protocol profile to the pack’s `FlowRecord` without redefining evidence semantics.

###### G.2:4.5.3 - GPatternExtension: DHCAlignmentHooks

**PatternScopeId:** `G.2:Ext.DHCAlignmentHooks`
**GPatternExtensionId:** `DHCAlignmentHooks`
**GPatternExtensionKind:** `DisciplineSpecific`
**SemanticOwnerPatternId:** `C.21` *(DHC semantics are owned by C.21)*
**Uses:** `{C.21, G.6, G.7}` *(DHC series + evidence path citations + bridge/CL regimes when alignment density is claimed)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DHCMethodRef.edition`
* `WindowRef?` *(if the DHC series is windowed)*
* `DHCSenseCellId[]` *(pack‑local ids for emitted DHC SenseCells; if any are public, cite via `UTSRowId[]`)* 
* `UTSRowId[]?` *(only if any DHC SenseCells / series ids are minted/evolved as public ids)*
* `PathId[]` / `PathSliceId[]` *(when alignment summaries cite evidence paths via G.6)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TelemetryDelta}`

**Notes (wiring‑only):**
* If DHC alignment summaries are emitted, this module ensures the DHC method edition and the cited evidence paths are visible.
* Units/constraints (semantic owner: `C.21`) must be **pinned, not redefined** here (e.g., `bridges_per_100_DHC_SenseCells`, `CL_min = 2` for cross‑Context counting, and the “CL=3 implies free substitution” interpretation when used).

###### G.2:4.5.4 - GPatternExtension: NQDAnnex

**PatternScopeId:** `G.2:Ext.NQDAnnex`
**GPatternExtensionId:** `NQDAnnex`
**GPatternExtensionKind:** `MethodSpecific`
**SemanticOwnerPatternId:** `C.18` *(NQD‑CAL semantics owned by C.18; explore/exploit logging by C.19 when used)*
**Uses:** `{C.18, C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `InsertionPolicyRef` *(policy‑id/ref)*
* `EmitterPolicyRef` *(policy‑id/ref)*
* `TaskSignatureRef?` *(when QD mode is trait‑gated)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (wiring‑only):**
* This module only pins the required references for replayability; it does not redefine QD semantics, dominance, or acceptance rules.

###### G.2:4.5.5 - GPatternExtension: InteropForms

**PatternScopeId:** `G.2:Ext.InteropForms`
**GPatternExtensionId:** `InteropForms`
**GPatternExtensionKind:** `InteropSpecific`
**SemanticOwnerPatternId:** `G.13`
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExternalIndexRef.edition`
* `ClaimMapperRef.edition`
* `MappingPolicyRef` *(policy‑id/ref)*
* `UTSRowId[]` *(for published external ids/aliases where relevant)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`

**Notes (wiring‑only):**
* Interop affects only representation and citation routes; it must not introduce alternate legality gates or acceptance semantics.

### G.2:5 - Archetypal Grounding (System / Episteme)

| Template element   | `U.System` illustration                                                                                                                                                                                                                                                  | `U.Episteme` illustration                                                                                                                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tell**           | A safety engineering team needs to choose a control stack across multiple engineering “schools” (robust control, learning‑based control, formal verification), under a declared operational context and a concrete `describedEntity` (the vehicle + operating envelope). | A research group must synthesize SoTA on “decision quality” across competing lineages (causal decision theory, evidential variants, bounded rationality, and active‑inference‑style formalisms), each with distinct evidence norms and semantics.       |
| **Show (failure)** | The team merges terms across contexts, treats incompatible test protocols as comparable, and collapses multiple partially ordered trade‑offs into one unqualified score. The resulting design cannot explain why a later safety review disagrees.                        | The group produces a single “best” metric of decision quality and retrofits definitions to fit it. Later, conflicting claims cannot be traced because evidence anchors and crossing losses were never made explicit.                                    |
| **Show (repair)**  | A conformant `G.2` pack keeps parallel Claim Sheets per `Tradition`, publishes explicit alignment/loss notes where reuse is attempted, and emits hand‑offs so CHR/CAL/selection can be authored without re‑inventing semantics.                                          | A conformant `G.2` pack preserves plural claims, publishes explicit bridge‑backed alignment where justified, represents indicators as families/variants, and makes evidence anchors and freshness windows visible so downstream re‑audits are possible. |

### G.2:6 - Bias-Annotation (informative)

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.

* **Selection bias (Gov/Onto).** Any harvesting protocol can over‑represent certain venues, languages, or evidence styles.
  *Mitigation:* pluralism floor + explicit `CorpusLedger` + explicit protocol pins.

* **Consolidation bias (Onto/Epist).** Pressure to “merge” lineages can erase incompatible commitments.
  *Mitigation:* keep Claim Sheets disjoint by default; require explicit alignment proof for fusion; preserve loss notes.

* **Recency bias (Prag).** Overweighting newest papers can hide durable backbone results; underweighting them misses SoTA drift.
  *Mitigation:* publish freshness windows and make them RSCR‑relevant.

* **Didactic bias (Did).** Micro‑examples can steer interpretation toward familiar domains.
  *Mitigation:* require heterogeneous substrates and explicit A.10 anchors.

### G.2:7 - Conformance Checklist (normative) — **CC‑G2**

| ConformanceId             | Requirement                                                                                                                                                                                                                                                                                                                                        | Purpose / Notes                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **CC‑G2‑CoreRef**         | A conforming `G.2` artefact **MUST** satisfy the **effective** core obligations declared by the `GCoreLinkageManifest` in `G.2:4.1` (per `G.Core` Expansion rule).                                                                                                                                                                                 | Phase‑2 bridge clause: ensures universal invariants are not redefined inside `G.2`. |
| **CC‑G2‑Pluralism‑1**     | A conforming pack **MUST** include at least **two** `Tradition` lineages and at least **three** distinct home `U.BoundedContext` entries across the corpus.                                                                                                                                                                                        | Prevents single‑lineage “SoTA” from masquerading as synthesis.                      |
| **CC‑G2‑Ledger‑1**        | A conforming pack **MUST** include `G.2a CorpusLedger` with inclusion/triage status and explicit rationale hooks per entry.                                                                                                                                                                                                                        | Makes discovery/triage auditable.                                                   |
| **CC‑G2‑FlowRecord‑1**    | A conforming pack **MUST** include `G.2h FlowRecord` that traces identification → screening → eligibility → included at a minimum granularity sufficient to reproduce the corpus boundary.                                                                                                                                                         | Prevents “mystery inclusion” and supports refresh.                                  |
| **CC‑G2‑ClaimSheets‑1**   | For each included `Tradition`, a conforming pack **MUST** include a `ClaimSheetId` that declares home context, `describedEntity`, evidence anchors, and freshness notes; it **MUST NOT** fuse cross‑`Tradition` claims by default.                                                                                                                 | Keeps plurality explicit and prevents hidden crossings.                             |
| **CC‑G2‑Palette‑1**       | A conforming pack **MUST** export `SoTA_Set@CG‑Frame` and `SoTAPaletteDescription` as citable views (via `SoTA_SetId`, `SoTAPaletteDescriptionId`) and ensure both are reconstructible from pack components by id (no hidden extra structure).                                                                                                      | Prevents downstream scraping of prose; keeps “M2 output” explicit.                  |
| **CC‑G2‑describedEntityMap‑1** | A conforming pack **MUST** include `G.2g describedEntity Map`, mapping (at minimum) each load‑bearing claim family and each minted/evolved public id to `describedEntity := ⟨GroundingHolon, ReferencePlane⟩`, and citing the relevant `ClaimSheetId` and evidence anchors (A.10 and/or G.6 paths when used).                                         | Keeps plane/holon boundaries explicit and citable.                                  |
| **CC‑G2‑Alignment‑1**     | Any cross‑`Tradition` consolidation **SHALL** be presented as either (i) disjoint parallel claims with explicit divergence, or (ii) an explicitly justified alignment proof; any reuse across `Tradition` boundaries **MUST** use explicit crossing surfaces per `CC‑GCORE‑CROSS‑1` (delegation).                                                  | Prevents silent semantic leakage.                                                   |
| **CC‑G2‑GammaSynth‑1**    | If the pack asserts cross‑source / cross‑`Tradition` **fusion/substitution** (not merely “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records satisfying `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit alignment refs + assurance tuple refs). If no fusion/substitution is asserted, the pack **SHALL** state so explicitly. | Restores the load‑bearing synthesis artefact (alias: `G.2‑F`) without shadow specs. |
| **CC‑G2‑Inventory‑1**     | A conforming pack **MUST** include `G.2c OperatorAndObjectInventory`, sufficient for downstream CHR/CAL authoring to begin without re‑harvesting terms.                                                                                                                                                                                            | Ensures the pack is actionable.                                                     |
| **CC‑G2‑Inventory‑2**     | `G.2c OperatorAndObjectInventory` entries **MUST** be treated as **stubs** for downstream authoring: they **MUST NOT** embed acceptance thresholds or claim legality decisions locally. If an entry is not a citation of an already‑owned CHR/CAL artefact, it **MUST** be explicitly marked as `stub` (typing/lawfulness `TBD`) and **MUST NOT** be used as if lawful. Legality/threshold semantics are routed to owner patterns (`G.3` for CHR, `G.4` for CAL) via explicit ids/pins. | Prevents “shadow CHR/CAL” and preserves lawfulness discipline without redefining it locally. |
| **CC‑G2‑MeasurementLawful‑1** | If any inventory entry is presented as **non‑stub** (i.e., already lawful/typed), the pack **MUST** cite the owning lawfulness discipline (e.g., `A.17–A.19/C.16` as applicable) and provide the minimal evidence anchors needed to justify that typing claim.                                                                                      | Prevents “quietly lawful” measurement claims inside the harvester pack.             |
| **CC‑G2‑MicroExamples‑1** | For every load‑bearing claim family, a conforming pack **MUST** include **at least two** worked micro‑examples on **heterogeneous substrates**, each with explicit A.10 carrier anchors, declared context + `describedEntity`, and an assurance tag (`TA`/`VA`/`LA`, where applicable).                                                          | Makes the synthesis teachable and anchor‑grounded.                                  |
| **CC‑G2‑UTS‑1**           | If the pack proposes or evolves any public ids, it **MUST** publish UTS proposals *(Name Cards + MDS where applicable)* and cite them via `UTSRowId[]`, satisfying `CC‑GCORE‑UTS‑1` (delegation).                                                                                                                                               | Keeps naming and evolution disciplined.                                             |
| **CC‑G2‑Families‑1**      | SoS indicators and candidate evaluation constructs **SHALL** be represented as **families/variants** (windows/constraints/assumptions) **with explicit Acceptance branch structure per variant** (branch ids/labels only), not as single unqualified scalars; any scalar summary **MAY** be included only as report‑only unless explicitly promoted by owner patterns. *(Set/portfolio discipline is delegated to `CC‑GCORE‑SET‑1`.)* | Prevents covert scalarization and keeps acceptance downstream-owned.                |
| **CC‑G2‑HandOff‑1**       | A conforming pack **MUST** emit hand‑off manifests to `G.3`, `G.4`, and `G.5` that cite pack components by id and identify which families/operators are intended for downstream formalisation or registry entry.                                                                                                                                   | Prevents downstream re‑authoring and drift.                                         |
| **CC‑G2‑CoverageGate‑1**  | The pack **MUST** declare `FamilyCoverageFloorK` and enforce it as a harvesting gate. It **MUST** either (i) specify `k` explicitly in an explicit `HarvestPolicyRef`, or (ii) use the pattern‑local default rule owned by `CC‑G2‑CoverageGate‑1`. *Default rule (owner‑local):* `k=3`. If the gate fails, the pack **MUST** (a) record the repair iteration in `FlowRecord`, and (b) broaden the search radius (new venues/corpora/contexts/traditions) rather than silently weakening the gate; if an exploration policy is used for this broadening, it **MUST** be pinned as a policy id/ref. | Makes “coverage floor” explicit and prevents “silent narrowing” under failure.      |
| **CC‑G2‑DistanceGate‑1**  | If a diversity‑by‑distance gate is used, the pack **MUST** pin `DistanceDefRef.edition` and the declared threshold (δ), and treat edits as RSCR‑relevant per `CC‑GCORE‑TRIG‑*` (delegation). If no such gate is used, the pack **SHALL** explicitly state that it is not used.                                                                     | Avoids implicit distance defaults and improves refreshability.                      |
| **CC‑G2‑RSCR‑1**          | A conforming pack **MUST** emit canonical `RSCRTriggerKindId` causes (not free text) for edits to evidence surfaces, name/tokenization surfaces (e.g., UTS proposals/aliases), crossings, planes, edition pins, and harvesting policy pins (`HarvestPolicyRef`), per `CC‑GCORE‑TRIG‑1…TRIG‑4` (delegation).                                                                                      | Keeps refresh reason codes stable and typed.                                        |
| **CC‑G2‑Ext‑GammaEpist‑1** | If `G.2:Ext.GammaEpistSynthesis` is used (i.e., any fusion/substitution is asserted), the pack **SHALL** expose the required pins listed in that extension and **SHALL NOT** redefine `Γ‑fold/Φ/penalty` semantics locally (route via owners by delegation).                                                                                       | Keeps synthesis auditable without creating shadow specs.                            |
| **CC‑G2‑Ext‑HarvestProtocols‑1** | If `G.2:Ext.HarvestProtocols` is used, the pack **SHALL** expose the required pins/criteria ids listed in that extension and **SHALL NOT** redefine evidence/quality semantics outside the declared protocol profile.                                                                                                                            | Keeps protocol variation modular and Phase‑3‑extractable.                           |
| **CC‑G2‑Ext‑DHC‑1**       | If `G.2:Ext.DHCAlignmentHooks` is used, the pack **SHALL** (a) expose the required pins listed in that extension, including `DHCSenseCellId[]`, and (b) declare the unit/constraint pins required by `C.21` (e.g., `bridges_per_100_DHC_SenseCells`, `CL_min=2`) without redefining their semantics locally (semantic owner: `C.21`).                                                             | Keeps DHC wiring auditable and non‑shadowing.                                       |
| **CC‑G2‑Ext‑NQD‑1**       | If `G.2:Ext.NQDAnnex` is used, the pack **SHALL** expose the required pins/editions/policies listed in that extension and **SHALL NOT** redefine QD semantics locally.                                                                                                                                                                             | Keeps QD/OEE wiring replayable and modular.                                         |
| **CC‑G2‑Ext‑Interop‑1**   | If `G.2:Ext.InteropForms` is used, the pack **SHALL** expose the required interop pins and **SHALL NOT** introduce alternative legality/acceptance semantics.                                                                                                                                                                                      | Prevents “foreign gate” shadowing.                                                  |

### G.2:8 - Common Anti‑Patterns and How to Avoid Them

* **AP‑G2‑1: “One true SoTA score.”**
  **Avoid:** selecting a single unqualified scalar metric as “the” SoTA.
  **Do instead:** represent evaluation constructs as families/variants; keep partial orders set‑returning (delegated).

* **AP‑G2‑2: Fusion without explicit alignment proof.**
  **Avoid:** merging rival `Tradition` claims into one statement “by common sense.”
  **Do instead:** preserve parallel Claim Sheets; if consolidation is required, publish explicit alignment proof or keep a divergence record.

* **AP‑G2‑3: Hidden protocol drift.**
  **Avoid:** changing the harvesting protocol (inclusion criteria, windowing, screening rubric) without pins.
  **Do instead:** pin harvesting policy/profile ids and treat changes as RSCR‑relevant.

* **AP‑G2‑4: Unanchored pedagogy.**
  **Avoid:** micro‑examples without carriers (they become folklore).
  **Do instead:** bind micro‑examples to A.10 anchors and declare `describedEntity`.

### G.2:9 - Consequences

* **Positive:** Downstream CHR/CAL/dispatch work becomes faster and less ambiguous because the pack is citable and structured.
* **Positive:** Plurality is preserved while still enabling disciplined comparability through explicit crossings.
* **Positive:** Refresh becomes tractable because pins and typed causes exist.
* **Negative:** Adds authoring overhead (ledger, flow record, micro‑examples, explicit pins).
* **Negative:** Requires governance discipline to prevent the pack from becoming an uncontrolled “everything bucket”.

### G.2:10 - Rationale

SoTA synthesis is a bottleneck for new `CG‑Frame` work: without a disciplined harvest, downstream formalization (CHR/CAL) and operational selection (G.5) either (i) inherit hidden semantic collisions, or (ii) re‑invent incompatible “mini‑standards.”
`G.2` resolves this by treating SoTA work as a **publishable kit**: explicit plurality, explicit crossings, explicit evidence anchors, and explicit hand‑offs.

### G.2:11 - SoTA-Echoing (informative)

This pattern aligns its *method options* (via Extensions and authoring practice) with widely used post‑2015 SoTA practices, while keeping FPF’s semantics stable and id‑based:

1. **PRISMA 2020 reporting discipline** (Page et al., 2021)
   *Status:* **Adopt (adapted)** — we adopt the idea of a transparent screening trail as `FlowRecord`, but keep it notation‑independent and concept‑level.

2. **Living systematic reviews** (Elliott et al., 2017 and subsequent living‑review practice)
   *Status:* **Adopt (as optional protocol family)** — the “living” stance is expressed as a harvesting protocol profile (Extension), with explicit freshness windows and RSCR‑relevant change causes.

3. **AMSTAR 2 critical appraisal** (Shea et al., 2017)
   *Status:* **Adapt** — we adapt the idea of structured quality appraisal into Claim Sheet evidence cues, without turning it into a single scalar rating.

4. **Science of Science synthesis** (Fortunato et al., 2018)
   *Status:* **Adopt (as content discipline)** — SoS indicators are treated as families/variants and wired as citable artefacts, not as a single “score”.

5. **Disruption / team‑structure indicators** (Wu, Wang & Evans, 2019 and follow‑on work)
   *Status:* **Adopt (as exemplar family)** — useful as an example of a SoS‑indicator family with strong dependence on windowing and corpus definition.

6. **Quality‑Diversity and open‑ended generation** (e.g., Fontaine et al., 2020 for CMA‑ME; Wang et al., 2019 for POET)
   *Status:* **Adopt (as optional annex wiring)** — when QD/OEE is relevant for the `CG‑Frame`, we include generator/method family cards and pin the required edition/policy surfaces via `G.2:Ext.NQDAnnex`, without embedding those semantics into the core pack.

### G.2:12 - Relations

* **Builds on:**

  * `G.Core` (core invariants, typed RSCR causes, default ownership routing)
  * `E.8` (pattern template discipline)
  * `E.10` (lexical/ontological rules; strict distinction; kind‑suffix discipline)
  * `E.19` (conformance discipline)
  * `A.10` (provenance anchors / carriers)
  * `B.3` (trust, freshness/decay as cited owners)
  * `F.9` (bridges and CL as cited owners)
  * `F.17` (UTS publication discipline; via delegation)
  * `G.0` (CG‑Spec legality gate; cited when legality surfaces are referenced)
  * `G.6` (EvidenceGraph / path citation surfaces when used)

* **Used by:**

  * `G.1` (generator chassis consumes harvested SoTA sets)
  * `G.3` (CHR authoring consumes operator/object inventory and claim sheets)
  * `G.4` (CAL authoring consumes operator stubs, acceptance branch scaffolding)
  * `G.5` (registry/dispatch consumes MethodFamily/GeneratorFamily cards)
  * `G.10` (shipping cites the pack as payload)
  * `G.11` (refresh orchestration can re‑invoke harvest via typed causes)

* **Relates to:**

  * `G.13` (interop surfaces when external indices are used)

### G.2:End

## G.3 - CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates

**Tag.** Architectural pattern (CHR kit; publishes lawful measurement primitives; constrains CAL authoring and selector/dispatch use)
**Stage.** *design‑time* (authoring & publication; enables lawful run‑time consumption by `G.4` / `G.5`)
**Primary output.** `CHR Pack@CG‑Frame` — a notation‑independent, UTS‑published CHR bundle that provides: typed Characteristics/Scales/Levels/Coordinates, legality + guard surfaces, aggregation/comparison specs, RSCR hooks/tests, and provenance pins.
**Primary hooks.** `G.1` (CG‑FrameContext), `G.2` (SoTA synthesis inputs), `A.19.CHR` (CHRMechanismSuite boundary + pins), `A.15.3` (SlotFillingsPlanItem baseline), `A.18/C.16` (MM‑CHR legality), `F.1–F.9` (Contexts/UTS/Bridges), `B.3` / `B.3.4` (trust, freshness/decay), `A.10` (provenance anchors/carriers), `G.6` (EvidenceGraph/Path citation), optional `C.18/C.19` (QD/OEE wiring), `G.11` (refresh orchestration).
**Non‑duplication note.** Universal Part‑G invariants (bridge‑only crossings, tri‑state semantics, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR triggers + alias docking, single‑owner defaults, linkage discipline) are owned by `G.Core`. This pattern cites them via `G.3:4.1` and delegates where needed.

### G.3:1 - Problem frame

A team is defining or evolving a `CG‑Frame` (via `G.1`) and has plural, competing SoTA traditions and constructs (via `G.2`). The team needs a *lawful characterization layer* that makes downstream work possible without hidden semantic drift:

* **CAL authoring (`G.4`)** needs typed, lawful operands and guard/legality surfaces to build admissibility and acceptance rules (thresholds and policy cut‑offs remain CAL‑owned).
* **Selector/dispatch (`G.5`)** needs CHR‑typed quantities and explicit provenance pins so selection can remain set‑returning and auditable under lawful orders.
* **Cross‑context reuse** must be explicit (bridges + loss accounting + pinned policy ids), and refresh must be tractable by typed RSCR causes rather than prose.

The deliverable is a **CHR Pack** that is **CG‑Frame‑scoped**, **notation‑independent**, and **UTS‑published**, with explicit edition/policy pins sufficient for reproducibility and RSCR.

### G.3:2 - Problem

Without a disciplined CHR authoring layer, teams repeatedly produce “measurable slots” that are *numerically manipulable but semantically unlawful*:

* **Meaning leaks** across contexts (same token, different referent/sense).
* **Illicit arithmetic** (e.g., averaging ordinals, mixing units, laundering polarity).
* **Hidden normalizations** that silently change scale type, polarity, or admissible transforms.
* **Unreproducible comparisons** (missing edition pins for methods/distances/policies; unclear reference plane).
* **Unscoped reuse** (no explicit bridge/loss notes; unclear `describedEntity` changes).
* **Un-auditable aggregation** (no explicit legality/guard surface; no proof hooks; unclear Γ‑fold ownership).
* **Refresh chaos** (changes in names/editions/policies do not map to typed RSCR causes).

### G.3:3 - Forces

| Force                                             | Tension                                                                        |
| ------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Pluralism vs comparability**                    | Preserve tradition‑specific meaning ↔ enable lawful cross‑tradition use.       |
| **Expressiveness vs legality**                    | Model rich measurement semantics ↔ block illegal operations “by construction”. |
| **Portability vs honesty**                        | Encourage reuse ↔ forbid implicit crossings and hidden loss.                   |
| **Ease of authoring vs auditability**             | Keep authoring teachable ↔ require explicit pins, provenance, and tests.       |
| **Downstream flexibility vs upstream discipline** | Let CAL/selector choose policies ↔ keep thresholds/policy cut‑offs out of CHR. |

### G.3:4 - Solution — CHR authoring kit and publication surface

#### G.3:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; routing/delegation hub)

**GCoreLinkageManifest (normative; size‑controlled).**

`GCoreLinkageManifest := ⟨
CoreConformanceProfileIds := {
GCoreConformanceProfileId.PartG.AuthoringBase,
GCoreConformanceProfileId.PartG.TriStateGuard,
GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
},
CorePinSetIds := {
GCorePinSetId.PartG.AuthoringMinimal,
GCorePinSetId.PartG.CrossingVisibilityPins
},

// Pins strengthened for CHR authoring (delta over PinSets)
CorePinsRequired := {
// NOTE: `CG-FrameContext`, `describedEntity`, `CNSpecRef.edition`, `CGSpecRef.edition` are already required
// by `GCorePinSetId.PartG.AuthoringMinimal` (cite, don’t restate here).
UTSRowId[],                      // required: CHR terms are public ids (Name Cards + lifecycle)
PathId[]/PathSliceId[],          // required: worked examples/tests and refresh anchoring cite paths
ReferencePlane,                  // required: definitional claims are plane-scoped
Φ/Ψ/Φ_plane policy-ids?,         // iff crossings/plane moves are exercised in examples or imports
ΓFoldRef.edition?                // iff an explicit Γ-fold artefact is pinned (otherwise use DefaultId)
// NOTE: method-/discipline-specific pins (e.g., DescriptorMapRef/DistanceDefRef/DHCMethodRef/InsertionPolicyRef)
// are declared only inside Extensions (e.g., `G.3:Ext.QD_OEE_Wiring`) to keep core linkage universal.
},

// consumed iff any published `CHR.AggregationSpec` relies on default Γ-fold (no explicit override pinned)
DefaultsConsumed := { DefaultId.GammaFoldForR_eff },

RSCRTriggerKindIds := {
RSCRTriggerKindId.EvidenceSurfaceEdit,
RSCRTriggerKindId.TokenizationOrNameChange,
RSCRTriggerKindId.CrossingSurfaceEdit,
RSCRTriggerKindId.ReferencePlaneEdit,
RSCRTriggerKindId.EditionPinChange,
RSCRTriggerKindId.PolicyPinChange,
RSCRTriggerKindId.DefaultOwnerChange,
RSCRTriggerKindId.FreshnessOrDecayEvent,
RSCRTriggerKindId.LegalitySurfaceEdit,
RSCRTriggerKindId.BaselineBindingEdit
}
⟩`

*(Nil‑elision + expansion rule are per `G.Core:4.2`. This pattern does not redefine the semantics of core conformance ids, trigger kinds, or defaults; it only declares applicability and required pins.)*

#### G.3:4.2 - Output surface: `CHR Pack@CG‑Frame` (normative)

`CHR Pack@CG‑Frame` is the CHR kit payload that downstream patterns cite and pin (it is not a “shadow spec” for CN/CG).

**Minimum exported objects (kit surface):**

* `CHR.Characteristic[]`
* `CHR.Scale[]`
* `CHR.Level[]` *(when the scale type requires explicit level sets / order structure)*
* `CHR.Coordinate[]` *(encodings + legality annotations; never an implicit “upgrade” of measurement structure)*
* `CHR.Guards` *(guard macro surface; semantics routed to owners; see `G.Core` + `A.18`)*
* `CHR.LegalityMatrix` *(admissible operations per scale type / unit / polarity regimes)*
* `CHR.AggregationSpecs` *(typed aggregators/comparators + proof hooks + edition pins where applicable)*
* `UTS` publication bundle: Name Cards (twin labels), lifecycle notes, and (when applicable) bridge/loss notes
* RSCR artefacts: `RSCRTestId[]` + worked examples + provenance pins (ReferencePlane, Path/PathSlice, policy ids)

**Mandatory provenance pins (conceptual, notation‑independent):**

* `ReferencePlane`
* `PathId/PathSliceId` citations for worked examples/tests
* R‑anchors (conceptual; KD‑CAL lanes when used) realised via `PathId/PathSliceId` and, where applicable, `A.10` anchor/carrier refs
* policy pins used by crossings or plane moves (when exercised)
* edition pins for any referenced method or metric definitions that affect interpretation

#### G.3:4.3 - Authoring workflow: CHR authoring chassis (S1–S8)

**S1 — Charter the measurement scope (scope anchor).**
Declare the CHR home context/scope for the CG‑Frame, including: `describedEntity` boundaries, `ReferencePlane`, freshness/decay expectations, and the list of contested terms likely to require bridging. Output a design‑time `MeasurementCharter` and `KindMap@Context`.
If freshness/decay expectations are anything beyond an explicit “non‑decaying” declaration, wire them via
`G.3:Ext.DecayWiring` (semantic owner: `B.3.4`) rather than encoding decay semantics in CHR prose.
If assurance‑subtype lane tags are used (e.g., TA/VA/LA), declare the lane regime here so downstream evidence discipline can remain lane‑pure (taxonomy/semantics owned by `B.3`; evidence‑path representation & audit owned by `G.6`; this pattern only records wiring).
**Lane docking (wiring‑only; normative).**
If `EvidenceLanes` are used, the charter MUST:
* enumerate the lane tags used (e.g., TA/VA/LA) and cite their semantic owner taxonomy (owner: `B.3`), plus the upstream provenance for their use when available (e.g., `SoTAPaletteDescriptionId` via `G.3:Ext.SoTAPackInputs`);
* expose any lane‑dependent tolerances / proof requirements via explicit pins (policy‑id and/or edition‑pinned refs), not prose;
* treat lane tags as provenance metadata (not Contexts): they MUST NOT be “bridged away” or silently mixed;
* if any cross‑lane comparison/aggregation is claimed, it MUST be explicit and pinned to the owning acceptance/evidence policy (typically `G.4`) and auditable via evidence paths (`G.6`); otherwise downstream consumers treat it as illegal.
*Crossing semantics and penalty routing are cited via `G.Core` (do not restate).*

**S2 — Mint or reuse terms (UTS‑first).**
For each candidate characteristic/scale/level/coordinate term: attempt reuse; otherwise mint via UTS Name Cards with twin labels and lifecycle notes. When a term is imported across contexts, the import must be explicit and auditable (bridge/loss notes live with the crossing artefacts; CHR only cites them).

**S3 — Define `CharacteristicCard` (the CHR unit of meaning).**
A CharacteristicCard is the minimum unit CHR publishes for downstream legality. It SHOULD include (field names are indicative; semantics routed to owners):

`CharacteristicCard := ⟨
  UTSRowId,
  Context,
  ReferencePlane,
  ObjectKind,
  Intent,
  Definition (typed),
  ObservableOf := ⟨instrument/protocol (A.10 anchors/carriers), uncertainty model, validity window⟩,
  EvidenceLanes? (KD‑CAL lanes; wiring only; semantics owned by `G.4` / `G.6`),
  ScaleRef,
  Polarity ∈ {↑, ↓, ⊥},
  Domain/Range,
  UnitSet,
  Bounds / zero semantics (as applicable),
  Freshness / half‑life (or explicit `NonDecayingDecl`; freshness/decay semantics owned by `B.3.4`),
  Missingness semantics (typed; include a classification/mapping when non‑trivial; downstream tri‑state handling is per G.Core),
  Stability/Reliability notes,
  RoleDecls? := RoleDecl[] (wiring‑only; each role declaration names its semantic owner + required pins; see `G.3:4.5`),
  QD.Role? ∈ {Q, D, QD-score} (interop alias for `RoleDecl` with `SemanticOwnerPatternId = C.18`; see `G.3:Ext.QD_OEE_Wiring`),
  Micro‑examples (R‑anchors: Path/PathSlice cited; lane tags where applicable)
⟩`

Where `RoleDecl := ⟨ roleLabel, SemanticOwnerPatternId, EditionPins?, PolicyPins? ⟩` (wiring‑only; semantics owned by `SemanticOwnerPatternId`).

Rules (CHR‑owned intent, semantics routed where indicated):

* Scale/unit/polarity legality obligations are **routed** to MM‑CHR owners (`A.18/C.16`) and must be *checkable* by downstream patterns.
* Missingness must be typed so downstream can apply tri‑state outcomes without silent coercion (tri‑state semantics are owned by `G.Core`).
* If `EvidenceLanes` are recorded, they are only lane tags for downstream evidence discipline (taxonomy owner: `B.3`; audit surface: `G.6`; any cross‑lane policy is owned by `G.4`); this pattern does not introduce lane semantics or invent bridge‑like constructs.
* If `RoleDecls` are used, each declaration MUST cite its semantic owner pattern (e.g., `C.18/C.19`) and surface the edition/policy pins required by that owner; CHR does not define role semantics locally.
* **Role docking (normative, wiring-only):** if any `RoleDecl` is present with `SemanticOwnerPatternId = X`,
  then `G.3` MUST include (or explicitly cite) a corresponding `GPatternExtension` block whose owner is `X`
  (or whose `Uses` includes `X`) and that surfaces the required pins for that role family. Otherwise the role
  declaration is non-conformant (it is an undocked semantic fragment).
* **Freshness docking (normative, wiring-only):** if a characteristic’s freshness/half-life is defined via a named
  decay model/policy (rather than a pure local statement), the relevant policy/ref MUST be pinned and routed to `B.3.4`
  via `G.3:Ext.DecayWiring`.
* If a characteristic is intended to be *promoted into* `CG‑Spec`, the linkage is explicit and edition‑pinned (wiring lives in an Extension; semantics owned by `G.0`).

**S4 — Define `ScaleCard` and `LevelCard` (lawful measurement).**
Publish the scale type and admissible transforms, plus levels/orders when applicable. CHR does not invent new legality semantics; it cites MM‑CHR owners and makes the legality surface concrete for the frame’s characteristics.

Typical distinctions that must be representable:

* **Nominal / categorical:** equality + counting; transforms are permutations.
* **Ordinal:** order‑preserving transforms; no arithmetic that presupposes intervals.
* **Interval:** affine transforms; differences meaningful; means may be lawful if justified.
* **Ratio:** positive scalar transforms; ratios meaningful; products/sums subject to unit discipline.
* **Count / rates:** explicit exposure/timebase requirements; rate conversions must be explicit.
* **Cyclic:** wrap‑around discipline + principal interval declaration.

**S5 — Define `CoordinatePolicy` (encodings without hidden cardinalization).**
When a numeric coordinate/embedding is used for convenience or tooling, CHR MUST publish:

* what invariants are preserved (order only / ratios / topology / wrap‑around),
* what remains illegal,
* what proof hooks are required if a stronger structure is claimed.

A coordinate never silently upgrades a scale type; if an upgrade is claimed, the proof burden is explicit and routed to MM‑CHR owners.

**S6 — Publish legality + guard surfaces (Guard Macros + LegalityMatrix).**
CHR publishes a `CHR.LegalityMatrix` and a `CHR.Guards` surface that downstream operators can reference.

Guard macro names are allowed as authoring ergonomics, but their semantics MUST be routed (no “shadow semantics” in this pattern). Examples of macro intents (owners in parentheses):

* `CSLC_PROOF_REQUIRED(x)` (MM‑CHR legality owners: `A.18/C.16`)
* `UNKNOWN_TRI_STATE(x)` (tri‑state semantics owner: `G.Core`)
* `UNIT_CHECK(x)` (MM‑CHR legality owners)
* `RETURN_SET_FOR_PARTIAL_ORDERS()` (set‑return semantics owner: `G.Core`)
* `METRIC_EDITION_REF(...)` (edition‑pin discipline owner: `G.Core`; metric semantics owner: `C.18`/`C.21` as applicable)

**S7 — Publish `AggregationSpecs` (typed, lawful, reproducible).**
CHR may publish typed aggregation/comparison specs that are *safe by construction* and usable as building blocks by `G.4` and `G.5`. For any published spec:

* The legality regime is explicit (scale/unit/polarity constraints + required proof hooks).
* If a contributor folding policy (Γ‑fold) is used and not explicitly overridden, it is referenced via `DefaultId.GammaFoldForR_eff` (single‑owner routing is via `G.Core.DefaultOwnershipIndex`; do not restate defaults here).
* If method‑role declarations imply metric‑driven comparisons (e.g., QD roles), the relevant edition/policy pins are surfaced (wiring lives in an Extension; semantics owned by the referenced patterns).

**S8 — Publish, test, and evolve (UTS + RSCR readiness).**
Publish the CHR pack and associated Name Cards to UTS. Attach:

* RSCR tests that check legality/guard coverage and reject illegal ops,
* worked examples with Path/PathSlice provenance,
* refresh/decay notes and deprecations with lexical continuity.

This step prepares the RSCR loop but does not own orchestration (owner: `G.11`).

#### G.3:4.4 - Interfaces (normative)

| Interface                           | Consumes                                          | Produces                                                         |
| ----------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------- |
| **G.3‑1 Charter_CHR**               | `CG‑FrameContext` (`G.1`), SoTA inputs (`G.2`)    | `MeasurementCharter`, `KindMap@Context`                          |
| **G.3‑2 MintOrReuse_Terms**         | candidate terms + UTS registry                    | Name Cards + UTS ids for `Characteristic/Scale/Level/Coordinate` |
| **G.3‑3 Define_Characteristic**     | `MeasurementCharter`, candidate semantics         | `CHR.Characteristic[]` (CharacteristicCards)                     |
| **G.3‑4 Define_ScaleLevel**         | CharacteristicCard + MM‑CHR rules                 | `CHR.Scale[]`, `CHR.Level[]`                                     |
| **G.3‑5 Define_CoordinatePolicy**   | Scale/Level + use‑case constraints                | `CHR.Coordinate[]` + legality annotations                        |
| **G.3‑6 Publish_GuardsAndLegality** | Scale/Level/Coordinate set                        | `CHR.Guards`, `CHR.LegalityMatrix`                               |
| **G.3‑7 Publish_AggregationSpecs**  | CHR set + legality hooks + (optional) metric refs | `CHR.AggregationSpecs` (+ proofs/refs + pins)                    |
| **G.3‑8 Publish_CHRPack**           | all CHR artefacts + tests/examples                | `CHR Pack@CG‑Frame` + UTS rows + RSCR tests                      |

#### G.3:4.5 - Extensions (pattern‑scoped; non‑core)

All blocks below are `GPatternExtension` modules (PatternScopeId‑scoped; **not** new PatternIds). They store wiring only and cite semantic owners.

**GPatternExtension: SuiteBoundaryLinkage**

* **PatternScopeId:** `G.3:Ext.SuiteBoundaryLinkage`
* **GPatternExtensionId:** `SuiteBoundaryLinkage`
* **GPatternExtensionKind:** `InteropSpecific`
* **SemanticOwnerPatternId:** `A.19.CHR`
* **Uses:** `{A.19.CHR, A.15.3}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CHRMechanismSuiteDescriptionRef.edition?` *(when the suite description is cited as a reproducibility baseline)*
  * `CHRMechanismSuiteSlotFillingsPlanItem` refs *(when planned baseline binds CHR artefacts into WorkPlanning)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.BaselineBindingEdit, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring‑only):** This module binds CHR authoring outputs to the P2W seam (`SlotFillingsPlanItem`); suite semantics and membership are owned by `A.19.CHR`.

**GPatternExtension: SoTAPackInputs**

* **PatternScopeId:** `G.3:Ext.SoTAPackInputs`
* **GPatternExtensionId:** `SoTAPackInputs`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **SemanticOwnerPatternId:** `G.2`
* **Uses:** `{G.2}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `ClaimSheetId[]` / operator & object inventory refs (as cited inputs)
  * `SoTAPaletteDescriptionId?` (when palette/traces are cited; used to dock contested‑term inventory and (if present) lane tags/tolerances)
  * `BridgeMatrixId?` (when terms/constructs are imported across traditions)
  * `UTSRowId[]` drafts/aliases from synthesis
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.CrossingSurfaceEdit}`
* **Notes (wiring‑only):** SoTA pluralism inputs are owned by `G.2`; this module only specifies which synthesis artefacts are cited while authoring CHR.

**GPatternExtension: CGSpecPromotionWiring**

* **PatternScopeId:** `G.3:Ext.CGSpecPromotionWiring`
* **GPatternExtensionId:** `CGSpecPromotionWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **SemanticOwnerPatternId:** `G.0`
* **Uses:** `{G.0}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CGSpecRef.edition` *(when a characteristic is promoted/linked into `CG‑Spec`)*
  * `CHR.Characteristic.id` pointers included in `CG‑Spec.Characteristics := [...]` *(no shadow ids; CG‑Spec stores pointers, see `G.0`)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
* **Notes (wiring‑only):** Promotion semantics and legality gate ownership stay with `G.0`; CHR only pins and cites.

**GPatternExtension: MMCHRLegalityWiring**

* **PatternScopeId:** `G.3:Ext.MMCHRLegalityWiring`
* **GPatternExtensionId:** `MMCHRLegalityWiring`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **SemanticOwnerPatternId:** `A.18`
* **Uses:** `{A.17, A.18, C.16}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * CSLC legality proof anchors/carriers (ids/refs as defined by MM‑CHR owners; cite `A.18/C.16`)
  * Unit coherence references (where units exist)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (wiring‑only):** This module wires CHR artefacts to MM‑CHR legality proof obligations; legality semantics are owned by the referenced patterns.

**GPatternExtension: DecayWiring**

* **PatternScopeId:** `G.3:Ext.DecayWiring`
* **GPatternExtensionId:** `DecayWiring`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **SemanticOwnerPatternId:** `B.3.4` *(freshness/decay semantics)*
* **Uses:** `{B.3.4, G.6}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `FreshnessWindowDeclRef` *(or equivalent window pin, as defined by the owner)*
  * `DecayPolicyIdRef?` *(policy-bound; if decay model is referenced by id)*
  * `PathSliceId[]` *(affected evidence carriers / examples that witness drift)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.BaselineBindingEdit}`
* **Notes (wiring‑only):** CHR does not define decay semantics; it only pins the owner-defined window/policy and ensures refresh can be triggered on decay events.

**GPatternExtension: QD_OEE_Wiring**

* **PatternScopeId:** `G.3:Ext.QD_OEE_Wiring`
* **GPatternExtensionId:** `QD_OEE_Wiring`
* **GPatternExtensionKind:** `MethodSpecific`
* **SemanticOwnerPatternId:** `C.18`
* **Uses:** `{C.18, C.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `DescriptorMapRef.edition` *(if any Characteristic declares descriptor roles)*
  * `DistanceDefRef.edition` *(if any Characteristic declares distance roles)*
  * `DHCMethodRef.edition` *(if any Characteristic is used as Q / QD-score)*
  * `InsertionPolicyRef?` *(when archive insertion semantics are declared for reproducibility)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring‑only):** QD/OEE semantics are owned by `C.18/C.19`. CHR only surfaces method‑role declarations
  (via `RoleDecls` or the interop alias `QD.Role`) and the edition/policy pins required for reproducible archive/front interpretation.

### G.3:5 - Archetypal Grounding

**AG‑1 — ML fairness auditing (post‑2015 selective and set‑valued practice).**
*System:* a CG‑Frame for evaluating deployed classifiers across cohorts with explicit abstention/defer behavior.
*CHR authoring:* publish `DemographicParityGap` and `EqualizedOddsGap` as Characteristics with:

* explicit ReferencePlane (deployment population + sampling regime),
* `ObservableOf` (audit protocol + uncertainty model + window),
* interval scale (bounded; zero semantics explicit),
* missingness semantics (cohort sparsity and label noise are typed),
* legality/guard surfaces that forbid illicit cohort mixing and require explicit proof hooks for aggregation across cohorts.

*Downstream:* CAL acceptance binds thresholds and failure behavior; selector remains set‑returning under partial orders and may treat “defer/abstain” as a first‑class outcome (tri‑state semantics routed via `G.Core`).

**AG‑2 — Clinical diagnostics (post‑2015 evidence‑aware evaluation).**
*System:* a CG‑Frame for comparing diagnostic pipelines under evolving datasets and protocols.
*CHR authoring:* publish `Sensitivity` and `Specificity` as ratio‑scale, dimensionless Characteristics on `[0,1]`, with:

* explicit `ObservableOf` (trial protocol, inclusion criteria, uncertainty model),
* freshness/decay expectations (protocol drift is modelled as decay),
* legality surfaces that forbid averaging incompatible ordinal labels (e.g., severity grades) and require explicit unit/exposure constraints for any derived rate.

*Downstream:* CAL acceptance owns thresholds and guard‑bands; evidence wiring is cited via Path/PathSlice to make refresh triggers actionable.

**AG‑3 — Quality‑Diversity / Illumination (post‑2015 MAP‑Elites/CMA‑ME lineage).**
*System:* a CG‑Frame where selection returns archives/fronts rather than a single winner.
*CHR authoring:* declare which Characteristics play Q/D/QD‑score roles and pin the metric definitions (descriptor map, distance definition, method editions) so archives are reproducible across runs and refresh can be triggered on edition changes. CHR does not scalarize partial orders; set‑return semantics are routed via `G.Core`.

### G.3:6 - Bias‑Annotation

CHR authoring is where many biases become “baked in” as measurement choices. Typical risks:

* **Proxy bias:** a convenient observable substitutes for the intended construct. Mitigation: require `ObservableOf` + ReferencePlane + micro‑examples; force explicit “what is being measured” rather than relying on labels.
* **Population and protocol shift:** a characteristic’s meaning changes when the sampling regime or protocol changes. Mitigation: explicit validity windows and freshness/decay expectations; edition pins for protocol definitions; RSCR triggers on freshness/decay events and evidence surface edits.
* **Ordinal misuse bias:** ordinal ratings treated as interval/ratio by convenience. Mitigation: publish scale type + admissible transforms; legality matrix + guard macros; reject coordinate upgrades without proof hooks.
* **Cross‑tradition/cross‑context bias:** imported terms erase local meaning. Mitigation: require explicit imports and loss notes; downstream penalties route to `R_eff` only (routed via `G.Core`), making loss visible rather than silently altering F/G semantics.
* **Metric gaming bias (QD and evaluation):** changing descriptors/distances changes what “diverse” means. Mitigation: edition‑pin metric definitions and make role declarations explicit (wiring via `C.18/C.19`).

### G.3:7 - Conformance Checklist (normative)

| ConformanceId     | Statement                                                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G3‑CoreRef** | `G.3` is conformant only if the applicable `G.Core` obligations declared in `G.3:4.1` are satisfied (effective expansion of profiles/sets + deltas; explicit pins; typed RSCR triggers; single‑owner defaults).                       |
| CC‑G3‑01          | `CHR Pack@CG‑Frame` is published as a notation‑independent kit payload with the minimum exported objects listed in `G.3:4.2`.                                                                                                         |
| CC‑G3‑02          | Every `CHR.Characteristic` has an explicit home `Context`, an explicit `ReferencePlane`, and a filled `ObservableOf` field (instrument/protocol + uncertainty model + validity window).                                               |
| CC‑G3‑03          | Every `CHR.Characteristic` declares its `ScaleRef`, `Polarity`, and `UnitSet` (or an explicit “unitless” declaration), plus bounds/zero semantics where applicable.                                                                   |
| CC‑G3‑04          | Missingness is typed in the CHR artefacts such that downstream tri‑state handling is possible without silent coercion. *(Tri‑state semantics are owned by `G.Core`; the typing obligation is CHR‑local.)*                              |
| CC‑G3‑05          | `CHR.Scale` / `CHR.Level` artefacts encode the scale type and admissible transforms, and make illicit arithmetic checkable by downstream consumers.                                                                                   |
| CC‑G3‑06          | Any published `CHR.Coordinate` includes a `CoordinatePolicy` that states preserved invariants and explicit non‑entitlements; coordinates do not silently upgrade measurement structure.                                               |
| CC‑G3‑07          | `CHR.LegalityMatrix` and `CHR.Guards` exist and are referenced by downstream operator authoring; semantics are routed to owners (MM‑CHR and `G.Core`), not duplicated locally.                                                        |
| CC‑G3‑08          | `CHR.AggregationSpecs` are typed and legality‑constrained; where Γ‑fold is required and no explicit override is pinned, it is referenced via `DefaultId.GammaFoldForR_eff` (single‑owner routing via `G.Core.DefaultOwnershipIndex`). |
| CC‑G3‑09          | If any characteristic is intended for promotion into `CG‑Spec`, the linkage is explicit and edition‑pinned (no shadow ids). *(Owner: `G.0`; wiring via `G.3:Ext.CGSpecPromotionWiring`.)*                                             |
| CC‑G3‑10          | UTS Name Cards exist for public ids minted/evolved by the CHR pack (twin labels + lifecycle notes). *(Delegation target: `CC‑GCORE‑UTS‑1` via `CC‑G3‑CoreRef`.)*                                                                      |
| CC‑G3‑11          | Worked examples and RSCR tests exist and cite `PathId/PathSliceId`; they cover illegal‑op refusal, unit/scale constraints, polarity invariants, and coordinate non‑entitlements.                                                      |
| CC‑G3‑12          | Thresholds/guard‑bands are not embedded in CHR artefacts; they remain owned by CAL acceptance clauses (`G.4`).                                                                                                                        |
| CC‑G3‑13          | When method‑role declarations are present (via `RoleDecls` and/or `QD.Role` alias), each declaration is **docked** to its semantic owner via a corresponding `G.3:Ext.*` module, and the owner-required edition/policy pins are surfaced to make downstream interpretation reproducible. *(QD/OEE owner: `C.18/C.19`; wiring via `G.3:Ext.QD_OEE_Wiring`.)* |
| CC‑G3‑14          | **Evidence wired.** Each `CHR.Characteristic` links to R‑anchors via `PathId/PathSliceId` (and, where applicable, `A.10` anchor/carrier refs), so downstream evidence discipline (`G.6`) can audit legality/guard claims.            |
| CC‑G3‑15          | An `Archetypal Grounding` section exists with at least two domain‑distinct examples that demonstrate lawful CHR typing/legality and the CHR↔CAL separation (notably: no thresholds in CHR).                                          |
| CC‑G3‑16          | If `EvidenceLanes` are used, lane tags are declared with a citation to their semantic owner taxonomy (`B.3`), and any lane‑dependent tolerances/proof requirements are explicitly pinned (policy‑id / edition refs). Cross‑lane comparison/aggregation is **illegal by default** unless an explicit owner policy makes it lawful (typically `G.4`), and it must be auditable via evidence paths (`G.6`). |
| CC‑G3‑17          | If the CHR outputs are bound into the planned baseline / suite seam, the binding uses `CHRMechanismSuiteSlotFillingsPlanItem` as defined in `A.19.CHR` + `A.15.3` (no local baseline variants; wiring via `G.3:Ext.SuiteBoundaryLinkage`). |
| CC‑G3‑18          | **Freshness is explicit.** Each `CHR.Characteristic` declares a validity window and either (i) an explicit `NonDecayingDecl` or (ii) a freshness/half‑life statement that is pinned/routed to the semantic owner (`B.3.4`) when policy‑bound (`G.3:Ext.DecayWiring`). Changes in decay windows/policies participate in RSCR via canonical trigger kinds declared in `G.3:4.1`. |


### G.3:8 - Common Anti‑Patterns and How to Avoid Them

* **Hidden cardinalization.** Don’t treat ordinal encodings as interval/ratio; do publish coordinate policies that explicitly preserve order‑only invariants and forbid arithmetic upgrades.
* **Unit laundering.** Don’t add or average quantities with incompatible units; do force explicit unit discipline and legality checks via MM‑CHR owners.
* **Polarity drift.** Don’t rely on “higher is better” implicitly; do publish polarity explicitly and make downstream use auditable.
* **Threshold leakage into CHR.** Don’t embed policy cut‑offs in CHR; do keep thresholds in CAL acceptance artefacts.
* **Unpinned semantics.** Don’t cite “the metric” or “the distance” without edition pins; do require edition‑pinned references when semantics affect interpretation.
* **Unscoped reuse.** Don’t reuse CHR terms across contexts without explicit import and loss notes; do keep crossings explicit and auditable (routed via `G.Core`).

### G.3:9 - Consequences

* **Legality becomes checkable.** Downstream patterns can reject illegal operations and rely on explicit legality surfaces rather than implicit conventions.
* **Comparability without semantic flattening.** Plural traditions remain representable because CHR preserves local meaning while making lawful relations explicit.
* **Reproducible downstream behavior.** Edition/policy pins make “why did this change?” answerable and RSCR actionable.
* **Authoring overhead.** The pattern shifts effort to up‑front authoring: explicit cards, pins, and tests are non‑optional when CHR becomes a public kit surface.

### G.3:10 - Rationale

CHR is the point where “numbers start moving” *only if* measurement semantics are stable enough to support lawful downstream reasoning. By making scale/unit/polarity explicit, publishing legality and guard surfaces, and requiring provenance pins, CHR authoring prevents downstream mechanisms from silently inventing their own legality assumptions.

Separating core invariants into `G.Core` prevents drift and ensures Part‑G‑wide properties (tri‑state, penalty routing, set‑return semantics, RSCR typing, default ownership) are single‑owner, while CHR remains responsible for CHR‑specific kit surfaces.

### G.3:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice by:

* treating abstention/defer and set‑valued outcomes as first‑class design objects (consistent with modern selective prediction and set‑valued reporting practice),
* keeping multiobjective and archive‑based reasoning set‑returning rather than silently scalarizing (consistent with QD/illumination and open‑ended evaluation practice after 2015),
* making evaluation semantics reproducible through explicit edition/policy pinning (aligned with the modern emphasis on reproducibility and “specifying the evaluation surface” rather than only reporting metrics),
* modularizing method‑family specifics (QD/OEE, explore‑exploit) via explicit wiring and ownership rather than embedding method semantics into universal measurement legality.

### G.3:12 - Relations

**Builds on:** `G.Core`, `G.1`, `G.2`, `G.6` (EvidenceGraph / Path citation), `A.19.CHR`, `A.15.3`, `A.17–A.18/C.16` (MM‑CHR), `F.1–F.9` (Contexts/UTS/Bridges), `B.3` / `B.3.4`, `A.10`, `E.10`, `E.5.1–E.5.3`.
**Uses (via Extensions):** `G.0` (promotion/linkage to `CG‑Spec`), optional `C.18/C.19` (QD/OEE wiring).
**Publishes to:** `G.4` (admissible operators + legality/guard macros + freshness routing), `G.5` (role declarations + pins for reproducibility), `UTS` (Name Cards + lifecycle), RSCR tests/hooks.
**Constrains:** any CAL/LOG/selector usage that consumes CHR (must treat CHR artefacts as typed/legal surfaces, not as prose hints).

### G.3:End

## G.4 - CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring

**Tag.** Architectural pattern (publishes `CAL Pack@CG-Frame`; consumes `CHR Pack@CG-Frame`; constrains selector/dispatcher usage; binds GateCrossing discipline; exposes `ReferencePlane` and penalty/guard policy pins to `SCR`)

**Stage.** design‑time (authoring & publication; enables lawful run‑time evaluation)

**Primary output.** A notation‑independent `CAL Pack@CG-Frame` containing:
`CAL.Charter@Context`, `CAL.Operator[]`, `CAL.Acceptance[]`, `CAL.Flow[]`,
`CAL.EvidenceProfiles`, `CAL.ProofLedger`, **optional** `CAL.NQD[]` (when declared),
UTS entries (Name Cards + twin labels + lifecycle notes incl. deprecations and lexical‑continuity notes),
RSCR tests, Worked‑Examples, and a `TaskMap@Context` (`TaskMap`; handoff surface consumed by `G.5`).

**Primary hooks.** `G.Core` (Part‑G invariants + RSCR trigger catalogue + default ownership index), `G.1` (CG‑FrameContext), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.0` (CG‑Spec legality gate), `A.19` (CN‑Spec), `A.18` (CSLC), `A.10` (provenance anchors), `B.3` (trust / freshness / decay), `E.18` + `A.21` + `A.27` (GateCrossing / CrossingSurface harnesses), `F.9` (BridgeCard / CL), `G.6` (EvidenceGraph / PathId / PathSliceId; wired via Extensions), `G.5` (Selector & Dispatch), `G.10` (shipping), `G.11` (refresh orchestration), plus Contexts/UTS/LEX disciplines already fixed elsewhere in the spec.

**Non‑duplication note.** Universal Part‑G invariants (no shadow specs, crossing visibility, tri‑state guard, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR causes, default ownership discipline, shipping boundary) are single‑owned by `G.Core` and are pulled into `G.4` only through the `G.Core linkage` manifest in **G.4:4.1** (and via explicit delegations in CC).

### G.4:1 - Problem frame

A CG‑Frame has:

* a declared `CG-FrameContext` (scope, described entity, plane),
* a plurality of method traditions and claims (SoTA inputs), and
* CHR‑typed measurement surfaces (`Characteristic/Scale/Coordinate` + legality guard macros).

Before any run‑time selection, comparison, aggregation, or portfolio formation is executed downstream, the CG‑Frame needs an explicit, auditable **calculus layer (CAL)** that:

1. defines *what operators exist* and what they are allowed to do over CHR types,
2. externalizes *fit‑for‑purpose acceptance* as typed predicates (with Context‑local thresholds), and
3. binds these choices to an evidence wiring surface (lanes, provenance anchors, policy pins, and refresh triggers) so that downstream selection, logging, parity, and shipping can cite *stable ids* rather than re‑inventing semantics.

This pattern provides the design‑time authoring kit and the publication surface for CAL artifacts, while delegating Part‑G‑wide invariants to `G.Core` and contract legality to `CG‑Spec`/`CN‑Spec`.

### G.4:2 - Problem

Teams repeatedly face drift and ambiguity in the calculus layer that sits between “typed measurements exist” and “a selector/dispatcher runs”:

* **Illicit operations** slip in (implicit cardinalization, unit laundering, ordinal arithmetic).
* **Acceptance is scattered** (thresholds embedded in code or in CHR prose; predicates not typed; unknown handling inconsistent).
* **Evidence wiring is underspecified** (which provenance anchors matter, what policy ids are in force, what is plane‑scoped, what changes must trigger refresh).
* **Cross‑context imports are silent** (hidden reuse of constructs across contexts/planes/editions without published GateCrossings and loss accounting).
* **Tooling artifacts become semantics** (vendor flags or implementation details substitute for a conceptual contract).

### G.4:3 - Forces

* **Expressiveness vs legality.** CAL must allow useful comparisons/aggregations while staying lawful under CHR typing and legality gates.
* **Pluralism vs comparability.** Multiple method traditions must coexist without forcing premature unification, yet remain cross‑citable and auditable.
* **Decision support vs auditability.** CAL must support selection and portfolio formation while preserving explicit, reviewable assumptions and proofs.
* **Exploration vs assurance.** CAL must support exploratory regimes (probing, novelty, open‑ended search) without letting un‑assured outputs silently become dominance claims.
* **Locality vs portability.** CAL must be Context‑local by default but prepared for explicit reuse via Bridges and published crossing surfaces.

### G.4:4 - Solution — CAL authoring kit and publication surface

#### G.4:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; routing/delegation hub)

**GCoreLinkageManifest (normative).** Canonical shape, Nil‑elision, and the Expansion rule are defined in `G.Core`.

`GCoreLinkageManifest := ⟨
CoreConformanceProfileIds := {
GCoreConformanceProfileId.PartG.AuthoringBase,
GCoreConformanceProfileId.PartG.TriStateGuard,
GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
GCoreConformanceProfileId.PartG.ShippingBoundary
},

CorePinSetIds := {
GCorePinSetId.PartG.AuthoringMinimal,
GCorePinSetId.PartG.CrossingVisibilityPins
},

CorePinsRequired := {
UTSRowId[],                 // CAL artefacts are public ids (Name Cards + lifecycle notes)
ΓFoldRef.edition?            // only when an explicit Γ‑fold override is pinned (otherwise use DefaultId)
},

// consumed iff no explicit `ΓFoldRef.edition` override is pinned
DefaultsConsumed := { DefaultId.GammaFoldForR_eff },

RSCRTriggerSetIds := { GCoreTriggerSetId.SoTAHarvestSynthesis },
RSCRTriggerKindIds := {      // deltas (Expansion rule applies)
  RSCRTriggerKindId.PenaltyPolicyEdit,
  RSCRTriggerKindId.DefaultOwnerChange,
  RSCRTriggerKindId.BaselineBindingEdit
}
⟩`

By the `G.Core` Expansion rule, the effective conformance ids / trigger kinds / pin obligations for `G.4` are the expansions of the referenced profiles/sets/pin‑sets plus the explicit deltas above.

Notes (normative intent, routed semantics):

* The semantics of tri‑state outcomes, penalty routing, set‑return discipline, crossing visibility, P2W split, typed RSCR causes, and default ownership are single‑owned by `G.Core` and are not redefined here.
* EvidenceGraph/Path pins (when used) are declared only via **`G.4:Ext.EvidenceGraphWiring`** in **G.4:4.5** (so `G.Core linkage` stays minimal and does not “pull in” `G.6` by default).
* Method‑specific pins (e.g., QD descriptor/distance/insert policy pins; open‑ended transfer rules pins) MUST appear only in **Extensions** blocks (see **G.4:4.5**) and MUST NOT introduce competing defaults.

#### G.4:4.2 - `CAL Pack@CG-Frame` surface (pattern‑owned kit)

`CAL Pack@CG-Frame` is the CG‑Frame’s published calculus layer. Minimally, it provides:

* `CAL.Charter@Context` — scope anchor for this CAL pack:

  * cites `CG-FrameContext`, `describedEntity`, `ReferencePlane`,
  * cites contract surfaces (`CNSpecRef`, `CGSpecRef`) by edition pins,
  * records the “assumption envelope” that acceptance predicates rely on (without minting a new contract surface).
  * emits `TaskMap@Context` (`TaskMap`) as the canonical handoff surface to `G.5` (task→gates/flows/evidence pins).
* `CAL.Operator[]` — typed operator cards (UTS‑published):

  * explicit signature over CHR types,
  * explicit preconditions/postconditions (incl. legality guard macros references),
  * explicit provenance/evidence hooks (by ids/pins, not by tool behavior).
* `CAL.Acceptance[]` — typed predicates with Context‑local thresholds:

  * binds to CHR characteristic ids (and, when inducing numeric comparison/aggregation, to `CG‑Spec.characteristic` ids),
  * exposes unknown handling and failure behavior via policy pins.
* `CAL.Flow[]` — legality‑checked compositions of operator cards:

  * declares result kind (scalar only when lawful; set/portfolio when partial orders remain partial orders),
  * records which acceptance clauses gate which flows.
* `CAL.EvidenceProfiles` — evidence wiring surface:

  * lane tags (`F/G/R`) / provenance anchors / policy pins needed for `SCR` and audit surfaces,
  * explicit freshness/decay hooks (freshness window + decay/Γ_time selectors) as pinned policies/refs (not prose).
  * explicit `ReferencePlane` + penalty routing policy ids (`Φ(CL)`, `Ψ(CL^k)`, `Φ_plane`) as citable pins; any such policy family is justified in `CAL.ProofLedger` (monotone + bounded).
* **Optional** `CAL.NQD[]` — QD/OEE‑related calculus surfaces when declared:

  * descriptor/distance/insertion artifacts are pinned by ids/editions,
  * semantics are owned by method‑specific owners (e.g., `C.18`, `C.19`) and not redefined by CAL.
* `CAL.ProofLedger` — a proof/justification ledger:

  * links legality, monotonicity, boundedness, and other soundness obligations to operator/flow/clause ids.
* Publication layer:

  * UTS Name Cards (twin labels) for all public ids,
  * RSCR tests ids and Worked‑Examples ids,
  * deprecation notices and edition bump notes as lifecycle artifacts.

Boundary discipline (normative):

* **No shadow specs**: CAL artefacts cite `CN‑Spec`/`CG‑Spec` and do not introduce competing “local specs” (delegated; see `CC‑GCORE‑CN‑CG‑1` via **CC‑G4‑CoreRef**).
* **No shipping ownership**: CAL does not own shipping (delegated; see `CC‑GCORE‑SKP‑1` via **CC‑G4‑CoreRef**).
* **No refresh ownership**: CAL does not own refresh orchestration; it only publishes pins/payload for refresh (owner: `G.11`).

**Minimal schema fragments (notation‑independent; fields for citation, not an implementation schema):**

```
CAL.Pack@CG-Frame :=
 ⟨ calPackId, charterId, taskMapId, operatorIds[], acceptanceClauseIds[], flowIds[],
 evidenceProfileIds[], proofLedgerId, nqdIds[]?,
    utsRowIds[], workedExampleIds[], rscrTestIds[], lifecycleNoteIds[] ⟩

CAL.Operator :=
  ⟨ operatorId(UTS), signature(CHR-typed), preconditions[], postconditions[],
  evidenceProfileRefs[]?, failureBehaviorRef?, crossingRefs[]? ⟩

CAL.Acceptance :=
  ⟨ clauseId(UTS), characteristicRefs[], cgSpecCharacteristicRefs[]?,
    predicateRef, unknownHandlingRef, failureBehaviorRef,
    evidenceProfileRefs[]?, crossingRefs[]? ⟩

CAL.Flow :=
  ⟨ flowId(UTS), dag(operatorIds, edges), gateClauses(acceptanceClauseIds),
    resultKind, decisionAidPolicyRef? ⟩

CAL.EvidenceProfile :=
  ⟨ evidenceProfileId(UTS), lanes(F/G/R), anchors(A.10)[],
    freshnessPolicyPins[]?, penaltyPolicyPins[]?, ΓFoldRef.edition? ⟩
```

#### G.4:4.3 - CAL authoring chassis C1–C9 (pattern‑owned kit)

**C1 — CAL Charter (scope anchor).**
Authors declare a `CAL.Charter@Context` that:

* anchors CAL to the CG‑Frame scope (`CG-FrameContext`, `describedEntity`, `ReferencePlane`),
* pins the relevant contract surfaces (`CNSpecRef.edition`, `CGSpecRef.edition`),
* records the local assumption envelope used by acceptance predicates (as explicit statements to be audited, not as hidden algorithmic assumptions),
* declares which CAL artifacts are intended to be cited downstream (UTS ids).
* emits a `TaskMap@Context` (`TaskMap`) that binds each declared `TaskSignature` (or task family) to:
  * eligible `CAL.FlowId[]` / `CAL.OperatorId[]`,
  * gating `AcceptanceClauseId[]` (ids of `CAL.Acceptance` clauses),
  * required `CAL.EvidenceProfileId[]`,
  * and any required policy pins/edition pins for reproducibility.
  This is the canonical “handoff manifest” consumed by `G.5` (thresholds remain only inside `CAL.Acceptance`).

**C2 — Operator Cards (typed & lawful).**
Each `CAL.Operator` is a UTS‑published, typed unit with:

* `OperatorId (UTS)`,
* `Signature` over CHR types,
* `Preconditions` (including references to CHR guard macros where applicable),
* `Postconditions / invariants`,
* `EvidenceProfileRef[]` (or an explicit “none”),
* `FailureBehaviorRef` (policy‑bound) for safe degradations and non‑catastrophic fallbacks.

**C3 — Acceptance Clauses (typed predicates; thresholds live here).**
Each `CAL.Acceptance` is a UTS‑published predicate with:

* stable `ClauseId (UTS)` for citation,
* explicit `CharacteristicRefs` (CHR ids) used by the predicate,
* `CGSpecRefs?` required iff the clause induces numeric comparison/aggregation,
* `EvidenceProfileRefs?` identifying evidence consulted (so `SCR` can surface the relevant pins),
* explicit **freshness envelope** (freshness window + decay/Γ_time selector refs/pins) when evidence recency is part of admissibility,
* `UnknownHandling` as a tri‑state choice (via `G.Core` semantics),
* `FailureBehaviorRef` (policy‑bound) for degrade/abstain behavior.
* `GateCrossingId[]` / `CrossingSurfaceId[]` **iff** the clause relies on cross‑context/plane/edition imports (no “silent reuse”).
  Missing required crossing artefacts is a conformance failure and blocks publication of the affected clause/flow (GateCrossing harness: `E.18`/`A.21`/`A.27`; crossing invariants: `G.Core`).

**C4 — Aggregation & comparison flows (safe by construction).**
`CAL.Flow` composes operators into legality‑checked DAGs and declares:

* which acceptance clauses gate the flow,
* which operator outputs are decision‑relevant vs report‑only,
* what the **result kind** is (scalar only where lawful; otherwise set/portfolio).
* any thinning/decision‑aid policy (e.g., ε‑front selection) as an explicit policy pin that **does not** silently replace the declared result kind.

**C5 — Evidence wiring surface.**
`CAL.EvidenceProfile` makes evidence hooks explicit:

* provenance anchor references (A.10‑style carriers/anchors, cited by id),
* lane tags (`F/G/R`) for each evidence contribution (no implicit lane mixing; penalties route only to `R_eff` as routed by `G.Core`),
* pinned policy ids for penalty routing and freshness/decay handling (incl. freshness window + decay/Γ_time selector pins; and `Φ(CL)`/`Ψ(CL^k)`/`Φ_plane` policy ids when used),
* declared inputs needed for `SCR` fields at run‑time (without embedding run‑time “gate decisions” into design‑time artifacts).

**C6 — NQD/OEE surface (optional; method‑specific semantics routed).**
If the CG‑Frame declares QD/OEE‑style regimes, CAL may publish `CAL.NQD[]` as a **surface** that:

* declares descriptor space and distance/insertion artifacts by ids and edition pins,
* records archive/illumination intent and “report‑only vs dominance” gating as explicit policy pins,
* **does not** redefine QD/OEE semantics (those remain owned by method‑specific patterns such as `C.18` / `C.19` and are wired via `Extensions`).

**C7 — ProofLedger (soundness & legality obligations).**
`CAL.ProofLedger` links each operator/flow/clause to:

* legality proof refs (incl. CSLC refs when numeric comparison/aggregation is induced),
* monotonicity/boundedness/stability proof refs for penalty/aggregation policies where relevant,
  * in particular: if an explicit `ΓFoldRef` is pinned (override), ProofLedger includes monotonicity + boundedness/boundary behavior proof refs for that fold.
* explicit statements of degradation conditions (what must happen when assumptions fail).

**C8 — Publication + RSCR + Bridges.**
CAL publication emits:

* UTS entries (Name Cards + twin labels) for all CAL ids,
* Worked‑Examples that exercise legality and acceptance claims,
* RSCR tests ensuring:

  * illegality is detected (e.g., forbidden ordinal arithmetic),
  * guard macro use is coherent,
  * flow legality checks are exercised,
  * acceptance clauses behave as authored on examples.

Any cross‑context/plane/edition import required by CAL publication is handled through GateCrossing/CrossingSurface discipline (as routed by `G.Core`), and CAL publication is blocked if required crossing artifacts are missing.

**C9 — Packaging & refresh readiness (without owning orchestration).**
CAL pack versions:

* record changes as edition‑pinned updates,
* publish deprecations/lifecycle notes for public ids,
* emit RSCR‑relevant trigger payload pins (editions/policies/UTS ids/paths) for refresh orchestration (owner: `G.11`).

#### G.4:4.4 - Interfaces (minimal I/O surface)

| Interface                 | Consumes                                            | Produces                                                                                  |
| ------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `G.4-1 Charter`           | `CG-FrameContext`, SoTA inputs, `CHR Pack@CG-Frame` | `CAL.Charter@Context` + `TaskMap@Context` (`TaskMap`)  |
| `G.4-2 Operators`         | CHR typing + SoTA operator inventory                | `CAL.Operator[]` (UTS ids; typed signatures; refs to evidence profiles & guards)  |
| `G.4-3 Acceptance`        | Task intent + policy pins + CHR characteristics     | `CAL.Acceptance[]` (typed; thresholds; freshness envelope pins; failure behavior refs)    |
| `G.4-4 Flows`             | Operator cards + admissible aggregators             | `CAL.Flow[]` (legality‑checked compositions; declared result kind)                        |
| `G.4-5 NQD Surface`       | Task intent + policy pins + (optional) QD/OEE inputs | `CAL.NQD[]` (descriptor/distance/insertion refs + edition pins; optional)  |
| `G.4-6 Publish`           | All above + proofs + examples  | Versioned `CAL Pack@CG-Frame`, UTS entries, RSCR tests, Worked‑Examples, lifecycle notes |

#### G.4:4.5 - Extensions (pattern‑scoped; non‑core)

`G.4` supports method‑family and discipline‑specific calculus variations exclusively via pattern‑scoped extensions.

**GPatternExtension block: `G.4:Ext.EvidenceGraphWiring`**
- **PatternScopeId:** `G.4:Ext.EvidenceGraphWiring`
- **GPatternExtensionId:** `EvidenceGraphWiring`
- **GPatternExtensionKind:** `InteropSpecific`
- **SemanticOwnerPatternId:** `G.6`
- **Uses:** `{G.6}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `EvidenceGraphId?`
  - `PathId[]/PathSliceId[]`
  - `UTSRowId[]` (for cited artifacts)
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
- **Notes (wiring‑only):** This block does not define EvidenceGraph semantics; it only fixes that CAL proofs/examples may cite evidence by Path ids.

**GPatternExtension block: `G.4:Ext.NQD`**
- **PatternScopeId:** `G.4:Ext.NQD`
- **GPatternExtensionId:** `NQD`
- **GPatternExtensionKind:** `MethodSpecific`
- **SemanticOwnerPatternId:** `C.18`
- **Uses:** `{C.18}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `DescriptorMapRef.edition`
  - `DistanceDefRef.edition`
  - `InsertionPolicyRef`
  - `ArchiveRef?`
  - `TaskSignatureRef?` (if activation is TaskSignature‑bound)
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
- **Notes (wiring‑only):** CAL does not redefine QD semantics; it only pins the artifacts needed for reproducible archive/descriptor behavior. Any archive/illumination summaries (e.g., coverage / QD‑score / occupancyEntropy / filledCells) are published as report‑only outputs unless an explicit CAL acceptance clause/policy authorizes promotion.

**GPatternExtension block: `G.4:Ext.EELog`**
- **PatternScopeId:** `G.4:Ext.EELog`
- **GPatternExtensionId:** `EELog`
- **GPatternExtensionKind:** `MethodSpecific`
- **SemanticOwnerPatternId:** `C.19`
- **Uses:** `{C.19}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `ExploreExploitBudgetPolicyRef`
  - `ProbeAccountingRef?`
  - `FailureBehaviorRef?` (if probe/sandbox is policy‑bound)
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**GPatternExtension block: `G.4:Ext.SoSLogBranches`**
- **PatternScopeId:** `G.4:Ext.SoSLogBranches`
- **GPatternExtensionId:** `SoSLogBranches`
- **GPatternExtensionKind:** `MethodSpecific`
- **SemanticOwnerPatternId:** `C.23`
- **Uses:** `{C.23}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `SoSLogRuleId[]`
  - `SoSLogBranchId[]`
  - `FailureBehaviorPolicyId`
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta}`
- **Notes (wiring‑only):** This block only pins branch/rule ids for degrade/abstain explanation; it does not redefine rule semantics.

**GPatternExtension block: `G.4:Ext.AcceptanceRiskControl`** *(Phase‑3 seed)*
- **PatternScopeId:** `G.4:Ext.AcceptanceRiskControl`
- **GPatternExtensionId:** `AcceptanceRiskControl`
- **GPatternExtensionKind:** `Phase3Seed`
- **SemanticOwnerPatternId:** `owner TBD`
- **Uses:** `∅`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `RiskControlPolicyRef`
  - `CalibrationWindowRef?`
  - `CoverageTargetRef?`
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
- **Notes (non‑normative seed):** Intended for post‑2015 acceptance families such as conformal risk control / set‑valued selective prediction, distributionally‑robust acceptance envelopes, and calibrated abstention policies; semantics must be owned elsewhere before becoming normative.

### G.4:5 - Archetypal Grounding

**Tell.** A CG‑Frame must choose and justify a set of candidate methods (possibly a portfolio) under explicit legality, evidence, and scope constraints. CHR provides the typed measurement surface; CAL turns it into executable, auditable predicates and flows.

**Show 1 (in‑context CAL pack skeleton).**
Context: R&D portfolio choice. CHR defines `SafetyClass(ord↑)`, `CostUSD_2026(ratio↓)`, `Readiness(nominal)`.

* `CAL.Operator: DominatesPareto`
  Signature over CHR types, precondition references CHR guard macros.
* `CAL.AcceptanceClause: AC_SafetyGate`
  Typed predicate binding `SafetyClass` (and its levels) with Context‑local thresholds; unknown handling uses tri‑state pins.
* `CAL.Flow: Flow_ParetoPortfolio`
  Produces a set/portfolio result kind; gates by `AC_SafetyGate` and `AC_Budget`.
* `CAL.EvidenceProfile: EP_SafetyEvidence`
  Declares anchor ids and freshness policy pins required for `SCR`.

Downstream, `G.5` consumes only the handoff manifest: clause ids, operator ids, and evidence profile ids (no embedded thresholds).

**Show 2 (explicit cross‑context import).**
A `SafetyClass` value is imported from a different Context/plane. CAL may still author an acceptance clause using that value, but only after the reuse is made explicit as a published crossing surface and the CAL artifacts cite the relevant ids/pins. The CAL pack remains Context‑local; portability is achieved through explicit crossings and citations, not by silently widening scope.

### G.4:6 - Bias-Annotation

CAL is where “what counts as acceptable” is encoded. Typical bias vectors include:

* threshold‑selection bias (arbitrary floors masquerading as natural laws),
* measurement bias amplified by illegitimate arithmetic or hidden scalarization,
* survivorship bias in Worked‑Examples and probe telemetry,
* Goodhart pressures when report‑only telemetry is accidentally treated as dominance.

The pattern mitigates these by requiring typed acceptance clauses, explicit policy pins, and an auditable proof/justification ledger, while keeping cross‑context reuse explicit and penalized only through the routed assurance lane.

### G.4:7 - Conformance Checklist (normative)

| ConformanceId     | Statement                                                                                                                                                                                                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G4‑CoreRef** | Conformance with `G.4` requires satisfying the effective `G.Core` obligations referenced by the `GCoreLinkageManifest` in **G.4:4.1** (profiles, pin sets, consumed defaults, and trigger kinds).                                                                                                              |
| **CC‑G4‑01**      | `CAL Pack@CG-Frame` is published as a notation‑independent object with stable UTS ids (Name Cards + twin labels) for `CAL.Charter`, `TaskMap`, all operator/acceptance/flow/evidence artifacts, Worked‑Examples, and lifecycle notes (incl. deprecations and lexical‑continuity notes). Tooling/vendor details remain non‑normative. |
| **CC‑G4‑02**      | `CAL.Charter@Context` pins `CG-FrameContext`, `describedEntity` (incl. `ReferencePlane`), and the relevant contract references by edition pins (`CNSpecRef.edition`, `CGSpecRef.edition`).                                                                                                                     |
| **CC‑G4‑03**      | Every `CAL.Operator` has an explicit CHR‑typed signature and explicit preconditions; any legality guard macros referenced are cited by id (no “implicit legality”).                                                                                                                                             |
| **CC‑G4‑04**      | Every `CAL.Acceptance` binds to CHR ids (`CharacteristicRefs`) and declares unknown handling and failure behavior via pins/refs; thresholds and cutoffs appear only here (not inside CHR artifacts and not inside operator prose). If the clause depends on cross‑context/plane/edition imports, it cites `GateCrossingId[]/CrossingSurfaceId[]`. |
| **CC‑G4‑05**      | If an acceptance clause, operator, or flow induces numeric comparison/aggregation, it cites the relevant `CG‑Spec.characteristic` ids and links to legality proof refs (CSLC) in the ProofLedger; otherwise it must be authored so that downstream can degrade/abstain rather than perform illegal operations. |
| **CC‑G4‑06**      | Every `CAL.Flow` declares its result kind and the set of gating acceptance clauses; any thinning/selection‑aid policies (e.g., ε‑front selection) are explicitly policy‑bound and do not silently replace the underlying result kind.                                                                      |
| **CC‑G4‑07**      | Every `CAL.EvidenceProfile` declares: provenance anchors (A.10), evidence lanes (`F/G/R`), freshness/decay pins (incl. freshness window + decay/Γ_time selector refs), and any penalty routing policy pins (`Φ(CL)`, `Ψ(CL^k)`, `Φ_plane`) needed for run‑time `SCR` surfacing. It either pins an explicit `ΓFoldRef.edition` override or (if absent) cites `DefaultId.GammaFoldForR_eff` (via `G.Core.DefaultOwnership`). Penalty policies affect `R_eff` only and do not define dominance. Any referenced penalty policy family is justified in the ProofLedger (monotone + bounded).  |
| **CC‑G4‑08**      | `CAL.ProofLedger` exists and is UTS‑citable; it links each operator/flow/clause to required proof/justification refs and records explicit degradation conditions when assumptions fail. If an explicit `ΓFoldRef` is pinned, it includes monotonicity + boundedness/boundary behavior proof refs for that fold. |
| **CC‑G4‑09**      | CAL publication includes RSCR tests and Worked‑Examples sufficient to detect illegality (incl. unit laundering / ordinal arithmetic), to exercise authored acceptance/flow behavior, and to validate the authored freshness envelope when it is part of admissibility; missing tests/examples are treated as an auditable gap, not as “assumed OK”. |
| **CC‑G4‑10**      | `TaskMap@Context` (`TaskMap`) is present and provides `G.5` with acceptance clause ids (`AcceptanceClauseId[]`; selector gates), operator/flow ids, and evidence profile ids required for explainability and audit; selector implementations must not embed thresholds or duplicate acceptance semantics.    |
| **CC‑G4‑11**      | Any method/discipline specifics are placed under `G.4:4.5 Extensions` as `GPatternExtension` blocks (stable `PatternScopeId`, explicit owner, pins, and RSCR triggers); no extension introduces competing defaults or replaces `G.Core` invariants. |
| **CC‑G4‑12**      | `CAL Pack@CG-Frame` includes lifecycle artifacts for public ids (deprecations / edition bumps / lexical‑continuity notes) and exposes refresh payload pins (editions/policies/UTS ids and, when present, PathId/PathSliceId) sufficient for `G.11` to plan RSCR without inferring semantics from prose. |
| **CC‑G4‑13**      | When `G.4:Ext.NQD` is present, `CAL.NQD[]` is present and is wired only via the declared semantic owner (`C.18`): at minimum it pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `InsertionPolicyRef`, and it treats archive/illumination summaries as report‑only unless explicitly promoted by a CAL acceptance clause/policy. |
| **CC‑G4‑14** | CAL does not mint new universal types to encode “strategy/policy”. Strategy is expressed as authored flows + acceptance clauses + policy/task pins (and downstream registry/composition in `G.5`); any specialization is introduced only via `GPatternExtension` wiring blocks or cited semantic owners.  |

### G.4:8 - Common Anti-Patterns and How to Avoid Them

* **Hidden thresholds.**
  Avoid: embedding cutoffs in CHR prose or in operator descriptions.
  Prefer: `CAL.AcceptanceClause` with explicit ids and pins.

* **Untyped “score(x)”.**
  Avoid: operators with implicit units and untracked legality assumptions.
  Prefer: explicit CHR‑typed operator signatures + cited legality checks.

* **Silent cross‑context reuse.**
  Avoid: importing constructs across Contexts/planes/editions without published crossings.
  Prefer: explicit crossing artifacts and citations; keep CAL pack Context‑local.

* **Acceptance as implementation detail.**
  Avoid: acceptance embedded in tool logic.
  Prefer: publish acceptance as citable CAL artifacts; downstream consumes ids.

* **Exploratory telemetry treated as dominance.**
  Avoid: letting probe/illumination telemetry quietly become a dispatch criterion.
  Prefer: keep it report‑only unless an explicit policy‑bound acceptance clause authorizes promotion.

### G.4:9 - Consequences

* CAL becomes a stable, citable calculus layer: operator/acceptance semantics are explicit artifacts, not tacit code behavior.
* Legality failures are surfaced as authoring defects (RSCR‑testable) rather than run‑time surprises.
* Downstream patterns (`G.5`, `G.8`, `G.9`, `G.10`, `G.11`) can reference stable ids/pins without redefining acceptance or operator semantics.
* Method pluralism is supported: multiple calculi can coexist as separate operator/flow/acceptance families, wired via Extensions rather than mixed into the core kit.

### G.4:10 - Rationale

CAL sits at the boundary where typed measurement becomes actionable choice. Making CAL a published, typed, and testable artifact reduces semantic drift and prevents “shadow legality gates” from emerging in tools or in downstream prose.

The design separates concerns:

* CHR owns measurement typing and legality guard macros,
* CG‑Spec/CN‑Spec own contract surfaces,
* `G.Core` owns Part‑G invariants and trigger/default discipline,
* `G.4` owns the CAL kit: authoring objects, publication surface, and handoff manifest.

This yields modularity (single owner per invariant/default), auditability (pins/ids and proof refs), and extensibility (method families attach through explicit extension modules).

### G.4:11 - SoTA-Echoing

CAL authoring is compatible with post‑2015 best practice families without confusing “popular” with “best‑available”:

* **Risk‑controlled acceptance**: modern conformal / selective / set‑valued prediction families where “abstain” is a first‑class, audited outcome (fits tri‑state gating + explicit calibration pins).
* **Robust acceptance envelopes**: distribution‑shift‑aware and distributionally‑robust acceptance styles, expressed as policy‑pinned predicates rather than hidden heuristics.
* **Modern multi‑objective practice**: preference‑aware, interactive, and set‑returning multi‑objective decision families that preserve partial orders and portfolios.
* **Quality‑Diversity after 2015**: archive‑based search families (e.g., CMA‑ME‑class) attach as wiring via edition‑pinned descriptor/distance/insertion artifacts.
* **Open‑ended exploration after 2015**: environment‑method co‑evolution families (e.g., POET‑class) attach through explicit generator family wiring and policy‑bound acceptance branches.

All of these remain method‑specific semantics and therefore belong in `Extensions` blocks (or their semantic owners), while `G.4` keeps the calculus kit stable and auditable.

### G.4:12 - Relations

**Builds on:** `G.Core` (and the pattern template discipline in `E.8`).

**Uses:** `G.1` (CG‑FrameContext), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.0` (CG‑Spec legality gate), `A.19` (CN‑Spec), `A.18` (CSLC), `A.10` (provenance anchors), `B.3` (trust/freshness/decay), `E.18` + `A.21` + `A.27` (GateCrossing harness), `F.9` (BridgeCard/CL).

**Uses (via Extensions):** `G.6` (EvidenceGraph/Path citation; when `G.4:Ext.EvidenceGraphWiring` is present), `C.18` (NQD), `C.19` (E/E‑LOG), `C.23` (SoS‑LOG).

**Used by:** `G.5` (selector/dispatcher), `G.8` (SoS‑LOG bundles), `G.9` (parity), `G.10` (shipping), `G.11` (refresh orchestration).
**Publishes to:** UTS (public ids + lifecycle), RSCR (tests + trigger emissions), `G.5` (handoff manifest), and (as cited payload) shipped packs owned by `G.10`.

**Constrains:** any run‑time LOG implementation that executes CAL operators/flows must treat CAL artifacts as citable contracts and must not re‑invent acceptance semantics.

### G.4:End

## G.5 - Multi‑Method Dispatcher & MethodFamily Registry

**Tag.** Architectural pattern (dispatcher/registry kit; selector façade)
**Stage.** *design‑time* authoring & registration with a *run‑time* selector façade (policy‑governed; edition‑aware)
**Primary output.** `MethodFamily Registry@CG‑Frame` + `GeneratorFamily Registry@CG‑Frame` + `Selector façade` surfaces (candidate sets, portfolio artefacts, DRR/SCR‑addressable audit pins)
**Primary hooks.** `G.Core`, `G.0 (CG‑Spec)`, `A.19 (CN‑Spec)`, `G.1–G.4`, `G.6–G.7`, `G.9–G.11`, `UTS (F.17–F.18)`, `GateCrossing/CrossingSurface (E.18; A.21)`, `CSLC (A.18)`, optional method/generator owners via Extensions (`C.18`, `C.19`, `C.23`, …).

**Non‑duplication note (Phase‑2, normative intent).** Universal Part‑G invariants (no shadow specs, crossing visibility, tri‑state, penalties→`R_eff` only, set‑return semantics, P2W split, typed RSCR causes, default ownership, shipping boundary) are **single‑owner in `G.Core`** and are **not re‑specified** here. This pattern cites them through the linkage manifest in **`G.5:4.1`** and (where needed for ID‑continuity) via **delegation statements** in `CC‑G5.*`.

### G.5:1 - Problem frame

A `CG‑FrameContext` (from **G.1**) and a `SoTA Synthesis Pack@CG‑Frame` (from **G.2**) expose multiple rival, internally coherent **method families** (and sometimes **generator families**) that can plausibly act on the same *describedEntity / ReferencePlane*.

At the same time, CHR/CAL authoring (from **G.3/G.4**) yields typed slots/scales/coordinates and admissible calculi/acceptance clauses—enough to formulate *eligibility*, *assurance*, and *legality* constraints, but not enough to pick “the method” without collapsing plurality.

You need a **notation‑independent** way to:

1. register method/generator families as *auditable, versioned* entries,
2. select/compose/fallback among them at run time for a concrete task instance,
3. publish stable identities to UTS, and
4. emit RSCR‑relevant triggers and pins without inventing new “shadow specs”.

### G.5:2 - Problem

How to design a **general, auditable dispatcher** that:

* supports **pluralism** (families from competing Traditions stay disjoint) while remaining **dispatchable** (selection is possible and explainable);
* does **not embed algorithmic dogma** in the core selector kernel;
* respects Context boundaries and crossing discipline (Bridge‑only; explicit pins);
* produces **set‑valued outcomes** when only partial orders are lawful;
* cleanly separates:

  * **pattern‑owned kit/surfaces** (registry + selector façade + publication surfaces),
  * **universal Part‑G invariants** (owned by `G.Core`),
  * **method/generator specifics** (wired only via `Extensions` blocks).

### G.5:3 - Forces

* **Pluralism vs. forced totalisation.** Many selection regimes are inherently partial‑order; forcing a scalar winner often creates illegal semantics.
* **Evidence realism vs. hard gates.** Eligibility/acceptance frequently depends on incomplete evidence; selection must remain auditable under tri‑state unknowns.
* **Reuse vs. leakage.** Cross‑Context reuse is valuable but must be explicit (Bridge + loss notes) and must not silently re‑ground semantics.
* **Exploration vs. exploitation.** Dispatch sometimes must probe alternatives under explicit policy/risk envelopes, but probing must not become an implicit fourth status.
* **Evolvability vs. churn.** Registries evolve (new families, deprecations, edition bumps); continuity must not be broken by “rename by meaning”.

### G.5:4 - Solution

#### G.5:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; single‑owner routing)

**GCoreLinkageManifest (normative; size‑controlled via profiles/sets).**
Effective obligations/pins/triggers are computed by union expansion of the referenced ids (per `G.Core:4.2.1`). Profiles/sets + explicit deltas; `Nil‑elision` applies.

* `CoreConformanceProfileIds :=`

  * `GCoreConformanceProfileId.PartG.AuthoringBase`
  * `GCoreConformanceProfileId.PartG.TriStateGuard`
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
  * `GCoreConformanceProfileId.PartG.ShippingBoundary`
* `CorePinSetIds :=`

  * `GCorePinSetId.PartG.AuthoringMinimal`
  * `GCorePinSetId.PartG.CrossingVisibilityPins` *(crossing‑aware use; pins from this set may be intentionally strengthened (optional→required) via `CorePinsRequired`)*
* `CorePinsRequired :=` *(delta over PinSets; pins/refs are id‑only; prefer strengthening optional→required over restating pins already covered by PinSets)*

  * `TaskSignatureRef` *(see `G.5:4.2` / S2)*
  * `MethodFamilyId[]` *(registry keys in scope)*
  * `GeneratorFamilyId[]?` *(when generator families are in scope)*
  * `PathId[]` *(audit citations for “why” and for evidence)*
  * `PathSliceId[]` *(audit citations for “why” and for evidence)*
  * `UTSRowId[]` *(published identities for selected/registered families and selector policy surfaces)*
  * `FailureBehaviorPolicyId?` *(only when degrade/abstain behavior is explicitly policy‑bound)*
  * `SoSLogBranchId?` *(only when degrade/abstain behavior is explicitly policy‑bound)*
* `DefaultsConsumed :=`

  * `DefaultId.GammaFoldForR_eff`
  * `DefaultId.PortfolioMode`
  * `DefaultId.DominanceRegime`
* `RSCRTriggerSetIds :=`

  * `GCoreTriggerSetId.RefreshOrchestration`
    *(payload pins: `TaskSignatureRef`, `CGSpecRef.edition`, `CNSpecRef.edition`, `MethodFamilyId[]`, `GeneratorFamilyId[]?`, `AcceptanceClauseId[]?`, `SoSLogBranchId?`, `FailureBehaviorPolicyId?`, `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `TransferRulesRef.edition?`, `InsertionPolicyRef?`, `PathId`, `PathSliceId`, `SCRId`, `DRRId`, `RSCRTestId[]`)*

#### G.5:4.2 - Dispatcher & Registry kit (pattern‑owned; notation‑independent)

G.5 owns the **kit surfaces** below. Their purpose is to make dispatch **possible and auditable** without embedding any method‑family semantics in the selector kernel.

**S1 — `MethodFamily Registry` (design‑time; per CG‑Frame).**
A registry row represents *a family*, not a single implementation. Minimal fields (conceptual, notationally independent):

* `Identity`: `MethodFamilyId`, `ContextId`, lineage/Tradition notes, `UTSRowId` (twin labels where applicable).
* `EligibilityStandardRef`: a typed predicate surface (tri‑state per `G.Core`), expressed in CHR/CAL terms and pinned to the relevant editions.
* `AssuranceProfileRef`: evidence‑lane expectations and assurance surface pins (SCR‑addressable).
* `LegalityBindings`: explicit references to the **single** contract surfaces (`CNSpecRef`, `CGSpecRef`) and to any required legality constraints (e.g., scale/unit legality via CSLC).
* `EvidencePins`: citations to `G.6` (`PathId/PathSliceId`) for claims/guarantees where such claims are asserted.
* `CrossingAllowance`: explicit Bridge/CL allowance pins **only** if cross‑Context operation is claimed.
* `PolicyHooksRef?`: optional pointers to policy owners (not defined here; wired via Extensions).

**S1′ — `GeneratorFamily Registry` (design‑time; optional; per CG‑Frame).**
A registry row for families that generate tasks/environments and/or co‑evolve solver families. G.5 owns the *surface*, not the generator semantics:

* `Identity`: `GeneratorFamilyId`, `ContextId`, `UTSRowId`.
* `GeneratorSignatureRef`: conceptual I/O and budget semantics.
* `EnvironmentValidityRegionRef?`: pinned constraints for generated environments/tasks.
* `TransferRulesRef.edition?`: required when the Open‑Ended mode is enabled (semantics owned elsewhere; see Extensions).
* `CouplerRefs?`: which `MethodFamilyId[]` can be coupled with this generator family.

**S2 — `TaskSignature` façade (design‑time + run‑time).**
A minimal typed record the dispatcher consumes. Its role is **pinning and auditability**, not over‑specification. It must be CHR/CAL‑typed and provenance‑aware.
G.5 treats `TaskSignatureRef` as an input surface; it does not define CHR/CAL semantics.

**S3 — `Selection kernel façade` (run‑time; policy‑governed).**
A notation‑independent selector that:

* consumes `TaskSignatureRef` + registry entries + pinned contract surfaces,
* applies eligibility/assurance gating (tri‑state),
* computes a lawful (possibly partial) order,
* returns a **set/portfolio** result (per `DefaultId.PortfolioMode` and explicit overrides),
* emits audit artefacts (DRR/SCR‑addressable pins).

**S4 — `Composition & fallbacks` templates (design‑time).**
A library of composition shapes (preconditioner → solver → verifier; cascades; meta‑selectors) **as templates**, legality‑checked and pinned. Concrete semantics of a particular strategy live in upstream method owners; G.5 only owns the composition surface.

**S5 — `Publication & telemetry` surface (run‑time).**
A standard surface to publish:

* `DRR` (decision rationale) + `SCR` (support/confidence routing) with explicit pins,
* portfolio/return‑set artefacts,
* telemetry pins to refresh orchestration (`G.11`), without owning orchestration.

**S6 — `Governance & evolution` surface (design‑time).**
Versioning, deprecation, and registry evolution discipline (UTS publication; continuity), without minting new Part‑G‑wide types.

#### G.5:4.3 - Selector specialization ladder (Phase‑2 alignment; head vs refinements)

Selection/dispatch is treated as a **mechanism family** whose specialization ladder must obey the **A.6.1:4.2.1** discipline (SlotKind invariance; specialization only via `⊑/⊑⁺`; no new mandatory inputs introduced by inherited ops).

**Normative alignment (cite, don’t duplicate):**

* `SelectorMechanism` is the *head* intension (generic selector façade).
* `SelectorMethodMechanism` and other method‑bound selectors are refinements (`⊑/⊑⁺`) that:

  * do not redefine universal invariants (those are routed via `G.Core`),
  * do not introduce new mandatory inputs to the selector façade beyond pinned policy/edition refs,
  * keep SlotKinds stable (refinements may narrow by specialization, not mutate kinds).

**Phase‑2 placement rule.** Method/generator specifics (QD archives, open‑ended portfolios, explore/exploit lenses, preference‑learning comparators, etc.) are **not** part of the selector head; they are connected via **`Extensions`** (`G.5:4.5`) through `Uses` and explicit pins.

#### G.5:4.4 - Interfaces (minimal I/O surface)

| Interface                         | Consumes                                                                                                                                                     | Produces                                                                                                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **G.5‑1 RegisterFamily**          | `SoTA` family cards (from `G.2`), CHR/CAL pins (from `G.3/G.4`), `CNSpecRef.edition`, `CGSpecRef.edition`, `ContextId`                                       | A `MethodFamily` registry row (`MethodFamilyId`, `EligibilityStandardRef`, `AssuranceProfileRef`, `UTSRowId`, pinned refs)                                                                                                                                 |
| **G.5‑2 RegisterGeneratorFamily** | `SoTA` generator family cards (from `G.2`), `ContextId`, pinned refs (including `TransferRulesRef.edition` when applicable)                                  | A `GeneratorFamily` registry row (`GeneratorFamilyId`, `GeneratorSignatureRef`, `UTSRowId`, pinned refs)                                                                                                                                                   |
| **G.5‑3 Select**                  | `TaskSignatureRef`, `MethodFamilyId[]` (in scope), pinned `CNSpecRef/CGSpecRef` (editions), policy refs (if any), audit citation pins (`PathId/PathSliceId`) | `CandidateSet` (set‑returning), portfolio artefact (per `PortfolioMode`), `DRR + SCR` pins; if no admissible candidate exists: return `CandidateSet=∅` plus an escalation hint (`ActionHint`) and the pins required to plan next steps (P2W split applies) |
| **G.5‑4 Compose**                 | `CandidateSet`, composition template refs, pinned legality constraints                                                                                       | Composite strategy surface (template‑level; legality‑checked; pinned)                                                                                                                                                                                      |
| **G.5‑5 Telemetry**               | run outcomes + citations + policy/edition pins                                                                                                               | refresh cues (typed RSCR causes + payload pins), parity deltas (if parity harness is in use), telemetry pins (selector‑side; orchestration owner is `G.11`)                                                                                                |

#### G.5:4.5 - Extensions (pattern‑scoped; non‑core)

All blocks below are **wiring‑only**: they declare `Uses` and required pins, but do not redefine semantics owned by the referenced patterns.

**GPatternExtension block: `G.5:Ext.EELog`**

* `PatternScopeId`: `G.5:Ext.EELog`
* `GPatternExtensionId`: `EELog`
* `GPatternExtensionKind`: `MethodSpecific`
* `SemanticOwnerPatternId`: `C.19`
* `Uses`: `{C.19}`
* `⊑/⊑⁺`: `∅`
* `RequiredPins/EditionPins/PolicyPins (minimum):`

  * `EELensPolicyRef` *(or equivalent lens/policy id owned by `C.19`)*
  * `RiskBudgetRef?`
  * `ProbeAccountingRef?`
  * `FailureBehaviorPolicyId?` *(if degrade behavior is routed through policy)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (wiring‑only; semantics routed):`

  * This block activates exploration/exploitation‑governed dispatch.
  * Post‑2015 examples that typically land here (as *wiring targets*, not core rules): modern bandit‑style or Bayesian selection under explicit risk budgets; adaptive evaluation/probing regimes; safe‑exploration variants where “abstain/degrade” is policy‑bound.

**GPatternExtension block: `G.5:Ext.SoSLOG`**

* `PatternScopeId`: `G.5:Ext.SoSLOG`
* `GPatternExtensionId`: `SoSLOG`
* `GPatternExtensionKind`: `MethodSpecific`
* `SemanticOwnerPatternId`: `C.23`
* `Uses`: `{C.23}`
* `⊑/⊑⁺`: `∅`
* `RequiredPins/EditionPins/PolicyPins (minimum):`

  * `SoSLogRuleId[]`
  * `SoSLogBranchId[]` *(including escalation branches, if used)*
  * `FailureBehaviorPolicyId` *(if degrade behavior is made explicit)*
  * `MaturityRungId[]?` *(when maturity ladders are used as gates; semantics owned by `C.23`)*
  * `AdmissibilityLedgerRef?` *(when selector consumes admissibility rows rather than recomputing thresholds)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
* `Notes (wiring‑only; semantics routed):`

  * This block pins dispatch decisions to explicit rule/branch ids, enabling auditable “why” without inventing a fourth acceptance status.

**GPatternExtension block: `G.5:Ext.NQD`**

* `PatternScopeId`: `G.5:Ext.NQD`
* `GPatternExtensionId`: `NQD`
* `GPatternExtensionKind`: `MethodSpecific`
* `SemanticOwnerPatternId`: `C.18`
* `Uses`: `{C.18, C.19}`
* `⊑/⊑⁺`: `∅`
* `RequiredPins/EditionPins/PolicyPins (minimum):`

  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `InsertionPolicyRef`
  * `TaskSignatureRef` *(when QD is enabled via TaskSignature flags/traits)*
  * `DHCMethodRef.edition?` *(when diversity/coverage telemetry is pinned to a DHC method)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (wiring‑only; semantics routed):`

  * G.5 core remains QD‑agnostic; QD semantics are routed to `C.18`.
  * Post‑2015 families that typically dock here: MAP‑Elites‑class QD (incl. later archive‑centric refinements), CMA‑ME‑class hybrids, modern illumination/coverage telemetry regimes where legality and edition pinning matter.

**GPatternExtension block: `G.5:Ext.OpenEndedFamilyWiring`**

* `PatternScopeId`: `G.5:Ext.OpenEndedFamilyWiring`
* `GPatternExtensionId`: `OpenEndedFamilyWiring`
* `GPatternExtensionKind`: `GeneratorSpecific`
* `SemanticOwnerPatternId`: `G.2` *(family semantics live in SoTA cards; G.5 only wires pins)*
* `Uses`: `{G.2, C.19, C.23}`
* `⊑/⊑⁺`: `∅`
* `RequiredPins/EditionPins/PolicyPins (minimum):`

  * `GeneratorFamilyId[]`
  * `TransferRulesRef.edition` *(mandatory when Open‑Ended is enabled)*
  * `EnvironmentValidityRegionRef?`
  * `CoEvoCouplerRef[]?`
  * `SoSLogBranchId[]?` *(when validity of generated tasks is gated by explicit branches)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (wiring‑only; semantics routed):`

  * This block enables portfolios of `{Environment, MethodFamily}` pairs without redefining generator semantics in G.5.
  * Post‑2015 examples typically referenced via `G.2` family cards: POET‑class and later open‑ended/co‑evolutionary regimes, including enhanced variants where transfer policies and validity gates must be edition‑pinned.

**GPatternExtension block: `G.5:Ext.PreferenceComparators`** *(Phase‑3 seed; owner TBD)*

* `PatternScopeId`: `G.5:Ext.PreferenceComparators`
* `GPatternExtensionId`: `PreferenceComparators`
* `GPatternExtensionKind`: `Phase3Seed`
* `SemanticOwnerPatternId`: `owner TBD`
* `Uses`: `∅`
* `⊑/⊑⁺`: `∅`
* `RequiredPins/EditionPins/PolicyPins (minimum):`

  * `PreferenceModelRef.edition?`
  * `ComparatorSpecRef.edition?`
  * `QueryPolicyRef?` *(e.g., when preference elicitation is interactive)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
* `Notes (seed only; no Phase‑2 norming):`

  * Reserved for preference‑learning and human‑in‑the‑loop comparator families (post‑2015), where “legality of comparison” and audit pins must be explicit. Formal owner pattern to be introduced in Phase‑3 if needed.

### G.5:5 - Archetypal Grounding

**Tell (archetype).**
**System** must choose among rival families without lying about measurement legality, crossings, or evidence. **Episteme** insists that what is chosen must remain comparable, auditable, and stable under refresh.

**Show 1 (multi‑Tradition dispatch; partial‑order outcome).**
A CG‑Frame includes multiple decision‑theoretic families with different admissibility assumptions. Evidence for some CHR traits is incomplete.
System registers families (S1), then runs `Select` (S3) on a pinned `TaskSignatureRef`. Eligibility is tri‑state; some families **abstain** due to missing minimal evidence pins. Among remaining candidates, only a partial order is lawful, so the selector returns a **set** (portfolio) and emits DRR/SCR pins that cite `PathSliceId` evidence. No shadow acceptance logic appears in the selector; it consumes pinned acceptance/legality surfaces.

**Show 2 (QD and Open‑Ended modes as Extensions).**
A frame enables illumination (archive semantics) and an optional generator family that proposes task variations.
System keeps the selector head unchanged, but activates `G.5:Ext.NQD` (pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion policy) and `G.5:Ext.OpenEndedFamilyWiring` (pins `TransferRulesRef.edition`). Portfolio results become `{Environment, MethodFamily}` sets under explicit pins and telemetry. Refresh triggers are emitted as canonical `RSCRTriggerKindId.*` with payload pins, without redefining trigger meaning locally.

### G.5:6 - Bias-Annotation

Potential biases and failure modes this pattern explicitly guards against:

* **Monoculture bias (single Tradition dominance by default).** Mitigation: registry requires explicit eligibility/assurance surfaces; selection is set‑returning under partial orders; method‑specific policies are explicit pins, not hard‑coded defaults.
* **Hidden scalarisation bias.** Mitigation: set‑return semantics is core‑routed; dominance regimes are explicit and default ownership is single‑owner.
* **“Tool equals method” bias.** Mitigation: notation independence + prohibition of tool keywords in core registry/eligibility fields; tool choices are outside the core.
* **Cross‑Context leakage bias.** Mitigation: explicit crossing pins only; Bridges + CL are required when crossings occur; no implicit crossings.
* **Survivorship bias in refresh.** Mitigation: RSCR triggers are typed/id‑based; freshness/decay and telemetry deltas are first‑class causes with canonical ids.

### G.5:7 - Conformance Checklist (normative)

| ConformanceId   | Statement |
| --------------- | ----------| 
| `CC‑G5‑CoreRef` | **Core conformance bridge.** `G.5` is conformant only if the **effective** `G.Core` obligations referenced by `G.5:4.1 (GCoreLinkageManifest)` are satisfied (after profile/set expansion and explicit deltas). |
| `CC‑G5.0`       | Core standards **SHALL** remain notation‑independent; vendor/tool keywords are forbidden in registry, eligibility, assurance, or selector‑kernel obligations (E.5.*). |
| `CC‑G5.1`       | Every `MethodFamily` **SHALL** declare an `EligibilityStandardRef` using CHR/CAL terms (typed; edition‑pinned where applicable). Standards **SHALL NOT** rely on tool‑specific keywords.  |
| `CC‑G5.2`       | Selection **SHALL** be a pure function of `TaskSignatureRef` + pinned policy/edition refs; side effects are limited to emitting DRR/SCR pins and telemetry/RSCR triggers (no hidden mutation of contract surfaces). |
| `CC‑G5.3`       | **Delegated (ID‑continuity).** Cross‑Context use **MUST** follow `G.Core` crossing visibility and penalty routing. **Delegation targets:** `CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑PEN‑1`.  |
| `CC‑G5.4`       | **Default owner for** `DefaultId.GammaFoldForR_eff`. The selector **MUST** default to the weakest‑link rule for `R_eff` and record contributors in SCR; it **MAY** use an alternative Γ‑fold only when provided by an explicitly pinned policy/profile with proof obligations satisfied (monotonicity; boundary behavior). |
| `CC‑G5.5`       | Ordinal scales **MUST NOT** be averaged/subtracted; any aggregation/comparison must respect CHR scale typing and legality constraints (incl. CSLC where applicable). |
| `CC‑G5.6`       | Method and generator family identities **SHALL** be published to UTS with the required naming discipline (twin labels where applicable; deprecations follow lexical continuity rules). *(Core routing applies; G.5 adds the registry‑specific publication obligation.)* |
| `CC‑G5.7`       | **Conditional.** If `G.5:Ext.EELog` is present, exploration **MUST** be budgeted under the pinned E/E‑LOG policy; probe outcomes **MUST** feed refresh via canonical RSCR trigger kinds. |
| `CC‑G5.8`       | **CG‑Frame gate enforced.** Selection rejects or abstains from candidates that do not meet the pinned `CG‑Spec.MinimalEvidence` requirements for the characteristics they cite. |
| `CC‑G5.9`       | **Delegated (ID‑continuity).** Set‑return semantics are routed via `G.Core`. **Delegation target:** `CC‑GCORE‑SET‑1`. Candidate ordering **MUST** be lawful over typed traits and legality constraints. If only a partial order is available, selection **MUST** return a set/portfolio result (no forced totalisation via illegal scalarisation). |
| `CC‑G5.10`      | **SCR completeness.** SCR **MUST** enumerate Γ‑fold contributors (when used), referenced contract surface editions, the evidence citations (`PathId/PathSliceId`) used in gating/rationale, and `MinimalEvidence` gating verdicts *(by lane & carrier, when such gating is relied upon).* |                                                      
| `CC‑G5.11`      | **Delegated (ID‑continuity).** Tri‑state eligibility/acceptance semantics and unknown handling are routed via `G.Core`. **Delegation target:** `CC‑GCORE‑GUARD‑1`. *(Includes the rule that `degrade(...)` is expressed via a pinned FailureBehavior/SoS‑LOG branch id — not as a fourth status.)* |
| `CC‑G5.12`      | **No “universal” cross‑Tradition scoring.** Cross‑Tradition selection **MUST NOT** rely on a single numeric formula not justified by pinned CHR/CAL constraints and the contract surfaces. If a triad/portfolio **claims universality**, it **MUST** satisfy **explicit, pinned** heterogeneity gates (ids/pins), e.g., `FamilyCoverage ≥ k` and `MinInterFamilyDistance ≥ δ_family`, where `k` and `δ_family` are declared by the pinned policy/TaskSignature/SoTA pack, and cite the relevant **Context Card id (F.1)** in DRR/SCR; otherwise treat the outcome as Context‑local.  |
| `CC‑G5.13`      | **Conditional.** If the selector consumes admissibility/maturity artefacts (e.g., via `G.5:Ext.SoSLOG`), it **MUST NOT** recompute thresholds; it consumes pinned admissibility ledger rows and cites clause/rung ids in audit pins. |
| `CC‑G5.14`      | **Φ(CL) / Φ_plane discipline.** If crossing or plane penalties are applied, the active penalty policy ids (e.g., `Φ(CL)`, `Φ_plane`) **MUST** be explicit in audit pins, and the pinned policies **MUST** satisfy the monotone & bounded requirements asserted by their owners and be published via the owner surface (e.g., `CG‑Spec`). SCR **MUST** record the policy‑id in use; penalty routing semantics remain routed via `G.Core`. |
| `CC‑G5.15`      | Units/scale legality **MUST** be established via CSLC (A.18) before any aggregation or Γ‑fold; unit/scale mismatches are a fail‑fast defect. |
| `CC‑G5.16`      | Hidden thresholds are forbidden. Thresholds live in explicitly pinned acceptance/eligibility policy artefacts, not in selector prose, LOG shells, or code.  |
| `CC‑G5.17`      | ReferencePlane **MUST** be declared (pinned) for any claim that is used in dispatch, and the selector’s audit artefacts must cite it (including plane‑crossing pins when applicable). |
| `CC‑G5.18`      | Numeric comparisons/aggregations used by dispatch **MUST** cite a lawful, edition‑pinned comparator/spec surface (as provided by the contract surfaces); illegal mixes of scale types are forbidden. |
| `CC‑G5.19`      | **Conditional (QD).** If `G.5:Ext.NQD` is present, the required QD telemetry triple (quality/diversity/QD summary) **MUST** be computable and publishable under the pinned descriptor/distance definitions and archive policy, without redefining their semantics in G.5. |
| `CC‑G5.20`      | **Conditional (QD).** QD/illumination summaries are treated as telemetry unless explicitly promoted by a pinned acceptance/policy artefact; the selector must record the promoting policy id in audit pins. |
| `CC‑G5.21`      | **Conditional (Archive/QD).** Any use of archives **MUST** declare `InsertionPolicyRef` and pin the required editions for reproducibility (e.g., descriptor/distance definitions and any method editions they depend on).  |
| `CC‑G5.22`      | **Conditional (QD).** Twin‑naming discipline for descriptor vs plain space (if used) must be respected (distinct objects; no aliasing).  |
| `CC‑G5.23`      | **Default owner for** `DefaultId.PortfolioMode`. The selector **MUST** expose `PortfolioMode ∈ {Pareto, Archive}` with **default = `Archive`**, and echo it in DRR/SCR and portfolio artefacts when not explicitly overridden by pinned policy/TaskSignature. `ε`‑fronts are allowed as *local* decision aids under `CG‑Spec` when explicitly pinned.  |
| `CC‑G5.23a`     | **Parity‑run publication.** If parity harness is in use, a selector/generator **MUST** publish a parity run and `ParityCard` to **UTS** (see `G.9`). This obligation remains mandatory irrespective of dominance/portfolio policy. |
| `CC‑G5.24`      | **Conditional (Open‑Ended).** If `G.5:Ext.OpenEndedFamilyWiring` is present, the selector **MUST** support portfolios of `{Environment, MethodFamily}` pairs as set‑valued outcomes under explicit pins. |
| `CC‑G5.25`      | **Conditional (Open‑Ended).** In Open‑Ended mode, `TransferRulesRef.edition` is mandatory and **MUST** be visible to telemetry and RSCR triggers.  |
| `CC‑G5.26`      | **Conditional (Archive/QD).** Within any archive niche/cell, ordering and tie‑breaks **MUST** remain lawful over compatible scales; illegal mixed‑scale weighted sums are forbidden. |
| `CC‑G5.27`      | If the selector cites any `GateCrossing`, the corresponding `CrossingSurface` publication **MUST** be present and conformant; missing/non‑conformant `CrossingSurface` blocks downstream consumption. | 
| `CC‑G5.28`      | **Default owner for** `DefaultId.DominanceRegime`. `DominanceRegime` **SHALL** default to `ParetoOnly`. Any inclusion of additional telemetry dimensions into dominance (e.g., illumination) requires an explicitly pinned acceptance/policy artefact and must be recorded in audit pins. **Parity‑run publication (CC‑G5.23a) remains mandatory** irrespective of dominance policy. |
| `CC‑G5.29`      | **Conditional (QD/Open‑Ended).** Any telemetry event that materially changes an archive/portfolio state **MUST** log `PathSliceId`, the active policy id, and the active editions of the relevant definition pins (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `TransferRulesRef.edition` when applicable) and expose them to RSCR triggers. |
| `CC‑G5.30`      | **No Strategy minting.** Within `G.5`, “strategy” is a policy‑bound composition surface; the pattern **SHALL NOT** mint a new universal `U.Type` named `Strategy` (E.10 discipline). If a stable reference is needed, publish composition/policy ids (e.g., UTS entries) rather than minting a universal type. |
| `CC‑G5.31`      | **Strategy hint on non‑admissible sets.** If selection yields `CandidateSet = ∅`, the selector **SHALL** emit an explicit escalation hint (`ActionHint`) that is **DRR/SCR‑compatible** and auditable: include (at minimum) the top‑3 blocking constraints as cited ids/pins, and (where applicable) the relevant edition pins (e.g., `TransferRulesRef.edition` in Open‑Ended mode) to guide exploration under explicitly pinned lenses (e.g., E/E‑LOG). |
| `CC‑G5.32`      | **Parity‑run publication + lawful roll‑ups.** If parity harness is in use, parity publication is required per `CC‑G5.23a` (ID‑continuity). Any scalar roll‑up or summary view **MUST** be lawful under **CG‑Spec** (no mixed‑scale sums), and published views must preserve set‑return semantics (no single‑score leaderboards as authoritative outputs without an explicit, lawful comparator surface). |

### G.5:8 - Common Anti-Patterns and How to Avoid Them

* **Anti‑pattern: “Selector as a shadow spec.”**
  *Symptom:* local acceptance/legality rules appear in selector prose/code, diverging from CN/CG/CAL.
  *Avoid:* route all contract semantics via `CNSpecRef/CGSpecRef` and pinned CAL artefacts; keep G.5 core as a façade.

* **Anti‑pattern: “Implicit crossings.”**
  *Symptom:* cross‑Context reuse is claimed without Bridge/CL pins, or without cited `CrossingSurface`.
  *Avoid:* require explicit crossing pins; block consumption without publication.

* **Anti‑pattern: “Hidden scalarisation.”**
  *Symptom:* partial orders are flattened into single winners “for convenience”.
  *Avoid:* return sets/portfolios; make dominance regimes explicit; keep telemetry report‑only unless promoted by explicit policy.

* **Anti‑pattern: “Method specifics in the selector head.”**
  *Symptom:* QD/OEE/preference models become mandatory for basic dispatch.
  *Avoid:* keep them in `G.5:Ext.*` blocks with explicit pins and `Uses`.

* **Anti‑pattern: “Churn by meaning.”**
  *Symptom:* registry entries are “renamed” to reflect updated interpretation, breaking continuity.
  *Avoid:* version/deprecate; keep stable ids; use explicit edition pins and deprecation notices.

### G.5:9 - Consequences

* **Auditable plurality.** Multiple Traditions can co‑exist without forced semantic flattening; dispatch remains explainable and evidence‑pinned.
* **Core stability.** Universal invariants are routed via `G.Core`; method/generator innovation does not churn the selector head.
* **Evolvability.** Registries support growth, retirement, and refresh with typed RSCR causes and explicit payload pins.
* **Composability.** Strategy templates and fallbacks remain legality‑checked and portable across implementations.

### G.5:10 - Rationale

* **Why registries?** Dispatch requires stable, auditable “family objects” with explicit eligibility and assurance surfaces; otherwise selection collapses into ad‑hoc tooling.
* **Why separation via Extensions?** QD/OEE/preference‑learning and similar families are fast‑moving and method‑specific; making them part of the selector head would force a universal semantics and violate strict distinction.
* **Why set‑return?** Partial orders are common and often the only lawful representation under heterogeneous scales; set‑return preserves semantics and makes tie criteria explicit.
* **Why explicit defaults with single owners?** Defaults are unavoidable; single‑owner indexing prevents competing defaults from silently diverging across patterns.

### G.5:11 - SoTA-Echoing

This pattern is designed to **host** (not redefine) post‑2015 SoTA families via `Uses` + edition/policy pins:

* **Quality‑Diversity / illumination (post‑2015 refinements).** Archive‑centric QD families (e.g., MAP‑Elites‑line evolutions, CMA‑ME‑line hybrids) fit naturally as `G.5:Ext.NQD` wiring with explicit descriptor/distance/insertion pins.
* **Open‑Endedness (post‑2015 wave).** POET‑class and later open‑ended/co‑evolutionary families dock via generator registries + `TransferRulesRef.edition` pins (`G.5:Ext.OpenEndedFamilyWiring`).
* **Algorithm selection & meta‑selection.** Modern selection under uncertainty, robust evaluation, and policy‑driven probing regimes dock via explicit policy owners (`C.19`‑style lenses) and typed telemetry pins, rather than as hard‑coded scoring rules.
* **Preference‑learning comparators.** Interactive and learned‑preference regimes (post‑2015) are treated as comparator/policy artefacts with explicit editions (Phase‑3 seed stub provided).

SoTA here is treated as **best‑known practice for a declared goal and constraint regime**, not “what is currently popular”.

### G.5:12 - Relations

**Builds on (normative):** `G.Core` (core invariants + linkage discipline).

**Uses (conceptual dependencies; cited via pins/ids):**

* Contract surfaces: `A.19 (CN‑Spec)`, `G.0 (CG‑Spec)`.
* Upstream kits: `G.1 (CG‑Frame Card)`, `G.2 (SoTA Pack)`, `G.3 (CHR Pack)`, `G.4 (CAL Pack)`.
* Evidence & crossings: `G.6 (EvidenceGraph; PathId/PathSliceId)`, `G.7 (Bridge/CL calibration)`, `E.18/A.21 (CrossingSurface/GateChecks)`.
* Planning/enactment boundary: `A.15.3 (SlotFillingsPlanItem)` as the planned baseline anchor (cited, not redefined).
* Optional method/generator owners via `G.5:Ext.*`: `C.18`, `C.19`, `C.23`, plus any future owner patterns (Phase‑3).

**Publishes to:** `UTS` (family ids, selector policy surfaces), `G.6` (audit citations), RSCR emission surfaces (typed triggers + payload pins), and downstream packs via the canonical shipping owner (`G.10`).

### G.5:End


## G.6 - Evidence Graph & Provenance Ledger

**Tag.** Architectural pattern
**Stage.** design‑time (assembly) + run‑time (telemetry ingestion)
**Primary output.** A notation‑independent `EvidenceGraph` + a stable `PathId` / `PathSliceId` citation surface + an SCR projection (“Assurance SCR”) suitable for audit, selection explainability, and refresh/RSCR wiring.
**Primary hooks.** A.10 (evidence anchors/carriers; SCR/RSCR anchoring), B.3 (assurance lanes and `F/G/R` skeleton), F.9 (BridgeCard/CL), G.4 (CAL `EvidenceProfiles` + `ProofLedger` linkage), `G.Core` (Part‑G invariants, RSCR trigger catalogue, default‑ownership index), E.18/A.21 (GateCrossing + CrossingSurface checks), F.17 (UTS publication), F.15 (RSCR), E.10 (LEX), E.5.* (notation‑independence discipline).
**Non‑duplication note.** Universal Part‑G invariants (no shadow specs; Bridge‑only crossings; tri‑state discipline; penalties→`R_eff` only; P2W split; typed/id‑based RSCR causes; single‑owner defaults; Δ‑discipline) are owned by `G.Core` and are *cited* via `CC‑GCORE‑*`. This pattern defines only the *EvidenceGraph kit* and its path‑addressable provenance surfaces.

### G.6:1 - Problem frame

SoTA claims, operators, and method families are admitted (or gated) using assurance signals derived from diverse artefacts and anchors. FPF already mandates **Evidence Graph Referring** (A.10), lane discipline, and the assurance skeleton (B.3). What is often still missing in practice is a *first‑class, citable* object that makes the provenance of an admission/decision **addressable**:

* *exactly which* anchors and bindings were used,
* *under which* `ReferencePlane` and `BoundedContext`,
* *with which* explicit crossings and penalty policies,
* *for which* time window (freshness/decay),
* in a way that selectors, audits, and maturity transitions can cite without copying tables or re‑telling a story.

This pattern introduces the missing kit: a typed, lane‑aware `EvidenceGraph` plus stable `PathId` / `PathSliceId` addresses that downstream LOG, UTS, parity, and refresh can cite.

**Why here (not in G.4)?** G.4 owns CAL artefacts (EvidenceProfiles, ProofLedger, acceptance policies). G.6 packages *cross‑artefact provenance* as a graph and mints *path identities* that downstream surfaces can cite without duplicating CAL tables or re‑inventing legality rules.

### G.6:2 - Problem

1. Readers cannot reliably **audit crossing/penalty and decay impacts** on claims without chasing many tables and informal narratives.
2. Cross‑Context/plane reuse must remain **Bridge‑only and explicit**, but provenance often hides crossings (or treats them as “obvious”).
3. Selection and maturity decisions need a stable **path address** to re‑check later, including after edition/policy/freshness changes.

### G.6:3 - Forces

| Force                        | Tension                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| **Provenance vs agility**    | Fine‑grained audit trails ↔ friction for authors.                                   |
| **Lane purity vs synthesis** | Keep TA/VA/LA separable ↔ publish a unified justification surface.                  |
| **Notation independence**    | Semantics in prose/math ↔ teams want diagrams/tables (informative only).            |
| **Design vs run**            | Design‑time evidence assembly ↔ run‑time telemetry ingestion must not be conflated. |
| **Crossings and planes**     | Crossings must be explicit and penalised correctly ↔ authors want “just reuse it”.  |

### G.6:4 - Solution — EvidenceGraph (notation‑independent; lane‑aware; path‑addressable)

#### G.6:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; routing/delegation hub)

**GCoreLinkageManifest (normative; size‑controlled).**

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
  },
  RSCRTriggerSetIds := { GCoreTriggerSetId.EvidenceGraphKit },
  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },
  CorePinsRequired := {
    EvidenceGraphId,
    EvidenceGraphRef.edition?,   // iff editioned as a published artefact
    PathId[]/PathSliceId[],      // strengthened (unconditional for G.6)
    UTSRowId[],                  // strengthened (UTS Name Cards + PathCards are required outputs)
    Γ_timePolicy?,               // iff empirical legs exist (or equivalently: window id carried by PathSliceId)
    ΓFoldRef.edition?,           // iff an explicit Γ-fold artefact is pinned
    CAL.ProofLedgerId[]?         // iff Γ-fold is overridden (cite CAL ProofLedger ids; owner: G.4)
  },
  DefaultsConsumed := { DefaultId.GammaFoldForR_eff },
  TriggerAliasMapRef? := G.Core.TriggerAliasMap.G6
⟩`

**Conditional add‑on (tri‑state guard).** If `G.6` is used to publish or consume guard outcomes (e.g., via `G.6:Ext.SoSLOGPathCitationWiring`), additionally require:
`CoreConformanceProfileIds += { GCoreConformanceProfileId.PartG.TriStateGuard }`.

*(Nil‑elision + expansion rule are per `G.Core:4.2`.)*

#### G.6:4.2 - EvidenceGraph (object; kit‑owned surface)

**Definition (object).** An `EvidenceGraph` is a **typed DAG** whose nodes are resolvable to A.10 anchors/carriers and evidencing roles, and whose edges represent minimal, normative provenance relations suitable for audit and path citation.

* **Nodes.** Each node is an A.10‑anchored evidence carrier or evidence role (e.g., a proof carrier, a measurement record carrier, a tool‑qualification carrier). Nodes MUST remain grounded in A.10 anchors and MUST NOT introduce mereological structure (A.10 firewall).
  * **Node kinds (explicit; stable).** Nodes MUST have an explicit kind tag `nodeKind ∈ {U.EvidenceRole, SymbolCarrier, TransformerRole, MethodDescription, Observation}` (as used in the existing Part‑G vocabulary), so downstream projections can remain notation‑independent and audit‑checkable.
  * **Extension pins.** Method‑family‑specific pins (e.g., QD/OEE) MUST NOT be introduced as new “core node kinds”; they are carried as additional pins only when the relevant `GPatternExtension` is in use and are recorded on UTS PathCards / SCR projections as required by that extension.
* **Edges (minimal normative vocabulary).** The pattern admits a small set of provenance edges sufficient for audit:

  * `verifiedBy` (formal line),
  * `validatedBy` (empirical line),
  * `fromWorkSet` (run‑time trace provenance),
  * `happenedBefore` (temporal ordering),
  * `derivedFrom` (controlled derivation).
  * *(Informative only)* `usedCarrier`, `interpretedBy` MAY appear as authoring aids, but MUST NOT be relied on for conformance checks (their semantics remain non‑normative in G.6).
    Additional narrative edges MAY exist as informative annotations but MUST NOT be relied on for conformance checks.
* **Lane tags.** Every binding on a path is lane‑typed with `assuranceUse ∈ {TA, VA, LA}` (lane separation remains explicit through to SCR projections; no silent cross‑lane averaging).
* **Externality (no self‑evidence).** Any evidencing `TransformerRole` that would certify the evaluated holon MUST be modelled as external (or model a meta‑holon explicitly); G.6 does not permit reflexive “self‑evidence” shortcuts.
* **Context and plane attachment.** Nodes and claims carry `BoundedContext` and `ReferencePlane`. Any movement across context/kind/plane/design↔run/edition boundaries is represented via explicit GateCrossing/CrossingSurface artefacts (with crossing pins routed per `G.Core`).

#### G.6:4.3 - PathId and PathSliceId (citable justification addresses)

**PathId (address for justifications).** A `PathId` is a stable identifier minted for a **claim‑local, lane‑typed** path in an `EvidenceGraph` under a declared scope slice (including a time selector where applicable) and a declared `ReferencePlane`. A `PathId` is meant to be citable from downstream artefacts (LOG, UTS, parity, shipping) without duplicating evidence tables.

A `PathId` citation surface SHALL include, at minimum:

* the lane split (TA/VA/LA) for the path,
* the explicit crossing pins (when crossings are traversed),
* the freshness/time attachment status for empirical legs (when present), including any explicit `validUntil`/expiry marker when one is declared (or a decay/freshness policy pin that implies expiry),
* the pinned policy identifiers relevant to the path’s penalty/trust wiring (policy ids are cited; policies remain owned elsewhere),
* the effective crossing‑trust “bottleneck” information when crossings exist (e.g., lowest `CL`/`CL^k`/`CL^plane` encountered on the cited slice),
* the effective `Γ‑fold` in force for any published/relied‑upon `R_eff` projection (default or explicit override), and (when overridden) the cited CAL `ProofLedger` ids that justify the override,
* the `EvidenceGraphId` and enough addressability to resolve the path to SCR/RSCR anchors.

**PathSliceId (time‑ & plane‑lifted snapshot).** A `PathSliceId` denotes a **release‑quality snapshot key** for a path under explicit time/plane binding (e.g., window policy + `ReferencePlane`) and is intended as the address used when refresh/RSCR wants *path‑granular* recomputation.

*The universal definition of “what kinds of changes force refresh” is owned by `G.Core` (typed trigger kinds). G.6 only makes the slice addressable and pin‑complete.*

When downstream methods require additional edition/policy pins for reproducibility (e.g., archive/illumination/QD surfaces), such pins are specified by the relevant `GPatternExtension` module(s) and are treated as *required pins when that extension is used*.

#### G.6:4.4 - Assurance and legality binding (delegation‑first; no shadow specs)

G.6 does not redefine B.3 or legality rules; it binds evidence paths to existing owners:

* **Assurance skeleton.** Lane separation and the `F/G/R` skeleton are as per B.3. Any statement about penalty routing or default Γ‑fold is delegated to `G.Core` and the default‑ownership index (do not restate).
* **CAL linkage.** When a path claims a proof obligation or an override (e.g., an explicit Γ‑fold override), it MUST cite the relevant CAL `ProofLedger` / `EvidenceProfiles` artefacts (G.4) rather than inventing local semantics.
* **Legality binding.** If a path includes numeric comparisons/aggregations, the legality surface MUST be *cited* via `CG‑Spec` (G.0) rather than re‑implemented in G.6 prose.

#### G.6:4.5 - Conceptual interface (notation‑independent surface; informative shapes)

These are conceptual shapes, not tool APIs (E.5 discipline).

* `Explain(pathId | pathSliceId)` → returns a citation‑ready explanation bundle: lane split, relevant pins (crossings/policies/editions), freshness binding, and links to contributing anchors (A.10) and any CAL evidence/profile refs.
* `PathsFor(claim, scopeSlice, referencePlane)` → enumerates admissible paths, returning `PathId[]` with enough metadata to support selection/audit queries.
* `Snapshot(pathId | pathSliceId)` → emits a release‑grade snapshot record (SCR/RSCR‑grade) whose keys are citable and whose pins are explicit.

#### G.6:4.6 - Extensions (pattern‑scoped; non‑core)

All blocks below are `GPatternExtension` modules (PatternScopeId‑scoped, **not** new PatternIds). They store wiring only and cite semantic owners.

**GPatternExtension: LegacyTriggerAliases**

* **PatternScopeId:** `G.6:Ext.LegacyTriggerAliases`
* **GPatternExtensionId:** `LegacyTriggerAliases`
* **GPatternExtensionKind:** `InteropSpecific`
* **SemanticOwnerPatternId:** `G.Core`
* **Uses:** `{G.Core}` *(cites `G.Core.TriggerAliasMap.G6`; does not redefine meanings)*
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `RSCRTriggerKindId` (canonical id recorded)
  * `RSCRTriggerAliasId?` *(e.g., legacy human labels such as `G.6:H3:...` recorded as labels only)*
  * `scope: PathSliceId[] | PathId[] | PatternScopeId`
  * `TriggerAliasMapRef := G.Core.TriggerAliasMap.G6` *(docking reference)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
* **Notes (wiring‑only):** This module preserves ergonomics/back‑compat by allowing `G.6:H3:*` labels, while requiring that recorded causes use canonical `RSCRTriggerKindId` (per `CC‑GCORE‑TRIG‑3`).

**GPatternExtension: SoSLOGPathCitationWiring**

* **PatternScopeId:** `G.6:Ext.SoSLOGPathCitationWiring`
* **GPatternExtensionId:** `SoSLOGPathCitationWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **SemanticOwnerPatternId:** `C.23`
* **Uses:** `{C.23, C.19, G.5, G.11}` *(SoS‑LOG decisions cite paths; optional lens/attribution wiring is owned by C.19; refresh consumes triggers)*
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `SoSLogRuleId[]` / `BranchId[]` *(as cited labels; semantics owned by C.23)*
  * `FailureBehaviorPolicyId` *(when `degrade(mode=...)` is used)*
  * `PathId[] | PathSliceId[]` (the cited justification addresses)
  * `LensId?` *(when a C.19 lens is used for attribution/explainability; id only; semantics owned by C.19)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
* **Notes (wiring‑only):** G.6 does not define LOG semantics; it defines the *path‑citation surface* that LOG must cite.

**GPatternExtension: BridgeSentinelWiring**

* **PatternScopeId:** `G.6:Ext.BridgeSentinelWiring`
* **GPatternExtensionId:** `BridgeSentinelWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **SemanticOwnerPatternId:** `G.7`
* **Uses:** `{G.7, G.11}` *(bridge/sentinel semantics & calibration artefacts are owned by G.7; refresh orchestration is owned by G.11)*
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**

  * `BridgeId/BridgeCardId`
  * `RegressionSetId?` / `SentinelId[]?` *(as published by G.7, when sentinel wiring is used)*
  * `PathId[] | PathSliceId[]` *(paths that cite the bridge and must be re‑audited on bridge/sentinel changes)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingSurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
* **Notes (wiring‑only):** This module requires that bridge/sentinel changes re‑trigger RSCR **path‑locally** for affected `PathId/PathSliceId` scopes, without redefining sentinel semantics (owned by G.7) and without inventing new trigger kinds (owned by `G.Core`).

**GPatternExtension: QD_OEE_TelemetryPins**

* **PatternScopeId:** `G.6:Ext.QD_OEE_TelemetryPins`
* **GPatternExtensionId:** `QD_OEE_TelemetryPins`
* **GPatternExtensionKind:** `MethodSpecific`
* **SemanticOwnerPatternId:** `C.18` *(QD artefact semantics); uses `C.19` for exploration/logging/lens wiring as needed*
* **Uses:** `{C.18, C.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**

  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `InsertionPolicyRef` *(policy id or pinned policy ref, per owner semantics)*
  * `EmitterPolicyRef?`
  * `LensId?` *(when a C.19 lens is used in selection/telemetry attribution)*
  * `TransferRulesRef.edition?` / `EnvironmentValidityRegionRef?` *(when open‑ended / transfer events are in scope)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring‑only):** This module enforces reproducibility of archive/illumination and open‑ended telemetry *when those surfaces are used*, without pulling QD/OEE semantics into the EvidenceGraph core.

---

### G.6:5 - Archetypal Grounding (System / Episteme)

**System (Γ_sys):** *Autonomous brake envelope claim.*
Claim: “Stop within 50 m from 100 km/h.” EvidenceGraph nodes include proof carriers (TA/VA), instrumented track tests (LA/VA), calibration carriers, and an external test lab as an external evidencing role (no self‑evidence). A `PathId` provides a stable justification address; empirical legs are bound to explicit windows; crossings (if any) are explicit and pinned.

**Episteme (Γ_epist):** *Benchmark parity/replication lineage (post‑2015 practice).*
Claim: “Method family M attains parity on ImageNet‑style tasks under a declared evaluation protocol.” EvidenceGraph nodes include replication carriers (LA), legality/metric‑soundness carriers (VA), and tool‑qualification carriers (TA). The cited `PathId` binds the `ReferencePlane`, the scope slice, and the pinned evaluation/legal surfaces (by edition/policy ids rather than prose). When refresh triggers occur (edition pin change, evidence surface edit, decay events), downstream artefacts can re‑cite or re‑compute using the same `PathSliceId` addressing discipline.

### G.6:6 - Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
Scope: Universal for the EvidenceGraph kit; any method‑specific telemetry/portfolio wiring is modularized as Extensions and cited to its semantic owners.

### G.6:7 - Conformance Checklist (normative) — **CC‑G6**

| ConformanceId                                     | Requirement                                                                                                                                                                                                                                                                                                                                                                  | Purpose |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **CC‑G6‑CoreRef**                                 | `G.6` is conformant only if it satisfies the **effective** `CC‑GCORE‑*` set expanded from the `GCoreLinkageManifest` in **§4.1** (explicit crossings & pins, penalties→`R_eff` only, P2W split, typed RSCR trigger kinds, single‑owner defaults, UTS discipline, Δ‑discipline).                                                                                                 | Route core invariants |
| **CC‑G6‑1 (Anchor & lanes)**                      | Every citable path MUST resolve to A.10 anchors (SCR/RSCR addressable) and MUST declare lane tags (`TA/VA/LA`) on bindings.                                                                                                                                                                                                                                                | Ground auditability |
| **CC‑G6‑2 (No self‑evidence)**                    | Any evidencing `TransformerRole` that certifies the evaluated holon is external; reflexive cases MUST be modelled as a meta‑holon.                                                                                                                                                                                                                                         | Avoid reflexive evidence |
| **CC‑G6‑3 (Context/Plane & crossings)**           | Paths MUST declare `BoundedContext` and `ReferencePlane`, and MUST expose explicit crossing pins when crossings are present. *(Delegation target: `CC‑GCORE‑CROSS‑1`.)*                                                                                                                                                                                                    | Make crossings explicit |
| **CC‑G6‑4 (Penalty routing)**                     | Any crossing/plane penalty wiring visible in G.6 artefacts MUST route penalties to `R_eff` only and MUST preserve `F/G` invariance under penalties. *(Delegation target: `CC‑GCORE‑PEN‑1`.)*                                                                                                                                                                             | Preserve lane purity |
| **CC‑G6‑5 (Γ‑fold discipline + default ownership)** | If a `Γ‑fold` is not explicitly overridden by pinned CAL artefacts, G.6 MUST cite the single owner of `DefaultId.GammaFoldForR_eff` rather than asserting a local default. If a `Γ‑fold` is explicitly overridden, the path/SCR surface MUST cite the relevant CAL `ProofLedger` ids and publish the override as an auditable pin (not as prose). *(Delegation: `CC‑GCORE‑DEF‑1`; override semantics owned by `G.4`.)* | Keep folding auditable |
| **CC‑G6‑6 (Time/decay/validity binding)**         | Empirical legs MUST expose freshness/time binding (window selector or policy pin) and MUST support an explicit `validUntil`/expiry marker when one is declared (or an equivalent decay/freshness policy pin that implies expiry). Expiry/decay MUST be representable as refresh/RSCR‑relevant change using typed canonical causes. *(Delegation intent: typed causes are core‑owned; see `CC‑GCORE‑TRIG‑*`.)*                                  | Enable refresh readiness |
| **CC‑G6‑7 (Design/run split)**                    | Design‑time method descriptions and run‑time work traces MUST NOT be fused into one undifferentiated node; the graph MUST preserve the design↔run boundary via explicit carriers/bridges. *(Delegation intent: P2W split is core‑owned; see `CC‑GCORE‑P2W‑1`.)*                                                                                                            | Preserve P2W boundary |
| **CC‑G6‑8 (SCR projection completeness)**         | For any cited `PathId/PathSliceId`, the Assurance SCR view MUST expose at least: lane split, scope/plane pins, freshness/validity binding, explicit crossing pins (and the effective bottleneck `CL`/`CL^k`/`CL^plane` when crossings exist), the effective `Γ‑fold` in force for any `R_eff` folding (default or override, plus CAL `ProofLedger` ids when overridden), and links to contributing A.10 anchors and any CAL evidence/profile refs. | Make decisions auditable |
| **CC‑G6‑9 (Citable PathIds)**                     | Any SoS‑LOG admit/degrade/abstain decision or maturity rung transition that relies on provenance MUST cite `PathId`(s) (or `PathSliceId`(s) when snapshot‑binding is required).                                                                                                                                                                                            | Decision traceability |
| **CC‑G6‑10 (SpanUnion justification note)**       | If a SpanUnion/non‑interaction claim is made across evidence lines, an explicit independence justification MUST be published (as an addressable artefact linked to the path).                                                                                                                                                                                                | Non‑interaction audit |
| **CC‑G6‑11 (UTS hooks)**                          | Evidence artefacts and paths minted for citation MUST be UTS‑citable with twin labels and edition pins. *(Delegation target: `CC‑GCORE‑UTS‑1`.)*                                                                                                                                                                                                                           | Stable citations |
| **CC‑G6‑12 (IndependenceCertificate)**            | Independence for SpanUnion claims MUST be carried by an `IndependenceCertificate` (per the relevant certificate pattern) and referenced from SCR/paths.                                                                                                                                                                                                                    | Certificate surface |
| **CC‑G6‑13 (Mandatory provenance pins)**          | Any published/cited path surface MUST expose: `EvidenceGraphId`, `PathId/PathSliceId`, lane split, scope/plane pins, freshness/validity pins when applicable, crossing pins when applicable, and the minimal pin set required by §4.1. When `R_eff` folding is published/relied upon, the effective `Γ‑fold` in force MUST be exposed (default or override, plus CAL `ProofLedger` ids when overridden). When QD/OEE telemetry pins are in use, the extension‑required edition/policy pins MUST also be exposed. | Pin completeness |
| **CC‑G6‑14 (Legality binding; no shadow specs)**  | If numeric operations are cited/used in a path, legality MUST be pinned/cited via `CG‑Spec` rather than asserted locally, and the path/SCR surface MUST fail fast on illegal arithmetic/typing (e.g., CSLC/scale violations); do not “promote” ordinal to cardinal by convention inside G.6. *(Delegation target for “no shadow specs”: `CC‑GCORE‑CN‑CG‑1`.)*                                                                                     | Prevent illicit arithmetic |
| **CC‑G6‑15 (Conditional: QD/OEE telemetry pins)** | *(Conditional)* If `G.6:Ext.QD_OEE_TelemetryPins` is used, the required edition/policy pins from that extension (at minimum `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and the relevant insertion/emitter/transfer policy pins when applicable) MUST be recorded for reproducibility and must participate in RSCR triggering using canonical trigger kind ids.                                                                 | Reproducible archive/OEE |

### G.6:7.5 - Interfaces & Hooks (normative)

Each hook below defines: **Trigger → Obligation → Publishes/Consumes → Invariants**.
Where universal invariants apply (crossings, penalties, trigger typing), this section *cites* `G.Core` rather than redefining semantics.

#### G.6:7.5.1 - H1 — UTS Name Card for Evidence Artefacts

* **Trigger.** A new EvidenceGraph node is minted (an A.10‑anchored evidence artefact or role).
* **Obligation.** Mint a UTS Name Card with twin labels (Tech/Plain), citing the home context anchor and any required edition pins.
* **Publishes/Consumes.** Publishes: UTS row. Consumes: A.10 anchor metadata.
* **Invariants.** UTS publication and any deprecation/aliasing follow `G.Core` routing to F.17 (UTS discipline).

#### G.6:7.5.2 - H2 — UTS PathCard (PathId/PathSliceId)

* **Trigger.** A new `PathId` (or `PathSliceId`) is minted.
* **Obligation.** Publish a UTS PathCard with twin labels, listing the explicit pins required by §4.1 (context/plane/time binding, crossing pins if any). If an extension requires additional pins for reproducibility (e.g., `G.6:Ext.QD_OEE_TelemetryPins`), those pins MUST be present when the extension is in use.
* **Publishes/Consumes.** Publishes: UTS row(s). Consumes: EvidenceGraph path metadata + any extension‑required pins.
* **Invariants.** Crossing visibility and penalty routing are delegated to `G.Core` (`CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑PEN‑1`).

#### G.6:7.5.3 - H3 — RSCR Trigger on Evidence‑Impacting Edit (typed; alias‑dockable)

* **Trigger.** Any edit in G.6 that can change a path’s audit‑relevant surface (evidence structure, crossing pins, penalty policy pins, plane binding, freshness binding, edition/policy pins, or telemetry‑bound fields).
* **Obligation.** Emit RSCR triggers **using canonical `RSCRTriggerKindId`** (from `G.Core`) and record affected scope (`PathId/PathSliceId`) plus payload pins required for downstream refresh. If a legacy `G.6:H3:*` label is recorded, it is recorded as an alias label and docked via `G.Core.TriggerAliasMap.G6`. When `G.6:Ext.BridgeSentinelWiring` is used, include the bridge/sentinel payload pins required by that extension.
* **Publishes/Consumes.** Publishes: RSCR triggers and any associated RSCR test ids. Consumes: relevant pins/refs and CAL artefact references where applicable.
* **Invariants.** Trigger typing and alias docking are delegated to `G.Core` (`CC‑GCORE‑TRIG‑*`). Penalty routing invariants are delegated (`CC‑GCORE‑PEN‑1`).

#### G.6:7.5.4 - H4 — SoS‑LOG Path Citation (selector explainability)

* **Trigger.** A SoS‑LOG rule yields a tri‑state decision for a selection‑relevant pair (e.g., `(TaskSignature, MethodFamily)`), and the decision is justified by evidence.
* **Obligation.** The branch record MUST cite the relevant `PathId/PathSliceId`(s) and the minimal pins required to re‑audit the justification. Any method‑specific attribution fields are handled via Extensions (e.g., `G.6:Ext.SoSLOGPathCitationWiring` for `LensId`/FailureBehavior wiring, `G.6:Ext.BridgeSentinelWiring` for bridge‑monitoring payload pins when cross‑context reuse is invoked, `G.6:Ext.QD_OEE_TelemetryPins` for QD/OEE pins).
* **Publishes/Consumes.** Publishes: an SCR‑visible branch record with cited paths. Consumes: EvidenceGraph path queries.
* **Invariants.** Tri‑state semantics are core‑owned (`CC‑GCORE‑GUARD‑1`); G.6 does not add a new decision value.

#### G.6:7.5.5 - H5 — Maturity Rung Transition Justification

* **Trigger.** A maturity rung transition is proposed and justified by evidence.
* **Obligation.** The transition MUST cite one or more `PathId/PathSliceId`(s) and MUST publish an updated maturity entry with those citations. Missing path citations forbid rung advance.
* **Publishes/Consumes.** Publishes: updated UTS entry for maturity artefacts. Consumes: cited paths and A.10 anchors.
* **Invariants.** Any thresholding policy remains owned by CAL/LOG owners; G.6 provides citation, not policy.

#### G.6:7.5.6 - H6 — Bridge/CL Edge Annotation (GateCrossings)

* **Trigger.** An EvidenceGraph edge traverses a declared GateCrossing boundary (context/kind/plane/design↔run/edition).
* **Obligation.** Publish a CrossingSurface‑checkable crossing record with explicit crossing pins (UTS row id, Bridge id/card id if applicable, CL regime pins if applicable, and plane pins if applicable).
* **Publishes/Consumes.** Publishes: crossing row/pins. Consumes: GateCrossing metadata and Bridge artefacts (when present).
* **Invariants.** Crossing visibility is core‑owned (`CC‑GCORE‑CROSS‑1`); penalties routing is core‑owned (`CC‑GCORE‑PEN‑1`).

#### G.6:7.5.7 - H7 — ReferencePlane penalty policy publication (ids only)

* **Trigger.** A path binds across different reference planes.
* **Obligation.** Publish the relevant policy identifiers (ids only; not tables) required to audit plane effects, alongside the path’s pins.
* **Publishes/Consumes.** Publishes: SCR/UTS fields containing policy ids. Consumes: the owner’s policy registries as cited artefacts (do not duplicate tables).
* **Invariants.** Penalty routing is delegated (`CC‑GCORE‑PEN‑1`); no shadow specs (`CC‑GCORE‑CN‑CG‑1`).

#### G.6:7.5.8 - H8 — CrossingSurface exposure (E.18)

* **Trigger.** G.6 artefacts are exported for release or consumed by downstream patterns that require GateCrossing checks.
* **Obligation.** Provide harness‑readable ids/pins so GateCrossing checks can verify: required crossing records exist, lexical constraints hold, and crossing pins are explicit.
* **Publishes/Consumes.** Publishes: checkable ids/pins. Consumes: GateCrossing + lexical rules.
* **Invariants.** Crossing discipline and ID continuity are core‑owned (`CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑ID‑*`).

#### G.6:7.5.9 - H9 — SCR surface for assurance provenance

* **Trigger.** A downstream artefact cites a path for audit/selection/maturity.
* **Obligation.** Expose the required provenance fields in SCR views: lane split, context/plane pins, freshness binding, crossing pins (when present), and links to A.10 anchors and CAL refs.
* **Publishes/Consumes.** Publishes: SCR view(s). Consumes: EvidenceGraph paths and cited owner artefacts.
* **Invariants.** Default ownership is routed (`CC‑GCORE‑DEF‑1`) when defaults are cited.

#### G.6:7.5.10 - H10 — ProofLedger linkage (CAL ↔ G.6)

* **Trigger.** A proof obligation or evidence role is attached to a claim and is represented in G.4 artefacts.
* **Obligation.** Link EvidenceGraph nodes/edges to CAL ProofLedger/EvidenceProfiles entries and to A.10 carriers via the minimal provenance edge vocabulary.
* **Publishes/Consumes.** Publishes: CAL proof refs as pins in the path explanation surface. Consumes: CAL artefacts.
* **Invariants.** G.6 does not redefine CAL proof semantics; it only cites them.

#### G.6:7.5.11 - H11 — Telemetry ingest (selector & probe outcomes)

* **Trigger.** Run‑time outcomes (selection, probes, parity runs, measurement updates) produce observations that bear on previously asserted claims.
* **Obligation.** Ingest the observation as a run‑time evidence line (anchored in A.10), with explicit lane typing and explicit scope/time binding. If method‑specific telemetry pins are required, they are governed by Extensions (e.g., `G.6:Ext.QD_OEE_TelemetryPins`).
* **Publishes/Consumes.** Publishes: new EvidenceGraph nodes/edges + any required UTS rows + typed RSCR triggers when impacts occur. Consumes: run‑time carriers/attestations as conceptual anchors.
* **Invariants.** P2W split is respected (`CC‑GCORE‑P2W‑1`); typed trigger discipline is respected (`CC‑GCORE‑TRIG‑*`).

#### G.6:7.5.12 - Minimal conformance (hooks)

1. UTS publication for minted evidence artefacts and paths (H1–H2), per routed UTS discipline.
2. Typed RSCR triggers on evidence‑impacting edits (H3) using canonical trigger kind ids.
3. LOG and maturity artefacts cite paths when evidence is used (H4–H5).
4. GateCrossing/crossing records are explicit and checkable when crossings occur (H6–H8).
5. SCR views expose the minimal provenance pins for cited paths (H9–H10).
6. Run‑time telemetry is ingested without collapsing design↔run boundaries (H11).

### G.6:8 - Common Anti-Patterns and How to Avoid Them

* **Narrative‑only provenance (“because story”).**
  **Avoid:** mint `PathId/PathSliceId` and require citation for any decision that claims evidence‑based justification (CC‑G6‑9).
* **Implicit crossings (“same thing, different context”).**
  **Avoid:** represent crossings only via explicit crossing artefacts/pins; treat edition/plane/context changes as explicit crossing‑relevant edits and trigger RSCR (core‑owned crossing discipline).
* **Smuggling legality rules into EvidenceGraph prose.**
  **Avoid:** cite/pin legality surfaces (`CG‑Spec` and CAL artefacts); do not introduce local “mini‑CG” rules in G.6 (route via `CC‑GCORE‑CN‑CG‑1`).
* **Unpinned editions/policies (“it’s obvious which version”).**
  **Avoid:** require explicit edition/policy pins on citable paths; treat changes as typed triggers.
* **Alias‑only RSCR causes (“H3: something changed”).**
  **Avoid:** record canonical `RSCRTriggerKindId` as the cause; aliases are labels only and must dock via `G.Core.TriggerAliasMap.G6`.

### G.6:9 - Consequences

**Benefits.** Path‑addressable provenance; crossing/plane effects are auditable by pins rather than folklore; selectors and auditors share the same object; refresh becomes localized (path‑scoped) rather than global “rerun everything”.
**Trade‑offs.** Authors must declare (or pin) time/plane/scope and keep pins explicit; mitigated by reusing CAL EvidenceProfiles and by modularizing method‑specific telemetry as Extensions.

### G.6:10 - Rationale

G.6 concretizes the “because‑graph” implicit in A.10 into a typed, lane‑aware DAG with stable path addresses. It relies on canonical owners for semantics:

* A.10 for anchoring discipline and carrier reality,
* B.3 for the assurance skeleton,
* G.4 for proof/evidence profile semantics,
* `G.Core` for universal crossing, penalty, default ownership, and typed RSCR cause discipline.

This preserves conceptual modularity: G.6 standardizes *addressable provenance*, not a competing legality or selection mechanism.

### G.6:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice in reproducibility and evaluation governance by:

* treating **provenance and versioning/pinning** as first‑class audit surfaces (rather than informal “methods” prose),
* enabling **selective re‑evaluation** (path‑scoped refresh) rather than global reruns whenever one policy/edition changes,
* separating **design‑time specifications** from **run‑time traces/telemetry**, matching modern reproducibility and “lineage” practice in complex ML/scientific pipelines,
* keeping **method‑family specifics** (e.g., archive/illumination/QD pins or open‑ended telemetry pins) modular via extension wiring instead of embedding them into the universal provenance core.

### G.6:12 - Relations

**Builds on:** `G.Core`, `A.10` (evidence anchors/carriers; SCR/RSCR), `B.3` (assurance skeleton), `F.9` (BridgeCard/CL), `G.4` (CAL EvidenceProfiles/ProofLedger), `E.18/A.21` (GateCrossing/CrossingSurface checks), `E.10` (lexical rules), `E.5.*` (notation independence), `F.17` (UTS), `F.15` (RSCR).
**Publishes to:** UTS (Name Cards + PathCards), SCR/RSCR surfaces, downstream selectors/LOG by `PathId` citation, refresh/orchestration as typed triggers (consumed by `G.11` when used).
**Used by:** `G.5` (selector explainability and admissibility justifications), `G.8` (SoS‑LOG bundles), `G.9` (parity harness traces), `G.10` (shipping pins and audit payload), `G.11` (refresh orchestration).
**Constrains:** downstream patterns MUST cite paths when evidence is claimed; they MUST treat edits to pinned evidence/crossing/policy/edition/time bindings as refresh‑relevant causes with canonical trigger ids (routing via `G.Core`).

### G.6:End

## G.7 - Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)

**Tag.** Architectural pattern
**Stage.** design‑time (calibration + publication) + run‑time (sentinel‑driven telemetry emission; orchestration owned by **G.11**)

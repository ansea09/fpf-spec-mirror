---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__005_solution.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:4 — Solution"
line_start: 93312
line_end: 93577
dependencies:
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.6.7"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.13"
  - "G.Core"
keywords:
  - "Default Governing Definition Index"
  - "ID continuity"
  - "Part‑G invariants"
  - "RSCR trigger kinds"
  - "core linkage"
  - "delegation-first core"
---

### G.Core:4 - Solution

`G.Core` establishes Part‑G‑wide invariants as **delegation rules + typed catalogs + authoring discipline**.

#### G.Core:4.1 - Delegation-first citation for Part‑G‑wide invariants

`G.Core` is a *citation hub*, not a “second spec”. For any Part‑G‑wide invariant that already has a governing definition, `G.Core`:

1) standardises naming via `SuiteObligations.*` (A.6.7:4.2), and
2) records where the invariant is governed, so downstream patterns cite rather than restate.

**Delegation table (normative index; no semantic duplication).**

| Obligation handle | Canonical governing definition(s) | Part‑G note |
| --- | --- | --- |
| `transport_declarative_only` + `cg_spec_cite_required_for_numeric_ops` | A.6.7 + A.19 (CN‑Spec) + G.0 (CG‑Spec) + A.19.CHR | CN/CG are *pins*, not copies (“governing spec refs are pins, not copies”). No embedded/shadow governing spec refs. |
| `bridge_only_crossings` | A.6.7 + E.18 | Any cross-Context or cross-plane/kind move is Bridge‑mediated; no implicit crossings. |
| `crossing_visibility_required` | E.18 (CrossingBundle) + A.6.7 | Crossing visibility is a published **CrossingBundle**. `edition_key` changes on **crossing‑relevant artefacts** (Bridge/CL surfaces, BridgeCards, CrossingBundle registries, and UTS rows for crossing artefacts) are treated as crossing-bundle edits. If the required CrossingBundle is missing/non‑conformant, downstream consumers MUST **abstain** from cross-Context or cross-plane reuse (no silent crossings). |
| `two_bridge_rule_for_described_entity_change` | A.6.7 | entityOfConcern retargeting requires an explicit KindBridge (`CL^k`) in addition to any Context/Plane Bridge. |
| `guard_decision_tristate(pass|degrade|abstain)` + `unknown_never_coerces_to_pass` | A.6.7 + C.23 | `GuardDecision := {pass|degrade|abstain}` only; `unknown` maps to `degrade`/`abstain` via explicit SoS‑LOG branch/policy pins. |
| `penalties_route_to_r_eff_only` | A.6.7 | Penalties affect the **R lane (R_eff)** only; **F/G invariants** must not be altered by penalties. |
| `no_silent_scalarisation_of_partial_orders` + `no_silent_totalisation` | A.6.7 | Partial orders stay set‑valued; no silent scalar ranks or “helpful” totalisation. |
| `planned_slot_filling_in_work_planning_only` + `finalize_launch_values_in_work_enactment_only` + `gate_decision_separation` | A.15.3 + A.19.CHR + A.6.7 | Planned baselines are WorkPlanning‑only; launch/finalization values are WorkEnactment‑only; planning does not govern GateDecision/DecisionLog semantics. |
| `DefaultGoverningDefinitionIndex.single_governing_definition_per_DefaultId` | this pattern | Any default names exactly one governing definition; `G.Core.DefaultGoverningDefinitionIndex` is an index, not a second spec. |

This pattern also governs four pieces of Part‑G‑wide infrastructure that are **not** already governed elsewhere:

* the typed **RSCRTriggerKindId catalogue** (single writer),
* the **Default Governing Definition Index** (one governing definition per DefaultId; index only), and
* the **Δ‑discipline** for ID‑stable deduplication (delegation without public‑ID breakage), and
* the **linkage compression catalogues** (`GCoreConformanceProfileId`, `GCoreTriggerSetId`, `GCorePinSetId`) used to keep `G.x` linkage sections small.

#### G.Core:4.2 - Mandatory `G.Core linkage` manifest requirement for every `G.x`

Every pattern `G.x` in Part G SHALL include a short, explicit **Core linkage** section that is notation‑independent and id‑based.

* Relations: `Builds on: G.Core`.
* Solution: include a section named `G.x:<n> - G.Core linkage (normative)` that contains a `GCoreLinkageManifest` listing, at minimum:

  * `CoreConformanceProfileIds := { GCoreConformanceProfileId… }` *(preferred)* and/or `CoreConformanceIds := { CC‑GCORE‑… }`
  * `RSCRTriggerSetIds := { GCoreTriggerSetId… }` *(preferred)* and/or `RSCRTriggerKindIds := { RSCRTriggerKindId… }`
  * `CorePinSetIds := { GCorePinSetId… }` *(preferred)* and/or `CorePinsRequired := { … }` *(pins/refs surfaced by the kit; include policy‑id pins and edition pins when applicable; list only additions/overrides if pin sets are used)*
  * `DefaultsConsumed := { DefaultId… }` *(ids only; governing definition is resolved via `G.Core.DefaultGoverningDefinitionIndex`; cite governing definition, don’t restate)*
  * `TriggerAliasMapRef?` *(present or cited) if the pattern uses local trigger tokens*

**Nil‑elision (normative size rule).** Any field whose value is `∅` MAY be omitted; omission means `∅` and does not relax any obligation.

**Expansion rule (normative).** If profile/set ids are used, the effective `CoreConformanceIds` / `RSCRTriggerKindIds` / `CorePinsRequired` are the unions of their expansions plus any explicitly listed ids (see `G.Core:4.2.2`, `G.Core:4.2.3`, and `G.Core:4.3.4.2`).

##### G.Core:4.2.1 - `GCoreLinkageManifest` (canonical shape)

`GCoreLinkageManifest` is the minimal, pattern‑local wiring manifest for citing `G.Core` without duplicating universal prose.

A `G.x` MAY render the manifest as prose, a table, or structured notation, but the ids SHALL be recoverable by authoring review:

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds?: {GCoreConformanceProfileId…},
  CoreConformanceIds?: {CC‑GCORE‑…},
  RSCRTriggerSetIds?: {GCoreTriggerSetId…},
  RSCRTriggerKindIds?: {RSCRTriggerKindId…},
  CorePinSetIds?: {GCorePinSetId…},
  CorePinsRequired?: {…pin ids…},
  DefaultsConsumed?: {DefaultId…},
  TriggerAliasMapRef?: TriggerAliasMapRef
⟩`

##### G.Core:4.2.2 - `GCoreConformanceProfileId` catalogue (compression primitive)

A `GCoreConformanceProfileId` is a stable identifier for a named set of `CC‑GCORE‑*` items. It exists solely to reduce repetition in `G.x` linkage sections (no new semantics).

| GCoreConformanceProfileId | Expands to `CC‑GCORE‑*` (set) | Notes |
| --- | --- | --- |
| `GCoreConformanceProfileId.PartG.AuthoringBase` | `{CC‑GCORE‑CN‑CG‑1, CC‑GCORE‑CROSS‑1, CC‑GCORE‑PEN‑1, CC‑GCORE‑SET‑1, CC‑GCORE‑P2W‑1, CC‑GCORE‑DEF‑1, CC‑GCORE‑TRIG‑1, CC‑GCORE‑TRIG‑2, CC‑GCORE‑TRIG‑3, CC‑GCORE‑TRIG‑4, CC‑GCORE‑ID‑1, CC‑GCORE‑ID‑2, CC‑GCORE‑LINK‑1, CC‑GCORE‑LINK‑2}` | Default baseline for most Part‑G kits. |
| `GCoreConformanceProfileId.PartG.TriStateGuard` | `{CC‑GCORE‑GUARD‑1}` | Add when the kit defines/consumes eligibility/guard outcomes. |
| `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted` | `{CC‑GCORE‑UTS‑1}` | Add when the kit mints/evolves public ids (UTS rows). |
| `GCoreConformanceProfileId.PartG.ShippingBoundary` | `{CC‑GCORE‑SKP‑1}` | Add when shipping boundaries are in scope for the kit. |

##### G.Core:4.2.3 - `GCorePinSetId` catalogue (compression primitive)

A `GCorePinSetId` is a stable identifier for a named set of commonly recurring **pin obligations** used in Part‑G kits. It exists solely to reduce repetition in `G.x` linkage sections (no new semantics).

**Conditional pins (normative).** In pin‑set expansions below, a pin marked with `?` is **conditional**: it **MUST** be present iff the pattern actually uses the corresponding surface/artefact class; otherwise it MAY be omitted (nil‑elision permitted) and is treated as `∅`. A `G.x` MAY strengthen a conditional pin to unconditional by listing it explicitly in `CorePinsRequired`.

| GCorePinSetId | Expands to `CorePinsRequired` (set) | Notes |
| --- | --- | --- |
| `GCorePinSetId.PartG.AuthoringMinimal` | `{CG-FrameContext, entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩, CNSpecRef.edition, CGSpecRef.edition}` | Baseline scope+spec pins for most Part‑G authoring kits (design‑time, citable, refreshable). |
| `GCorePinSetId.PartG.CrossingVisibilityPins` | `{BridgeId/BridgeCardId, BridgeMatrixId?, CL/CL^k/CL^plane, Φ/Ψ/Φ_plane policy-ids, CrossingBundleId?, UTSRowId[]?, PathId[]/PathSliceId[]?}` | Use when the kit asserts or consumes crossings (Bridge‑only + visible). Conditional pins cover “only if that bundle is used” cases (UTS publication, path‑citable evidence, explicit CrossingBundle reference). |

#### G.Core:4.3 - RSCR Trigger Catalogue and docking discipline

`G.Core` is the **single writer** for Part‑G‑wide trigger kinds.

##### G.Core:4.3.1 - Definitions

* **RSCRTriggerKindId**
  Canonical, stable identifier for a *trigger kind* (a class of “why RSCR/refresh must fire”). Cross-pattern reason code.

* **RSCRTriggerAliasId**
  Pattern-scoped human label/token kept for ergonomics and alias continuity (e.g., `G.11:T4`, `G.6:H3:lane-tag correction`).

* **TriggerAliasMap**
  Mapping table: `RSCRTriggerAliasId → {RSCRTriggerKindId…}` (1..n).

* **RSCRTrigger**
  Minimal conceptual form (notation-independent):

  ```
  RSCRTrigger := ⟨
    triggerKindId: RSCRTriggerKindId,
    scope: PathSliceId[] | PathId[] | PatternScopeId,
    payloadPins: { …id pins… }
  ⟩
  ```

  Where `payloadPins` contains any edition pins, policy-ids, Bridge ids, evidence pins, regression-set ids, etc., required to make the trigger actionable.

##### G.Core:4.3.2 - Governing-definition model

* TriggerGoverningDefinition := `G.Core`.
* Any new trigger kind SHALL be added to `G.Core` first.
* Other patterns MAY define aliases only (or cite shared alias maps), and MUST map aliases to canonical kinds.

##### G.Core:4.3.3 - Authoring rules

* **No implicit triggers:**
  Any RSCR/SCR/refresh artefact that *records reasons* MUST record canonical `RSCRTriggerKindId`. Aliases may be recorded as labels, but must not be the only reason code.

* **No implicit overloading:**
  A local token string (e.g., `T4`) SHALL NOT silently change meaning across patterns; namespace is part of the alias (`G.11:T4` ≠ `A.20:T4`).

* **Granularity discipline:**
  If a local cause is narrower than an existing canonical kind, map it to that kind and keep the nuance as a local scope note. If the difference matters for planning/selection, add a new canonical kind.

* **Multi-cause discipline:**
  When an event spans multiple canonical kinds, record multiple triggers (preferred) or map the alias to a set `{…}` and require emitting the full set.

##### G.Core:4.3.4 - Seed canonical catalogue (Phase‑2 minimum)

The Phase‑2 stabilized canonical catalogue (based on the Phase‑2 inventory; sufficient to dock deprecated `G.6:H3` and `G.11:T0…T7` trigger labels and to populate `RSCRTriggerKindIds` in `G.0…G.13`):

* `RSCRTriggerKindId.LegalitySurfaceEdit`
* `RSCRTriggerKindId.PenaltyPolicyEdit`
* `RSCRTriggerKindId.CrossingBundleEdit`
* `RSCRTriggerKindId.ReferencePlaneEdit`
* `RSCRTriggerKindId.EditionPinChange`
* `RSCRTriggerKindId.TokenizationOrNameChange`
* `RSCRTriggerKindId.PolicyPinChange`
* `RSCRTriggerKindId.TelemetryDelta`
* `RSCRTriggerKindId.FreshnessOrDecayEvent`
* `RSCRTriggerKindId.EvidenceSurfaceEdit`
* `RSCRTriggerKindId.MaturityRungChange`
* `RSCRTriggerKindId.BaselineBindingEdit`
* `RSCRTriggerKindId.DefaultGoverningDefinitionChange`

##### G.Core:4.3.4.1 - Canonical kind definitions (normative, minimal)

Each `RSCRTriggerKindId` SHALL have a short, stable definition in `G.Core` (single-writer) to prevent semantic drift.

| RSCRTriggerKindId | Minimal meaning (cause class) | Typical payload pins (non-exhaustive) |
| --- | --- | --- |
| `RSCRTriggerKindId.LegalitySurfaceEdit` | A legality surface changed (CG‑Spec: ComparatorSet/SCP/Γ_fold/MinimalEvidence, or equivalent legality inputs). | `CGSpecRef.edition`, `ComparatorSetRef.edition`, `SCPRef.edition`, `ΓFoldRef.edition` |
| `RSCRTriggerKindId.PenaltyPolicyEdit` | A penalty / Φ / Ψ / FailureBehavior / SoS‑LOG branch policy changed. | penalty policy ids, `Φ`/`Ψ` policy ids, SoS‑LOG branch id pins |
| `RSCRTriggerKindId.CrossingBundleEdit` | A crossing bundle changed (Bridge/CL routing, crossing-bundle registry cards, crossing policy pins), including `edition_key` changes of crossing‑relevant artefacts (BridgeCards, CrossingBundle registries, UTS rows for crossing artefacts). | `BridgeId/BridgeCardId`, `BridgeMatrixId?`, `CL*` ids, crossing policy ids, `UTSRowId[]`, `PathId/PathSliceId?` |
| `RSCRTriggerKindId.ReferencePlaneEdit` | ReferencePlane or plane-routing surface changed. | `ReferencePlaneId`, plane-policy ids |
| `RSCRTriggerKindId.EditionPinChange` | Any pinned edition relevant to downstream artifacts changed (including **`CNSpecRef.edition`**, `CGSpecRef.edition`, comparator/method/descriptor/distance/etc.). Crossing‑artefact edition_key changes are additionally classified as `CrossingBundleEdit` per multi‑cause discipline. | changed `*.edition` pins, affected `PathSliceId`s |
| `RSCRTriggerKindId.TokenizationOrNameChange` | A published tokenization / naming / alias surface changed in a way that can affect docking, citations, or dispatch (e.g., UTS Name Cards, twin labels, alias maps). | affected `UTSRowId[]`, `NameCardId[]`, alias ids / maps |
| `RSCRTriggerKindId.PolicyPinChange` | A policy-id pin used by characterization changed (selection, insertion, emission, routing, refresh policy, etc.). | policy ids (and other non-edition configuration pins when they are explicitly pinned) |
| `RSCRTriggerKindId.TelemetryDelta` | Telemetry inputs that influence refresh/selection changed (not merely display-only). | telemetry ids/refs, `Audit`-published pins |
| `RSCRTriggerKindId.FreshnessOrDecayEvent` | Time/freshness/decay conditions affecting validity changed (window shift, decay thresholds, freshness policy edits). | freshness window refs/ids, decay/freshness policy ids |
| `RSCRTriggerKindId.EvidenceSurfaceEdit` | Evidence graph / evidence surface changed in ways that affect admissibility/acceptance/comparison. | evidence pins, `EvidenceGraph` refs, affected `PathId`s |
| `RSCRTriggerKindId.MaturityRungChange` | Maturity rung/ladder state changed for relevant artifacts or paths. | maturity rung ids, affected scopes |
| `RSCRTriggerKindId.BaselineBindingEdit` | Planned baseline bindings changed (planned slot fillings / binding refs), requiring a re-run along the P2W path. | `SlotFillingsPlanItem` refs, planned pins, variance pins |
| `RSCRTriggerKindId.DefaultGoverningDefinitionChange` | The governing definition of a `DefaultId` (as recorded in `G.Core.DefaultGoverningDefinitionIndex`) changed, or a default row was added/deprecated. | affected `DefaultId.*`, old governing definition ref, new governing definition ref |

##### G.Core:4.3.4.2 - Canonical trigger sets (compression primitive)

`GCoreTriggerSetId` identifies a named set of `RSCRTriggerKindId` values. A `G.x` MAY cite trigger sets in `RSCRTriggerSetIds` instead of repeating long `RSCRTriggerKindIds` lists.

| GCoreTriggerSetId | RSCRTriggerKindIds (set) | Notes |
| --- | --- | --- |
| `GCoreTriggerSetId.CGSpecGate` | `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}` | Covers CG‑Spec legality‑gate kits (e.g., `G.0`). |
| `GCoreTriggerSetId.SoTAHarvestSynthesis` | `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}` | Covers SoTA harvesting/synthesis packs (e.g., `G.2`). |
| `GCoreTriggerSetId.EvidenceGraphKit` | `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.BaselineBindingEdit}` | Covers EvidenceGraph/SCR kits (e.g., `G.6`). |
| `GCoreTriggerSetId.BridgeCalibrationKit` | `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.BaselineBindingEdit}` | Covers bridge calibration/CL kits (e.g., `G.7`). |
| `GCoreTriggerSetId.RefreshOrchestration` | `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.BaselineBindingEdit}` | Covers refresh orchestration (e.g., `G.11`). |

##### G.Core:4.3.5 - Initial alias maps

These alias maps are normative docking artefacts and preserve deprecated alias labels while moving semantics to canonical ids.

**TriggerAliasMap.G11**
Based on the existing trigger catalogue in `G.11` (`T0…T7`).

* `G.11:T0 → { RSCRTriggerKindId.PolicyPinChange }`
* `G.11:T1 → { RSCRTriggerKindId.TelemetryDelta }`
* `G.11:T2 → { RSCRTriggerKindId.EditionPinChange }`
* `G.11:T3 → { RSCRTriggerKindId.EditionPinChange }`
* `G.11:T4 → { RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit }`
* `G.11:T5 → { RSCRTriggerKindId.FreshnessOrDecayEvent }`
* `G.11:T6 → { RSCRTriggerKindId.MaturityRungChange }`
* `G.11:T7 → { RSCRTriggerKindId.PolicyPinChange }`

**TriggerAliasMap.G0 (reserved; empty in Phase‑2).**
Map any stable deprecated registry-hook labels emitted/recorded by `G.0` to the canonical kinds above (typically `LegalitySurfaceEdit`, `PenaltyPolicyEdit`, `CrossingBundleEdit`, `ReferencePlaneEdit`, `TokenizationOrNameChange`), preserving the original label text as `RSCRTriggerAliasId`. If none exist, `G.0` SHOULD emit canonical `RSCRTriggerKindId` values directly.

**TriggerAliasMap.G6**
EvidenceGraph `H3` example causes → canonical kinds:

* `G.6:H3:freshness/decay change → { RSCRTriggerKindId.FreshnessOrDecayEvent }`
* `G.6:H3:Bridge CL/CL^k or loss update → { RSCRTriggerKindId.CrossingBundleEdit }`
* `G.6:H3:Φ/Ψ policy change → { RSCRTriggerKindId.PenaltyPolicyEdit }`
* `G.6:H3:lane tag correction → { RSCRTriggerKindId.EvidenceSurfaceEdit }`
* `G.6:H3:ReferencePlane correction → { RSCRTriggerKindId.ReferencePlaneEdit }`
* `G.6:H3:QD/OEE artefact updates (U.DescriptorMapRef.edition/DistanceDef, EmitterPolicyRef, InsertionPolicyRef, archive K-capacity) → { RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange }`

#### G.Core:4.4 - Default Governing Definition Index

`G.Core` provides an index of Part‑G defaults with **one governing definition** per `DefaultId`. The index is not a “second spec”; it is a cross-reference table that points to the *governing definition reference* (a CC item, policy‑id, or TaskSignature rule) and states applicability conditions.

##### G.Core:4.4.1 - Definitions

* **DefaultId**
  Stable identifier of a default (a default constant or default rule).

* **DefaultGoverningDefinitionRef**
  A reference to the governing definition of the default (e.g., a CC item id like `CC‑G5.23`, or a policy id, or a TaskSignature rule definition).

##### G.Core:4.4.2 - Rules

* Exactly one governing definition per `DefaultId`.
* Any other mention in `G.x` MUST be a citation/delegation to the governing definition, not a competing statement.
* A default may be conditional (default-rule) with explicit applicability conditions.
* The Default Governing Definition Index SHALL NOT be used to “smuggle” mandatory invariants as defaults. Invariants remain invariants (typically cited through `CC‑GCORE‑…` and their canonical governing definitions).

##### G.Core:4.4.3 - Seed Default Governing-definition assignment entries (Phase‑2 minimum)

| DefaultId                       | DefaultGoverningDefinitionRef                                           | Notes |
| ------------------------------ | --------------------------------------------------------- | ----- |
| `DefaultId.PortfolioMode`       | `CC‑G5.23`                                                | Existing governing definition; other mentions delegate to it. |
| `DefaultId.DominanceRegime`     | `CC‑G5.28`                                                | Existing governing definition; other mentions delegate to it. |
| `DefaultId.GammaFoldForR_eff`   | `CC‑G5.4`                                                 | Default Γ‑fold for `R_eff` is weakest‑link; overrides require explicit CAL support. |

This table may grow over time; the rule is that the **governing definition must already be named** (or be intentionally set to `G.Core` when the default is truly Part‑G‑wide and not governed elsewhere). Any change in a row (add/remove/change governing definition) SHALL be treated as a refresh‑sensitive edit and recorded as `RSCRTriggerKindId.DefaultGoverningDefinitionChange` (payload: affected `DefaultId.*`, old governing definition ref, new governing definition ref).

#### G.Core:4.5 - ID continuity protocol (Δ‑discipline)

When moving universal norms out of `G.x` into `G.Core`:

* existing public CC ids in `G.x` that may be referenced externally SHALL NOT be deleted or renamed;
* such CC items SHALL become **delegation** items that point to the relevant `CC‑GCORE‑…` item(s);
* each `G.x` SHALL add exactly one bridge CC item `CC‑Gx‑CoreRef` (first in its CC list) that makes linked `CC‑GCORE‑…` items mandatory for `G.x` conformance.

Deprecated trigger labels (e.g., `G.11:T*`, `G.6:H3:*`) are preserved as aliases and MUST map to canonical trigger kinds.

Non-CC public identifiers (e.g., `UTSRowId`, `RSCRTriggerAliasId`, deprecation notices, edition bumps) MUST obey the same Δ-discipline: preserve old ids; represent drift via alias/deprecation/edition evolution (see `F.17 (UTS)`); and emit canonical trigger kinds (`RSCRTriggerKindId.TokenizationOrNameChange`, `RSCRTriggerKindId.EditionPinChange`) when downstream impact is possible.

#### G.Core:4.6 - Explicit non-goals

`G.Core` does not:

* introduce CG‑frame kit entities (e.g., BridgeMatrix/ReferencePlane/Φ registries); those remain in their governing `G.x`;
* introduce method-family taxonomies, discipline packs, or generator orchestration mechanisms; those remain as `Extensions` in their governing definitions (e.g., synthesis/shipping/refresh patterns);
* define refresh algorithms; it defines trigger kinds and docking only.

---


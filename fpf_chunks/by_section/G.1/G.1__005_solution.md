---
chunk_kind: "child"
pattern_id: "G.1"
pattern_title: "CG‑Frame‑Ready Generator"
section_id: "G.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.1/G.1__005_solution.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "G.1 — CG‑Frame‑Ready Generator"
  - "G.1:4 — Solution"
line_start: 101121
line_end: 101403
dependencies:
  - "A.10"
  - "A.15.3"
  - "A.19"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.Core"
keywords:
  - "CGFrameLibraryId"
  - "CGKitId manifest"
  - "RSCR linkage surfaces"
  - "RefreshReadinessCardId"
  - "ShortlistId"
  - "SoTA_SetId"
  - "UTS/Name Cards"
  - "VariantPoolId"
  - "and set-result scaffold"
  - "edition pins"
  - "generator"
  - "generator chassis"
  - "selector"
  - "set-result outcome"
  - "set-return selection"
  - "shipping and refresh boundaries"
  - "six-card kit (M1-M6)"
---

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

  // Kit identifiers governed by this pattern (the “six cards”).
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

  // Consumed defaults (each default cites the governing definition listed in `G.Core.DefaultGoverningDefinitionIndex`).
  DefaultsConsumed := {
    DefaultId.GammaFoldForR_eff,   // governing definition: CC-G5.4
    DefaultId.PortfolioMode,       // governing definition: CC-G5.23
    DefaultId.DominanceRegime      // governing definition: CC-G5.28
  }
⟩
```

**Citation rule (normative):** `CC‑GCORE‑*`, `RSCRTriggerKindId.*`, and `DefaultId.*` semantics are governed by their canonical definitions: primarily `G.Core`, and for the defaults above the definitions listed in `G.Core.DefaultGoverningDefinitionIndex`. `G.1` MUST NOT restate or redefine those semantics.

#### G.1:4.2 - Six‑module generator chassis (normative)

**Core artefact:** `CGFrameReadyGeneratorKit := ⟨M1, M2, M3, M4, M5, M6⟩`, where each `Mi` is a **card** with an explicit I/O surface and stable identifiers.
`CGKitId` identifies the versioned **kit manifest** (`CG‑Kit@CG‑Frame`) that lists the six card ids and the minimal wiring pins needed to treat the chassis as a reusable unit (this is **not** a shipping pack; shipping remains governed by `G.10`).

The chassis is *view‑friendly*: it is an inventory of “what exists and how it is wired”, not a second specification of CN/CG/CHR/CAL/selection semantics.

##### M1 — CG‑FrameContext Card (scope anchor)

**Governs (kit surface):**

* `CG‑FrameContext` and its **binding pins**:

  * `entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩` *(pin set: `PartG.AuthoringMinimal`)*
  * `CNSpecRef.edition`, `CGSpecRef.edition` *(pin set: `PartG.AuthoringMinimal`)*
  * `ReferenceMap` *(cite `G.0:CG‑Spec.ReferenceMap`; do not duplicate semantics)*
  * any declared crossing/policy pins *(pin set: `PartG.CrossingVisibilityPins`)*

**Purpose:** provide the *single scope anchor* used by all downstream cards.

**Notes:** any spec-legality content is **cited** via `A.19 (CN‑Spec)` and `G.0 (CG‑Spec)` (delegation target: `CC‑GCORE‑CN‑CG‑1` via `CC‑G1‑CoreRef`); this card does not introduce a local “mini‑spec”.

##### M2 — SoTA_Set@CG‑Frame (harvester output card)

**Governs (kit surface):**

* `SoTAPaletteDescriptionId` and `SoTA_SetId` bound to `CG‑FrameContext`
* explicit provenance anchors for the set (via `A.10`), and any published UTS stubs/rows when applicable

**Governing pattern:** harvesting discipline and SoTA-pack payload are governed by `G.2`.
In `G.1`, M2 is a *slot in the chassis* and a wiring surface; it does not redefine the harvesting method.

##### M3 — VariantPool (candidate inventory + emitter trace)

**Governs (kit surface):**

* `VariantPoolId` bound to `CG‑FrameContext`
* per‑candidate minimal traceability fields (emitter identity, `EmitterPolicyRef` (policy‑id/ref; defined by the governing pattern), method/generator refs when declared, edition pins, provenance anchors)
* optional, per‑candidate **assurance preview pointers** (e.g., `PathSliceId?` and/or `SCRId?` when early assurance is recorded) and optional **QD/Open‑Ended scaffolding stubs** (only when introduced by explicit `GPatternExtension` blocks)

**Guardrails (via G.Core):**

* tri‑state eligibility handling, penalties routing, crossing visibility, and set‑return constraints are not defined here; they are enforced via `G.Core` conformance.

**Governing pattern for method payload:** method‑specific emitter semantics are governed by `Extensions` (e.g., `C.17`, `C.18`, `C.19`).
M3 MUST remain method‑agnostic in its core definition: it is an inventory surface, not an algorithm spec.

##### M4 — Shortlist (selector/assurer output)

**Governs (kit surface):**

* `ShortlistId` bound to `CG‑FrameContext`
* a selected set of candidates plus rationale and assurance records (`SCRId` required; `DRRId` optional; cite `PathId/PathSliceId` when applicable)
* optional **front metadata or archive metadata** needed for reproducibility when used: ε‑front parameters and/or archive snapshot hooks, with governing-definition assignment through `G.5` / `C.18` / `C.19` (no local semantics in `G.1`)

**Governing pattern:** selection/dispatch semantics are governed by `G.5`.
M4 MUST preserve *set‑return semantics* (as governed by `G.Core`) and MUST NOT hard‑code a forced singleton outcome.

##### M5 — CG‑FrameLibrary (published bindings index)

**Governs (kit surface):**

* `CGFrameLibraryId` bound to `CG‑FrameContext`
* an index of referenced CG‑Frame artefacts ready for reuse:

  * CHR/CAL/LOG bundles (by their ids; semantics governed by `G.3`, `G.4`, `G.8`)
  * published identifiers (UTS rows, Name Cards) per Part‑F governing definitions
  * additional Part‑F binding surfaces (e.g., RoleDescription templates, Concept‑Set rows) by governing definition‑ids only
  * RSCR test identifiers (e.g., from `F.15`) and worked examples (where applicable)

**Boundary:** M5 is a **kit/library surface**, not shipping. If a shipped pack is needed, governing-definition assignment is `G.10`.

##### M6 — RefreshReadiness Card (telemetry hooks + wiring)

**Governs (kit surface):**

* `RefreshReadinessCardId` bound to `CGFrameLibraryId` (and thus to `CG‑FrameContext`)
* `CGKitId` (the versioned kit manifest) binding `M1…M6` into a single reusable unit; it MUST enumerate the card ids and MAY carry references to deprecations/edition bumps minted by the canonical governing definitions
* declared telemetry hooks (what signals are observed, with what pins)
* declared RSCR wiring: which `RSCRTriggerKindId` are relevant (canonical ids), with minimal required payload pins (including `SlotFillingsPlanItemRef[]` when the chassis is bound into WorkPlanning)

**Boundary:** orchestration semantics are governed by `G.11`.
M6 prepares *refresh‑readiness metadata* and wiring stubs; it does not define scheduling/priority heuristics.

#### G.1:4.3 - Minimal I/O surface (normative)

| Module | Consumes                                                                    | Produces                                                                               |
| ------ | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| M1     | CG‑Frame brief + `entityOfConcern` + `CNSpecRef/CGSpecRef` (edition‑pinned) | `CG‑FrameContext` + context pins                                                       |
| M2     | discovery inputs + inclusion criteria *(via G.2)*                           | `SoTA_SetId` (+ provenance anchors; optional UTS stubs/rows)                           |
| M3     | `SoTA_SetId` + local constraints + emitter policy pins *(via Extensions)*   | `VariantPoolId` (+ candidate trace/provenance; optional method payload via Extensions) |
| M4     | `VariantPoolId` + acceptance/eligibility surfaces *(via G.4/G.5)*           | `ShortlistId` (selected set / set-result) + rationale refs                                         |
| M5     | `ShortlistId` + CHR/CAL/LOG bundle refs + UTS/Name refs                     | `CGFrameLibraryId` (library index; publish‑ready bindings)                             |
| M6     | telemetry inputs + freshness/decay policy pins + RSCR tests                 | `CGKitId` + `RefreshReadinessCardId` (wiring to `G.11`; no orchestration governance)    |

#### G.1:4.4 - Extensions (pattern‑scoped; non‑core)

All method/discipline/generator specifics MUST be expressed as `GPatternExtension` blocks.

> Guard: `G.1:Ext.*` are **PatternScopeId** values (internal, pattern‑scoped), not new patterns and not new `PatternId`.

##### GPatternExtension — `G.1:Ext.HarvesterWiring`

**PatternScopeId:** `G.1:Ext.HarvesterWiring`
**GPatternExtensionId:** `HarvesterWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.2`
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
**GoverningPatternId:** `G.5`
**Uses:** `{G.5, G.4}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ShortlistId`
* `SCRId` *(assurance and rationale record by id; semantics governed by the selector and assurance governing definitions)*
* `DRRId?` *(when a decision‑rationale artefact is minted; otherwise omitted)*
* `TaskSignatureRef?` *(if selection is task‑templated; otherwise omitted)*
* `AcceptanceClauseId[]` *(as referenced from `G.4` outputs)*
* any explicit selector policy pins *(policy‑id/ref; defined by the governing pattern)* when not defaulted (the omitted default cites its governing definition through `G.Core.DefaultGoverningDefinitionIndex`)

**Notes (wiring‑only):** `G.1` does not redefine selection: it binds M4’s output surface to the `G.5` selector/dispatcher kernel.

##### GPatternExtension — `G.1:Ext.CreativityCHR`

**PatternScopeId:** `G.1:Ext.CreativityCHR`
**GPatternExtensionId:** `CreativityCHR`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `C.17`
**Uses:** `{C.17, G.3}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `CHRPackId?` *(if creativity characteristics are published/typed)*
* edition/policy pins required by the chosen creativity characteristic set (governed by `C.17`)

**Notes (wiring‑only):** `G.1` only records which creativity characteristics are used for M3/M4 wiring; legality/typing lives in the CHR governing definitions.

##### GPatternExtension — `G.1:Ext.NQD`

**PatternScopeId:** `G.1:Ext.NQD`
**GPatternExtensionId:** `NQD`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
**Uses:** `{C.18, C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `InsertionPolicyRef` *(policy id / ref, as defined by the governing definition)*
* `TaskSignatureRef?` *(when QD is enabled via TaskSignature flags/traits rather than by an external switch)*
* `DHCMethodRef.edition?` *(when illumination/coverage summaries are pinned to a method)*
* `EmitterPolicyRef` *(policy‑id/ref; points to the exploration governance governing definition, e.g., `C.19` when E/E‑LOG is used)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (wiring‑only):** QD/QD‑adjacent algorithm families and their parameterisations belong to `C.18 and C.19`; `G.1` only fixes the pins needed to make the VariantPool and Shortlist reproducible.

##### GPatternExtension — `G.1:Ext.OpenEndedFamilyWiring`

**PatternScopeId:** `G.1:Ext.OpenEndedFamilyWiring`
**GPatternExtensionId:** `OpenEndedFamilyWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.2` *(family semantics are governed by SoTA cards; this block only wires pins; selector-side wiring is governed by `G.5`.)*
**Uses:** `{G.2, G.5, C.19, C.23}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GeneratorFamilyId[]`
* `TransferRulesRef.edition` *(mandatory when Open‑Ended is enabled)*
* `EnvironmentValidityRegionRef?`
* `CoEvoCouplerRef[]?`
* `SoSLogBranchId[]?` *(when validity of generated tasks is gated by explicit branches)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (wiring‑only):** this block enables declared sets of `{Environment, MethodFamily}` pairs without redefining generator semantics in `G.1`; it should cite/align with the selector‑side wiring in `G.5:Ext.OpenEndedFamilyWiring`.

##### GPatternExtension — `G.1:Ext.RefreshWiring`

**PatternScopeId:** `G.1:Ext.RefreshWiring`
**GPatternExtensionId:** `RefreshWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.11`
**Uses:** `{G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `RefreshReadinessCardId`
* `RSCRTestId[]`
* canonical `RSCRTriggerKindId[]` emitted/recorded (aliases only as labels, if any)
**RSCRTriggerSetIds:** `{GCoreTriggerSetId.RefreshOrchestration}`
**Notes (wiring‑only):** M6 declares readiness and wiring; orchestration semantics (queueing, prioritisation, cadence) are governed by `G.11`.

##### GPatternExtension — `G.1:Ext.ShippingWiring`

**PatternScopeId:** `G.1:Ext.ShippingWiring`
**GPatternExtensionId:** `ShippingWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.10`
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


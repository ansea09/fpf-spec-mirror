---
chunk_kind: "child"
pattern_id: "G.8"
pattern_title: "SoS‑LOG Bundles & Maturity Ladders"
section_id: "G.8:5"
section_title: "Extensions (pattern‑scoped; non‑core)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.8/G.8__006_extensions-pattern-scoped-non-core.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "G.8 — SoS‑LOG Bundles & Maturity Ladders"
  - "G.8:5 — Extensions (pattern‑scoped; non‑core)"
line_start: 80314
line_end: 80428
dependencies:
  - "A.10"
  - "A.21"
  - "C.18"
  - "C.19"
  - "C.22"
  - "C.23"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.17"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "SoS-LOG"
  - "admissibility ledger"
  - "rule ids"
  - "tri-state {pass"
---

### G.8:5 - Extensions (pattern‑scoped; non‑core)

`G.8` keeps method/generator specificity out of the core kit. Any such specificity appears as `GPatternExtension` blocks with stable **PatternScopeId**s.

#### G.8:5.1 - `G.8:Ext.SoSLOGWiring`

**PatternScopeId:** `G.8:Ext.SoSLOGWiring`
**GPatternExtensionId:** `SoSLOGWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.23`
**Uses:** `{C.23}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoSLogRuleId[]`
* `SoSLogBranchId[]?`
* `FailureBehaviorPolicyId?` *(when degrade behaviour is policy‑bound)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.8:4.1`)*
**Notes (wiring‑only):**
* Rule meaning, branch taxonomy, and “probe/sandbox” semantics are governed by `C.23`; this module only binds ids and pins.

#### G.8:5.2 - `G.8:Ext.AcceptanceWiring`

**PatternScopeId:** `G.8:Ext.AcceptanceWiring`
**GPatternExtensionId:** `AcceptanceWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `G.4`
**Uses:** `{G.4}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `AcceptanceClauseId[]`
* `EvidenceProfileId[]?` *(if the ledger/bundle cites evidence profile ids rather than only paths)*
* `PromotionPolicyId?` *(only if telemetry may be promoted into dominance by explicit CAL policy)*

**RSCRTriggerKindIds (optional delta):** `{RSCRTriggerKindId.PolicyPinChange}` *(only if acceptance policies are pinned as ids in the bundle/ledger)*
**Notes (wiring‑only):**
* Thresholds remain governed by `G.4` Acceptance; this module carries only clause ids and policy pins.

#### G.8:5.3 - `G.8:Ext.BridgeReuseWiring`

**PatternScopeId:** `G.8:Ext.BridgeReuseWiring`
**GPatternExtensionId:** `BridgeReuseWiring`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.7`
**Uses:** `{G.7, F.9}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `BridgeId/BridgeCardId`
* `CL/CL^k/CL^plane`
* `Φ/Ψ/Φ_plane policy-ids`
* `BridgeCalibrationTableId?`, `RegressionSetId?` *(if cited as calibration evidence)*

**RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(only if the bundle/ledger explicitly binds calibration records by id)*
**Notes (wiring‑only):**
* Present only when `SoS‑LOGBundle@Context` asserts cross-Context or cross-plane reuse. No additional crossing semantics are defined here.

#### G.8:5.4 - `G.8:Ext.QDArchiveTelemetry`

**PatternScopeId:** `G.8:Ext.QDArchiveTelemetry`
**GPatternExtensionId:** `QDArchiveTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
**Uses:** `{C.18, G.5}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `EmitterPolicyRef`
* `InsertionPolicyRef`
* `CharacteristicSpaceRef.edition?` *(required iff cell boundaries / de‑dup / parity depend on the space definition)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring‑only):**
* Archive/illumination signals are telemetry; promotion into dominance is only via explicit `G.4` policy pins.

#### G.8:5.5 - `G.8:Ext.ExploreExploitTelemetry`

**PatternScopeId:** `G.8:Ext.ExploreExploitTelemetry`
**GPatternExtensionId:** `ExploreExploitTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.19`
**Uses:** `{C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExploreExploitBudgetPolicyId?`
* `ProbeAccountingId?`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring‑only):**
* When “probe/sandbox” is used, the controlling policy ids are pinned and recorded in the ledger/bundle trace.

#### G.8:5.6 - `G.8:Ext.OpenEndedWiring`

**PatternScopeId:** `G.8:Ext.OpenEndedWiring`
**GPatternExtensionId:** `OpenEndedWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.5` *(generator family registry surface; algorithm semantics remain external to Part‑G core)*
**Uses:** `{G.5}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GeneratorFamilyId`
* `TransferRulesRef.edition`
* `EnvironmentValidityRegionId?`
* `CouplerPolicyId?`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
**Notes (wiring‑only):**
* Open‑ended coverage/regret (or similar) remains telemetry unless explicitly promoted by a governing-pattern policy.


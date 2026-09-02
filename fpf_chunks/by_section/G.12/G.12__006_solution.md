---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline-Health Time Series and Views)"
section_id: "G.12:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__006_solution.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "G.12 — DHC Dashboards (Discipline-Health Time Series and Views)"
  - "G.12:4 — Solution"
line_start: 106856
line_end: 107004
dependencies:
  - "A.19"
  - "A.2.6"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.21"
  - "C.29"
  - "E.10"
  - "E.24.PUB"
  - "E.5.2"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.Core"
keywords:
  - "DHC"
  - "PathId/PathSliceId"
  - "RSCR/refresh wiring"
  - "UTS twins"
  - "admissible telemetry"
  - "dashboard"
  - "discipline health"
  - "edition pins"
  - "time-series"
  - "view-only slices"
---

### G.12:4 — Solution

#### G.12:4.0 — G.Core linkage

This pattern consumes G.Core obligations only for the branches actually opened.

**GCoreLinkageManifest (G.12)**

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`
  }.
* `RSCRTriggerSetIds` := {`GCoreTriggerSetId.BridgeCalibrationKit`} only when crossing or refresh wiring is used.
* `RSCRTriggerKindIds` := {`RSCRTriggerKindId.LegalitySurfaceEdit`} only when a persisted series or view depends on that surface. Optional panels add only their own declared trigger kinds.
* `DefaultsConsumed` := `∅`; portfolio defaults become current only through `G.12:Ext.PortfolioTelemetry`.
* `CorePinSetIds` := {`GCorePinSetId.PartG.AuthoringMinimal`, `GCorePinSetId.PartG.CrossingVisibilityPins`} with nil-elision.

The minimal durable series basis is `DHCSeriesRef.edition`, `DisciplineRef`, `IntendedUse`, `ClaimScopeRef`, exact coordinate-result refs, and their windows. Each coordinate resolves the complete `DHCReplayBasis` from C.21. `PathSliceId[]`, crossing pins, public-name rows, shipping pins, publication refs, and telemetry pins are conditional.

#### G.12:4.1 — Objects

| Local name | Exact object | Boundary |
| --- | --- | --- |
| `DHCCoordinateResultRef` | Ref to one persisted C.21/C.16 coordinate-result episteme and its active C.21 replay basis. | It is not a row, series, evidence path, or acceptance decision. |
| `DHCSeries` | One C.2.1 episteme whose EntityOfConcern is the discipline and whose ClaimGraph orders coordinate-result refs by explicit windows under one intended use, ClaimScope, and comparison basis. | It is not a public U-kind, publication occurrence, dashboard, carrier, or Work. |
| `DHCRow` | One representation element showing an exact coordinate-result ref and selected readable fields. | It does not compute, establish, or replace the result. |
| `DashboardSlice` | A C.29 view or grouping over exact row, result, or series refs. | It adds no comparison, normalization, acceptance, or selection semantics. |
| `DHCTelemetryPin` | A G.11-facing refresh payload with a canonical trigger, exact affected scope, and changed definition, window, evidence, or policy pins. | It is not evidence, currentness, an edition relation, or refresh Work. |
| dashboard publication | An E.24.PUB occurrence for one selected series or view edition, audience, bounded use, form, carrier, and availability interval. | A UTS row, rendering, upload, or release label does not make it obtain. |

Conceptual forms:

```text
DHCSeries := <
  DHCSeriesRef.edition,
  DisciplineRef,
  IntendedUse,
  ClaimScopeRef,
  ComparisonBasis,
  CoordinateResultRefs[],
  WindowOrder,
  DHCDefinitionSetRef.edition?,
  TargetSliceRef?,
  CurrentnessRuleRef?
>

DHCRow := <
  RowId,
  DHCCoordinateResultRef,
  Window,
  DisplayedValue,
  DisplayedScaleOrUnit,
  DisplayedStance?,
  DisplayAnnotations?
>

DashboardSlice := <
  DashboardSliceId,
  DHCSeriesRef.edition?,
  IncludedCoordinateResultRefs[],
  IncludedRowIds[],
  ViewSpecRef?,
  Annotations?
>
```

`TargetSliceRef` is present only when the series construction or publication consumes an A.2.6 selection. The ClaimGraph must then state how each selected slice belongs to or is covered by the authoritative `ClaimScope`. A changing time window is not silently encoded as “latest.”

#### G.12:4.2 — Method of obtaining the result

**Stage A — Select what the view is about**

1. **Start from exact results.** Select persisted C.21 coordinate-result refs for one already identified discipline. Do not compute from labels or restate Characteristic semantics in G.12.
2. **Fix use, scope, and windows.** Name IntendedUse and ClaimScope. Add a `TargetSliceRef` only when the computation or publication really consumes it, and state its relation to the scope.
3. **Check replay identity.** For every coordinate, resolve the C.21 `DHCReplayBasis`: Characteristic, Scale, Unit when current, `DHCMethodRef.edition`, exact Method and MethodDescription, model or calibration pins when used, time or population basis, and any distance or definition-set edition.
4. **Choose the comparison branch.** Directly comparable C.16 readings need no Bridge. Actual distinct-local-sense use cites the obtaining F.9 relation, direction, admitted use, and loss. Add reference-plane routing only when a real plane crossing is used; cite its exact basis, and keep any assurance consequence in R only.
5. **Open optional panels only when used.** Portfolio, QD, open-ended, maturity, SoTA, shipping, and advanced-view fields appear only through their extension blocks.

**Stage B — Construct or update content**

1. When new coordinates are required, separately identify the C.16 measurement Method, MethodDescription, model, calibration, dated Work, result, and result episteme. G.12 creates none of them from a row.
2. Assemble or revise the `DHCSeries` ClaimGraph from exact coordinate-result refs and windows. This assembly may be dated Work; the series episteme is its result, not the Work or work record.
3. Apply A.18 and any exact A.19/G.0 comparison, normalization, distance, or aggregation rule actually used. Nominal and ordinal values remain non-arithmetic unless an explicit lawful transformation creates another Scale.
4. Construct `DHCRow` and `DashboardSlice` representations. They may omit fields for readability only when every displayed claim still resolves its exact result and replay basis.

**Stage C — Publish or refresh only when required**

1. If public designators are needed, use F.18 for names of already constituted series or views. A name row is not publication.
2. If an audience must be able to obtain the selected edition, establish E.24.PUB with exact audience, bounded use, form, carrier, and interval.
3. If changed definitions, windows, evidence paths, crossing bases, or policies must trigger selective maintenance, emit G.11 telemetry pins naming the affected result or series slice. Otherwise stop without refresh wiring.

#### G.12:4.9 — Optional Extensions

> An extension adds only the panel-specific fields, pins, and triggers consumed by that view. It does not redefine C.21, C.16, comparison, evidence, publication, selection, or refresh semantics.

##### `G.12:Ext.SoTAPalette` — SoTA palette alignment

* `PatternScopeId`: `G.12:Ext.SoTAPalette`
* `GPatternExtensionKind`: `InteropSpecific`
* `GoverningPatternId`: `G.2`
* Optional pins: `SoTA_PackRef.edition?`, exact F.17 cell refs, and obtaining F.9 relation refs when alignment is actually displayed.
* No additional trigger kind by default.

##### `G.12:Ext.PortfolioTelemetry` — selector result panel

* `PatternScopeId`: `G.12:Ext.PortfolioTelemetry`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `G.5`
* Conditional values: `TaskSignatureRef?`, resolved `DominanceRegime`, resolved `PortfolioMode`, and exact selector result and basis refs.
* Set-returning semantics remain visible. A scalar headline is only a view annotation unless a separate policy lawfully constructs it.

##### `G.12:Ext.QDTelemetry` — illumination or archive panel

* `PatternScopeId`: `G.12:Ext.QDTelemetry`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.18`
* Conditional pins: `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `CharacteristicSpaceSpecRef.edition?`, `InsertionPolicyRef`, `EmitterPolicyRef?`, `ArchiveSnapshotRef?`, and `PathSliceId[]` when refresh uses them.
* Illumination and coverage stay telemetry unless a separate accepted policy promotes them.

##### `G.12:Ext.OpenEndedTelemetry` — open-ended or transfer panel

* `PatternScopeId`: `G.12:Ext.OpenEndedTelemetry`
* `GPatternExtensionKind`: `GeneratorSpecific`
* `GoverningPatternId`: `C.19`
* Conditional pins: `TransferRulesRef.edition`, `EnvironmentValidityRegionId?`, `ProbeBudgetPolicyId?`, and `PathSliceId[]`.
* Open-ended signals do not become dominance objectives by display.

##### `G.12:Ext.MaturityLadderPanel` — maturity view

* `PatternScopeId`: `G.12:Ext.MaturityLadderPanel`
* `GPatternExtensionKind`: `DisciplineSpecific`
* `GoverningPatternId`: `G.8`
* Conditional values: `MaturityCardRef`, `MaturityRungId?`, and evidence-path refs when the displayed rung relies on them.
* Adds `RSCRTriggerKindId.MaturityRungChange` only for a refresh-wired view.

##### `G.12:Ext.PackInclusion` — shipping stub

* `PatternScopeId`: `G.12:Ext.PackInclusion`
* `GPatternExtensionKind`: `InteropSpecific`
* `GoverningPatternId`: `G.10`
* Conditional values: exact pack ref, selected `DHCSeriesRef.edition` or `DashboardSliceRef`, and the replay or shipping pins the included claims actually require.
* G.10 governs shipping; this extension only identifies what is included.

##### `G.12:Ext.ViewFamilySeed` — advanced view seed

This non-normative seed reserves no semantics. An embedding, prediction, change-point, or drift panel needs its own selected governor, inputs, limitations, and policy before it can affect a claim or decision.


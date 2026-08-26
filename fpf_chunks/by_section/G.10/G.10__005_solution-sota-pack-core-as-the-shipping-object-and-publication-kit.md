---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:4"
section_title: "Solution — SoTA‑Pack(Core) as the shipping object and publication kit"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__005_solution-sota-pack-core-as-the-shipping-object-and-publication-kit.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:4 — Solution — SoTA‑Pack(Core) as the shipping object and publication kit"
line_start: 103432
line_end: 103714
dependencies:
  - "A.10"
  - "A.15.3"
  - "C.18"
  - "C.21"
  - "E.18"
  - "E.5.2"
  - "F.17-F.18"
  - "G.11"
  - "G.12"
  - "G.12-G.13"
  - "G.13"
  - "G.2"
  - "G.2-G.9"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "AuditPins"
  - "CrossingBundle"
  - "MOOManifest"
  - "PathId/PathSliceId"
  - "PortfolioRosterId"
  - "RSCR wiring"
  - "SoTA-Pack(Core)"
  - "UTS publication"
  - "edition pins"
  - "no semantic respecification"
  - "notation-independent pack"
  - "pack-boundary governing definition"
  - "parity pins"
  - "selector-ready publication surface"
  - "shipping"
  - "telemetry pins"
---

### G.10:4 - Solution — `SoTA‑Pack(Core)` as the shipping object and publication kit

`G.10` defines a **pack-governed** shipping surface: a notation‑independent object that **cites** all upstream artefacts by stable ids/refs and exposes the minimum pins required to (a) consume the result via selection, (b) audit it via path citations and crossing bundles, and (c) refresh it via typed RSCR triggers.

#### G.10:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; Default Governing Definition Index citation)

**GCoreLinkageManifest (G.10)** *(normative; expands per `G.Core:4.2`; `Nil‑elision` applies)*
Effective obligations/pins/triggers are computed as **union(expand(sets), explicit deltas)** under `Nil‑elision`.

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`
  }

* `RSCRTriggerSetIds` := { `GCoreTriggerSetId.RefreshOrchestration` }
  *(payload pins: `PackId(UTS)`, `publicationScopeId`, `CNSpecRef.edition`, `CGSpecRef.edition`, `PlanItemRefs := SlotFillingsPlanItemRef[]`, `AuditPins`, `UTSRowId[]`, `PathId/PathSliceId`, crossing policy pins, `TelemetryPinIds`, relevant upstream artefact ids)*

* `DefaultsConsumed` := {
  `DefaultId.PortfolioMode`,
  `DefaultId.DominanceRegime`,
  `DefaultId.GammaFoldForR_eff`
  }
  *(Governing definitions are resolved through `G.Core.DefaultGoverningDefinitionIndex` and are not restated here.)*

* `CorePinSetIds` := {
  `GCorePinSetId.PartG.AuthoringMinimal`,
  `GCorePinSetId.PartG.CrossingVisibilityPins`
  }

* `CorePinsRequired` *(pattern delta; pin names only; id‑valued unless noted)* := {
  `PackId(UTS)`,
  `publicationScopeId`,
  `contextSliceId?`,

  `PlanItemRefs := SlotFillingsPlanItemRef[]?` *(WorkPlanning planned baseline refs)*,
  `AuditPins` *(pack‑level pin bundle: edition pins (only on `…Ref.edition`), policy‑ids, UTS/Path pins; ids only)*,

  `UTSRowId[]`,
  `PathId[]?`, `PathSliceId[]?`,
  `CrossingBundleIds := CrossingBundleId[]?`,
  `TelemetryPinIds := TelemetryPinId[]?`,
  `PortfolioRosterId?`,

  `MOOManifestId?` *(method‑of‑obtaining‑output disclosure; conceptual object id)*
  }
  *(Optional pins from `CrossingVisibilityPins` MAY be strengthened to unconditional by listing them above; `G.10` typically strengthens `UTSRowId[]` and path/crossing bundles when the pack is publicly shipped.)*

* `TriggerAliasMapRef` := `∅` *(no local trigger tokens in Phase‑2)*

> **Mode‑specific definition pins.** Any additional pins required for QD/OEE/interop shipping are introduced only by `GPatternExtension` blocks in `G.10:4.6` (never smuggled into the core linkage).

#### G.10:4.2 - `SoTA‑Pack(Core)` object model (normative; notation‑independent)

`SoTA‑Pack(Core)` is a **shipment object** (a *pack*, not a kit and not a suite) that **cites** upstream artefacts and exposes pack‑level pins required for downstream use.

```
SoTA‑Pack(Core) :=
⟨
  PackId(UTS),
  publicationScopeId,
  contextSliceId?,
  CG-FrameContext,
  entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩,

  // Governing spec refs (refs + edition pins; semantics governed by their patterns)
  CNSpecRef := ⟨A.19 ref, CNSpecRef.edition⟩,
  CGSpecRef := ⟨G.0 ref,  CGSpecRef.edition⟩,

  // Selector-facing selection/parity roster token (conceptual; no formats mandated)
  PortfolioRosterId?,        // produced by `G.10‑1` as part of composition; may cite ε and the applicable pinned regime/mode refs

  // Cited payload packs/kits (ids only; semantics governed by the cited governing patterns)
  SoTAHarvestPackId?          // e.g., G.2 output id
  CHRPackId?                  // G.3 output id
  CALPackId?                  // G.4 output id
  EvidenceGraphId?            // G.6 output id
  BridgeMatrixId?             // G.2/G.7 cited id
  BridgeCalibrationTableId?   // G.7 output id
  SoSLOGBundleId?             // G.8 output id
  ParityReportId?             // G.9 output id
  DashboardSliceId?           // G.12 output id (optional)
  InteropSurfaceId?           // G.13 output id (optional)

  // Path citation surface (ids only; semantics governed by A.10/G.6)
  PathIds := PathId[]?,
  PathSliceIds := PathSliceId[]?,

  // Planned baseline + audit pins (P2W-aware; ids only)
  PlanItemRefs := SlotFillingsPlanItemRef[]?,
  AuditPins := { id pins… },                 // editions only on `…Ref.edition`; includes policies, UTS/Path pins, crossing pins

  // Crossing visibility surface (per GateCrossing; ids only)
  CrossingBundleIds := CrossingBundleId[]?,

  // Telemetry hooks for refresh planning (ids only; PathSlice-keyed; policy-id pinned)
  TelemetryPinIds := TelemetryPinId[]?,

  // Method-of-obtaining-output (MOO) disclosure (conceptual; ids only)
  MOOManifestId?,

  Notes?
⟩
```

#### G.10:4.2.1 - Portfolio roster (normative; pack-governed; governing-definition delegating)

`PortfolioRosterId` identifies the **selector‑facing** pack roster token. The corresponding `PortfolioRoster@Context` is one citation-and-binding roster record inside the shipped publication form, not a publication face kind, publication form kind, interop publication form kind, or carrier kind:
it MUST NOT redefine selection / selected-set semantics (governed by `G.5`) or parity semantics (governed by `G.9`).
Mode‑specific definition pins (QD/OEE/interop) are introduced only via `G.10:Ext.*` blocks.

```
PortfolioRoster@Context :=
⟨
  PortfolioRosterId,
  PackId(UTS),
  CG-FrameContext,
  entityOfConcern,

  // Selector operation and default-resolution support
  portfolioMode?,
  dominanceRegime?,
  ε?,

  // Published selector outcome and set-result declaration (metadata fields, not local semantics)
  selectorOutcomeKind?,
  setResultFamily?,
  handoffKind?,
  subjectKind?,
  sourceSetFamily?,
  derivedViewKind?,
  sourceSetComposition?,
  basePaletteRef?,
  lensId?,
  shortlistId?,
  promotionPolicyRef?,
  retentionIntent?,

  // Selector-facing roster + provenance hooks (ids only)
  MethodFamilyIds := MethodFamilyId[]?,
  GeneratorFamilyIds := GeneratorFamilyId[]?,
  ParityReportId?,
  SCRId[]?, DRRId[]?,

  // Pin reuse: prefer referencing the enclosing pack’s AuditPins bundle
  AuditPins?,
  Notes?
⟩
```

*Presence rule:* `PortfolioRosterId` MAY be omitted only when the shipped pack is *inputs‑only*
(e.g., shipping CHR/CAL/evidence without any selector‑consumable selected-set/shortlist output).

The `selectorOutcomeKind`, `setResultFamily`, `handoffKind`, `sourceSetFamily`, `sourceSetComposition`, `derivedViewKind`, `basePaletteRef`, `lensId`, and `shortlistId` fields in this roster are payload metadata fields or refs inside the shipped publication form. They do not define publication face kinds, publication form kinds, interop publication form kinds, or carrier kinds, and they do not let `G.10` re-govern `G.5`, `C.18`, `C.19`, or `G.2` semantics.

**Interpretation constraints (normative by delegation).** Any universal invariants governing (i) CN/CG spec-ref governing-definition assignment, (ii) crossing visibility and penalty routing, (iii) tri‑state guards, (iv) set‑return semantics, (v) P2W split, (vi) defaults, and (vii) RSCR trigger typing are **not restated here** and are enforced via `G.Core` conformance (see `CC‑G10‑CoreRef`).

#### G.10:4.3 - Shipping choreography (normative; governing-definition delegating)

`G.10` prescribes a minimal, governing-definition delegating sequence for composing a shipped pack:

1. **S‑1 — Gather & pin.** Collect upstream artefact ids and verify the **required pins** implied by the linkage manifest (edition pins, policy pins, UTS/Path pins).
2. **S‑2 — Compose `SoTA‑Pack(Core)` + MOO disclosure.** Assemble the pack object and attach a **`MOOManifest`** that lists the referenced mechanisms/policies/editions that produced the shipped outcomes (ids only; semantics stay with governing definitions).
3. **S‑3 — Publish selection/parity roster (selector‑facing).** Produce a selector‑readable `PortfolioRosterId` with the parity/definition pins required for reproducibility; do not mandate formats.
4. **S‑4 — Anchor and publish path citations.** Ensure A.10 anchors exist and publish/record `PathId/PathSliceId` citations required for downstream explainability (e.g., `C.23/H4`) and maturity rung changes.
5. **S‑5 — Expose CrossingBundle.** For each GateCrossing relevant to the shipped artefacts, expose the required `CrossingBundle` references (fail fast on missing or non‑conformant bundles when required).
6. **S‑6 — Emit telemetry pins for refresh planning.** Whenever illumination increases or archive/OEE pin state changes, emit PathSlice‑keyed telemetry with policy‑id and the active `…Ref.edition` pins (and QD `EmitterPolicyRef`/`InsertionPolicyRef` when applicable).
7. **S‑7 — Publish to UTS (twin labels).** Mint/refresh UTS Name Cards needed to cite the pack and shipped heads (Tech/Plain twins when required); cross‑Context identity travels only via Bridges with CL and loss notes.
8. **S‑8 — Optional: ingest interop surface.** If `G.13` interop is in use, ingest/cite `InteropSurface@Context` as annotation-only notes, pinning external index editions; do not redefine interop semantics.

#### G.10:4.4 - Interfaces & hooks (selector‑ and audit‑facing)

| ID         | Interface (conceptual)     | Consumes                                                          | Produces                                                |
| ---------- | -------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| **G.10‑1** | `Compose_SoTA_Pack`        | `G.*` outputs, ComparatorSet, Bridges, editions, SCR/DRR deltas     | `SoTA‑Pack(Core)` (UTS row + surfaces) + `AuditPins` (+ `MOOManifestId?`) (+ `PortfolioRosterId?`) |
| **G.10‑2** | `Publish_UTS`              | `PackId(UTS)`, `UTSRowId[]`, deprecation/edition‑bump notes       | UTS rows/Name Cards for the pack and shipped heads (incl. twins when required) |
| **G.10‑3** | `Expose_CrossingHooks`     | GateCrossings, lanes/planes/contexts                              | **CrossingBundle** (**E.18:CrossingBundle**) per GateCrossing; **fail** on missing/non‑conformant bundles |
| **G.10‑4** | `Pack_MOO`                 | referenced mechanism/policy/edition ids                           | `MOOManifestId` (ids only; governing-definition delegating) |
| **G.10‑5** | `Emit_TelemetryPins`       | Illumination/archive/OEE events                                   | PathSlice‑keyed telemetry: `policy‑id`, `…Ref.edition` (+ QD/OEE pins when applicable) |
| **G.10‑6** | `Publish_PathCitations`    | A.10 anchors, PathIds                                             | PathId/PathSlice citations for `C.23/H4` & rung changes |
| **G.10‑7** | `Ingest_InteropSurface?`   | (optional) `G.13 InteropSurface@Context`                          | Annotated pack notes citing external‑index editions     |

*Surfaces remain **conceptual** per **E.5.2**; RO‑Crate/ORKG/OpenAlex mappings belong to **Annex/Interop** and do not affect Core conformance.*

> **Note.** Any concrete serialisation/export is *not* part of this interface set. Serialisation belongs to interop/annex governing-definition assignment and must not become the governing definition.

#### G.10:4.5 - Consequence of governing-definition assignment (normative boundary statement)

`G.10` is the **one governing definition** of “shipping” in Part G *(by delegation to `CC‑GCORE‑SKP‑1`)*.
Other `G.x` patterns may produce artefacts that are shipped, but they must not embed shipping obligations; they cite `G.10` shipping surfaces instead.

#### G.10:4.6 - Extensions (pattern‑scoped; non‑core)

All method‑/generator‑/interop‑specific shipping extension declarations live here as `GPatternExtension` blocks.

##### GPatternExtension — `G.10:Ext.QDArchiveShippingPins`

**PatternScopeId:** `G.10:Ext.QDArchiveShippingPins`
**GPatternExtensionId:** `QDArchiveShippingPins`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
**Uses:** `{C.18, C.21, G.5, G.8, G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* active fields from C.21's DHC replay basis *(only when shipped archive telemetry consumes a C.21 DHC coordinate; carry exactly the fields used rather than a generic method-spec or metric-edition pin)*
* `EmitterPolicyRef` *(policy‑id / ref)*
* `InsertionPolicyRef` *(policy‑id / ref)*
* `CharacteristicSpaceRef` *(id/ref; iff archive partitioning is declared)*
* `CharacteristicSpaceRef.edition?` *(iff partitioning depends on an editioned space definition)*
* `PathSliceId[]` *(to bind telemetry/refresh scope when archive behaviour is present)*
**RSCRTriggerSetIds:** `∅` *(covered by `G.10` core linkage via `GCoreTriggerSetId.RefreshOrchestration`)*
**Notes (shipping-pin discipline):**
* This block never redefines archive semantics; it only states which pins must be present in the shipped pack when QD archive fields are present.

##### GPatternExtension — `G.10:Ext.OEEShippingPins`

**PatternScopeId:** `G.10:Ext.OEEShippingPins`
**GPatternExtensionId:** `OEEShippingPins`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.5`
**Uses:** `{G.5, G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `TransferRulesRef.edition`
* `EnvironmentValidityRegion?` *(id/ref; iff an explicit region is declared as part of generator-family support)*
* `PathSliceId[]` *(scope key for refreshable generator telemetry when present)*

**RSCRTriggerSetIds:** `∅` *(covered by the core trigger set)*
**Notes (shipping-pin discipline):**
* “Open‑endedness” semantics remain defined by the governing pattern; the pack only carries the pins required to make the shipped claim replayable/auditable.

##### GPatternExtension — `G.10:Ext.InteropCitation`

**PatternScopeId:** `G.10:Ext.InteropCitation`
**GPatternExtensionId:** `InteropCitation`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.13`
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `InteropSurfaceId`
* `ExternalIndexRef.edition`
* `ClaimMapperRef.edition`
* `PlaneMapRef.edition?`
* `MappingPolicyRef`

**RSCRTriggerSetIds:** `∅` *(covered by the core trigger set)*
**Notes (shipping-pin discipline):**
* This block only records that an interop surface contributed to the shipped pack’s provenance; it does not redefine any crosswalk semantics.

#### G.10:4.7 - Published surfaces must ship kind, source, derivation, lens, and shortlist token

- Published surfaces should carry the selector outcome kind and, when applicable, the set-result kind or handoff kind, plus the subject kind, source set kind, and relevant declared surface pins.
- These are publication payload metadata fields inside `SoTA-Pack(Core)`, not publication face kinds, publication form kinds, interop publication form kinds, or carrier kinds.
- Good publication fields include `selectorOutcomeKind`, `setResultFamily`, `handoffKind`, `subjectKind`, `sourceSetFamily`, `sourceSetComposition`, `dominanceRegime`, `lensId`, `shortlistId`, and any declared archive or promotion-policy ids that the reader needs to interpret the visible set.
- Those payload fields should use controlled tokens, cited ids, or already-declared head labels rather than shipping-local prose values.
- When the visible surface or the shortlisted source is one derived tradition view, also publish the derivation explicitly.
- Useful additional fields there include `derivedViewKind`, `basePaletteRef`, and the declared `qId` or reachability rule id that disciplined that derivation.
- `portfolioMode` may remain as one support field about selector operation, but it should not stand in for the public set label.
- A published surface should mirror semantics that are already declared in the governing palette, front, archive, or shortlist language.
- It should not redefine that semantics locally.
- When one shipped surface still needs a plain-language label, use the declared set-result kind and source set rather than falling back to `portfolioMode`.

#### G.10:4.7.1 - Worked publication slice

- If the visible surface is one tradition front under the declared `Q`, publish `selectorOutcomeKind=SetResultOutcome`, `setResultFamily=Front`, `sourceSetFamily=Front`, `derivedViewKind=TraditionFront`, and keep `basePaletteRef=SoTAPaletteDescriptionId` recoverable instead of pretending that the palette itself already was that front.
- If one shortlist is emitted from that derived tradition front, publish `selectorOutcomeKind=SetResultOutcome`, `setResultFamily=Shortlist`, `sourceSetFamily=Front`, `derivedViewKind=TraditionFront`, `basePaletteRef=SoTAPaletteDescriptionId`, and the named `lensId` together.
- If that same shortlisted surface is emitted as one stable public object, also publish `shortlistId=<...>` and keep it recoverable that the token names that shortlist rather than replacing it.
- If one retained tradition archive view is shown, publish `selectorOutcomeKind=SetResultOutcome`, `setResultFamily=Archive`, `sourceSetFamily=Archive`, `derivedViewKind=TraditionArchive`, and keep the same `basePaletteRef` recoverable.
- If the shortlist is later ordered, publish `setResultFamily=RankedShortlist` and keep the declared source set visible.
- Do not publish `setResultFamily=ChoiceSet` unless the shipped object is explicitly one mathematical analysis artifact rather than the public selected set.
- Do not publish `sourceSetFamily=TraditionPalette` alone when the visible object is already one derived tradition view; readers need to know which view is on the surface and which base palette it depends on.
- Do not publish `TraditionFront` or `TraditionArchive` as if they were the default meaning of `Tradition`.
- Do not ask `portfolioMode` to tell the reader whether they are seeing one palette, one front, one archive, or one shortlist.


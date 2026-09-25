---
chunk_kind: "child"
pattern_id: "G.2"
pattern_title: "Harvest and Synthesize SoTA for a CG-Frame"
section_id: "G.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.2/G.2__005_solution.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "G.2 — Harvest and Synthesize SoTA for a CG-Frame"
  - "G.2:4 — Solution"
line_start: 111614
line_end: 111923
dependencies:
  - "A.10"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "E.10"
  - "E.19"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.13"
  - "G.3-G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "BridgeMatrix"
  - "DeclaredSubstrateAtlasView"
  - "FlowRecord"
  - "GammaEpistSynthId"
  - "SoTA Synthesis Pack@CG-Frame"
  - "SoTA harvest"
  - "SoTAPaletteDescription"
  - "Tradition"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "palette-first"
  - "state of the art"
  - "synthesis"
---

### G.2:4 - Solution

#### G.2:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative).**
*(Canonical form, Nil‑elision, and Expansion rule are defined in `G.Core`.)*

```text
GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
  },
  RSCRTriggerSetIds := {GCoreTriggerSetId.SoTAHarvestSynthesis},
  CorePinSetIds := {GCorePinSetId.PartG.CrossingVisibilityPins}, // expands only for actual channel/receiving-use conditions under G.Core:4.2.3; no crossing means no crossing pins

  CorePinsRequired := {
    // Scope pins (G.2‑specific)
    CGFrameId, // identifies the exact CG-frame, which is the declared framing episteme; its cited ClaimGraph keeps source and edition, claim regions, EntityOfConcern, comparison basis, and intended use recoverable
    Tradition[],
    entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩,
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
    HarvestPolicyRef?, // required when a coverage judgement is made
    CoverageJudgementRef?, // the pack judgement, required for a relied-on coverage result
    DistanceDefRef.edition?,
    InclusionCriteriaId?,
    ScreeningRubricId?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := ∅
⟩
```

*(RSCR payload pins: `ClaimSheetId[]`, `SoTA_SetId`, `SoTAPaletteDescriptionId`, `BridgeMatrixId?`, `GammaEpistSynthId[]?`, `UTSRowId[]?`, `DistanceDefRef.edition?`, `HarvestPolicyRef?`, `InclusionCriteriaId?`, `ScreeningRubricId?`, `PathId/PathSliceId?` when path‑citable evidence or a stable freshness window is pinned.)*

**Pattern‑local default rules (governed by this pattern; not a Part‑G‑wide `DefaultId`).**

`FamilyCoverageFloorK := 3` *(unless explicitly overridden by `HarvestPolicyRef` and recorded in `FlowRecord`)*. This threshold supplies no counted population or same-family rule; those must be explicit before a coverage judgement. An undefined basis is unassessable, not a measured failure. Whenever coverage is judged, `HarvestPolicyRef` is required even when k uses this fallback; its applicability, receiving question, counted population/scope, grouping and same-family equivalence must be fixed before counting. An override changes k, not the unit or the independent pluralism duties.

**Counted-family basis.** The HarvestPolicy defines which candidates enter the counted population and when two entries represent the same family for this receiving question. Count equivalence classes under that rule. Repeated cards, aliases and source references for one family add zero. A combined method/generator population needs one receiving purpose and an overlap rule: a generator that is also a method is not counted twice unless the policy deliberately defines separate role-qualified units and justifies that interpretation. Freeze this basis before inspecting the count; changing it to turn a failure into three is not a repair of coverage.

The pack's coverage judgement carries the policy/edition, counted units, deduplication basis, count, k and pass/fail result, or the exact missing basis when unassessable. Give this existing pack component a local `CoverageJudgementRef` for citation. Evaluate lineage and materially distinct entry plurality separately. Cards and downstream consumers cite this same judgement instead of choosing their own unit. Compare counts across packs only when their bases match, or after an explicitly justified common-basis recount.

#### G.2:4.2 - Kit: `SoTA Synthesis Pack@CG‑Frame` (surface governed by this pattern)

A conforming `G.2` publication produces a **notation‑independent pack** whose internal organisation is free, but whose exported **named components and views** are stable and citable:

Each named component is addressable via a stable **pack‑local identifier** (e.g., `CorpusLedgerId`, `ClaimSheetId`, `FlowRecordId`) for citation and RSCR scoping. If any component is minted/evolved as a **public id**, it is published and cited via `UTSRowId[]` per `CC‑GCORE‑UTS‑1` (delegation).

0. **`SoTA_Set@CG‑Frame`** *(export view; “M2 output” consumed downstream)*
   A read‑optimised view over the harvested candidate set that downstream generator/selector work treats as the “harvester output set”.
   **Constraint (normative):** `SoTA_Set@CG‑Frame` **MUST** be reconstructible from pack components by id (no “hidden extra set”). Its coverage result cites the pack's `CoverageJudgementRef`, including its fixed HarvestPolicy basis; the export view does not redefine family membership.

1. **`G.2a CorpusLedger`**
   Ledger of candidate sources. Each row names the exact source and edition, claim region used, triage status (for example, include, park, or retire), evidence locator, and rationale for this CG-frame and receiving use.

2. **`G.2b ClaimSheets[Tradition]`**
   Typed Claim Sheets per `Tradition`, each with:

   * exact source and edition, claim region, effective ReferenceScheme where meaning matters, EntityOfConcern, and comparison basis for the stated use,
   * explicit evidence anchors/citations (A.10 and/or EvidenceGraph refs when available),
   * explicit freshness window notes and risk/trust cues *(cite `B.3` governing definitions when using trust/decay language)*.

3. **`G.2c OperatorAndObjectInventory`**
   Inventory of candidate CHR terms (characteristics/scales/coordinates) and candidate CAL operators/flows *as stubs* for downstream authoring.

4. **`G.2d BridgeMatrix`**
   A citable alignment/divergence surface across `Tradition`×`Tradition`, with explicit losses and row scopes.
   If any row asserts substitution or fusion across sources or across `Tradition` records, the pack **MUST** attach a `GammaEpistSynthId` record (alias: **`G.2‑F`**) per `G.2:Ext.GammaEpistSynthesis` (no silent fusion).

5. **`G.2e MicroExamples`**
   Worked micro-examples for load-bearing claims. Each names the exact source and edition, claim region, EntityOfConcern, comparison basis, and intended use; cites its evidence carrier or A.10 evidence-provenance path; and annotates applicable assurance types (`TA`, `VA`, or `LA`). The example card is only a publication form for those claims.

6. **`G.2f UTSProposals`**
   Draft Name Cards + Minimal Definitional Sheets (MDS) + alias proposals (incl. concept‑set linkage where applicable), with the required publication pins.

7. **`G.2g entityOfConcern Map`**
   Map from key terms/claims/public ids to `GroundingHolon`, `ReferencePlane`, and minimal reference cues for later CHR/CAL authoring.

8. **`G.2h PRISMA Flow Record`**
   A screening/eligibility trail for how sources entered the pack (method‑profile is allowed; see Extensions).
   *(Name is historical; the artefact remains notation‑independent.)* The pack coverage judgement and its policy basis are recoverable here, separately from the lineage and material-entry pluralism results.

9. **`G.2i SoSIndicatorFamilies`**
   Indicator *families* as variants (windows/constraints/assumptions) **with explicit Acceptance branches per variant** (branch ids/labels only; threshold semantics belong to CAL governing definitions).

10. **`G.2j MethodFamilyCards`**
    Candidate method families with a shared signature and a plurality of implementations, each with validity regions, cost/complexity notes, and known failure modes.
    When the pack targets downstream registry/dispatch, MethodFamily cards **SHOULD** include the declared refs and pins `G.5` needs (eligibility predicate refs, assurance profile cues, and the pack ids that justify the family).

11. **`G.2k GeneratorFamilyCards`** *(if applicable)*
    Candidate generator families for environment/task generation with declared validity regions and transfer hooks.

12. **`G.2l Annexes`** *(optional; governing-definition-cited; see Extensions)*
    For example: QD/NQD annexes, discipline‑specific indicator annexes, interop forms.

**SoTAPaletteDescription** *(export view; required downstream)*
A view‑friendly description object (pack‑local `SoTAPaletteDescriptionId`) that binds together:

* the `SoTA_Set@CG‑Frame` view,
* `ClaimSheetId[]`, `OperatorAndObjectInventory`, `BridgeMatrixId?`,
* `SoSIndicatorFamilies` (with variant/branch structure),
* `MethodFamilyCards` / `GeneratorFamilyCards?`,
* `MicroExamples`, `UTSProposals`,
* and the `entityOfConcern Map` for citation and later CHR/CAL authoring.

**Note (normative intent):** this is the primary “consumable surface” for `G.3/G.4/G.5`; it prevents downstream patterns from scraping free prose.

**Editorial template: 1‑page “SoTA Sheet” per Tradition (informative).**
When authoring `ClaimSheets[Tradition]`, teams often benefit from a single‑page template: scope + claims + evidence anchors + validity region + failure modes + freshness window + cross‑Tradition reuse notes + pointers to micro‑examples.

#### G.2:4.3 - Harvester loop (conceptual choreography; pattern-governed)

A conforming `G.2` pack publication is built by iterating the following conceptual loop until the declared gates are satisfied:

1. **Declare scope and plurality.**
   Identify the exact CG-frame (the declared framing episteme), the initial `Tradition` set, each intended claim region and EntityOfConcern, the comparison basis, and the receiving use. Record the cited CG-frame and source editions and evidence anchors in the pack pins rather than hiding them in a generic context field. Before counting, fix the HarvestPolicy's receiving question, counted population, grouping and same-family equivalence, including overlap handling for a combined population.

2. **Discover and triage sources (ledger‑first).**
   Populate `CorpusLedger` via:

   * adding seed sources,
   * expansion via citation chaining and keyword family exploration,
   * pruning using load‑bearing relevance tests tied to the declared CG‑Frame scope.

3. **Distill claims per `Tradition`.**
   For each `Tradition`, author a Claim Sheet that preserves internal commitments and cites evidence anchors. Do not fuse cross‑`Tradition` claims at this stage.

4. **Inventory operators/objects for downstream authoring.**
   Extract candidate measurement terms and operator stubs for later CHR/CAL authoring (without asserting legality or thresholds locally).

5. **Build alignment/divergence surfaces.**
   Where reuse across `Tradition` is desired, record the obtaining correspondence and its exact basis in `BridgeMatrix`: F.9 for sense correspondence, C.3.3 for kind correspondence, or the direct rule for a plane relation, as actually used. State preserved distinctions and losses for the receiving question. Consolidation requires explicit alignment proof. Add bundle or gate anchors only for an independently applicable E.18 flow crossing or A.21 gate, under `CC‑GCORE‑CROSS‑1`.

6. **(Alias: G.2‑F) Produce Γ_epist synthesis records when fusion/substitution is asserted.**
   If a `G.2` pack publication asserts fusion or substitution across sources or across `Tradition` records (beyond mere “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records per `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit object alignment refs + assurance tuple refs), and it **MUST** keep penalties routed to `R_eff` only by delegation (`CC‑GCORE‑PEN‑1`).

7. **Publish teachable micro‑groundings.**
   Attach worked micro-examples to load-bearing claims, each tied to the exact source and edition, claim region, EntityOfConcern, comparison basis, intended use, and evidence carrier or A.10 evidence-provenance path.

8. **Apply gates and record repairs.**
   Apply that fixed HarvestPolicy basis and count its distinct units before comparing coverage with `FamilyCoverageFloorK` (and apply any optional diversity-by-distance gate under its own basis). Missing count semantics returns an unassessable result and the exact missing basis, not an instruction to search more. If a defined gate fails, the pack **MUST**:
   * record the failure and the repair iteration in `FlowRecord` and `CorpusLedger`,
   * pin the updated `HarvestPolicyRef` / criteria ids (if changed),
   * iterate the loop rather than silently weakening the gate.

9. **Emit hand‑off manifests and export views.**
   Produce explicit manifests to:

   * `G.3` (CHR authoring),
   * `G.4` (CAL authoring),
   * `G.5` (registry/dispatch),

   so that downstream work can cite pack components by id rather than re‑authoring them. Each relied-on coverage result carries the same `CoverageJudgementRef` and its policy basis; a downstream method-selection use cannot treat a combined method/generator count as a method-only count.
   The pack **MUST** also export `SoTA_Set@CG‑Frame` and `SoTAPaletteDescription` as the default downstream consumption surfaces (ids pinned).

#### G.2:4.4 - Interfaces (minimal I/O Standard)

| Interface         | Consumes                                                      | Produces                                                                    |
| ----------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **G.2-1 Harvest** | exact CG-frame (the declared framing episteme) identified by `CGFrameId`, initial `Tradition[]`, source edition and claim-region boundary, EntityOfConcern, comparison basis, receiving use, `HarvestPolicyRef` whenever coverage is judged | `SoTA Synthesis Pack@CG-Frame` (G.2a-G.2l) |
| **G.2‑2 Extend**  | existing Pack + new sources/anchors + updated policy pins     | updated Pack + RSCR‑relevant trigger emissions (canonical kinds)            |
| **G.2‑3 HandOff** | Pack                                                          | `CHR‑handoff` (to G.3), `CAL‑handoff` (to G.4), `Registry‑handoff` (to G.5) |

*Note:* Orchestration of re‑runs is governed by `G.11`; this pattern only defines what a conforming (re)harvest produces and what pins it must expose.

#### G.2:4.5 - Extensions (pattern‑scoped; non‑core)

`Extensions` are pattern‑scoped annexes. They do not introduce Part‑G‑wide norms; they declare the additional pins required when those semantics are active and cite the corresponding governing patterns.

###### G.2:4.5.1 - GPatternExtension: GammaEpistSynthesis

**PatternScopeId:** `G.2:Ext.GammaEpistSynthesis`
**GPatternExtensionId:** `GammaEpistSynthesis`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.2`
**Uses:** `{G.Core, B.3, F.9, G.6}` *(penalty routing + trust/decay cues + bridges/CL + evidence path citation when used)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GammaEpistSynthId[]` *(pack‑local ids of synthesis records; emitted iff fusion/substitution is asserted)*
* `EvidenceAnchorRef[]` *(provenance union; evidence carriers cited by A.10 evidence-provenance paths)*
* `BridgeMatrixId` and `BridgeCardId[]` *(explicit object alignment references when crossing is involved)*
* `CL/CL^plane` and `Φ/Ψ/Φ_plane policy-ids` when required by the cited crossing or actually used loss model *(semantics and penalties → `R_eff` remain governed by the cited definitions)*
* `PathId/PathSliceId?` *(only when citing via `G.6`)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`

**Notes (normative intent; duplication‑avoidant):**
* The auditable synthesis record identified by `GammaEpistSynthId` binds: (i) provenance union, (ii) explicit object alignment refs, (iii) assurance tuple refs (via their governing definitions) for each asserted fusion/substitution. A B.1.3 `Γ_epist^synth` application and its returned episteme remain separate from this record.
* This extension cites the `Γ‑fold`, `Φ`, and penalty rules through `G.Core` and exposes the pins needed for replay. When B.3/C.2.2 supplies no justified common numerical score or loss calculation, retain the separate support, actual mapping limitations and bounded assurance conclusion; a synthesis record does not supply the missing model.

###### G.2:4.5.2 - GPatternExtension: HarvestProtocols

**PatternScopeId:** `G.2:Ext.HarvestProtocols`
**GPatternExtensionId:** `HarvestProtocols`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `G.2`
**Uses:** `{B.3, A.10}` *(for freshness/decay and provenance anchors, when protocol requires them explicitly)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `HarvestPolicyRef` *(declares the chosen protocol family and its parameters)*
* `FlowRecordId` *(protocol‑specific profile id or rubric id may be attached here)*
* `InclusionCriteriaId` / `ScreeningRubricId` *(ids only; semantics remain local to the protocol family)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (extension discipline):**
* This extension binds a declared protocol profile to the pack’s `FlowRecord` without redefining evidence semantics.

###### G.2:4.5.3 - GPatternExtension: DHCAlignmentHooks

**PatternScopeId:** `G.2:Ext.DHCAlignmentHooks`
**GPatternExtensionId:** `DHCAlignmentHooks`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `C.21` *(DHC semantics are governed by C.21)*
**Uses:** `{C.21, G.6, G.7}` *(DHC series + evidence path citations + bridge/CL regimes when alignment density is claimed)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DHCMethodRef.edition`
* `WindowRef?` *(if the DHC series is windowed)*
* exact F.17 `SchemeSenseCell` refs used by the DHC comparison set (use `SenseCellAddressRef` where a durable address is needed; cite `UTSRowId[]` only for independently public ids)
* `UTSRowId[]?` *(only if a cited cell or series id is independently minted or evolved as a public id)*
* `PathId[]` / `PathSliceId[]` *(when alignment summaries cite evidence paths via G.6)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TelemetryDelta}`

**Notes (extension discipline):**
* If DHC alignment summaries are emitted, this extension ensures the DHC method edition and the cited evidence paths are visible.
* AlignmentDensity uses C.21's Unit `obtaining_relations/100_compared_cells`: fix the exact compared F.17 cell set and count the exact obtaining directed F.9 relations, retaining each relation's orientation and admitted-use qualifier. Keep observed loss in its evidence account. A CL calibration label does not include or exclude a relation by itself. Any independently justified receiving-use filter must name its own policy and resulting population; it is not a C.21 CL threshold.
* For example, three obtaining directed relations in a fixed set of 100 compared cells give a density of 3 in that Unit. Changing a CL label while relation truth, population and admitted-use qualifier remain fixed leaves the density 3. A fourth calibration row labelled CL=2 with no obtaining relation adds nothing. If a use condition actually changes which relations qualify, restate that changed population before comparing densities.

###### G.2:4.5.4 - GPatternExtension: NQDAnnex

**PatternScopeId:** `G.2:Ext.NQDAnnex`
**GPatternExtensionId:** `NQDAnnex`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18` *(NQD-CAL semantics are governed by C.18; explore/exploit logging is governed by C.19 when used)*
**Uses:** `{C.18, C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `InsertionPolicyRef` *(policy‑id/ref)*
* `EmitterPolicyRef` *(policy‑id/ref)*
* `TaskSignatureRef?` *(when QD mode is trait‑gated)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (extension discipline):**
* This extension only pins the required references for replayability; it does not redefine QD semantics, dominance, or acceptance rules.

###### G.2:4.5.5 - GPatternExtension: InteropForms

**PatternScopeId:** `G.2:Ext.InteropForms`
**GPatternExtensionId:** `InteropForms`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.13`
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExternalIndexRef.edition`
* `ClaimMapperRef.edition`
* `MappingPolicyRef` *(policy‑id/ref)*
* `UTSRowId[]` *(for published external ids/aliases where relevant)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`

**Notes (extension discipline):**
* Interop affects only representation and citation routes; it must not introduce alternate legality gates or acceptance semantics.

#### G.2:4.6 - Palette first

- `SoTAPaletteDescription` is one plurality-preserving palette.
- It is not by itself one `Front`, one `Archive`, or one `Shortlist`.
- When that palette's members are traditions, `TraditionPalette` is the reader-facing tradition-only palette head over the same palette declaration, not one second governing definition. For methods, hypotheses, or other members, keep `SoTAPaletteDescription` or `Palette + SubjectKind` explicit instead.
- Traditions remain in the palette until a later surface declares comparison, retention, or choice semantics explicitly.
- `TraditionFront` is one derived view over the declared palette under one declared `Q`; the `Q` basis stays pinned separately and the view does not rename `Tradition` or `SoTAPaletteDescription`.
- `TraditionArchive` is one derived retention view over that same palette under one declared reachability or coverage rule; that rule stays pinned separately and the view does not turn the palette into one archive by default.
- When one derived tradition view is shown, keep the base palette recoverable at the same time.
- When comparison or retention needs richer geometry or atlas language, treat that as support for the derivation rather than as the default meaning of the palette.
- A reader should be able to say both `this is the palette` and `this is the derived tradition view currently being shown` without collapsing those two objects.

#### G.2:4.7 - Optional atlas interpretation of a declared palette

Use `TraditionAtlasView` only when the reader needs several derived views or interpretive qualifiers together to understand a grouping, omission risk or comparison boundary. Otherwise use the palette and its declared front, archive or shortlist, or the thinner `DeclaredSubstrateInterpretiveView`. A naming-only question belongs to F.18.

`TraditionAtlasView` specializes `DeclaredSubstrateAtlasView` under A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW and retains that declaration by value: the base palette, active source set or result, `TypedSetViews` when several declared views are combined, the space/map references and interpretive qualifiers actually used, and the reason the thinner view is insufficient. Cite `SearchSpaceRef` or `OutcomeSpaceRef` for the corresponding declared spaces. Add `SpaceMetricRef`, `TransitionRelationRef` and `BridgeDistortionNote` only for the comparison, reachability, transition or cross-scale claim that needs them. An `OutcomeMapRef` identifies a mapping from the stated result into an outcome/effect space; it does not turn the palette or result into that space. Their formal claims retain their own governing definitions.

If the interpretation changes the base source-to-outcome relation or its distortion, reopen the substrate declaration. Different atlas views may use different spaces, metrics, relations or mathematical traditions; one view does not settle those choices for every other view.


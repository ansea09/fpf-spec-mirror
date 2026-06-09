---
chunk_kind: "child"
pattern_id: "G.2"
pattern_title: "SoTA Harvester & Synthesis"
section_id: "G.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/G.2/G.2__005_solution.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "G.2 — SoTA Harvester & Synthesis"
  - "G.2:4 — Solution"
line_start: 77305
line_end: 77615
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
  - "synthesis"
---

### G.2:4 - Solution

#### G.2:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

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
    HarvestPolicyRef?,
    DistanceDefRef.edition?,
    InclusionCriteriaId?,
    ScreeningRubricId?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := ∅
⟩`

*(RSCR payload pins: `ClaimSheetId[]`, `SoTA_SetId`, `SoTAPaletteDescriptionId`, `BridgeMatrixId?`, `GammaEpistSynthId[]?`, `UTSRowId[]?`, `DistanceDefRef.edition?`, `HarvestPolicyRef?`, `InclusionCriteriaId?`, `ScreeningRubricId?`, `PathId/PathSliceId?` when path‑citable evidence or a stable freshness window is pinned.)*

**Pattern‑local default rules (governed by this pattern; not a Part‑G‑wide `DefaultId`).**

`FamilyCoverageFloorK := 3` *(unless explicitly overridden by `HarvestPolicyRef` and recorded in `FlowRecord`)*

#### G.2:4.2 - Kit: `SoTA Synthesis Pack@CG‑Frame` (surface governed by this pattern)

A conforming `G.2` publication produces a **notation‑independent pack** whose internal organisation is free, but whose exported **named components and views** are stable and citable:

Each named component is addressable via a stable **pack‑local identifier** (e.g., `CorpusLedgerId`, `ClaimSheetId`, `FlowRecordId`) for citation and RSCR scoping. If any component is minted/evolved as a **public id**, it is published and cited via `UTSRowId[]` per `CC‑GCORE‑UTS‑1` (delegation).

0. **`SoTA_Set@CG‑Frame`** *(export view; “M2 output” consumed downstream)*
   A read‑optimised view over the harvested candidate set that downstream generator/selector work treats as the “harvester output set”.
   **Constraint (normative):** `SoTA_Set@CG‑Frame` **MUST** be reconstructible from pack components by id (no “hidden extra set”).

1. **`G.2a CorpusLedger`**
   Ledger of candidate sources with Context and triage status (e.g., include / park / retire) and explicit rationale hooks.

2. **`G.2b ClaimSheets[Tradition]`**
   Typed Claim Sheets per `Tradition`, each with:

* explicit `U.BoundedContext` and `entityOfConcern`,
* explicit evidence anchors/citations (A.10 and/or EvidenceGraph refs when available),
* explicit freshness window notes and risk/trust cues *(cite `B.3` governing definitions when using trust/decay language)*.

3. **`G.2c OperatorAndObjectInventory`**
   Inventory of candidate CHR terms (characteristics/scales/coordinates) and candidate CAL operators/flows *as stubs* for downstream authoring.

4. **`G.2d BridgeMatrix`**
   A citable alignment/divergence surface across `Tradition`×`Tradition`, with explicit losses and row scopes.
   If any row asserts substitution or fusion across sources or across `Tradition` records, the pack **MUST** attach a `GammaEpistSynthId` record (alias: **`G.2‑F`**) per `G.2:Ext.GammaEpistSynthesis` (no silent fusion).

5. **`G.2e MicroExamples`**
   Worked micro‑examples for load‑bearing claims, each citing A.10 carriers, declaring context + `entityOfConcern`, and annotating assurance type(s) (`TA`/`VA`/`LA`, where applicable).

6. **`G.2f UTSProposals`**
   Draft Name Cards + Minimal Definitional Sheets (MDS) + alias proposals (incl. concept‑set linkage where applicable), with the required publication pins.

7. **`G.2g entityOfConcern Map`**
   Map from key terms/claims/public ids to `GroundingHolon`, `ReferencePlane`, and minimal reference cues for later CHR/CAL authoring.

8. **`G.2h PRISMA Flow Record`**
   A screening/eligibility trail for how sources entered the pack (method‑profile is allowed; see Extensions).
   *(Name is historical; the artefact remains notation‑independent.)*

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
   Declare `CG-FrameContext`, the initial `Tradition` set, and the `entityOfConcern` surface for each intended claim region. Record these declarations in the pack pins (not as implicit assumptions).

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
   If a `G.2` pack publication asserts fusion or substitution across sources or across `Tradition` records (beyond mere “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records per `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit object alignment refs + assurance tuple refs), and it **MUST** keep penalties routed to `R_eff` only by delegation (`CC‑GCORE‑PEN‑1`).

7. **Publish teachable micro‑groundings.**
   Attach worked micro‑examples to load‑bearing claims, each tied to A.10 carriers and declaring context + `entityOfConcern`.

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
* `EvidenceAnchorRef[]` *(provenance union; A.10 carriers)*
* `BridgeMatrixId` and `BridgeCardId[]` *(explicit object alignment references when crossing is involved)*
* `CL/CL^plane` + `Φ/Ψ/Φ_plane policy-ids` *(ids only; semantics governed by cited definitions; penalties → `R_eff` only by delegation)*
* `PathId/PathSliceId?` *(only when citing via `G.6`)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`

**Notes (normative intent; duplication‑avoidant):**
* `Γ_epist^synth` is an auditable record that binds: (i) provenance union, (ii) explicit object alignment refs, (iii) assurance tuple refs (via existing governing definitions) for each asserted fusion/substitution.
* This extension **does not** redefine `Γ‑fold`, `Φ`, or penalty semantics; it only requires the pins/refs needed for replayability and auditability (see `G.Core` delegations).

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
* `DHCSenseCellId[]` *(pack‑local ids for emitted DHC SenseCells; if any are public, cite via `UTSRowId[]`)*
* `UTSRowId[]?` *(only if any DHC SenseCells / series ids are minted/evolved as public ids)*
* `PathId[]` / `PathSliceId[]` *(when alignment summaries cite evidence paths via G.6)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TelemetryDelta}`

**Notes (extension discipline):**
* If DHC alignment summaries are emitted, this extension ensures the DHC method edition and the cited evidence paths are visible.
* Units/constraints (governing pattern: `C.21`) must be **pinned, not redefined** here (e.g., `bridges_per_100_DHC_SenseCells`, `CL_min = 2` for cross‑Context counting, and the “CL=3 implies free substitution” interpretation when used).

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

#### G.2:4.7 - Atlas views stay optional neighboring interpretation over one declared palette and declared set results

- `TraditionAtlasView` is one declared optional neighboring interpretive view over one palette and any declared front, archive, or shortlist surfaces drawn from it, while the cited substrate-bearing line, the active source set or active set result, and any cited `SearchSpaceRef`, `OutcomeSpaceRef`, or other declared space refs remain recoverable.
- `TraditionAtlasView` is the `G.2` use-site specialization of `DeclaredSubstrateAtlasView`; keep the generic interpretive-view declaration in `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW`.
- It is not the default meaning of `Tradition` or `SoTAPaletteDescription`.
- Stay palette-first when the harvest or synthesis question can already be judged from the declared palette together with ordinary front, archive, or shortlist surfaces.
- Use `TraditionAtlasView` only when the reader must hold several declared derived views or interpretive qualifiers together to see why one tradition grouping, omission risk, or comparison boundary matters.
- A conforming `TraditionAtlasView` must keep the same atlas-form interpretation declaration that `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` requires by value: recoverable base palette, active source set or active set result, `TypedSetViews` when several declared set views are held together, cited `SearchSpaceRef`, `OutcomeSpaceRef`, or other declared space refs, cited declared map refs such as `OutcomeMapRef`, cited qualifiers such as `SpaceMetricRef`, `TransitionRelationRef`, and `BridgeDistortionNote`, and one explicit reason why thinner `DeclaredSubstrateInterpretiveView` is insufficient here.
- It may help explain where one tradition, method family, or retained line sits relative to another, but it should not silently redefine the base palette or one derived front view or archive view.
- If one atlas view uses several typed views over the same source set, keep the active set result, any cited `SearchSpaceRef`, `OutcomeSpaceRef`, or other declared space ref, and any `BridgeDistortionNote` recoverable instead of letting `TraditionAtlasView` hide those choices.
- Treat the atlas layer as optional neighboring interpretation, not as ordinary palette-first core. Use `SpaceMetricRef` or `TransitionRelationRef` only when one declared comparison, reachability, transition, or cross-scale state-change claim actually depends on that formal support; otherwise leave them unstated.
- Use `OutcomeMapRef` only when the atlas must show how one declared set result maps into one outcome-side or effect-side declared space/ref; it does not turn the palette, front, archive, or shortlist into that outcome-side declared space/ref.
- If one atlas reading would materially change the base source-to-outcome relation or distortion posture, reopen the substrate declaration instead of treating that change as one local `G.2` convenience.
- If one thinner `DeclaredSubstrateInterpretiveView` already keeps the question legible, prefer that thinner interpretation form and leave atlas specialization unused.
- `SearchSpaceRef` and `OutcomeSpaceRef` doctrine, transition-aware novelty, metric-transfer loss, and cross-scale geometry belong to a heavier formal layer: keep them outside ordinary palette-first use unless the current comparison, reachability, transition, or multilevel claim explicitly needs them, and do not pull them in merely because one richer comparative reading is mathematically available.
- If no declared atlas view is needed, stay with the simpler palette-first and declared-derived-view surfaces.
- Different atlas views may rely on different declared spaces, metrics, bridges, or transition supports; keep that plurality visible rather than forcing one geometry monoculture across every neighboring view.
- If several mathematical traditions remain plausible, keep that plurality visible rather than pretending the atlas already fixes one final formalism.
- If the question is naming-side only, use `F.18` for that wording choice rather than letting atlas-form interpretation language carry the naming decision by itself.


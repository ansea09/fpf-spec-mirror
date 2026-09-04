---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:4"
section_title: "Solution — Conceptual interop kit: registered sources, alignment cards, feature derivations, and RSCR‑wired telemetry"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__005_solution-conceptual-interop-kit-registered-sources-alignment-cards-feature-derivations-and-rscr-wired-telemetry.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:4 — Solution — Conceptual interop kit: registered sources, alignment cards, feature derivations, and RSCR‑wired telemetry"
line_start: 107108
line_end: 107233
dependencies:
  - "A.18"
  - "A.19"
  - "E.10"
  - "E.18"
  - "E.5.2"
  - "F.17"
  - "G.0"
  - "G.12"
  - "G.13"
  - "G.2"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CHR-typed SoS features"
  - "ClaimMapperCard@Context"
  - "ExternalIndexCard@Context"
  - "InteropSurface@Context"
  - "RSCRTriggerKindId"
  - "UTS twins"
  - "claim mapper"
  - "edition pins"
  - "embedding spec"
  - "external index"
  - "interop"
  - "mapping policy"
  - "plane map"
  - "telemetry pin"
---

### G.13:4 - Solution — Conceptual interop kit: registered sources, alignment cards, feature derivations, and RSCR‑wired telemetry

#### G.13:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core`.

**GCoreLinkageManifest (normative).**
*(Canonical form, Nil‑elision, and Expansion rule are defined in `G.Core`.)*

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
    GCoreConformanceProfileId.PartG.ShippingBoundary
  },
  RSCRTriggerSetIds := {GCoreTriggerSetId.SoTAHarvestSynthesis},
  RSCRTriggerKindIds := {RSCRTriggerKindId.BaselineBindingEdit},   // delta: planned‑baseline linkage edits can be interop‑relevant

  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },

  CorePinsRequired := {
    // Interop pins (G.13‑specific; avoid duplicating `GCorePinSetId.PartG.CrossingVisibilityPins`)
    ExternalIndexRef.edition,
    ClaimMapperRef.edition?,
    MappingPolicyRef?,
    PlaneMapRef.edition?,
    ScaleEmbeddingSpecRef.edition?,

    EvidenceGraphId?,
    InteropSurfaceId?
  },

  DefaultsConsumed := {DefaultId.PortfolioMode, DefaultId.DominanceRegime}
⟩`

**Payload‑pin note (informative).** When emitting RSCR triggers for interop‑driven changes, payload pins should include the edited edition/policy identifiers, the impacted scope, and the applicable crossing‑visibility pins (per `GCorePinSetId.PartG.CrossingVisibilityPins`) when crossings/UTS/paths are involved.

#### G.13:4.2 - Interop kit objects & surfaces (pattern-governed; notation‑independent)

All objects below are **conceptual**. Any concrete serialisation belongs to Annex/Interop or tooling notes and is not normative for Part‑G conformance.

* **`ExternalIndexCard@Context`** — registration of an external source and its snapshot.

  **Shape (conceptual):**
  `⟨ ExternalIndexId, ProviderName?, ExternalIndexType, CoverageScope, Licence?, ExternalEdition, FreshnessWindow?, entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩, Notes? ⟩`

  **Intent.** Create a stable, citable “source card” so downstream artefacts can pin the *card edition* via `ExternalIndexRef.edition`, while the provider snapshot remains visible as `ExternalEdition` (do not echo provider snapshot ids into downstream cards; cite refs instead).

* **`ClaimMapperCard@Context`** — a conceptual “mapping recipe” that yields FPF‑native artefacts from an external source.

  **Shape (conceptual):**
  `⟨ MapperId, ExternalIndexId, MappingPolicyRef, Targets{ClaimSheet|BridgeHints|SoSFeatureSet|UTSProposals}, PlaneMapRef?, ScaleEmbeddingSpecRef?, EvidenceGraphId?, CSLCProofStubs? ⟩`

  **Notes.**

  * This is **not** a shadow legality gate. It is an interop surface that **cites** governing definitions (`A.19`, `G.0`, `G.3`, `G.4`) and publishes the required pins for downstream audit/refresh.
  * When cross‑plane or cross‑context reuse is implicated, the alignment outputs must use the existing crossing bundles (see `G.Core` linkage).
  * Avoid “edition echo”: downstream artefacts cite `ExternalIndexRef.edition` and `ClaimMapperRef.edition` (and optional `PlaneMapRef.edition` / `ScaleEmbeddingSpecRef.edition`) rather than copying snapshot ids/editions as free fields.

* **`SoSFeatureTransform@Context`** — declares how external signals become **CHR‑typed** SoS features (for DHC/dashboard usage and/or SoS‑LOG rule evaluation).

  **Shape (conceptual):**
  `⟨ SoSFeatureTransformId, Inputs{ClaimSheetId[] | ExternalSignalsRef}, SoSFeatureSetId, FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}, ReferencePlane, EvidenceGraphId?, PathSliceId[]?, ProofHooks? ⟩`

  **Notes.**

  * The derivation is a **typing + provenance** surface; it does not introduce new comparators or new governance cards or legality gates.

* **`ScaleEmbeddingSpec@Context`** — optional constraints for representation/space alignment used inside an alignment recipe.

  **Shape (conceptual):**
  `⟨ ScaleEmbeddingSpecId, IntendedUse, AllowedTransformFamily, RequiredPins{NormalizationMethodRef.edition?}, ProhibitedCoercions ⟩`

  **Design intent.** Make any representation alignment *explicitly constrained* and edition‑pinned, instead of silently “creating a new scale”.
  **LEX/UTS note (informative).** `ScaleEmbeddingSpec` is a new LEX head; when it mints a public id it must be published to UTS with twin labels (see `G.Core` / UTS profile).

* **`IndexTelemetryPin`** — an emitted refresh input that makes interop changes RSCR‑visible.

  **Shape (conceptual; RSCR‑typed):**
  `⟨ triggerKindId: RSCRTriggerKindId, scope: PathSliceId[] | PathId[] | PatternScopeId, payloadPins{ExternalIndexId, ExternalIndexRef.edition, ClaimMapperRef.edition?, MappingPolicyRef?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, PathId[]?, PathSliceId[]?, UTSRowId[]?, …} ⟩`

  **Publication.** Emitted to `G.11` as refresh input; recorded with canonical `RSCRTriggerKindId` causes.

* **`InteropSurface@Context`** — a selector-facing or dashboard-facing summary of what interop publications and records exist and how they are pinned.

  **Shape (conceptual):**
  `⟨ InteropSurfaceId, ExternalIndexId, ExternalIndexRef.edition, MapperId?, ClaimMapperRef.edition?, MappingPolicyRef?, SoSFeatureSetId?, EvidenceGraphId?, PathSliceId[]?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, UTSRowId[] ⟩`

  **Publication.** Published to UTS with twin labels as applicable.

#### G.13:4.3 - Generation‑first interop flow (notation‑independent; governing-definition delegating)

1. **Register source editions.** Author `ExternalIndexCard@Context` for each external source/snapshot used for SoTA authoring, including `ExternalEdition` and the `entityOfConcern` plane anchor.
2. **Author mapping recipes.** Create `ClaimMapperCard@Context` describing which FPF artefacts are produced (ClaimSheets, BridgeHints, feature sets, UTS proposals), and which policies/specs constrain the mapping (policy refs + optional `PlaneMapRef` / `ScaleEmbeddingSpecRef`).
3. **Produce FPF‑native inputs.** Use the alignment recipe outputs as inputs to:

   * `G.2` harvesting (ClaimSheets / operator & object inventories / candidate bridge hints),
   * `G.3` CHR typing (when numeric signals are formalized as CHR characteristics/scales/coordinates),
   * `G.4` acceptance/threshold policies (when a downstream decision requires explicit CAL policy rather than telemetry),
   * `G.12` dashboards (when derived SoS features are used as DHC slots).
4. **Feed selection/parity/shipping without smuggling semantics.**

   * `G.5` consumes the produced artefacts under its own governing spec refs and returns set‑valued outcomes (selector semantics remain governed by `G.5` + `G.Core`).
   * `G.9` parity consumes pinned editions/windows and produces traceable parity reports.
   * `G.10` shipping may include interop surfaces **as cited publications or records**; `G.13` does not govern shipping.
5. **Emit telemetry and refresh causes.** Any change in external editions, alignment policies, plane maps, or embedding specs emits:

   * a canonical `RSCRTriggerKindId` (per `G.Core`),
   * a scope (`PathSliceId[]` and/or `PatternScopeId`),
   * payload pins (editions/policies/UTS rows),
     enabling `G.11` to plan slice‑scoped refresh.

#### G.13:4.4 - Interfaces — minimal I/O standard (conceptual; kit‑only)

| ID   | Interface   | Consumes  | Produces   |
| ---- | ----------- | --------- | ---------- |
| **G.13‑1 `Register_ExternalIndex`**  | Register `ExternalIndexCard@Context` | Provider metadata, scope, **ExternalEdition**, freshness, entityOfConcern anchor   | `ExternalIndexCard@Context` (+ UTS row when published)   |
| **G.13‑2 `Map_ClaimsToFPF`**   | Apply `ClaimMapperCard@Context`   | `ExternalIndexCard@Context`, `MappingPolicyRef`, optional `PlaneMapRef`/`ScaleEmbeddingSpecRef`, optional EvidenceGraph hooks | `ClaimSheet@Context`, `BridgeHints`, optional `SoSFeatureSet@Context`, optional UTS proposals |
| **G.13‑3 `Derive_SoSFeatures`**  | Produce CHR‑typed SoS features  | ClaimSheets / external signals refs, CHR typing refs, legality proof hooks | `SoSFeatureSet@Context` (CHR‑typed; provenance pinned)   |
| **G.13‑4 `Publish_InteropSurface`**  | Publish interop summary | outputs of G.13‑2/‑3, UTS refs | `InteropSurface@Context` (+ UTS rows/twins) |
| **G.13‑5 `Emit_IndexTelemetryPin`** | Emit refresh input  | edition/policy changes + scope + payload pins  | telemetry to `G.11` (typed causes + payload pins)   |
| **G.13‑6 `Wire_To_SoTA_Pack`** | Provide shipping hook  | `InteropSurface@Context` + citations to upstream artefacts  | `G.10` pack hooks (as cited payload; no serialisation mandated)  |


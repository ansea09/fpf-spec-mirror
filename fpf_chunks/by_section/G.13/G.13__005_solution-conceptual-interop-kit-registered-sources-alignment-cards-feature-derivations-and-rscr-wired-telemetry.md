---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:4"
section_title: "Solution — Conceptual interop kit: registered sources, alignment cards, feature derivations, and RSCR‑wired telemetry"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__005_solution-conceptual-interop-kit-registered-sources-alignment-cards-feature-derivations-and-rscr-wired-telemetry.md"
commit_sha: "b223469ecafb9735c1d9bac220671e3336618339"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:4 — Solution — Conceptual interop kit: registered sources, alignment cards, feature derivations, and RSCR‑wired telemetry"
line_start: 132857
line_end: 132998
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

* **`ClaimMapperCard@Context`** — a declaration of the recipe whose application maps an external source into FPF-native inputs.

  **Shape (conceptual):**
  `⟨ MapperId, ExternalIndexId, MappingPolicyRef, Targets{ClaimSheet|BridgeHints|SoSFeatureSet|UTSProposals}, PlaneMapRef?, ScaleEmbeddingSpecRef?, EvidenceGraphId?, CSLCProofStubs? ⟩`

  **Notes.**

  * This is **not** a shadow legality gate. It is an interop surface that **cites** governing definitions (`A.19`, `G.0`, `G.3`, `G.4`) and publishes the required pins for downstream audit/refresh.
  * When cross-plane or cross-context reuse is implicated, alignment outputs must cite the actual relation and the receiving-use and reliance grounds required by its governor. Carry bundle or gate anchors when an independently applicable `E.18` flow crossing or `A.21` gate consumes the alignment, as required by `CC‑GCORE‑CROSS‑1`.
  * Avoid “edition echo”: downstream artefacts cite `ExternalIndexRef.edition` and `ClaimMapperRef.edition` (and optional `PlaneMapRef.edition` / `ScaleEmbeddingSpecRef.edition`) rather than copying snapshot ids/editions as free fields.

* **`SoSFeatureTransform@Context`** — declares how external signals become **CHR‑typed** SoS features (for DHC/dashboard usage and/or SoS‑LOG rule evaluation).

  **Shape (conceptual):**
  `⟨ SoSFeatureTransformId, Inputs{ClaimSheetId[] | ExternalSignalsRef}, SoSFeatureSetId, FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}, ReferencePlane, EvidenceGraphId?, PathSliceId[]?, ProofHooks? ⟩`

  **Notes.**

  * The derivation records **typing + provenance**; comparator and legality definitions remain with the cited governing patterns. When features are used as DHC measurements, establish or reuse C.16 measurement results. Make the active C.21 `DHCReplayBasis` recoverable for every persisted, compared, aggregated, or published coordinate.

* **`ScaleEmbeddingSpec@Context`** — optional constraints for representation/space alignment used inside an alignment recipe.

  **Shape (conceptual):**
  `⟨ ScaleEmbeddingSpecId, IntendedUse, AllowedTransformFamily, RequiredPins{NormalizationMethodRef.edition?}, ProhibitedCoercions ⟩`

  **Design intent.** Make any representation alignment *explicitly constrained* and edition‑pinned, instead of silently “creating a new scale”.
  **LEX/UTS note (informative).** `ScaleEmbeddingSpec` is a LEX head; when a public id is minted for a `ScaleEmbeddingSpec`, the corresponding UTS row must be published under F.17 with the Tech designation and any Plain designation needed for a stated didactic use.

* **`IndexTelemetryPin`** — an emitted refresh input that makes interop changes RSCR‑visible.

  **Shape (conceptual; RSCR‑typed):**
  `⟨ triggerKindId: RSCRTriggerKindId, scope: PathSliceId[] | PathId[] | PatternScopeId, payloadPins{ExternalIndexId, ExternalIndexRef.edition, ClaimMapperRef.edition?, MappingPolicyRef?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, PathId[]?, PathSliceId[]?, UTSRowId[]?, …} ⟩`

  **Publication.** Emitted to `G.11` as refresh input; recorded with canonical `RSCRTriggerKindId` causes.

* **`InteropSurface@Context`** — a selector-facing or dashboard-facing summary of what interop publications and records exist and how they are pinned.

  **Shape (conceptual):**
  `⟨ InteropSurfaceId, ExternalIndexId, ExternalIndexRef.edition, MapperId?, ClaimMapperRef.edition?, MappingPolicyRef?, SoSFeatureSetId?, EvidenceGraphId?, PathSliceId[]?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, UTSRowId[] ⟩`

  **Publication.** Published to UTS with twin labels as applicable.

#### G.13:4.3 - Use external sources to construct the needed input

Start with the input required by the receiving method and actual records from the external source. Reuse an adequate mapping recipe. To construct or revise one, establish the transformation and its limits before publishing its card and routing its outputs.

##### G.13:4.3.1 - Construct and check the mapping

1. **Recover the required output meaning.** Read the receiving operation’s input definition and conditions. For a G.2 ClaimSheet, this includes the claim, its subject, scope and source support; for a CHR feature, the subject, characteristic, scale, units and observation basis come from G.3/C.16. For a Bridge hint, preserve the two local meanings and the proposed relation for F.9 to examine. Select only the outputs needed by the receiving question.
2. **Recover what the available source fields denote.** Inspect actual records together with the provider’s definitions for that edition: the counted or described object, population, inclusion rules, units, dates/windows, missing-value conventions and identifiers. Follow a record’s citation to the underlying source when its metadata does not contain the claim or conditions needed. A field name is a locator; its definition and examples establish what a value represents. If the definition is unavailable, ask the provider or obtain the specified source passage before using the ambiguous field for that output.
3. **Connect each required output to its basis.** Select the exact source passage or field that supplies it, or define the operation that derives it. Direct copying requires compatible meanings. A count requires the population, inclusion predicate and identity/equivalence rule; a unit conversion requires a lawful scale conversion; a claim extraction retains the source’s subject, conditions and contrary evidence under G.2. For a semantic correspondence use F.9’s relation construction and its separate receiving-use test. For a measurement use C.16’s measurement model and G.3’s lawful operations. Where the needed transformation is not supplied by those methods or by an available domain method, identify the unsupplied transformation and the source or competent supplier needed to construct it.
4. **Apply the recipe to real records.** Work through at least one representative record to the required result and inspect a consequential variation, such as a duplicate identifier, an absent value, a changed time window or a different population definition. Choose the variation from the recipe’s actual assumptions. Retain the source value and derivation sufficiently for the receiving use to check them. Missing or ambiguous values remain missing or ambiguous; they become zero, false or a negative claim only when the source meaning and derivation establish that result.
5. **Return the obtained input or its exact gap.** A mapped result carries its source edition, applicable scope and transformation basis. A failed compatibility condition supports rejection of that mapping. An unresolved field definition, relation, measurement procedure or source claim prevents only the outputs that depend on it. Identify what source, observation or method construction could settle the gap and what can already be used. When the receiving contract requires a complete bundle, retain that unmet condition rather than treating a partial mapping as the bundle.

**Worked mapping.** Suppose a review needs the number of distinct research articles in a named collection published during 2025, and source-grounded ClaimSheets about their methods. The available index supplies records with `work_id`, `year`, `record_type`, a citation and an abstract. In this illustrative provider contract, `year` means first publication year, `work_id` identifies a work across duplicate records, and `record_type = research_article` is the relevant inclusion class. The recipe filters the stated collection by year and class, groups qualifying records by `work_id`, and counts those groups. Three qualifying records with ids `w1, w1, w2` yield two works. The result retains that population and counting basis; use as a DHC measurement additionally establishes the C.16 result and C.21 replay basis.

For the ClaimSheets, the citation leads to the article text. The reviewer extracts the method claim with its tested population and conditions under G.2; an abstract that omits those conditions leaves an extraction gap to settle from the article. The count and metadata alone supply no performance claim. If the provider instead defines `work_id` as a record identifier, the same three values no longer establish two distinct works: obtain an identity rule or source-level matching method before returning the work count. If `year` means index ingestion year, the recipe must obtain publication dates to answer the original question. Changing the receiving question to the number of index records ingested in 2025 can make those fields sufficient for that different result.

##### G.13:4.3.2 - Publish and use the established recipe

1. **Register source editions.** Author `ExternalIndexCard@Context` for each external source snapshot mapped through this kit, including `ExternalEdition` and the `entityOfConcern` plane anchor.
2. **Author mapping recipes.** Create `ClaimMapperCard@Context` for the established transformation and its limits, identifying the produced artefacts and applicable policy/spec references. Include `PlaneMapRef` or `ScaleEmbeddingSpecRef` when the transformation uses them.
3. **Produce FPF-native inputs.** Apply the recipe and route its obtained outputs to the receiving operation, for example:

   * `G.2` harvesting (ClaimSheets / operator & object inventories / candidate bridge hints),
   * `G.3` CHR typing (when numeric signals are formalized as CHR characteristics/scales/coordinates),
   * `G.4` acceptance/threshold policies (when a downstream decision requires explicit CAL policy rather than telemetry),
   * `G.12` dashboards (when derived SoS features support DHC readings; measurement claims consume C.16 results with the C.21 replay basis required by their use).
4. **Use the resulting inputs under the receiving rules.** Open only the applicable branch:

   * When selection or a selector-facing declaration is needed, `G.5` consumes the applicable grounded inputs and returns its declared outcome: a set result, narrowed handoff, abstain or escalation.
   * When a reproducible parity report is needed, `G.9` consumes the pinned editions and windows under its comparison plan.
   * When shipping is needed, `G.10` may include interop surfaces as cited publications or records.
5. **Emit telemetry and refresh causes.** On any change in external editions, alignment policies, plane maps, or embedding specs, emit:

   * a canonical `RSCRTriggerKindId` (per `G.Core`),
   * a scope (`PathSliceId[]` and/or `PatternScopeId`),
   * payload pins (editions/policies/UTS rows),
     enabling `G.11` to identify dependent uses and choose the further work their changed basis requires.

#### G.13:4.4 - Interfaces — minimal I/O standard (conceptual; kit‑only)

| ID   | Interface   | Consumes  | Produces   |
| ---- | ----------- | --------- | ---------- |
| **G.13‑1 `Register_ExternalIndex`**  | Register `ExternalIndexCard@Context` | Provider metadata, scope, **ExternalEdition**, freshness, entityOfConcern anchor   | `ExternalIndexCard@Context` (+ UTS row when published)   |
| **G.13‑2 `Map_ClaimsToFPF`**   | Apply `ClaimMapperCard@Context`   | `ExternalIndexCard@Context`, `MappingPolicyRef`, optional `PlaneMapRef`/`ScaleEmbeddingSpecRef`, optional EvidenceGraph hooks | `ClaimSheet@Context`, `BridgeHints`, optional `SoSFeatureSet@Context`, optional UTS proposals |
| **G.13‑3 `Derive_SoSFeatures`**  | Produce CHR‑typed SoS features  | ClaimSheets / external signals refs, CHR typing refs, legality proof hooks | `SoSFeatureSet@Context` (CHR‑typed; provenance pinned)   |
| **G.13‑4 `Publish_InteropSurface`**  | Publish interop summary | outputs of G.13‑2/‑3, UTS refs | `InteropSurface@Context` (+ UTS rows/twins) |
| **G.13‑5 `Emit_IndexTelemetryPin`** | Emit refresh input  | edition/policy changes + scope + payload pins  | telemetry to `G.11` (typed causes + payload pins)   |
| **G.13‑6 `Wire_To_SoTA_Pack`** | Provide shipping hook  | `InteropSurface@Context` + citations to upstream artefacts  | `G.10` pack hooks (as cited payload; no serialisation mandated)  |


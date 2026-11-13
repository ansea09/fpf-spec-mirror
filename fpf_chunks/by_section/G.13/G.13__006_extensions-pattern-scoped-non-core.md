---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:5"
section_title: "Extensions (pattern‑scoped; non‑core)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__006_extensions-pattern-scoped-non-core.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:5 — Extensions (pattern‑scoped; non‑core)"
line_start: 141132
line_end: 141201
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

### G.13:5 - Extensions (pattern‑scoped; non‑core)

Use `GPatternExtension` blocks with stable **PatternScopeId**s for provider- and method-specific requirements. The blocks identify the required pins, editions and policies. Cite the governing pattern and the provider or method that supplies the meaning or transformation used.

#### G.13:5.1 - `G.13:Ext.ExternalIndexProviderWiring`

- **PatternScopeId:** `G.13:Ext.ExternalIndexProviderWiring`
- **GPatternExtensionId:** `ExternalIndexProviderWiring`
- **GPatternExtensionKind:** `InteropSpecific`
- **GoverningPatternId:** `G.13` (source registration and refresh wiring)
- **Uses:** `{G.13}`
- **⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExternalIndexType`
* `ExternalEdition` *(as published on `ExternalIndexCard@Context`)*
* `Licence?`
* `CoverageScope`
* `ProviderChangePolicyId?` *(if provider‑specific “schema drift” handling exists)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*

**Notes (wiring-only):**

* Provider‑specific ingestion choices (e.g., OpenAlex‑class, Crossref‑class, ORKG‑class, discipline repositories) **must not** become Part-G-wide norms. This module only records which provider cards exist and which editions/policies are pinned.

#### G.13:5.2 - `G.13:Ext.EmbeddingBasedAlignment`

- **PatternScopeId:** `G.13:Ext.EmbeddingBasedAlignment`
- **GPatternExtensionId:** `EmbeddingBasedAlignment`
- **GPatternExtensionKind:** `MethodSpecific`
- **GoverningPatternId:** `G.13` (mapping interface); the selected alignment method governs its transformation and qualification.
- **Uses:** `{G.13, A.19, E.5.2}`
- **⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ScaleEmbeddingSpecRef.edition`
* `NormalizationMethodRef.edition?` *(when a declared normalization/representation transform is used)*
* `MappingPolicyRef`
* `EvidenceGraphId?` *(when evidence paths for alignment decisions are published)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*

**Notes (wiring-only):**

* A selected embedding-based method supplies the transformation and its qualification for the receiving relation. Cite that method and its edition with the applicable `ScaleEmbeddingSpec` and `NormalizationMethod` references.

#### G.13:5.3 - `G.13:Ext.EntityResolutionAndAliasDocking`

- **PatternScopeId:** `G.13:Ext.EntityResolutionAndAliasDocking`
- **GPatternExtensionId:** `EntityResolutionAndAliasDocking`
- **GPatternExtensionKind:** `InteropSpecific`
- **GoverningPatternId:** `G.13` (mapping interface), `F.17` (public naming); the selected entity-resolution method governs the identity judgement.
- **Uses:** `{F.17, E.10}`
- **⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `UTSRowId[]` *(for externally‑sourced entities that become publicly citable)*
* `ExternalIdAliasSetId?` *(labels only; canonical ids remain UTS ids)*
* `TokenizationPolicyId?`

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*

**Notes (wiring-only):**

* Establish source-entity identity through the selected resolution method before docking its external identifiers as aliases. Preserve the basis for identifying two records as one entity, or leave that identity unresolved; publishing an alias does not establish it.


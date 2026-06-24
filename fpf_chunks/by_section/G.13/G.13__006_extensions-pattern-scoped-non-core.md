---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:5"
section_title: "Extensions (pattern‑scoped; non‑core)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__006_extensions-pattern-scoped-non-core.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:5 — Extensions (pattern‑scoped; non‑core)"
line_start: 90463
line_end: 90527
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

`G.13` keeps provider/method specifics out of the kit core. Any such specificity appears as `GPatternExtension` blocks with stable **PatternScopeId**s. These modules are **wiring‑only**: they bind pins/editions/policies and cite the governing pattern rather than redefining semantics.

#### G.13:5.1 - `G.13:Ext.ExternalIndexProviderWiring` *(Phase‑3 seed)*

**PatternScopeId:** `G.13:Ext.ExternalIndexProviderWiring`
**GPatternExtensionId:** `ExternalIndexProviderWiring`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `governing pattern not yet selected` *(Annex/Interop or a future dedicated interop-governing pattern)*
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExternalIndexType`
* `ExternalEdition` *(as published on `ExternalIndexCard@Context`)*
* `Licence?`
* `CoverageScope`
* `ProviderChangePolicyId?` *(if provider‑specific “schema drift” handling exists)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*
**Notes (seed; wiring‑only):**

* Provider‑specific ingestion choices (e.g., OpenAlex‑class, Crossref‑class, ORKG‑class, discipline repositories) **must not** become Part‑G‑wide norms in Phase‑2. This module only records which provider cards exist and which editions/policies are pinned.

#### G.13:5.2 - `G.13:Ext.EmbeddingBasedAlignment` *(Phase‑3 seed; method‑specific wiring stub)*

**PatternScopeId:** `G.13:Ext.EmbeddingBasedAlignment`
**GPatternExtensionId:** `EmbeddingBasedAlignment`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `governing pattern not yet selected` *(Annex/Interop or a future dedicated interop-governing pattern; Phase-3 governing-pattern decision required)*
**Uses:** `{G.13, A.19, E.5.2}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ScaleEmbeddingSpecRef.edition`
* `NormalizationMethodRef.edition?` *(when a declared normalization/representation transform is used)*
* `MappingPolicyRef`
* `EvidenceGraphId?` *(when evidence paths for alignment decisions are published)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*
**Notes (wiring‑only; post‑2015 practice orientation):**

* “Embedding‑based” techniques are treated as **declared transforms** constrained by `ScaleEmbeddingSpec` and/or `NormalizationMethod` references, rather than as implicit semantics.
* The module binds editions and policies; it does not define what is “similar enough”.

#### G.13:5.3 - `G.13:Ext.EntityResolutionAndAliasDocking` *(interop‑specific; Phase‑3 seed)*

**PatternScopeId:** `G.13:Ext.EntityResolutionAndAliasDocking`
**GPatternExtensionId:** `EntityResolutionAndAliasDocking`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `governing pattern not yet selected` *(likely UTS-adjacent; requires Phase-3 governing-pattern decision)*
**Uses:** `{F.17, E.10}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `UTSRowId[]` *(for externally‑sourced entities that become publicly citable)*
* `ExternalIdAliasSetId?` *(labels only; canonical ids remain UTS ids)*
* `TokenizationPolicyId?`

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*
**Notes (seed; wiring‑only):**

* This module exists to prevent “ID drift by renaming” for externally sourced entities. It is intentionally a Phase‑3 seed until its governing pattern is selected.


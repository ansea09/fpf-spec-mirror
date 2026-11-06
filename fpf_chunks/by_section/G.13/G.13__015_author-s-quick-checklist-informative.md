---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:14"
section_title: "Author’s quick checklist (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__015_author-s-quick-checklist-informative.md"
commit_sha: "d8dd955fddb923b5b946d2c5865d0665cff5a67e"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:14 — Author’s quick checklist (informative)"
line_start: 133169
line_end: 133177
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

### G.13:14 - Author’s quick checklist (informative)

1. Establish the needed input and mapping from source definitions and actual records under :4.3; register each source snapshot with its `ExternalEdition`.
2. Author a `ClaimMapperCard@Context` with explicit `MappingPolicyRef` and required edition pins.
3. If you derive SoS features, declare a `SoSFeatureTransform@Context` and cite CHR typing refs and provenance hooks.
4. Publish an `InteropSurface@Context` that cites all active `…Ref.edition` values and UTS rows.
5. On any external edition or policy change, emit canonical RSCR trigger causes with explicit scope + payload pins.
6. Keep provider and method conditions with the applicable extension and its cited procedure.


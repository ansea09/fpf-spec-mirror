---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:12"
section_title: "SoTA-Echoing (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__013_sota-echoing-informative.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:12 — SoTA-Echoing (informative)"
line_start: 130960
line_end: 130971
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

### G.13:12 - SoTA-Echoing (informative)

* **Scholarly claim graphs & open indexes.** Research knowledge graphs and scholarly indexes can supply claim representations and concept taxonomies as mapping inputs. Treat these as *sources* registered via `ExternalIndexCard`, not as governing patterns.

* **Neural representations for scientific text.** Scientific encoders, such as SciBERT-class and citation-aware SPECTER-class representations, are candidates for alignment heuristics whose suitability must be established for the receiving question. In FPF terms, they belong behind `ScaleEmbeddingSpec` + pinned editions/policies (see `G.13:Ext.EmbeddingBasedAlignment`).

* **Schema matching and entity resolution.** Candidate approaches include deep entity matching, contrastive representation alignment and graph alignment. Select a mapping procedure for the stated relation and evidence, then record its use and limitations through the applicable extension.

* **Systematic-review reporting.** PRISMA-style records make source selection and exclusions inspectable. They can supply provenance and coverage inputs; G.2 still judges coverage for the receiving question. Preserve source editions and windows when consuming those records.

* **QD / Illumination and OEE declared set results.** When a QD or OEE use consumes an external taxonomy or environment corpus, expose its edition and mapping basis. Coverage and regret remain telemetry unless the applicable governing rule explicitly promotes them into the decision criteria.


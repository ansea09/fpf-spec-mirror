---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__002_problem-frame.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:1 — Problem frame"
line_start: 132234
line_end: 132241
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

### G.13:1 - Problem frame

External scholarly indexes and discipline repositories supply inputs for SoTA authoring. Examples include concept or dataset registries, paper/claim graphs, taxonomy stores and science-of-science indicator feeds. Their values must retain their source meaning and limits when used in FPF characterization, comparison, selection or reporting.

A mapping with unstated assumptions can change the receiving claim: edition drift becomes invisible, cross‑plane/context reuse becomes implicit, and external signals quietly start acting like a shadow governing spec ref.

`G.13` provides **registration, alignment and telemetry hooks** for whichever Part-G use needs those sources. A source may supply G.2 synthesis, G.3 characterization, G.5 selection, G.9 comparison or G.12 reporting inputs. G.10 carries an interop surface when shipping is needed; G.11 reconsiders dependent uses after a relevant change. These are connected uses, not a compulsory pipeline.


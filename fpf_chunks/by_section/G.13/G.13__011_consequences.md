---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:10"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__011_consequences.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:10 — Consequences"
line_start: 82688
line_end: 82694
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

### G.13:10 - Consequences

* **Interop becomes refresh‑ready.** External source drift produces typed RSCR causes with scopes/payload pins; refresh becomes slice‑scoped rather than global guesswork.
* **Generation‑first authoring becomes cheaper.** External sources become controlled inputs into SoTA synthesis and declared set-result exploration, not ad‑hoc audit decoration.
* **Conceptual hygiene improves.** Explicit cards + edition pins reduce semantic leakage from tools/formats/providers.
* **Cross‑tradition reuse becomes auditable.** Plane/context reuse is surfaced as crossings rather than embedded assumptions.


---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__001_intro.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:intro — Intro"
line_start: 106636
line_end: 106646
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

## G.13 - External Interop Hooks for SoTA Discipline Packs (conceptual)

**Tag.** Architectural kit pattern (conceptual interop kit; notation‑independent; normative when used)
**Stage.** *design‑time registration & alignment* → *run‑time ingestion, telemetry, refresh*
**Primary hooks.** `G.Core` (Part‑G core invariants + trigger catalogue + Default Governing Definition Index), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.4` (CAL Pack), `G.5` (selector & registries), `G.6` (EvidenceGraph + PathId/PathSliceId), `G.7` (BridgeMatrix + CL/planes), `G.8` (SoS‑LOG bundle surfaces), `G.9` (parity harness), `G.10` (shipping), `G.11` (refresh orchestration), `G.12` (dashboards), `A.19` (CN‑Spec), `A.18` (CSLC legality), `G.0` (CG‑Spec), `F.17` (UTS), `F.9` (BridgeCard / CL), `E.17` (publication faces), `E.5.2` (notation independence), `E.18/A.21` (GateCrossing/CrossingBundle checks).

**Status.** Stable (Phase‑2 universalized; `G.Core` linkage explicit)
**Normativity.** Normative when used (when any `G.13` surface is authored/emitted/consumed); informative otherwise.

**Non‑duplication note (Phase‑2 universalization).** This pattern **does not restate** Part‑G‑wide invariants (CN/CG spec-ref governing-definition assignment, crossing visibility, penalty routing, set‑return discipline, typed RSCR triggers, Default Governing Definition Index, Δ‑discipline). Those are governed in `G.Core` and referenced here via the linkage manifest and CC delegations (*cite, don’t duplicate*).


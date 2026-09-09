---
chunk_kind: "child"
pattern_id: "G.13"
pattern_title: "External Interop Hooks for SoTA Discipline Packs (conceptual)"
section_id: "G.13:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.13/G.13__001_intro.md"
commit_sha: "886e84cadcc302e1c622aec02a0a0ba1e1c3955d"
heading_path:
  - "G.13 — External Interop Hooks for SoTA Discipline Packs (conceptual)"
  - "G.13:intro — Intro"
line_start: 107556
line_end: 107566
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
**Primary hooks.** `G.Core` (Part‑G core invariants + trigger catalogue + Default Governing Definition Index), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.4` (CAL Pack), `G.5` (selector & registries), `G.6` (EvidenceGraph + PathId/PathSliceId), `G.7` (BridgeMatrix + CL/planes), `G.8` (SoS‑LOG bundle surfaces), `G.9` (parity harness), `G.10` (shipping), `G.11` (refresh orchestration), `G.12` (dashboards), `A.19` (CN‑Spec), `A.18` (CSLC legality), `G.0` (CG‑Spec), `F.17` (UTS), `F.9` (cross-semantic relations and bounded-use claims), `E.17` (publication faces), `E.5.2` (notation independence), `E.18` (crossing visibility when a selected transformation-flow structure is in use), `A.21` (gate decisions under an applicable profile).

**Status.** Stable
**Normativity.** Normative when used (when any `G.13` surface is authored/emitted/consumed); informative otherwise.

**Part‑G linkage.** `G.Core` governs Part‑G‑wide invariants; the linkage manifest in §4.1 and the conformance checklist in §8 name the applicable obligations.


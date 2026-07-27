---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__001_intro.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:intro — Intro"
line_start: 99300
line_end: 99307
dependencies:
  - "A.10"
  - "A.15.3"
  - "C.18"
  - "E.18"
  - "E.5.2"
  - "F.17-F.18"
  - "G.11"
  - "G.12"
  - "G.12-G.13"
  - "G.13"
  - "G.2"
  - "G.2-G.9"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "AuditPins"
  - "CrossingBundle"
  - "MOOManifest"
  - "PathId/PathSliceId"
  - "PortfolioRosterId"
  - "RSCR wiring"
  - "SoTA-Pack(Core)"
  - "UTS publication"
  - "edition pins"
  - "no semantic respecification"
  - "notation-independent pack"
  - "pack-boundary governing definition"
  - "parity pins"
  - "selector-ready publication surface"
  - "shipping"
  - "telemetry pins"
---

## G.10 - SoTA Pack Shipping

**Tag:** Architectural pattern (conceptual; notation‑independent; pack‑boundary governing definition)
**Stage:** release‑time composition and publication; edition‑aware; **GateCrossing‑gated** via `E.18` CrossingBundle (and the relevant GateCrossing harness patterns).
**Builds on:** `G.Core` (Part‑G core invariants and delegation); upstream pack/kit governing definitions as cited publications or records (not redefined here).
**Governs (scope boundary):** *shipping* of Part‑G outputs as a **pack** (`SoTA‑Pack(Core)`), including the pack‑level publication kit: (i) selector‑facing selection/parity roster, (ii) PathId/PathSlice citation surface, (iii) telemetry pins for refresh planning, and (iv) optional interop ingestion as citation‑only notes.
**Does not govern:** governing spec refs (`CN‑Spec`, `CG‑Spec`), CHR/CAL semantics, selection semantics, evidence semantics, bridge calibration semantics, refresh orchestration (these remain with their governing definitions and are **cited**).


---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__001_intro.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:intro — Intro"
line_start: 131074
line_end: 131084
dependencies:
  - "A.10"
  - "A.15.3"
  - "C.18"
  - "C.21"
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

> **Status:** Stable

**Use this when.** Part-G output must reach a selector, auditor or maintainer as one citable, editioned shipment. Start from that receiving use, collect the required upstream references and preserve the conditions for interpreting their results. A sufficient existing result can be cited directly; creating a new pack is needed only for this shipping use.

For an independently applicable `E.18` flow crossing or `A.21` gate, carry its required CrossingBundle or gate anchors into the shipped pack.
**Builds on:** `G.Core` (Part‑G core invariants and delegation); upstream pack/kit governing definitions as cited publications or records (not redefined here).
**Governs (scope boundary):** *shipping* of Part‑G outputs as a **pack** (`SoTA‑Pack(Core)`), including the pack‑level publication kit: (i) selector‑facing selection/parity roster, (ii) PathId/PathSlice citation surface, (iii) telemetry pins for refresh planning, and (iv) optional interop ingestion as citation‑only notes.
**Does not govern:** governing spec refs (`CN‑Spec`, `CG‑Spec`), CHR/CAL semantics, selection semantics, evidence semantics, bridge calibration semantics, refresh orchestration (these remain with their governing definitions and are **cited**).


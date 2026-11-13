---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__001_intro.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:intro — Intro"
line_start: 139752
line_end: 139765
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

**Use this when.** Part-G output must reach a selector, auditor or maintainer as one citable, editioned shipment. Start from that receiving use, collect the required upstream references and preserve the conditions for interpreting their results. You can cite a sufficient existing result directly. Create a new pack only when the receiving use calls for a shipment.

For an independently applicable `E.18` flow crossing or `A.21` gate, carry its required CrossingBundle or gate anchors into the shipped pack.

**Builds on:** `G.Core` defines the shared Part‑G invariants and delegation. Cite the publications or records that define the upstream packs and kits.

**Governs:** shipping Part‑G outputs as a `SoTA‑Pack(Core)`. A selector-facing outcome gets a selection/parity roster. The kit also exposes applicable `PathId`/`PathSliceId` citations and telemetry pins for refresh planning, and may include interop notes used only as citations. An inputs-only pack may omit the roster.

**Cites:** The definitions of `CN‑Spec` and `CG‑Spec`, CHR/CAL, selection, evidence, bridge calibration and refresh orchestration remain with their governing patterns.


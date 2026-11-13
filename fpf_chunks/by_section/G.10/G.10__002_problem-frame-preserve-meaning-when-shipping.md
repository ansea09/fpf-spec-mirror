---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:1"
section_title: "Problem frame — Preserve meaning when shipping"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__002_problem-frame-preserve-meaning-when-shipping.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:1 — Problem frame — Preserve meaning when shipping"
line_start: 139766
line_end: 139775
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

### G.10:1 - Problem frame — Preserve meaning when shipping

Part G produces publications and records governed by its kits and suites (harvest packs, CHR/CAL packs, evidence graphs, bridge calibration records, log bundles, parity reports). Without a defined pack boundary, shipping can become:

* a tool-specific export without citable contents, or
* a change to legality, defaults or selection semantics made in the course of shipping without being declared, or
* a brittle hand‑off that cannot support RSCR/refresh (no actionable pins/editions/policies attached).

`G.10` defines the **single normative shipping surface** for Part G, `SoTA‑Pack(Core)`, and how to compose a pack that a selector can use and an auditor can cite. `G.Core` governs the shared invariants.


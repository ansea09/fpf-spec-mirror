---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
section_id: "G.11:1"
section_title: "Problem frame — Keeping shipped SoTA current without global rebuilds"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__003_problem-frame-keeping-shipped-sota-current-without-global-rebuilds.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "G.11 — Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
  - "G.11:1 — Problem frame — Keeping shipped SoTA current without global rebuilds"
line_start: 129947
line_end: 129957
dependencies:
  - "A.10.1"
  - "A.6.RCD"
  - "B.3.4"
  - "C.11.DUA"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
  - "C.32.P2S"
  - "E.18"
  - "F.15"
  - "G.10"
  - "G.12"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G11"
keywords:
  - "Bridge Sentinels"
  - "PathSlice"
  - "RSCR"
  - "deprecation"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
  - "use-qualified currentness"
---

### G.11:1 - Problem frame — Keeping shipped SoTA current without global rebuilds

Part G produces shipped, selector-ready publication units and records: packs, bundles, evidence graphs, parity reports, and dashboards. Once shipped, they are exposed to:

* **telemetry** (illumination and archive changes, parity outcomes, dashboard deltas),
* **currentness conditions** (a relied-on premise changes, a justified review becomes due, or an actual qualification or use window ends),
* **edition drift** (descriptor, distance, or transfer rules bump; policy pins evolve),
* **bridge evolution** (CL or plane penalties or calibrations update).

G.11 governs the connection from typed refresh causes and their affected uses to selected plans and execution reports. G.Core supplies cause semantics and the applicable invariants.


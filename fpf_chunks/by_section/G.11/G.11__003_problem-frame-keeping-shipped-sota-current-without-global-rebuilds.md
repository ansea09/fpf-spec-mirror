---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:1"
section_title: "Problem frame — Keeping shipped SoTA current without global rebuilds"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__003_problem-frame-keeping-shipped-sota-current-without-global-rebuilds.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:1 — Problem frame — Keeping shipped SoTA current without global rebuilds"
line_start: 92804
line_end: 92819
dependencies:
  - "B.3.4"
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
  - "decay"
  - "deprecation"
  - "edition bumps"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
---

### G.11:1 - Problem frame — Keeping shipped SoTA current without global rebuilds

Part G produces shipped, selector-ready publication units and records: packs, bundles, evidence graphs, parity reports, and dashboards. Once shipped, they are exposed to:

* **telemetry** (illumination and archive changes, parity outcomes, dashboard deltas),
* **decay** (freshness windows expire; epistemic debt grows),
* **edition drift** (descriptor, distance, or transfer rules bump; policy pins evolve),
* **bridge evolution** (CL or plane penalties or calibrations update).

Without an explicit orchestration kit, refresh becomes either:

* a brittle set of ad-hoc “full rerun” rituals, or
* an audit-only refresh result that silently accumulates drift.

`G.11` is the **Part G governing definition** of the **refresh orchestration kit**: it turns typed refresh causes into **scoped plans** and **auditable execution reports**, while delegating all cause semantics and universal invariants to `G.Core`.


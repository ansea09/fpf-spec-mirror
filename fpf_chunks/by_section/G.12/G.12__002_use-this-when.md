---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline-Health Time Series and Views)"
section_id: "G.12:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__002_use-this-when.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "G.12 — DHC Dashboards (Discipline-Health Time Series and Views)"
  - "G.12:0 — Use This When"
line_start: 106412
line_end: 106419
dependencies:
  - "A.19"
  - "A.2.6"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.21"
  - "C.29"
  - "E.10"
  - "E.24.PUB"
  - "E.5.2"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.Core"
keywords:
  - "DHC"
  - "PathId/PathSliceId"
  - "RSCR/refresh wiring"
  - "UTS twins"
  - "admissible telemetry"
  - "dashboard"
  - "discipline health"
  - "edition pins"
  - "time-series"
  - "view-only slices"
---

### G.12:0 — Use This When

Use G.12 when a team needs several recorded C.21 coordinate results arranged across windows, a dashboard view over them, or refresh wiring for that view.

Start from the C.21 results, not from a screen layout. State the discipline, intended use, ClaimScope, coordinate-result refs, and windows. Stop with a local view when no audience publication or refresh use exists.

Do not use G.12 for one ordinary field-health claim, to manufacture measurements from rows, to turn a dashboard into evidence or authority, or to require publication and telemetry for every C.21 use.


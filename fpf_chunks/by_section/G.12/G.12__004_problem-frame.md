---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline-Health Time Series and Views)"
section_id: "G.12:2"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__004_problem-frame.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "G.12 — DHC Dashboards (Discipline-Health Time Series and Views)"
  - "G.12:2 — Problem Frame"
line_start: 106834
line_end: 106846
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

### G.12:2 — Problem Frame

Dashboards drift or become misleading when they:

* treat `ClaimScope` and a selected `TargetSlice` as one field;
* copy a value without its C.21 replay basis;
* average nominal or ordinal values or mix Units;
* hide normalization, distance, comparison, or target-band rules;
* require a Bridge for every source difference or omit F.9 when distinct local senses are actually related;
* turn a row, screenshot, UTS name, form, or carrier into the measurement or series episteme;
* turn selected sets or archives into one scalar winner; or
* rebuild everything because changed definition and evidence pins cannot be localized.


---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline-Health Time Series and Views)"
section_id: "G.12:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__003_intent.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "G.12 — DHC Dashboards (Discipline-Health Time Series and Views)"
  - "G.12:1 — Intent"
line_start: 103739
line_end: 103748
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

### G.12:1 — Intent

Produce a reproducible discipline-health series and view while keeping five objects separate:

1. C.16 measurement results and their C.2.1 coordinate-result epistemes;
2. one optional C.2.1 `DHCSeries` episteme that orders exact result refs by window;
3. rows and slices that represent those results or series;
4. any E.24.PUB publication occurrence, form, carrier, audience, and availability interval; and
5. any measurement, series-assembly, rendering, upload, or refresh Work.


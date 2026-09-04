---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline-Health Time Series and Views)"
section_id: "G.12:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__005_forces.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "G.12 — DHC Dashboards (Discipline-Health Time Series and Views)"
  - "G.12:3 — Forces"
line_start: 106847
line_end: 106856
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

### G.12:3 — Forces

| Force | Tension |
| --- | --- |
| Readable view vs replay | A useful dashboard should be easy to read, while every relied-on coordinate must return to its exact definition and result. |
| Stable history vs changed definitions | A new method or Scale edition may invalidate trend comparability without changing historical results. |
| Optional publication vs local use | A local view may be enough; audience availability adds a separate publication relation. |
| Selective refresh vs process burden | Refresh needs actionable pins, but a one-off view needs no telemetry framework. |
| Set-valued results vs headline pressure | A view can summarize without manufacturing a scalar winner. |


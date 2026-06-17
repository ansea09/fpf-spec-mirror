---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
section_id: "G.12:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__002_intent.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
  - "G.12:1 — Intent"
line_start: 84204
line_end: 84211
dependencies:
  - "A.19"
  - "C.18"
  - "C.19"
  - "C.21"
  - "E.10"
  - "E.5.2"
  - "F.17"
  - "F.18"
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

Produce **admissible, reproducible, refresh-aware discipline-health dashboards** by turning **C.21** DHC definitions into:

1. a **UTS‑published** time series (`DHCSeries@Context`) whose rows are evidence‑citable by **`PathId`/`PathSliceId`**,
2. a dashboard slice view (`DashboardSlice@Context`) that is **view‑only** (no hidden re‑aggregation or “new objectives”), and
3. **telemetry pins** that allow **G.11** to plan **slice‑scoped refresh** (rather than “rerun everything”).


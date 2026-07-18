---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
section_id: "G.12:9"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__010_relations.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
  - "G.12:9 — Relations"
line_start: 97022
line_end: 97027
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

### G.12:9 — Relations

**Builds on:** `G.Core`, `C.21`, `G.6`, `G.11`, `A.19`, `G.0`, `F.17/F.18`, `E.5.2`, `E.10`.
**Coordinates with:** `G.5` *(when selector set-result outputs are consumed)*, `G.7` *(when crossings/plane routing or `CL/Φ/Ψ/Φ_plane` policy pins are used)*, `G.8` *(when maturity ladder view is included)*, `G.10` *(when dashboard slices are shipped)*.
**Constrains:** dashboard consumers: dashboards are projections over pinned, evidence‑citable rows; they do not mint new governing-spec semantics.


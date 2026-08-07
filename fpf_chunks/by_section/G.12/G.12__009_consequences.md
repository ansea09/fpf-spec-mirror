---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
section_id: "G.12:8"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__009_consequences.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
  - "G.12:8 — Consequences"
line_start: 103703
line_end: 103708
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

### G.12:8 — Consequences

* **Dashboards become reproducible artefacts, not screenshots.** A `DHCRow@Context` is re‑derivable under pinned editions and evidence windows.
* **Selective maintenance becomes possible.** Telemetry pins let `G.11` refresh what changed (path slice / window / method edition), rather than rerunning the entire pipeline.
* **Illicit scalarization is structurally discouraged.** Set‑returning and CN/CG-governed semantics are preserved into the dashboard layer.


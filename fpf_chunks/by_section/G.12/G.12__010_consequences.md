---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline-Health Time Series and Views)"
section_id: "G.12:8"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__010_consequences.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "G.12 — DHC Dashboards (Discipline-Health Time Series and Views)"
  - "G.12:8 — Consequences"
line_start: 107126
line_end: 107133
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

### G.12:8 — Consequences

**Benefits.** Dashboard claims can be read quickly and replayed from exact result and definition refs. Historical results remain distinct from changed definitions, and refresh can be local when needed.

**Costs.** A relied-on trend needs exact result, scope, window, and replay identities. Publication and refresh add their own conditional work.

**Risks avoided.** Screenshot-as-result, context-container resurrection, scope/slice collapse, hidden method drift, illicit ordinal arithmetic, scalarization by view, and carrier-as-publication are blocked.


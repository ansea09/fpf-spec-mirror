---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline-Health Time Series and Views)"
section_id: "G.12:5"
section_title: "Interfaces"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__007_interfaces.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "G.12 — DHC Dashboards (Discipline-Health Time Series and Views)"
  - "G.12:5 — Interfaces"
line_start: 104751
line_end: 104761
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

### G.12:5 — Interfaces

| Interface | Consumes | Produces |
| --- | --- | --- |
| `Create_DHCSeries` | exact coordinate-result refs, discipline, intended use, ClaimScope, windows, comparison basis, optional definition-set and target-slice refs | one C.2.1 `DHCSeries` episteme edition |
| `Update_DHCSeries` | prior series edition, added or replaced exact result refs, affected windows, edition rule | successor series episteme edition plus exact edition relation when asserted |
| `Render_DHCView` | exact result or series refs, view specification, annotations | `DHCRow[]` and/or `DashboardSlice` representations |
| `Publish_DHCView` | selected episteme or view edition plus E.24.PUB audience, bounded use, form, carrier, and interval | obtaining publication relation when its predicate holds |
| `Emit_DHCTelemetry` | exact changed definition, window, evidence, crossing, or policy pin and affected slice | G.11-facing telemetry payload |
| optional panel interfaces | the corresponding extension's exact values | only that panel's representation and conditional refresh pins |


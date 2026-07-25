---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
section_id: "G.12:5"
section_title: "Interfaces (conceptual; kit surface)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__006_interfaces-conceptual-kit-surface.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
  - "G.12:5 — Interfaces (conceptual; kit surface)"
line_start: 99890
line_end: 99903
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

### G.12:5 — Interfaces (conceptual; kit surface)

| ID  | Interface   | Consumes   | Produces  |
| --- | ----------- | ---------- | --------- |
| **G.12‑1 `Create_DHCSeries`** | Create/bind a DHC series scope (C.21‑grounded; edition‑aware) | `DHCSlotId[]`, `DHCPackRef.edition?`, `DHCMethodSpecRef.edition`, `TargetSlice` (USM), `WindowSpec?`, `ReferencePlane`, `CNSpecRef.edition`, `CGSpecRef.edition` | `DHCSeries@Context` (UTS publication unit; edition‑aware) |
| **G.12‑2 `Update_DHCSeries`** | Compute/update one or more rows under pinned conditions (run‑time; Work/Audit‑citable) | `PathSliceId[]`, `EvidenceGraphId?`, `DHCMethodRef.edition`, `DHCMethodSpecRef.edition`, `Γ_time`, crossing pins (if any) | `DHCRow@Context[]` (UTS publication units; stance and pins; `DesignRunTag = run`) |
| **G.12‑3 `Integrate_PortfolioTelemetry`** *(extension‑gated)* | Integrate selector set-result evidence into a slice/series | See `G.12:Ext.PortfolioTelemetry` | Extension‑gated fields / telemetry pins |
| **G.12‑4 `Integrate_QDTelemetry`** *(extension‑gated)* | Integrate QD illumination/archive telemetry | See `G.12:Ext.QDTelemetry` | Extension‑gated fields / telemetry pins |
| **G.12‑5 `Integrate_OEETelemetry`** *(extension‑gated)* | Integrate open‑endedness / transfer telemetry | See `G.12:Ext.OpenEndedTelemetry` | Extension‑gated fields / telemetry pins |
| **G.12‑6 `Publish_DashboardSlice`** | Publish a view slice as a projection over computed rows | `DHCSeriesId(UTS)[]`, `DHCRowId(UTS)[]?`, `SliceAnnotations?` | `DashboardSlice@Context` (UTS publication unit; view‑only) |
| **G.12‑7 `Emit_TelemetryPins`** | Emit RSCR‑actionable telemetry pins for refresh | `RSCRTriggerKindId`, `scope`, `payloadPins` | `DHCTelemetryPin[]` (consumed by `G.11`) |

(*No file formats are introduced here; serialisation recipes live under shipping or interop governance.*)


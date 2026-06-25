---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
section_id: "G.12:10"
section_title: "Author’s quick checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__011_author-s-quick-checklist.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
  - "G.12:10 — Author’s quick checklist"
line_start: 91063
line_end: 91072
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

### G.12:10 — Author’s quick checklist

1. Declare the dashboard series scope: `TargetSlice` (USM tuple), `ReferencePlane`, and an explicit `Γ_time` regime (per‑row; optionally a `WindowSpec` that yields the row windows).
2. Select `DHCSlotId[]` and cite **C.21** (do not restate slot semantics).
3. Pin `DHCMethodSpecRef.edition` and `DHCMethodRef.edition` for every computed slot/value (plus any other definition pins actually used).
4. Ensure rows are evidence‑citable by `PathSliceId[]` and include explicit `Γ_time` (row is run‑time: `DesignRunTag = run`).
5. Publish UTS publication units with twins and the required pins.
6. Emit canonical telemetry pins (`RSCRTriggerKindId` + scope + payload pins) for `G.11`.
7. If SoTA palette hooks / selection / QD / OEE / maturity / shipping panels are needed, add the corresponding `G.12:Ext.*` blocks and satisfy their pins.


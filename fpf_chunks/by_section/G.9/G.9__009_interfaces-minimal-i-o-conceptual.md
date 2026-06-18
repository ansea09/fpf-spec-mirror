---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:5"
section_title: "Interfaces (minimal I/O; conceptual)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__009_interfaces-minimal-i-o-conceptual.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:5 — Interfaces (minimal I/O; conceptual)"
line_start: 82935
line_end: 82945
dependencies:
  - "A.19"
  - "A.21"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.22.1"
  - "C.23"
  - "C.27"
  - "C.28"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "adaptation parity"
  - "benchmark plan"
  - "comparator pins"
  - "freshness windows"
  - "parity harness"
  - "selected-set outcomes"
---

### G.9:5 — Interfaces (minimal I/O; conceptual)

| Interface                          | Consumes                                                                                                                                         | Produces                                                                                        |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **G.9‑1 `Plan_Parity`**            | `BaselineSet`, `BaselineBindingRef`, `FreshnessWindows`, `Budgeting?`, `EpsilonDominance?`, `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`, `SCPRef.edition?`, `MinimalEvidenceRef.edition?`, `UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`, `ParityPinSet`, `PlanItemRefs[]?` | `ParityPlan@Context` (UTS entry; edition‑pinned)                                                |
| **G.9‑2 `Run_Parity`**             | `ParityPlan@Context`, `TaskSignatureRef` (S2), **G.5‑3 Select**                                                                                  | Selector outputs (selected sets / archives / sets as refs), DRR+SCR pins with `PathId[]`/`PathSliceId?` |
| **G.9‑3 `Publish_ParityReport`**   | parity-run trace refs + active pins                                                                                                            | `ParityReport@Context` (UTS publication record; emits canonical RSCR ids)                       |
| **G.9‑4 `Expose_ParityTelemetry`** | Telemetry deltas (archive changes, coverage/regret signals, etc.)                                                                                | Telemetry events carrying `PathSliceId?`, policy‑ids, and edition pins for refresh wiring       |

*Publication records are conceptual here; serialisations belong in shipping and interop publication forms (see `G.10` and interop annexes), not in `G.9`.*


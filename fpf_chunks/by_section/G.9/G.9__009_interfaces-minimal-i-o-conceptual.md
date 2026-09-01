---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:5"
section_title: "Interfaces (minimal I/O; conceptual)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__009_interfaces-minimal-i-o-conceptual.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:5 — Interfaces (minimal I/O; conceptual)"
line_start: 105436
line_end: 105446
dependencies:
  - "A.19"
  - "A.2.6"
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
  - "U.ClaimScope"
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
| **G.9‑1 `Plan_Parity`**            | exactly one subject branch—one `EntityOfConcernRef` or exact `targetRefs[]` under their existing kinds and editions—plus `GroundingHolonRef`, `ReferencePlane`, `ClaimScope`, `EvaluationWindow`, `BaselineSet`, `BaselineBindingRef`, `FreshnessWindows`, `Budgeting?`, `EpsilonDominance?`, `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`, mode-specific measurement or normalization editions when used, `SCPRef.edition?`, `MinimalEvidenceRef.edition?`, `UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`, `ParityPinSet`, `EvidenceGraphId`, `PathId[]`, `PathSliceId?`, `PlannedFillingRows[]?` | one immutable `ParityPlan` WorkPlan edition and its exact `ParityPlanRef` |
| **G.9‑2 `Run_Parity`**             | exact `ParityPlanRef`, `TaskSignatureRef` (S2), **G.5‑3 Select**                                                                                | selected-set, archive, or other set refs; DRR and SCR pins with `PathId[]` and, when needed, `PathSliceId` |
| **G.9‑3 `Publish_ParityReport`**   | exact `ParityPlanRef`, parity-run trace refs, and active pins                                                                                   | `ParityReport` carrying the same exact plan ref and baseline binding (UTS publication record; emits canonical RSCR ids) |
| **G.9‑4 `Expose_ParityTelemetry`** | Telemetry deltas (archive changes, coverage/regret signals, etc.)                                                                                | Telemetry events carrying `PathSliceId?`, policy‑ids, and edition pins for refresh wiring       |

*Publication records are conceptual here; serialisations belong in shipping and interop publication forms (see `G.10` and interop annexes), not in `G.9`.*


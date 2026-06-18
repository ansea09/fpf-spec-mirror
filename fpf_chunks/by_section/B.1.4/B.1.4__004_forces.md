---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__004_forces.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:3 — Forces"
line_start: 30604
line_end: 30612
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
keywords:
  - "composition"
  - "order-sensitive"
  - "temporal aggregation"
  - "time-series"
---

### B.1.4:3 - Forces

| Force                                 | Tension                                                                                                          |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Order fidelity vs. Simplicity**     | Preserve step order (non‑COMM) ↔ Keep reasoning lightweight and composable.                                      |
| **Temporal coverage vs. Flexibility** | Ensure gap/overlap discipline across phases ↔ Allow rolling windows and partial histories.                       |
| **Locality vs. Concurrency**          | Keep branches deterministic and independent ↔ Exploit parallelism where it is safe.                              |
| **Universality vs. Fit**              | One pattern for systems and epistemes ↔ Different edge types (`SerialStepOf`, `PhaseOf`) and different carriers. |


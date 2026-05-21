---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:8"
section_title: "Anti‑patterns and their fixes"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__009_anti-patterns-and-their-fixes.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:8 — Anti‑patterns and their fixes"
line_start: 29001
line_end: 29012
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

### B.1.4:8 - Anti‑patterns and their fixes

| Anti‑pattern                         | Symptom                                                     | Fix                                                                                                                     |
| ------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Structure‑as‑sequence**            | `StepB ComponentOf StepA` to force an order                 | Use `SerialStepOf` (Γ\_ctx) and an explicit `σ` with a join condition if needed.                                        |
| **History‑as‑structure**             | `v2 ComponentOf v1`                                         | Use `PhaseOf`; if identity actually changed, model a Transformer (A.12) producing a new holon.                          |
| **Parallelism without independence** | Declaring `ParallelFactorOf` but sharing hidden state       | Either declare the shared state as an interface and remove independence, or refactor so branches are truly independent. |
| **Overlapping phases**               | Two `PhaseOf` intervals for the same carrier overlap        | Split the intervals or justify overlap as measurement resolution; otherwise fold is invalid.                            |
| **DesignRunTag chimera**               | Mixing run logs with design plan in one Γ\_ctx/Γ\_time fold | Split into two graphs by scope; relate through a Transformer or mapping at value level.                                 |
| **Cost in Γ\_time**                  | Trying to sum energy in Γ\_time                             | Route costs to Γ\_work per phase; Γ\_time composes history, not expenditure.                                            |



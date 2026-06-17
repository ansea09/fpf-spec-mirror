---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Graph & Proofs"
section_id: "B.1.1:9"
section_title: "Anti‑pattern diagnostics (before → after)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__010_anti-pattern-diagnostics-before-after.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "B.1.1 — Dependency Graph & Proofs"
  - "B.1.1:9 — Anti‑pattern diagnostics (before → after)"
line_start: 29990
line_end: 30000
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
keywords:
  - "dependency graph"
  - "proofs"
  - "set"
  - "slice"
  - "structural aggregators"
  - "sum"
---

### B.1.1:9 - Anti‑pattern diagnostics (before → after)

| Anti‑pattern                     | Symptom                                                        | Replace with                                                                                                                                            |
| -------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Collection as stock**          | `Cell_i MemberOf Battery` then summing “capacity” via MemberOf | Use `PortionOf` for capacity partitions; use `ComponentOf` for physical pack assembly; keep MemberOf only for the *set of cells* as a collection holon. |
| **External supplier as part**    | `PowerGrid ComponentOf Plant`                                  | Model `PowerGrid` as an external holon with `U.Interaction` at the plant boundary; keep plant internals as `ComponentOf`.                               |
| **Order encoded as structure**   | `Step2 ComponentOf Step1`                                      | Use `SerialStepOf`/`ParallelFactorOf` and Γ\_method.                                                                                                      |
| **History encoded as structure** | `v2 ComponentOf v1`                                            | Use `PhaseOf` for time slices of the *same* carrier, or a Transformer creating a new holon (A.12) if identity changes.                                  |
| **Mapping as parthood**          | `DigitalTwin ConstituentOf Turbine`                            | Keep the twin as a separate holon; link by `U.Interaction` and value‑level mapping; do not use parthood.                                                |
| **DesignRunTag chimera**           | Mix of CAD nodes and telemetry nodes                           | Split into two graphs (`design` vs `run`) and connect via a Transformer role if needed.                                                                 |


---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:3"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__004_problem.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:3 — Problem"
line_start: 58727
line_end: 58733
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:3 - Problem

1. **Morphisms ≠ Graph.** A catalog of morphism-scoped patterns (e.g., UNM, Selector, Work, Refresh) does not, by itself, explain **how the whole graph is built, constrained, and audited**.
2. **Flow proliferation.** Multiple “reference flows” can be declared; readers need **one graph discipline** that keeps them admissible and comparable **without privileging any single flow**.
3. **Unsafe publication.** Faces re‑list I/O, hide scalarization, or omit edition/plane pins; cross‑Context reuse lacks **Bridge/CL** citation; **plane penalties** appear in F/G instead of R.
4. **Cycles without norms.** Selection↔Planning loops run without explicit **budget (Γ_time)**, **FreshnessRequest**, or **slice‑scoped** refresh; `FinalizeLaunchValues` (launch‑value slot filling) is performed too early (outside `U.Work` (`U.WorkEnactment`)).


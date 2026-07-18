---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:3"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__004_problem.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:3 — Problem"
line_start: 78324
line_end: 78330
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P2W support"
  - "composition"
  - "crossings"
  - "flow valuation"
  - "guards"
  - "selected transformations"
  - "transformation flow structure"
---

### E.18:3 - Problem

1. **Mathematical lens != selected structure.** A catalog of morphism-scoped, transformation-scoped, mechanism-scoped, work-scoped, or refresh-scoped patterns does not, by itself, explain **how the whole selected structure is built, constrained, and audited**.
2. **Flow proliferation.** Multiple “reference flows” can be declared; practitioners need **one structure discipline** that keeps their flow relations typed and comparable **without privileging any single flow**.
3. **Unsafe publication.** Faces re‑list inputs and outputs, hide scalarization, or omit edition and plane pins; cross‑Context reuse lacks **Bridge and CL** citation; **plane penalties** appear in F-lane or G-lane instead of R-lane.
4. **Cycles without norms.** Selection↔Planning loops run without explicit **budget (Γ_time)**, **FreshnessRequest**, or **slice‑scoped** refresh; `FinalizeLaunchValues` (launch‑value slot filling) is performed too early (outside `U.Work` (`U.WorkEnactment`)).


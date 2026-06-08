---
chunk_kind: "child"
pattern_id: "B.1"
pattern_title: "Universal Algebra of Aggregation (Γ)"
section_id: "B.1:5"
section_title: "Domain‑Specific “Flavours” of Γ"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1/B.1__006_domain-specific-flavours-of.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "B.1 — Universal Algebra of Aggregation (Γ)"
  - "B.1:5 — Domain‑Specific “Flavours” of Γ"
line_start: 29049
line_end: 29061
dependencies:
  - "A.1"
  - "A.9"
  - "B.1.x"
  - "B.2"
keywords:
  - "COMM"
  - "IDEM"
  - "LOC"
  - "MONO"
  - "WLNK"
  - "aggregation"
  - "composition"
  - "gamma operator"
  - "holon"
  - "invariants"
---

### B.1:5 - Domain‑Specific “Flavours” of Γ

The core signature of Γ never changes, but each discipline supplies a **flavour** that instantiates the quintet with domain‑appropriate mathematics and measurement units.

| Flavour      | Typical domain                                               | Dropped / relaxed invariants   | Added compensating rules                                                            | Canonical reference model (post‑2015)                                  |
| ------------ | ------------------------------------------------------------ | ------------------------------ | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Γ\_sys**  | Physical & cyber‑physical systems                            | *None*                         | –                                                                                   | ISO 15926‑2024 *Plant Data* roll‑up; NASA 2023 Integrated Hazard Model |
| **Γ\_epist** | Knowledge graphs, meta‑analysis                              | *None*                         | Provenance weighting (PW‑1), Citation transparency (PW‑2)                           | OntoCommons 2024 audit trail                                           |
| **Γ\_time**  | Time‑series forecasting, digital twins                       | COMM → **partial**; LOC waived | Coverage completeness (TS‑1), Temporal alignment (TS‑2)                             | EU Battery Passport 2025 reliability stack                             |
| **Γ\_ctx**   | Order‑sensitive processes, quantum pipelines, social surveys | COMM & LOC waived              | Reproducibility hash (CTX‑1), Partial‑order soundness (CTX‑2), Observer log (CTX‑3) | CERN HL‑LHC workflow 2024                                              |

> **Didactic hint for managers:** choose the flavour whose examples look like your own dashboards; then verify your tooling honours its extra rules.


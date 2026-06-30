---
chunk_kind: "child"
pattern_id: "A.9"
pattern_title: "Cross‑Scale Consistency (C‑3)"
section_id: "A.9:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.9/A.9__003_problem.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.9 — Cross‑Scale Consistency (C‑3)"
  - "A.9:2 — Problem"
line_start: 19850
line_end: 19859
dependencies:
  - "A.1"
  - "A.8"
  - "A.9"
  - "B.1"
keywords:
  - "aggregation"
  - "composition"
  - "holarchy"
  - "invariants"
  - "roll-up"
---

### A.9:2 - Problem

| Failure Mode              | Real‑World Symptom                                         |
| ------------------------- | ---------------------------------------------------------- |
| **Invalid extrapolation** | Unit‑tested module fails once integrated.                  |
| **Brittle dashboards**    | Portfolio KPI “green” hides a red supplier averaged away.  |
| **Compositional chaos**   | Different teams’ roll‑ups yield non‑deterministic results. |

These pathologies derail safety cases and budget decisions across disciplines.


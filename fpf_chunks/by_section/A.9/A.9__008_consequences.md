---
chunk_kind: "child"
pattern_id: "A.9"
pattern_title: "Cross‑Scale Consistency (C‑3)"
section_id: "A.9:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.9/A.9__008_consequences.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.9 — Cross‑Scale Consistency (C‑3)"
  - "A.9:7 — Consequences"
line_start: 22537
line_end: 22545
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

### A.9:7 - Consequences

| Benefit                      | Why it matters                                                   | Trade‑off / Mitigation                                                           |
| ---------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Stable roll‑ups**          | Summaries and reports remain faithful as parts evolve.          | Requires early agreement on `Γ`; offer reference libraries.                      |
| **Visible risk floor**       | WLNK blocks “averaging away” critical weaknesses.                | Can look overly conservative; redundancy, when real, lifts the minimum honestly. |
| **Parallel progress**        | COMM + LOC allow distributed teams to integrate without re‑work. | Needs explicit independence assumptions; templates guide authors.                |
| **Objective emergence flag** | Quintet failure becomes a measurable R\&D signal.                | Teams must learn to document MHTs instead of ignoring anomalies.                 |


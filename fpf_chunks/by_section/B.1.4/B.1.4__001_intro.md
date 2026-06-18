---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__001_intro.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:intro — Intro"
line_start: 30575
line_end: 30585
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

## B.1.4 - Contextual & Temporal Aggregation (Γ\_ctx & Γ\_time)

> **Status:** Stable

> **► decided‑by: A.14 Advanced Mereology**
**A.14 compliance —** **Γ\_ctx** relies on **SerialStepOf/ParallelFactorOf** (order semantics); **Γ\_time** composes **PhaseOf** slices of the *same* carrier with coverage/no‑overlap; **PortionOf** is orthogonal (quantities within steps), mappings are not parthood.

> **Plain‑English headline.**
> Use **Γ\_ctx** when *the order of steps changes meaning*.
> Use **Γ\_time** when *we are aggregating the same carrier across a timeline*.


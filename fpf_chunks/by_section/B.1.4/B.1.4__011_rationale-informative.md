---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:10"
section_title: "Rationale (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__011_rationale-informative.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:10 — Rationale (informative)"
line_start: 30249
line_end: 30252
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

### B.1.4:10 - Rationale (informative)

This pattern implements **A.15’s ordered relations** (`SerialStepOf`, `ParallelFactorOf`) and leverages **A.14’s `PhaseOf`** for timeline; consistent with **Strict Distinction**: order and time are not structure, and costs are not history. The adapted invariants (NC‑1..3 and T‑1..3) give precise replacements for COMM/LOC where these do not hold, while retaining WLNK and MONO. The result is a small, stable interface that matches how engineers and researchers already argue about procedures and histories, without importing domain‑specific notations into the kernel.


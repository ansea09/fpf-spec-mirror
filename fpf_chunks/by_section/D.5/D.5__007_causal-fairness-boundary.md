---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:4"
section_title: "Causal Fairness Boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__007_causal-fairness-boundary.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:4 — Causal Fairness Boundary"
line_start: 67596
line_end: 67603
dependencies:
  - "A.10"
  - "B.3"
  - "C.16"
  - "C.28"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.4"
  - "E.13"
  - "E.17"
  - "E.5.4"
keywords:
---

### D.5:4 - Causal Fairness Boundary

A fairness claim can be associative, interventional, or counterfactual. D.5 records the ethical-audit use of that claim, but `C.28` owns the causal-use question, causality-ladder rung, estimand, identification, realizability, evidence design, `CausalEvidenceSupportBasis`, and causal-use verdict.

Metric-only fallback: if only metric disparity is claimed and no causal fairness use is made, record it as metric or evaluation use. Do not add causal-fairness machinery by vocabulary alone.

Fairness escalation rule: an interventional-action proxy may admit bounded interventional fairness use, but it cannot be published as counterfactual fairness without the needed C.28 evidence value and verdict.


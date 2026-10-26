---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:10a"
section_title: "Trade‑offs & mitigations"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__012_trade-offs-mitigations.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:10a — Trade‑offs & mitigations"
line_start: 49737
line_end: 49742
dependencies:
  - "A.17"
  - "A.18"
  - "B.4"
  - "B.5"
  - "B.5.2"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.19"
  - "G.5"
keywords:
---

### B.5.2.1:10a - Trade‑offs & mitigations

* **Cognitive effort.** Interpreting Pareto sets and coverage maps adds overhead. Use the compact comparison view in §7 with its coordinate meanings and provenance.
* **Locality.** Novelty/diversity are **context‑local**; Cross‑context reuse requires **re‑measurement or an explicit mapping**.
* **Metric gaming & collinearity.** Avoid making **N** and **S** redundant by policy; when strong collinearity is detected, freeze one as informative only and record rationale in the DRR.


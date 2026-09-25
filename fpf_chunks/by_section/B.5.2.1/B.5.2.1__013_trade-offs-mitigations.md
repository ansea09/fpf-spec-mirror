---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:10a"
section_title: "Trade‑offs & mitigations"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__013_trade-offs-mitigations.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:10a — Trade‑offs & mitigations"
line_start: 46726
line_end: 46732
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

* **Cognitive effort.** Interpreting Pareto sets and coverage maps adds thinking overhead. *Mitigation:* standard “NQD Card” + default grids; keep **Characteristics** small in number (≤ 7). *Manager shortcut:* pick 2–3 **Q** characteristics that reflect the anomaly, then run with defaults.
* **Locality.** Novelty/diversity are **context‑local**; Cross‑context reuse requires **re‑measurement or an explicit mapping**. This pattern **does not define** Cross‑context operational controls.
* **Not a magic idea machine.** Abduction remains human/agentic; the pattern *structures* search, it does not automate insight. B.5.2 supplies the explanatory-hypothesis contribution; B.5 selects the next needed reasoning contribution.
* **Metric gaming & collinearity.** Avoid making **N** and **S** redundant by policy; when strong collinearity is detected, freeze one as informative only and record rationale in the DRR.


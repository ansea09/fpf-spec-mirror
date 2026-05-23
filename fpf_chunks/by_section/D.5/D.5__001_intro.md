---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias-Audit & Ethical Assurance"
section_id: "D.5:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__001_intro.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "D.5 — Bias-Audit & Ethical Assurance"
  - "D.5:intro — Intro"
line_start: 49350
line_end: 49358
dependencies:
  - "B.3"
  - "B.3.3"
  - "C.28"
  - "E.5.4"
keywords:
  - "AI ethics"
  - "assurance"
  - "audit"
  - "bias"
  - "ethics"
  - "fairness"
  - "responsible AI"
  - "review cycle"
  - "taxonomy"
---

## D.5 - Bias-Audit & Ethical Assurance

**Use this when.** Use this pattern when a holon, model, metric, decision system, policy, or authored FPF claim may create unfair, biased, or ethically unsafe effects for people or groups. If the fairness claim is causal — for example "this intervention is fair", "this policy would have prevented harm", "this model is counterfactually fair", or "this practice causally reduces disparity" — keep the ethical audit in `D.5` and cite `C.28` for causal-use question, causality-ladder rung, estimand, causal evidence support basis, identification, realizability, evidence design, support record, and support verdict.

**Not this pattern when.** If the live question is only measurement construction, use `C.16`; if it is only causal-use support without fairness or ethical audit, use `C.28`; if it is only an assurance claim or assurance support posture, use `B.3`. Metric disparity alone is not yet causal fairness.


**Causal-fairness boundary.** A local `C.28` causal-fairness repair, such as adding a causal-use question, estimand, support basis, support record, or supported-fairness-use and unsupported-fairness-use pair, is not by itself the Bias-Audit Cycle. It remains a local support repair until the claim, model, metric, policy, or decision system is in a `D.5` project, release, assurance, or human/group-impact audit condition.


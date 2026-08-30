---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:6.1"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__010_bias-annotation.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:6.1 — Bias-Annotation"
line_start: 69118
line_end: 69126
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

### D.5:6.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Audit as document ritual | A register or report exists but does not change intended use, residuals, or constraints. | Tie each concern to audited EntityOfConcern, intended use, evidence, mitigation, and accepted residual. |
| Metric fairness overclaim | A metric comparison is published as causal or counterfactual fairness. | Recover the fairness claim kind. For counterfactual fairness, require C.28 identification assumptions and estimation consistency when an estimate is used before D.5 consumes the support result. |
| Assurance as authorization | Ethical assurance is treated as permission to proceed. | Record assurance as assurance or evidence relation and keep `D.4` and `D.5` use separate. |
| Bias category replaces object | REP, ALG, VIS, MET, or LNG code is treated as the governed object. | Use codes only as concern locators; keep audited EntityOfConcern and intended use explicit. |


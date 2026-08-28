---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:4"
section_title: "Causal Fairness Boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__007_causal-fairness-boundary.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:4 — Causal Fairness Boundary"
line_start: 68091
line_end: 68100
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

A fairness claim may be associative, interventional, or counterfactual. C.28 supplies the causal-use question, rung, estimand, separate support components, common-threat result, and `CausalUseSupportResultRef`. D.5 keeps the bias/fairness audit and its conclusion.

When counterfactual fairness is consequential, reusable, published, or used for assurance, the cited C.28 components expose the additional counterfactual-identifiability assumptions required for that question. If the audit relies on an estimated fairness result, they also expose the estimate and its estimation-consistency result. Missing identification or consistency lowers the C.28 result to `bounded` or `unsupported`; more of the same data does not repair either gap.

Cite the C.28 result from the existing `BiasAuditReport@Context`. Do not open a separate C.28 fairness card; D.5 defines no such output. Metric-only fallback remains cheaper: when only metric disparity is claimed, record the metric or evaluation result and stop. An interventional proxy may support a bounded interventional fairness statement, but it does not establish counterfactual fairness without the required estimand and support components.

The C.28 result is one evidence basis. It does not certify fairness, approve a release, or supply ethical assurance; D.5 and any downstream decision or assurance pattern make those separate conclusions.


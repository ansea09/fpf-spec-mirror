---
chunk_kind: "child"
pattern_id: "A.3.3.PI"
pattern_title: "Retain the Information Needed for Prediction"
section_id: "A.3.3.PI:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.PI/A.3.3.PI__011_architectural-rationale.md"
commit_sha: "98777b284b6a41fa3481a1230a16182d0f323c2a"
heading_path:
  - "A.3.3.PI — Retain the Information Needed for Prediction"
  - "A.3.3.PI:10 — Architectural Rationale"
line_start: 10280
line_end: 10287
dependencies:
  - "A.3.3"
  - "A.3.3.CC"
  - "A.3.3.TR"
  - "B.5.FM"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.29.1"
keywords:
---

### A.3.3.PI:10 - Architectural Rationale

The independently useful result is a description or uncertainty account that supports a prediction. Configuration construction determines compatible values; rule construction relates their changes. Prediction-information work asks which distinctions from those accounts must remain available for the future question.

That question is shared by physical measurement, mathematical reduction and computational state design. The common construction compares merged cases and repairs a consequential loss. Subject Methods supply physical laws, observability results, estimation techniques and efficient approximations.

A present model state, an observed value, a history and a distribution conditioned on observations carry different information. Keeping their roles explicit permits a compact predictor without claiming that its retained values identify every physical detail. A short-horizon output and an iteratively updated predictive state are also different useful results.


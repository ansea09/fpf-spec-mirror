---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias-Audit & Ethical Assurance"
section_id: "D.5:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__002_problem-frame.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "D.5 — Bias-Audit & Ethical Assurance"
  - "D.5:1 — Problem Frame"
line_start: 49250
line_end: 49255
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

### D.5:1 - **Problem Frame**

FPF is designed to produce reliable, objective, and trustworthy holons. However, formal correctness (`FV` score) and empirical validation (`EV` score) are not sufficient on their own. Any record, model, metric, policy, or decision system designed by humans or trained on human-generated data is susceptible to hidden cognitive, cultural, and algorithmic biases. A perfectly verified control system can still be unsafe if its requirements were based on a biased assumption about operator behavior. A highly accurate machine learning model can be deeply unfair if its training data was not representative.

A fairness claim can also be unsafe by causal overclaim. "This policy is fair because a metric improved" is not the same claim as causal fairness, counterfactual fairness, or path-specific fairness. `D.5` therefore brings causal fairness into the audit entry surface: the audit must distinguish metric disparity, associative fairness evidence, interventional fairness proxy, and counterfactual fairness claim before the ethical assurance record is treated as supported.


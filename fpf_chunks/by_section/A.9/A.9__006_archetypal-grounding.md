---
chunk_kind: "child"
pattern_id: "A.9"
pattern_title: "Choose and Check an Aggregation Law for the Intended Result"
section_id: "A.9:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.9/A.9__006_archetypal-grounding.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "A.9 — Choose and Check an Aggregation Law for the Intended Result"
  - "A.9:5 — Archetypal Grounding"
line_start: 24039
line_end: 24053
dependencies:
  - "A.19.CN"
  - "A.19.ULSAM"
  - "B.1"
  - "B.2"
  - "C.29"
keywords:
  - "aggregation law"
  - "bounds"
  - "cross-scale consistency"
  - "dependency model"
  - "intended result"
  - "ordered composition"
  - "singleton identity"
---

### A.9:5 - Archetypal Grounding

These six cases are constructed model checks, not empirical performance reports. Read each row from the intended result through its model to the warranted answer.

| Intended result and stated model | Selected law, result and limit |
|---|---|
| Total of disjoint exact resource contributions 2 and 3 on one additive quantity scale | Addition gives `2 + 3 = 5` under B.1.6. No weakest-part cap applies to this total; exceeding either part creates no new whole. |
| Probability that both independent components succeed, with probabilities .9 and .8 | The joint-success model selects multiplication: `.9 × .8 = .72`. A minimum would not calculate that probability. |
| Probability that at least one of those same independent components succeeds | The alternative-success model selects `1 - (1-.9)(1-.8) = .98`. Identical marginals and unchanged components support a different law because the intended event changed. |
| Compose `f(x)=x+1` and `g(x)=2x` in the required order | `g(f(x))=2x+2` differs from `f(g(x))=2x+1`. Keep the order; no Characteristic or measurement Scale is required for this function-composition claim. |
| Reorder or repartition disjoint exact additive resource contributions | Exact addition permits the stated reorder and regrouping. That argument establishes neither arbitrary floating-point regrouping nor independence of repeated-source evidence. Check the actual numerical and source conditions when they matter. |
| New evidence defeats independence in the reliability cases, while the assembly retains its identity | Withdraw the .72/.98 computations that used independence. Obtain a justified dependence model or return only a supported bound or the separate marginals. The same assembly remains the subject unless its independent identity rule requires a different conclusion. |

For the additive construction, the singleton base case returns 2 from the one-element input `[2]`. It does not claim `2 + 2 = 2`. Nor does writing the same observation twice create two independent observations.


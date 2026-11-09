---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility and Proxy-to-Value Alignment"
section_id: "E.13:10"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__013_sota-echoing.md"
commit_sha: "b223469ecafb9735c1d9bac220671e3336618339"
heading_path:
  - "E.13 — Pragmatic Utility and Proxy-to-Value Alignment"
  - "E.13:10 — SoTA-Echoing"
line_start: 105223
line_end: 105233
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "E.12"
  - "E.14"
  - "E.19"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
keywords:
  - "Campbell"
  - "Goodhart"
  - "minimally viable value slice"
  - "pragmatic utility"
  - "proxy-to-value alignment"
  - "surrogation"
---

### E.13:10 - SoTA-Echoing

| Claim | Source lineage | Local adoption |
| --- | --- | --- |
| A measure used for decision or control can corrupt the process it monitors. | [Campbell, *Assessing the Impact of Planned Social Change* (1976), pp. 49–52](https://www.humanlearning.systems/uploads/08%20Assessing%20the%20Impact%20of%20Planned%20Social%20Change.pdf), a historical account of indicator pressure and distortion. | `CurrentProxyUse` distinguishes measure, target, incentive, gate, and release argument. |
| Proxy optimization has distinct failure modes. | [Manheim and Garrabrant, *Categorizing Variants of Goodhart's Law* (2018/2019)](https://arxiv.org/abs/1803.04585), distinguishing mechanisms of harmful proxy overoptimization. | `WhatGotWorse` and protected qualities prevent a single proxy from standing for value. |
| Measures can replace the strategic construct in decision makers' minds. | [Choi, Hecht and Tayler, *Lost in Translation* (2012)](https://scholarsarchive.byu.edu/facpub/8208/), on strategy surrogation and incentive compensation. | The proxy is never named as the value; the intended value is named first. |
| Optimizing an imperfect reward or specification can satisfy the formal signal while missing the intended outcome. | [Skalse et al., *Defining and Characterizing Reward Hacking* (2022)](https://arxiv.org/abs/2209.13085), a formal treatment of proxy and true reward divergence under stated policy assumptions. | Evaluation values, judge scores, and all-`5` posture are treated as proxies that require value-slice and protected-quality checks. |
| Useful measures should be derived from goals and questions. | [Basili, Caldiera and Rombach, *The Goal Question Metric Approach*](https://www.cs.umd.edu/~mvz/handouts/gqm.pdf), deriving measurement from goals, questions and interpretation context. | E.13 asks for intended value/objective before proxy and asks which decision or work the proxy affects. |
| Human values require stakeholder and use-context inquiry, not only formal metrics. | [Value Sensitive Design's tripartite methodology](https://vsdesign.org/vsd/), connecting stakeholder values with conceptual, empirical and technical investigations. | The minimally viable value slice may include user, operator, manager, safety, or affected-stakeholder evidence when those values are live. |


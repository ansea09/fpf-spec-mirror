---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility and Value Alignment"
section_id: "E.13:10"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__013_sota-echoing.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "E.13 — Pragmatic Utility and Value Alignment"
  - "E.13:10 — SoTA-Echoing"
line_start: 68677
line_end: 68687
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
| A measure used for decision or control can corrupt the process it monitors. | Goodhart and Campbell indicator-pressure lines. | `CurrentProxyUse` distinguishes measure, target, incentive, gate, and release argument. |
| Proxy optimization has distinct failure modes. | Manheim/Garrabrant Goodhart variants and later proxy-failure work. | `WhatGotWorse` and protected qualities prevent a single proxy from standing for value. |
| Measures can replace the strategic construct in decision makers' minds. | Management-accounting surrogation work by Choi, Hecht, Tayler, and later studies. | The proxy is never named as the value; the intended value is named first. |
| Optimizing an imperfect reward or specification can satisfy the formal signal while missing the intended outcome. | AI safety specification-gaming and reward-hacking work, including formal reward-hacking analyses and current reasoning-model specification-gaming evaluations. | Evaluation values, judge scores, and all-`5` posture are treated as proxies that require value-slice and protected-quality checks. |
| Useful measures should be derived from goals and questions. | Goal-Question-Metric and GQM+Strategies measurement alignment. | E.13 asks for intended value/objective before proxy and asks which decision or work the proxy affects. |
| Human values require stakeholder and use-context inquiry, not only formal metrics. | Value Sensitive Design and value-oriented design lines. | The minimally viable value slice may include user, operator, manager, safety, or affected-stakeholder evidence when those values are live. |


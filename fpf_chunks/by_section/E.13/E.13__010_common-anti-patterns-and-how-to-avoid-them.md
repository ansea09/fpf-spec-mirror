---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility and Value Alignment"
section_id: "E.13:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "886e84cadcc302e1c622aec02a0a0ba1e1c3955d"
heading_path:
  - "E.13 — Pragmatic Utility and Value Alignment"
  - "E.13:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 80941
line_end: 80951
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

### E.13:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Score as value | A higher score is reported as practical improvement. | Name intended value, proxy use, and value slice. |
| All-`5` targeting | A pattern or DRR is rewritten to make every coordinate defensible as `5`. | Use the evaluation as measurement; repair content movement and protected trade-offs. |
| Source-count proof | More citations or source rows are treated as better decision quality. | Ask which decision payload changed. |
| Dashboard myopia | A visible dashboard metric improves while unmeasured harm rises. | Add protected qualities and split measure from value. |
| Proxy as gate authority | A proxy is treated as authority for release or gate passage without satisfying the rule that governs that decision. | Apply the governing release rule for release, `A.21` for gate passage, and `B.3` for an assurance claim; keep proxy use bounded. |
| Value slice missing | Practical payoff is asserted but never shown in a case. | Add a minimally viable value slice or lower the payoff claim. |


---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__011_rationale.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:9 — Rationale"
line_start: 72118
line_end: 72123
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.11"
  - "E.19"
  - "E.2.DA"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.21:9 - Rationale

`E.21` keeps the measuring device simple: one object kind, one ordinal scale, one required coordinate set, one status set, and one stop condition. The evaluation never asks whether a coordinate is active. It asks what value the current pattern and its named evidence basis earn under the declared use.

The mature-pattern parity coordinate is deliberately strict because recent short patterns looked formally clean while lacking the worked slices, source carry-through, lowering conditions, and transfer coverage present in mature FPF patterns. The repair is not "make everything long"; it is "carry the selected mature ingredients that the declared use needs."


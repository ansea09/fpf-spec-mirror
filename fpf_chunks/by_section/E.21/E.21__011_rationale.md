---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__011_rationale.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:9 — Rationale"
line_start: 87667
line_end: 87672
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.1"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.11"
  - "E.19"
  - "E.2.DA"
  - "E.21"
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

`E.21` keeps the declared measurement structure simple: one checked-object class, one ordinal scale, one required coordinate set, one non-arithmetic `PatternQualityQBundle` result payload, one local status set, and one stop-condition form. The specification marks no coordinate inactive; an evaluator applies them all, and the result episteme states what value the exact checked pattern edition and named evidence basis support under the declared use.

The mature-pattern parity coordinate is deliberately strict because recent short patterns looked formally clean while lacking the worked slices, source carry-through, lowering conditions, and transfer coverage present in mature FPF patterns. The repair is not "make everything long"; it is "carry the selected mature ingredients that the declared use needs."


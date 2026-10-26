---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Indicatorization (UINDM): Select Indicators Under a Declared Policy"
section_id: "A.19.UINDM:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__012_rationale.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.19.UINDM — Indicatorization (UINDM): Select Indicators Under a Declared Policy"
  - "A.19.UINDM:10 — Rationale"
line_start: 37817
line_end: 37825
dependencies:
keywords:
  - "CHR suite stage indicatorize"
  - "CN-Spec.indicator_policy"
  - "IndicatorChoicePolicy"
  - "indicator set"
  - "indicatorization"
  - "tri-state admissibility (pass"
---

### A.19.UINDM:10 - Rationale

Indicatorization is separated because it answers a different question from scoring or comparison:

* Indicatorization determines **which coordinates may be used** under the indicator-selection policy.
* Scoring, aggregation, and comparison determine **how** those coordinates are transformed, combined, or ordered under their admissibility conditions.

By making indicatorization selection‑only, UINDM avoids “semantic alchemy” (changing meanings while claiming to merely “pick indicators”) and supports the CHR suite’s broader discipline: explicit specification references, any actually used crossing relations, and explicit handling of uncertainty via tri‑state guards.


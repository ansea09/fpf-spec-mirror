---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Indicatorization (UINDM): Select Indicators Under a Declared Policy"
section_id: "A.19.UINDM:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__012_rationale.md"
commit_sha: "73e53b7b1a40aae81d6871f327e5bf7b1c495e23"
heading_path:
  - "A.19.UINDM — Indicatorization (UINDM): Select Indicators Under a Declared Policy"
  - "A.19.UINDM:10 — Rationale"
line_start: 38529
line_end: 38537
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

By making indicatorization selection‑only, UINDM avoids “semantic alchemy” (changing meanings while claiming to merely “pick indicators”) and supports the CHR suite’s broader discipline: explicit spec refs, explicit crossings, and explicit handling of uncertainty via tri‑state guards.


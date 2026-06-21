---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Unified Indicatorization Mechanism (UINDM)"
section_id: "A.19.UINDM:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__012_rationale.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.19.UINDM — Unified Indicatorization Mechanism (UINDM)"
  - "A.19.UINDM:10 — Rationale"
line_start: 27786
line_end: 27794
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

Indicatorization is separated because it is a different kind of commitment than scoring or comparison:

* Indicatorization commits to **which coordinates are allowed to matter** under policy.
* Scoring/aggregation/comparison commit to **how** allowed coordinates are transformed, folded, or ordered under admissibility gates.

By making indicatorization selection‑only, UINDM avoids “semantic alchemy” (changing meanings while claiming to merely “pick indicators”) and supports the CHR suite’s broader discipline: explicit spec refs, explicit crossings, and explicit handling of uncertainty via tri‑state guards.


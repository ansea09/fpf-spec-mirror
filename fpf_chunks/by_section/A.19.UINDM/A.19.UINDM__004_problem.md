---
chunk_kind: "child"
pattern_id: "A.19.UINDM"
pattern_title: "Indicatorization (UINDM): Select Indicators Under a Declared Policy"
section_id: "A.19.UINDM:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UINDM/A.19.UINDM__004_problem.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.19.UINDM — Indicatorization (UINDM): Select Indicators Under a Declared Policy"
  - "A.19.UINDM:2 — Problem"
line_start: 37589
line_end: 37597
dependencies:
keywords:
  - "CHR suite stage indicatorize"
  - "CN-Spec.indicator_policy"
  - "IndicatorChoicePolicy"
  - "indicator set"
  - "indicatorization"
  - "tri-state admissibility (pass"
---

### A.19.UINDM:2 - Problem

Engineering teams routinely need to decide “which characteristics count as indicators” for a CN‑frame—when a downstream score, comparison, aggregation or selection depends on that choice. Leaving the choice implicit can produce these failures:

* **Hidden indicatorization:** downstream mechanisms (scoring/comparison/selection) implicitly decide which characteristics matter, making the CHR pipeline opaque and hard to audit.
* **NCV conflation:** measurability (or “having an NCV”) is treated as sufficient to be an indicator, collapsing the crucial distinction between “measurable characteristic” and “indicator chosen under policy.”
* **Drift and non-determinism:** indicator sets vary between teams, bearer classes, source or corpus editions, windows, and intended uses without stable policy and basis pins, making comparisons and decisions irreproducible.
* **Silent evidence coercion:** missing/unknown evidence is implicitly treated as acceptable (“pass”) or collapsed to an empty set, degrading decision quality without visibility.


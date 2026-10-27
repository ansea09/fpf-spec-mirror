---
chunk_kind: "child"
pattern_id: "A.18"
pattern_title: "Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
section_id: "A.18:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.18/A.18__008_conformance-checklist.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.18 — Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
  - "A.18:7 — Conformance Checklist"
line_start: 34365
line_end: 34385
dependencies:
  - "A.17"
  - "A.19"
  - "A.19.CHR"
  - "A.19.CN"
  - "B.3"
  - "C.16"
  - "G.0"
keywords:
  - "CSLC"
  - "Characteristic"
  - "Coordinate"
  - "Level"
  - "Scale"
  - "lawful comparability"
  - "measurement interpretability"
  - "no illegal averaging"
  - "one-characteristic-one-scale rule"
  - "ordinal vs cardinal scale"
  - "scale order"
  - "use-dependent preference"
---

### A.18:7 - Conformance Checklist

When defining a new metric template or using measurements, practitioners **SHALL** verify the following:

1.  **One characteristic, one scale:** Each metric **template** binds exactly **one Characteristic** to exactly **one Scale**. If you find a metric trying to cover multiple things at once, split it into separate metrics.

2. **Order and preference:** Is the Scale's order interpretable for the Characteristic? When the use judges which value is preferable, is that preference stated? A descriptive magnitude comparison requires only the measurement interpretation. A target-based evaluation states its target and how deviations are compared.

3. **Unit and Level clarity:** State the applicable Unit or dimensionless-value convention and make it recoverable for each quantitative value. Define named Levels within their Scale. A label may occur on different Scales, but the receiving use must be able to recover which meaning applies. Keep the Unit separate from the Characteristic name.

4.  **Scale-appropriate operations only:** Only perform those comparisons or calculations that are valid for the given scale type. For a nominal scale, the Scale supplies equality but no intrinsic order; a use-dependent preference is a separate rule. For an ordinal Scale, its order alone does not justify arithmetic differences between numerical labels. For interval scales, an operation must respect the Scale's admissible changes of origin and unit; differences and appropriate means can be meaningful, while ratios of raw values generally are not. For ratio scales, ratios are meaningful, but further calculation still needs the applicable quantity or scoring relation and its conditions, with compatible units. For example, encoding High as 3 and Medium as 2 supplies no interpretation of their mean, 2.5.

5.  **No bare numbers:** Never present a raw number or value without its context of Characteristic and Scale. If someone sees “42” in your output, they should _also_ see or know “42 of what, measured how.” A reader who is not aware of the metric’s template should not be left guessing what a given value signifies. In practice, this means labeling reports and data with the metric name or identifier so that values can be traced back to their meaning.

6. **Cross-template operations:** For a conversion, recover the relation between compatible Scales, including units. For a quantity calculation, recover the model and its conditions under C.16. For an evaluative comparison or combination, state the ScoringMethod, its preference under A.17-R7 and its bounded Score output range. For example, converting 0.5 minutes to 30 seconds preserves duration; combining cost and reliability into a score needs an evaluation rule.

7.  **Level optionality respected:** If your Characteristic doesn’t naturally have tiers, don’t force it to have **Level** names (you can leave the Level concept unused). Conversely, if your Characteristic is commonly described in categories, it’s fine to define Levels for clarity. The key is to use the Level field intentionally: either not at all (for truly continuous measures) or in a fixed, **non-overlapping** way (for discrete categories). Do not use “Level” for something that behaves like a continuous value (it would be confusing to assign a label where a number would do, or vice versa).
8. **Comparability test:** For a direct magnitude comparison, use the same Characteristic and Scale, with compatible measurement conditions under C.16. A declared conversion can establish that common basis. A preference judgement additionally uses its declared preference; changing that preference alone does not change the measurement Scale.

A.17 and E.10 supply the vocabulary. A template can expose missing fields; it does not establish that the declared meanings, measurement model or resulting inference are adequate.


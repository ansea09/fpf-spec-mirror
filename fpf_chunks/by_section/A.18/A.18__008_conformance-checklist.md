---
chunk_kind: "child"
pattern_id: "A.18"
pattern_title: "CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
section_id: "A.18:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.18/A.18__008_conformance-checklist.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.18 — CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
  - "A.18:7 — Conformance Checklist"
line_start: 36008
line_end: 36028
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

1. **One Characteristic, one Scale:** Each metric template binds exactly one Characteristic to exactly one Scale. Keep different reported Characteristics in separate templates. A calculated quantity or composite Score may use multiple inputs under §4.2.

2. **Order and preference:** Is the Scale's order interpretable for the Characteristic? When the use judges which value is preferable, is that preference stated? A descriptive magnitude comparison requires only the measurement interpretation. A target-based evaluation states its target and how deviations are compared.

3. **Unit and Level clarity:** State the applicable Unit or dimensionless-value convention and make it recoverable for each quantitative value. Define named Levels within their Scale. A label may occur on different Scales, but the receiving use must be able to recover which meaning applies. Keep the Unit separate from the Characteristic name.

4.  **Scale-appropriate operations only:** Only perform those comparisons or calculations that are valid for the given scale type. For a nominal scale, the Scale supplies equality but no intrinsic order; a use-dependent preference is a separate rule. For an ordinal Scale, its order alone does not justify arithmetic differences between numerical labels. For interval scales, an operation must respect the Scale's admissible changes of origin and unit; differences and appropriate means can be meaningful, while ratios of raw values generally are not. For ratio scales, ratios are meaningful, but further calculation still needs the applicable quantity or scoring relation and its conditions, with compatible units. For example, encoding High as 3 and Medium as 2 supplies no interpretation of their mean, 2.5.

5.  **No bare numbers:** Never present a raw number or value without its context of Characteristic and Scale. A reader seeing “42” should be able to recover “42 of what, measured how,” even without knowing the metric’s template. Label reports and data with the metric name or identifier so values can be traced back to their meaning.

6. **Cross-template operations:** For a conversion, recover the relation between compatible Scales, including units. For a quantity calculation, recover the model and its conditions under C.16. For an evaluative comparison or combination, state the ScoringMethod, its preference under A.17-R7 and its Score Scale and output range, including any required bounds. For example, converting 0.5 minutes to 30 seconds preserves duration; combining cost and reliability into a score needs an evaluation rule.

7. **Level optionality:** Use named Levels when they help express the selected Scale's discrete values or non-overlapping categories. Define the categories and their boundaries; leave Level unused for an uncategorized continuous measurement.
8. **Comparability test:** For a magnitude comparison, use the same Characteristic and Scale, with compatible measurement conditions under C.16. A declared conversion can establish that common basis. A preference judgement additionally uses its declared preference; changing that preference alone does not change the measurement Scale.

A.17 and E.10 supply the vocabulary. A template can expose missing fields; it does not establish that the declared meanings, measurement model or resulting inference are adequate.


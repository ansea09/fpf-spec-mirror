---
chunk_kind: "child"
pattern_id: "A.18"
pattern_title: "Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
section_id: "A.18:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.18/A.18__008_conformance-checklist.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.18 — Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
  - "A.18:7 — Conformance Checklist"
line_start: 29876
line_end: 29896
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CN"
  - "B.3"
  - "C.16"
  - "D.4"
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

3.  **Unit and level clarity:** If the Scale is quantitative, specify the **Unit** (e.g. _seconds, meters, %_) and make sure all values include or assume that unit. If the Scale has named Levels, list them clearly and use them consistently. Do **not** use the same label to mean different things on different scales, and avoid using unit terms in Characteristic names (the unit belongs with the scale).

4.  **Scale-appropriate operations only:** Only perform those comparisons or calculations that are valid for the given scale type. For a nominal scale, you can check equality but not order. For an ordinal scale, you can order or rank values but not do math like “A minus B.” For interval scales, addition/subtraction is OK (with unit conversion if needed), but ratio comparisons (A is twice B) might not make sense without a true zero. For ratio scales, all arithmetic operations are allowed _with proper attention to units_. This check prevents logical errors (e.g. averaging “High” (3) and “Medium” (2) and getting 2.5 — which is meaningless).

5.  **No bare numbers:** Never present a raw number or value without its context of Characteristic and Scale. If someone sees “42” in your output, they should _also_ see or know “42 of what, measured how.” A reader who is not aware of the metric’s template should not be left guessing what a given value signifies. In practice, this means labeling reports and data with the metric name or identifier so that values can be traced back to their meaning.

6. **Cross-template operations:** For a conversion, recover the relation between compatible Scales, including units. For a quantity calculation, recover the model and its conditions under C.16. For an evaluative combination, state the ScoringMethod and preference under A.17-R7. For example, converting 0.5 minutes to 30 seconds preserves duration; combining cost and reliability into a score needs an evaluation rule.

7.  **Level optionality respected:** If your Characteristic doesn’t naturally have tiers, don’t force it to have **Level** names (you can leave the Level concept unused). Conversely, if your Characteristic is commonly described in categories, it’s fine to define Levels for clarity. The key is to use the Level field intentionally: either not at all (for truly continuous measures) or in a fixed, **non-overlapping** way (for discrete categories). Do not use “Level” for something that behaves like a continuous value (it would be confusing to assign a label where a number would do, or vice versa).
8. **Comparability test:** For a direct magnitude comparison, use the same Characteristic and Scale, with compatible measurement conditions under C.16. A declared conversion can establish that common basis. A preference judgement additionally uses its declared preference; changing that preference alone does not change the measurement Scale.

_(The above serve as normative checkpoints. Many of these are automatically supported by using the standard metric templates in software: e.g. the system will enforce one Characteristic per template, require a unit for ratio scales, etc. The **Lexical rules** from A.17/E.10 are assumed: use canonical names and notations for all parts of the metric.)_


---
chunk_kind: "child"
pattern_id: "A.18"
pattern_title: "Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
section_id: "A.18:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.18/A.18__004_forces.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "A.18 — Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
  - "A.18:3 — Forces"
line_start: 34337
line_end: 34348
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

### A.18:3 - Forces

- **F1 — Disciplinary interpretation.** Physical measurements and human assessments can use the same structural distinctions while retaining their different domain assumptions and methods.

- **F2 — Comparability and alternative Scales.** Compare values under a common Characteristic and Scale with compatible conditions under C.16. The same Characteristic may use different Scales, such as temperature in Celsius or Kelvin; use a declared conversion when the comparison needs a common Scale.

- **F3 — Scale integrity.** Retain the distinction between category, order, interval and ratio structure. Numerical labels alone establish neither distances nor admissible arithmetic.

-   **F4 – Named tiers vs. continuous magnitudes.** In many domains, **named Levels** (tiers or grades) are useful – e.g. Technology Readiness Levels or bond credit ratings – whereas in others, a continuous scale is needed. The pattern should support **optional Level labels** (for tiered scales) _without forcing_ every scale to have such labels. In other words, Levels are an add-on for discrete/tiered scales, not a requirement for truly continuous measures.

-   **F5 – Method agnosticism.** The kernel Standard should say _what_ must be defined (Characteristic, Scale, etc.) but **not prescribe how measurements are obtained**. Whether a value comes from a sensor reading, a simulation, or an expert judgment is up to the respective patterns (e.g. Sys-CAL vs. KD-CAL). The pattern must not bake in any process or scoring methodology; it types the reported values, while C.16 and the receiving use supply the further measurement and comparability conditions. This avoids locking in any particular assessment method.


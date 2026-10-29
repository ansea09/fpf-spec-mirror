---
chunk_kind: "child"
pattern_id: "A.18"
pattern_title: "Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
section_id: "A.18:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.18/A.18__003_problem.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "A.18 — Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)"
  - "A.18:2 — Problem"
line_start: 34327
line_end: 34336
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

### A.18:2 - Problem

**Uninterpretable measurements.** A reported “4”, “High” or “9.81” needs its Characteristic, Scale and measurement conditions to be interpreted as a measurement. Across disciplines, “5” could encode an ordinal risk rank, a length in meters or a satisfaction assessment under a stated model. Common failures include:

- In an ordinal Scale such as _Novice < Skilled < Expert_, the order is meaningful; assigning 1 and 3 to its labels supplies no distance that would justify their arithmetic mean.

- Interval and ratio calculations require compatible units, the Scale's transformation rules and the relation being calculated. Combining seconds and minutes requires conversion; a ratio calculation also depends on the meaning of zero.

A practitioner needs the measured aspect, its Scale and the rule for the proposed operation. Otherwise equal numerical encodings can hide incompatible meanings, such as a 4-star rating and 4 seconds. Qualitative tiers need no invented distances between their labels.


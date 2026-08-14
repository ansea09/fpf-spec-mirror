---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:6"
section_title: "Scale-type admissibility quick reference (Informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__007_scale-type-admissibility-quick-reference-informative.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:6 — Scale-type admissibility quick reference (Informative)"
line_start: 47506
line_end: 47526
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16.P"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "G.11"
  - "G.4"
  - "G.6"
keywords:
  - "C.2.1 result episteme"
  - "Characteristic"
  - "Level/Coordinate"
  - "Scale"
  - "Unit"
  - "actual bindings"
  - "bounded later use"
  - "calibration"
  - "comparability"
  - "dated measurement work"
  - "input/output quantities"
  - "measurand"
  - "measurement result"
  - "measurement subject"
  - "method"
  - "model"
  - "polarity"
  - "provenance"
  - "uncertainty"
---

### C.16:6 - Scale-type admissibility quick reference (Informative)

> **Didactic note.** This table is a memory aid for engineers and managers. It does **not** introduce new admissibility rules. Normative admissibility of operations by scale type is governed by **A.18 (CSLC)** and, where mechanized in CG‑frames, by the relevant admissibility profiles.
> If any row below conflicts with A.18, treat it as an illustrative example and follow A.18.

| Scale type   | Comparisons    | Location          | Differences        | Ratios                   | Admissible summaries                                  | Typical unsupported anti-patterns                                   |
| ------------ | -------------- | ----------------- | ------------------ | ------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------- |
| **Nominal**  | =, ≠           | mode, frequencies | —                  | —                        | counts, proportions                                   | averaging labels; ordering categories without a declared order      |
| **Ordinal**  | <, =, > (rank) | median, quantiles | **not meaningful** | —                        | order‑respecting summaries (median rank, percentiles) | arithmetic mean of ranks; variance on ranks; linear blends of ranks |
| **Interval** | <, =, >        | mean location     | Δ meaningful       | ratio **not** meaningful | mean, sd of **differences**, correlation              | ratio claims (“twice as hot” in °C); geometric mean                 |
| **Ratio**    | <, =, >        | mean location     | Δ meaningful       | ratios meaningful        | arithmetic/geometric means, cv, growth rates          | adding heterogeneous units; log on nonpositive values               |

**Reminders (informative; see A.18 for normative rules).**
G‑1 (Order). On ordinal, transforms should be **monotone**.
G‑2 (Differences). On interval or ratio, **Δ** is meaningful; on ordinal or nominal, it is undefined.
G‑3 (Ratios). Only ratio Scales admit **x/y** semantics; interval, ordinal, or nominal do not.
G‑4 (Unit coherence). Interval or ratio arithmetic presumes compatible units (or a declared conversion).
G‑5 (Target polarity). If polarity is targeted, comparisons use distance‑from‑target semantics as declared by the relevant subject pattern, template, and cited method or mechanism.

*(These rules line up with the MM‑CHR exposition of CSLC and term discipline; A.17 fixes the lexical side.)*


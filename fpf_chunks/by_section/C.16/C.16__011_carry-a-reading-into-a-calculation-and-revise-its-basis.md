---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:12"
section_title: "Carry a reading into a calculation and revise its basis"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__011_carry-a-reading-into-a-calculation-and-revise-its-basis.md"
commit_sha: "4e277189a17b8f9bd3dcdda5df58623d9085ede9"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:12 — Carry a reading into a calculation and revise its basis"
line_start: 58825
line_end: 58832
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
  - "Scale order"
  - "Unit"
  - "actual bindings"
  - "bounded later use"
  - "calibration"
  - "comparability"
  - "dated measurement work"
  - "indication-producing procedure"
  - "input/output quantities"
  - "measurand"
  - "measurement result"
  - "measurement subject"
  - "measurement-model construction"
  - "method"
  - "model"
  - "provenance"
  - "uncertainty"
---

### C.16:12 - Carry a reading into a calculation and revise its basis

A retained account attributes temperature `20 °C ± 1 °C` to Pump P over window W under a named specification and model; the interval is a bound for this example. Its content is a `ReadingContent` member. Relying on it as a measurement result still needs the performed-measurement and uncertainty grounds above. The Coordinate 20 on the Celsius Scale, the interval, the reading content and an episteme stating that content answer different questions.

A declared scoring rule reads that Celsius position and assigns `g(c)=c/40` on `[0,40]`, with higher temperature preferred in this illustrative use. With the required admission grounds, it returns score content for P at W: `0.5`, bounded by `[0.475,0.525]` under this interval-propagation rule. That content can pass to a comparator accepting this score Scale and bound. The scoring calculation supplies no second temperature measurement. If an upstream UNM instead supplies `293.15 K`, the number cannot fill the Celsius argument. Apply the declared inverse conversion, or select a kelvin-input scoring rule whose correspondence is established.

Now comparison of the written model and calibration record reveals that the measurement needs a `+2 °C` correction not included before. The corrected account attributes `[21,23] °C`, and this same scoring rule gives `[0.525,0.575]`. Recover whether the specification already permitted this calibrated correction or must itself change. Preserve the earlier assertion and its basis, then reconsider the scores and comparisons that relied on it. A new window W2 instead needs a new attribution for W2; it can leave the Characteristic, Scale, specification and scoring rule unchanged. These returns follow from the general identity and replacement rules, not from the displayed numbers alone.


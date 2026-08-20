---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:11"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:11 — Common Anti-Patterns and How to Avoid Them"
line_start: 47278
line_end: 47287
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

### C.16:11 - Common Anti-Patterns and How to Avoid Them

- **Template as occurrence.** A reusable `U.DHCMethod`, model, signature, or calibration procedure is treated as proof that work occurred. Ground dated work and actual bindings.
- **Generic result field.** A record has `result=...` without saying whether it is output, indication, measurement result, diagnosis, verdict, or decision. Name the direct result kind and governor.
- **Evidence algebra.** Evidence locators are unioned as though idempotence or count determined uncertainty or warrant. Use measurement-model uncertainty propagation and exact A.10/B.3 reliance separately.
- **Scale drift.** A template id survives changed Scale, model, unit, or calibration semantics. Publish a successor and state the relation; do not mutate historical readings.
- **Arithmetic on ordinal.** Encoded levels are averaged or ratio-compared. Stay with order-preserving operations or introduce a separately governed scoring method and Scale.
- **Multi-Characteristic stuffing.** One reading carries a vector while pretending to be one measurement. Create separate results and declare any later aggregation.
- **Result-to-verdict shortcut.** A value inside a tolerance is called accepted without performed criterion evaluation. Ground the separate evaluation work, exact clause application, verdict episteme, and later decision.


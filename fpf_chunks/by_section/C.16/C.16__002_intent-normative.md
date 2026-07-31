---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:1"
section_title: "Intent (Normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__002_intent-normative.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:1 — Intent (Normative)"
line_start: 47149
line_end: 47162
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

### C.16:1 - Intent (Normative)

**Name.** *Measurement & Metrics Characterization (MM‑CHR).*

**Use this when.** Use C.16 when a reading, score, rating, sensor indication, dashboard value, or claimed comparison must be made interpretable as a measurement. The working question is: what exact subject or measurand was measured, for which Characteristic and Scale, by which method and model, under which calibration and time stance, with what attributed value and uncertainty?

**What changes in practice.** Instead of carrying a number and a source link, the practitioner recovers a complete measurement chain: reusable specification, exact measurand, method, model, calibration basis, input and output quantities, dated measurement work, direct bindings, measurement result, one result episteme, and provenance. A reader can then tell what the reading supports and what still requires a diagnostic, criterion, assurance, causal, acceptance, or decision pattern.

**Not this pattern when.** Use A.17 for the Characteristic, A.18 for scale-operation legality, C.16.P while measurement wording is still ambiguous, A.19 for comparison or selection, C.28 for causal use, A.10/G.6 for provenance, B.3 for assurance, G.4 for an acceptance declaration, G.11 for currentness, and C.11 for a decision result. C.16 supplies none of those results by implication.

**Local designators.** `MeasurementSpecification`, `MeasurementMethod`, `MeasurementModel`, `MeasurementWork`, `MeasurementResult`, and `MeasurementResultEpisteme` name exact objects in one case; they are not new public U-kinds or universal relation types. `MeasurementMethod` is one exact `U.Method`; `MeasurementWork` is one dated `U.Work`; `MeasurementResultEpisteme` is one C.2.1 episteme.

**Compatibility with the retained measurement family.** `U.DHCMethod` remains the durable measurement-definition value that fixes the Characteristic, Scale, unit and polarity and cites the exact method and model. `U.Measure` remains the durable reading claim: when persisted, it is the C.2.1 result episteme that states the C.16 measurement result. `U.Unit` carries quantity-kind and conversion semantics when the Scale requires them. `U.EvidenceStub` is only a compact locator into A.10/G.6 provenance; it is not the measurement result, an evidence carrier, a work record, or a relation that establishes measurement.


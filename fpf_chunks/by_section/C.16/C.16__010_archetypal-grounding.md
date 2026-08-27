---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:8.3"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__010_archetypal-grounding.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:8.3 — Archetypal Grounding"
line_start: 47329
line_end: 47336
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

### C.16:8.3 - Archetypal Grounding

**Calibrated detector receiver.** The detector emits raw counts. Its processing yields an indication of `41.8 kPa`. The measurand is gas pressure at port P over the stated sampling window; Characteristic is Pressure; Scale is a ratio quantity scale; Unit is kPa. Measurement model `PressureModel-4` uses counts, reference offset, temperature, and calibration coefficients as inputs and pressure as output. Dated measurement work names its performer, detector, port, resources, bindings, calibration basis, and uncertainty propagation. The C.16 result attributes `41.8 kPa ± 0.6 kPa` to the measurand under that basis; one C.2.1 episteme states it. The raw counts, displayed indication, actual pressure, result episteme, a later leak diagnosis, and a pressure-limit verdict remain different objects.

**Internal-combustion-engine test bench.** One dated test-bench work occurrence binds the engine, dynamometer, fuel batch, ambient conditions, method, model, and calibration records. Torque, exhaust temperature, and emissions are three Characteristics with separate Scales and result epistemes; their input quantities, output quantities, covariance where relevant, and uncertainties remain separately recoverable. Aggregation work may later construct a declared performance summary, and evaluation work may apply an emissions criterion. Neither the summary nor the pass/fail verdict is the torque or emissions measurement result.

**Architecture coupling.** The measurand is the exact ordered module pair under a declared dependency census window, not either module alone. The Characteristic is Coupling on an ordinal Scale. The method description defines generic dependency classes; dated work binds the actual codebase edition and pair. The result episteme states the Level and basis. A later release decision may rely on it, but the dashboard tile and decision record do not establish the census work.


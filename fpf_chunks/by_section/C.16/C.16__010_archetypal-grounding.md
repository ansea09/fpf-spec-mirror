---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:8.3"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__010_archetypal-grounding.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:8.3 — Archetypal Grounding"
line_start: 49683
line_end: 49708
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

### C.16:8.3 - Archetypal Grounding

**Calibrated detector receiver.** The detector emits raw counts. Its processing yields an indication of `41.8 kPa`. The measurand is gas pressure at port P over the stated sampling window; Characteristic is Pressure; Scale is a ratio quantity scale; Unit is kPa. Measurement model `PressureModel-4` uses counts, reference offset, temperature, and calibration coefficients as inputs and pressure as output. Dated measurement work names its performer, detector, port, resources, bindings, calibration basis, and uncertainty propagation. The C.16 result attributes `41.8 kPa ± 0.6 kPa` to the measurand under that basis; one C.2.1 episteme states it. The raw counts, displayed indication, actual pressure, result episteme, a later leak diagnosis, and a pressure-limit verdict remain different objects.

**Internal-combustion-engine test bench.** One dated test-bench work occurrence binds the engine, dynamometer, fuel batch, ambient conditions, method, model, and calibration records. Torque, exhaust temperature, and emissions are three Characteristics with separate Scales and result epistemes; their input quantities, output quantities, covariance where relevant, and uncertainties remain separately recoverable. Aggregation work may later construct a declared performance summary, and evaluation work may apply an emissions criterion. Neither the summary nor the pass/fail verdict is the torque or emissions measurement result.

**Architecture coupling.** The measurand is the exact ordered module pair under a declared dependency census window, not either module alone. The Characteristic is Coupling on an ordinal Scale. The method description defines generic dependency classes; dated work binds the actual codebase edition and pair. The result episteme states the Level and basis. A later release decision may rely on it, but the dashboard tile and decision record do not establish the census work.

#### C.16:8.3.1 - A voltmeter changes the voltage it reads

The sought quantity is the open-circuit voltage E of a source. Model the source as an ideal voltage E in series with resistance R_s; the connected voltmeter has input resistance R_m. The meter closes the circuit. Ohm's law gives current I=E/(R_s+R_m), and the indication is V=I R_m. The measurement relation is therefore E=V(1+R_s/R_m).

For E=10 V and R_s=R_m=1 megohm, the indication is 5 V. The known resistance ratio recovers the open-circuit value as 10 V. The difference comes from the measurement interaction.

If both E and R_s are unknown, one indication leaves several pairs compatible with it. For V=5 V, R_m=1 megohm and an available bound 0.8≤R_s≤1.2 megohm, the conditional voltage interval is 9≤E≤11 V. That interval may answer the question. When a narrower answer is needed, a second indication with a different known input resistance supplies another equation, provided the source stays unchanged and the circuit model still applies. Repeating the original arrangement supplies the same relation and leaves this ambiguity.

These calculations use an ideal circuit. For an obtained measurement result, include uncertainty in the indications and resistances and any model inadequacy that affects the use.

#### C.16:8.3.2 - Interpreting an assessment of independent performance

The sought quantity p is the fraction of a population able to perform a specified action independently under stated conditions. An applicable assessment calibration supplies a, the probability of a positive test when the capability is present, and b, the probability when it is absent. Partitioning the population by that capability gives the expected positive fraction q=ap+b(1-p).

With a=0.9 and b=0.1, the relation is q=0.1+0.8p. An observed positive fraction 0.7 gives the estimate p=0.75 under this model. Sampling uncertainty, uncertainty in the calibrated rates and their applicability determine how precisely that estimate can be used. When a=b, the expected positive fraction is independent of p, so this test supplies no such distinction.

Now allow hints during the assessment. The earlier a and b may no longer describe the procedure. With the changed rates unknown, the positive fraction alone no longer determines p. If the independent-performance claim is still needed, return to that performance condition or obtain a calibration applicable to the changed procedure. The model explains which inference is available; it uses the subject's account of the capability and its assessment.


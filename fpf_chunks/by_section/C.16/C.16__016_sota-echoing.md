---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:14.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__016_sota-echoing.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:14.1 — SoTA-Echoing"
line_start: 57901
line_end: 57916
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

### C.16:14.1 - SoTA-Echoing

These sources contribute different parts of measurement interpretation. Their quantity, model and observation concepts retain their source meanings; correspondence to an FPF concept requires F.9 only when the use depends on that semantic mapping.

| Source | Measurement contribution | Use boundary |
| --- | --- | --- |
| [JCGM 200:2012, VIM3, entry 2.9](https://jcgm.bipm.org/vim/en/2.9.html) | A measurement result comprises attributed values with the relevant information needed to interpret them. | An indication, raw output, actual subject state, diagnosis, verdict or decision has a different role in the measurement and its use. |
| [JCGM GUM-6:2020, *Developing and using measurement models*](https://doi.org/10.59161/JCGMGUM-6-2020) | Model construction and adequacy connect actual inputs, output quantity, assumptions, calibration, covariance and uncertainty propagation within a validity domain. | Model input/output roles are not universal Work relations. A formula does not establish performed measurement work; more provenance pointers do not reduce uncertainty. |
| [ISO 80000-1:2022, *Quantities and units — Part 1: General*](https://www.iso.org/standard/76921.html) and [ISO/IEC 25024:2015, *Measurement of data quality*](https://www.iso.org/standard/35749.html) | Quantity, unit and data-quality-measure definitions can supply the terms used by a measurement. | A standard label alone establishes neither Scale-compatible arithmetic nor comparability, acceptance or a C.16 result. |
| [QUDT Schema 3.4.0, June 2026 catalogue](https://www.qudt.org/catalog/qudt-catalog.html) | Citable identifiers distinguish quantity kinds, units, dimensions and datatypes. Source-local citation needs no additional semantic mapping; a different intended local sense does. | A shared URI does not establish the same measurand, Scale, model, calibration regime or direct comparability. |
| [W3C/OGC SOSA/SSN Recommendation, 19 October 2017](https://www.w3.org/TR/vocab-ssn/), and [2023 Edition First Public Working Draft, 16 September 2025](https://www.w3.org/TR/vocab-ssn-2023/) | Observation and procedure accounts can supply relevant subject, property and measurement information. Interpret each claim under its cited edition; a draft proposal carries its stated draft status. | An observation graph does not by itself establish FPF Work identity, actual bindings, a measurement result, its episteme or a later use. A correspondence claim needs its own basis. |

**Constructing and revising the model.** GUM-6:2020, §§7, 9-10 and 12, supplies the distinction between the measurement principle, effects of implementation and adequacy for use. Section :5.3.1 turns that distinction into a construction and an ambiguity test. The circuit and assessment cases work this instruction using their stated subject models.

[Dounas-Frazer and Lewandowski (2018), §2](https://arxiv.org/pdf/1805.10334), distinguishes models of the phenomenon and measurement equipment and allows revision of either model or either physical arrangement. C.16 adopts those different returns. Its stopping question is the intended use of the measurement: a sufficient interval can end the work, while a consequential discrepancy can require further investigation. B.5 and C.11.DUA supply the wider inquiry and choice.


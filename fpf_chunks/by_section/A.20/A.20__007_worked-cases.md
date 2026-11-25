---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Constraint Validity for Transformation Steps"
section_id: "A.20:5"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__007_worked-cases.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "A.20 — Constraint Validity for Transformation Steps"
  - "A.20:5 — Worked cases"
line_start: 41452
line_end: 41467
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "A.6.1"
  - "A.6.4"
  - "B.3"
  - "C.2.1"
  - "C.27"
  - "E.17"
  - "E.18"
  - "E.20"
  - "F.9"
  - "G.11"
keywords:
---

### A.20:5 - Worked cases

#### A.20:5.1 - Satisfied unit-conversion constraint

`TemperatureConversion-7` converts a Celsius input to kelvin. For the numerical Celsius value `c` and numerical kelvin value `k`, the named constraint requires `k = c + 273.15` and `k >= 0`; the corresponding temperature is `k K`. It is required for this use. For input 25 °C, the test obtains 298.15 K and a non-negative result, so the outcome is `satisfied`. The witness records the input, formula edition, output, and test result for this evaluation window.

The local summary is `satisfied` because this is the complete required set for the stated case. That result does not say that a release gate passed or that conversion Work occurred.

#### A.20:5.2 - Violation and missing-witness variants

If the implementation returns 297.15 K for 25 °C, that output violates the formula constraint. The exact output may be unavailable while an applicable bound still settles the question. An output in the interval [296, 297] K cannot equal 298.15 K, so that bound also establishes a violation. An interval [298, 299] K establishes non-negativity but leaves exact equality open. With that evidence the combined constraint has outcome `unknown`. If the evaluation was never performed, its state is `notRun`. A separately commissioned execution is still due.

#### A.20:5.3 - Lossy retargeting

Suppose an A.6.4 arrow r relates an episteme about a detailed equipment classification to one about three maintenance classes. A separate q affirmatively states that the receiving classes preserve the maintenance action selected for every source case under named conditions and allows loss of manufacturer-specific distinctions for that use. Because that proposition is the named internal constraint here, A.20 tests it on the stated cases. A sample supports only those sampled cases unless the evaluation also supplies an argument covering the proposition’s universal quantifier. No reverse mapping is part of that constraint. Facts that establish the invariant and keep loss within the boundary yield the A.20 outcome `satisfied`; a counterexample yields `violated`; a missing deciding fact yields `unknown`. The separate A.6.4 current-case judgement then compares all current facts with q's conditions and proposition and reports `satisfies`, `fails`, or `cannot decide`; the A.20 outcome does not replace it. Any operation that produced the receiving episteme remains separate.


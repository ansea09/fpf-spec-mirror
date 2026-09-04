---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Constraint Validity for Transformation Steps"
section_id: "A.20:5"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__007_worked-cases.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.20 — Constraint Validity for Transformation Steps"
  - "A.20:5 — Worked cases"
line_start: 35069
line_end: 35084
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

`TemperatureConversion-7` converts a Celsius input to kelvin. The named constraint says that the output must equal the input plus 273.15 K and must remain at or above 0 K. It is required for this use. For input 25 °C, the test obtains 298.15 K and a non-negative result, so the outcome is `satisfied`. The witness records the input, formula edition, output, and test result for this evaluation window.

The local summary is `satisfied` because this is the complete required set for the stated case. That result does not say that a release gate passed or that conversion Work occurred.

#### A.20:5.2 - Violation and missing-witness variants

If the same implementation returns 297.15 K for 25 °C, the formula constraint is `violated` and the returned values are the counterexample. If the implementation output cannot be recovered, the outcome is `unknown`, not `violated` and not `satisfied`. If the test was never run, its evaluation state is `notRun` and the summary is `unresolved`.

#### A.20:5.3 - Lossy retargeting

Suppose an A.6.4 arrow r relates an episteme about a detailed equipment classification to one about three maintenance classes. A separate q affirmatively states that the receiving classes preserve the maintenance action selected for every source case under named conditions and allows loss of manufacturer-specific distinctions for that use. Because that exact proposition is the named internal constraint here, A.20 tests it on the stated cases. No reverse mapping is part of that constraint. Exact facts that establish the invariant and keep loss within the boundary yield the A.20 outcome `satisfied`; a counterexample yields `violated`; a missing deciding fact yields `unknown`. The separate A.6.4 current-case judgement then compares all exact current facts with q's conditions and proposition and reports `satisfies`, `fails`, or `cannot decide`; the A.20 outcome does not replace it. Any operation that produced the receiving episteme remains separate.


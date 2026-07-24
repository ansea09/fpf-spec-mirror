---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__005_solution.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:4 — Solution"
line_start: 64285
line_end: 64305
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.32"
  - "C.32.ACS"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "architecture-characteristic eval program"
  - "comparison input"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:4 - Solution

Create an architecture-characteristic eval program only after the evaluated criteria rows exist in `C.32.ACS` or a declared C.25 Q-Bundle slot.

Work in this order:

1. Reference the evaluated ACS criteria set, evaluated rows, and any Q-Bundle slots.
2. State the eval purpose: current characterization, candidate comparison, portfolio-frontier work, post-change impact measurement, monitoring, or trigger for the next synthesis pass.
3. Name the candidates, bearers, and selected structures being evaluated.
4. Establish the parity frame: context, resource budget, time window, units, admissible observation or evidence inputs, and policy for missing or unknown readings.
5. Choose eval scope: one criterion, coupled criteria, one Q-Bundle slice, a candidate portfolio, or a holistic use slice.
6. Choose eval operations. Use measurement, simulation, benchmark, scenario walkthrough, monitor, review, or evidence audit according to the claim. Use `test` only when the eval operation is actually checking an expectation or hard constraint.
7. Declare the result form: reading, band, rank, dominance relation, trade-off front, qualitative state, or evidence finding.
8. Name proxy risk and protected counter-characteristics before the eval result can drive work. Optimize only the cycle's chosen indicators; keep the remaining protected characteristics visible as guardrails or risk signals.
9. State the receiving use: `C.32` synthesis input, `C.32.MLAO` residual input, `E.23` improvement feedback, `A.19.CPM` comparison input, `A.19.SelectorMechanism` selection input, `C.11` choice input, input for publishing a selected set under `G.5`, or architecture-decision input for `C.32.PAD`.
10. Refresh or retire the eval program when the evaluated row, C.32 candidate palette, bearer, selected structure, environment, parity frame, or source-currentness relation changes.

**Stop condition.** Stop C.32.ACE when the eval program names evaluated rows or Q-Bundle slots, evaluated candidates or structures, parity frame, eval purpose, eval operation, result form, receiving use, proxy risk, protected counter-characteristics, and refresh or retire condition.

**Lowering condition.** Keep the result as an eval result only while the evaluated rows, evaluated candidates or structures, parity frame, eval operation, result form, and receiving use still match the work being done. Lower the result to report-only when missing data, proxy risk, or parity-frame mismatch prevents synthesis, comparison, selection, publication of a selected set, choice, evidence, assurance, or decision use. Retire the eval program when its evaluated row, bearer, selected structure, environment, source-currentness relation, or receiving use no longer belongs to the current architecture work. Return to `C.32.ACS` when the criteria row is missing or wrong, to `C.16` when measurement validity is current, to `C.25` when the evaluated item is composite, and to the named receiving pattern when a stronger downstream claim is current.


---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__005_solution.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:4 — Solution"
line_start: 64469
line_end: 64489
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
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
4. Establish one exact `U.ClaimScope`, the relevant A.2.6 `U.ContextSlice` membership, effective `U.ReferenceScheme` and reference plane, evaluation window, input projections, resource budget, units, admissible observation or evidence inputs, and missing-or-unknown policy. Record their parity requirement in `parityFrameRef`; the parity-frame record does not replace those bindings.
5. Choose eval scope: one criterion, coupled criteria, one Q-Bundle slice, a candidate portfolio, or a holistic use slice.
6. Choose eval operations. Use measurement, simulation, benchmark, scenario walkthrough, monitor, review, or evidence audit according to the claim. Use `test` only when the intended operation checks an expectation or hard constraint. When evaluation actually occurs, recover each exact evaluator through A.13 and let A.15.1 independently admit the `U.Work` occurrence and enacted Method. Add `evaluationWorkAttributionRefs` only when the record or receiving use expressly represents precise assignment-bound attribution. Independently identify the relation or A.6.1 application binding that obtains and the typed result; the program record itself does not run.
7. Declare the result form. Examples include a reading, band, rank, dominance relation, trade-off front, qualitative state, or evidence finding; use the definition and test for the actual result kind.
8. Name proxy risk and protected counter-characteristics before the eval result can drive work. Optimize only the cycle's chosen indicators; keep the remaining protected characteristics visible as guardrails or risk signals.
9. State the receiving use: `C.32` synthesis input, `C.32.MLAO` residual input, `E.23` improvement feedback, `A.19.CPM` comparison input, `A.19.SelectorMechanism` selection input, `C.11` choice input, input for a selected-set result declared under `G.5`, or architecture-decision input for `C.32.PAD`. For publication input, distinguish `E.17` source-backed face and source return from the `E.24.PUB` publication occurrence and audience availability.
10. Refresh or retire the eval program when the evaluated row, C.32 candidate palette, bearer, selected structure, environment, parity frame, or source-currentness relation changes.

**Stop condition.** Stop C.32.ACE when the eval program names evaluated rows or Q-Bundle slots, evaluated candidates or structures, parity frame, eval purpose, eval operation, result form, receiving use, proxy risk, protected counter-characteristics, and refresh or retire condition.

**Lowering condition.** Keep the result as an eval result only while the evaluated rows, evaluated candidates or structures, parity frame, eval operation, result form, and receiving use still match the work being done. Lower the result to report-only when missing data, proxy risk, or parity-frame mismatch prevents synthesis, comparison, selection, selected-set result declaration, actual publication, choice, evidence, assurance, or decision use. Retire the eval program when its evaluated row, bearer, selected structure, environment, source-currentness relation, or receiving use no longer belongs to the current architecture work. Use `C.32.ACS` when the criteria row is missing or wrong, `C.16` when measurement validity is current, `C.25` when the evaluated item is composite, and the named pattern for the next question when a stronger downstream claim is current.


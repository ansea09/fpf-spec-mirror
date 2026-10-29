---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__005_solution.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:4 — Solution"
line_start: 77197
line_end: 77217
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
  - "architecture fitness-function source wording"
  - "architecture-characteristic eval program"
  - "comparison input"
  - "current-architecture evaluation"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "monitoring"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:4 - Solution

Create an architecture-characteristic eval program only after the evaluated criteria rows exist in `C.32.ACS` or a declared C.25 Q-Bundle slot.

Work in this order:

1. Reference the evaluated ACS criteria set, evaluated rows, and any Q-Bundle slots.
2. State the eval purpose: current characterization, candidate comparison, portfolio-frontier work, post-change impact measurement, monitoring, or trigger for the next synthesis pass.
3. Name the candidates, bearers, and selected structures being evaluated.
4. Establish one exact `U.ClaimScope`, the relevant A.2.6 `U.ContextSlice` membership, effective `U.ReferenceScheme` and reference plane, evaluation window, input projections, resource budget, units (when required by the scale), admissible observation or evidence inputs, and missing-or-unknown policy. When the intended inference relies on parity, establish the required comparable conditions and use `parityFrameRef` if a record is useful. The frame does not replace the underlying bindings.
5. Choose eval scope: one criterion, coupled criteria, one Q-Bundle slice, a candidate portfolio, or a holistic use slice.
6. Choose eval operations. Use measurement, simulation, benchmark, scenario walkthrough, monitor, review, or evidence audit according to the claim. Use `test` only when the intended operation checks an expectation or hard constraint. When a particular actual evaluation Work occurrence is claimed, recover each evaluator's A.13 core and let A.15.1 independently admit the occurrence from its history, Method actually followed, extent and containing-System relation. Add `evaluationWorkAttributionRefs` only when the record or receiving use expressly represents precise assignment-bound attribution. Add an operation-application relation only when that claim is needed and its predicate obtains. Establish the typed result separately; the program record itself does not run.
7. Declare the result form. Examples include a reading, band, rank, dominance relation, trade-off front, qualitative state, or evidence finding; use the definition and test for the actual result kind.
8. Examine material proxy risk before the eval result drives work, and protect the characteristics or constraints it could compromise. If no material risk is found, retain that basis. Optimize only the chosen indicators; keep binding constraints and other necessary safeguards visible.
9. State the receiving use: `C.32` synthesis input, `C.32.MLAO` residual input, `E.23` improvement feedback, `A.19.CPM` comparison input, `A.19.SelectorMechanism` selection input, `C.11` choice input, input for a selected-set result declared under `G.5`, or architecture-decision input for `C.32.PAD`. For publication input, distinguish `E.17` source-backed face and source return from the `E.24.PUB` publication occurrence and audience availability.
10. When a criterion, candidate, bearer, structure, environment, parity condition or source premise changes, identify which evaluation dependence is affected. Revise or retire the program if its operation or conditions no longer support the receiving use; retain it when its grounds still apply.

**Stop condition.** Stop C.32.ACE when the account makes the evaluated rows or slots, subject, purpose, operation, result form, receiving use and necessary conditions recoverable, including parity for a dependent comparison and material proxy risks or protected losses. Retain an adequate existing evaluation program; a changed premise identifies what to revisit.

**Lowering condition.** Use each result only for claims supported by its evaluated subject, criteria, operation and conditions. Missing data, uncontrolled proxy risk or failed parity blocks the inference that depends on it; retain independently usable readings and qualified reports. Publishing such a report does not itself claim the unavailable comparison or decision. Reuse a program for new candidates when its conditions still apply, or revise the affected operation when they do not. Use ACS for a missing or wrong criterion, C.16 for measurement validity and C.25 for a composite quality; comparison, evidence, assurance and decisions retain their own rules.


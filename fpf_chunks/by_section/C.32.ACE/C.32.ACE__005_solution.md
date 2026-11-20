---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__005_solution.md"
commit_sha: "5e9f4d868afa1f9db90d4c7ff6840bd55f3b8d18"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:4 — Solution"
line_start: 81964
line_end: 81984
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

Identify at least one declared criterion for the evaluation. Use a C.32.ACS row, a C.25 Q-Bundle slot, or both when the evaluation needs both.

Work in this order:

1. Cite each evaluated criterion where it is defined. For an ACS row, include the set it belongs to. For a Q-Bundle slot, identify the bundle and slot. Recover the result it asks for, such as a bound for every request or the share of requests within a limit.
2. State the eval purpose: current characterization, candidate comparison, portfolio-frontier work, post-change impact measurement, monitoring, or trigger for the next synthesis pass.
3. Name the candidates, bearers, and selected structures being evaluated.
4. Establish the exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership and effective reference scheme. Retain every declared selector and the plane, time stance or window, input projection, resource budget, applicable units, admissible inputs and missing-data treatment required by the chosen operation and receiving inference. Establish parity when that inference depends on comparable conditions; `parityFrameRef` can retain it but does not replace the underlying facts. An atemporal structural judgement needs no invented temporal window; actual measurement and dated Work retain their own conditions.
5. Choose eval scope: one criterion, coupled criteria, one Q-Bundle slice, a candidate portfolio, or a holistic use slice.
6. Choose eval operations. An evaluation can derive a consequence from qualified premises, measure performance or examine an existing result for applicability. Choose measurement, simulation, benchmark, walkthrough, monitoring, review or evidence audit according to what remains open. Name the derivation and its premises when relying on a calculated bound. An existing result can settle the criterion directly. Use `test` only when the intended operation checks an expectation or hard constraint. When a particular evaluation Work occurrence is claimed, recover each evaluator's A.13 core and let A.15.1 independently admit the occurrence from its history, Method followed, extent and containing-System relation. Add `evaluationWorkAttributionRefs` only when the record or receiving use represents precise assignment-bound attribution. Add an operation-application relation only when that claim is needed and its predicate obtains. Establish the typed result separately; the program record does not run.
7. Declare the result form. Examples include a reading, band, rank, dominance relation, trade-off front, qualitative state, or evidence finding; use the definition and test for the result kind.
8. Examine material proxy risk before the eval result drives work, and protect the characteristics or constraints it could compromise. If no material risk is found, retain that basis. Optimize only the chosen indicators; keep binding constraints and other necessary safeguards visible.
9. State the receiving use: `C.32` synthesis input, `C.32.MLAO` residual input, `E.23` improvement feedback, `A.19.CPM` comparison input, `A.19.SelectorMechanism` selection input, `C.11` choice input, input for a selected-set result declared under `G.5`, or architecture-decision input for `C.32.PAD`. For publication input, distinguish `E.17` source-backed face and source return from the `E.24.PUB` publication occurrence and audience availability.
10. When a criterion, candidate, bearer, structure, environment, parity condition or source premise changes, identify which evaluation dependence is affected. Revise or retire the program if its operation or conditions no longer support the receiving use; retain it when its grounds apply.

**Stop condition.** Stop C.32.ACE when the account makes the evaluated rows or slots, subject, purpose, operation, result form, receiving use and necessary conditions recoverable, including parity for a dependent comparison and material proxy risks or protected losses. Retain an adequate existing evaluation program; a changed premise identifies what to revisit.

**Lowering condition.** Use each result only for claims supported by its evaluated subject, criteria, operation and conditions. Missing data, uncontrolled proxy risk or failed parity blocks the inference that depends on it; retain independently usable readings and qualified reports. Publishing such a report does not itself claim the unavailable comparison or decision. Reuse a program for new candidates when its conditions apply, or revise the affected operation when they do not. Use ACS for a missing or wrong criterion, C.16 for measurement validity and C.25 for a composite quality; comparison, evidence, assurance and decisions retain their own rules.


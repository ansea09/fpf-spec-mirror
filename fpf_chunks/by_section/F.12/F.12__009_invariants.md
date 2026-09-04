---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:8"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__009_invariants.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:8 — Invariants"
line_start: 97000
line_end: 97014
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.3.2"
  - "A.6.1"
  - "A.6.RCD"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.2"
  - "E.13"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.9"
  - "U.PromiseContent"
keywords:
  - "EvidenceStatus"
  - "PromiseContent"
  - "RequirementStatus"
  - "declared result scale"
  - "delivery Work"
  - "evaluation Work"
  - "indicator recovery"
  - "measured value"
  - "observation"
  - "operation result binding"
---

### F.12:8 - Invariants

1. **Exact promise.** The evaluation identifies the `U.PromiseContent` claim, not merely an SLO label or cell.
2. **Delivery-side relations.** The judged delivery Work or population and the applicable A.2.3 promise-use, delivered-outcome, and fulfilment relations remain distinct from evaluation.
3. **Outcome evidence.** Observations and values concern the promised characteristic of that Work; outputs and approvals alone are insufficient.
4. **Direct-before-proxy.** When observation and measurement directly concern the promised characteristic, use C.16 and A.10 and add no proxy. A distinct indicator relation needs exact participants and a defining or testing pattern, or the result is `missing-governor`.
5. **Window and population.** Both are explicit and match the promise.
6. **Evaluation Work and application.** A System performs dated evaluation Work, enacts the evaluation Method, and applies the exact A.6.1 operation with recoverable inputs and result binding.
7. **Declared result scale.** Characteristic, scale, unit, aggregation, threshold, exclusions, and admissible result values are stated as applicable. Boolean, trichotomous, graded, `N/A`, and `Inconclusive`-including scales are examples, not defaults.
8. **Status separation.** `Satisfied` and `Violated` are RequirementStatus values reached only through a direct acceptance result. `Inconclusive` is an EvidenceStatus value unless the declared local result scale independently admits that label; insufficient evidence otherwise leaves RequirementStatus pending.
9. **Optional verdict episteme.** A durable C.2.1 assertion is created only for a named later use and never replaces the application result, status-use occurrence, evidence relation, or fulfilment relation.
10. **Bounded reliance.** A.10 governs evidence use; B.3 is used only for assurance or material reliance; E.13 is used only for an optimized or decision-driving proxy.
11. **Non-retroactivity.** Later promise, monitor, MethodDescription edition, or interpretation changes do not silently alter past evaluations or assertions.
12. **Cells are addresses only.** An F.17 cell may identify local meaning but establishes none of the substantive claims above.


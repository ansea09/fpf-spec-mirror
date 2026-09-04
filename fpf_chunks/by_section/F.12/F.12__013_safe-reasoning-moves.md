---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:12"
section_title: "Safe reasoning moves"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__013_safe-reasoning-moves.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:12 — Safe reasoning moves"
line_start: 97069
line_end: 97083
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

### F.12:12 - Safe reasoning moves

1. **Match scope.** Confirm that the promise content covers the exact delivery Work or population and keep A.2.3 promise use, delivery, and fulfilment distinct.
2. **Name the window.** Make time, batch, phase, and exclusions explicit.
3. **Test direct measurement first.** Confirm whether each observation and its measurement model directly concern the promised characteristic; if so, use C.16 and A.10 and add no proxy.
4. **Recover an indicator only when needed.** When another characteristic stands in, name both participants, the defining or testing pattern, coverage, and loss. Use C.16.P for recovery and A.6.RCD `missing-governor` when the relation is absent.
5. **Check values.** Name characteristic, scale, unit, aggregation, and uncertainty.
6. **Perform the evaluation.** Name the performing System, evaluation Work, enacted Method, exact A.6.1 application, input bindings, and result binding. Cite a particular MethodDescription edition only when it changes the result or replay.
7. **Use evidence directly.** Record the A.10 evidence-use claim. Enter B.3 only for assurance or material reliance, and E.13 only when a proxy is optimized or drives a decision, gate, incentive, release argument, reputation signal, or repair.
8. **Keep the result on its declared scale.** Boolean, trichotomous, graded, `N/A`, and `Inconclusive`-including scales are examples, not defaults.
9. **Map status separately.** Use `RequirementStatus=Satisfied` or `RequirementStatus=Violated` only through the direct acceptance result. Evidence insufficiency can support `EvidenceStatus=Inconclusive` and leave the requirement pending, or produce an exact locally declared result.
10. **Create a verdict episteme only on demand.** Use C.2.1 only when another use needs a durable assertion about the result or status.
11. **Aggregate explicitly.** Population-level results and statuses follow the promise's stated quantifier; they are not inferred from a few green cases.
12. **Preserve history.** New promises, monitors, evaluation methods, or scales create new evaluations rather than changing old ones silently.


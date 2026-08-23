---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:6"
section_title: "The binding, as eight practical rules"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__007_the-binding-as-eight-practical-rules.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:6 — The binding, as eight practical rules"
line_start: 93446
line_end: 93479
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

### F.12:6 - The binding, as eight practical rules

**R1 — Match the promise to delivery.**
Use A.2.3 to keep the exact promise content, `PromiseContentUse`, delivered outcome, and fulfilment relations distinct for the Work occurrence or population being judged. An abstract service label or lexical cell is not enough, and the later evaluation does not make those delivery-side relations obtain.

**R2 — First test for direct measurement.**
Ask whether the observation and measurement model directly concern the promised characteristic of the relevant Work outcome inside the window. If they do, use C.16 for measurement and A.10 for evidence use; add no proxy relation. Commands, approvals, and MethodDescriptions are not outcome evidence by themselves.

**R3 — Recover any real indicator relation.**
If a distinct observed indicator stands in for the promised characteristic or outcome, name both participants and cite the pattern that defines or tests that exact relation. Use C.16.P to recover the construction and distortion risk. If no current rule supplies the relation, stop with A.6.RCD `missing-governor`; do not treat the word *proxy*, A.10 evidence use, or B.3 reliance as its substitute. Use E.13 only when the indicator is optimized or used as a target, incentive, gate, release argument, reputation signal, repair target, or decision driver.

**R4 — Perform the evaluation.**
Name the System that performs dated evaluation Work and the evaluation Method it enacts. Identify the A.6.1 operation application, its selected facts and state references, the applied acceptance rule, and the result binding. Surface a particular MethodDescription edition only when selecting that edition changes the result or its replay.

**R5 — Use the declared result scale.**
Name the characteristic, scale, unit, aggregation, comparison, and admissible result values through the acceptance specification's `verdictScaleDescriptionRef`. Typical calculation shapes include:

* a value at or above, or at or below, a threshold;
* a stated percentile at or below a target;
* a share such as good time divided by total time;
* an event count within a limit;
* all relevant values remaining inside a band.

The calculation shape does not select a verdict scale. Use the exact scale declared by the acceptance specification.

**R6 — State every needed relation directly.**
Use A.2.3 for promise use, delivery, and fulfilment; C.16 for observation and measurement; the defining or testing pattern for any indicator relation; A.10 for evidence use; B.3 only for assurance or material reliance; and F.9 only when distinct local meanings themselves require a semantic relation. One generic Bridge cannot establish clause–Work fit, measurement, indicator validity, evidence, evaluation, status, or fulfilment.

**R7 — Keep the window and population explicit.**
A monthly verdict, a batch verdict, and an incident verdict are different claims. A new promise, monitor, or window does not rewrite an earlier verdict.

**R8 — Preserve result, status, and assertion boundaries.**
Keep the operation result on its declared acceptance scale. Map it to `RequirementStatus=Satisfied` or `RequirementStatus=Violated` only through the exact F.10 rule. If evidence coverage, indicator adequacy, scale conversion, or relation support is insufficient, use `EvidenceStatus=Inconclusive`, leave `RequirementStatus=Pending`, or return the exact local result declared by the acceptance scale. Create a C.2.1 verdict episteme only when another use needs that durable assertion.


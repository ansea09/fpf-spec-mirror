---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
section_id: "F.12:7"
section_title: "Evaluation shapes"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__008_evaluation-shapes.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "F.12 — Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
  - "F.12:7 — Evaluation shapes"
line_start: 106562
line_end: 106581
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

### F.12:7 - Evaluation shapes

The calculation shapes and examples below take independently admitted delivery and evaluation Work as inputs under A.2.3:4.3. Their population, measurement and acceptance claims still need the stated local basis.

#### F.12:7.1 - Availability share

Promise: availability is at least 99.9% for a calendar month. Delivery Work: the defined service-delivery occurrences or population during that month. Evidence: observations and measurement results for the promised availability characteristic. A System performs evaluation Work; its A.6.1 application binds the in-scope values and returns the declared result. If the observation model already concerns the promised characteristic, there is no proxy relation. If synthetic probes instead indicate a different user-experience characteristic, name the exact indicator relation, its defining or testing pattern, uncovered regions or degradations, and the evidence-use boundary; otherwise stop with `missing-governor`.

#### F.12:7.2 - Latency percentile

Promise: p95 response latency is at most 120 ms for a stated request population and window. Evidence: response-time observations for that population. Evaluation Work applies the declared sampling, exclusion, and percentile rule and binds its result on the declared acceptance scale. Sampling bias or missing paths can support `EvidenceStatus=Inconclusive` and leave `RequirementStatus=Pending`, or yield a locally declared result when the scale explicitly says so.

#### F.12:7.3 - Safety or quality band

Promise: temperature remains within `[L,U]` during the batch phase. Evidence: calibrated temperature observations for the relevant EntityOfConcern and interval. Evaluation Work applies the stated sampling, uncertainty, and band rule; the exact application binds the values and returns a result on the declared scale. A RequirementStatus follows only through its own rule.

#### F.12:7.4 - Incident duration

Promise: restoration occurs within 60 minutes for each in-scope incident. Delivery Work: each handling occurrence. Evidence: observations of the defined start and restoration events. Evaluation Work applies the elapsed-time rule to those bindings and returns its declared result. A BPMN design may be a MethodDescription under A.3.2, but it is not either Work occurrence or evidence of the result.


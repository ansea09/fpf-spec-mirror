---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:11"
section_title: "Extended worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__012_extended-worked-examples.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:11 — Extended worked examples"
line_start: 97130
line_end: 97147
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

### F.12:11 - Extended worked examples

#### F.12:11.1 - CDN latency by region

Promise content: p95 end-user latency ≤ 200 ms per region per month. Delivery Work population: delivery occurrences per region in that month. Evidence: response-time observations tagged by region and path. If probes measure the promised characteristic directly, use C.16 and A.10 without a proxy. If they indicate a distinct user-experience characteristic, name the exact probe-to-user relation, its defining or testing pattern, and last-mile loss. Evaluation Work returns one result per region on the declared scale. A global all-regions statement is a separate logical aggregation of those results or statuses, not a property of a table row.

#### F.12:11.2 - Stroke care door-to-needle

Promise content: at least 90% of in-scope ischemic-stroke episodes achieve door-to-needle ≤ 30 minutes in the quarter. Delivery Work population: patient-episode care occurrences. Evidence: observations of defined door and needle events. Evaluation Work binds those events, counts qualifying episodes, divides by the eligible population, and returns the declared result. Missing triage tags or event ambiguity may support `EvidenceStatus=Inconclusive` and leave `RequirementStatus=Pending`, or produce the exact local result declared by the acceptance scale.

#### F.12:11.3 - Cold-chain warehouse

Promise content: product temperature remains in `[2,8] °C` for at least 99.5% of each day. Delivery Work: the daily storage occurrence or defined population. Evidence: calibrated thermistor observations. First ask whether the measurement model directly concerns product exposure. If sensor position indicates another characteristic, name the exact indicator relation and its stratification loss or stop at `missing-governor`. Evaluation Work returns in-band covered time divided by in-scope time on the declared scale. Any result assertion, RequirementStatus, evidence use, and material reliance statement retain the indicator limit separately.

#### F.12:11.4 - SaaS incident MTTR

Promise content: MTTR ≤ 60 minutes for each in-scope incident. Delivery Work: each incident-handling occurrence. Evidence: observed start-fix and restoration events. Evaluation Work applies the declared duration operation and binds one result per incident. Quarterly reporting explicitly aggregates those results or their separately warranted statuses.


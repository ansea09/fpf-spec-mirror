---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
section_id: "F.12:11"
section_title: "Extended worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__012_extended-worked-examples.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "F.12 — Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
  - "F.12:11 — Extended worked examples"
line_start: 131688
line_end: 131711
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

Promise content: p95 end-user latency ≤ 200 ms per region per month. Delivery Work population: delivery occurrences per region in that month. Evidence: response-time observations tagged by region and path. If probes measure the promised characteristic directly, use C.16 and A.10 without a proxy. If they indicate a distinct user-experience characteristic, name the exact probe-to-user relation, its defining or testing pattern, and last-mile loss.

Evaluation Work applies the regional rule to its observations. A numerical p95 needs a nonempty population with the required measurement basis. If the population was empty, use the contract’s specified empty-region treatment. Missing observations alone do not establish an empty region. A single region that breaches its threshold suffices to reject a promise made to every region. To accept it, the evidence must cover them all. A separate promise about the pooled population uses that population’s latency distribution and can give a different answer.

#### F.12:11.2 - Stroke care door-to-needle

Promise content: at least 90% of in-scope ischemic-stroke episodes achieve door-to-needle ≤ 30 minutes in the quarter. Delivery Work population: patient-episode care occurrences. Evidence: observations of defined door and needle events. Evaluation Work binds those events and divides the qualifying count by the eligible count when the denominator is positive. For an established empty eligible population, use the stipulated empty-population treatment or report that the percentage is undefined.

If missing triage tags or ambiguous events leave both threshold outcomes possible, identify what remains unresolved. A formal evidence status, requirement status or local acceptance result needs its own applicable rule.

#### F.12:11.3 - Cold-chain warehouse

Promise content: product temperature remains in `[2,8] °C` for at least 99.5% of each day. Delivery Work: the daily storage occurrence or defined population. Evidence: calibrated thermistor observations. First ask whether the measurement model directly concerns product exposure. If the measurement concerns another characteristic, such as air temperature at the sensor, establish its indicator relation to product temperature and account for stratification loss. Return `missing-governor` if no rule defines or tests that relation. Otherwise apply the rule with the available coverage.

Apply the promise to the entire in-scope day. For equally weighted minutes, the known in-band count is a lower bound. Adding all unclassified minutes gives an upper bound. Of 1,440 minutes, 1,433 in band suffice for 99.5%. Eight confirmed out of band already establish failure. With 1,430 confirmed in band and ten unclassified, two further in-band minutes would give 1,432 and four would give 1,434. If both completions are compatible with the evidence and the applicable rule, both outcomes remain possible. An independent bound establishing that at least three of the ten minutes were in band already settles this threshold. Use the contract's own treatment of missing readings and assess a separately promised trace on its own terms. Retain relevant indicator limits in the result, status and reliance claim.

#### F.12:11.4 - SaaS incident restoration duration

Promise content: restoration within 60 minutes for each in-scope incident. Delivery Work: each incident-handling occurrence. Use the start event named by the contract and the observed restoration event. If notification at 10:00 starts the clock and service returns at 11:15, the interval is 75 minutes. Starting repair at 10:40 gives a different, 35-minute interval. Apply the declared duration rule per incident. Quarterly reporting aggregates those results or their separately warranted statuses.


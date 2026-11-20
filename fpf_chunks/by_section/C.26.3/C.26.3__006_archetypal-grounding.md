---
chunk_kind: "child"
pattern_id: "C.26.3"
pattern_title: "Viability-Envelope Boundary Regulation"
section_id: "C.26.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.3/C.26.3__006_archetypal-grounding.md"
commit_sha: "5e9f4d868afa1f9db90d4c7ff6840bd55f3b8d18"
heading_path:
  - "C.26.3 — Viability-Envelope Boundary Regulation"
  - "C.26.3:5 — Archetypal Grounding"
line_start: 70082
line_end: 70111
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.3"
  - "A.6"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "U.Dynamics"
keywords:
  - "allostasis"
  - "boundary regulation"
  - "failure mode"
  - "homeostasis"
  - "metric-induced distortion"
  - "quality bundle"
  - "sensor/probe/actuator split"
  - "service viability"
  - "viability envelope"
---

### C.26.3:5 - Archetypal Grounding

In this constructed case, a platform team must preserve checkout service during a traffic spike. The receiving service requirement specifies both timely responses and sufficiently current payment-failure status. The team traces a proposed increase in cache duration: serving more requests from cache may reduce delay, while retaining old status longer can mislead customers and increase support contacts.

`CheckoutSystem-1` is independently recognized under A.1 as the deployed System. `CheckoutPromiseContent-1` separately states the checkout outcome and reliability on which customers may rely. For this example, the receiving requirement sets the latency limit at 250 ms for the highest five-minute p95 in the incident hour and the stale-status limit at 1% of statuses in that hour. The support limit is derived from the provision reserved for this incident: four available specialists can each handle up to five comparable contacts within the hour under the stipulated workload, giving reserved capacity for 20. These are constructed requirement and capacity premises, not limits inferred from the observed averages.

Compare two matched one-hour windows under the stipulated spike condition, before and after the cache-setting change:

| Constraint and subject | Required bound | Before cache-setting change | After cache-setting change |
| --- | --- | ---: | ---: |
| CheckoutSystem-1 request latency, highest five-minute p95 within each hour | <=250 ms | 350 ms | 180 ms |
| CheckoutSystem-1 stale payment-failure statuses over the incident hour | <=1% | 0.2% | 3% |
| Incident support demand: customer contacts requiring handling during that hour | <=20 | 10 | 45 |

In this constructed case the highest five-minute p95 falls from 350 to 180 ms. In the second hour the status and support bounds are both exceeded. That hour therefore fails the joint requirement.

The decision combines properties of CheckoutSystem-1 with demand on the incident-support team. The support figure counts contacts requiring handling; a count of completed handling would concern actual support Work. Operator attention, if added, would concern the people handling those contacts. Fulfillment of CheckoutPromiseContent-1 still needs its own evaluation.

Suppose the acceptable stale-status bound is missing. Demand of 45 contacts already exceeds capacity for 20, so the joint requirement failed in this hour. Keep the observed stale-status rate of 3%. Recover the freshness requirement if deciding whether that rate also fails or which remedy to pursue.

A dashboard query is an observation operation unless a behavior-changing effect is separately established.

For this hour the team can report that service fell outside the required bounds. To decide whether changing the cache setting caused the difference or would restore service in another spike, examine how the setting affected reads and updates and what else differed between the two hours. That account can guide comparison of a shorter cache duration and a bypass for payment-failure updates, including their effects on upstream work and latency.

Recover the proposal's object, adaptation cost, applicable authority and realization latency before choosing it; a planned enactment belongs in a WorkPlan. Missing intervention evidence leaves the diagnosis useful.

If support capacity is independently revised to 50 comparable contacts per hour under the same conditions, the same demand of 45 contacts satisfies that revised constraint, but the 3% stale-status result still exceeds the retained 1% requirement.




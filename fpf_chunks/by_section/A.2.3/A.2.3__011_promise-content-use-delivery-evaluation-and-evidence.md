---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent — Promised Outcomes and Acceptance Criteria"
section_id: "A.2.3:8"
section_title: "Promise-content use, delivery, evaluation, and evidence"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__011_promise-content-use-delivery-evaluation-and-evidence.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "A.2.3 — U.PromiseContent — Promised Outcomes and Acceptance Criteria"
  - "A.2.3:8 — Promise-content use, delivery, evaluation, and evidence"
line_start: 6195
line_end: 6263
dependencies:
  - "A.2.2"
  - "A.2.8"
  - "A.6.C"
  - "A.6.P"
  - "E.10"
  - "F.12"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptance specification"
  - "access specification"
  - "claim scope"
  - "promise content"
  - "promised outcome"
  - "provider and consumer system-role kinds"
---

### A.2.3:8 - Promise-content use, delivery, evaluation, and evidence

Keep `PromiseContentUse`, `PromisedOutcomeDeliveryRelation`, evaluation `U.Work`, the actual evaluation-operation application and result binding, any verdict episteme, and A.10 evidence relations separate. A direct relation may obtain even when the current episteme about it is unresolved; evidence supports the claim and does not become the relation.

#### A.2.3:8.1 - Core relations

**`PromiseContentUse : U.Relation`.** This direct use relation obtains between one delivery-work occurrence and one promise-content edition during one named promise-use interval; it makes no fulfilment claim.

```text
PromiseContentUse : U.Relation
  DeliveryWorkOccurrenceSlot: U.Work, U.EntityRef
  PromiseContentSlot: U.PromiseContent, U.EpistemeRef
  PromiseUseIntervalSlot: temporal interval, byValue
```

Its occurrence key is `<DeliveryWorkOccurrenceSlot, PromiseContentSlot, PromiseUseIntervalSlot>`.

**`PromisedOutcomeDeliveryRelation : U.Relation`.** This derived relation obtains between one delivery-work occurrence and the A.2.3:4.1.1 `OutcomeSpec` resolved from the `PromiseContentUse` occurrence in which that work participates, when the conditions below hold.

```text
PromisedOutcomeDeliveryRelation : U.Relation
  DeliveryWorkOccurrenceSlot: U.Work, U.EntityRef
  PromisedOutcomeSpecificationSlot: U.Episteme, U.EpistemeRef constrained to A.2.3:4.1.1 OutcomeSpec
```

The relation obtains only when one `PromiseContentUse` occurrence has the delivery Work and promise-content edition as participants, that edition resolves the same `OutcomeSpec`, and the mode-specific conditions hold. `workSpec` tests selected Work facts. `resultSpec` tests the exact affected referent and selected post-work state; any actual-change, production, delivery, acceptance, receiving-use, or optional Delta-lens claim remains separately governed.

Its occurrence key is `<DeliveryWorkOccurrenceSlot, PromisedOutcomeSpecificationSlot>`. The readable predicate is `deliversPromisedOutcome(W, OS)`. An episteme may assert that this relation obtains and evidence may support the assertion; neither makes the underlying facts satisfy the specification.

**Acceptance evaluation result.** Apply the criterion to the required state, specified delivery, eligible population or reporting interval (§§4.3, 8.2). Where actual evaluation Work is at issue, follow the §4.3 performer-and-Work route before attributing the selected Method. Add F.6 for an exact assignment-bound claim. Cite a MethodDescription when its edition-specific claims are used. Keep the operation application, result binding, optional verdict episteme, any identity-inception claim and supporting evidence relations separate.

A.10's descriptive evidence-provenance account cites the relevant facts and records reliance for the bounded assertion use; a passing disposition requires the evidence demanded by that claim and its direct acceptance rule. The account and verdict do not make fulfilment obtain.

**`PromiseContentFulfilmentRelation : U.Relation`.** This derived relation obtains between one delivery-work occurrence and one promise-content edition when the conditions below hold.

```text
PromiseContentFulfilmentRelation : U.Relation
  FulfilmentWorkOccurrenceSlot: U.Work, U.EntityRef
  FulfilledPromiseContentSlot: U.PromiseContent, U.EpistemeRef
```

The semantic predicate for this relation is satisfied only when `PromiseContentUse` obtains for the same work and promise-content participants, `PromisedOutcomeDeliveryRelation` obtains for that work and the `OutcomeSpec` resolved from that promise content, and the acceptance predicate declared by `acceptanceSpec` is satisfied for the exact delivery-work facts, affected or delivered entities, post-work state, and any direct delivery or acceptance relation required by the criterion. `PromiseContentFulfilmentRelation` obtains for the declared participants when that semantic predicate is satisfied. Its occurrence key is `<FulfilmentWorkOccurrenceSlot, FulfilledPromiseContentSlot>`. The readable predicate is `fulfilsPromiseContent(W, SC)`.

A later evaluation may change the supported assertion about whether the relation obtains; it does not change relation identity. When satisfaction of any required predicate is unresolved, no positive fulfilment assertion is available for reliance.

Expose a relation-occurrence reference only when a downstream relation or claim needs that identity, such as a unit-of-delivery selector or a fulfilment measure. Otherwise use the readable predicate. For one `ResultOnly` promise, evidence establishing the required state for the specified referent and time can satisfy its acceptance criterion. Apply any additional acceptance conditions, including a new inspection if expressly required. Identifying Work becomes necessary when the claim concerns which Work fulfilled the promise or when the accepted terms require it. A period or population verdict may rely on these individual relations where the criterion counts them. It may instead be settled by a warranted tally, bound or service-state record. A positive readiness verdict during a shift without callers produces no individual `fulfilsPromiseContent(W, SC)` for a call.

> **Invariant:** `fulfilsPromiseContent(W, SC)` implies that `PromiseContentUse(W, SC, T)` obtains for some declared interval `T`, that `deliversPromisedOutcome(W, resolve(SC.promisedOutcomeSpecRef))` obtains, and that the acceptance criteria declared in `SC.acceptanceSpec` are satisfied. An exact evaluation-result episteme may support the corresponding assertion through independently established evidence-use relations cited in A.10's descriptive account; neither that episteme nor the account becomes a fulfilment-relation participant.
>
> **Counting rule:** Separate per-promise counts of performed deliveries may each use the one-per-fulfilment default. When combining quantities across promises, declare whether the same Work, site or other agreed unit contributes once or separately to the total. Use `dedupeKeyRef` or the counting-policy episteme to express that boundary.

#### A.2.3:8.2 - Promise-content delivery measures

Read the promise before choosing what to count. Does it cover each performed job, each eligible request or recipient, or provision throughout a period? Apply the eligibility rule and the promised time boundary to that unit. For a measure of performed jobs, let `W(SC, T)` be the delivery-work occurrences for which `PromiseContentUse` obtains with `SC` during interval `T`, and `W✓(SC, T)` its subset for which `PromiseContentFulfilmentRelation` obtains. For a measure of requests, identify the eligible requests, match each to any qualifying delivery by its deadline, and retain eligible requests without qualifying Work in the population. One request can generate several jobs. A readiness promise can apply even during an interval without requests.

For example, suppose the complete request register shows ten eligible requests due this week. The job register covers the same period and shows nine jobs, each for a different request. Eight met their deadlines, one was late and the tenth request received no work by its deadline. Eight of ten met the request promise. Eight of the nine performed jobs were timely. Choose the population that answers the consumer’s question. With incomplete records, use the possible totals consistent with the evidence. A bound that settles the agreed threshold can support that decision while the exact rate remains open.

* **Accepted units:** Compute `delivered(SC, T)` for the units and period selected under §4.1.2. With delivery Work as the unit and the default rule, `delivered(SC, T) = |W✓(SC, T)|`. Suppose instead that an agreement counts each of three rooms available at 18:00. If two were available and the third was closed, the count is two, even on a day with no delivery Work. Two observations of one room still establish one room under this rule.
* **Nonfulfilment among performed jobs:** for nonempty `W(SC,T)`, `rejectRate(SC, T) = 1 − |W✓(SC,T)| / |W(SC,T)|` for a binary criterion when both counts are known. If `partial` is possible, state how it counts. A missing judgment about a job leaves its individual outcome open. A complete tally may still establish the aggregate. When `W(SC,T)` is empty, declare a reporting rule before returning a value; this formula has a zero denominator.
* **Lead time:** declare the characteristic definition and aggregation separately. The definition may use work duration or request-to-completion delta; the aggregation may use an average or named percentile.
* **Availability and uptime claims:** select one declared characteristic instead of treating the labels as synonyms. Use observations that cover the required hours and service conditions, applying the C.16 measurement template, `Gamma_time` policy and relevant evidence relations. Work records contribute when they establish a fact the measure uses. Identify any measurement Method that changes the interpretation; cite a `U.MethodDescription` only when this claim uses that edition's claims.
* **Cost to serve:** sum `Γ_work` per resource category over the work the cost question includes (A.15.1). Use `W✓` for cost of fulfilled jobs alone. A total operating cost can also include failed attempts and standby work.

Support each measurement-result claim with the records that cover its unit and period, its C.16 measurement template and the relevant A.10 evidence relations. Work records give resource and time actuals for the Work performed. Request records or grounds for service availability may supply facts that those work records cannot establish. Make the measurement Method explicit where it affects interpretation and cite a `U.MethodDescription` when the result depends on that edition’s claims.

Aggregation across time uses the `Gamma_time` policy referenced by the named C.16 measurement template or acceptance specification; an unqualified KPI label does not select that policy.

When a measure needs a B.1.4 temporal-phase aggregation of one carrier, recover the selected policy—for example, union of covered intervals or their convex hull—together with carrier identity, time window, the coverage and overlap conditions consumed by that policy, and admissible use. An adequate ordinary account can state the result; use a separate `ContextTemporalAggregation@Context` record when the receiving use needs it. If those one-carrier conditions do not hold, this example is inapplicable; state the aggregation required and apply its defining rule. Union and convex hull are policy choices, not defaults; `Gamma_time` does not select either by itself.


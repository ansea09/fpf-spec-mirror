---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:8"
section_title: "Promise-content use, delivery, evaluation, and evidence"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__012_promise-content-use-delivery-evaluation-and-evidence.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:8 — Promise-content use, delivery, evaluation, and evidence"
line_start: 4028
line_end: 4084
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.2.9"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "F.12"
  - "F.9"
  - "U.Capability"
  - "U.ClaimScope"
  - "U.Episteme"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
  - "U.WorkScope"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptanceSpec"
  - "accessSpec"
  - "claim scope (G)"
  - "promise content"
  - "provider/consumer roles"
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

Its occurrence key is `<DeliveryWorkOccurrenceSlot, PromiseContentSlot, PromiseUseIntervalSlot>`. Obtaining of this relation implies neither successful delivery nor intention, judgement, or claim-making by either participant.

**`PromisedOutcomeDeliveryRelation : U.Relation`.** This derived relation obtains between one delivery-work occurrence and the A.7 `OutcomeSpec` resolved from the `PromiseContentUse` occurrence in which that work participates, when the conditions below hold.

```text
PromisedOutcomeDeliveryRelation : U.Relation
  DeliveryWorkOccurrenceSlot: U.Work, U.EntityRef
  PromisedOutcomeSpecificationSlot: U.Episteme, U.EpistemeRef constrained to A.7 OutcomeSpec
```

The relation obtains only when one `PromiseContentUse` occurrence has the delivery work and a promise-content edition as participants, that edition's `promisedOutcomeSpecRef` resolves to the same `OutcomeSpec`, and the specification's mode-specific conditions hold. When `workSpec` is present, selected work facts satisfy `workSpec.workPredicateRef`. When `resultSpec` is present, the exact affected referent and post-work state expressed by the selected effect Delta satisfy `resultSpec.postConditionRef`; any current production, delivery, or acceptance relation remains separately governed. Its occurrence key is `<DeliveryWorkOccurrenceSlot, PromisedOutcomeSpecificationSlot>`. The readable predicate is `deliversPromisedOutcome(W, OS)`, where `OS` denotes that resolved `OutcomeSpec`. An episteme may assert that this relation obtains, and evidence may support that assertion; neither the assertion nor the evidence makes the work facts or post-work state satisfy the specification.

**Acceptance evaluation result.** A holder system performs evaluation `U.Work` by the evaluation method described in `acceptanceSpec`, using the same selected facts about delivery work and post-work states. The actual evaluation-operation application carries exact argument bindings and the verdict value in its declared result binding. When another use needs a durable evaluation-result episteme, C.2.1 governs that episteme, and A.15.PROD governs any current identity-inception claim linking exact work, actual change, and episteme identity. A.10 evidence relations support the relied-on assertions. The promise content does not perform the evaluation or compute the verdict; the operation-result binding, result episteme, and evidence relations support the assertion rather than making the fulfilment relation obtain.

**`PromiseContentFulfilmentRelation : U.Relation`.** This derived relation obtains between one delivery-work occurrence and one promise-content edition when the conditions below hold.

```text
PromiseContentFulfilmentRelation : U.Relation
  FulfilmentWorkOccurrenceSlot: U.Work, U.EntityRef
  FulfilledPromiseContentSlot: U.PromiseContent, U.EpistemeRef
```

The semantic predicate for this relation is satisfied only when `PromiseContentUse` obtains for the same work and promise-content participants, `PromisedOutcomeDeliveryRelation` obtains for that work and the `OutcomeSpec` resolved from that promise content, and the acceptance predicate declared by `acceptanceSpec` is satisfied for the exact delivery-work facts, affected or delivered entities, post-work state, and any direct delivery or acceptance relation required by the criterion. `PromiseContentFulfilmentRelation` obtains for the declared participants when that semantic predicate is satisfied. Its occurrence key is `<FulfilmentWorkOccurrenceSlot, FulfilledPromiseContentSlot>`. The readable predicate is `fulfilsPromiseContent(W, SC)`. A later evaluation may change the supported assertion about whether the relation obtains; it does not change relation identity. When satisfaction of any required predicate is unresolved, no positive fulfilment assertion is available for reliance.

The explicit `RelationSignature` declarations are warranted only when `unitOfDelivery` selectors or fulfilment measures refer to relation-occurrence identity. Ordinary prose may stop at the readable predicates when no later relation refers to that occurrence identity.

> **Invariant:** `fulfilsPromiseContent(W, SC)` implies `PromiseContentUse(W, SC, T)`, `deliversPromisedOutcome(W, resolve(SC.promisedOutcomeSpecRef))`, and satisfaction of the acceptance criteria declared in `SC.acceptanceSpec`; an evaluation-result episteme and A.10 evidence relations support the corresponding assertion without becoming relation participants.
> **Invariant:** One work occurrence can fulfil several promise contents only when each promise content's counting rule states `dedupeKeyRef` or refers to a counting-policy episteme under its direct governing pattern; no silent double counting.

#### A.2.3:8.2 - Promise-content delivery measures

Let `W(SC, T)` be the set of delivery-work occurrences for which `PromiseContentUse` obtains with `SC` during interval `T`. Let `W✓(SC, T)` be the subset for which `PromiseContentFulfilmentRelation` obtains with `SC`.

* **Delivered units:** `delivered(SC, T)` is computed from the set `W✓(SC, T)` using `unitOfDelivery`’s **countingRule** (A.7:5.10). Default (when `unitOfDelivery` is absent): `delivered(SC, T) = |W✓(SC, T)|` (one unit per accepted delivery work).
* **Rejection rate:** `rejectRate(SC, T) = 1 − |W✓(SC,T)| / |W(SC,T)|` (declare handling of `partial`).
* **Lead time:** declare the characteristic definition and aggregation separately. The definition may use work duration or request-to-completion delta; the aggregation may use an average or named percentile.
* **Availability and uptime claims:** select one declared characteristic instead of treating the labels as synonyms. Derive its observed characteristic value from selected work facts and telemetry observations through its C.16 measurement template, `Gamma_time` policy, and evidence relations; cite a `U.MethodDescription` when a particular measurement method affects the reading.
* **Cost‑to‑serve:** sum of `Γ_work` over `W✓` per resource category (A.15.1).

Each resulting `U.Measure` claim is derived from selected facts about `U.Work` occurrences through its C.16 measurement template and named A.10 evidence relations; when a particular measurement method matters, its `U.MethodDescription` is cited. The promise-content episteme is never the bearer of resource or time actuals.
Aggregation across time uses the `Gamma_time` policy referenced by the named C.16 measurement template or acceptance specification; an unqualified KPI label does not select that policy. When a measure needs a B.1.4 temporal-phase aggregation of one carrier, name one `ContextTemporalAggregation@Context` record and its exact selected policy—for example, union of observed values or their convex hull—together with carrier identity, time window, coverage and non-overlap conditions, and admissible use. If those one-carrier conditions do not hold, return to the direct aggregation owner instead of using this example. Union and convex hull are policy choices, not defaults; `Gamma_time` does not select either by itself.


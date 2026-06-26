---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:8"
section_title: "Evidence relations & operators (Promise content ⇄ Work)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__012_evidence-relations-operators-promise-content-work.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:8 — Evidence relations & operators (Promise content ⇄ Work)"
line_start: 3298
line_end: 3325
dependencies:
  - "A.1.1"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.3.1"
  - "A.3.2"
  - "A.6.8"
  - "A.6.C"
  - "E.10"
  - "F.12"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.ClaimScope"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Scope"
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

### A.2.3:8 - Evidence relations & operators (Promise content ⇄ Work)

To keep the promise-to-evidence relation explicit:

#### A.2.3:8.1 - Core relations

* **`claimsPromiseContent(Work, PromiseContent)`** — the Work instance **intends** to fulfil the promise content (pre‑verdict).
* **`deliversPromisedOutcome(Work, OutcomeSpec)`** - the Work instance evidences delivery of the promised outcome spec (work facet, result facet, or both); derived from Work's input, output, and Delta anchors plus the `U.OutcomeSpec` (and MAY be asserted explicitly for auditability).
* **`acceptanceVerdict(Work, PromiseContent)`** -> {`pass`, `fail`, `partial`, context-specific grades} - computed by applying `acceptanceSpec` (with its declared **Gamma_time** and claim scope) to the same Work facts and evidence used to establish delivery.
* **`fulfilsPromiseContent(Work, PromiseContent)`** — the Work instance both (i) **delivers** the promised outcome spec and (ii) **passes** the promise content’s `acceptanceSpec`.
* **`usesAccess(Work, MethodDescription)`** — consumer Work that uses the service access specification to request or obtain delivery work (when applicable).

> **Invariant:** `fulfilsPromiseContent(W,SC)` ⇒ `claimsPromiseContent(W,SC)` and `deliversPromisedOutcome(W, SC.promisedOutcomeSpecRef)` and `acceptanceVerdict(W,SC)=pass`.
> **Invariant:** A Work can claim or fulfil **multiple** promise contents only if the context declares a counting policy (no silent double-counting).

#### A.2.3:8.2 - Service‑clause performance operators

Let `W(SC, T)` be the set of Work that `claimsPromiseContent(-,SC)` within time window `T`. Let `W✓(SC, T)` be those with `fulfilsPromiseContent`.

* **Delivered units:** `delivered(SC, T)` is computed from the set `W✓(SC, T)` using `unitOfDelivery`’s **countingRule** (A.7:5.10). Default (when `unitOfDelivery` is absent): `delivered(SC, T) = |W✓(SC, T)|` (one unit per accepted delivery work).
* **Rejection rate:** `rejectRate(SC, T) = 1 − |W✓(SC,T)| / |W(SC,T)|` (declare handling of `partial`).
* **Lead time:** average or percentile of `duration(Work)` or of request-to-completion delta (declare definition).
* **Availability or uptime:** computed from Work and telemetry events per the context's definition (declare availability source).
* **Cost‑to‑serve:** sum of `Γ_work` over `W✓` per resource category (A.15.1).

All metrics are **functions of Work evidence**; the promise content object is never the bearer of actuals.
Aggregation across time uses `Γ_time` policies (union vs convex hull) chosen by the KPI owner.


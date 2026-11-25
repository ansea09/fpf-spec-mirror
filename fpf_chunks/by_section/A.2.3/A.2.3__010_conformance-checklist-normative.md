---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent — Promised Outcomes and Acceptance Criteria"
section_id: "A.2.3:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__010_conformance-checklist-normative.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "A.2.3 — U.PromiseContent — Promised Outcomes and Acceptance Criteria"
  - "A.2.3:7 — Conformance Checklist (normative)"
line_start: 6114
line_end: 6194
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

### A.2.3:7 - Conformance Checklist (normative)

**CC‑A2.3‑0 (Prose head phrase).**
In normative prose, an instance of `U.PromiseContent` SHALL be referred to as a **promise content** (or **service offering clause** or **service promise clause**) and SHALL NOT be referenced by the bare head noun *service*. For the conditional L-SERV recovery rule, see CC-A2.3-10.

**CC‑A2.3‑1 (Type).**
`U.PromiseContent` **IS** a consumer-facing promise-content `U.Episteme`. One or more exact `EpistemePublicationRelation` occurrences may make the same selected promise-content edition available through separately identified expressions and carriers without changing its episteme identity. Identify reusable forms when their rules matter. No expression, publication form, or presentation carrier is the promise content. `U.PromiseContent` is not a `U.System`, `U.Method`, `U.MethodDescription`, `U.Work`, or `U.WorkPlan`.

**CC-A2.3-2 (Semantic locality).**
Every promise content names its effective `ReferenceScheme`, `promisedOutcomeSpecRef`, and exact `U.ClaimScope`. A selected `BoundedModelUseStructure` may be designated only by the receiving assertion or use when it changes one model-local interpretation; it is neither a promise-content field nor an optional participant or identity discriminator of `PromiseContentUse`.

**CC-A2.3-3 (System-role kinds stay distinct from holders and assignments).**
`providerSystemRoleKindRef` and, when present, `consumerSystemRoleKindRef` are promise-content fields typed by `U.KindRef` and resolve to local system-role kinds. When actual provider or consumer assignments are claimed, their species are declared under `U.SystemRoleAssignment`; a kind label or reference alone identifies neither a holder nor a performer.

**CC-A2.3-4 (Acceptance).**
`acceptanceSpec` **MUST** be present and **MUST** define what unit and eligible population the promise covers and how to judge the outcome as pass, fail or a declared grade against named criteria and target values. When the unit is a performed job, the criterion assesses that Work. A criterion about requests, recipients or a period also accounts for eligible cases for which no Work occurred. Any SLA deontics are represented through `U.Commitment`. The promise content **MUST** declare **Claim scope (G)** where operating conditions, populations, locales, or another claim extent matter. Every verdict cites an explicit **Gamma_time** window.

If the acceptance criteria mention measurable characteristics such as availability, latency, accuracy, cost, or safety, each characteristic MUST be introduced through C.16 with its scale, unit when applicable, and measurement specification under C.16:5.2. A relied-on measured verdict additionally names its supporting evidence and direct evidence relations. When a quality-family label hides several possible contributors, use C.25 to retain the one characteristic or structured bundle that the acceptance claim needs. If the reading depends on a particular measurement Method, identify that Method. Cite its `U.MethodDescription` only when the acceptance claim depends on that edition's claims. The characteristic is referenced by its exact identifier rather than by an unqualified KPI label.

**CC‑A2.3‑5 (Access).**
When the promised use relies on a request-facing access Method, `accessSpec` **MUST** identify the A.3.2-admitted `U.MethodDescription` that describes it. Separately recover the endpoint, desk, manifold, or other exact bearer through A.6.P:4.11a. Apply A.1 or A.1.SCR only when a current claim depends on that bearer being an access-point `U.System`; otherwise keep the bearer without the stronger claim. If no access-method description is current because access is ambient, `accessSpec` may be omitted. In either branch, keep an eligibility predicate in the promise content when eligibility is promised; when eligibility depends on a separately obtaining admission relation, identify that relation and use the pattern that defines or tests it.

**CC‑A2.3‑6 (Unit of delivery + counting rule).**
For a receiving use that counts or measures accepted service, derive the unit from the promise. Use the one-per-fulfilment default for a count of fulfilled delivery-work occurrences. For another unit or boundary, state the applicable `unitOfDelivery` rule, including how it treats rework or aggregation across promises. The resulting quantity may enter a separately governed charging relation.
The rule identifies the instances that count under the agreed criterion and how their quantities combine. Several visits to one eligible site can establish one accepted site or several performed visits, depending on the promise. The counting rule must distinguish those uses when their quantities differ.

**CC‑A2.3‑7 (No actuals on Promise Content).**
Resource and time actuals belong to the performed `U.Work` occurrence under A.15.1. An incident-log episteme may describe that occurrence and may separately participate in an evidence relation for a stated claim; neither the log nor its participation in that evidence relation fills a `U.PromiseContent` slot.

**CC-A2.3-8 (Provider capability stays separate).**
When delivery depends on provider ability, use the A.2.2 qualified ability claim about the provider System and the separate capability-fit predicate for the planned delivery work. Do not insert capability into promise-content identity or infer capability or fit from a system-role designation or assignment.

**CC-A2.3-9 (Edition and promise-use interval).**
A change to `content`, `promisedOutcomeSpecRef`, or `effectiveReferenceScheme` creates a new promise-content episteme edition under the C.2.1 identity rule. Each `PromiseContentUse` occurrence has one promise-content edition and one delivery-work occurrence as participants and `PromiseUseIntervalSlot` as its temporal qualifier; an untyped `version` or `timespan` entry fills none of those positions.

**CC‑A2.3‑10 (Lexical rule).**
Apply E.10 **L-SERV** and **A.6.P:4.11a** only when *service* or access-like wording occurs in a relied-on FPF claim, recommendation, decision, gate, assurance, publication, or reuse and hides the concrete subject, participant, predicate, kind, permission, Work occurrence, or next route. The author **MUST** name that hidden choice or stop the relied-on use; quoted, historical, illustrative, and harmless ordinary wording is outside this rule.

**CC‑A2.3‑11 (No mereology).**
Do **not** place a promise content clause in PBS or SBS, or treat it as a part or component. Structural assemblies live in PBS and SBS; the promise clause is an episteme (A.2.3). For hidden service referents, see CC-A2.3-10.

**CC-A2.3-12 (Plan, work, and evidence stay distinct).**
Planned-work windows and calendars are content of `U.WorkPlan` (A.15.2). Performed delivery belongs to `U.Work` (A.15.1). Exact affected referents, pre-work and post-work states, and direct actual-change, production, delivery, or acceptance relations remain separate. Evidence epistemes and evidence-use relations support assertions about those facts; they are not slots or parts of the Work occurrence.

**CC-A2.3-13 (Claim scope, work scope, and promise-use interval).**
The promise-content episteme names one exact `U.ClaimScope`; an intended maximal extent is stated as that scope rather than represented by omission. The qualified ability claim about the provider separately designates its `U.WorkScope`; this work-condition basis is distinct from the episteme's ClaimScope. `PromiseUseIntervalSlot` is the temporal qualifier of each `PromiseContentUse` occurrence.

The `ScopeCoverage` predicate is satisfied only when the selected context slice belongs to the claim scope. When membership depends on time, name an explicit `Gamma_time` selector and its membership boundary; retain every selector already declared in the slice even when this predicate does not inspect it. Neither temporal extent nor capability scope replaces claim scope.

**CC-A2.3-14 (Scheme and scope bridges).**
Cross-scheme reuse first names the exact obtaining F.9 Bridge occurrence. A separate current C.2.1 claim with affirmative polarity must say that this Bridge suits the named bounded promise-content use, in the stated direction, under the use-specific correspondence rule, and within the permitted-loss tolerance. Ordinary reliance requires the exact A.10 evidence-provenance relation with `RelianceDisposition=pass` for that use. Use B.3 only when a named assurance claim is current; its result supports, narrows, or blocks only that bounded assurance use. Cross-scope reuse separately names the mapped `U.ClaimScope` and its A.2.6 relations.

**CC-A2.3-15 (OutcomeSpec typing).**
`promisedOutcomeSpecRef` MUST be a `U.EpistemeRef` resolving to an A.2.3:4.1.1 `OutcomeSpec` specification-use episteme. It MUST NOT point at a concrete `U.Work` occurrence, affected or delivered entity, actual operation-result binding, verdict episteme, or downstream effect, and `OutcomeSpec` MUST NOT be written as an independently admitted `U.OutcomeSpec`.

**CC-A2.3-16 (OutcomeSpec is explicit and mode‑complete).**
`promisedOutcomeSpecRef` MUST be present and MUST reference an `OutcomeSpec` that declares `mode in {WorkOnly, ResultOnly, Composite}` and satisfies A.2.3:4.1.1 mode completeness:
* `WorkOnly` → `workSpec` present, `resultSpec` absent
* `ResultOnly` → `resultSpec` present, `workSpec` absent
* `Composite` → both `workSpec` and `resultSpec` present

**CC-A2.3-17 (OutcomeSpec predicates and delivery-work relations).**
To determine whether a `U.Work` occurrence participating in `PromiseContentUse` delivers the promised outcome, resolve `OS` as the A.2.3:4.1.1 `OutcomeSpec` from `SC.promisedOutcomeSpecRef` and test the following applicable conditions.

* If `OS.workSpec` is present, the selected facts about the work occurrence satisfy `OS.workSpec.workPredicateRef`; when `methodConstraintRef` is present, the enacted method is compatible with that constraint.
* If `OS.resultSpec` is present, the exact affected referent and selected post-work state satisfy `OS.resultSpec.postConditionRef` on its declared state plane. Any actual-change, production, delivery, acceptance, receiving-use, or optional mathematical Delta-lens claim remains separately governed.
* A.10 evidence relations obtain between each relied-on satisfaction assertion and its supporting evidence epistemes.

Assert delivery only after these mode-specific conditions are established. Explicitly individuate `PromisedOutcomeDeliveryRelation` only when a downstream relation or claim must refer to its occurrence identity; otherwise retain the readable `deliversPromisedOutcome(W, OS)` assertion.

**CC-A2.3-18 (Acceptance evaluation supports rather than constitutes fulfilment).**
For an acceptance judgement, select the evidence for the unit, interval and condition the promise covers (§§4.3, 8.2). An individual delivery requires its Work facts and required states or relations. A readiness or population judgement may be supported by service-state or coverage records. If the claim concerns a particular evaluation Work or the agreement requires one, use A.13 to identify its actual evaluator and A.15.1 to admit its occurrence before attributing the Method selected in `acceptanceSpec`. Add F.6 for an exact assignment-bound attribution. Cite a MethodDescription when the claim depends on that edition.

The actual operation application carries its argument and result bindings. Any durable verdict episteme, any identity-inception claim, and evidence-use relations remain separate. Independently established A.10 evidence relations support reliance on the fulfilment assertion; they do not constitute fulfilment.

**CC-A2.3-19 (OutcomeSpec ↔ unitOfDelivery coherence).**
When `unitOfDelivery` is present, its `selectorRef` identifies the agreed units that satisfy `SC.promisedOutcomeSpecRef` and the applicable acceptance criterion. For performed deliveries it may select the Work occurrences in `FulfilmentWorkOccurrenceSlot` of obtaining `PromiseContentFulfilmentRelation` occurrences. For a state promised of an entity or throughout an interval, it selects qualifying entities or intervals on the stated grounds. A cross-promise aggregate using the same unit requires a `dedupeKeyRef` or a counting policy specifying when to count it again.

**CC-A2.3-20 (Unit of delivery is computable from the facts its criterion requires).**
If `unitOfDelivery` is present, it follows A.2.3:4.1.2. For a pure count, identify its selector, quantity rule and any deduplication boundary. When the count depends on a measurement reading, identify its Method and required specification values; cite a MethodDescription only when the calculation or interpretation uses claims in that edition. Retain the evidence-admissibility conditions, evidence epistemes and evidence-use relations required for reliance on the count.


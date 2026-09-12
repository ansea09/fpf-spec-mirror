---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__006_archetypal-grounding-tell-show-show.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 12142
line_end: 12237
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "E.10"
  - "E.17"
  - "F.12"
  - "F.18"
  - "U.Commitment"
  - "U.PromiseContent"
  - "U.SpeechAct"
  - "U.Work"
keywords:
  - "MUST NOT"
  - "MVPK no-new-semantics"
  - "OPTIONAL"
  - "SHOULD"
  - "a mechanism entry predicate enters A"
  - "an individual duty"
  - "and SHOULD NOT enter D for a generic prescription or"
  - "and an actual A.21 GateDecisionResult"
  - "and authority-looking synonyms trigger the A.6 A6-AW-* branch: a current norm or grant enters D"
  - "are statement operators"
  - "atomic L/A/D/E rows"
  - "commitment or grant"
  - "dated Work"
  - "description and publication"
  - "exercise"
  - "four-question contract lens"
  - "gate"
  - "not ontology or quadrant selectors. MUST"
  - "obtaining versus representation"
  - "or evaluated finding enters E. If the wording does not expose the branch and direct object"
  - "or prohibition. MAY"
  - "promise content"
  - "recommendation-as-duty"
  - "rewrite it or mark it informative"
  - "separate result and evidence"
  - "speech-act Work"
  - "when separately instituted for an actual bearer"
---

### A.6.C:5 — Archetypal Grounding (Tell–Show–Show)

#### A.6.C:5.1 — Tell

When boundary contract-language leaves a consequential ambiguity, recover the actual claim and referent, then answer only the live questions below. Keep ordinary metonymy when its capable participant and relation are locally recoverable; a literal act or individual commitment needs that participant and the governing conditions.

1. **What was promised?** State the exact promise-content claim if one exists.
2. **What was said, published, or instituted?** Identify the speech-act Work, each description/publication object, and each institutional effect separately under its subject pattern.
3. **What governance or permission-looking claim exists?** State either a generic D prescription with its exact normative source and applicability, an individual D claim about an exact obtaining commitment with its actual bearer and institution basis, or the selected `A6-AW-*` claim in its own quadrant. State responsibility separately under its admitted domain predicate or return its exact missing governor.
4. **What happened, what followed, and what supports reliance?** State dated Work, each current result/change/delivery/acceptance claim, and each A.10 evidence claim separately; omit absent claims.

When those answers need stable reuse, decision, audit, dispute, or cross-face projection, write them in the one A.6.B Claim Register: one atomic statement, direct object, exact subject assertion, non-semantic pattern locator, and quadrant per row. Otherwise stop with the repaired atomic prose. Faces cite reused claim IDs or canonical locations; they do not create another bundle record.

#### A.6.C:5.2 — Show (System archetypes)

**(A) Software API boundary**

*Draft wording (contract soup):*
“The Payments API guarantees idempotency. Clients must provide `Idempotency-Key`. We log all requests. Availability is 99.9%.”

**Source clauses and additional illustrative premises:**

Preserve “We log all requests”; the draft supplies no particular logging Work or observation basis. “Availability is 99.9%” does not say whether 99.9% is a target, a promised bound, or an observed value; that meaning remains unresolved.

For the extended case below, assume the `PaymentsAPI` description/publication, definitions of idempotency and key uniqueness, a gate policy with an additional key-validity condition, and a generic provider-side idempotency prescription. These are additional case premises, not atoms recovered from the draft. The source's client requirement remains to provide `Idempotency-Key`.

* **Description/publication:** signature or mechanism publication for `PaymentsAPI` (MVPK faces: TechCard, InteropCard).
* **L:** define idempotency and the uniqueness semantics of `Idempotency-Key`.
  (“Idempotent” is a semantic property, not a duty.)
* **A:** admissibility predicate: request is admissible iff `Idempotency-Key` is present and valid.
  (Gate belongs to mechanism.)
* **D:** the API policy generically requires covered clients to provide `Idempotency-Key`. In this extended case it also states a provider-side idempotency prescription. No individual commitment follows from those clauses alone. If the case claims that `ClientIntegrator-A` or `ProviderSystem-A` bears one of those duties, cite that bearer's exact separately instituted A.2.8 commitment.
  (Responsibility, if claimed, needs its own direct relation.)
* **E — additional hypothetical evaluation:** suppose admitted system `PaymentsAvailabilityEvaluator-A` performed `AvailabilityEvaluation-Payments-T1 : U.Work` over the exact Payments API request population and window `T` using the availability metric stipulated for this evaluation. Exact A.6.1 application `PaymentsAvailabilityApplication-T1` has result binding `availabilityResult -> AvailabilityResult-Payments-T1`; that C.2.1 result episteme states `observedAvailability=99.9%` for `T`. When the SLA decision relies on this result, an A.10 path links it to the exact request-log and measurement carriers used. This hypothetical observation does not select the meaning of the draft's unlabeled 99.9%.

**(B) Hardware interface boundary**

*Draft wording:*
“The connector guarantees safe operation. Devices must not exceed 20V. Negotiation must succeed before power is applied.”

**Source requirements and additional illustrative premises:**

The draft leaves open whether “Devices must not exceed 20V” is a device-behavior constraint or an obligation on a capable bearer, and it does not identify the safe-operation predicate. Preserve the 20V upper bound and the requirement that negotiation succeed before power is applied. The additional gate and test below do not resolve the bearer or safety choices.

* **Description/publication — additional case premise:** assume a published interface spec supplying the pinout, electrical ranges, handshake procedure, and the test declaration used below.
* **L:** electrical invariants and allowable ranges are definitions and invariants (truth-conditional).
* **A — additional gate premise:** suppose the interface specification makes power delivery admissible only after the handshake state reaches an agreed mode.
* **Requirement awaiting classification:** retain “Devices must not exceed 20V”; recover its constraint or duty-bearer reading before assigning it to L or D. The negotiation-before-power requirement remains distinct from the additional gate predicate.
* **E — additional hypothetical test:** suppose admitted system `HardwareTestSystem-A` performed `ConnectorSafetyEvaluation-T1 : U.Work` over `Connector-C1` under the declared method, load, and temperature window. Exact A.6.1 application `ConnectorSafetyApplication-T1` has result binding `safetyResult -> ConnectorSafetyResult-T1`; that C.2.1 result episteme states `maximumObservedVoltage=19.8V`, `handshakeState=agreed-before-power`, and `ConnectorSafetyCriterion-v3=satisfied` for those conditions. When relied on, an A.10 path links this result to exact `TestReport-C1-T1`, `VoltageTrace-C1-T1`, and `NegotiationLog-C1-T1` carriers. In this hypothetical test, 19.8V is below the retained 20V upper bound. The separately given criterion result does not by itself settle the draft's unspecified safe-operation claim.

**(B-PER) Compact permission replay (only when the permission branch is live)**

*Situation:* “`ReleaseAuthoritySystem`, acting as release grantor under assignment `ReleaseGrantor-A`, approved `DeploymentAgent-A`, acting under assignment `Operator-A`, to deploy `Release-4711` after preflight.”

**Unpack + classify:**

* **Promise content (optional):** `SVC-RELEASE-4711` states which release artifact eligible consumers are promised.
* **Speech-act Work:** `ReleaseGrantorAssignment` is a declared `U.SystemRoleAssignment` species. Occurrence `ReleaseGrantor-A` has admitted System `ReleaseAuthoritySystem` as holder and the local release-grantor kind as assigned-kind value. That System performs dated `Approve` occurrence `SA-4711` under the assignment. The assignment supplies only the holder and assigned-kind facts used by the policy. Any authority required by `ReleaseGrantPolicy` must obtain independently. Under the applicable policy, `SA-4711` institutes—not merely publishes—grant occurrence `PER-4711` only if the A.2.8.PER obtaining conditions hold.
* **D — current grant (`A6-AW-NORM-GRANT`):** `ReleaseOperatorAssignment` is another declared species. Occurrence `Operator-A` has admitted System `DeploymentAgent-A` as holder and covers this window. The grant's beneficiary participant cites that occurrence, and its permitted-action participant is `U.EpistemeRef(Deploy-Release-4711)`. This Claim Register row uses `U.RelationRef(PER-4711)`, constrained to `GrantedPermissionRelation@Context`, as its `directObjectDesignation`. `SA-4711`, the two assignments, policy, context, scope, and window remain grounds or qualifiers. The model may use this D claim only while the A.2.8.PER conditions make `PER-4711` obtain and the row cites the named occurrence, act, and policy.
* **E — weak evaluation alternative (`A6-AW-WEAK`):** if the basis establishes only current absence of prohibition in a sufficiently complete frame, record `NonProhibitionFinding@Context`; do not promote it to a strong grant or place it in D.
* **A — independent entry predicate (`A6-AW-GATE`):** “deployment is admissible iff `PER-4711` currently obtains and preflight is green” is an `A-*` predicate. It may consume the grant as one condition but is neither the grant nor proof of gate passage. If an actual gate decision is also asserted, record its exact A.21 `GateDecisionResult`, bounded action, applicable profile application, complete required check-application result set, decision value, and consequence as a separate E claim.
* **E — actual Work and exercise (`A6-AW-EXERCISE`):** A.13 first recovers admitted System `DeploymentAgent-A` as the exact actual performer through obtaining assignment occurrence `Operator-A` of declared species `ReleaseOperatorAssignment`; A.15.1 independently admits dated `U.Work` occurrence `DeployRun-4711`. Because this permission-exercise branch expressly consumes precise assignment-bound attribution, F.6 then relates that already admitted Work through the same assignment and checks holder equality and coverage. The Work must instantiate the action specification inside the grant's scope and window. Only then may `PermissionExerciseRelation@Context` bind `WorkRef(DeployRun-4711)` to `U.RelationRef(PER-4711)`, constrained to `GrantedPermissionRelation@Context`. The assignment contributes the beneficiary and attribution facts consumed here. Failed F.6 leaves the Work intact but blocks this attribution-dependent exercise branch. Planned work, the approval wording, and preflight alone are not exercise.
* **E — optional result or delivery:** if `DeployRun-4711` returns `ReleaseArtifact-4711`, cite the exact A.6.1 result binding or an already governed subject-specific `WorkResultRelation`; if that artifact is transferred, cite the independently obtaining delivery/transfer relation defined by its subject pattern.
* **E — evidence (optional):** an A.10 path may link the exact grant, Work, exercise, result, or delivery claim to its current carriers for one bounded reliance use.

#### A.6.C:5.3 — Show (Episteme archetypes)

**(C) Multiparty protocol boundary (behavioural and session-type motif)**

*Draft wording:*
“The protocol guarantees progress. Participants must follow the sequence.”

**Source clauses and additional illustrative premises:**

The progress guarantee still needs its semantic or operational meaning. For the illustrative case below, assume the published protocol description and the trace-admissibility criteria; the named trace evaluation is an additional hypothetical case.

* **Description/publication:** protocol description (could be a type spec or protocol spec plus explanatory views).
* **L — when the guarantee is semantic:** the progress property is a law over the protocol model (truth-conditional, within the theory).
* **A:** admissibility: when an interaction trace is considered valid or admissible (e.g., runtime checks; compilation checks; gating conditions for entering a session).
* **D:** the protocol description generically requires covered participants to follow the stated sequence. It asserts no individual commitment occurrence.
* **E — additional hypothetical trace evaluation, not inferred from the progress guarantee:** suppose admitted system `ProtocolConformanceEvaluator-A` performed `ProtocolConformanceRun-T1 : U.Work` over bounded interaction `Trace-42`. Exact A.6.1 application `ProtocolConformanceApplication-T1` has result binding `conformanceResult -> ProtocolConformanceResult-T1`; that C.2.1 result episteme states `conformanceVerdict=pass` and `observedTerminalState=completed` under `ProtocolConformanceCriterion-v5`. For a disputed interaction, an A.10 path links this result to exact `MessageTrace-42`, `ConformanceRunRecord-T1`, and `ProtocolAuditRecord-42` carriers.

**(D) Socio-technical “SLA + audit trail” boundary**

*Draft wording:*
“Provider shall respond within 4 hours for Severity‑1 incidents. Only Severity‑1 is covered. Evidence is provided by ticket logs.”

**Unpack + classify:**

* **Promise content (service promise clause, when present):** a responsiveness promise for a defined incident class and window is separate from the SLA's generic prescription.
* **Description/publication:** SLA publication (and its views for different audiences).
* **A:** admissibility predicate for the promise: ticket qualifies iff severity classification meets stated conditions.
* **D:** the SLA clause generically requires the covered Provider to respond within 4 hours for Severity-1 incidents; only Severity-1 is covered. Claim that actual provider `ProviderSystem-A` bears the four-hour duty only after the SLA's individualizing rule and required actual basis establish one exact A.2.8 commitment; otherwise keep the clause generic.
* **Evidence source clause:** the draft names ticket logs as evidence; it supplies no measured response interval.
* **E — additional hypothetical response evaluation:** suppose admitted system `SLAEvaluator-A` performed `ResponseEvaluation-Ticket-17 : U.Work` over Severity-1 ticket `Ticket-17` under the declared clock and measurement method. Exact A.6.1 application `ResponseMeasurementApplication-Ticket-17` has result binding `responseIntervalResult -> ResponseIntervalResult-Ticket-17`; that C.2.1 result episteme states `observedResponseInterval=3h42m` and `withinFourHourTarget=true`. When the SLA decision relies on this result, an A.10 path links it to exact ticket, response-timestamp, clock-source, and severity-classification carriers. The four-hour requirement is from the source; `3h42m` is the additional hypothetical observation.


---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__006_archetypal-grounding-tell-show-show.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 11968
line_end: 12054
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
  - "and authority-looking synonyms trigger the A.6 A6-AW-* branch: a current norm or grant enters D"
  - "are statement operators"
  - "atomic L/A/D/E rows"
  - "commitment or grant"
  - "dated Work"
  - "description and publication"
  - "four-question contract lens"
  - "gate"
  - "not ontology or quadrant selectors. MUST"
  - "obtaining versus representation"
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

If you use contract-language for a boundary, do not treat “the interface or specification” as an acting system. Instead:

1. **What was promised?** Record the exact promise-content claim if one exists.
2. **What was said, published, or instituted?** Give the speech-act Work, each description/publication object, and each institutional effect its own row and subject pattern.
3. **What governance or permission-looking claim exists?** Record either a generic D prescription with its exact normative source and applicability, an individual D claim about an exact obtaining commitment with its actual bearer and institution basis, or the selected `A6-AW-*` claim in its own quadrant. State responsibility separately under its admitted domain predicate or return its exact missing governor.
4. **What happened, what followed, and what supports reliance?** Record dated Work, each current result/change/delivery/acceptance claim, and each A.10 evidence claim separately; omit absent rows.

Write those answers in the one A.6.B Claim Register: one atomic statement, direct object, exact subject assertion, non-semantic pattern locator, and quadrant per row. Faces cite the claim IDs; they do not create another bundle record.

#### A.6.C:5.2 — Show (System archetypes)

**(A) Software API boundary**

*Draft wording (contract soup):*
“The Payments API guarantees idempotency. Clients must provide `Idempotency-Key`. We log all requests. Availability is 99.9%.”

**Unpack + classify:**

* **Description/publication:** signature or mechanism publication for `PaymentsAPI` (MVPK faces: TechCard, InteropCard).
* **L:** define idempotency and the uniqueness semantics of `Idempotency-Key`.
  (“Idempotent” is a semantic property, not a duty.)
* **A:** admissibility predicate: request is admissible iff `Idempotency-Key` is present and valid.
  (Gate belongs to mechanism.)
* **D:** the API policy generically requires covered clients to satisfy the gate and states the provider-side idempotency and availability prescriptions. No individual commitment follows from those clauses alone. If the case claims that `ClientIntegrator-A` or `ProviderSystem-A` bears one of those duties, cite that bearer's exact separately instituted A.2.8 commitment.
  (Do not say “the API commits”. Responsibility, if claimed, needs its own direct relation.)
* **E:** evidence expectations: audit and log carriers include request id, idempotency key, rejection reason; availability measurement uses defined window and signal definition.

**(B) Hardware interface boundary**

*Draft wording:*
“The connector guarantees safe operation. Devices must not exceed 20V. Negotiation must succeed before power is applied.”

**Unpack + classify:**

* **Description/publication:** published interface spec (pinout, electrical ranges, handshake procedure).
* **L:** electrical invariants and allowable ranges are definitions and invariants (truth-conditional).
* **A:** admissibility predicate: power delivery is admissible only after handshake state reaches an agreed mode.
* **D:** the interface specification's normative section contains generic prescriptions for covered manufacturers or integrators to implement the handshake and enforce voltage limits; it asserts no individual commitment occurrence.
* **E:** evidence: test-report carriers; measurement traces; observable negotiation logs (if exposed), or lab measurements under a declared method.

**(B-PER) Compact permission replay (only when the permission branch is live)**

*Situation:* “`ReleaseAuthoritySystem`, acting as release grantor under assignment `ReleaseGrantor-A`, approved `DeploymentAgent-A`, acting under assignment `Operator-A`, to deploy `Release-4711` after preflight.”

**Unpack + classify:**

* **Promise content (optional):** `SVC-RELEASE-4711` states which release artifact eligible consumers are promised; that content establishes no speech act, commitment, grant, deployment Work, result, or delivery.
* **Speech-act Work:** `ReleaseGrantorAssignment` is a declared `U.SystemRoleAssignment` species. Occurrence `ReleaseGrantor-A` has admitted System `ReleaseAuthoritySystem` as holder and the local release-grantor kind as assigned-kind value. That System performs dated `Approve` occurrence `SA-4711` under the assignment. The assignment supplies only the holder and assigned-kind facts used by the policy; it neither performs the act nor supplies authority. Any authority required by `ReleaseGrantPolicy` must obtain independently. Under the applicable policy, `SA-4711` institutes—not merely publishes—grant occurrence `PER-4711` only if the A.2.8.PER obtaining conditions hold. Approval text and a register row that names `PER-4711` do not establish that fact.
* **D — current grant (`A6-AW-NORM-GRANT`):** `ReleaseOperatorAssignment` is another declared species. Occurrence `Operator-A` has admitted System `DeploymentAgent-A` as holder and covers this window. The grant's beneficiary participant cites that occurrence, and its permitted-action participant is `U.EpistemeRef(Deploy-Release-4711)`. This Claim Register row uses `U.RelationRef(PER-4711)`, constrained to `GrantedPermissionRelation@Context`, as its `directObjectDesignation`. `SA-4711`, the two assignments, policy, context, scope, and window remain grounds or qualifiers. The model may use this D claim only while the A.2.8.PER conditions make `PER-4711` obtain and the row cites the named occurrence, act, and policy; the row itself does not make the grant current.
* **E — weak evaluation alternative (`A6-AW-WEAK`):** if the basis establishes only current absence of prohibition in a sufficiently complete frame, record `NonProhibitionFinding@Context`; do not promote it to a strong grant or place it in D.
* **A — independent entry predicate (`A6-AW-GATE`):** “deployment is admissible iff `PER-4711` currently obtains and preflight is green” is an `A-*` predicate. It may consume the grant as one condition but is neither the grant nor proof of gate passage.
* **E — actual Work and exercise (`A6-AW-EXERCISE`):** A.13 first recovers admitted System `DeploymentAgent-A` as the exact actual performer through obtaining assignment occurrence `Operator-A` of declared species `ReleaseOperatorAssignment`; A.15.1 independently admits dated `U.Work` occurrence `DeployRun-4711`. Because this permission-exercise branch expressly consumes precise assignment-bound attribution, F.6 then relates that already admitted Work through the same assignment and checks holder equality and coverage. The Work must instantiate the action specification inside the grant's scope and window. Only then may `PermissionExerciseRelation@Context` bind `WorkRef(DeployRun-4711)` to `U.RelationRef(PER-4711)`, constrained to `GrantedPermissionRelation@Context`. The assignment contributes the beneficiary and attribution facts consumed here; it neither classifies the performer, grounds or creates performance, nor performs the Work. Failed F.6 leaves the Work intact but blocks this attribution-dependent exercise branch. Planned work, the approval wording, and preflight alone are not exercise.
* **E — optional result or delivery:** if `DeployRun-4711` returns `ReleaseArtifact-4711`, cite the exact A.6.1 result binding or an already governed subject-specific `WorkResultRelation`; if that artifact is transferred, cite the independently obtaining delivery/transfer relation defined by its subject pattern. Work, result, and delivery do not imply one another.
* **E — evidence (optional):** an A.10 path may link the exact grant, Work, exercise, result, or delivery claim to its current carriers for one bounded reliance use. The carriers create none of those objects.

#### A.6.C:5.3 — Show (Episteme archetypes)

**(C) Multiparty protocol boundary (behavioural and session-type motif)**

*Draft wording:*
“The protocol guarantees progress. Participants must follow the sequence.”

**Unpack + classify:**

* **Description/publication:** protocol description (could be a type spec or protocol spec plus explanatory views).
* **L:** safety and progress properties as laws over the protocol model (truth-conditional, within the theory).
* **A:** admissibility: when an interaction trace is considered valid or admissible (e.g., runtime checks; compilation checks; gating conditions for entering a session).
* **D:** the protocol description carries generic prescriptions for covered implementers or operators: implement the protocol, do not send messages outside the state machine, and publish conformance records when required. It asserts no individual commitment occurrence.
* **E:** evidence: message trace carriers, conformance test-run records, and audit trails for disputed interactions.

**(D) Socio-technical “SLA + audit trail” boundary**

*Draft wording:*
“Provider shall respond within 4 hours for Severity‑1 incidents. Only Severity‑1 is covered. Evidence is provided by ticket logs.”

**Unpack + classify:**

* **Promise content (service promise clause):** responsiveness promise for a defined incident class and window.
* **Description/publication:** SLA publication (and its views for different audiences).
* **A:** admissibility predicate for the promise: ticket qualifies iff severity classification meets stated conditions.
* **D:** the SLA clause is first a generic prescription for covered providers, clients, and auditors. Claim that actual provider `ProviderSystem-A` bears the four-hour duty only after the SLA's individualizing rule and required actual basis establish one exact A.2.8 commitment; otherwise keep the clause generic.
* **E:** evidence: ticket carriers, timestamps, classification records, and the measurement procedure binding “4 hours” to a time window and clock source.


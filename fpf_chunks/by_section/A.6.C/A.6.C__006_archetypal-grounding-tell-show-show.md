---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__006_archetypal-grounding-tell-show-show.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 10424
line_end: 10510
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.8"
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
  - "and SHOULD NOT enter D only for an accountable duty"
  - "and authority-looking synonyms trigger the A.6 A6-AW-* branch: a current norm/grant enters D"
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
---

### A.6.C:5 — Archetypal Grounding (Tell–Show–Show)

#### A.6.C:5.1 — Tell

If you use contract-language for a boundary, do not treat “the interface or specification” as an acting system. Instead:

1. **What was promised?** Record the exact promise-content claim if one exists.
2. **What was said, published, or instituted?** Give the speech-act Work, each description/publication object, and each institutional effect its own row and direct owner.
3. **What governance or permission-looking claim exists?** Record the accountable commitment or selected `A6-AW-*` claim with its own participants, source, and quadrant.
4. **What happened, what followed, and what supports reliance?** Record dated Work, each current result/change/delivery/acceptance claim, and each A.10 evidence claim separately; omit absent rows.

Write those answers in the one A.6.B Claim Register: one atomic statement, direct object, owner, and quadrant per row. Faces cite the claim IDs; they do not create another bundle record.

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
* **D:** client implementers are obligated to satisfy the gate; provider implementers are accountable for the idempotency behavior **as defined in L** when the gate holds; provider commits to the availability target (scoped by window and exclusions).
  (Name the committing role; do not say “the API commits”.)
* **E:** evidence expectations: audit and log carriers include request id, idempotency key, rejection reason; availability measurement uses defined window and signal definition.

**(B) Hardware interface boundary**

*Draft wording:*
“The connector guarantees safe operation. Devices must not exceed 20V. Negotiation must succeed before power is applied.”

**Unpack + classify:**

* **Description/publication:** published interface spec (pinout, electrical ranges, handshake procedure).
* **L:** electrical invariants and allowable ranges are definitions and invariants (truth-conditional).
* **A:** admissibility predicate: power delivery is admissible only after handshake state reaches an agreed mode.
* **D:** manufacturer or integrator obligations: implement handshake; enforce voltage constraints.
* **E:** evidence: test-report carriers; measurement traces; observable negotiation logs (if exposed), or lab measurements under a declared method.

**(B-PER) Compact permission replay (only when the permission branch is live)**

*Situation:* “`ReleaseAuthoritySystem`, acting as release grantor under assignment `ReleaseGrantor-A`, approved `DeploymentAgent-A`, acting under assignment `Operator-A`, to deploy `Release-4711` after preflight.”

**Unpack + classify:**

* **Promise content (optional):** `SVC-RELEASE-4711` states which release artifact eligible consumers are promised; that content establishes no speech act, commitment, grant, deployment Work, result, or delivery.
* **Speech-act Work:** `ReleaseAuthoritySystem`, an admitted `U.System`, performs dated `Approve` occurrence `SA-4711` under exact obtaining grantor assignment `RoleAssignmentRef(ReleaseGrantor-A)`. That assignment's `HolderSystemSlot` names `ReleaseAuthoritySystem`; the assignment supplies role and authority but does not perform the act. Under current `ReleaseGrantPolicy`, `SA-4711` institutes—not merely publishes—grant occurrence `PER-4711` only if the A.2.8.PER obtaining conditions hold. Approval text and a register row that names `PER-4711` do not establish that fact.
* **D — current grant (`A6-AW-NORM-GRANT`):** the grant's beneficiary participant is `RoleAssignmentRef(Operator-A)`, held for this window by admitted operator `U.System` `DeploymentAgent-A`; its permitted-action participant is `U.EpistemeRef(Deploy-Release-4711)`. `SA-4711`, `RoleAssignmentRef(ReleaseGrantor-A)`, policy, context, scope, and window remain ground or qualifiers. The model may use this D claim only while those A.2.8.PER conditions make `PER-4711` obtain and the row cites that exact occurrence, act, and policy; the row itself does not make the grant current.
* **E — weak evaluation alternative (`A6-AW-WEAK`):** if the basis establishes only current absence of prohibition in a sufficiently complete frame, record `NonProhibitionFinding@Context`; do not promote it to a strong grant or place it in D.
* **A — independent entry predicate (`A6-AW-GATE`):** “deployment is admissible iff `PER-4711` currently obtains and preflight is green” is an `A-*` predicate. It may consume the grant as one condition but is neither the grant nor proof of gate passage.
* **E — actual Work and exercise (`A6-AW-EXERCISE`):** admitted operator `U.System` `DeploymentAgent-A` must first perform dated `U.Work` occurrence `DeployRun-4711` under `RoleAssignmentRef(Operator-A)`. That assignment must cover the Work, and the Work must instantiate the action specification inside the grant's scope and window. Only then may `PermissionExerciseRelation@Context` bind `WorkRef(DeployRun-4711)` to `U.EntityRef(PER-4711)`. The assignment grounds the performance and beneficiary match; it does not perform the Work. Planned work, the approval wording, and preflight alone are not exercise.
* **E — optional result or delivery:** if `DeployRun-4711` returns `ReleaseArtifact-4711`, cite the exact A.6.1 result binding or an already governed subject-specific `WorkResultRelation`; if that artifact is transferred, cite the independently obtaining subject-owned delivery/transfer relation. Work, result, and delivery do not imply one another.
* **E — evidence (optional):** an A.10 path may link the exact grant, Work, exercise, result, or delivery claim to its current carriers for one bounded reliance use. The carriers create none of those objects.

#### A.6.C:5.3 — Show (Episteme archetypes)

**(C) Multiparty protocol boundary (behavioural and session-type motif)**

*Draft wording:*
“The protocol guarantees progress. Participants must follow the sequence.”

**Unpack + classify:**

* **Description/publication:** protocol description (could be a type spec or protocol spec plus explanatory views).
* **L:** safety and progress properties as laws over the protocol model (truth-conditional, within the theory).
* **A:** admissibility: when an interaction trace is considered valid or admissible (e.g., runtime checks; compilation checks; gating conditions for entering a session).
* **D:** obligations on implementers or operators: implement the protocol; do not send messages outside the allowed state machine; publish conformance records if required.
* **E:** evidence: message trace carriers, conformance test-run records, and audit trails for disputed interactions.

**(D) Socio-technical “SLA + audit trail” boundary**

*Draft wording:*
“Provider shall respond within 4 hours for Severity‑1 incidents. Only Severity‑1 is covered. Evidence is provided by ticket logs.”

**Unpack + classify:**

* **Promise content (service promise clause):** responsiveness promise for a defined incident class and window.
* **Description/publication:** SLA publication (and its views for different audiences).
* **A:** admissibility predicate for the promise: ticket qualifies iff severity classification meets stated conditions.
* **D:** provider commitment to meet the target; client duties (e.g., provide required info); auditor duties if applicable.
* **E:** evidence: ticket carriers, timestamps, classification records, and the measurement procedure binding “4 hours” to a time window and clock source.


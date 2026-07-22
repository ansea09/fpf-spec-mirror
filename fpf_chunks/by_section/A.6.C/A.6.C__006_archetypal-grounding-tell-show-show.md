---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__006_archetypal-grounding-tell-show-show.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 10266
line_end: 10348
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
  - "(RFC 2119 + RFC 8174)"
  - "A as predicates (“is admissible iff…”)"
  - "Boundary Norm Square (L/A/D/E)"
  - "MVPK faces “no new semantics”"
  - "RECOMMENDED"
  - "REQUIRED"
  - "SLA/guarantee claim classification"
  - "accountable commitment vs exact permission result"
  - "and E as observable/evidenced properties. If a BCP‑14 keyword or synonym appears in an L/A/E claim"
  - "and OPTIONAL"
  - "as a disciplined modality family"
  - "contract bundle unpacking"
  - "exercise"
  - "finding"
  - "in L/A/E claims"
  - "including common synonyms such as SHALL"
  - "non-violation"
  - "permission projections cite the corresponding D- and exact A.2.8.PER grant"
  - "phrase L as definitions or invariants (“is defined as…”"
  - "promise content ≠ work"
  - "promise-act/utterance separation"
  - "the face is non-conformant until rewritten without the BCP‑14 keyword or moved out of the face"
  - "the sentence MUST be rewritten to remove the keyword or moved out of the face"
  - "“holds iff…”)"
---

### A.6.C:5 — Archetypal Grounding (Tell–Show–Show)

#### A.6.C:5.1 — Tell

If you use contract-language for a boundary, do not treat “the interface or specification” as an acting system. Instead:

1. Identify the **promise content** (promise content) being promised,
2. Identify the accountable **Commitment** holder(s) for a duty/recommendation/prohibition branch; when permission is current, identify the exact `A.2.8.PER` grant, finding, exercise, non-violation, or conflict result and preserve that object's own participants and references,
3. Identify the **Utterance** surfaces that publish the boundary (signature or mechanism descriptions plus MVPK views),
4. Identify the **Performed work and evidence** carriers that could adjudicate whether commitments were met or whether actual work exercised a grant or was non-violating in the checked frame,
5. Classify each claim through **L/A/D/E** and reference across quadrants rather than paraphrasing.

#### A.6.C:5.2 — Show (System archetypes)

**(A) Software API boundary**

*Draft wording (contract soup):*
“The Payments API guarantees idempotency. Clients must provide `Idempotency-Key`. We log all requests. Availability is 99.9%.”

**Unpack + classify:**

* **Utterance:** signature or mechanism publication for `PaymentsAPI` (MVPK faces: TechCard, InteropCard).
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

* **Utterance:** published interface spec (pinout, electrical ranges, handshake procedure).
* **L:** electrical invariants and allowable ranges are definitions and invariants (truth-conditional).
* **A:** admissibility predicate: power delivery is admissible only after handshake state reaches an agreed mode.
* **D:** manufacturer or integrator obligations: implement handshake; enforce voltage constraints.
* **E:** evidence: test-report carriers; measurement traces; observable negotiation logs (if exposed), or lab measurements under a declared method.

**(B-PER) Compact permission replay (only when the permission branch is live)**

*Situation:* “ReleaseAuthority approved Operator-A to deploy Release-4711; deployment is allowed after preflight.”

**Unpack + classify:**

* **Utterance and institution:** the dated `Approve` speech-act occurrence `SA-4711`, performed by the exact grantor assignment under current `ReleaseGrantPolicy`, institutes—not merely publishes—the separately represented grant occurrence `PER-4711`. Approval text without that policy and act does not create the grant.
* **D — permission result:** `GrantedPermissionRelation@Context` names beneficiary `RoleAssignmentRef(Operator-A)` and `permittedActionSpecificationRef = U.EpistemeRef(Deploy-Release-4711)`; `SA-4711`, the grantor assignment, policy, context, scope, and window remain ground or qualifiers. If the available basis establishes only current absence of prohibition, record `NonProhibitionFinding@Context` instead and do not promote it to a strong grant.
* **A — independent entry predicate:** “deployment is admissible iff `PER-4711` currently obtains and preflight is green” is an `A-*` predicate. It may consume the grant as one condition but is neither the grant nor proof of gate passage.
* **Work and exercise:** only after later dated actual `U.Work` occurrence `DeployRun-4711` exists, instantiates the action specification, matches the beneficiary branch, and stays inside the grant's scope and window may `PermissionExerciseRelation@Context` bind `WorkRef(DeployRun-4711)` to `U.EntityRef(PER-4711)`. Planned work, the approval wording, and preflight alone are not exercise.
* **E:** speech-act, policy-edition, grant-occurrence, preflight, work, and observation carriers support the classified claims without replacing their direct objects.

#### A.6.C:5.3 — Show (Episteme archetypes)

**(C) Multiparty protocol boundary (behavioural and session-type motif)**

*Draft wording:*
“The protocol guarantees progress. Participants must follow the sequence.”

**Unpack + classify:**

* **Utterance:** protocol description (could be a type spec or protocol spec plus explanatory views).
* **L:** safety and progress properties as laws over the protocol model (truth-conditional, within the theory).
* **A:** admissibility: when an interaction trace is considered valid or admissible (e.g., runtime checks; compilation checks; gating conditions for entering a session).
* **D:** obligations on implementers or operators: implement the protocol; do not send messages outside the allowed state machine; publish conformance records if required.
* **E:** evidence: message trace carriers, conformance test-run records, and audit trails for disputed interactions.

**(D) Socio-technical “SLA + audit trail” boundary**

*Draft wording:*
“Provider shall respond within 4 hours for Severity‑1 incidents. Only Severity‑1 is covered. Evidence is provided by ticket logs.”

**Unpack + classify:**

* **Promise content (service promise clause):** responsiveness promise for a defined incident class and window.
* **Utterance:** SLA publication (and its views for different audiences).
* **A:** admissibility predicate for the promise: ticket qualifies iff severity classification meets stated conditions.
* **D:** provider commitment to meet the target; client duties (e.g., provide required info); auditor duties if applicable.
* **E:** evidence: ticket carriers, timestamps, classification records, and the measurement procedure binding “4 hours” to a time window and clock source.


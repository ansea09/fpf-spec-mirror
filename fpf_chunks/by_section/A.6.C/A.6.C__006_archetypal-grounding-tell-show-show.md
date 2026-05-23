---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__006_archetypal-grounding-tell-show-show.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 8601
line_end: 8671
dependencies:
  - "A.15.1"
  - "A.2.3"
  - "A.2.4"
  - "A.2.8"
  - "A.2.9"
  - "A.6"
  - "A.6.8"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "E.10"
  - "E.17"
  - "F.12"
  - "F.18"
  - "U.Commitment"
  - "U.EvidenceRole"
  - "U.PromiseContent"
  - "U.SpeechAct"
  - "U.Work"
keywords:
  - "(RFC 2119 + RFC 8174)"
  - "(e.g"
  - "A as predicates (“is admissible iff…”)"
  - "Boundary Norm Square (L/A/D/E)"
  - "MVPK faces “no new semantics”"
  - "OPTIONAL)"
  - "RECOMMENDED"
  - "REQUIRED"
  - "SLA/guarantee claim classification"
  - "and E as observable/evidenced properties. If a BCP‑14 keyword (or synonym) appears in an L/A/E claim"
  - "as a disciplined modality family"
  - "contract bundle unpacking"
  - "in L/A/E claims"
  - "including common synonyms (SHALL"
  - "phrase L as definitions/invariants (“is defined as…”"
  - "promise content (promise content) ≠ work"
  - "promise-act/utterance/commitment separation"
  - "the face is non‑conformant until rewritten (no BCP‑14 keyword) or moved out of the face"
  - "turn it into explanatory prose that cites the relevant claim IDs) or moved out of the face"
  - "“holds iff…”)"
---

### A.6.C:5 — Archetypal Grounding (Tell–Show–Show)

#### A.6.C:5.1 — Tell

If you use contract-language for a boundary, do not treat “the interface/spec” as an agent. Instead:

1. Identify the **promise content** (promise content) being promised,
2. Identify the accountable **Commitment** holder(s) (roles/agents),
3. Identify the **Utterance** surfaces that publish the boundary (signature/mechanism + MVPK views),
4. Identify the **Work + Evidence** carriers that could adjudicate whether commitments were met,
5. Route each claim through **L/A/D/E** and reference across quadrants rather than paraphrasing.

#### A.6.C:5.2 — Show (System archetypes)

**(A) Software API boundary**

*Draft wording (contract soup):*
“The Payments API guarantees idempotency. Clients must provide `Idempotency-Key`. We log all requests. Availability is 99.9%.”

**Unpack + route:**

* **Utterance:** signature/mechanism publication for `PaymentsAPI` (MVPK faces: TechCard, InteropCard).
* **L:** define idempotency and the uniqueness semantics of `Idempotency-Key`.
  (“Idempotent” is a semantic property, not a duty.)
* **A:** admissibility predicate: request is admissible iff `Idempotency-Key` is present and valid.
  (Gate belongs to mechanism.)
* **D:** client implementers are obligated to satisfy the gate; provider implementers are accountable for the idempotency behavior **as defined in L** when the gate holds; provider commits to the availability target (scoped by window/exclusions).
  (Name the committing role; do not say “the API commits”.)
* **E:** evidence expectations: audit/log carriers include request id, idempotency key, rejection reason; availability measurement uses defined window and signal definition.

**(B) Hardware interface boundary**

*Draft wording:*
“The connector guarantees safe operation. Devices must not exceed 20V. Negotiation must succeed before power is applied.”

**Unpack + route:**

* **Utterance:** published interface spec (pinout, electrical ranges, handshake procedure).
* **L:** electrical invariants / allowable ranges are definitions and invariants (truth-conditional).
* **A:** admissibility predicate: power delivery is admissible only after handshake state reaches an agreed mode.
* **D:** manufacturer/integrator obligations: implement handshake; enforce voltage constraints.
* **E:** evidence: test-report carriers; measurement traces; observable negotiation logs (if exposed), or lab measurements under a declared method.

#### A.6.C:5.3 — Show (Episteme archetypes)

**(C) Multiparty protocol boundary (behavioural/session type motif)**

*Draft wording:*
“The protocol guarantees progress. Participants must follow the sequence.”

**Unpack + route:**

* **Utterance:** protocol description (could be a type/protocol spec plus explanatory views).
* **L:** safety/progress properties as laws over the protocol model (truth-conditional, within the theory).
* **A:** admissibility: when an interaction trace is considered valid/admissible (e.g., runtime checks; compilation checks; gating conditions for entering a session).
* **D:** obligations on implementers/operators: implement the protocol; do not send messages outside the allowed state machine; publish conformance records if required.
* **E:** evidence: message trace carriers, conformance test-run records, and audit trails for disputed interactions.

**(D) Socio-technical “SLA + audit trail” boundary**

*Draft wording:*
“Provider shall respond within 4 hours for Severity‑1 incidents. Only Severity‑1 is covered. Evidence is provided by ticket logs.”

**Unpack + route:**

* **Promise content (service promise clause):** responsiveness promise for a defined incident class and window.
* **Utterance:** SLA publication (and its views for different audiences).
* **A:** admissibility predicate for the promise: ticket qualifies iff severity classification meets stated conditions.
* **D:** provider commitment to meet the target; client duties (e.g., provide required info); auditor duties if applicable.
* **E:** evidence: ticket carriers, timestamps, classification records, and the measurement procedure binding “4 hours” to a time window and clock source.


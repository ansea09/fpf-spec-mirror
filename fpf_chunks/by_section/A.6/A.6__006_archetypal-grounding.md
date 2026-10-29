---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack: Classify and Place Boundary Claims"
section_id: "A.6:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__006_archetypal-grounding.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "A.6 — Signature Stack: Classify and Place Boundary Claims"
  - "A.6:5 — Archetypal Grounding"
line_start: 14002
line_end: 14068
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.8.PER"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
keywords:
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "Work versus non-Work effect"
  - "acceptance"
  - "actual occurrence"
  - "and evidence"
  - "atomic L/A/D/E claims"
  - "delivery"
  - "in invariants"
  - "publication face"
  - "reference predicates by ID or canonical location from CC when needed"
  - "separate result"
  - "signature and mechanism declarations"
  - "six-way authority-word branch"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:5 - Archetypal Grounding

> **Informative.** Worked examples for learning the L/A/D/E claim-classification discipline; they do not add requirements beyond A.6:7.

#### A.6:5.1 - Apply the same classification to different boundary subjects

The two cases below distinguish declaration, admissibility, governance and actual effect or evidence claims. Classification determines where a claim belongs; its subject pattern determines whether the claimed object or relation obtains. Keep that object distinct from the episteme stating the claim and its publication carrier.

#### A.6:5.2 - Payment-processing System and its API boundary

**System:** the payment-processing System supplying the “Payment Authorize” service.

* **Signature layer (A.6.0).**

  * Vocabulary: `PaymentRequest`, `AuthDecision`, `MerchantId`, `Money`, etc.
  * Laws: e.g., “If decision is APPROVED then reservedAmount = requestedAmount” (truth‑conditional).
  * Applicability: bounded context “Payments Authorization”.

* **Mechanism layer (A.6.1).**

  * Admissibility gate: request is admissible iff `tokenValid ∧ merchantActive ∧ amountWithinLimit`.
  * Boundary transport details: HTTP headers and idempotency-key carriage. Declare canonical currency-conversion operations under A.6.1.
  * The local Audit and observability section specifies required evidence carriers (e.g., `AuthorizationRecord` event, log entry) and their fields, correlation IDs and retention class. Retention duties remain D-claims.

* **Actual occurrence and work layer.**

  * The payment-handling occurrence is `U.Work` only when its exact actual performer first has the A.13 core and A.15.1 independently admits the occurrence from its Method, time, containing System, and other required direct facts. If this payment account also asks under which assignment the performer acted, add F.6 through the same obtaining A.13 assignment; missing or failed attribution leaves the payment Work intact.
  * The ledger reservation change, event emission, timer transition, or retry effect is a separate actual-occurrence claim under A.3/A.3.4 or its exact interaction or causal-use pattern. Check each effect separately: knowing that the payment Work occurred does not show that the ledger changed, an event was emitted, or a retry happened.
  * Traces, logs, and metrics enter an A.10 evidence path for the exact effect being relied on; carrier presence creates neither Work nor change.
* **Publication faces (MVPK).**

  * PlainView: narrative for stakeholders (what the service promise is, in plain terms).
  * TechCard: signature or mechanism details (types, error codes, version policy, admissibility predicate refs).
  * InteropCard: machine‑exchange oriented boundary details (canonical field names, schema refs, transport bindings).
  * AssuranceLane: evidence bindings (which carriers exist, how to adjudicate `E-*` claims, retention and access duties by reference).

**Effects-and-handlers analogy.** In this software example, the signature exposes the operation interface. A.6.1 governs declared operation semantics and the separate realization relation; the realizing entity supplies the concrete handler implementation. Implementations can change while preserving the declared operation meanings and applicable constraints.

**Classification example:**

* “A request is admissible iff `tokenValid ∧ merchantActive ∧ amountWithinLimit`” belongs in Quadrant A (the declared admissibility gate).
* “Clients MUST include Idempotency-Key” is a D prescription. If an admission rule also requires that header, reference that rule’s predicate; the three-condition predicate above does not include it. An obtaining individual `U.Commitment` additionally needs the actual bearer, constitutive rule, instituting basis and direct predicate under A.2.8.
* “System emits AuthorizationRecord” is ambiguous between a generic emission rule and an actual event report. Only the actual-event reading belongs in E, with its occurrence basis supplied; the wording alone does not choose that reading.

#### A.6:5.3 - Published evaluation protocol

**Episteme:** A published “Model Evaluation Protocol” for a safety‑critical classifier.

* **Signature layer:** names operations such as `Evaluate(model, dataset) → Report` and states metric definitions (AUROC, calibration error) as Laws. A.6.1 governs the corresponding operation declaration and its argument/result meanings.

* **Mechanism layer:** the entry predicate requires the declared dataset/license condition, measurement-environment constraints and pinned seeds. Classify a separate institutional permission claim under its own `A6-AW-*` branch when one is made.

* **Deontics and commitments:** the protocol may prescribe that reviewers use dataset vX.Y and that authors publish MVPK faces and cite the measurement environment. If an organisation has an individual review-SLA duty, identify that actual admitted System or other A.2.8 party as bearer and establish the direct `U.Commitment` predicate. Any system-role classification or assignment remains a separate possible applicability ground.

* **Effects and evidence:** the dated evaluation run is a Work occurrence only when A.15.1 grounds it; its result episteme, any model or dataset change, and the report publication remain separate. Report files, logs, hashes, and trace IDs support the selected claims through A.10 but create none of those occurrences or results.

**Non-Work E contrast.** A seedling's spontaneous first-leaf unfolding can be an actual A.3.4 transformation with no performer, assignment, method, or Work occurrence. Measurements may support that exact change claim through A.10; neither the observation work nor its carrier becomes the change.

* **Multi‑view (MVPK face designators):**

  * PlainView for decision makers: what this protocol means for assurance.
  * TechCard for engineers: metric definitions named by value, admissibility predicates, and a clearly marked **Norms-and-commitments** section (D‑claims) for governance.
  * InteropCard for exchange-oriented consumers: conceptual field names, anchors, and schema references.
  * AssuranceLane for auditors: evidence map (which carriers support which occurrence claims) and adjudication steps keyed by `E-*` IDs.

This protocol description connects metric definitions with conditions for an evaluation and interpretation of its report. The signature stack keeps those claims available to their different uses.


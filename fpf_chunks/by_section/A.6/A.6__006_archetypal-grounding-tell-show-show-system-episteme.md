---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:5"
section_title: "Archetypal Grounding (Tell–Show–Show; System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__006_archetypal-grounding-tell-show-show-system-episteme.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:5 — Archetypal Grounding (Tell–Show–Show; System / Episteme)"
line_start: 8504
line_end: 8568
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.2.3"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.MultiViewDescribing"
  - "U.Signature"
  - "U.View"
  - "U.Viewpoint"
  - "U.Work"
keywords:
  - "A.6.B L/A/D/E claims"
  - "Confuses deontics with mathematical admissibility"
  - "MUST"
  - "Rewrite as declarative predicate"
  - "SHOULD"
  - "and MAY)"
  - "authority-wording split"
  - "boundary"
  - "boundary claim-classification fields"
  - "in invariants"
  - "probe/order/frame/export/state-reading claims"
  - "promise/commitment/API/policy wording"
  - "reference predicate IDs from CC when needed"
  - "register-backed status boundary"
  - "signature stack"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:5 - Archetypal Grounding (Tell–Show–Show; System / Episteme)

> **Informative.** Worked examples for learning the L/A/D/E claim-classification discipline; they do not add requirements beyond A.6:7.

#### Tell (universal rule)

A boundary description is evolvable iff its claims are separated across the signature stack and each statement is classified by the boundary discipline matrix to its proper layer (Laws, Admissibility, Deontics and commitments, Effects and evidence), while preserving EntityOfConcern and Description-episteme / publication-carrier separation.

#### Show #1 (`U.System`): effectful API boundary (algebraic effects intuition)

**System:** A “Payment Authorize” service.

* **Signature layer (A.6.0).**

  * Vocabulary: `PaymentRequest`, `AuthDecision`, `MerchantId`, `Money`, etc.
  * Laws: e.g., “If decision is APPROVED then reservedAmount = requestedAmount” (truth‑conditional).
  * Applicability: bounded context “Payments Authorization”.

* **Mechanism layer (A.6.1).**

  * Admissibility gate: request is admissible iff `tokenValid ∧ merchantActive ∧ amountWithinLimit`.
  * Transport: HTTP headers, idempotency key transport, canonical currency conversions.
  * Audit and observability: specifies required evidence carriers (e.g., `AuthorizationRecord` event, log entry) and their semantics (fields, correlation IDs, retention class).

* **Realization and work layer.**

  * Actual side effects: reservation entry in ledger, emission of event, timers, retries.
  * Evidence: traces, logs, metrics.

* **Publication faces (MVPK).**

  * PlainView: narrative for stakeholders (what the service promise is, in plain terms).
  * TechCard: signature or mechanism details (types, error codes, version policy, admissibility predicate refs).
  * InteropCard: machine‑exchange oriented boundary details (canonical field names, schema refs, transport bindings).
  * AssuranceLane: evidence bindings (which carriers exist, how to adjudicate `E-*` claims, retention and access duties by reference).

**SoTA tie‑in:** This boundary is naturally understood using *algebraic effects and handlers*: the signature is the “operation interface” (effect signature), while the mechanism or realization provides handlers (semantics). The stack keeps the abstract operation signature stable while allowing multiple handlers and realizations to evolve.

**Classification example:**

* “Defined iff tokenValid” belongs in Quadrant A (admissibility gate).
* “Clients MUST include Idempotency‑Key” belongs in Quadrant D (role-assignment or acting-system obligation) but should reference the same gate semantics to avoid divergence.
* “System emits AuthorizationRecord” belongs in Quadrant E (evidence via carriers).

#### Show #2 (`U.Episteme`): published evaluation protocol boundary (multi‑view + evidence)

**Episteme:** A published “Model Evaluation Protocol” for a safety‑critical classifier.

* **Signature layer:** defines operations like `Evaluate(model, dataset) → Report` and truth‑conditional definitions of metrics (AUROC, calibration error) as Laws.

* **Mechanism layer:** admissibility gate encodes when evaluation is permitted: dataset version must match declared license; measurement environment must meet constraints; seeds pinned.

* **Deontics and commitments:** reviewers MUST use dataset vX.Y; authors SHALL publish MVPK faces and cite the measurement environment; an organisation commits to a review SLA (explicitly a role-assignment or acting-system commitment).

* **Effects and evidence:** the produced report file, logs of evaluation runs, cryptographic hashes, and trace IDs are carriers. A.7 discipline prevents calling the report “the evaluation” (object) and prevents treating the file as the model.

* **Multi‑view (MVPK canonical face kinds only):**

  * PlainView for decision makers: what this protocol means for assurance.
  * TechCard for engineers: metric definitions named by value, admissibility predicates, and a clearly marked **Norms-and-commitments** section (D‑claims) for governance.
  * InteropCard for exchange-oriented consumers: conceptual field names, anchors, and schema references (concrete format mapping lives outside Part E).
  * AssuranceLane for auditors: evidence map (which carriers prove what happened) and adjudication steps keyed by `E-*` IDs.

This episteme is a boundary because it mediates between theory (“metric definitions”) and work (“a run produced a report”). The signature stack provides the stable interface for that mediation.


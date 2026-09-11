---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__012_sota-echoing.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:11 — SoTA-Echoing"
line_start: 10651
line_end: 10671
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

### A.6:11 - SoTA-Echoing

> **Informative.**

* **Adopt — algebraic effects and handlers / effect systems.** Effect systems distinguish operation signatures from handler semantics (e.g., Koka’s effect typing; effect handlers in OCaml 5). In this analogy, `U.Signature` carries the boundary declaration, A.6.1 governs operation declarations and their realization relation, and the realizing entity supplies the implementation. Substitution requires the declared meanings and applicability to be preserved.

* **Adopt — session and behavioural types for protocol boundaries.** Behavioural typing treats boundaries as typed interaction protocols with progress and safety properties. A.6’s classification matrix makes protocol laws (Quadrant L) explicit and separates entry gates (Quadrant A) from general prescriptions or exact individual commitments (Quadrant D) and runtime evidence (Quadrant E), reducing ambiguity.

* **Adapt — categorical optics, lenses, and bidirectional transformations.** Lenses supply useful construction expressions with coherence laws. FPF uses that lesson only for explicit A.6.3 construction or C.29 representation: a projection expression, publication face, and `U.View` remain different objects, while any cross-context reuse stays explicit.

* **Adapt — model-based views-as-queries practice.** Query and projection operations can construct candidate epistemes and make omissions inspectable. E.17.0 still tests each candidate independently against one exact viewpoint episteme; generation, selection, or a `viewpointRef` alone supplies no `U.View` membership.

* **Adapt — DDD bounded contexts and microservice contract-language practice.** Architecture practice keeps meaning local and makes crossings explicit. A.6’s stack and L/A/D/E claim-classification discipline provide a precise placement scheme for what belongs to the context boundary claim set, what belongs at the entry gate, what belongs to governance duties, and what belongs to observability evidence.

* **Adapt — observability as evidence discipline.** Traces, logs and metrics can supply evidence inputs for an exact claim. Use A.10 for the evidence-provenance relation and bounded reliance.

* **Adapt — Zero Trust, dynamic authorization, and policy-as-code practice.** Authorization practice separates policy, API, or schema text from a decision over subject, requested policy operation or work class, affected resource or work target, context, policy or gate version, decision source, and evidence. Cedar-style policy language and Zanzibar-style relation authorization are useful practice references for this split: the wording is not the decision. A.6 keeps policy, API, or schema wording in classified `L-*`, `A-*`, `D-*`, and `E-*` claims and uses `A.15.4` while appearance hides a prerequisite for work or reliance; `A.15` retains the enactment-alignment question.
* **Adopt, adapt, and reject stance for authority-looking boundary wording.** A.6 adopts policy-as-code separation of text from evaluated decisions, uses credentials and registers as source/currentness evidence, and rejects any visible wording or display as a substitute for the selected `A6-AW-*` branch.

* **Adapt — Markov blankets and active inference as probabilistic boundary views only after restoration.** Markov-blanket thinking can help pick observables and diagnose boundary-condition failures, but the source phrase must be restored before it carries an A.6 boundary claim. It may name accepted local Markov dynamics, a mathematical or probabilistic lens, a holon delimitation or crossing relation, an interface, an interface module, a physical component, a boundary description, or an agency-threshold claim. A.6 uses the phrase only after the boundary claim set is recovered; it does not replace deontics, invariants, admissibility gates, or the subject pattern of the physical or mathematical claim.


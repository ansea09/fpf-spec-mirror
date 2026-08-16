---
chunk_kind: "child"
pattern_id: "A.6.S"
pattern_title: "U.SignatureEngineeringPair - Signature engineering via a ConstructorSignature and a TargetSignature"
section_id: "A.6.S:5"
section_title: "Archetypal Grounding — Tell–Show–Show"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.S/A.6.S__007_archetypal-grounding-tell-show-show.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.6.S — U.SignatureEngineeringPair - Signature engineering via a ConstructorSignature and a TargetSignature"
  - "A.6.S:5 — Archetypal Grounding — Tell–Show–Show"
line_start: 20857
line_end: 20924
dependencies:
  - "A.12"
  - "A.3"
  - "A.6.0"
  - "A.6.2"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.19"
keywords:
  - "ConstructorSignature"
  - "EFEM"
  - "MVPK views (no new semantics)"
  - "TargetSignature"
  - "appear"
  - "claim register"
  - "editioning"
  - "no epistemic agency"
  - "quadrant classification is governed by A.6.B)"
  - "retargeting"
  - "signature engineering"
  - "slot/base change lexicon"
  - "two-signature arrangement"
---

### A.6.S:5 - Archetypal Grounding — Tell–Show–Show

**Tell.** A TargetSignature becomes stable and evolvable when you model both the *target signature* and the *engineering signature* that constructs it, and you force every change to be expressed as either (a) a view, (b) a disciplined slot/base construction step, or (c) an explicit retargeting to a new edition.

#### A.6.S:5.1 - Show — System archetype

**Working situation.** A payments microservice exposes an external boundary used by multiple client systems.

**Half‑signature input (what arrives).**
“Service binds a `User` to a `PaymentMethod`, anchors charges to the `Ledger`, and guarantees idempotency.”

**Constructed signature epistemes.**

* **TargetSignature:** `PaymentBoundarySignature`

  * **Vocabulary:** operations like `Authorize`, `Charge`, `Refund`; slots made explicit (e.g., `UserRefSlot`, `PaymentMethodRefSlot`, `LedgerEntryRefSlot`).
  * **Laws (examples):** “Charge is idempotent under IdempotencyKey”; “Refund does not increase net balance”.
  * **Applicability:** Payments external API; effective ReferenceScheme and scope are named by the signature edition.

* **ConstructorSignature:** `PaymentSignatureEngineering`

  * Performer System: `PaymentSignatureEngineeringPipeline`, if that team-and-toolchain candidate is admitted as one `U.System` under A.1. It performs the construction Work. State any local system-role classification separately, and use F.6 to identify the assignment under which it acted. A short example may omit the assignment identifier when it is unused.
    It enacts the constructor operations as Work and produces new editions and publication carriers.

  * Slot operations used (as operator descriptions; enacted via Work):

    * `bind/rebind` to bind API field names (e.g., `userId`, `paymentMethodId`) to SlotKinds (`UserRefSlot`, `PaymentMethodRefSlot`) where a language expression exists,
    * `initialize` or `edit<...>` to introduce SlotSpecs and to by‑value edit Vocabulary and Laws in the TargetSignature,
    * `resolve<…>` to disambiguate overloaded prose markers (e.g., “idempotency”) into explicit SlotKinds + laws,
    * `retarget<LedgerRefSlot>` when switching the referenced ledger holon/edition (ref change, not by‑value editing).
  * Base operations used:

    * `declareBase` to ground “Ledger” via an explicit baseRelation and scope,
    * `rescope` when moving from “internal ledger view” to “external client view”,
    * `refreshWitnesses` when decision‑relevant evidence/pins must be updated for continued use.

* **Publication.**
  MVPK faces published as views of the TargetSignature: a PlainView for non‑specialists, a TechCard for implementers, and an InteropCard for integrators, all derived without adding new claims beyond the canonical claim set.

**What A.6.S prevents here.** The phrase “guarantees idempotency” does not silently become a deontic promise or an operational gate. It becomes: (a) an L‑claim (law) in the SoI; (b) if needed, a mechanism‑level admissibility condition for when the guarantee holds; and (c) evidence claims in work logs when validated.

#### A.6.S:5.2 - Show — Episteme archetype

**Working situation.** A research group publishes a signature for a boundary concept used across multiple theories—a common interface between models.

**Half‑signature input.**
“We define correspondence between model A and model B; parameters are anchored to a reference dataset.”

**Constructed signature epistemes.**

* **TargetSignature:** `ModelCorrespondenceSignature`

  * **Vocabulary:** relation `Corresponds(A_model, B_model, Φ_bridge)` with explicit slot kinds and ref/value modes.
  * **Laws:** invariants about correspondence preservation (“observable X is preserved up to tolerance ε”).
  * **Applicability:** the named model-alignment question and use; effective schemes and any actual F.9 relation are stated separately.

* **ConstructorSignature:** `CorrespondenceSignatureEngineering`

  * Performer System: `CorrespondenceSignatureWorkbench`, if the author-and-toolchain candidate is admitted as one `U.System` under A.1. It performs the construction Work; any local system-role classification and obtaining assignment remain separate.

  * Slot operations used: `resolve` to unpack “correspondence” into an explicit bridge slot; `edit<Laws>` (by‑value) to make tolerance explicit; `retarget<ModelRefSlot>` when moving from a draft model edition to a published edition.
* Base operations used: `declareBase` to ground “reference dataset” as an explicit base with scope/time policy; `retime` when updating the reference window.

* **Publication.**
  The SoI is published in multiple viewpoints (e.g., a mathematical view and an engineering view). Differences are handled as views, not as semantic drift.

**What A.6.S prevents here.** “Anchored to a dataset” does not remain a vague metaphor. It becomes a declared base and, when the dataset changes, an explicit base‑change operation rather than a silent reinterpretation.


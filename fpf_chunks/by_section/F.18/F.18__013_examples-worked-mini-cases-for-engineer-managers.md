---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:12"
section_title: "Examples (worked mini‑cases for engineer‑managers)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__013_examples-worked-mini-cases-for-engineer-managers.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:12 — Examples (worked mini‑cases for engineer‑managers)"
line_start: 74653
line_end: 74685
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1-F.17"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:12 - Examples (worked mini‑cases for engineer‑managers)

> These examples are deliberately simple. They show how local-first minting, one-way unification, and dependency-stratum discipline operate together.

**12.1 “Module” vs “Component” (engineering structure).**

* *Stewardship Context A (Platform)* mints **Component** with MDS: “A physically or logically integrated part whose removal would alter the integrity of the whole.” **Structural**.
* *Stewardship Context B (App Team)* mints **Module** with MDS: “A deployable bundle of functionality maintained as a unit.” **Epistemic** (usage practice), not a structural claim.
* **Unification:** An alignment bridge states: “In Platform, every Component may include one or more Modules; Modules are not Parts.” Dependencies are one-way: *Module* depends on *Component*; *Component* does not depend on *Module*. No synonymy asserted. Both names remain in their stewardship Contexts.

**12.2 “Incident” vs “Event” (operational sense).**

* *Stewardship Context C (Operations)* mints **Incident** with MDS: “An unplanned interruption or reduction in the quality of a service.” **Epistemic**.
* *Stewardship Context D (Monitoring)* mints **Event** with MDS: “A recorded observation of a state change in a system.” **Epistemic**.
* **Unification:** Bridge notes: “Some Events are Incidents when they degrade service; not all Events are Incidents.” **Plain** labels (and at most one alias per register) may vary (e.g., “Outage” as an alias for **Incident**), but the **Row IDs** stay distinct. No part‑whole claims are implied.

**12.3 “Customer” vs “Account Holder” (business roles).**

* *Stewardship Context E (Sales)* mints **Customer**: “A party that receives value from an offering in exchange for consideration.” **Epistemic**.
* *Stewardship Context F (Finance)* mints **Account Holder**: “A party legally responsible for an account.” **Epistemic**.
* **Unification:** Bridge states overlaps and divergence: “A Customer can be an Account Holder; an Account Holder may not be a Customer (e.g., trustee).” The stewardship Contexts retain stewardship; a shared Working-Name “Client” may be used in executive materials with a clear note: **Working-Name only; see Concept-IDs for decisions**.

**12.4 “Batch” vs “Lot” (collection vs integration).**

* *Stewardship Context G (Manufacturing)* mints **Batch**: “A collection of items produced under shared conditions.” **Epistemic membership**.
* *Stewardship Context H (Quality)* mints **Lot**: “An integrated whole packaged and tracked as one item.” **Structural whole**.
* **Unification:** Bridge notes: “A **Lot** may originate from a single **Batch** or a slice of a Batch; not every Batch yields a single Lot.” Relation mapping: **MemberOf** (Batch membership) vs **ComponentOf**/**Whole** (Lot integration). *Loss note:* membership evidence does **not** imply part‑whole structure; part‑whole structure does **not** imply shared production conditions.

**12.5 “Palette label” vs “Atlas label” (NQD/OEE naming-side interpretation).**

* A naming pass compares candidate labels over one active palette and shortlist. The card keeps the active palette recoverable and uses thinner interpretive-view wording, because the question is only which label best fits the current candidate spread.
* Later, the same naming discussion must explain why one label misleads unless the reader can see the palette together with a derived archive, an `OutcomeMapRef`, and one `BridgeDistortionNote`. In that case atlas wording is allowed, but the card still names the base palette and records that the atlas is only optional interpretive help for the naming explanation.
* In both cases, guarded-head notes stay on the naming side: they explain alias risk or mismatch patterns, not who stewards the substrate or which publication face is authoritative.

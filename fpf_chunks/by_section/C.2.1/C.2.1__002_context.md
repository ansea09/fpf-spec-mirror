---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__002_context.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:1 — Context"
line_start: 35087
line_end: 35117
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.6.5"
  - "A.7"
  - "B.1.3"
  - "C.2"
  - "E.10.D2"
  - "E.17"
  - "E.17.0-E.17.2"
  - "E.18"
keywords:
---

### C.2.1:1 - Context

FPF’s kernel recognises two archetypal sub‑holons: **System** and **Episteme**. Systems are operational wholes; **epistemes** are **knowledge holons**—theories, models, specifications, standards, algorithms, proofs—whose reason for being is to **say something defeasible or deductive about something** and to be **held to account** by justification.

**Readers.** Engineering managers and lead designers who need a uniform way to reason about **theories, specifications, algorithms, proofs**—from charter memos up to formal axiomatics—without collapsing into tooling or discipline‑specific notations.

KD‑CAL (C.2) needs a precise notion of **what an episteme is** and **how it mediates** between:

* the thing(s) it is about,
* the contexts and systems that ground and test it, and
* the representational machinery (notations, carriers, operations) we use to work with it.

Contemporary work on **formal languages as cognitive artifacts** (Dutilh Novaes), **operational iconicity** of notations (Krӓmer), **material engagement** (Malafouris), **distributed representations** and **latent‑space communication** in ML, and **tool‑augmented reasoning** (ReAct‑style agent loops) shows that:
* the relation between an episteme and its **EntityOfConcernSlot** is not a single undifferentiated “Object” vertex: it involves explicit **slots and morphisms** (EntityOfConcern-reference mapping, grounding, evaluation) typed by SlotKinds and contexts;
* **representations** come in heterogeneous forms (symbolic, diagrammatic, latent, interactive), with very different **admissible operations**;
* **inference** is often **mixed‑mode**: symbolic reasoning plus calls to tools, solvers, and learned models.

FPF therefore needs a **more modular, slot-relation ontology** for epistemes which:
* keeps **KD-CAL** and `EntityOfConcern` / Description-episteme boundary plus specification use/refinement discipline intact,
* is compatible with **A.6.0/A.6.5** signatures (`SlotKind`/`ValueKind`/`RefKind`),
* can be used uniformly by A.6.2-A.6.4 (epistemic morphisms) and E.17.* (views & publication),
* preserves real graph-valued structures such as `ClaimGraph` and `JustificationGraph` as values inside or beside the episteme relation, and
* keeps the coarse **semantic triangle** only as a **didactic projection**, not the normative ontology.

In this pattern:
* `U.Episteme` is the **holon genus** for epistemes (C.2), with components and identity governed by A.1/A.6.0/A.7.
* `U.EpistemeSlotRelation` names the **internal slot relation** of `U.Episteme`: the small, typed n-ary relation over episteme positions (`EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`) on which KD-CAL, A.6.2-A.6.4 and E.17.* rely.
* Species such as `U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication` are holonic realisations of `U.Episteme` whose component structure is constrained to be compatible with `U.EpistemeSlotRelation`.

**Adopted EntityOfConcern family.** C.2.1 uses `EntityOfConcernSlot`, `entityOfConcernRef`, `EntityOfConcernRef`, `EntityOfConcernChangeMode`, and `EntityOfConcernClass` as the adopted slot/ref/class family. These names are the current C.2.1 vocabulary and must not be shadowed by a second episteme ontology.


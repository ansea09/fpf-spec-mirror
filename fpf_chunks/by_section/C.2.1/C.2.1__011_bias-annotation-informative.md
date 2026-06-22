---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:10"
section_title: "Bias-Annotation  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__011_bias-annotation-informative.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:10 — Bias-Annotation  (informative)"
line_start: 36730
line_end: 36749
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.6.5"
  - "A.7"
  - "B.1.3"
  - "C.2"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0-E.17.2"
  - "E.18"
keywords:
---

### C.2.1:10 - Bias-Annotation  *(informative)*

**Episteme‑first and pragmatics‑first.**
The pattern assumes that a claim-bearing episteme is meaningful only when it is **about something for someone under some perspective**. This follows the pragmatic turn in semantics: EntityOfConcern and concerns are not afterthoughts but part of the core structure. The slot relation is organized around EntityOfConcern, GroundingHolon, Viewpoint, and ClaimGraph positions, while graph-valued fillers such as `ClaimGraph` and `JustificationGraph` remain distinct values inside those positions.

**Operational and representational bias.**
C.2.1+ anticipates that certain RepresentationSchemes are **operational** in Novaes’ sense (admitting direct syntactic inference, like pen-and-paper arithmetic or proof states) while others are **purely notational**. The pattern remains neutral on which schemes are used but bakes in a place for operations and carriers so that:

* symbol‑manipulating tools (SAT solvers, SMT solvers, proof assistants, classical programming languages),
* distributed and latent representations (LLM embeddings, latent protocols like "DroidSpeak", "Coconut"-style communication),
* hybrid ReAct‑style agent loops

can all be treated as different species operating over the same `U.EpistemeSlotRelation`. There is a bias towards making these operational differences **explicit** instead of hiding them behind "the model".

**Viewpoint and stakeholder bias.**
The pattern leans on the ISO‑style idea that viewpoints encode **stakeholder concerns and role‑families**, but it generalises this beyond architecture. `U.Viewpoint` is intentionally context-local and not bound to any single discipline; still, the examples are skewed toward engineering and epistemic use‑cases.

**Didactic bias.**
The pattern is written to be teachable: semantic triangles are kept as didactic projections; examples like stools on lab rigs, services and SLAs, and model‑evaluation epistemes are deliberately simple. This may under‑represent more exotic epistemes (e.g. artistic, law-domain, or socio‑technical ones), but the intention is that these use the same slots with different species‑level constraints.


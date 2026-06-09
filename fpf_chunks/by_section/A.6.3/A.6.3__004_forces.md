---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — EntityOfConcern-preserving morphism"
section_id: "A.6.3:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__004_forces.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.6.3 — U.EpistemicViewing — EntityOfConcern-preserving morphism"
  - "A.6.3:3 — Forces"
line_start: 10003
line_end: 10023
dependencies:
  - "A.6.0"
  - "A.6.2"
  - "A.6.5"
  - "A.7"
  - "B.5.3"
  - "C.2"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
keywords:
---

### A.6.3:3 - Forces

* **Same EntityOfConcern, different concerns.**
  Stakeholders want different slices of the same description and specification-useification, sometimes under different viewpoints, without re-identifying the system, method, service, or other entity that fills `EntityOfConcernSlot`.

* **Internal vs cross‑episteme views.**
  Some views depend only on a single episteme (direct viewing); others depend on a **CorrespondenceModel** (e.g. aligning requirements and design models). Both are admissible, but they require **different witnesses**.

* **Conservativity vs expressivity.**
  A view must not introduce new commitments about the EntityOfConcern, but it may:

  * aggregate or factor claims,
  * change representation regime (diagrammatic vs symbolic vs latent),
  * or shift to a different inference regime, **as long as this is conservative**.

* **EntityOfConcern and Description-episteme boundary and specification-use strictness.**
  `…Description` names a Description episteme, and `…Spec` names a Description episteme admitted for specification use whose `subjectRef` decodes to `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩` when the declared checkability/formality gate is present. Viewing works over these `DescriptionContext` triples without collapsing the EntityOfConcern into the Description episteme or Description episteme admitted for specification use produced by the use, while still allowing that EntityOfConcern to be a `U.Episteme` when an episteme is under concern; it also must not confuse those epistemes with publication faces or carriers.

* **Slot discipline and modularity.**
  With C.2.1 and A.6.5, epistemes now have explicit `SlotKind`/`ValueKind`/`RefKind` triples. Viewing invariants must be stated **per SlotKind**, not in terms of ad‑hoc “fields”, so they can be reused across engineering, publication, and discipline packs.


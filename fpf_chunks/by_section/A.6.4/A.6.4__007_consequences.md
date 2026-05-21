---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — describedEntity‑retargeting morphism"
section_id: "A.6.4:6"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__007_consequences.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — describedEntity‑retargeting morphism"
  - "A.6.4:6 — Consequences"
line_start: 11875
line_end: 11893
dependencies:
  - "A.1"
  - "A.6.2"
  - "C.2"
  - "C.2.1"
  - "E.18"
  - "E.TGA"
  - "F.9"
  - "U.EpistemeSlotGraph"
  - "U.EpistemicRetargeting"
keywords:
  - "KindBridge"
  - "SquareLaw-retargeting"
  - "StructuralReinterpretation"
  - "describedEntity shift"
  - "retargeting"
  - "subject retargeting"
---

### A.6.4:6 - Consequences

* **Clear separation of Viewing vs Retargeting.**
  A.6.3 and A.6.4 now jointly distinguish:
  * **views**: same `DescribedEntityRef`, possible representation/viewpoint changes;
  * **retargetings**: different `DescribedEntityRef` under `KindBridge` and invariants.

* **Canonical governing pattern for StructuralReinterpretation.**
  E.TGA StructuralReinterpretation becomes a **species of `U.EpistemicRetargeting`**, not an ad‑hoc special node. This reduces duplication and clarifies how CL penalties and Bridges are used.

* **Invariants become first‑class.**
  Retargeting makes invariants explicit and type‑checked: every such morphism must state what it preserves and how that is expressed in KD‑CAL/LOG‑CAL.

* **Safer cross‑plane reasoning.**
  ReferencePlane crossings and kind‑level moves are handled via existing Bridges (Part F), with CL^plane/CL^k penalties and SquareLaw witnesses, instead of hidden in implementation details.

* **Better integration with I/D/S.**
  For `…Description`/`…Spec` epistemes, retargeting is the only place where `DescribedEntityRef` in `DescriptionContext` is allowed to change; all other I/D/S‑level operations (Describe/Specify, Viewing) keep it fixed.


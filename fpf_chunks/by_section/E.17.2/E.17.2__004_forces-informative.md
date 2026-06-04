---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB — Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:3"
section_title: "Forces  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__004_forces-informative.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.17.2 — TEVB — Typical Engineering Viewpoints Bundle"
  - "E.17.2:3 — Forces  (informative)"
line_start: 62318
line_end: 62329
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.TGA"
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.2:3 - Forces  *(informative)*

| Force                                       | Tension                                                                                                                                                                       |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs domain idioms**           | We need engineering viewpoints that work for *any* holon (hardware, software, or socio-technical), yet remain recognisable to practitioners steeped in domain-specific frameworks. |
| **Parsimony vs expressiveness**             | A small, stable **NQD-front** set of engineering view families (Function, Behaviour and Process, Role-Enactor, Module-Interface) vs the temptation to proliferate specialised views for every stakeholder group or quality attribute. |
| **Neutral core vs architecture frameworks** | FPF core must stay neutral and not encode a specific framework (4+1, DoDAF, etc.), while still being compatible with them.                                                    |
| **Consistency vs organisational autonomy**  | Central TEVB definitions must be stable, yet individual organisations need room to refine concerns and episteme kinds within the bundle.                                      |
| **EntityOfConcern and Description-episteme boundary plus specification-use clarity vs convenient shortcuts**   | Viewpoints must not re-introduce `Role` as a coordinate in EntityOfConcern and Description-episteme boundary or specification-use discipline, nor blur Description-episteme and specification-use distinctions with publication face, form, or carrier distinctions, even though practitioners informally mix these.             |

TEVB resolves these by fixing a **minimal engineering bundle** and leaving customisation to **species patterns and ViewpointBundleLibrary entries** that refine concerns and allowed episteme kinds without changing the core families.


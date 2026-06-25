---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:9"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__010_archetypal-grounding.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:9 — Archetypal Grounding"
line_start: 36977
line_end: 36984
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

### C.2.1:9 - Archetypal Grounding

**System-description episteme.** A pump maintenance specification is an episteme whose EntityOfConcernSlot points to the pump or pump class, whose GroundingHolonSlot may point to the plant or test bench, whose ClaimGraph states maintenance claims, and whose ReferenceScheme explains how part names, measurements, and operating states refer to the pump in that bounded context. The PDF, database row, and rendered checklist are publication and carrier values, not the episteme itself.

**Episteme-about-episteme case.** A review note about a simulation model is also an episteme, but its EntityOfConcernSlot points to the simulation model episteme. The slot relation still separates the reviewed episteme, the review episteme, the claim graph, grounding holon, reference scheme, and evidence relation; the fact that the EntityOfConcern value is itself an episteme does not create a second ontology.

**Multi-view description case.** An architecture description may publish several views under different viewpoints. Each view is an episteme view constrained by the same episteme slot relation, while the publication face or carrier belongs to E.17 rather than to the episteme core.


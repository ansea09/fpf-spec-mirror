---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:5"
section_title: "Semantic triangle as didactic view  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__006_semantic-triangle-as-didactic-view-informative.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:5 — Semantic triangle as didactic view  (informative)"
line_start: 36823
line_end: 36852
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

### C.2.1:5 - Semantic triangle as didactic view  *(informative)*

**Position.** The classical semiotic or semantic triangle ("Symbol-Concept-Object", Ogden-Richards and Frege-Carnap style) is **not** the normative ontology for epistemes in FPF. For `U.Episteme`, it is treated as a **didactic projection** of `U.EpistemeSlotRelation`. The projection compresses several SlotSpecs and graph-valued fillers into three teaching corners:
* **"Symbol" corner** ~= {`U.RepresentationToken`, `U.RepresentationScheme`, `U.PresentationCarrier`} when C.2.1+ is in use; in the minimal core this is collapsed into whichever external carrier bears the `U.ClaimGraph` publication.
* **"Concept" corner** ~= `U.ClaimGraph` + `U.ReferenceScheme` under a chosen `U.Viewpoint`. This is the claim content plus its interpretation recipe.
* **"Object" corner** ~= the slot filler of `EntityOfConcernSlot` (ValueKind `U.Entity`) plus the slot filler of `GroundingHolonSlot` (ValueKind `U.Holon`) and the grounding relation between them.

Under this didactic projection the triangle is a **three-corner quotient** of the episteme slot relation:
```text
(Symbol)      = RepresentationToken + Scheme + Carrier
(Concept)     = ClaimGraph + ReferenceScheme (+ Viewpoint)
(Object)      = EntityOfConcern + GroundingHolon
```

All **viewpoints, operations, carriers and reference planes** are suppressed in the classical diagram. The cost of this suppression is precisely the confusion that motivates C.2.1:
* describing becomes a single unlabeled arrow,
* inference regimes disappear,
* measurement and grounding are invisible.

**Didactic use.** C.2.1 allows the triangle **only** in the following cases:
1. As an **introductory picture** in guidance material ("this is the coarse triangle; the actual pattern is the episteme slot relation").
2. As a **quotient diagram**: an explicit note that "this figure ignores viewpoint, grounding, carrier, and operationality; see C.2.1 for the full structure".
3. As an **external-triangle alignment aid** when mapping to standards or literature that speak only in triangle terms.

**Guard.** Any pattern or documentation page that uses a "semantic triangle" diagram **MUST** either:
* explicitly state "this is a didactic projection of C.2.1 `U.EpistemeSlotRelation`", or
* treat it as an external-triangle reference when aligning with external standards.

The triangle **MUST NOT** be used as a kernel-level ontology or as a source for morphism laws. All normative reasoning about epistemes proceeds via the slots, graph-valued fillers, non-graph-valued fillers, and components governed by `U.EpistemeSlotRelation`.


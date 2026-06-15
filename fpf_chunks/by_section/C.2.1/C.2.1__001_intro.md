---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__001_intro.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:intro — Intro"
line_start: 35068
line_end: 35086
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

## C.2.1 - U.Episteme - Epistemes and their slot relation

> **One-line summary.** `U.Episteme` is the holon type for epistemes; its internal ontology is given by `U.EpistemeSlotRelation`, a typed n-ary relation with `SlotSpec` discipline over `EntityOfConcern`, `GroundingHolon`, `ClaimGraph`, `Viewpoint`, `View`, and `ReferenceScheme`. Under `C.29`, a filled episteme may be represented as a tuple view over that relation; `ClaimGraph` and `JustificationGraph` remain graph-valued fillers or attached graph-valued structures, not tuples. A coarse Symbol-Concept-Object triangle may be used only as a didactic projection of this slot relation, not as the normative ontology.

> **Status:** Stable
> **Normativity:** Normative except where a section is explicitly marked informative

**Use this pattern when** a theory, model, specification, standard, proof, algorithm, diagram, dashboard, view, or publication is being treated as a knowledge holon and the project must know what it is about, what claim graph it carries, how it is grounded, which viewpoint or view is current, and which reference scheme makes the claims readable.

**Primary EntityOfConcern.** The `EntityOfConcern` is `U.Episteme`: a knowledge holon whose identity and admissible use are governed by `U.EpistemeSlotRelation`, not by its carrier, notation, publication face, or one didactic semantic-triangle projection.

**First useful move.** Fill the small episteme slot relation: `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot`, `ViewpointSlot`, and `ViewSlot` when current. Then decide which claim, view, publication, specification-use, morphism, evidence, or grounding relation is actually being used, and keep that relation with its governing pattern.

**What goes wrong if missed.** A PDF, diagram, proof script, algorithm text, model output, or dashboard becomes "the theory"; the described EntityOfConcern drifts; a publication is used as evidence or authority by appearance; and several local description triangles grow into incompatible episteme ontologies.

**What this buys.** The practitioner can keep the episteme, its described object, grounding holon, claim graph, viewpoint, view, reference scheme, carrier, publication, and evidence relation separate while still using one compact slot relation across C.2, A.6.2-A.6.4, E.17, and related description/specification-use patterns.

**Not this pattern when.** Use the direct governing pattern when the current question is the described system or holon (`A.7` and system/holon patterns), a publication face or carrier (`E.17`), evidence or assurance (`A.10`, `G.6`, `B.3`), mathematical-lens use (`C.29`), a method or method description (`A.3.1`, `A.3.2`), or a wording-use repair (`E.10`, `C.2.P`, `C.2.P.DR`, `F.18`, `F.19`). `C.2.1` governs the episteme slot relation itself.


---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__016_relations.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:13 — Relations"
line_start: 82915
line_end: 82924
dependencies:
  - "A.10"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.View"
keywords:
---

### E.17:13 - Relations
* **Architecture ADR projection boundary:** `C.32.ADR` is the architecture-specific publication projection for `ArchitectureDecisionDescription@Project`. E.17 keeps publication face, source episteme, carrier, scope, and downstream typed value separate for the broader MVPK claim.
  In that name, `@Project` is a compatibility and retrieval cue only. E.17 infers no project entity, composite-work identity, context, authority, viewpoint, or parthood from it; `C.30.AD` and `C.32.ADR` must identify the exact composite `U.Work` and the direct description-use or publication-use relation when project locality is current.

* **Builds on:** `C.2.1` for selected-edition identity; `E.24.PUB` for `PublicationFormExpressionRelation`, `PublicationFormBearingRelation`, and the exact publication occurrence; `E.17.0` for viewpoint and `U.View` membership; `A.22` for selected structure; `C.29` for representation; `A.7` and `E.10.D2` for carrier, front-end, EntityOfConcern, Description-episteme, and specification-use discipline; `A.6.2`-`A.6.3` for optional source-to-candidate construction; `E.8` and `E.10` for authoring and publication-language discipline; and Part F and Part G for bridge, terminology, characteristic, and pin discipline.
* **Constrains:** publication-face-emitting automation and hand-written faces. When another episteme is constructed from a source, A.6.3 supplies the separate construction relation; E.17.0 separately tests viewpoint conformance, and E.24.PUB separately identifies publication occurrence/form/carrier. Readable form creates none of those relations, nor an evidence path, gate decision, work occurrence, assurance record, release source, or bridge declaration.
* **Neighboring-pattern boundary use:** use the compact boundary aid in `E.17:5.1d` when a publication-facing unit starts carrying work, reliance, evidence, assurance, gate, release, bridge, explanation, comparison, retargeting, carrier, or front-end claims beyond ordinary publication use. This Relations section cites that aid instead of repeating the whole map.
* **Part F bridge wording boundary:** when the publication face uses or invites "same", "equivalent", "align", "map", substitutable, interchangeable, attribute, entity, or profile matching, or other Bridge-wording pressure across contexts, use Part F and `A.6.9` to repair the wording. Use F.9 for the Bridge and bounded-use claim, and F.9.1 only for a separate optional stance note about that claim. Neither object follows from a publication face, and no local Bridge taxonomy is introduced here.
* **Coordinates with:** `C.2.P` for exact source-expression and source-to-use recovery before publication-facing wording is relied on; `A.15.4` for appearance-based reliance repair; C-cluster selection or archive patterns when separately constructed epistemes are selected or retained; CHR and UNM for measurement and normalization semantics; F.9 for exact Bridge occurrences, bounded-use claims, optional `CL`, evidence and loss boundaries, and optional Cards; F.9.1 for separate optional stance epistemes; and `A.6.9` for sameness wording. Publication faces remain publication forms; their bounded-use declarations, selected or receiving epistemes, occurrences, and carriers remain separate, and face status never establishes `U.View` membership.


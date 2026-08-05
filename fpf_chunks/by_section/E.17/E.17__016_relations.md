---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__016_relations.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:13 — Relations"
line_start: 80770
line_end: 80779
dependencies:
  - "A.15.4"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
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
* **Constrains:** publication-face-emitting automation and hand-written publication faces. When one receiving episteme is actually constructed from a source, A.6.3 governs that separate relation; the face and publication occurrence are not species of viewing. Readable form creates no second EntityOfConcern-to-Description mechanism, specification-use gate, evidence path, gate decision, work occurrence, assurance record, release source, or bridge declaration.
* **Neighboring-pattern boundary use:** use the compact boundary aid in `E.17:5.1d` when a publication-facing unit starts carrying work, reliance, evidence, assurance, gate, release, bridge, explanation, comparison, retargeting, carrier, or front-end claims beyond ordinary publication use. This Relations section cites that aid instead of repeating the whole map.
* **Part F bridge wording boundary:** when the publication face uses or invites "same", "equivalent", "align", "map", substitutable, interchangeable, attribute, entity, or profile matching, or other bridge-wording claim pressure across contexts, the wording repair belongs to Part F and `A.6.9`; the bridge relation belongs to `F.9` or `F.9.1`. `E.17` does not create a local bridge taxonomy.
* **Coordinates with:** `C.2.P` for exact source-expression and source-to-use recovery before publication-facing wording is relied on; `A.15.4` for appearance-based reliance repair; C-cluster selection or archive patterns when exact face epistemes are selected or retained; CHR and UNM for measurement and normalization semantics; `F.9` or `F.9.1` for exact bridge relations; and `A.6.9` for sameness wording. Publication faces remain publication forms and uses, never views by face status.


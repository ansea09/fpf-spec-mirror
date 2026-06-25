---
chunk_kind: "child"
pattern_id: "A.6.P"
pattern_title: "Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline"
section_id: "A.6.P:11"
section_title: "SoTA-Echoing (informative; post-2015 alignment)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P/A.6.P__014_sota-echoing-informative-post-2015-alignment.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "A.6.P — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline"
  - "A.6.P:11 — SoTA-Echoing (informative; post-2015 alignment)"
line_start: 14069
line_end: 14082
dependencies:
  - "A.10"
  - "A.2.4"
  - "A.2.6"
  - "A.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.8"
  - "A.6.9"
  - "A.6.A"
  - "A.6.B"
  - "A.6.H"
  - "A.6.S"
  - "A.7"
  - "C.16.Q"
  - "C.2.1"
  - "C.2.2a"
  - "C.26"
  - "C.3.3"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
  - "QualifiedRelationRecord"
  - "RelationKind"
  - "coupling"
  - "endpoint referential compression"
  - "export"
  - "language-state seam"
  - "lexical guardrails"
  - "measurement"
  - "probe"
  - "relation precision restoration"
  - "selected support reading"
  - "support/support-headed wording"
  - "under-specified relational language"
---

### A.6.P:11 — SoTA-Echoing (informative; post-2015 alignment)

A.6.P echoes contemporary practice across independent traditions, while remaining notation-neutral and Context-local. A row is retained only when it changes the A.6.P solution, checklist, boundary, worked case, or reopen condition.

| Practice source line | Use of source | Echo | What A.6.P adopts or adapts | What A.6.P rejects |
| --- | --- | --- | --- | --- |
| W3C SHACL Recommendation (2017) for shape validation over RDF graph assertions. | Current-standard and reference use for assertion and constraint separation; not a complete current-best answer for FPF relation precision restoration. | Separates graph assertions from constraints over node and value shapes. | Adopts explicit structural constraint thinking for relation records and mutates `CC-A.6.P-2`: relation claims need explicit SlotSpecs, qualifiers, witness expectations, and admissible use, not only prose assertions. | Rejects treating validation shape notation as the required FPF notation or as a substitute for relation-kind selection and lexical guardrails. |
| RDF-star / SPARQL-star W3C Community Group Report (2021) and RDF and SPARQL WG current line for quoted triples and statement qualification. | Current-practice and working-standardization source use for qualified statements; not stable ontology authority for FPF. | Shows why hidden arity and qualification need explicit representation when statements carry statement-about-statement claim. | Adapts the qualification pressure into `RelationKind` plus qualifier slots and change-class lexicon; mutates the hidden-arity and candidate-set examples. | Rejects "reification solves the relation" when kind selection, endpoints, admissible use, and change semantics remain hidden. |
| ISO/IEC/IEEE 42010:2022 architecture-description practice on viewpoints, model kinds, and correspondences. | Current-standard and reference use for viewpoint accountability and correspondence discipline. | Treats viewpoints and correspondences as first-class description concerns. | Adopts viewpoint accountability for relation qualification and mutates boundary cases involving views, viewpoints, correspondences, and silent polarity flips. | Rejects importing architecture-description ontology as the general relation ontology; architecture-specific cases still go to `C.30`, `C.30.ASV`, or `C.30.P`. |
| Pickering, Gibbons, and Wu, "Profunctor Optics: Modular Data Accessors" (ICFP 2017) and successor optics practice. | Current formal-lens source use for bidirectional view and update intuition; used as a stabilizing lens, not as mandatory notation. | "Pairs of projections plus invariants" makes multi-view relation discipline teachable. | Adapts optics as a didactic stabilizer for multi-view relation repair and mutates the rationale for stable lens -> explicit slots -> change classes. | Rejects requiring profunctor notation or treating formal elegance as proof of admissible relation use. |
| Fong and Spivak, "Seven Sketches in Compositionality" (2019), as applied-category-theory lineage for compositional modeling. | Lineage and didactic source use for compositional lens choice; not by itself current-best source use for FPF wording repair. | Shows why stable abstract lenses can be reused across domains. | Adapts compositionality as a reason to keep A.6.P notation-neutral while requiring relation slots and change lexicon; mutates the rationale and teaching examples. | Rejects adding a global category-theory ontology to FPF relation repair. |

These echoes justify why A.6.P is structured as: **stable lens -> explicit slots -> explicit change classes -> lexical guardrails**, rather than "just define the verb". A source row that does not change A.6.P fields, examples, checklist rows, boundaries, or reopen conditions is decorative and should be removed or demoted to lineage outside the SoTA echo.


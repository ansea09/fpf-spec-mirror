---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__003_problem.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:2 — Problem"
line_start: 36899
line_end: 36958
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

### C.2.1:2 - Problem

Without a shared **episteme constitution**, teams fall into recurring failure modes:

1. **EntityOfConcern-Description episteme-publication carrier soup.** Diagrams and files are treated as *the theory itself*. Changes to a PDF are confused with theoretical change.
2. **EntityOfConcern blur.** A spec seems to describe “everything in general”. The **EntityOfConcernSlot** - what exactly this knowledge describes - is implicit and drifts, while the **GroundingHolonSlot** that would say where the claim is grounded is also missing.
3. **Proof vs program confusion.** Algorithms, specifications, and proofs are mixed: a “proof” is used as if it were a tested routine; a “program” is cited as if it entailed a theorem (Curry–Howard misunderstood).
4. **Trust without evidence relation.** Claims accumulate with no explicit **justification graph** or **evidence freshness**, so assurance degrades invisibly.
5. **Category errors at execution.** Epistemes appear as *actors* (“the standard enforces…”) instead of **systems** acting *with* or *on* epistemes such as data sets or algorithms.

The coarse Symbol-Concept-Object semantic triangle is useful only as a didactic projection over the richer slot relation: **Concept** approximates `ClaimGraph`, **Object** approximates `EntityOfConcern` plus `ReferenceScheme`, and **Symbol** approximates notation or representation tokens.

This projection can still help with:
* separating **meaning** (Concept) from **carriers**, and
* integrating KD‑CAL’s **F–G–R** characteristics (Formality, ClaimScope, Reliability).

But the projection has structural blind spots when used as ontology:

1. **No explicit EntityOfConcern slot.**
   The “Object vertex” bundles together *what the episteme is about* with *how we interpret and test it*. There is no explicit **slot** for the entity of concern (`U.Entity`) and no clear separation between:
   * the **EntityOfConcern value**, and
   * the **ReferenceScheme** used to read claims as statements about that thing.

2. **Grounding collapses into Object.**
   Material and organisational contexts (labs, infrastructures, organisations) that **ground** an episteme (in Malafouris' sense) are hidden in the Object and Reference map. KD-CAL and Bridges need explicit **GroundingHolon** positions.

3. **Viewpoints are not first‑class.**
   ISO‑style **viewpoints** (families of stakeholders, concerns, conformance rules) and their induced **views** appear only indirectly, via KD‑CAL or MVPK. There is no explicit `U.Viewpoint` / `U.View` pair at the episteme core, which makes it hard to:

   * connect to **DescriptionContext** for Description epistemes, including Description epistemes admitted for specification use,
   * organize multi‑view descriptions (E.17.0), or
   * align publication viewpoints with engineering viewpoints.

4. **Representations and operations are compressed into “Symbol”.**
   Very different representational regimes are flattened into one Symbol vertex:

   * label-only notations (no internal inference calculus),
   * fully operational calculi (e.g., proof assistants),
   * interactive visualisations,
   * latent vectors and prompt‑programs for LLMs.
     There is no place to say “this representation admits **syntactic inference** of such‑and‑such kind” vs “this is just a **passive label**”.

5. **No explicit signature discipline.**
   The triangle speaks of "Object", "Concept", and "Symbol" but not of **slots** and **references** in the sense of A.6.5 `U.RelationSlotDiscipline`. In episteme this leads to:
   * names where **slot, value and ref** are conflated (`EntityOfConcernRef` used as if it were a slot),
   * ambiguity between the **EntityOfConcern value** (what the episteme describes) and the **episteme** (the description),
   * fragile interoperability with signatures for roles, methods, services.

Thus we have problems of:
* **EntityOfConcern drift.**
 Specifications and models accumulate without a stable notion of **which EntityOfConcernSlot value they carry**; fields like `SubjectRef` carry too many distinct meaning-kinds and resist safe refactoring.
* **Viewpoint confusion.**
  Engineering, publication and governance views are mixed, making it hard to maintain consistency across publication faces and publication forms or to reason about conformity of descriptions under different viewpoints.
* **Representation mismatches.**
  Trade‑offs between neural vs symbolic, diagrammatic vs textual, or interactive vs batch representations cannot be expressed at the episteme level; they leak into ad‑hoc tool descriptions.
* **Broken modularity.**
  As soon as we add KD-CAL, LOG-CAL, MVPK, and E.18, multiple **implicit triangles** appear, each with slightly different semantics, instead of a single shared `U.EpistemeSlotRelation`.

We need a replacement for the triangle that keeps its **didactic clarity** but matches the **slot-relation, graph-valued-claim, and morphism-centric** reality of contemporary epistemic work.


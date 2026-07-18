---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__001_intro.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoints Bundle"
  - "E.17.2:intro — Intro"
line_start: 75054
line_end: 75101
dependencies:
  - "A.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

## E.17.2 - `TEVB` - Typical Engineering Viewpoints Bundle
> **Type:** Part E viewpoint-bundle species pattern
> **Status:** Stable
**Use this when.** A team needs a small reusable set of engineering viewpoints for a holon so that functional, procedural, allocation-responsibility, and module-interface descriptions stay comparable across diagrams, models, cards, and architecture-description bundles.

**First output.** One TEVB bundle use naming `VF.TEVB.ENG`, the selected holon as `EntityOfConcernRef`, the active `VP.*` viewpoint, and the bounded description or specification-use case being written or checked.

**What goes wrong if missed.** Engineering views, publication faces, diagrams, and architecture-specific views collapse into one label, so functional, procedural, allocation-responsibility, and module-interface material cannot be compared safely.

**What this buys.** TEVB gives a compact engineering viewpoint bundle for holons while leaving architecture-specific view adequacy, publication form, role assignment, method, work, and module-interface claims with their direct owners.

**Not this pattern when.** If the current question is architecture structural-view adequacy, architecture description adequacy, publication-form behavior, role assignment, method or work alignment, or module-interface relation repair, use the governing pattern and keep TEVB only as the viewpoint-bundle reference when current.

> **Tech‑name:** `TEVB` (Typical Engineering Viewpoints Bundle, bundle id `VF.TEVB.ENG`)
> **Plain‑name:** typical engineering viewpoints bundle for holons
> **Tag:** Archetypal species of `U.ViewpointBundle` for engineering holons

**Status.** Stable; archetypal, notation‑agnostic species of `U.ViewpointBundle` / `U.ViewpointBundleLibrary`.
It is an engineering‑level bundle over holons; it does not itself constitute an architecture framework or architecture‑specific viewpoint library. Architecture‑focused viewpoint bundles are introduced as separate `U.ViewpointBundle` species that may import TEVB.

**Builds on.**
* **E.17.0 — `U.MultiViewDescribing`.** Supplies the generic notion of `U.Viewpoint`, `U.View`, and `ViewFamily` over an `EntityOfConcernClass ⊑ U.Entity` (here: `EntityOfConcernClass = U.Holon`).
* **E.17.1 — `U.ViewpointBundleLibrary`.** Provides the generic `U.ViewpointBundle`/`ViewFamilyId` structure; TEVB is a concrete bundle (`VF.TEVB.ENG`) in the core library.
* **A.1 — Holon.** Holon kinds `U.System` and `U.Episteme` as the typical engineering entities of concern.
* **A.6.2–A.6.4 — Episteme morphisms.** `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, `U.EpistemicRetargeting` as the generic morphism classes behind engineering views.
* **A.7 and E.10.D2 - Strict Distinction: EntityOfConcern, Description episteme, and Description episteme admitted for specification use.** TEVB uses DescriptionContext; engineering descriptions and specifications under TEVB are Description epistemes and specification-use cases with explicit `ViewpointRef`.
* **C.2.1 — `U.EpistemeSlotRelation`.** Provides `EntityOfConcernSlot`, `ViewpointSlot`, `ViewSlot` and the slot discipline (A.6.5) used by TEVB-aligned Description epistemes and specification-use Description epistemes.

**Used by.**
* **E.18:5.12 — transformation-flow viewpoint-family map.** As a canonical consumer, `E.18` binds its engineering transformation-flow families (Functional, Procedural, allocation-responsibility or device-structure, Module-Interface) to TEVB viewpoints `VP.Functional`, `VP.Procedural`, `VP.AllocationResponsibility`, `VP.ModuleInterface`.
* **E.17 (MVPK).** Publication of engineering morphisms uses TEVB engineering viewpoints on the Description-episteme and specification-use side and separate publication-side viewpoints over publication faces and forms.
* **Engineering description and specification-use patterns.** System, method, module-interface, and allocation-responsibility-related Description-episteme and specification-use patterns for holons (`U.System`, `U.Episteme`) refer to TEVB when declaring their `ViewpointRef`.
* **ISO-aligned architecture-description bundles.** Architecture-specific viewpoint-bundle species reuse TEVB as the canonical engineering view family (Functional vs Structural etc.) over systems and their epistemes.

**Guard (lexical & ontological).**
**Selected-family scope.** TEVB's engineering viewpoints are scoped by `EntityOfConcernClass = U.Holon` with usual `U.System` and `U.Episteme` cases. ISO 42010 concern, viewpoint, and view language is used as architecture-description practice alignment, not as imported FPF ontology.

1. **Engineering scope only.** TEVB applies to `EntityOfConcernClass = U.Holon` with typical cases `U.System` and `U.Episteme`. Using TEVB viewpoints for non‑holonic entities (e.g., pure data structures, abstract theories) requires an explicit species‑level justification; by default it is a conformance violation.
2. **Viewpoint vs publication faces, forms, and carriers.** `VP.Functional`, `VP.Procedural`, `VP.AllocationResponsibility`, `VP.ModuleInterface` are **viewpoints** (`U.Viewpoint` specifications), not publication face, publication form, rendering, or carrier names. A conforming TEVB use keeps `{PlainView, TechCard, NormsCard, InteropCard, AssuranceLane, ...}` as publication faces and publication forms under MVPK and does not use `VP.*` ids as carrier or publication-form ids.
3. **EngineeringVPId vs publication-side viewpoint id.** `VP.*` in this pattern are **EngineeringVPId** values (E.18:5.12). MVPK publication uses separate publication-side viewpoint ids, linked to TEVB viewpoints only through correspondences.
4. **No new role coordinates in EntityOfConcern and Description-episteme boundary and specification-use discipline.** TEVB may name stakeholder or audience families, and the `VP.AllocationResponsibility` id may name a viewpoint, but TEVB does not introduce a new allocation-responsibility root kind, `U.Role`, or `U.RoleAssignment` as coordinates in Description episteme or specification-use case signatures (E.10.D2). Work-facing roles, holders, assignments, method alignment, performed work, and role names remain governed by `A.2`, `A.2.1`, `A.15`, and Part F role-description or naming patterns.
5. **EntityOfConcern retention.** In ordinary TEVB use, `DescriptionContext.EntityOfConcernRef` remains the holon selected by `EntityOfConcernClassSpec`. Capability, Method, procedure terms, control-logic terms, role-assignment and responsibility structure, structural architecture, module, interface, and allocation terms are viewpoint concern and content inside the Description episteme unless the text explicitly opens A.6.4 retargeting with a KindBridge and species-extension rule.

   When `EntityOfConcernRef` is `U.Episteme`, role-assignment or responsibility statements in a TEVB view govern systems or acting holons around that episteme, such as authors, maintainers, users, assurers, or transformers. They do not make the episteme itself hold a work-facing role. Episteme-side participation is expressed through C.2.1 slots, source-use relations, publication-use relations, or viewpoint concern unless a governing work-facing pattern explicitly introduces a system or acting-holon role assignment.

6. **No extra viewpoints inside TEVB.** TEVB defines a **fixed core set** of four engineering viewpoints. Other labels such as assurance-oriented, interoperability-oriented, information-oriented or data-oriented, operational-oriented or deployment-oriented, and mission-oriented or context-oriented may appear only as **lexical family labels** in E.18:5.12 (for example, as `ViewFamilyId` and `AliasInViewFamilies` values for transformation-flow species). They do not extend `TEVB.EngBundle.viewpoints` and are not additional `U.Viewpoint` kinds in this bundle; when SoTA or local practice demands explicit assurance, information, or mission viewpoints, provide them as **separate `U.ViewpointBundle` species** imported alongside TEVB rather than by mutating `VF.TEVB.ENG`.
7. **Not an architecture framework.** TEVB is an engineering‑level viewpoint bundle; architecture‑specific viewpoint bundles and architecture frameworks must be introduced as separate `U.ViewpointBundle` species that may import TEVB. They keep `VF.TEVB.ENG` as the engineering viewpoint bundle and put architecture-only viewpoints in separate architecture-specific `U.ViewpointBundle` species.


---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB — Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__001_intro.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.17.2 — TEVB — Typical Engineering Viewpoints Bundle"
  - "E.17.2:intro — Intro"
line_start: 55316
line_end: 55346
dependencies:
  - "A.1"
  - "A.6.2"
  - "A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.TGA"
  - "F.18"
  - "U.Episteme"
  - "U.EpistemeSlotGraph"
  - "U.MultiViewDescribing"
  - "U.System"
  - "U.ViewpointBundleLibrary"
keywords:
  - "E.TGA bindings"
  - "EoIClass = U.Holon"
  - "Functional/Procedural/Role-Enactor/Module-Interface views"
  - "ISO 42010 mapping"
  - "engineering viewpoints"
  - "holon"
---

## E.17.2 - `TEVB — Typical Engineering Viewpoints Bundle`

> **Tech‑name:** `TEVB` (Typical Engineering Viewpoints Bundle, bundle id `VF.TEVB.ENG`)
> **Plain‑name:** typical engineering viewpoints bundle for holons
> **Tag:** Archetypal species of `U.ViewpointBundle` for engineering holons

**Status.** New; archetypal, notation‑agnostic species of `U.ViewpointBundle` / `U.ViewpointBundleLibrary`.
It is an engineering‑level bundle over holons; it does not itself constitute an architecture framework or architecture‑specific viewpoint library. Architecture‑focused viewpoint bundles are introduced as separate `U.ViewpointBundle` species that may import TEVB.

**Builds on.**
* **E.17.0 — `U.MultiViewDescribing`.** Supplies the generic notion of `U.Viewpoint`, `U.View`, and `ViewFamily` over an `EoIClass ⊑ U.Entity` (here: `EoIClass = U.Holon`).
* **E.17.1 — `U.ViewpointBundleLibrary`.** Provides the generic `U.ViewpointBundle`/`ViewFamilyId` structure; TEVB is a concrete bundle (`VF.TEVB.ENG`) in the core library.
* **A.1 — Holon.** Holon kinds `U.System` and `U.Episteme` as the typical engineering entities‑of‑interest.
* **A.6.2–A.6.4 — Episteme morphisms.** `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, `U.EpistemicRetargeting` as the generic morphism classes behind engineering views.
* **A.7 / E.10.D2 — Strict Distinction & I/D/S.** I/D/S discipline and DescriptionContext; engineering descriptions/specifications under TEVB are D/S‑epistemes with explicit `ViewpointRef`.
* **C.2.1 — `U.EpistemeSlotGraph`.** Provides `DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot` and the slot discipline (A.6.5) used by TEVB‑aligned descriptions/specs.

**Used by.**
* **E.18:5.12 — E.TGA viewpoint map.** As a canonical consumer, E.TGA binds its engineering transduction families (Functional, Procedural, Role‑Enactor/Device‑Structure, Module‑Interface) to TEVB viewpoints `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, `VP.ModuleInterface`.
* **E.17 (MVPK).** Publication of engineering morphisms uses TEVB engineering viewpoints on the description/spec side and PublicationVPs on the Surface side.
* **Engineering description/spec patterns.** System, method, module/interface and role‑related description/spec patterns for holons (`U.System`, `U.Episteme`) refer to TEVB when declaring their `ViewpointRef`.
* **ISO‑aligned architecture‑description bundles.** Future species patterns for architecture‑specific viewpoint bundles reuse TEVB as the canonical engineering view family (Functional vs Structural etc.) over systems and their epistemes.

**Guard (lexical & ontological).**
1. **Engineering scope only.** TEVB applies to `EoIClass = U.Holon` with typical cases `U.System` and `U.Episteme`. Using TEVB viewpoints for non‑holonic entities (e.g., pure data structures, abstract theories) requires an explicit species‑level justification; by default it is a conformance violation.
2. **Viewpoint vs Surface.** `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, `VP.ModuleInterface` are **viewpoints** (intensional `U.Viewpoint` specifications), **not** Surface kinds. They MUST NOT be used as carrier/Surface names (those remain `{PlainView, TechCard, NormsCard, InteropCard, AssuranceLane, …}` under L‑SURF).
3. **EngineeringVPId vs PublicationVPId.** `VP.*` in this pattern are **EngineeringVPId** values (E.18:5.12) and SHALL NOT be reused as PublicationVPs in MVPK. MVPK must introduce separate `PublicationVPId` symbols, linked to TEVB viewpoints only through correspondences.
4. **No new role coordinates in I/D/S.** TEVB references stakeholder groups via `U.RoleEnactor` families but does not introduce `U.Role` as a coordinate in I/D/S signatures (E.10.D2). Role semantics remain confined to RoleEnactment patterns (A.15, F‑R family).
5. **No extra viewpoints inside TEVB.** TEVB defines a **fixed core set** of four engineering viewpoints. Other labels such as “Assurance‑Oriented”, “Interop‑Oriented”, “Information/Data‑Oriented”, “Operational/Deployment”, “Mission/Context” may appear only as **lexical aliases** in E.18:5.12 (e.g. as `ViewFamilyId` / `AliasInViewFamilies` values for transduction species). They MUST NOT extend `TEVB.EngBundle.viewpoints` and MUST NOT be interpreted as additional `U.Viewpoint` kinds in this bundle; when SoTA or local practice demands explicit assurance, information, or mission viewpoints, these SHALL be provided as **separate `U.ViewpointBundle` species** that can be imported alongside TEVB rather than by mutating `VF.TEVB.ENG`.
6. **Not an architecture framework.** TEVB is an engineering‑level viewpoint bundle; architecture‑specific viewpoint bundles and architecture frameworks MUST be introduced as separate `U.ViewpointBundle` species that may import TEVB. They MUST NOT redefine `VF.TEVB.ENG` as an “architecture viewpoint library” or extend it with architecture‑only viewpoints.


---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:7.2"
section_title: "SoTA-Echoing - Alignment with post-2015 engineering practice"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__012_sota-echoing-alignment-with-post-2015-engineering-practice.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoints Bundle"
  - "E.17.2:7.2 — SoTA-Echoing - Alignment with post-2015 engineering practice"
line_start: 70875
line_end: 70891
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

### E.17.2:7.2 - SoTA-Echoing - Alignment with post-2015 engineering practice

* Modern architecture standards built on ISO/IEC/IEEE 42010 describe viewpoint libraries in which functional, behavioural and process, structural and deployment, and business and usage concerns are the dominant clusters; sector RAs such as IoT RA 30141 and space‑domain RAs provide explicit functional and construction and implementation viewpoints alongside business and usage and trustworthiness viewpoints. TEVB reuses the functional and construction and structural clusters as `VP.Functional` and `VP.ModuleInterface`, while treating business and trustworthiness as separate bundles.
* Model-based systems engineering practice (INCOSE MBSE guidance, SysML v2 “views-as-queries”, UAF/NAF view grids) converges on a small set of core diagram families: structure, behaviour, allocation and responsibility, requirements and mission. TEVB’s `VP.Procedural` and `VP.AllocationResponsibility` correspond to the behaviour and allocation-and-responsibility concerns, respectively, and are designed to be notation-neutral over SysML-, UAF-, UML-, and Capella-style models.
* The FBS family of design ontologies (Function–Behaviour–Structure and extensions) provides a widely used conceptual source for separating what a system is for, what it does over time, and what it consists of. TEVB’s four viewpoints intentionally implement a Function-Behaviour-Structure-plus-responsibility split at the holon level: `VP.Functional` ≈ Function, `VP.Procedural` ≈ Behaviour, `VP.ModuleInterface` ≈ Structure, with `VP.AllocationResponsibility` capturing the explicit mapping from functions and behaviours to role-assignment and responsibility structures.
* Within FPF itself, `E.18` transformation-flow “viewpoint families” (Functional, Procedural, Allocation-Responsibility or Device-Structure, Module-Interface, plus assurance, interoperability, data, operational, and mission labels) are harmonised by letting the **core four** be TEVB viewpoints and treating the rest as lexical or bundle-level overlays, not as new kernel viewpoints.

#### E.17.2:7.3 - Why TEVB stays small

TEVB is deliberately *not* a complete architecture framework. It gives FPF a stable, holon‑centred engineering bundle that:
* is small enough to keep in working memory and to govern via EpistemeSlotRelation discipline;
* is expressive enough to represent mappings from SoTA architecture frameworks (4+1, domain‑specific RAs, UAF/NAF grids, SysML‑based MBSE method kits);
* can be safely combined with additional `U.ViewpointBundle` species (safety and assurance packs, business and mission packs, and information and data packs) without mutating the core four;
* sits conceptually **below** architecture‑specific viewpoint libraries, which are introduced as separate `U.ViewpointBundle` species layering TEVB with mission, quality, and business viewpoints instead of redefining TEVB.

As SoTA evolves, new bundles can be added or TEVB can gain a new edition with a revised NQD‑frontier, but the TEVB‑A edition fixed here remains the archetypal engineering bundle for holons.


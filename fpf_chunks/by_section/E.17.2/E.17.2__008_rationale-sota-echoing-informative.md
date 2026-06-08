---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB — Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:7"
section_title: "Rationale & SoTA echoing  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__008_rationale-sota-echoing-informative.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "E.17.2 — TEVB — Typical Engineering Viewpoints Bundle"
  - "E.17.2:7 — Rationale & SoTA echoing  (informative)"
line_start: 63225
line_end: 63252
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.TGA"
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.2:7 - Rationale & SoTA echoing  *(informative)*

#### E.17.2:7.1 - NQD‑grounded choice of the core four

Part G’s NQD discipline treats candidate viewpoint families as points in an N/U/C/D quality space (Use‑Value, Constraint‑Fit, Novelty, Diversity_P). Applied to a SoTA‑harvested candidate set of engineering viewpoints (Functional, Behavioural/Procedural, Structural/Module, Allocation/Role, Information/Data, Assurance/Safety, Mission/Context, Deployment/Operational, Business/Usage), this yields a small Pareto frontier for *engineering holon* viewpoints. On that frontier, the `F–B–S+R` cut implemented by `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` is the minimal set that:
* spans the Function-Behaviour-Structure ontology used in contemporary design theory while adding an explicit allocation/responsibility concern;
* aligns with the “functional”, “process”, “structural”, and “deployment” clusters recurrent in standards and architecture frameworks;
* stays neutral with respect to domain‑specific qualities (`‑ilities`) and business/mission framing, which are captured in separate Q‑Bundles and governance-oriented viewpoint bundles rather than in TEVB itself.

Other candidates (e.g. dedicated information, assurance, or mission viewpoints) remain important but either duplicate concerns already captured by TEVB (when specialised to engineering holons) or are better modelled as orthogonal quality bundles (C.25) or non-engineering viewpoint bundles (business and governance viewpoint bundles). TEVB therefore pins only the core four and leaves the rest to specialised families.

#### E.17.2:7.2 - Alignment with post‑2015 engineering practice

* Modern architecture standards built on ISO/IEC/IEEE 42010 describe viewpoint libraries in which functional, behavioural/process, structural/deployment, and business/usage concerns are the dominant clusters; sector RAs such as IoT RA 30141 and space‑domain RAs provide explicit functional and construction/implementation viewpoints alongside business/usage and trustworthiness viewpoints. TEVB reuses the functional and construction/structural clusters as `VP.Functional` and `VP.ModuleInterface`, while treating business and trustworthiness as separate bundles.
* Model-based systems engineering practice (INCOSE MBSE guidance, SysML v2 “views-as-queries”, UAF/NAF view grids) converges on a small set of core diagram families: structure vs behaviour vs allocation/responsibility vs requirements/mission. TEVB’s `VP.Procedural` and `VP.RoleEnactor` correspond to the behaviour and allocation/responsibility concerns, respectively, and are designed to be notation-neutral over SysML/UAF/UML/Capella-style models.
* The FBS family of design ontologies (Function–Behaviour–Structure and extensions) provides a widely used conceptual source for separating what a system is for, what it does over time, and what it consists of. TEVB’s four viewpoints intentionally implement an FBS+R split at the holon level: `VP.Functional` ≈ Function, `VP.Procedural` ≈ Behaviour, `VP.ModuleInterface` ≈ Structure, with `VP.RoleEnactor` capturing the explicit mapping from functions/behaviours to role‑enacting carriers.
* Within FPF itself, E.TGA’s “viewpoint families” (Functional, Procedural, Role-Enactor or Device-Structure, Module-Interface, plus assurance, interoperability, data, operational, and mission aliases) are harmonised by letting the **core four** be TEVB viewpoints and treating the rest as lexical or bundle-level overlays, not as new kernel viewpoints.

#### E.17.2:7.3 - Why TEVB stays small

TEVB is deliberately *not* a complete architecture framework. It gives FPF a stable, holon‑centred engineering bundle that:
* is small enough to keep in working memory and to govern via EpistemeSlotGraph discipline;
* is expressive enough to represent mappings from SoTA architecture frameworks (4+1, domain‑specific RAs, UAF/NAF grids, SysML‑based MBSE method kits);
* can be safely combined with additional `U.ViewpointBundle` species (safety/assurance packs, business/mission packs, information/data packs) without mutating the core four;
* sits conceptually **below** architecture‑specific viewpoint libraries, which are introduced as separate `U.ViewpointBundle` species layering TEVB with mission/quality/business viewpoints instead of redefining TEVB.

As SoTA evolves, new bundles can be added or TEVB can gain a new edition with a revised NQD‑frontier, but the TEVB‑A edition fixed here remains the archetypal engineering bundle for holons.


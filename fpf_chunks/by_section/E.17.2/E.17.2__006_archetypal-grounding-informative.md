---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB — Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:5"
section_title: "Archetypal grounding  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__006_archetypal-grounding-informative.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "E.17.2 — TEVB — Typical Engineering Viewpoints Bundle"
  - "E.17.2:5 — Archetypal grounding  (informative)"
line_start: 64981
line_end: 65011
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
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.2:5 - Archetypal grounding  *(informative)*

A minimal TEVB instantiation looks as follows:

```
TEVB.EngBundle :
  U.ViewpointBundle {
    viewFamilyId   = VF.TEVB.ENG
    EntityOfConcernClassSpec   = { h : U.Holon | HolonKind(h) ∈ {System, Episteme} }
    viewpoints     = { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
    LibraryRef     = FPF.Core.Viewpoints
  }
```

Each `VP.*` viewpoint is a `U.Viewpoint` as in E.17.0, with:

* `viewpointId ∈ {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`,
* `EntityOfConcernClassSpec` inherited from `TEVB.EngBundle`,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` aligned with the subsections above.

**Engineering holon (example).**

Let `Plant_X : U.System` be a production plant, and `ControlStack_X : U.Episteme` be its control and optimisation stack as a holon.

* Under `VP.Functional`, `Plant_X` is viewed as a bundle of capabilities, functional behaviors, and required transformations: material/energy/product flows, optimisation functions, safety envelopes.
* Under `VP.Procedural`, `Plant_X` is viewed as sets of procedures and control sequences: startup/shutdown, normal operation, emergency handling.
* Under `VP.RoleEnactor`, `Plant_X` is viewed as networks of role‑enactors: human operators, controllers, subsystems enacting roles in SOPs and safety cases.
* Under `VP.ModuleInterface`, `Plant_X` is viewed as modules and interfaces: equipment units, pipelines, control modules, buses, and their interfaces and specifications.

Each of these is a **family of Description epistemes and specification-use cases** with `DescriptionContext = ⟨EntityOfConcernRef(Plant_X or ControlStack_X), BoundedContextRef, ViewpointRef=VP.*⟩` and TEVB ensures that `E.18` and MVPK can rely on this common structure.


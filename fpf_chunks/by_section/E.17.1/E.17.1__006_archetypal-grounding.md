---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__006_archetypal-grounding.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:5 — Archetypal Grounding"
line_start: 79602
line_end: 79610
dependencies:
  - "A.16.0"
  - "A.22"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.13"
  - "C.2.1"
  - "C.2.2a"
  - "C.29"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "E.7"
  - "F.9"
  - "F.9.1"
keywords:
  - "alias discipline"
  - "engineering/management/research bundles"
  - "governance"
  - "import discipline"
  - "reusable viewpoint family"
  - "viewpoint bundle"
---

### E.17.1:5 - Archetypal Grounding


**Tell.** A viewpoint bundle library lets FPF say "use this already-defined viewpoint family" without confusing that family with the concrete views or publication faces that later realize it.

**Show (System).** A TEVB engineering bundle can package exact `U.ViewpointRef` members `ref(VP.Functional)`, `ref(VP.Procedural)`, `ref(VP.AllocationResponsibility)`, and `ref(VP.ModuleInterface)` for holon descriptions. Each reference resolves the exact viewpoint episteme P designated by its corresponding `VP.*` token. Later `MultiViewDescribing` uses import that exact bundle edition and the needed reference subset rather than redefining the same engineering viewpoints each time.

**Show (Episteme).** A governance-oriented bundle can package exact `U.ViewpointRef` members `ref(VP.Risk)`, `ref(VP.Control)`, `ref(VP.Compliance)`, and `ref(VP.Operations)` as one reusable family for service or program descriptions. Each reference resolves the exact viewpoint episteme P designated by its corresponding `VP.*` token. Publication faces/forms may later expose that family, but the bundle itself remains a value inside a viewpoint-family catalogue `U.Episteme`, not the report publication face.


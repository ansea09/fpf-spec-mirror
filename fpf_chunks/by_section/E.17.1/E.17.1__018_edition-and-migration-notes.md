---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:17"
section_title: "Edition and Migration Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__018_edition-and-migration-notes.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:17 — Edition and Migration Notes"
line_start: 78297
line_end: 78319
dependencies:
  - "A.16.0"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.2.2a"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.18"
  - "E.7"
  - "F.9"
  - "F.9.1"
  - "U.MultiViewDescribing"
keywords:
  - "alias discipline"
  - "engineering/management/research bundles"
  - "governance"
  - "import discipline"
  - "reusable viewpoint family"
  - "viewpoint bundle"
---

### E.17.1:17 - Edition and Migration Notes

#### E.17.1:17.1 - Rename vs semantic change

A lexical rename that leaves viewpoint meaning and membership unchanged may be treated as a naming-layer migration. A change in membership, concern, admissibility, or member semantics is not just a rename; it requires a new edition or a new local bundle.

#### E.17.1:17.2 - Migration from local `Sigma` lists

Legacy `U.MultiViewDescribing` families often publish only one local list of viewpoints. Migration should proceed by:

1. identifying recurring families across several such local lists,
2. publishing those families as explicit bundles,
3. then rewriting the local families to import the new `ViewFamilyId` and declare any subset selection explicitly.

This sequence preserves provenance and avoids pretending that the reusable family had always existed.

#### E.17.1:17.3 - Migration from publication-face/form-bound naming

If a legacy practice uses one label interchangeably for a viewpoint family, a report section, and a publication face, migration should separate those positions explicitly. `ViewFamilyId` remains at the bundle layer; `U.Viewpoint` ids remain at the viewpoint layer; publication-face names remain publication-layer vocabulary.

#### E.17.1:17.4 - Boundary to annex growth

Annex manifests are useful, but a bundle should not become a thin shell hiding all of its meaning elsewhere. The core bundle still needs enough explicit member and family structure to stand on its own. Annexes deepen reuse; they do not replace the bundle's primary declaration.

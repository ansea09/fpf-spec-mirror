---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:17"
section_title: "Edition and Migration Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__018_edition-and-migration-notes.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:17 — Edition and Migration Notes"
line_start: 81899
line_end: 81921
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
---

### E.17.1:17 - Edition and Migration Notes

#### E.17.1:17.1 - Rename vs semantic change

A lexical rename that leaves viewpoint meaning and membership unchanged may be treated as a naming-layer migration. A change in membership, concern, admissibility, or member semantics is not just a rename; it requires another catalogue edition or family declaration.

#### E.17.1:17.2 - Migration from local `Sigma` lists

Legacy `MultiViewDescribing` uses often publish only one local list of viewpoints. Migration should proceed by:

1. identifying recurring families across several such local lists,
2. publishing those families as explicit bundles,
3. then rewriting the local families to import the new ordinary family designator and declare any subset selection explicitly.

This sequence preserves provenance and avoids pretending that the reusable family had always existed.

#### E.17.1:17.3 - Migration from publication-face/form-bound naming

If a legacy practice uses one label interchangeably for a viewpoint family, a viewpoint, a report section, and a publication face, migration separates those positions explicitly. The ordinary family designator remains at the declaration layer; exact `U.ViewpointRef` values resolve P while any reader-facing viewpoint token is only P's designator; publication-face names remain publication-layer vocabulary.

#### E.17.1:17.4 - Boundary to annex growth

Annex references are useful, but a declaration should not become a thin shell hiding all of its meaning elsewhere. The core declaration claim block still needs enough explicit member and family structure to stand on its own. Annexes deepen reuse; they do not replace the declaration's primary claims.

---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__002_problem-frame.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:1 — Problem frame"
line_start: 61896
line_end: 61903
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

### E.17.1:1 - Problem frame

**Selected-family discipline.** Viewpoint bundles declare `EntityOfConcernClassSpec` constraints for the selected entities their viewpoints can describe. Bundle labels, aliases, annexes, files, and publication faces never select the entity by themselves.

`U.MultiViewDescribing` lets a description family state that one entity of concern is rendered through several viewpoints with declared correspondences. In practice many such viewpoint families recur across projects and schools: engineering teams reuse functional / procedural / structural / interface viewpoints; governance teams reuse risk / control / compliance / operations viewpoints; research teams reuse theory / experiment / inference / limitation viewpoints.

FPF therefore needs one explicit governing pattern for reusable viewpoint families so that authors can import them, name them stably, review them once, and keep viewpoint-family identity separate from document labels and publication faces/forms.


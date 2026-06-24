---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__003_problem-frame.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:1 — Problem frame"
line_start: 54894
line_end: 54908
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD.BA"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.MLAO"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "G.5"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "candidate-description boundary"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:1 - Problem frame

Architecture practice needs durable descriptions: multi-view documents, view models, generated relation graphs, architecture transformation-flow views, LCA control sketches, module or interface diagrams, deployment views, model cards, system cards, and architecture decision description sets. These descriptions are useful because they let teams compare, reuse, refresh, inspect, and use architecture claims across viewpoint families and working concerns; A.15 allocation-responsibility semantics apply only when a project role relation itself is being governed.

The difficulty is that the description is not the architecture. The same architecture can have several descriptions. The same description set can contain several views. Each view is written from one viewpoint or concern-framed practice and can hide, lose, coarsen, or emphasize different structure. A view can describe functional structure, flow or transformation-flow structure, control structure, module or interface structure, placement structure, information custody, evidence-reuse relation, assurance relation, scale or coarsening relation, or another declared architecture-relevant structure.

The first-minute practitioner can ask:

- What `ArchitectureOf@Context` is this description about?
- Which selected structures or structure kinds does this view describe?
- Which viewpoint makes this view useful?
- What correspondence connects this view to the architecture claim and other views?
- When does source return to a source episteme, source view, or direct governing pattern for that claim become necessary?
- What admissible architecture move remains after the description has been used?


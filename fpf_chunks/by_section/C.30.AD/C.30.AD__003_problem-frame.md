---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__003_problem-frame.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:1 — Problem frame"
line_start: 60244
line_end: 60259
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
  - "A.6.3.NAR"
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
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
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

The difficulty is that a description is not the architecture, an obtaining architecture relation, or its selected structure. The same holon and architecture-relation occurrence can have several descriptions. A description set can contain several separately identified epistemes. One such episteme is a `U.View` only while an exact `EpistemeViewpointConformanceRelation` obtains between that same episteme and one exact viewpoint episteme. Each view can hide, lose, coarsen, or emphasize different structure. A view can describe functional structure, flow or transformation-flow structure, control structure, module or interface structure, placement structure, information custody, evidence-reuse relation, assurance relation, scale or coarsening relation, or another declared architecture-relevant structure.

The first-minute practitioner can ask:

- What exact holon, obtaining `ArchitectureRelation` occurrence, or selected structure is this description episteme about?
- What exact claim graph, one EntityOfConcern, and effective `U.ReferenceScheme` keep that episteme identifiable?
- Which selected structures or structure kinds does this description carry?
- Which exact viewpoint episteme and conformance relation, if any, make this same episteme a `U.View`?
- What correspondence connects this description to architecture claims and other view epistemes without inventing a subject relation?
- Which source episteme, source view, representation, or publication enters this use through which source-to-use path, and what stronger use would activate a source-return condition?
- What admissible architecture move remains after the description has been used?


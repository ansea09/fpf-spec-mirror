---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__003_problem-frame.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:1 — Problem frame"
line_start: 57238
line_end: 57253
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
  - "E.10.D2"
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

Architecture practice needs descriptions that remain useful over time: multi-view documents, view models, generated relation graphs, transformation-flow views, control sketches, module or interface diagrams, deployment views, model cards, system cards, and architecture-decision description sets. Teams use them to compare, reuse, refresh, and inspect architecture claims. If a project also claims a system-role assignment, Work attribution, authority, or responsibility, keep that as a separate claim: use A.2.1 and F.6 for assignment and Work, and an admitted domain relation or an A.6.RCD missing governor for responsibility. `VP.AllocationResponsibility` is only a clue to the concern.

A description is not the architecture, an architecture relation that actually holds, or the selected structure. The same holon or relation occurrence can have several descriptions, and a description set can contain several separately identified epistemes. A description counts as `U.View` only while the E.17.0 conformance relation actually holds between that same episteme and one viewpoint episteme. Different views can hide, lose, coarsen, or emphasize different structures: for example functional, flow, control, module, interface, placement, information-custody, evidence-reuse, assurance, or scale structure.

The first-minute practitioner can ask:

- What holon, obtaining `ArchitectureRelation` occurrence, or selected structure is this description about?
- Which ClaimGraph, EntityOfConcern, and reference scheme identify the description?
- Which structures and structure kinds does it describe?
- If it is called a `U.View`, which viewpoint and which conformance relation make that true?
- What claim or relation connects it to architecture claims and other views without pretending that proximity creates correspondence?
- Which sources, representations, or publications enter this use, by what path, and when must stronger use return to a source?
- After using the description, what architecture move remains admissible?


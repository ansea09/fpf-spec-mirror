---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__003_problem.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:2 — Problem"
line_start: 61892
line_end: 61904
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.21"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
  - "G.5"
keywords:
  - "ArchitectureDecisionRelation@Project"
  - "accepted loss"
  - "affected selected structure"
  - "architect-developer split"
  - "architecture-characteristic trade-off"
  - "method-use instruction"
  - "project architecture decision"
  - "reopen condition"
  - "selected architecture option"
---

### C.32.PAD:2 - Problem


Architecture synthesis produces candidates; project work still needs a decision. The decision is not the candidate palette, not the selected set publication, not the architecture description, and not the ADR file. It is the project relation that says which architecture option is now pursued and what follows from that selection.

The problem is difficult because architecture decisions sit between structures and methods. Architecture descriptions describe selected structures of the target holon. A project architecture decision can also tell developer roles which method description, architectural style, pattern use, or work boundary they must follow so that later work produces or preserves the intended structures. For example, "use the client-server style here" is a method-use instruction whose intended result is a module and interaction structure of the target system. The decision relation must keep both sides visible: intended structure of the transformed holon and method expectations for the transformer holon.

The problem is also multilevel. The architect may decide selected structures at one holon level while developers later refine lower-level structures. A decision must therefore say where the architect-owned architecture claim stops, where developer-owned refinement starts, which source detail must remain recoverable, and which result can reopen the decision. If that boundary is missing, architecture governance becomes either empty advice or uncontrolled micro-management.

Finally, architecture decisions are evolutionary. They are made under current candidate knowledge, current characteristic criteria, current eval readings, and current organization or tool constraints. They should be explicit enough for present work and cheap enough to supersede when a better candidate, changed characteristic pressure, or transformer-transformed mismatch appears.

C.32.PAD solves the post-synthesis decision problem by making the decision relation explicit before any ADR-like publication projection is written.


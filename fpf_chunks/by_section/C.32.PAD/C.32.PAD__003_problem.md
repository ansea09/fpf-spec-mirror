---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__003_problem.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:2 — Problem"
line_start: 66151
line_end: 66163
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.6"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.2"
  - "A.2.1"
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
  - "C.30.TFS-REL"
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
  - "E.18.NET"
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


Architecture synthesis produces candidates; the Systems performing project Work still need a decision, while any local system-role kind, direct assignment species, authority, or responsibility claim remains a separate fact established through its own pattern. The decision is not the candidate palette, the declared selected-set result, its publication, the architecture description, or the ADR file. It is the architecture decision relation that identifies the composite project Work, says which architecture option is now pursued for it, and records what follows from that selection.

The problem is difficult because architecture decisions sit between structures and Methods. C.30 keeps an obtaining `ArchitectureRelation` with its holon and selected `U.Structure` separate from an `ArchitectureClaim` carrying candidate, required, desired, or expected content. A project architecture decision can tell intended developer Systems which Method description, architectural style, pattern use, or work boundary to follow so that later work aims to produce or preserve the intended structures. For example, "use the client-server style here" is a Method-use instruction whose intended result is a module and interaction structure of the described System. The decision relation must keep actual or modal structure content, intended Systems, local kinds, separate System-classification judgments, assignment requirements and current assignment occurrences, plans and commitments, permissions and authority, and actual Work as separate branches. Route unresolved role wording through `E.10.ROLE`. When C.32.CONWAY supplies an influence-source architecture or selected structure, that source remains non-agentive and does not become the performer.

The problem is also multilevel. The architecture decision may fix selected structures at one holon level while leaving lower-level refinement open. It must therefore say which structure is fixed, which refinement remains open, which source detail must remain recoverable, and which result can reopen the decision. If that boundary is missing, the decision becomes either empty advice or uncontrolled micro-management.

Finally, architecture decisions are evolutionary. They are made under current candidate knowledge, current characteristic criteria, current eval readings, and current organization or tool constraints. They should be explicit enough for present work and cheap enough to supersede when a better candidate, changed characteristic pressure, or architecture-influence/transformed-side fit changes.

C.32.PAD solves the post-synthesis decision problem by making the decision relation explicit before any ADR-like publication projection is written.


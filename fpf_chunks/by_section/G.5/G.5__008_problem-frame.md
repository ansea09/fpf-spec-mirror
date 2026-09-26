---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Method-Family Registry, Dispatch and Selected-Set Result Declaration"
section_id: "G.5:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__008_problem-frame.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "G.5 — Method-Family Registry, Dispatch and Selected-Set Result Declaration"
  - "G.5:1 — Problem frame"
line_start: 113139
line_end: 113152
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
  - "E.4.PFR"
  - "G.0"
  - "G.11"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "JointUseSet"
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry and eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set result declaration"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:1 - Problem frame


The exact `CG‑Frame` card from **G.1** and `SoTA Synthesis Pack@CG‑Frame` from **G.2** name the frame, `EntityOfConcernRef`, ReferencePlane, source rows, and rival internally coherent **method families** (and sometimes **generator families**) that may address the same declared task. If their breadth is used as a premise, cite G.2's pack `CoverageJudgementRef` and its HarvestPolicy basis. Registration does not recount cards as families; a combined method/generator coverage result does not establish method-only coverage for dispatch.

At the same time, the scale and coordinate definitions from **G.3** and the typed operator-argument and result declarations from **G.4** make admissible calculi and acceptance clauses explicit - enough to formulate *eligibility*, *assurance*, and *admissibility* constraints, but not enough to pick "the method" without collapsing plurality.

You need a **notation‑independent** way to:

1. register method families and generator families as *auditable, versioned* entries,
2. select, compose, or fall back among them at run time for a concrete task instance,
3. declare stable selected-set results, including retained-alternative and all-member results, and publish stable identities to UTS when required, and
4. emit RSCR‑relevant triggers and pins without inventing new “shadow specs”.


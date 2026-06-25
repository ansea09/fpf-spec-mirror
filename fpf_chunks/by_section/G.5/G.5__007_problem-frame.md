---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__007_problem-frame.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:1 — Problem frame"
line_start: 87795
line_end: 87807
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "G.0"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
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
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:1 - Problem frame

A `CG‑FrameContext` (from **G.1**) and a `SoTA Synthesis Pack@CG‑Frame` (from **G.2**) expose multiple rival, internally coherent **method families** (and sometimes **generator families**) that can plausibly act on the same `EntityOfConcernRef` and ReferencePlane.

At the same time, the typed slot, scale, and coordinate definitions from **G.3** and **G.4** yield admissible calculi and acceptance clauses - enough to formulate *eligibility*, *assurance*, and *admissibility* constraints, but not enough to pick "the method" without collapsing plurality.

You need a **notation‑independent** way to:

1. register method families and generator families as *auditable, versioned* entries,
2. select, compose, or fall back among them at run time for a concrete task instance,
3. publish stable selected-set results and stable identities to UTS, and
4. emit RSCR‑relevant triggers and pins without inventing new “shadow specs”.


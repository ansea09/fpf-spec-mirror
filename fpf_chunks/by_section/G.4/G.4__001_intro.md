---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__001_intro.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:intro — Intro"
line_start: 99723
line_end: 99734
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.18"
  - "A.19"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.23"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CAL Pack@CG-Frame"
  - "Context charter"
  - "acceptance clause"
  - "legal flow"
  - "pass \\"
  - "typed operator card"
---

## G.4 - CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring

**Use this when.** A team has typed characteristics and now needs to publish reusable operators, acceptance clauses, and legal compositions before any candidate is actually evaluated. The working object is one design-time `CAL Pack@CG-Frame`, not an evaluation run, verdict, selector outcome, assurance case, or decision.

**First move.** Write one plain acceptance sentence for one task: “For subject `x` in Context `C`, apply declared operator `O` to named C.16 result episteme `E`; return `pass | fail | unknown` under clause `A`, threshold/policy `P`, and stated currentness window.” Then turn only the nouns needed by that sentence into stable CAL declarations.

**Smallest viable CAL pack.** Publish one Context charter, one typed operator card, one acceptance clause with unknown/failure behavior, one legal flow, one evidence/currentness profile, one proof-or-gap row, one worked declaration example, and a minimal `TaskMap` that cites their ids. Stop there when this pack answers the task; method-family extensions, archive surfaces, crossing records, and additional policy pins enter only when the case actually needs them.

**What changes in practice.** Thresholds and failure behavior stop hiding in code, illegal arithmetic becomes an authoring defect, and runtime workers can cite stable declarations without pretending that a card, flow, manifest, proof row, or stored evidence ref performed an evaluation.

**Not this pattern.** Use C.16 for the measurement result, A.19 for comparison/selection, A.15.1 and A.6.1 for dated evaluation work and actual bindings, C.2.1 for the verdict episteme, A.10/G.6 for provenance, G.11 for currentness, B.3 for assurance, and C.11 for a decision. If the immediate question is whether a declared clause actually ran and what result obtained, go directly to the declaration-to-runtime boundary in §4.4a.


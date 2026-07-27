---
chunk_kind: "child"
pattern_id: "C.34"
pattern_title: "Structural Correspondence, Equivalence, and Morphism Adequacy"
section_id: "C.34:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.34/C.34__003_problem.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.34 — Structural Correspondence, Equivalence, and Morphism Adequacy"
  - "C.34:2 — Problem"
line_start: 66303
line_end: 66310
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "A.6.M"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ADR"
  - "C.32.PAD"
  - "E.18"
  - "F.15"
  - "F.9"
keywords:
  - "directionality"
  - "equivalence"
  - "lost structure"
  - "mapping mode"
  - "morphism"
  - "preserved structure"
  - "scope"
  - "structural correspondence"
---

### C.34:2 - Problem

Architecture work often needs "same enough" claims. A view should correspond to a description. A generated graph should preserve selected dependencies. A candidate should preserve required interfaces while changing placement. A realized structure should match an expected selected structure enough for an evaluation or decision repair. A neural-network substitution should preserve dataflow or routing while changing memory and compute trade-offs.

The dangerous shortcut is to accept visual similarity, label sameness, graph isomorphism, or formal vocabulary as adequacy. An edge-isomorphic graph can lose relation semantics. A projection can preserve module names while dropping control authority. A category-theoretic morphism can be useful as a C.29 lens without proving architecture equivalence. A DSM cluster can preserve co-change pressure while losing functional bearer semantics.

C.34 makes the preservation claim explicit before the result is used.


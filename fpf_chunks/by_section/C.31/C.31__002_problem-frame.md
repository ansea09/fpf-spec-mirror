---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__002_problem-frame.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:1 — Problem frame"
line_start: 57524
line_end: 57553
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31.ASAP"
  - "C.31.RSA"
  - "C.32"
  - "G.5"
keywords:
  - "ModularityVectorLite"
  - "bespoke residue"
  - "cohesion"
  - "coupling"
  - "evidence reuse"
  - "interface variation"
  - "modularity characteristics"
  - "reusable-structure characteristics"
  - "substitutability"
---

### C.31:1 - Problem frame

Use this pattern when modularity or reusable-structure language is doing work in an architecture discussion and the practitioner needs to know which few characteristics matter, what repair follows, and whether any measurement or comparison is admissible.

The first useful move is deliberately small:

```text
ModularityVectorLite:
  describedHolonRef:
  boundedContextRef:
  architectureClaimRef?:
  structureKindRefs:
  threeLiveCharacteristicsAtMost:
  observedProblem:
  repairDirection:
  relatedClaimGovernanceIfClaimed:
  nonAdmissibleOverread:
  stopCondition:
```

Start with recognition, at most three characteristics under evaluation, the observed problem, and a repair direction. A report-only proxy is an admissible stop when no beyond-local-repair use is being made.

Claim-use boundary: comparison, publication, evidence, assurance, gate, decision, benchmark, causal-use, cross-case reuse, selection, procurement, and architecture scale-preference are beyond-local-repair uses in C.31. Add their fields only when that use is being made and recoverable by value and the governing pattern can be named.

What goes wrong if C.31 is missed: "modular" becomes a binary label; a single modularity score hides incompatible characteristics; interface publication is confused with substitutability; internal cohesion is improved while evidence reuse gets worse; bespoke residue moves from templates into work or assurance; and complexity language becomes a commensurable score without a declared characteristic, scale, measurement basis, comparison basis, or admissible-use boundary.

What C.31 buys in practice: the practitioner can see which modularity characteristic changes the next architecture use, which false use is blocked, which repair is plausible, and which governing pattern governs measurement, evidence, causal, scale, selection, or accounting claims.

Not this pattern when the question under repair is only source-label recovery, module-interface relation repair, reusable-structure accounting, general measurement admissibility, quality-family claim, architecture scale-preference claim, mathematical-lens use, candidate architecture synthesis, or selection. Use `C.30.STRAT`, `A.6.M`, `C.31.RSA`, `C.16`, `C.25`, `C.31.ASAP`, `C.29`, `G.5`, or `C.11` as appropriate; do not treat C.31 as the synthesis or selector pattern.


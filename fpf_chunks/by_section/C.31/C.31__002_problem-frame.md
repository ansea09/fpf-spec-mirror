---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__002_problem-frame.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:1 — Problem frame"
line_start: 74327
line_end: 74360
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
  - "C.31"
  - "C.31.ASAP"
  - "C.31.RSA"
  - "C.32"
  - "C.32.P2S"
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

First identify the few characteristics that matter to the architecture question, the observed difficulty and any needed repair. An adequate ordinary account can finish; `ModularityVectorLite` offers a compact way to retain it:

```text
ModularityVectorLite:
  describedHolonRef:
  architectureQuestion:
  intendedArchitectureUse:
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?:
  architectureClaimRef?:
  selectedStructureRefs:
  structureKindRefs:
  threeLiveCharacteristicsAtMost:
  observedProblem:
  repairDirection:
  relatedClaimPatternLocatorsIfClaimed:
  nonAdmissibleOverread?:
  stopCondition:
```

For the first diagnostic move, select at most three characteristics and connect them to the observed problem and any warranted repair. This limits the first inquiry, not the eventual analysis. A clearly bounded report-only proxy can be a sufficient result.

Claim-use boundary: before relying on a characteristic for comparison, causal explanation, assurance, selection or another further use, establish the grounds required by that claim. Making a qualified local account available to an audience preserves its limits; publication alone does not turn it into a measurement or a selection result. Add only the information on which the receiving use depends.

What goes wrong if C.31 is missed: "modular" becomes a binary label; a single modularity score hides incompatible characteristics; interface publication is confused with substitutability; internal cohesion is improved while evidence reuse gets worse; bespoke residue moves from templates into work or assurance; and complexity language becomes a commensurable score without a declared characteristic, scale, measurement basis, comparison basis, or admissible-use boundary.

What C.31 buys in practice: the practitioner can choose the modularity characteristic that matters, identify a warranted repair, and determine what further measurement, evidence, causal, scale, selection or accounting grounds the intended use requires.

Not this pattern when the question under repair is only source-label recovery, module-interface relation repair, reusable-structure accounting, general measurement admissibility, quality-family claim, architecture scale-preference claim, mathematical-lens use, candidate architecture synthesis, or selection. Use `C.30.STRAT`, `A.6.M`, `C.31.RSA`, `C.16`, `C.25`, `C.31.ASAP`, `C.29`, `C.32`, `G.5`, or `C.11` as appropriate: `C.32` governs candidate architecture synthesis, `G.5` selected-set result declaration, and `C.11` local choice.


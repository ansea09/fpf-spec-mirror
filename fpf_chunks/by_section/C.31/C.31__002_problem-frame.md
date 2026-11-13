---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__002_problem-frame.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:1 — Problem frame"
line_start: 78483
line_end: 78535
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
  liveCharacteristics:
  observedProblem:
  repairDirection:
  relatedClaimPatternLocatorsIfClaimed:
  nonAdmissibleOverread?:
  stopCondition:
```

For the first diagnostic move, select the characteristics needed to explain the observed problem and choose the next warranted repair. Keep this first inquiry small while preserving every distinction that changes that move. A bounded report-only proxy can be a sufficient result.

Claim-use boundary: before relying on a characteristic for comparison, causal explanation, assurance, selection or another further use, establish the grounds required by that claim. Making a qualified local account available to an audience preserves its limits; publication alone does not turn it into a measurement or a selection result. Add only the information on which the receiving use depends.

What goes wrong if C.31 is missed:

- "modular" becomes a binary label;
- a single modularity score hides incompatible characteristics;
- interface publication is confused with substitutability;
- internal cohesion is improved while evidence reuse gets worse;
- bespoke residue moves from templates into work or assurance; and
- complexity language becomes a commensurable score without a declared characteristic, scale, measurement basis, comparison basis, or admissible-use boundary.

What C.31 buys in practice: the practitioner can choose the modularity characteristic that matters, identify a warranted repair, and determine what further measurement, evidence, causal, scale, selection or accounting grounds the intended use requires.

For a question limited to one of the following, use the indicated pattern instead of C.31:

| Question | Pattern |
| --- | --- |
| Source-label recovery | `C.30.STRAT` |
| Module-interface relation repair | `A.6.M` |
| Reusable-structure accounting | `C.31.RSA` |
| General measurement admissibility | `C.16` |
| Quality-family claim | `C.25` |
| Architecture scale-preference claim | `C.31.ASAP` |
| Mathematical-lens use | `C.29` |
| Candidate architecture synthesis | `C.32` |
| Selection | `G.5` for selected-set result declaration; `C.11` for local choice |


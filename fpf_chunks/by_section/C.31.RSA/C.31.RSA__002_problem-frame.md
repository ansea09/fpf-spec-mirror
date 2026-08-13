---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__002_problem-frame.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:1 — Problem frame"
line_start: 63881
line_end: 63913
dependencies:
  - "A.10"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "G.5"
  - "G.6"
keywords:
  - "accounting basis"
  - "bespoke residue"
  - "refactoring opportunity"
  - "report-only share"
  - "reusable share"
  - "reusable-structure accounting"
  - "source return"
---

### C.31.RSA:1 - Problem frame

Use this pattern when a practitioner needs to locate where reusable structure lives, where bespoke residue grows, which accounting basis is being used, what can be refactored, and what remains a bounded exception or source-return condition. A report-only share stays report-only unless the relevant outside-RSA use is governed by its governing pattern.

Claim-use boundary: any use that relies on the RSA account to make a stronger claim is outside RSA. Examples include comparison, publication, evidence validity, assurance or safety-case reliance, gate use, architecture scale preference, causal use, selected-set result declaration, candidate synthesis, and local decision. Record with C.31.RSA only the reusable locus, bespoke residue, accounting basis, report-only share, repair direction, and source-return condition. Add another claim only after naming and applying the pattern that defines and tests it.

The first useful move is `ReusableStructureTriage`:

```text
ReusableStructureTriage:
  describedHolonRef:
  boundedContextRef:
  architectureClaimRef?:
  structureRefs or structuralAspectRefs:
  whereReusableStructureCurrentlyLives:
  whereBespokeResidueCurrentlyGrows:
  residueRefactoredInto:
    template | interfaceSpecification | methodDescription |
    workStructure | evidencePackage | assuranceArgumentStructure | otherDeclared
  residueAcceptedAsBoundedException:
  sourceReturnCondition?:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

Use the fuller accounting description only when an accounting basis and structure references are declared. Ordinary use stops when the practitioner knows where reusable structure lives, where bespoke residue grows, what can be refactored, and what remains a bounded exception.

What goes wrong if C.31.RSA is missed: a reusable share is treated as a proof of modularity; one-off work is hidden under a reuse label; evidence reuse is counted without validity context; hidden residual uncertainty is averaged with reusable templates; and "more reusable structure" is treated as always better.

What C.31.RSA buys in practice: the practitioner can state where structure is reusable, where it is bespoke, what source-side distinctions must remain reachable, and when the result is only report-only accounting.

Not this pattern when the question under repair is source-label recovery, module-interface relation repair, modularity-characteristic selection, measurement or comparability admissibility, architecture scale preference, mathematical-lens use, or any outside-RSA use named above. Use `C.30.STRAT`, `A.6.M`, `C.31`, `C.16`, `A.10`, `B.3`, `G.6`, `C.31.ASAP`, `C.29`, `G.5`, or `C.11` as appropriate; do not treat C.31.RSA as the synthesis or selector pattern.


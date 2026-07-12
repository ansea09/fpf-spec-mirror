---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__002_problem-frame.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:1 — Problem frame"
line_start: 60296
line_end: 60384
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "synthesis structure map"
  - "trade-off front"
---

### C.32:1 - Problem frame

Use this pattern when a practitioner has a grounded `ArchitectureOf@Context` question and needs to synthesize several candidate architecture configurations across selected structures before comparison, archive or front-policy work, publication of a selected set, or decision.

Primary working reader: an architect or architecture-responsible practitioner preparing alternatives for one described holon before comparison, selection, publication of a selected set, local choice, or project decision.

Typical entry phrases:

```text
"The functional structure is clear, but module allocation and placement change the trade-off."
"One platform proposal improves reuse and worsens evidence or control burden."
"A search or workshop produced options; which selected structures and architecture characteristics do they change?"
"We need a candidate palette with structurally different architecture configurations before choosing one."
"The architecture of the team or tool that changes the target holon no longer fits the target architecture."
```

**First-minute use slice.** A regulated product-family team has a grounded `ArchitectureOf@Context` for a field device family. The work question is synthesis: how should required functions, constructive modules, field placement, control responsibility, and certification evidence be coordinated so maintainability, substitutability, latency, and evidence reuse stay acceptable? Using C.32, the practitioner first builds a synthesis structure map, then records three candidate configurations: one shared module grammar with tighter evidence scope, one product-family split with lower interface burden, and one bounded exception that keeps the existing module split but changes evidence responsibility and reopen trigger. The team now has candidate architecture configurations under declared characteristics, not one attractive platform proposal.

The primary `EntityOfConcern` is the local candidate architecture palette for one synthesis question over `ArchitectureOf@Context`. The described holon can be a system, product family, organization-as-system, discipline, AI-agent setup, built asset, episteme, work occurrence, or another admitted holon kind when the governing FPF pattern admits that use. Source labels such as practice, culture, tradition, style, method, or role enter C.32 only after they are restored into admitted holons, method-side structures, role-side structures, work structures, epistemes, bounded contexts, or C.36 cultural-evolution relations by their governing patterns. Architecture pressure may concern method-family or role-side structures, but then C.32 treats them as selected structures or adjacent governed values around a described holon or bounded context, not as admitted holon kinds by label. C.32 is not software-system architecture by default; software-system sources are one source family and one domain example.

What goes wrong if C.32 is missed: the team optimizes one visible structure, such as modules, placement, team responsibility, control relation, or evidence package, and then treats that local improvement as architecture synthesis. The competing structures, architecture characteristics, losses, and alternatives disappear before they can be compared.

What C.32 buys in practice: a practitioner can build a small set of candidate architecture configurations, each grounded in selected structure changes, architecture characteristics, known losses, and receiving patterns.

Ordinary working move: name the selected structures that really change, name the few architecture characteristics that make the trade-off real, then write two to five candidate configurations with gain, loss, preserved structure, hidden loss, and next receiving use.

Adoption test: after using C.32, another practitioner can see at least two structurally different candidate configurations, the selected-structure changes, the architecture characteristics under pressure, each gain and loss, the source-return condition, and the next receiving use.

Use C.32 only for candidate palette construction. Do not use it to ground the architecture claim, recover one structure, build characteristic criteria rows, design eval programs, handle transformer correspondence, run archive or front-policy work, publish a selected set, choose locally, or decide the project architecture.

Common exits by claim kind:

- `C.30` grounds the architecture claim; `C.30.ASV`, `A.6.F`, and `A.6.M` recover structural views, function wording, and module-interface relations.
- `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, `C.25`, `C.31`, `C.31.ASAP`, and `C.16` govern starter heads, project criteria rows, eval programs, Q-Bundles, modularity or scale-preference claims, and measurement.
- `C.32.MLAO`, `C.32.CONWAY`, `C.32.FAIL`, and `C.29` govern residual-reducing frames, transformer-transformed correspondence, candidate repair, and mathematical-lens use.
- `A.19.CPM`, `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `C.11`, and `C.32.PAD` govern comparison, selection, archive, front, publication of a selected set, local choice, and decision work.
- `C.30.AD`, `E.17`, `E.24.PUB`, `A.10`, and `B.3` govern architecture-description, publication-face, evidence, and assurance claims.

The first useful output is `CandidateArchitecturePalette@Project`. It is the project working record for candidate-palette construction. The name does not introduce a new `U.*` kind, and the record does not carry selection, publication, evidence, assurance, or decision authority.

For a first pass, fill only the described holon, bounded context, synthesis question, synthesis structure map, live architecture-characteristic rows, candidate configurations, and palette stop condition. Add optional refs only when they change the next use of the palette:

```text
CandidateArchitecturePalette@Project:
  describedHolonRef:
  boundedContextRef:
  synthesisQuestion:
  architectureSynthesisFrameRef?:
  synthesisStructureMap:
    - structureKindRef:
      selectedStructureRef?:
      contributionToSynthesis:
      constraintOrAffordance:
      governingPatternRef:
      sourceReturnCondition?:
  architectureCharacteristicCriteriaSetRef?:
  architectureCharacteristicCriteriaRowRefs:
  qBundleRefs?:
  characteristicImprovementCycleRef?:
  architectureIdealityPressureRef?:
  scaleAmenabilityPolicyRef?:
  functionBearerFeasibilityRef?:
  candidateArchitectureConfigurations:
    - candidateId:
      candidateName:
      selectedStructureChanges:
        - structureKindRef:
          selectedStructureRef?:
          changeMade:
          governingPatternRef:
      affectedArchitectureCharacteristicRefs:
      affectedCriteriaRowRefs?:
      architectureCharacteristicEvalResultRefs?:
      qBundleRefs?:
      expectedArchitectureGain:
      knownArchitectureLoss:
      constraintFit:
      preservedStructure:
      lostOrHiddenStructure:
      sourceCueRefs?:
      sourceSideReferent?:
      sourceReturnCondition:
      nextUse:
  tradeoffFrontOrArchiveRef?:
  evolutionWindowRef:
  transformerTransformedCorrespondenceRef?:
  paletteStopCondition:
```


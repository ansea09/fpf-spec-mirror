---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__002_problem-frame.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:1 — Problem frame"
line_start: 61253
line_end: 61357
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
  - "C.32.MWA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
  - "U.Structure"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "selected-structure contribution rows"
  - "trade-off front"
---

### C.32:1 - Problem frame

Use this pattern when a practitioner has a C.30-grounded architecture question for one exact described holon and needs to synthesize several candidate architecture configurations across selected structures before comparison, archive or front-policy work, selected-set result declaration, actual publication, or decision. Keep any obtaining C.30 `ArchitectureRelation` occurrences, the selected `U.Structure` values they relate to the holon, and any candidate, required, desired, or expected structures named only in an `ArchitectureClaim` distinct throughout the synthesis.

Primary working reader: an architect or architecture-responsible practitioner preparing alternatives for one described holon before comparison, selection, selected-set result declaration, actual publication, local choice, or project decision.

Typical entry phrases:

```text
"The functional structure is clear, but module allocation and placement change the trade-off."
"One platform proposal improves reuse and worsens evidence or control burden."
"A search or workshop produced options; which selected structures and architecture characteristics do they change?"
"We need a candidate palette with structurally different architecture configurations before choosing one."
"The architecture of the team or tool that changes the target holon no longer fits the target architecture."
```

**First-minute use slice.** A regulated product-family team has a C.30-grounded architecture question for one exact field-device-family holon. The question names its current obtaining `ArchitectureRelation` occurrences and their selected structures separately from candidate or expected structures stated only in the current `ArchitectureClaim`. The work question is synthesis: how should required functions, constructive modules, field placement, control responsibility, and certification evidence be coordinated so maintainability, substitutability, latency, and evidence reuse stay acceptable? Using C.32, the practitioner first records the selected structures and what each contributes to the synthesis, then records three candidate configurations: one shared module grammar with tighter evidence scope, one product-family split with lower interface burden, and one bounded exception that keeps the existing module split but changes evidence responsibility and reopen trigger. The team now has candidate architecture configurations under declared characteristics, not one attractive platform proposal and not new obtaining architecture relations by candidate wording.

The primary `EntityOfConcern` is the candidate architecture palette for one C.30-grounded synthesis question. Its inputs are the described holon, any obtaining `ArchitectureRelation` occurrences and their selected `U.Structure` participants, and any candidate, required, desired, or expected structures stated only in an `ArchitectureClaim`.

The described holon may be a system, product family, organization-as-system, discipline, AI-agent setup, built asset, episteme, Work occurrence, or another admitted holon kind. Do not admit a source label as a holon. For example, *practice*, *culture*, *tradition*, *style*, *Method*, or *role* may refer to a Method, Method relation structure, relation among local system-role kinds, classification, assignment, Work structure, episteme, source-local meaning, or C.36 cultural-evolution relation. Recover the actual object and claim through its subject pattern; route unresolved claim-bearing *role* wording through `E.10.ROLE`.

ClaimScope and a bounded model-use structure qualify the named use; neither becomes the holon. Architecture pressure may concern Method-family structures, relations among local kinds, classifications, or assignments. Keep each as a selected structure or separate input for the named architecture use, not as a holon kind or function bearer by label. C.32 is not software-system architecture by default; software-system sources are one source family and one domain example.

What goes wrong if C.32 is missed: the team optimizes one visible structure, such as modules, placement, team responsibility, control relation, or evidence package, and then treats that local improvement as architecture synthesis. The competing structures, architecture characteristics, losses, and alternatives disappear before they can be compared.

What C.32 buys in practice: a practitioner can build a small set of candidate architecture configurations, each grounded in selected structure changes, architecture characteristics, known losses, and patterns for the next questions.

Ordinary working move: name the selected structures that really change, name the few architecture characteristics that make the trade-off real, then write two to five candidate configurations with gain, loss, preserved structure, hidden loss, and next receiving use.

Adoption test: after using C.32, another practitioner can see at least two structurally different candidate configurations, the selected-structure changes, the architecture characteristics under pressure, each gain and loss, the source-return condition, and the next receiving use.

Use C.32 only for candidate palette construction. Do not use it to ground the architecture claim, recover one structure, build characteristic criteria rows, design eval programs, handle architecture-influence correspondence, run archive or front-policy work, declare a selected-set result, publish it to an audience, choose locally, or decide the project architecture.

Use `C.32.MWA` instead when several structures of Methods, Work, subjects and their descriptions, capabilities and providers, and cultural change do not line up one-for-one and the needed result is one usable practice architecture. Keep C.32 for a palette of candidate configurations for one grounded architecture question; do not copy the C.32.MWA action sequence here.

Common exits by claim kind:

- `C.30` grounds the described holon, any obtaining `ArchitectureRelation`, its selected `U.Structure`, and any separate `ArchitectureClaim`; `C.30.ASV`, `A.6.F`, and `A.6.M` recover structural views, function wording, and module-interface relations.
- `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, `C.25`, `C.31`, `C.31.ASAP`, and `C.16` govern starter heads, project criteria rows, eval programs, Q-Bundles, modularity or scale-preference claims, and measurement.
- `C.32.MLAO`, `C.32.CONWAY`, `C.32.FAIL`, and `C.29` govern residual-reducing frames, architecture-influence and transformed-architecture correspondence, candidate repair, and mathematical-lens use.
- Use `A.19.CPM` for comparison, `A.19.SelectorMechanism` for set-returning selection, `C.18` and `C.19` for archive, front, and current-pool treatment, `G.5` for selected-set result declaration, `C.11` for local choice, and `C.32.PAD` for a project architecture decision. When audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability.
- `C.30.AD`, `E.17`, `E.24.PUB`, `A.10`, and `B.3` govern architecture-description, publication-face, evidence, and assurance claims.

The first useful output is `CandidateArchitecturePalette@Project`. It is the project working record for candidate-palette construction. The name does not introduce a new `U.*` kind, and the record does not carry selection, publication, evidence, assurance, or decision authority.

For a first pass, fill only the described holon, synthesis question, intended palette use, current architecture relations and selected structures that change the question, selected-structure contribution rows, live architecture-characteristic rows, candidate configurations, and palette stop condition. Add ClaimScope or a bounded model-use structure only when it changes synthesis; add other optional refs only when they change the next use of the palette:

```text
CandidateArchitecturePalette@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureSynthesisProjectUseRelationRef?: U.RelationRef resolving to the exact synthesis-use or work-use relation
  architectureQuestionCardRef?: C.30 ArchitectureQuestionCard@Project ref when that exact card is the intake
  describedHolonRef:
  architectureClaimRef?: C.30 ArchitectureClaimRef when a durable actual, candidate, required, desired, or expected claim is current
  currentArchitectureRelationRefs[]?: exact obtaining C.30 ArchitectureRelation refs only
  currentSelectedStructureRefs[]?: the U.Structure participants of those obtaining relations
  synthesisQuestion:
  intendedPaletteUse:
  claimScopeRef?: U.ClaimScope
  boundedModelUseStructureRef?: A.1.1 BoundedModelUseStructure, only when its organization changes synthesis
  architectureSynthesisFrameRef?:
  selectedStructureContributionRows:
    - structureKindRef:
      selectedStructureRef?:
      contributionToSynthesis:
      constraintOrAffordance:
      relationFunctionClaimRef:
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
          relationFunctionClaimRef:
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
  architectureInfluenceCorrespondenceRef?: C.32.CONWAY frame or exact pair-row ref
  paletteStopCondition:
```

Across C.32, `@Project` is a compatibility and retrieval cue, not a project kind or relation assertion. `CandidateArchitecturePalette@Project`, `ArchitectureSynthesisFrame@Project`, and `ArchitectureCharacteristicImprovementLoop@Project` establish no composite project work, context, authority, viewpoint, or parthood by name. When one of these records is genuinely local to one actual project, identify the exact composite `U.Work` and the direct relation by which synthesis framing, palette construction, or improvement feedback concerns that work. Otherwise no project-work relation is implied. A cited `ArchitectureQuestionCard@Project` transfers neither project locality nor architecture truth: each affirmative `currentArchitectureRelationRef` must already resolve to one obtaining C.30 occurrence, while candidate, required, desired, or expected structure remains claim content until the C.30 predicate is independently satisfied.


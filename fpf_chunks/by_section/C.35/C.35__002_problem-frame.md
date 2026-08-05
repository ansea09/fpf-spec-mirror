---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Structural Synthesis and Discovery Adequacy"
section_id: "C.35:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__002_problem-frame.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "C.35 — Structural Synthesis and Discovery Adequacy"
  - "C.35:1 — Problem frame"
line_start: 67800
line_end: 67864
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.22"
  - "A.3.4"
  - "A.6.M"
  - "A.6.RCD"
  - "C.16"
  - "C.18"
  - "C.19"
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
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.36"
  - "E.18"
  - "F.6"
  - "G.5"
keywords:
  - "DSM"
  - "LLM"
  - "NAS"
  - "candidate admission"
  - "described structure"
  - "generated carrier"
  - "produced carrier"
  - "source return"
  - "structural discovery"
  - "structural synthesis"
---

### C.35:1 - Problem frame

Use this pattern when a generated, searched, clustered, queried, learned, transformed, simulated, or discovered output that carries or describes selected structure may seed or inform architecturing, and the practitioner must decide whether it can enter architecture work before or around `C.32` candidate admission.

Primary working reader: an architect, architecture researcher, AI-assisted architecture worker, model-based engineer, or reviewer receiving an output that carries or describes selected structure from DSM and MDM modularization, MBSE query and view generation, graph grammar, model transformation, NAS, DSE, QD, OEE, and NQD search, LLM-assisted architecture design, code-agent mapping, simulation, benchmark trace, or source discovery.

Typical entry phrases:

```text
"The LLM generated an architecture diagram; can it seed synthesis?"
"The DSM clustering suggests modules; is this a candidate architecture yet?"
"The MBSE query produced a view; what selected structure does it describe?"
"NAS found a Pareto point; what architecture claim can use it?"
"A graph grammar transformed the model; what preservation and bearer boundary must be checked?"
```

The first useful output is `StructuralSynthesisDiscoveryAdequacyNote@Project`:

```text
StructuralSynthesisDiscoveryAdequacyNote@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  structuralSynthesisAdequacyNoteProjectUseRelationRef?: U.RelationRef governed by the exact architecture-use or work-use pattern
  groundedArchitectureQuestionRef:
  selectedSourceStructureRefs:
  generationOrDiscoveryMethodRef:
  generationOrDiscoveryWorkOccurrenceRef?: U.EntityRef constrained to one independently admitted U.Work
  generationOrDiscoveryWorkAttributionRef?: U.RelationRef constrained to the exact F.6 performedUnderAssignment occurrence when attribution is current
  searchOrQuerySpaceRef?:
  constraintRefs:
  producedCarrierOrDescriptionRefs:
  describedStructureRefs?:
  synthesisStructureMapOrTransformationTrace?:
  actualTransformationRefs?:
  workToTransformationOrProductionClaimRefs?:
  preservedStructure:
  lostStructure:
  constraintGovernedUnfoldingStructureRef?:
  sourceLabelRecoveryRef?:
  observationAndUncertaintyRefs?:
  validationOrComparisonRefs?:
  selectedCandidateStructureRefs?:
  candidateAdmissionCondition:
  bearerOrRealizationBoundary:
  realizedHolonStructureRefs?:
  measurementOrEvalReturnRefs?:
  bearerFeasibilityQuestionRef?:
  receivingGoverningPatternRef:
  receivingClaimKind:
  admissibleUse:
  nonAdmissibleUse:
  carrierAdmissionReturnCondition:
```

Here `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the note is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work` and `structuralSynthesisAdequacyNoteProjectUseRelationRef` identifies the direct relation by which that exact project Work uses the note. The suffix or either reference alone establishes no project locality. The note and the composite project Work remain distinct.

When generation or discovery is claimed as performed work, `generationOrDiscoveryWorkOccurrenceRef` identifies one independently admitted dated `U.Work`; its performer System, exact obtaining `U.RoleAssignment`, F.6 `performedUnderAssignment` attribution when current, enacted Method, extent, and containing System remain under A.15.1, A.2.1, and F.6. The Method, Work, note, and produced carrier or description are different objects. `actualTransformationRefs` may cite only independently identified A.3.4 bounded changes; a method label, transformation trace, graph edge, or before-and-after picture does not make a transformation actual. Any positive link from the Work to an actual transformation or produced entity must cite an exact direct predicate, an admitted A.6.RCD local claim, or the selected A.15.PROD branch in `workToTransformationOrProductionClaimRefs`; otherwise keep the objects separate and return the exact `missing-governor`. Every structure reference likewise resolves to an independently selected A.22 `U.Structure`; a carrier, graph, cluster, or description does not supply its four identity discriminators.

Adoption test: after using C.35, another practitioner can tell what was produced, which structure it describes, what it preserves and loses, what must happen before C.32 admission or realization claims, and which governing pattern receives the next claim.

What C.35 buys in practice: the practitioner can accept useful generated or discovered output without handing it authority. The pattern lets a search output, cluster, query result, model transformation, or LLM proposal become candidate input for architecturing only after carrier, described structure, admission condition, and receiving governing pattern are named.

Ordinary working move: name the produced carrier first, then the described structure, then the admission condition. If those three cannot be separated, do not let the output enter C.32 or a decision.

Not this pattern when the current question is how to search, choose, measure, decide, authorize, publish, govern a reusable generator, govern a cultural-evolution case, or run the work itself. Use the governing pattern for that question first, including `C.36` for the cultural-evolution relation bundle. Return to C.35 only when a produced carrier must be admitted or rejected before another architecture pattern relies on it.


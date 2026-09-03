---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Structural Synthesis and Discovery Adequacy"
section_id: "C.35:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__002_problem-frame.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "C.35 — Structural Synthesis and Discovery Adequacy"
  - "C.35:1 — Problem frame"
line_start: 67320
line_end: 67422
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

Use this pattern when a generated, searched, clustered, queried, learned, transformed, simulated, or discovered result may seed or inform architecturing, and the practitioner must decide what that exact result is and whether it can enter architecture work before or around `C.32` candidate admission.

Primary working reader: an architect, architecture researcher, AI-assisted architecture worker, model-based engineer, or reviewer receiving an exact result from DSM and MDM modularization, MBSE query and view generation, graph grammar, model transformation, NAS, DSE, QD, OEE, and NQD search, LLM-assisted architecture design, code-agent mapping, simulation, benchmark trace, or source discovery.

Typical entry phrases:

```text
"The LLM generated an architecture diagram; can it seed synthesis?"
"The DSM clustering suggests modules; is this a candidate architecture yet?"
"The MBSE query produced a view; does it describe an obtaining structure or only propose one?"
"NAS found a Pareto point; what architecture claim can use it?"
"A graph grammar transformed the model; what preservation and bearer boundary must be checked?"
```

**Primary working object.** The exact generated or discovered result on which the next architecture use would rely.

**First useful move.** Recover that result by its truthful kind, then say what organization it concerns, what the intended next use still requires, and what must not be inferred. If the organization is only proposed, keep it modal in an exact C.30 `ArchitectureClaim`. Treat a graph, diagram, matrix, encoding, or model as a separate C.29 representation when representation operations matter. Publication detail enters only when availability or form changes the use.

**Normal first result.** One sentence containing the same four facts is conforming. When a visible note is clearer, write only:

```text
Result: <exact result relied on>
Organization: <what already obtains or is only proposed>
Next-use condition: <one condition still required>
Limit and return: <forbidden overread and where to return>
```

Stop there when another practitioner can make the intended next move safely. Only when result identity, branch evidence, or a receiving claim must be reidentified independently, extend those four facts into the optional `StructuralSynthesisDiscoveryAdequacyNote@Project` C.2.1 episteme:
~~~text
StructuralSynthesisDiscoveryAdequacyNote@Project:
  resultRef:
  organizationConcern:
  nextArchitectureUseAndCondition:
  forbiddenOverreadOrReturn:
  resultKindAndIdentityRule?:
  admissibleUse?:
  unresolvedConditions?:
  representationRef?:
  representedObjectRef?:
  publicationFormRef?:
  publicationOccurrenceRef?:
  presentationCarrierRef?:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  structuralSynthesisAdequacyNoteProjectUseRelationRef?: U.RelationRef under a named architecture-use or work-use predicate when that relation identity is material
  groundedArchitectureQuestionRef?:
  resultBranch?: transformation | discovery | generative-proposal
  generationOrDiscoveryMethodRef?:
  generationOrDiscoveryWorkRef?: U.EntityRef constrained to U.Work
  generationOrDiscoveryWorkAttributionRefs?: refs to obtaining F.6 performedUnderAssignment relations only when the note or receiving use expressly represents attribution
  workToTransformationOrProductionClaimRefs?:
  transformationBranch?:
    exactSourceObjectRefs:
    exactResultObjectRefs:
    transformationTraceRef:
    preservedStructure:
    lostStructure:
    actualTransformationRefs?:
  discoveryBranch?:
    observationOrExtractionBasis:
    observedInferredUnknownStatus:
    coveredRegion:
    unexploredRegion:
    uncertainty:
    validation:
  generativeProposalBranch?:
    constraintRefs:
    proposedOrganizationContent:
    knownOmissions:
    validationNeeds:
    declaredBaselineComparison?:
      exactBaselineObjectRefs:
      preservedStructure:
      lostStructure:
  obtainingConstraintGovernedUnfoldingStructureRef?: exact A.22.CGUS reference only
  sourceLabelRecoveryRef?:
  obtainingStructureRefs?: exact A.22 U.Structure references only
  modalArchitectureClaimRef?: C.30 ArchitectureClaimRef or C.2.1 ClaimAddress to its exact claim
  candidateAdmissionCondition?:
  bearerOrRealizationBoundary?:
  obtainingRealizedHolonStructureRefs?: exact positive A.22 references only
  measurementOrEvalReturnRefs?:
  bearerFeasibilityQuestionRef?:
  nextClaimOrRuleRef?:
  receivingClaimKind?:
~~~
The note's first four fields reproduce the readable minimum; every later field is conditional on an actual dependency of the selected branch or receiving use. Its EntityOfConcern is the exact result designated by `resultRef`, not the reference value, representation, publication occurrence, form, or carrier used to reach it. When publication detail is relied on, `publicationFormRef`, `publicationOccurrenceRef`, and `presentationCarrierRef` each name their truthful object; omit every one that the receiving use does not need. Its ClaimGraph states the organization concerned, intended next use and condition, forbidden overread or return, and any additional admissible use or unresolved condition that the receiving use needs. Do not open or fill the dossier merely to prove completeness.

Here `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the note is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work` and `structuralSynthesisAdequacyNoteProjectUseRelationRef` identifies the direct relation by which that exact project Work uses the note. The suffix or either reference alone establishes no project locality. The admission-note episteme, its exact result, and the composite project Work remain distinct.

When the admission claim relies on performed generation or discovery, `generationOrDiscoveryWorkRef` is mandatory and names an independently admitted `U.Work` occurrence whose exact actual performers have A.13 cores and which A.15.1 admits independently; otherwise omit the Method and Work fields. `generationOrDiscoveryWorkAttributionRefs` are optional and appear only when the note or receiving use expressly represents precise assignment-bound attribution through the same obtaining A.13 assignment. Missing or failed F.6 leaves the Work ref intact. The Method, Work, attribution, admission-note episteme, generated result, representation, and any publication occurrence or carrier remain different objects.

`actualTransformationRefs` may cite only independently identified A.3.4 bounded changes; a Method label, transformation trace, graph edge, or before-and-after picture does not make a transformation actual. Any positive link from the Work to an actual transformation or produced entity must cite its declared predicate, an admitted A.6.RCD local claim, or the selected A.15.PROD branch in `workToTransformationOrProductionClaimRefs`; otherwise keep the objects separate and return `missing-governor`. An entry in `obtainingStructureRefs` resolves to an independently selected A.22 `U.Structure` with independently identified constituents, exact obtaining relation occurrences, applied constraints, and one named use frame. Whenever the result or a branch proposes an organization, `modalArchitectureClaimRef` is mandatory and identifies the exact C.30 `ArchitectureClaim` or ClaimAddress; its proposed constituents and relations stay modal until the A.22 basis actually exists. A result, representation, publication item, graph, cluster, description, or plausible modal wording supplies none of those four discriminators.

**Adoption test.** After using C.35, another practitioner can state the four-line minimum or an equivalent sentence: the exact result, the organization that already obtains or is only proposed, the one condition required for the next use, and the forbidden overread or return. That practitioner can also distinguish claim content, an obtaining A.22 structure, a C.29 representation, and a publication-side object. Additional identity, branch, Work, bearer, publication, evaluation, or next-claim detail appears only when the receiving use relies on it.

**What C.35 buys in practice.** The practitioner can keep a useful generated or discovered result without handing it architecture authority. Architecture use attaches to the exact result; changing a rendering or file does not silently change the admitted claim, and admitting a carrier does not silently admit claim content.

**Ordinary working move.** Write the one sentence or four lines first. Recover whether the organization already obtains or is only proposed, and stop if the next move and return are clear. Use A.22 only when its four identity discriminators resolve; otherwise keep the proposal modal in its exact architecture claim. Add a C.29 representation, branch basis, Method, Work, bearer, publication, evaluation, or exact next-claim reference only when the intended use depends on it.

**Not this pattern when.** If the current question is how to search, choose, measure, decide, authorize, publish, govern a reusable generator, govern a cultural-evolution case, or run the work itself, use the pattern that defines or decides that question first, including `C.36` for the cultural-evolution relation bundle. Use C.35 only when an exact generated or discovered result must be admitted or rejected before another architecture claim relies on it.


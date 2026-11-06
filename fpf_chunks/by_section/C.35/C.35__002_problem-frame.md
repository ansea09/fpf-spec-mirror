---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Assess Generated or Discovered Results for Architecture Use"
section_id: "C.35:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__002_problem-frame.md"
commit_sha: "4e277189a17b8f9bd3dcdda5df58623d9085ede9"
heading_path:
  - "C.35 — Assess Generated or Discovered Results for Architecture Use"
  - "C.35:1 — Problem frame"
line_start: 81077
line_end: 81179
dependencies:
  - "A.13"
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
  - "candidate input"
  - "discovered result"
  - "generated result"
  - "modal architecture proposal"
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
"The MBSE query produced a view; which organization is observed, proposed, or still unestablished?"
"NAS found a Pareto point; what architecture claim can use it?"
"A graph grammar transformed the model; what preservation and bearer boundary must be checked?"
```

**Primary working object.** The exact generated or discovered result on which the next architecture use would rely.

**First useful move.** Identify the result and the organization it concerns, then state its supported next use and any condition or limitation that affects reliance. Distinguish supported, refuted and unestablished claims about existing organization from proposals for a possible organization. Keep a proposal modal; add exact C.30 claim identity when the receiving use needs independent reidentification. Keep a representation distinct from its represented object when correspondence or representation operations matter. Use `C.30.AD` or `C.30.ASV` for architecture descriptions or views, and `C.29` for a remaining mathematical-representation choice, transfer, or reliance question. Publication detail enters only when availability or form changes the use.

**Normal first result.** A short sentence can suffice; reuse an adequate existing account. When separate lines help, use:

```text
Result: <exact result relied on>
Organization: <organization concerned; whether the claim about it is established, refuted or unestablished, or presents a proposal>
Next use: <supported use and any unresolved condition>
Limit and return, if needed: <material limitation and how to resolve it>
```

Stop there when another practitioner can make the intended next move safely. Only when result identity, branch evidence, or a receiving claim must be reidentified independently, extend those four facts into the optional `StructuralSynthesisDiscoveryAdequacyNote@Project` C.2.1 episteme:
~~~text
StructuralSynthesisDiscoveryAdequacyNote@Project:
  resultRef:
  organizationConcern:
  nextArchitectureUseAndCondition:
  forbiddenOverreadOrReturn?:
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
The note retains the result, organization, next use and any material limit or return; its fields are included when the selected branch or receiving use needs them. Its EntityOfConcern is the exact result designated by `resultRef`, not the reference value, representation, publication occurrence, form, or carrier used to reach it. When publication detail is relied on, `publicationFormRef`, `publicationOccurrenceRef`, and `presentationCarrierRef` each name their truthful object; omit every one that the receiving use does not need. Its ClaimGraph states the organization concerned, supported next use, and any material limitation or unresolved condition. A plausible mistaken inference is corrected when that changes reliance. Do not open or fill the dossier merely to prove completeness.

Here `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the note is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work` and `structuralSynthesisAdequacyNoteProjectUseRelationRef` identifies the direct relation by which that exact project Work uses the note. The suffix or either reference alone establishes no project locality. The admission-note episteme, its exact result, and the composite project Work remain distinct.

When reliance depends on how the result was actually generated or discovered, retain the actual operation and the material source, input, performer and condition facts needed to establish that history and its bearing on the result. For an express claim about a particular `U.Work`, `generationOrDiscoveryWorkRef` names that independently admitted occurrence: its actual performers have A.13 cores and A.15.1 supplies Work admission. Include the Method reference when the receiving claim depends on that Method. `generationOrDiscoveryWorkAttributionRefs` appear only for precise assignment-bound F.6 attribution. Missing or failed F.6 attribution alone leaves independently admitted Work intact; recheck an admission premise questioned by the same finding and any conclusion depending on it. The operation, Work, attribution, admission-note episteme, result, representation and publication objects retain their distinct identities.

`actualTransformationRefs` cite independently identified A.3.4 bounded changes. A positive link from Work to an actual transformation or produced entity uses the applicable declared predicate and its supporting facts, including A.15.PROD when its branch is selected. Return `missing-governor` under A.6.RCD when no applicable predicate governs the link; leave missing case facts unresolved and reject a link contradicted by them. An entry in `obtainingStructureRefs` resolves to an A.22 `U.Structure` with independently identified constituents, obtaining relation occurrences, applied constraints and a named use frame. An incomplete basis for a claim about existing organization leaves that claim unestablished. A proposal remains modal until its proposed organization obtains; supply `modalArchitectureClaimRef` when that claim must be independently reidentified. A result, representation, publication item, graph, cluster or description supplies only the structural facts it actually establishes.

**Adoption test.** After using C.35, another practitioner can state the four-line minimum or an equivalent sentence: the exact result, the organization concerned and whether the claim about it is established, refuted or unestablished, or presents a proposal, the supported next use and any unresolved condition, material limitation or required return. That practitioner can also distinguish claim content, an obtaining A.22 structure, its representation, and a publication-side object when those distinctions affect use. Additional identity, branch, Work, bearer, publication, evaluation, or next-claim detail appears only when the receiving use relies on it.

**What C.35 buys in practice.** The practitioner can keep a useful generated or discovered result without handing it architecture authority. Architecture use attaches to the exact result; changing a rendering or file does not silently change the admitted claim, and admitting a carrier does not silently admit claim content.

**Ordinary working move.** Explain the organization concerned, its actual or proposed status, what remains unestablished, and the use the result supports. Stop when the next move and any material limit or return are clear. Claim an obtaining A.22 structure only when its four identity discriminators resolve. Preserve an unestablished claim about existing organization as unresolved and a proposal as modal. Add exact claim identity, representation, branch, Method, Work, bearer, publication or evaluation detail when the intended use depends on it; use C.29 for an unresolved mathematical-representation choice, transfer, or reliance question.

**Not this pattern when.** If the current question is how to search, choose, measure, decide, authorize, publish, govern a reusable generator, govern a cultural-evolution case, or run the work itself, use the pattern that defines or decides that question first, including `C.36` for the cultural-evolution relation bundle. Use C.35 only when an exact generated or discovered result must be admitted or rejected before another architecture claim relies on it.


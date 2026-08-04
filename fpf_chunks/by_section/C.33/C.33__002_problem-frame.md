---
chunk_kind: "child"
pattern_id: "C.33"
pattern_title: "Structural Information Adequacy for Architecture Capture and Missing-Structure Return"
section_id: "C.33:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.33/C.33__002_problem-frame.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "C.33 — Structural Information Adequacy for Architecture Capture and Missing-Structure Return"
  - "C.33:1 — Problem frame"
line_start: 67389
line_end: 67448
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "A.6.M"
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
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.18"
  - "F.15"
  - "F.9"
  - "G.5"
keywords:
  - "captured selected structure"
  - "carrier"
  - "lost structure"
  - "missing structure"
  - "missing-structure return"
  - "observer boundary"
  - "selected structure"
  - "structural information adequacy"
---

### C.33:1 - Problem frame

Use this pattern when an architect has a description, view, decision record, ADR-like projection, eval report, method handoff, generated relation graph, source model, or realized holon observation that carries or describes selected architecture-relevant structure and needs to know which selected structure is actually recoverable for the next architecture use.

Use the same pattern when the carrier is a narrative rendering or principle-framework publication for architecture work: the carrier may preserve a problem-to-structure ordering, problem-situation architecture, solution-move architecture, candidate trade-off, decision rationale, or missing-structure cue, but it may also hide selected structures that the next architecture use still needs. In architecture-mediated rendering, inspect the chain from carrier to architecture description or view, then to architecture as selected structures in context, then to wider selected source structures, because each relation may have captured and lost different structure.

Primary working reader: an architect, architecture reviewer, method steward, or AI-assisted architecture worker who must use one carrier or observation without letting it stand for the whole architecture, the project decision, evidence sufficiency, or realized structure.

Typical entry phrases:

```text
"This view is useful, but what structure does it actually capture?"
"The ADR says what was decided; which selected structures and hidden losses does it leave behind?"
"The code-agent map found dependencies and invariants; can we rely on them for architecture work?"
"The neural-network architecture review names attention, cache, router, and pruning; what FPF structures are recoverable?"
"The operation observation shows the real system diverged; what actual structure is visible enough to return to synthesis?"
```

The first useful output is `StructuralInformationAdequacyNote@Context`. It is a project-side adequacy note for one declared architecture use. It is not a C.16 characteristic, not a measurement, not an evidence record, not an assurance result, not a project decision, and not an architecture description by itself.

For the first pass, fill only the fields that prevent the next wrong use:

```text
StructuralInformationAdequacyNote@Context:
  architectureClaimRef?:
  describedHolonRef:
  boundedContextRef:
  selectedStructureRefs:
  selectedSourceStructureRefs?:
  sourceDescriptionOrViewRefs?:
  narrativeRenderingRefs?:
  constraintGovernedUnfoldingStructureRef?:
  decisionOrRecordCarrierRefs?:
  realizedStructureObservationRefs?:
  capturedSelectedStructure:
  expectedButUncapturedStructureHypothesis?:
  lostOrHiddenStructure:
  compressionOrAbstractionMode?:
  observerOrBudgetBoundary?:
  relationObservationClass?:
  typedRelationSemantics?:
  unexploredRegionRefs?:
  sourceLabelRecoveryRef?:
  mathematicalLensUseOutputRef?:
  measurementOrEvalRefs?:
  admissibleUse:
  nonAdmissibleUse:
  missingStructureReturnCondition:
  receivingGoverningPatternRef:
  receivingClaimKind:
```

Adoption test: after using C.33, another practitioner can tell what selected structure is captured, what structure is expected but not captured, what is lost or hidden, what use is admissible, which non-admissible uses are blocked, and which governing pattern receives the next claim.

What C.33 buys in practice: the practitioner can use a partial carrier without pretending it is complete. The pattern turns "this diagram, ADR, graph, report, or observation is useful" into a reviewable statement about captured structure, missing structure, missing-structure return, and receiving governing pattern.

Ordinary working move: underline the carrier sentence, diagram, graph edge set, or observation being relied on; write what selected structure it captures; write what it leaves out; then name the use that remains admissible.

Not this pattern when the current question asks whether the architecture, record, lens, reading, decision, authorization, or publication is admissible. Use the governing pattern for that question first. Return to C.33 only when that governing pattern relies on a carrier whose captured structural content and missing structural content must be made explicit.


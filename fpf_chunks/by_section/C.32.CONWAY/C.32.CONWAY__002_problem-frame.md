---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Transformer and Transformed Architecture Correspondence"
section_id: "C.32.CONWAY:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__002_problem-frame.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.32.CONWAY — Transformer and Transformed Architecture Correspondence"
  - "C.32.CONWAY:1 — Problem frame"
line_start: 64102
line_end: 64193
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.3.4"
  - "A.3.4.P"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.29"
  - "C.30"
  - "C.32"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.18"
  - "G.5"
keywords:
  - "Conway correspondence"
  - "changing relation"
  - "coordination cost"
  - "inverse Conway maneuver"
  - "selected-structure correspondence"
  - "transformed holon"
  - "transformer holon"
---

### C.32.CONWAY:1 - Problem frame

Use this pattern when a practitioner is synthesizing an architecture for a holon that changes another holon, and the architecture of the changing holon constrains, enables, or degrades the architecture of the holon being changed.

Primary working reader: an architect or architecture-responsible practitioner who must co-synthesize selected structures of the changing holon and the changed holon under one changing relation.

Typical entry phrases:

```text
"The product architecture we want cannot be built by the existing manufacturing line."
"The service boundaries we chose still require every team to coordinate every release."
"The method family changes documents, but its review roles do not match the evidence structure it must create."
"The AI-agent toolchain changes project work products, but its control and evidence boundaries do not match the transformed work-product architecture."
"We need an inverse Conway candidate alternative, not another diagram of the desired transformed-holon architecture."
```

**First-minute use slice.** A product-family team wants independently replaceable field modules. The existing manufacturing and certification organization is built around one batch line and one shared evidence responsibility. Using C.32.CONWAY, the practitioner names the two holons in the changing relation: the manufacturing and certification holon as transformer, and the product family as transformed holon. The C.32 candidate palette now includes three architecture configurations: change the manufacturing cell and evidence roles to match module variation, change the product-family module split to fit the fixed line, or keep a bounded mismatch with a clear exception cost and reopen trigger.

The primary `EntityOfConcern` is a local correspondence frame inside architecture candidate synthesis. The frame relates selected structures of the changing holon and selected structures of the changed holon under one changing relation. Organization-design decisions, organization-design authority relations, module-interface repair, structural-equivalence claims, and architecture decisions belong to their governing patterns when those claims are being made; C.32.CONWAY may use them only as constraints, costs, or candidate-change inputs.

What goes wrong if C.32.CONWAY is missed: the team either treats the existing organization, toolchain, manufacturing line, method family, or communication structure as if it already settled the transformed-holon architecture, or it draws a desired transformed-holon architecture that the changing holon cannot actually produce, test, maintain, evolve, or certify.

What C.32.CONWAY buys in practice: the practitioner can turn Conway pressure and inverse Conway maneuvers into candidate alternatives inside the C.32 palette. An alternative may change the transformer side, the transformed side, both sides, or a bounded mismatch; each variant names gains, losses, affected architecture characteristics, and the receiving pattern.

Ordinary working move: name the changing holon, the changed holon, the changing relation, and the selected structures on both sides; then prepare alternatives that change the transformer side, the transformed side, both sides, or keep a bounded mismatch.

Adoption test: after using C.32.CONWAY, the recorded candidate palette states whether each alternative changes the transformer side, the transformed side, both sides, or a bounded mismatch, and what gain, loss, affected characteristic, and stop condition follow.

Not this pattern when the current work is only module-interface repair, bounded-transformation identification, work or role assignment without architecture synthesis, mathematical structural similarity, local choice, or project architecture decision.

Common exits by claim kind:

- `A.6.M` for module-interface repair.
- `A.3.4` or `A.3.4.P` for bounded transformation.
- The A.15 family, `A.2`, or the direct role pattern for work and responsibility.
- `C.29` and the project-selected structural-equivalence pattern for structural similarity.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `G.5` for selected-set publication; `C.18` and `C.19` for archive, front, or pool-treatment policy.
- `C.11` for fixed local choice and `C.32.PAD` for project decision.

The first useful output is `TransformerTransformedArchitectureCorrespondenceFrame@Project`. The frame is the project working record for the correspondence question. It records candidate co-synthesis pressure; it does not make a C.29 structural-equivalence claim, organization-design decision, or new correspondence ontology:

For a first pass, fill only the bounded context, synthesis question, changing relation, transformer holon, transformed holon, the selected-structure pair that changes the candidate frame, affected architecture characteristics, candidate configurations, and next governing pattern. Add full correspondence claims, C.29 refs, detailed source-return fields, and extra structure pairs only when a receiving comparison, structural-similarity, publication, choice, or decision claim needs them.

```text
TransformerTransformedArchitectureCorrespondenceFrame@Project:
  boundedContextRef:
  synthesisQuestion:
  changingRelationRef:
  transformerHolonRef:
  transformedHolonRef:
  transformerArchitectureRef?:
  transformedArchitectureRef?:
  transformerSelectedStructureMap:
    - structureKindRef:
      selectedStructureRef?:
      contributionToChangingRelation:
      architectureCharacteristicPressure:
      governingPatternRef:
      sourceReturnCondition?:
  transformedSelectedStructureMap:
    - structureKindRef:
      selectedStructureRef?:
      requiredArchitectureRole:
      architectureCharacteristicPressure:
      governingPatternRef:
      sourceReturnCondition?:
  correspondenceClaims:
    - correspondenceId:
      transformerStructureRef:
      transformedStructureRef:
      correspondenceUse:
      pressureDirection:
      affectedArchitectureCharacteristicRefs:
      expectedArchitectureGain:
      knownArchitectureLoss:
      preservedStructure:
      lostOrHiddenStructure:
      receivingPatternRef:
      sourceReturnCondition:
  candidateArchitectureConfigurations:
    - candidateRef:
      transformerSideChange:
      transformedSideChange:
      coordinationChange:
      expectedArchitectureGain:
      knownArchitectureLoss:
      stopOrEscalationCondition:
  c29LensOrStructuralEquivalenceRef?:
  nextGoverningPatternRef:
```


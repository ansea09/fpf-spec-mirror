---
chunk_kind: "child"
pattern_id: "B.2.3"
pattern_title: "Meta-Holon Transition With Episteme Result"
section_id: "B.2.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.3/B.2.3__006_solution.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "B.2.3 — Meta-Holon Transition With Episteme Result"
  - "B.2.3:4 — Solution"
line_start: 33696
line_end: 33769
dependencies:
  - "A.1"
  - "A.10"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CSC"
  - "A.6.4"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "B.3.5"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.29"
  - "E.17"
  - "E.24.UK"
  - "F.18"
  - "F.19"
  - "U.EpistemeSlotRelation"
keywords:
---

### B.2.3:4 - Solution

Use B.2.3 as the episteme-result specialization of B.2.

#### B.2.3:4.1 - Episteme-Result MHT Slice

When `mhtResultEpistemeRef` is selected, use:

```text
EpistemeResultMHTSlice@Context:
  existingWholeRef: U.Holon
  mhtResultEpistemeRef: U.Episteme
  boundedContextRef:
  selectedTriggerProfileRef: MHTTriggerProfile@Context
  existingWholeExplanationCheckRef: ExistingWholeExplanationCheck@Context
  epistemeKindAdmissionRef: C.2.1
  epistemeSlotRelationRef: U.EpistemeSlotRelation
  entityOfConcernSlotRef:
  groundingHolonSlotRef:
  claimGraphSlotRef:
  referenceSchemeSlotRef:
  viewpointSlotRef?
  viewSlotRef?
  publicationOrSourceUseRefs?
  constituentEpistemeRefs:
  synthesisWorkRefs?
  evidenceOrAssuranceRefs:
  mathematicalLensUseRefs?
  blockedOverreads:
```

This slice is not a U-kind and not a second episteme ontology. It is the B.2 record slice that says the MHT result is an episteme and names the C.2.1 relation that governs it.

#### B.2.3:4.2 - Episteme Slot Re-Basing

For the result episteme, re-base at least these C.2.1 slots when current:

- `EntityOfConcernSlot`: what the result episteme is about;
- `GroundingHolonSlot`: where the result claim is grounded or tested;
- `ClaimGraphSlot`: what the result episteme says as a claim structure;
- `ReferenceSchemeSlot`: how claims are read as about their entities;
- `ViewpointSlot` and `ViewSlot`: when the result episteme has viewpoint-governed views;
- publication, source-use, and representation relations when the result episteme is published, cited, carried, or represented.

Do not infer these slots from the existence of a publication set. Fill them as episteme slots.

#### B.2.3:4.3 - Episteme Trigger Interpretation

Interpret `MHTTriggerProfile@Context` for epistemes without giving agency to epistemes:

| Trigger family in `MHTTriggerProfile@Context` | Episteme-result reading | Direct owner kept visible |
| --- | --- | --- |
| Delimitation change | The knowledge body now has a stable EntityOfConcern, scope, reference scheme, and claim scope. | `C.2.1`, `A.7`, source-use owners |
| Objective or evaluation change | The result episteme answers or evaluates a question that the collection did not answer as one claim-bearing whole. | `C.2.1`, `C.16`, `E.21` or relevant evaluation owner |
| Supervision or coordination change | Principles, axioms, invariants, reference schemes, or claim-graph constraints organize how constituent claims are interpreted. | `C.2.1`, `A.6.0`, `A.6.1`, `C.29` when formal lens is current |
| Capability or closure evidence | The result episteme enables a new explanatory, predictive, specification, or coordination use. | `C.2.1`, `C.16`, `A.10`, use-specific owner |
| Agency threshold | Usually not applicable to the episteme itself; if agency is claimed, recover the acting system in role. | `A.12`, `A.2.1`, `A.13`, `A.19`, `C.16` |
| Temporal consolidation | A field, standard, or theory becomes one current knowledge body after phase consolidation or source-currentness change. | `C.27`, `E.17`, source-use owners |
| Context reframe | New terms, reference schemes, or EntityOfConcern mapping reframe the knowledge body. | `C.2.1`, `A.6.3`, `A.6.4`, `F.18` |

B.2.3 uses these rows as evidence to inspect. B.2 decides whether whole reidentification is admitted.

#### B.2.3:4.4 - Blocked Readings

Do not use B.2.3 as:

- a name for generic emergence;
- an authority claim for a publication;
- an agentive claim about a theory, standard, or doctrine;
- an effect-free episteme morphism, view, retargeting, or coarsening;
- a second episteme ontic beside C.2.1;
- a shortcut from source synthesis to high trust;
- a replacement for source-use, evidence, assurance, or publication patterns.


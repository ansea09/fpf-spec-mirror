---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Unfolding"
section_id: "C.32.P2S:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__005_solution.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Unfolding"
  - "C.32.P2S:4 — Solution"
line_start: 60194
line_end: 60278
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22.CGUS"
  - "A.3.4"
  - "B.2"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.2"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.18"
  - "E.18.3"
  - "E.23"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
keywords:
  - "ArchitectureUnfoldingStructureUse@Project"
  - "ProblemToStructureArchitecturingFlowCard@Project"
  - "actual-structure feedback"
  - "candidate structures"
  - "expected structures"
  - "governing-pattern-specific return"
  - "problem-to-structure architecturing unfolding"
  - "selected structures"
  - "structural uncertainty"
---

### C.32.P2S:4 - Solution

Create or update one `ProblemToStructureArchitecturingFlowCard@Project` and move through the smallest useful spine below. Stop at the first pattern that fully governs the current claim; continue the P2S card only while the connected architecture flow remains the current object needing review.

Use the analogy with `E.18.1` P2W narrowly. P2W carries an accepted problem-side record or accepted `ProblemCard@Context` plus the carried distinction into a next governed FPF use. C.32.P2S carries architecture-relevant pressure and structural uncertainty into candidate structures, selected structures, project architecture decision, realization work, actual-structure feedback, and governing-pattern-specific next actions. The analogy ends when the current claim is method, work, telemetry, publication, or improvement-loop governance; then use the receiving governing pattern rather than stretching P2S into generic process management.

1. Recover the problem pressure or architecture concern. Name the pressure kind, problem-pressure signals, any source-use records, affected holon, and the first governing pattern. If the pressure is still only a problem-side signal, use `C.22.2` before P2S continues.
2. Recover the described holon, bounded context, candidate or selected structure kinds, selected structures when available, and architecture characteristics. Use `C.30` for the grounded architecture claim, `C.32.HCS` for starter characteristic heads, `C.32.ACS` for project criteria rows, and `C.25` when a composite quality family is current.
3. Represent future-structure uncertainty. State unknown structure kinds, unknown internal composition, candidate bearers, interfaces, allocations, variation points, constraints, expected structures, and the condition that returns the work to stronger inspection of the selected or expected structure. Record what is captured, handed off, latent, hidden, or lost.
4. Generate architecture ideas, principles, constraints, and candidate structure changes. Use an admitted problem-side record, source-pack cue, architecture pressure note, or candidate-generation input only after the affected selected structure, architecture characteristic, expected gain, accepted loss, and receiving governing pattern are recoverable.
5. Synthesize candidate architecture configurations and candidate sets through `C.32`. Keep function-bearing feasibility, constructive modules, placement, control, transformation-flow, work, role, information, evidence, scale, and other selected structures visible when they change the candidate.
6. Compare, retain, publish, or return alternatives through the pattern that governs the set relation. Use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.18` and `C.19` for archive, front, and pool policy, `G.5` for publication of a selected set, and `C.11` for a fixed local choice.
7. Make a project architecture decision through `C.32.PAD` when implementation commitment is current. The decision relation names the selected architecture option, affected structures, trade-off, accepted losses, method and work consequences, accepted lost-structure return, and decision repair or supersession condition.
8. Publish descriptions, views, ADR-like records, narrative renderings, or other records only as descriptions, structure-to-narrative renderings, or publication forms of structures, decision relations, method expectations, description or view loss repair, and reader use. Use `C.30.AD`, `C.30.ASV`, `C.32.ADR`, `A.6.3.NAR`, `E.17`, and `E.24.PUB` as applicable.
9. Hand transformer roles the method descriptions, constraints, readiness expectations, work expectations, and structure-use return conditions needed to realize selected structures. Use `A.15`, `A.15.2`, and `A.15.5` for method, work-plan, and readiness claims.
10. Realize selected structures in the transformed holon through domain work. Use `A.15.1` for performed work and `A.3.4` when one bounded transformation claim is current. The P2S card records refs; it does not perform the work.
11. Observe, inspect, measure, and evaluate actual selected structures, architecture-characteristic results, and functional-characteristic or capability implications in operation or use. Ask whether the realized structures enable or block the functions and effects they were meant to bear, and ask what selected structure, accepted loss, counter-characteristic, or functional implication got worse when a visible metric improved. Do not turn functional demand into an architecture characteristic or an eval result into decision authority. Use `C.32.ACE` for eval programs and eval results, `C.16` for measurement, and `C.25` for Q-bundles. Use `E.23` when repeated improvement method is current, `G.11` when currentness, telemetry, edition, freshness, or decay orchestration is current, `E.18` for transformation-flow slice-local refresh, `C.18` or `C.19` for archive, front, and pool updates, `C.32.PAD` or `C.32.ADA` for decision repair or supersession, `C.32` for new synthesis, and `C.30.AD` or `C.30.ASV` for architecture-description or structural-view loss repair. Feed actual-structure divergence, eval results, functional implications, freshness loss, description or view loss, and new constraints into the return or repair action governed by the receiving pattern.

When one holon changes another holon, add the transformer/transformed branch before candidate synthesis becomes narrow. Name the changing relation, the transformer holon, the transformed holon, and selected structures on both sides when they constrain the candidate set. Use `C.32.CONWAY` to frame candidate families: change transformer-side structures, change transformed-side structures, change both, or declare a bounded mismatch with the named correspondence or decision-repair return condition.

#### C.32.P2S:4.1 - P2S Unfolding Structure Block

When the P2S card must remain reusable across decision, description, work, and feedback governing patterns, add this local block. `P2SUnfoldingStructureBlock` is an architecture-facing local `A.22.CGUS` `U.Structure` specialization block governed here for problem-to-structure architecturing use. It is not a root U-kind, not an architecture decision, not an ADR, not an architecture description, and not a work plan by itself.

```text
P2SUnfoldingStructureBlock:
  unfoldingStructureRef: current architecture-facing ConstraintGovernedUnfoldingStructure record
  problemPressureRef:
  selectedOrUnknownStructureRefs[]:
  architectureContentLoci[]:
  structuralUncertaintyLoci[]:
  candidateSynthesisLoci[]:
  decisionLinkageRef?:
  realizationWorkLinkageRef?:
  actualStructureFeedbackRef?:
  e18TransformationFlowUnfoldingRefs[]?:
  descriptionRefs[]?:
  blockedOverread: not architecture decision, not ADR, not work plan by itself
```

The block is useful when the architecture work has to show how problem pressure constrains candidate, selected, expected, or actual structures without hiding which pattern governs the next claim. `unfoldingStructureRef` names the current CGUS record or local architecture-facing structure block; an A.22-level narrower-specialization relation, when needed, remains `specializedStructureRef?` on the A.22.CGUS record. `decisionLinkageRef` points to `C.32.PAD` only when a project architecture decision is current. `descriptionRefs[]` point to `C.30.AD`, `C.30.ASV`, `C.32.ADR`, `A.6.3.NAR`, or publication governing patterns only when a description, view, ADR projection, narrative rendering, or publication claim is current. `realizationWorkLinkageRef` points to the A.15 family; the P2S block does not authorize or record performed work.

Use `e18TransformationFlowUnfoldingRefs[]` only for slices whose substrate is transformation-flow structure. P2S itself is broader: it can carry module, functional, placement, control, role, method, evidence, scale, information, and other architecture-relevant structures through architecture synthesis and feedback.

#### C.32.P2S:4.2 - Architecture Unfolding Structure Use

Use `ArchitectureUnfoldingStructureUse@Project` when a named constraint-governed unfolding structure is being used as architecture-relevant structure inside problem-to-structure architecturing. This is a dependent architecture-use relation record owned here and by the relevant C.30 or C.32 architecture pattern. It is not a root U-kind, not an architecture decision, not an architecture description, not an ADR projection, and not realization work.

```text
ArchitectureUnfoldingStructureUse@Project:
  kind: dependent architecture-use relation record under C.32.P2S, C.30, and adjacent architecture governing patterns
  architectureQuestionRef:
  architectureOfRef:
  unfoldingStructureRef:
  architectureStructureUseKind:
    transformationFlow |
    methodWork |
    control |
    narrativePublication |
    evidenceAssurance |
    referenceCurrentnessRefresh |
    otherDeclared
  architectureViewpointRef?:
  affectedSelectedStructures[]:
  architectureCharacteristicRefs[]:
  acceptedLosses[]:
  methodOrWorkLinkageRefs[]?:
  architectureDecisionRef?:
  architectureDescriptionRefs[]?:
  architectureUseReturnCondition:
  repairOrSupersessionCondition:
```

`architectureQuestionRef` and `architectureOfRef` name the architecture question and described holon in bounded context. `unfoldingStructureRef` names the CGUS or local block being used. `affectedSelectedStructures[]`, `architectureCharacteristicRefs[]`, and `acceptedLosses[]` state why the unfolding structure matters for architecture rather than for a generic route. Method and work refs point to the A.15 family only as realization or feedback linkage. Decisions, descriptions, ADR-like projections, measurements, evals, evidence, gates, publication, and performed work still exit to their direct governing patterns.

Stop conditions:

- stop at `C.22.2` when the signal is not yet a reviewable problem-side record;
- stop at `C.30` or `C.30.ASV` when the current need is only architecture claim or structural-view adequacy;
- stop at `C.32` when the next useful artifact is a candidate palette rather than a whole P2S carry-through record;
- stop at `C.32.PAD` when the project architecture decision is current;
- stop at the A.15 family when the current question is method, work planning, readiness, or performed work;
- stop at `C.16`, `C.25`, `C.29`, `C.32.ACE`, `E.23`, or `G.11` when the current claim is measurement, quality-bundle, mathematical-lens, eval, improvement, or `G.11` currentness refresh;
- return to P2S only when a later governing pattern returns architecture pressure that changes candidate structures, expected structures, actual structures, selected structures, or the stronger-structure inspection return condition.


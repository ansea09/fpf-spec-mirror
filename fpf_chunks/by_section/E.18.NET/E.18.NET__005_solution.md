---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__005_solution.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:4 — Solution"
line_start: 84305
line_end: 84447
dependencies:
  - "A.1.STM"
  - "A.12"
  - "A.15"
  - "A.15.6"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.30.TFS-REL"
  - "C.32.CONWAY"
  - "E.11"
  - "E.11.PUA"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.18.3"
  - "F.18"
  - "U.Transfer"
keywords:
---

### E.18.NET:4 - Solution

#### E.18.NET:4.1 - Select a dependent non-agentive structure

`TransformationFlowStructureNetwork@Context` is a dependent, non-agentive specialization of `U.Structure` defined by E.18.NET and selected through the A.22 identity law. It is not a root U-kind, acting system, holon, workflow, graph, record, publication, `FlowValuation`, WorkPlan, or performed Work. The `@Context` suffix qualifies retrieval and use; it adds no identity discriminator.

For `N : TransformationFlowStructureNetwork`, recover exactly:

```text
StructureIdentity(N) = <
  directMemberRefs[],
  selectedCrossFlowRelationOccurrenceRefs[],
  selectedNetworkConstraintRefs[],
  networkUseFrame
>
```

The four field names have the same meanings as in the first-use result: exact direct members, exact selected obtaining cross-flow occurrence refs, exact applied network constraints, and one concrete use frame. `returnCondition` is not a fifth identity discriminator; it records when the current use must return and reselect.

The direct-member set contains at least two exact values. Each member is one independently identified `TransformationFlowStructure` or one independently identified E.18.NET-conforming `TransformationFlowStructureNetwork`. At least one selected relation occurrence binds positions in different direct members or in different leaf TFS members reached through them. The use frame says what the practitioner will decide or do with this selected organization and names the forbidden overread. “Current use”, “appropriate network”, and the title of a diagram are not use frames.

A row in a record does not create a member or make membership obtain. This profile needs no generic `networkMemberOf` relation. If a future receiver needs a separately re-identifiable world-side membership occurrence, reopen that relation question under A.6.RCD; do not infer it from the member list.

#### E.18.NET:4.2 - Reidentification and change locality

Replacing a direct member, selected relation occurrence, applied endpoint or exposure constraint, acyclicity constraint, or named selection-use frame identifies another selected network. Reidentifying a nested member reopens every parent network that selects that exact member.

Changing only a name, reference designator, record edition, graph layout, mathematical description, publication, selecting system, selection Work, evidence item, `FlowValuation`, `PathSliceId`, or local `DesignRunTag` leaves the network unchanged when the four A.22 discriminators still resolve to the same values.

#### E.18.NET:4.3 - Recurse through finite member paths

The selected direct-member nesting is acyclic. No direct or transitive member path from a network resolves back to that network, and every member path used by a reference is finite. This permits build-the-builder and supply-network recursion without inventing level-1, level-2, or level-3 network kinds.

Cycles among selected cross-flow relation occurrences remain possible when their applicable predicates and constraints permit them. Feedback from operation or evaluation to development is therefore compatible with acyclic membership: the cycle is among those relation occurrences, not in network containment.

`E.18` defines the complete `FlowPositionRef` identity. Import that tuple unchanged; E.18.NET defines only the `ExposedFlowPositionRef` extension needed for a boundary position reached through one finite member path:

```text
FlowPositionRef := <
  transformationFlowStructureRef,
  localFlowPositionId
>

ExposedFlowPositionRef := <
  networkStructureRef,
  memberPath[],
  leafFlowPositionRef
>
```

Every hop in `memberPath[]` resolves through the preceding network's direct members. Its final member is the TFS named by `leafFlowPositionRef`. When the path crosses a nested network, the leaf position must be one of the boundary positions that nested network exposes for the current higher-level use. Two different paths to the same leaf TFS position are two different exposures.

The parent network may compose the finite path and use the exposed boundary. It may not copy or silently flatten the nested member's internal structure. `FlowValuation`, `PathSliceId`, actual fillings, and `DesignRunTag` qualify use of a position; they are not part of `FlowPositionRef` or `ExposedFlowPositionRef` identity.

#### E.18.NET:4.4 - Keep valuation and design/run state leaf-local

Each `positionBindingRef` cites an E.18 position/valuation binding or a declaration-local binding whose pattern defines the needed participant meanings, value kind, and reference mode. A network introduces no universal cross-flow value kind.

`DesignRunTag` belongs to one exact position binding inside one exact leaf TFS. A network has no network-level `FlowValuation`, global design/run ladder, or automatic crossing that changes the carried entity's kind. If the same episteme fills local positions in different members—for example one position concerned with design work and another with production, verification, or later operation—record each leaf-local binding and the exact relation that obtains between them. Those ordinary member descriptions create no fixed TFS taxonomy or lifecycle phase.

#### E.18.NET:4.5 - Preserve the direct cross-flow relations

For every relation used by the network, recover:

- the exact obtaining occurrence;
- the exact relation kind;
- the pattern that defines or tests its predicate, applicability, and occurrence-identity rule;
- the complete signature and participant order;
- the endpoint member and position binding for every participant; and
- direction only when the direct relation has direction.

An n-ary relation remains n-ary. Do not decompose it into invented binary arrows. A row, edge label, shared entity, temporal adjacency, operation result, plan row, or graph connection never makes the relation obtain.

`U.Transfer` remains E.18's internal relation kind for one TFS. It is not a universal relation between network members. For any production, use, participation, evaluation, correspondence, feedback, dependency, supply, or other cross-flow relation, the relation kind must already be admitted. Use its applicable relation pattern to recover the participant meanings, predicate, applicability, and occurrence-identity rule; current case facts or constituting history must satisfy the predicate affirmatively. Only then does one world-side occurrence obtain. Use A.6.REL only when a named use must distinguish that occurrence from another. For ordinary network selection, the PatternID and exact relation occurrence are enough; add `relationFunctionClaimRef` to the defining or constraining `ClaimGraph` only when comparison, migration, or reliance depends on that exact rule identity. The network selects only the exact already-obtaining occurrence ref.

If no admitted relation kind and applicable predicate cover the intended participants and use, carry `missing-governor` from the pattern governing the relation claim. If required case facts are unavailable, carry its `missing-information` result; if the available basis is sufficient to apply the positive test but that test fails, carry `factually unsupported`. Neither result by itself establishes a negative. Carry an inapplicable or negative result only when the governing pattern defines that outcome and its current basis establishes it. Only a positive obtaining occurrence may fill `selectedCrossFlowRelationOccurrenceRefs[]`.

After a positive occurrence is established, test the E.18.NET endpoint and position bindings separately. A missing binding blocks network selection but does not change the relation result. Missing members, applied constraints, and use-frame values are likewise separate network-selection blockers. A row, graph edge, or episteme neither admits a relation kind nor creates an occurrence. In none of these branches substitute `creates`, `produces`, `uses`, `input`, `output`, `result`, `handoff`, or `transfer` as a generic edge.

#### E.18.NET:4.6 - Record the network without replacing it

When the selected answer must survive beyond the immediate work, describe it with a separate C.2.1 episteme:

```text
TransformationFlowStructureNetworkRecord@Context <: U.Episteme:
  entityOfConcernRef: one exact TransformationFlowStructureNetwork ref
  entityOfConcernKindRef: TransformationFlowStructureNetwork
  claimScope?: U.ClaimScope
  effectiveReferenceScheme: U.ReferenceScheme
  directMemberRows[]:
    memberRef: TransformationFlowStructureRef | TransformationFlowStructureNetworkRef
  exposedFlowPositionRows[]:
    exposedFlowPositionRef: ExposedFlowPositionRef
    memberPath[]
    leafTransformationFlowStructureRef
    leafFlowPositionRef
  crossFlowRelationRows[]:
    exactRelationOccurrenceRef: U.RelationRef
    exactRelationKindRef: U.KindRef
    subjectPatternLocator: U.EntityRef, locating the pattern that defines or tests this relation
    relationFunctionClaimRef?: U.EntityRef, referencing the exact defining or constraining ClaimGraph when the recorded use depends on that rule identity
    endpointRows[]:
      relationParticipantPositionRef
      memberRef
      flowPositionRef: FlowPositionRef | ExposedFlowPositionRef
      positionBindingRef
  architectureCorrespondenceRowRefs[]?: C.32.CONWAY episteme refs
  selectedNetworkConstraintRefs[]
  networkUseFrame
  preservedNetworkStructure
  lostOrHiddenNetworkStructure
  returnCondition
```

The record describes the network; it is not the network. Its member and relation rows cite objects that already exist and occurrences that already obtain. An architecture-correspondence row is a qualified reading only. It contributes no member or selected cross-flow relation unless an exact separately grounded relation occurrence and endpoint bindings also satisfy the network identity.

E.18.NET defines this composite locator for one nested cross-flow row:

```text
NetworkCrossFlowRelationRowRef := <
  transformationFlowStructureNetworkRecordRef: U.EpistemeRef, referencing one exact current TransformationFlowStructureNetworkRecord@Context edition,
  exactRelationOccurrenceRef: U.RelationRef,
  orderedEndpointBindingIdentity[]: <
    relationParticipantPositionRef,
    memberRef,
    flowPositionRef: FlowPositionRef | ExposedFlowPositionRef,
    positionBindingRef
  >
>
```

Resolve the record ref first, then match `crossFlowRelationRows[]` by the exact occurrence ref and the complete ordered endpoint-binding identity. Exactly one row must match. Zero matches or several matches leave the locator unresolved and stop that consumer; never fall back to the containing record, the occurrence alone, or a prose pointer. `NetworkCrossFlowRelationRowRef` is a reference shape, not a U-kind, episteme, or relation occurrence. Its `U.EpistemeRef` targets the containing record, never the nested row.

#### E.18.NET:4.7 - Keep descriptions, demonstrations, architecture, and Work outside identity

Use E.18.2 for a graph, hypergraph, network expression, wiring diagram, category-theory object, tuple, fold, or other mathematical description of the selected network. State what that description preserves and loses. A rendered graph or publication face remains under E.17 and C.29 as applicable.

Use A.22.CGUS and E.18.3 for an admitted network-aware `DemonstrativeUnfoldingSlice@Context`. Its finite paths must map to already admitted included positions, its cross-flow relations must cite admitted exact relation-reference epistemes, and its tags remain in leaf-local bindings. The slice demonstrates one traversal; it is neither the network nor an actual trajectory, WorkPlan, or Work occurrence.

Use C.30.TFS-REL when architecture uses the selected network. Name one exact containing holon whose `ArchitectureOf@Context` selects the network, or explicitly state the inter-holon use and its participating architecture claims without inventing a bearer. Use C.32.CONWAY only for its one-pair architecture-influence reading; the pair neither acts nor becomes the network.

Only admitted Systems perform Work. Selecting a network, writing its record, or drawing its graph may be Work when A.15.1 admits the occurrence; none is performance by the network, and no Work claim is needed merely to select or discuss the network. When selection Work is material, cite the independently established A.15.1/F.6 result and leave its assignment and attribution proof with those patterns. Keep the Method, performer, dated Work, result episteme, selection or decision relation, and any C.11 choice result separate. A result episteme is not a decision or accountability relation by form; state accountability, duty, responsibility, or authority only through the exact direct relation that obtains.


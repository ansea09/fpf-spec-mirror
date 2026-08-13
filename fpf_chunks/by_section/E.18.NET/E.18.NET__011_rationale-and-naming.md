---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:10"
section_title: "Rationale and naming"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__011_rationale-and-naming.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:10 — Rationale and naming"
line_start: 86248
line_end: 86269
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

### E.18.NET:10 - Rationale and naming

The selected head preserves the established `TransformationFlowStructure` name, says that the members are structures rather than valuations, and supports recursion without fixed levels. The shorter cue “transformation-flow network” is retrieval wording only after the governed value is clear.

Mint vs reuse: E.18.NET mints the durable names `TransformationFlowStructureNetwork`, `TransformationFlowStructureNetworkRecord@Context`, `ExposedFlowPositionRef`, and `NetworkCrossFlowRelationRowRef` for the governed value family, separate description episteme, and two reference shapes defined here. It reuses `U.Structure`, `U.Episteme`, `TransformationFlowStructure`, `FlowPositionRef`, relation kinds, and relation occurrences without changing their meanings; labels, records, and references create none of those values.

```text
NameCard:
  NameCardId: NC-TRANSFORMATION-FLOW-STRUCTURE-NETWORK
  GovernedValueRef: TransformationFlowStructureNetwork@Context <: U.Structure
  SubjectPatternLocator: E.18.NET
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: recursive selected organization over independently identified TransformationFlowStructure or TransformationFlowStructureNetwork values and exact cross-flow relation occurrences, with member boundaries and locally exposed positions preserved
  TechLabel: TransformationFlowStructureNetwork
  PlainLabel: network of transformation-flow structures
  CandidateSet: TransformationFlowStructureNetwork; TransformationFlowNetwork; CrossFlowRelationStructure; TransformationFlowDependencyStructure; CoupledTransformationFlowStructure; FlowOfFlows; CreatorGraph; CreationStructure
  RejectedCandidates: TransformationFlowNetwork can mean one network-shaped TFS; CrossFlowRelationStructure hides the transformation-flow use; TransformationFlowDependencyStructure narrows to one projection; CoupledTransformationFlowStructure suggests one merged TFS; FlowOfFlows conflicts with FlowValuation; CreatorGraph confuses the ontic structure with a graph and narrows change to creation; CreationStructure excludes operation, repair, modification, and reuse
  SelectionRationale: preserve the established TransformationFlowStructure head, make structures rather than valuations the members, and permit recursive membership without numbered levels
  LineageEntries: flow-of-flows and creator-graph examples remain retrieval lineage for the stress cases; fixed two-level and one-giant-flow ontic readings are retired
  RefreshCondition: reopen if repeated use cannot distinguish one TFS with several valuations, one subflow, and a recursive network of independently identified TFS values
```


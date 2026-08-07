---
chunk_kind: "child"
pattern_id: "E.18.NET"
pattern_title: "Network of Transformation-Flow Structures"
section_id: "E.18.NET:1"
section_title: "Problem frame — intent and first useful result"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.NET/E.18.NET__002_problem-frame-intent-and-first-useful-result.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "E.18.NET — Network of Transformation-Flow Structures"
  - "E.18.NET:1 — Problem frame — intent and first useful result"
line_start: 85100
line_end: 85141
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

### E.18.NET:1 - Problem frame — intent and first useful result

Use this pattern when one engineering question depends on two or more independently identified transformation-flow structures, or on nested networks of them, and at least one exact relation connects positions across their boundaries. Typical situations include a toolchain that builds another tool, a production system related to the product it helps produce, or an operating flow whose observation returns to a separate development flow.

Start with the practical choice, not with a graph:

1. decide whether the case is several valuations of one flow structure, an internal portion of one flow structure, or a network of independent flow structures;
2. identify each candidate member independently;
3. name the exact obtaining relation occurrences that connect positions in different members;
4. select only the members, relations, boundary exposures, and constraints needed for the current question; and
5. return one exact network reference, or stop at the proposed description and name the absent identity discriminator or exact relation-status result.

The first useful result is therefore small. It is either:

```text
selectedNetworkRef: one exact TransformationFlowStructureNetwork
directMemberRefs[]: at least two refs to independently identified TransformationFlowStructure or E.18.NET-conforming TransformationFlowStructureNetwork values
selectedCrossFlowRelationOccurrenceRefs[]: exact selected obtaining relations under their direct patterns
selectedNetworkConstraintRefs[]: exact applied endpoint, boundary-exposure, and acyclic direct-member constraints
networkUseFrame:
  questionOrAction: the concrete question answered or action enabled
  forbiddenOverread: what this selection does not establish
returnCondition: the first member, relation, constraint, or use-frame change that reopens selection
```

or an exact stop such as:

```text
proposedNetworkDescriptionRef: current diagram or record
blockedClaim: "the compiler-building flow produces the compiler-use flow input"
directRelationStatus:
  missing-governor: no direct relation kind/predicate governs these participants and use
  unresolved-grounding: a governor exists but current facts do not decide its predicate
  false-predicate: current facts fail the predicate, so no occurrence fills the network
  missing-endpoint-binding: an occurrence obtains but one required position binding is absent
result: exactly one applicable status above
```

If any `directMemberRefs[]`, `selectedCrossFlowRelationOccurrenceRefs[]`, `selectedNetworkConstraintRefs[]`, or `networkUseFrame` value is absent or unresolved, keep `proposedNetworkDescriptionRef` and name that exact missing discriminator. Use `directRelationStatus` only for the relation branch shown above; a missing member, applied constraint, or use frame keeps its own stop. Do not assert `selectedNetworkRef` until all four discriminators are recoverable.

Do not use E.18.NET merely because one flow branches, contains a detailed portion, has several valuations, or is drawn as a network. Use E.18 for one selected `TransformationFlowStructure`, its valuations and internal `U.Transfer` relations; use E.18's `SubflowRef` for one parent-relative internal portion. Use E.18.2 when the current object is a graph, wiring diagram, tuple, category-theory expression, or another mathematical description. Use A.22.CGUS and E.18.3 when the current object is an admitted demonstrative traversal rather than the network itself.


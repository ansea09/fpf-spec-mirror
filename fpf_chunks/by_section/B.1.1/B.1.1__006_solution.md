---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Structure and Relation Grounding"
section_id: "B.1.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__006_solution.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "B.1.1 — Dependency Structure and Relation Grounding"
  - "B.1.1:4 — Solution"
line_start: 35546
line_end: 35611
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.22"
  - "A.6.5"
  - "B.1"
  - "B.1.4"
  - "B.3.5"
  - "C.13"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
keywords:
---

### B.1.1:4 - Solution

Use dependency structure first; use graph representation second.

#### B.1.1:4.1 - Dependency Structure Frame

```text
DependencyStructure@Context:
  structureUnderConcernRef:
  boundedContextRef:
  candidateNodeRefs:
  dependencyRelationRefs:
  partWholeRelationRefs?
  boundaryCrossingRelationRefs?
  orderRelationRefs?
  temporalRelationRefs?
  resourceRelationRefs?
  representationRelationRefs?
  evidenceRelationRefs?
  publicationOrSourceUseRefs?
  designRunTag?
  directOwnerRefs:
```

This frame is not a U-kind. It records which relation claims are current and which direct owners govern them.

#### B.1.1:4.2 - Graph Representation

Use graph language only when a graph is the selected mathematical or representation lens:

```text
DependencyGraphRepresentation@Context:
  representedDependencyStructureRef:
  nodeExpression:
  edgeExpression:
  graphPropertyChecks?
  mathLensRef?
  publicationOrViewRef?
```

The graph may express acyclicity, reachability, cutsets, weak links, flow, or traceability. Those checks apply to the graph expression and bear on the selected relation only when the relation owner admits the mapping.

#### B.1.1:4.3 - Relation Grounding Guide

| If the edge means... | Recover... | Direct owner |
| --- | --- | --- |
| part of the whole | part-whole relation over admitted holons | `A.14`, `C.13`, `B.1` |
| member of a collection | membership or collection-as-whole claim | `A.14`, `C.13`, `C.16` |
| phase of the same carrier | temporal phase relation | `A.14`, temporal owner, `B.1.4` |
| ordered step or branch | method, process-view, or order relation | method owner, `B.1.4`, `C.29` when lens is current |
| performed work part | work occurrence relation with evidence and timing | `A.15.1` |
| external influence, signal, supply, measurement, or control | boundary-crossing relation or direct transformation, evidence, measurement, source-use, or control relation | `A.1`, `A.3.4`, `A.10`, `C.26`, or direct owner |
| representation, dashboard, digital twin, or architecture description | description or representation relation, not parthood | `C.2.1`, `E.17`, `C.30.AD`, `C.30.AD.BA` |

#### B.1.1:4.4 - Graph Checks Are Conditional

Acyclicity, topological order, cutset, reachability, and flow checks are useful only after the graph is selected as a lens over a selected relation structure.

Do not infer:

- parthood from graph adjacency;
- independence from graph separation without relation-owner admission;
- performed work from a planned step graph;
- whole reidentification from a graph property without B.2;
- architecture from a graph without selected-structure and architecture owners.


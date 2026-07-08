---
chunk_kind: "child"
pattern_id: "C.2.P.DR"
pattern_title: "Declarative Representation Precision Restoration"
section_id: "C.2.P.DR:5"
section_title: "Worked slices"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P.DR/C.2.P.DR__007_worked-slices.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "C.2.P.DR — Declarative Representation Precision Restoration"
  - "C.2.P.DR:5 — Worked slices"
line_start: 40460
line_end: 40548
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19.SPR"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "B.3"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "E.8"
  - "F.19"
keywords:
---

### C.2.P.DR:5 - Worked slices

#### C.2.P.DR:5.1 - Graph path in a transformation-flow structure

Wording: "The P2W path routes the team from principle to work."

Repair:

```text
DeclarativeRepresentationRepair:
  EncounteredRepresentation: P2W path or path slice in a selected TransformationFlowStructure
  RepresentationKind: graph path or PathSlice candidate under E.18 and E.18.1
  RepresentedEntityOfConcernOrClaim: carry-through relation from accepted problem-side material to next FPF kind named by value
  SourceOrPublicationRelation: current graph or pattern publication when relevant
  TemptingImperativeOverread: ordered work route for the team
  RecoveredGoverningPattern: E.18.1, with A.15.2 or A.15.1 only if planned or dated work is current
  RetainedUse: graph representation or path representation and carry-through record
  BlockedOverread: no work route or prescribed workflow by path shape alone
  StopOrReopenCondition: reopen when path, source currentness, graph edition, or intended work relation changes
```

#### C.2.P.DR:5.2 - Evidence path near release

Wording: "The evidence path authorizes release."

Repair: `A.10` can state an evidence path for the claim or effect. Release, permission, or gate passage requires the authority, gate, or release pattern that governs that claim. This pattern is used only if `path` wording itself is causing the representation to be overread as a permission route.

#### C.2.P.DR:5.3 - Query plan and access path

Wording: "The query plan calls the production work sequence."

Repair: recover whether the query plan is an optimizer representation, method description, formal substrate, source cue, evidence relation, work plan, or actual work trace. If it only represents query evaluation choices, do not treat it as `U.WorkPlan` or `U.Work`. If the current claim concerns method semantics, use `A.3.1`; if it concerns a method description, use `A.3.2`; if it concerns a performed query run, use `A.15.1` and the evidence pattern or source-use pattern.

#### C.2.P.DR:5.4 - Dashboard predicate

Wording: "The dashboard green path lets the release move."

Repair: recover dashboard face, source relation, status or state bearer, value frame, source currentness, and gate or release claim. The dashboard may be a publication face and source cue; it is not release permission unless the gate or authority pattern consumes the source and states that effect.

#### C.2.P.DR:5.5 - Pattern relation

Wording: "This pattern exits to A.10."

Repair: if the current relation is "use `A.10` when an evidence relation or provenance relation is current", write that declarative boundary. Do not use exit, receiver, route, owner, home, dispatch, or call language unless the pattern is actually about an action occurrence, work plan, control mechanism, or communication relation that has those semantics.

#### C.2.P.DR:5.6 - Solver algorithm

Wording: "The solver algorithm is the mechanism."

Repair: recover the current ontic slot, relation position, use relation, or claim kind. The solver configuration may be `U.MethodDescription`; the accepted semantic way of solving may be `U.Method`; the MILP formulation may expose formal substrate and mathematical-lens use; a reusable operation algebra with laws and admissibility predicates may be `U.Mechanism`; a solver run may be `U.Work`; a run result may be evidence for another claim. Select `A.6.1` and `E.20` only when mechanism fields are present in the current claim.

#### C.2.P.DR:5.7 - Reactor-cooling flow graph

Wording: "The preserved heat-flow path authorizes the valve change."

Repair:

```text
DeclarativeRepresentationRepair:
  EncounteredRepresentation: reactor-cooling heat-flow graph with one highlighted preserved path
  RepresentationKind: graph path or flow relation representation under E.18 and C.29 when mathematical-lens use is current
  RepresentedEntityOfConcernOrClaim: preserved heat-flow structure and boundary conditions for the cooling subsystem
  SourceOrPublicationRelation: current engineering review publication, source relation, or gate record when one is cited
  TemptingImperativeOverread: graph path authorizes physical valve-change work
  RecoveredGoverningPattern: E.18 and C.29 for graph and lens use; A.21, A.10, A.15.2, and A.15.1 only if gate, evidence, work plan, or dated work is current
  RetainedUse: graph structure for comparison, model review, and source-finding
  BlockedOverread: no release, gate passage, physical intervention, or work occurrence by highlighted path alone
  StopOrReopenCondition: reopen when gate decision, source currentness, measurement boundary, or work plan becomes current
```

#### C.2.P.DR:5.8 - CRISPR guide-selection table

Wording: "The guide-selection table approves the edit."

Repair:

```text
DeclarativeRepresentationRepair:
  EncounteredRepresentation: CRISPR guide-selection table with off-target scores and candidate ranking
  RepresentationKind: table representation, characteristic-space representation, or evidence-facing representation, depending on the claim being made
  RepresentedEntityOfConcernOrClaim: candidate guide comparison, off-target risk claim, or experimental-design option
  SourceOrPublicationRelation: lab notebook, protocol publication, source episteme, or review record when current
  TemptingImperativeOverread: ranked row approves biological intervention
  RecoveredGoverningPattern: C.16 or A.19 for characteristics when current; A.10 for evidence; A.15.2 for experimental work plan; A.21 or authority pattern only if approval or gate claim is current
  RetainedUse: source-finding, candidate comparison, and constraint review
  BlockedOverread: no edit approval, work occurrence, safety claim, or gate passage from table rank alone
  StopOrReopenCondition: reopen when protocol, gate decision, evidence path, role authorization, or dated lab work becomes current
```


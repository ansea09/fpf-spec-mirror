---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__002_problem-frame.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:1 — Problem frame"
line_start: 62188
line_end: 62225
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.3"
  - "B.2.5"
  - "B.3"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.17.0"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller and plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:1 - Problem frame

Use this pattern when a selected control structure or control-structure relation changes the next architecture move: a controller regulates a plant, an observer or estimator changes what can be known, a planner provides references to lower-rate control, a supervisor constrains a subsystem, a policy loop changes allowed behavior, or an LCA cue makes roles, rates, observation boundaries, actuation boundaries, feedback, or externalities architecture-relevant.

The first-minute working situation is ordinary engineering talk: a diagram says the supervisor watches a subsystem, a controller regulates a plant, an observer estimates state, a planner gives references to a lower-rate controller, or a policy or control relation changes allowed controller behavior. The useful first move is to recover a `ControlStructureViewNote`: which exact holon, actual architecture relation or bounded architecture claim is current; which exact selected control structure, control roles, and independently obtaining relations are present; which rate bands or recovered control-layer relations are claimed; which feedback or externality boundaries are named; and which governing pattern carries each additional claim. If the source only says `layer`, `level`, `tier`, or `stack` without a control-specific relation, use `C.30.STRAT` first.

What goes wrong if C.30.LCA is missed: a control diagram becomes the control structure, `U.View`, or proof; stratification labels bypass `C.30.STRAT` and carry undeclared scope; and `B.2.5`, E.18 transformation-flow prose, or Layered Control Architecture prose is overread as control adequacy.

What C.30.LCA buys in practice: the practitioner can keep useful controller, plant, observer, regulator, supervisor, feedback, rate, and control-layer language while recovering an exact selected control structure, one description episteme, its possible E.17.0 view conformance, and the governing pattern that carries any proof or claim named by value.

Not this pattern when the issue under repair is generic stratification or source-label repair, only an E.18 transformation-flow path slice, function description, module boundary, measurement head, causal intervention, or safety case. Use `C.30.STRAT`, `C.30.TFS-REL`, `A.6.F`, `A.6.M`, `C.16`, `C.28`, or the assurance/evidence pattern governing the claim as appropriate.

The primary EntityOfConcern for a full C.30.LCA description or view is one exact selected control `U.Structure`. The description, selected structure, controlled holon, actual architecture relation, bounded architecture claim, exact viewpoint, conformance occurrence, control-role assignments, direct control relations, diagram, representation, proof claims, and publication remain separate. Ordinary use may stop with a typed note:

```text
ControlStructureViewNote ordinary minimum:
  architectureRelationOccurrenceRef?: ArchitectureRelationRef
  architectureClaimRef?: U.EpistemeRef constrained to ArchitectureClaim
  describedHolonRef?: U.HolonRef
  selectedControlStructureRef?:
  controlledHolonRef:
  candidateViewEpistemeRef?: U.EpistemeRef
  exactViewpointRef?: U.ViewpointRef
  viewpointConformanceRelationRef?: EpistemeViewpointConformanceRelationRef
  controllerRoleAssignmentRef?:
  selectedControlRelationRef:
  feedbackClosureState: closed | oneWay | unclear
  controlLayerRelationRef?:
  rateBandRef?:
  stratificationRepairRef?:
  nextGoverningPatternApplicationRef?:
  stopCondition:
```

The ordinary note requires an exact described or controlled holon plus one selected control structure or honest structure gap and at least one direct control relation when a positive relation claim is made. `architectureRelationOccurrenceRef` is filled only when that direct C.30 occurrence obtains; `architectureClaimRef` remains optional claim content or trace. The note does not become a C.2.1 episteme or `U.View` by its field names.

Use full `ControlStructureView` only when an independently identified architecture-description episteme about the exact selected control structure satisfies the fixed E.17.0 predicate for one exact viewpoint. Full use is justified when roles, relations, rates, recovered control-layer labels, boundary refs, source return, representation/publication, or explicit governing-pattern applications matter beyond the note.


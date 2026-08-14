---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__002_problem-frame.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:1 — Problem frame"
line_start: 62530
line_end: 62575
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

Use this pattern when a selected control structure or an exact control relation changes the next architecture move: source prose says that a controller regulates a plant, an observer or estimator changes what can be known, a planner provides references to lower-rate control, a supervisor constrains a subsystem, or a policy loop changes allowed behavior. Treat those labels as cues to recover the direct relation and participant meanings first. A participating System, local system-role kind, separate System-classification judgment, assignment, Method, or Work is a separate fact included only when it independently obtains.

The first-minute working situation is ordinary engineering talk: a diagram says the supervisor watches a subsystem, a controller regulates a plant, an observer estimates state, a planner gives references to a lower-rate controller, or a policy or control relation changes allowed controller behavior. The useful first move is to recover a `ControlStructureViewNote`: which holon, architecture relation or bounded architecture claim is current; which selected control structure and obtaining control relations are present; what each participant means in those relations; which rate bands or recovered control-layer relations are claimed; which feedback or externality boundaries are named; and which subject assertion and defining or constraining `ClaimGraph` state each additional claim. Then add an admitted System, optional local kind, separate optional System-classification judgment, optional obtaining assignment, Method, and complete Work-attribution basis only when each is separately current. If the source only says `layer`, `level`, `tier`, or `stack` without a control-specific relation, use `C.30.STRAT` first.

What goes wrong if C.30.LCA is missed: a control diagram becomes the control structure, `U.View`, or proof; stratification labels bypass `C.30.STRAT` and carry undeclared scope; and `B.2.5`, E.18 transformation-flow prose, or Layered Control Architecture prose is overread as control adequacy.

What C.30.LCA buys in practice: the practitioner can keep useful controller, plant, observer, regulator, supervisor, feedback, rate, and control-layer language while recovering a selected control structure, one description episteme, its possible E.17.0 view conformance, and the pattern used to state or test each proof or claim.

Not this pattern when the issue under repair is generic stratification or source-label repair, only an E.18 transformation-flow path slice, function description, module boundary, measurement head, causal intervention, or safety case. Use `C.30.STRAT`, `C.30.TFS-REL`, `A.6.F`, `A.6.M`, `C.16`, `C.28`, or the applicable assurance or evidence pattern to state or test the current claim.

The primary EntityOfConcern for a full C.30.LCA description or view is one exact selected control `U.Structure`. The description, selected structure, controlled holon, actual architecture relation, bounded architecture claim, exact viewpoint, conformance occurrence, direct control relations and participant meanings, any participating Systems, local classifications, assignments, Methods or Work, diagram, representation, proof claims, and publication remain separate. Ordinary use may stop with a typed note:

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
  selectedControlRelationRef:
  selectedControlParticipantRefs:
  controllerSystemRef?: U.EntityRef constrained to U.System
  controllerSystemRoleKindRef?: U.KindRef
  controllerSystemRoleClassificationJudgmentRef?: U.RelationRef
  controllerAssignmentSpeciesRef?: U.RelationKindRef constrained under U.SystemRoleAssignment
  controllerAssignmentOccurrenceRef?: U.RelationRef constrained to an obtaining occurrence of controllerAssignmentSpeciesRef
  actualControlWorkRef?: U.EntityRef constrained to U.Work
  feedbackClosureState: closed | oneWay | unclear
  controlLayerRelationRef?:
  rateBandRef?:
  stratificationRepairRef?:
  nextPatternUseRef?:
  stopCondition:
```

The ordinary note requires an exact described or controlled holon plus one selected control structure or honest structure gap and at least one direct control relation when a positive relation claim is made. `architectureRelationOccurrenceRef` is filled only when that direct C.30 occurrence obtains; `architectureClaimRef` remains optional claim content or trace. The note does not become a C.2.1 episteme or `U.View` by its field names.

When either form includes actual control Work, each Work ref names an independently identified `U.Work` occurrence. All facts required by A.15.1, A.2.1, and F.6 remain recoverable; the note or view creates none of them.

Use full `ControlStructureView` only when an independently identified architecture-description episteme about the selected control structure satisfies the fixed E.17.0 predicate for one viewpoint. Full use is justified when control-participant meanings, direct relations, rates, recovered control-layer labels, boundary refs, source return, representation or publication, or the patterns used for particular claims matter beyond the note.


---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__002_problem-frame.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:1 — Problem frame"
line_start: 61371
line_end: 61406
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

Use this pattern when a control diagram, control-language source, or selected control structure changes the next architecture move. Start with an ordinary question: what actually controls what, through which observation, command, reference, supervision, or feedback relation? A label such as controller, plant, observer, planner, supervisor, or policy loop is only a cue; identify the relation and what each participant does in it before relying on the diagram.

A participating System, local system-role kind, System-classification judgment, assignment, Method, or Work is a separate fact. Add it only when it independently obtains and changes the use of the control-structure result.

The first useful result can be one sentence: “Supervisor S sends allowed-mode commands to controller C and receives status feedback; this diagram does not yet establish stability or safety.” The small note below retains that result and the next action. If the source says only `layer`, `level`, `tier`, or `stack` without a control-specific relation, use `C.30.STRAT` first.

What goes wrong if C.30.LCA is missed: a control diagram becomes the control structure, `U.View`, or proof; stratification labels bypass `C.30.STRAT` and carry undeclared scope; and `B.2.5`, E.18 transformation-flow prose, or Layered Control Architecture prose is overread as control adequacy.

What C.30.LCA buys in practice: the practitioner can keep useful controller, plant, observer, regulator, supervisor, feedback, rate, and control-layer language while recovering a selected control structure, one description episteme, its possible E.17.0 view conformance, and the pattern used to state or test each proof or claim.

Not this pattern when the issue under repair is generic stratification or source-label repair, only an E.18 transformation-flow path slice, function description, module boundary, measurement head, causal intervention, or safety case. Use `C.30.STRAT`, `C.30.TFS-REL`, `A.6.F`, `A.6.M`, `C.16`, `C.28`, or the applicable assurance or evidence pattern to state or test the current claim.

The primary EntityOfConcern for a full C.30.LCA description or view is one exact selected control `U.Structure`. The description, selected structure, controlled holon, architecture relation, architecture claim, viewpoint, conformance occurrence, control relations and their participants, any participating Systems, classifications, assignments, Methods or Work, diagram, representation, proof claims, and publication remain separate. Start with the smallest useful note:

```text
ControlStructureViewNote ordinary minimum:
  controlledHolonRef:
  selectedControlStructureRef?:
  structureGap?:
  selectedControlRelationRef:
  controlRelationParticipantRefs:
  feedbackClosureState: closed | oneWay | unclear
  nextPatternUseRef?:
  stopCondition:
```

Use either `selectedControlStructureRef` or an honest `structureGap`. A positive control claim also names at least one obtaining control relation and its participants. This note is enough when those values make the next action clear; its fields do not turn it into a C.2.1 episteme or `U.View`.

Add a described holon, an architecture-relation occurrence or claim, rate bands, control-layer relations, boundaries, view and viewpoint-conformance facts, source return, representation, or publication only when they change the intended use. Add participating Systems, local classifications, assignments, Methods, Work, and F.6 attribution only when those neighboring facts are independently current.

When either form includes actual control Work, each Work ref names an occurrence independently admitted under A.15.1 after every exact actual performer is recovered through A.13. `assignmentRows` and `actualControlWorkAttributionRefs` remain optional: include them only when the note, view, or receiving use expressly represents precise assignment-bound attribution. Any present attribution ref resolves through F.6 to the same obtaining A.13 assignment; absence or failure of that relation leaves the Work ref intact. The note or view creates none of these facts.

Use full `ControlStructureView` only when an independently identified architecture-description episteme about the selected control structure satisfies the fixed E.17.0 predicate for one viewpoint. Full use is justified when control-participant meanings, direct relations, rates, recovered control-layer labels, boundary refs, source return, representation or publication, or the patterns used for particular claims matter beyond the note.


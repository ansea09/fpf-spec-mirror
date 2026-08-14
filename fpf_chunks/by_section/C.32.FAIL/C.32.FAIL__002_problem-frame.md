---
chunk_kind: "child"
pattern_id: "C.32.FAIL"
pattern_title: "Architecture Failure Recognition and Repair"
section_id: "C.32.FAIL:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.FAIL/C.32.FAIL__002_problem-frame.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "C.32.FAIL — Architecture Failure Recognition and Repair"
  - "C.32.FAIL:1 — Problem frame"
line_start: 66433
line_end: 66498
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.2"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.RCD"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.27"
  - "C.29"
  - "C.3"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.P"
  - "C.31"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ROLE"
  - "E.17"
  - "E.18"
  - "E.18.NET"
  - "E.24.PUB"
  - "F.6"
  - "G.5"
keywords:
  - "architecture failure cue"
  - "architecture repair cue"
  - "candidate repair"
  - "repair-entry family"
  - "selected-structure relation"
  - "source overread"
  - "stressed architecture object"
---

### C.32.FAIL:1 - Problem frame

Use this pattern when a practitioner sees a recurring architecture-synthesis failure and needs to turn that warning into the smallest repair action over a named architecture object before evidence, assurance, selection, or decision claims are current.

Primary working reader: an architect or architecture-responsible practitioner who sees a warning sign during synthesis and needs the first architecture repair action, not a larger risk catalogue.

Typical entry cues:

```text
"This looks modular, but changes still cross hidden dependencies."
"The model is called a module, but the interface is weak."
"The platform promise hides exception growth."
"The search picked a winner, but the alternatives and losses disappeared."
"The graph looks convincing, but we cannot say which architecture object it repairs."
```

**First-minute use slice.** A team calls an ML model a module in a safety-relevant product architecture. Using C.32.FAIL, the practitioner does not add another warning name. The practitioner names the architecture object under stress: a candidate module-interface relation for the described product holon. The blocked overread is: model file equals stable module. The first repair action is to recover interface behavior, admissible-use conditions, change policy, and evidence-decay boundary before using the model as a module. If a safety assurance claim is current, the case escalates only after that architecture repair is named.

The primary `EntityOfConcern` is one repair cue for one architecture object under stress. The cue is a working repair aid, not a risk register, assurance case, selection result, release argument, or decision object.

What goes wrong if C.32.FAIL is missed: failure language degenerates into a warning bank. The team can say what looks suspicious, but it cannot say which architecture object must be repaired or which pattern defines or constrains the next claim.

What C.32.FAIL buys in practice: a practitioner can convert a vague failure signal into one typed repair action, keep the repair near the selected structure, and stop before nearby decision, release, or governance claims expand the case.

Ordinary working move: convert the symptom into four fields: architecture object under stress, blocked overread, first repair action, and stop or escalation condition.

Adoption test: after using C.32.FAIL, a reader can see four things in the cue: the architecture object under stress, the blocked overread, the first repair action, and the pattern for the next question or stop condition.

Use another pattern when the current work is only lexical cleanup, evidence sufficiency, release, architecture description, MVPK publication face, comparison, selection, archive, front, selected-set result declaration, actual publication, local choice, or final architecture decision. Use C.32.FAIL only when the failure cue changes the first architecture repair action.

Common exits by claim kind:

- `C.30.P`, `A.6.F`, `A.6.M`, `C.31`, `C.32`, `C.32.MLAO`, and `C.32.CONWAY` for architecture or selected-structure repair.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `C.18` and `C.19` for archive, front, pool-treatment, or retained-stepping-stone claims.
- `A.10` for evidence, `B.3` for assurance, and `A.20` or `A.21` for gate or release claims.
- `C.30.AD` for architecture description, `E.17` for a source-backed publication face and source return, and `E.24.PUB` for the publication occurrence and audience availability.
- `G.5` for selected-set result declaration, `C.11` for local choice, and `C.32.PAD` for a project decision. For publication, keep the distinct E.17 and E.24.PUB uses just named.

The first useful output is `ArchitectureRepairCue@Project`. It is a working record for one repair action. It names the stressed architecture object and first repair; it is not a failure ontology, risk register, assurance case, release argument, selection result, or decision:

```text
ArchitectureRepairCue@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureRepairCueProjectUseRelationRef?: U.RelationRef defined by the exact repair-use or work-use pattern
  symptom:
  describedHolonRef:
  architectureClaimRef?:
  architectureConcern:
  intendedRepairUse:
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?:
  architectureObjectUnderStress:
  selectedStructureRef?:
  sourceCueRef?:
  failureEvidenceRefs:
  blockedOverread:
  firstPatternLocator:
  repairAction:
  sourceReturnCondition:
  stopCondition:
  escalationIfCurrent:
```

Here `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the repair cue is genuinely used in one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work` and `architectureRepairCueProjectUseRelationRef` identifies the direct relation by which that exact project Work uses the cue. Any separately claimed repair Work and its own cue-use or work-to-change relation remain under their direct governors. The cue, the actual repair Work, the architecture object under stress, and the composite project Work remain distinct.


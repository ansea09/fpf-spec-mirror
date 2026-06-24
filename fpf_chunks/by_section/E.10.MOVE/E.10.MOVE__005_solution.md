---
chunk_kind: "child"
pattern_id: "E.10.MOVE"
pattern_title: "Move and Readiness Wording Precision Restoration"
section_id: "E.10.MOVE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.MOVE/E.10.MOVE__005_solution.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "E.10.MOVE — Move and Readiness Wording Precision Restoration"
  - "E.10.MOVE:4 — Solution"
line_start: 65920
line_end: 65995
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.16"
  - "A.16.0"
  - "A.21"
  - "A.3.4.P"
  - "B.1.6"
  - "C.24"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.11.PUR"
  - "E.17"
  - "E.18.1"
  - "E.24"
  - "G.6"
keywords:
---

### E.10.MOVE:4 - Solution

Apply this recovery order:

1. Recover the project concern first: what object, situation, relation, or intended result made the wording matter?
2. Classify source use: seminar pattern-use language, TameFlow `MOVE` source use, work-entry readiness, local move locus, ordinary prose, or quote-only wording.
3. Decide the direct governed value: `PatternUseRecommendation@Context`, E.18.1 P2W, `U.WorkPlan`, PlanItem, `SlotFillingsPlanItem`, `WorkEntryReadiness@Context`, A.21 `GateDecision`, performed `U.Work`, `U.Transformation`, `U.Method`, `U.MethodDescription`, A.16 language-state move, C.24 call planning, C.30 architecture candidate move, selected set, publication expression, source relation, or ordinary prose.
4. If several values are current, split them and name the direct governing pattern for each.
5. Preserve the remaining reader use. The repair fails if the text becomes formally clean but no longer tells the practitioner what can be done now.
6. Use `A.3.4.P` for the change-situation branch and return to `E.10.MOVE` only for pattern-use, project concern, or work-entry readiness wording left after the transformation branch is recovered.

#### E.10.MOVE:4.1 - MoveAndReadinessWordingRepair note

```text
MoveAndReadinessWordingRepair:
  EncounteredWording:
  BoundedTextSpan:
  ProjectConcern:
  SourceUseClass: seminarPatternUse | tameFlowMoveSource | workEntryReadiness | localMoveLocus | ordinaryProse | quoteOnly
  RecoveredRelations:
  DirectGoverningPatterns:
  RetainedPlainWording:
  BlockedOverread:
  RequiredSplit?:
  FinalWordingOrBlocker:
  RemainingReaderUse:
```

The note is a temporary wording-use restoration aid. It does not create project records, gate decisions, WorkPlans, or work occurrences.

#### E.10.MOVE:4.2 - Short Cue Set

Trigger this pattern only when the wording has FPF-governed use:

- move, first useful move, working move, professional move, SoTA move, strong move, admissible move, next move;
- step, action, application, solution, next action, work item, work entry;
- full kit, full-kitting, readiness, ready, committed, launch-ready;
- TameFlow `MOVE` or source MOVE;
- route, workflow, and process when the wording hides pattern-use, project-concern, or readiness relation rather than a transformation-situation claim.

The list is not a replacement vocabulary. It is a recognition aid for the recovery order.

#### E.10.MOVE:4.3 - Source-Use Classes

| SourceUseClass | Typical recovery |
| --- | --- |
| `seminarPatternUse` | `PatternUseRecommendation@Context`, `PatternUseSequence@Context`, publication phrase, or direct neighboring pattern. |
| `tameFlowMoveSource` | WorkPlan, PlanItem, full-kit preparation, `WorkEntryReadiness@Context`, A.21 when gate decision is current, preparation `U.Work`, target `U.Work`, resource relation, or result relation. |
| `workEntryReadiness` | `WorkEntryReadiness@Context`, `FullKitCondition`, A.15.2, A.15.3, A.15.1, A.21, B.1.6, or A.15.4. |
| `localMoveLocus` | A.16 language-state move, C.24 call-planning action, C.30 architecture candidate move, or another accepted local locus. |
| `ordinaryProse` | Keep or lightly rewrite without FPF restoration. |
| `quoteOnly` | Keep as source wording and block stronger use. |

#### E.10.MOVE:4.4 - Relation to A.3.4.P

Use `A.3.4.P` first when the wording is mainly about change in the world or a transformation-flow structure:

- process, workflow, path, pipeline, operation, flow, transformation, change, circuit, network, and route-like wording;
- graph path, path slice, flow valuation, or transformation-flow structure claims;
- method, mechanism, work, or publication-description confusion caused by change-situation wording.

Use `E.10.MOVE` when the remaining question is: which project concern, pattern use, work-entry readiness relation, or local move locus should the reader use next? If both are current, split the text and apply both patterns to their own current objects.

#### E.10.MOVE:4.5 - Durable Name Repair

Durable field and record names must name their direct governed value. Examples:

| Dirty durable name | Prefer |
| --- | --- |
| `FirstMoveRecord@Context` | `FirstApplicationRecord@Context` when the object is the first application record. |
| `RelationMoveNow` | `CurrentRelationGovernedUse` when the object is source-restoration use. |
| `NextMoveHypothesis` | `RecommendedPatternUse` or another direct candidate, selected set, work, gate, or architecture object. |
| `Pattern-Use Sequence` | `PatternUseSequence@Context` when the durable relation is meant. |

Do not run these as mechanical global replacements. Recover the governed object first.


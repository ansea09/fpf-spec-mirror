---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "Principles-to-Work Carry-Through"
section_id: "E.18.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__005_solution.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "E.18.1 — Principles-to-Work Carry-Through"
  - "E.18.1:4 — Solution"
line_start: 67523
line_end: 67675
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.0"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.22.2"
  - "C.29"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.19"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
  - "P2W"
  - "accepted ProblemCard@Context"
  - "carry-through record"
  - "evaluation refresh"
  - "formal substrate"
  - "mechanism realization"
  - "method-family selection"
  - "principles-to-work"
  - "work planning"
---

### E.18.1:4 - Solution

The solution has two parts: use the declarative carry-through structure below to select one relation-governed P2W move, then fill the carry-through or replay record only for the relation being made. The locus and relation vocabulary names which distinction can be preserved, which FPF relation is recovered, which record is written, which cue is stopped, and which earlier application reopens after a problem-side result becomes useful for work.

#### E.18.1:4.0 - P2W Declarative Carry-Through Structure

Use P2W as a declarative carry-through structure of relation-governed moves from an accepted `ProblemCard@Context` to accepted FPF applications. The structure is not a prescribed FPF-use procedure. It can be expressed as a graph-shaped description or joined with project workflow material only when the workflow or mathematical graph description is the current EntityOfConcern of a governed use: a `U.MethodDescription`, `U.WorkPlan`, `TransformationFlowStructure`, flow valuation, or `E.18.2` mathematical description. P2W itself shows which distinction can be preserved, which FPF relation is recovered, which record is written, which cue is stopped, and which earlier application reopens after a problem-side result becomes useful for work.

The carry-through structure has nine recurring loci. A concrete P2W application selects a carry-through slice: it may use one locus, branch into several applications, split one source phrase into several records, stop with a reduced-use cue, or reopen an earlier locus when measurement or source currentness changes.

| Locus | Question answered | Output of the P2W move |
|---|---|---|
| `AcceptedProblemSideOutput` | What accepted problem-side material is being preserved for the next use? | Problem-card reference plus carried distinction. |
| `NextFPFUseQuestion` | What is the next unsettled FPF kind or relation? | One question stated in FPF vocabulary. |
| `FirstPrinciplesLens` | What structure, invariant, loss, or payoff makes the next move worth formal treatment? | Preserved structure, lost structure, payoff, and stop condition. |
| `DeclarationStack` | Which `U.Signature(profile=FormalSubstrate)`, `PrincipleFrame`, ontology, CHR, measurement, normalization, or bridge relation is needed? | Declaration or reference to the declaration relation named by value. |
| `MechanismMethodCandidate` | Is the next work-facing issue mechanism-position meaning, method-position meaning, method comparison, or retained-set handling? | Mechanism cue, method cue, comparison cue, selector cue, or retained-set cue. |
| `TransformationTemporalAspect` | Is the next issue a bounded transformation under conditions, a temporal aspect of a governed object or claim, or the adequacy of an authored temporal claim? | `A.3.4`, `C.27.TA`, or `C.27` application. |
| `WorkPreparation` | Is a planning record, slot-filling plan item, feasibility note, evidence-reference pin, or freshness request needed? | `U.WorkPlan`, PlanItem, or `SlotFillingsPlanItem` application. |
| `PerformedWorkAndResult` | Has dated `U.Work` occurred, and what result-related records appeared? | Work occurrence plus unpacked artifact, telemetry, acceptance, measurement, source, or role-enactability relation. |
| `ReturnAndRefresh` | Did measurement, source currentness, reference plane, or problem-side wording change an earlier assumption? | Return to the affected application with the changed relation named. |

P2W relation labels are `carry`, `recover`, `write`, `split`, `stop`, and `return`. `Carry` preserves a distinction from the problem side. `Recover` names the FPF kind or relation. `Write` creates or amends the governed record. `Split` separates one source phrase into several applications. `Stop` preserves a reduced-use cue when no relation-governed continuation is available. `Return` reopens the smallest earlier application whose assumption changed. These are carry-through relation labels for P2W use, not a project-work procedure.

#### E.18.1:4.1 - Carry-through record

For first-minute use, fill only `ProblemCardRef`, `CarriedDistinction`, `NextFPFUseQuestion`, and either `RecoveredFPFKindOrRelation` or `StopCondition`. Use the remaining fields only when the move continues, splits, writes a record, or returns after a changed assumption.

Use one filled record when applying P2W. It is the local project-facing record of the pattern. Do not copy an empty form into project material; if a field cannot be filled with recovered claim content, state the stop condition or leave the field out.

```text
P2W carry-through record:
  ProblemCardRef: ProblemCard@Context PC-FAB-042, accepted for a cooling-fixture deformation problem.
  CarriedDistinction: the deformation is not one more tuning defect; the problem card identifies a conserved heat-flow structure that must survive method choice.
  NextFPFUseQuestion: does the team need mathematical-lens use or a `U.Signature(profile=FormalSubstrate)` declaration before method selection?
  P2WLocus: FirstPrinciplesLens -> DeclarationStack.
  RecoveredFPFKindOrRelation: mathematical-lens use plus `U.Signature(profile=FormalSubstrate)` and `PrincipleFrame` declaration relation.
  SelectedApplication: `C.29` for preserved and lost structure; `A.6.0` for `U.Signature(profile=FormalSubstrate)` and `PrincipleFrame` when the declaration is written.
  WrittenRecordOrApplication: a short `U.Signature(profile=FormalSubstrate)` declaration naming the heat-flow invariant, the boundary conditions being preserved, the deformation factors left outside the model, and the payoff for later method comparison.
  NotCarried: no method is selected by this record.
  StopCondition: stop before method selection until comparator, measurement, and selected-set relations are named.
  ReturnTrigger: later result measurement shows that the planned module-interface constraint used the wrong reference plane.
  SourceCurrentnessCheck: source restoration and refresh reopen the measurement, normalization, planning, and method-comparison applications; the earlier U.Work occurrence is cited but not rewritten by P2W.
```

`ProblemCardRef` and `CarriedDistinction` locate the accepted problem-side material and the distinction being carried. `NextFPFUseQuestion`, `P2WLocus`, and `RecoveredFPFKindOrRelation` keep the next FPF kind or relation explicit before a continuing carry-through relation is used. `SelectedApplication` and `WrittenRecordOrApplication` name what is used or written.

`NotCarried` is a compact field, not a place to repeat boundary doctrine from other governing patterns. It names only the local overread that would change this P2W move. `StopCondition`, `ReturnTrigger`, and `SourceCurrentnessCheck` keep stopping and reopening tied to a changed relation, measurement, source-currentness, or problem-side assumption.

This record shows the complete P2W relation structure: problem-side distinction, first-principles value, selected FPF application, written record, stop condition, and return after measurement and source-currentness change.

#### E.18.1:4.2 - Positive move table

| Locus reached | P2W move | Record or continuation |
|---|---|---|
| Accepted problem-side output | State what is carried from the problem card and what question under repair remains. | P2W carry-through record begins. |
| First-principles or mathematical cue | Name preserved structure, lost structure, payoff, and stop condition. | Mathematical-lens use or `U.Signature(profile=FormalSubstrate)` declaration. |
| Ontology, UTS, CHR, or `PrincipleFrame` cue | Order ontology, UTS, characteristic, measurement, and principle-frame declarations before downstream use. | Declaration-stack application. |
| Mechanism-position or method-position cue | Separate mechanism-position meaning from method-position meaning, method comparison, and retained-set handling. | Mechanism-position, method-position, method-comparison, selector, or retained-set application. |
| Bounded transformation or temporal-aspect cue | Separate bounded transformation, temporal aspect, and temporal-claim adequacy. | `A.3.4` for bounded transformation, `C.27.TA` for temporal aspect, or `C.27` when authored temporal-claim adequacy or currentness-use is being made. |
| Planning cue | Write or amend a planning record, plan item, evidence-reference pin, freshness request, or planned constraint. | `A.15.2 U.WorkPlan` or plan-item application. |
| Dated performed `U.Work` | Record the work occurrence and relation to plan, gate, launch values, provenance, and later result records. | Performed-work application plus any separate entry or provenance relation. |
| Result phrase | Split the phrase into artifact, resource, launch-value, telemetry, acceptance, measurement, source, quality, done-state, feedback, parity, refresh, or role-enactability relation. | One or more result-related applications. |
| Changed measurement or source currentness | Return to the smallest earlier application whose assumption changed. | Measurement, normalization, source-restoration, refresh, planning, method-comparison, or problem-side correction. |

#### E.18.1:4.3 - Locus Use Details

Problem-side input: P2W starts only from accepted problem-side material. The record carries the distinction that matters for the next move, not the whole problem-side pattern.

First-principles and declarations: mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, ontology, UTS, CHR, measurement, normalization, bridge, and `PrincipleFrame` material are handled as declaration-stack applications. The P2W record names which declaration or neighboring relation is being written or cited, what structure is preserved, what is lost, and which downstream relation is still unsettled.

When mathematical wording points both to a formal declaration and to a mathematical lens, P2W does not decide by vocabulary. Use the slot discipline in `A.6.0:10a.1`: `A.6.0` owns `U.Signature(profile=FormalSubstrate)` declaration, `C.29` owns mathematical-lens use, `A.6.1` owns mechanism consumption or realization, and `E.18.1` owns only the carry-through cue and next-relation selection.

Mechanism and method: do not decide by noun. Recover the claim position. A mechanism-position claim names operation algebra, law set, applicability predicates, effect realization, or mechanism-description need. A method-position claim names a context-defined semantic way of doing work, candidate set, comparison, selector, retained set, or selected-record need. A shared source label, project-side name, or recognizable change concern may require linked method and mechanism typed values, but P2W records only which relation is being carried through and leaves the other typed value as a stopped cue unless its governing pattern is opened.

Transformation and temporal aspects: a problem-side distinction may point to a bounded transformation, a temporal aspect, and a temporal-claim adequacy question at once. Do not fold these into method, mechanism, plan, or work. `A.3.4` owns bounded transformation under conditions, including transformed object, pre-state, post-state, condition set, and admissible effect claim. `C.27.TA` owns temporal aspects such as interval, deadline, cadence, rhythm, synchronization, currentness window, recovery timing, or stabilization timing when the aspect itself is being named. `C.27` owns adequacy, supported use, unsupported use, or source-currentness use of authored temporal claims.

Planning and performed work: planning records are `A.15.2 U.WorkPlan` values or plan-item records, including evidence-reference pins, feasibility notes, freshness requests, and planned constraints. Performed work is a dated `U.Work` occurrence. P2W records which side of that boundary the carry-through record uses and which later result records have appeared.

Result carry-through: a result phrase is treated as a bundle of possible records. The P2W move is to unpack it before it guides any next move.

Structure, publication, function, module-interface, and integration cues: a transformation-flow structure, mathematical graph description, diagram, or publication can help classify the P2W move. Function wording continues only as an `A.6.F` function or functional-relation claim; interface, port, protocol, connection, resource limit, or integration wording continues only as a module-interface, signature-slot, reusable-structure, or architecture relation named by value through `A.6.M`, `A.6.5`, `C.31`, or the `C.30` family. Otherwise the wording remains classification material for the P2W record.

#### E.18.1:4.4 - Boundary and relation discipline

P2W is not a catalogue of boundary doctrines from other governing patterns. It has one local boundary rule: carry only the distinction accepted on the problem side, recover the next FPF kind or relation, and stop anything that would require a different governing relation until that relation is being made.

| Source pressure | Local P2W decision | Continuation |
|---|---|---|
| Problem-side material | Carry only the accepted distinction and the next FPF-use question. | Continue when the next FPF kind or relation is named; otherwise stop before P2W begins. |
| First-principles or mathematical wording | State preserved structure, lost structure, payoff, and stop condition. | Continue only as mathematical-lens use or as a `U.Signature(profile=FormalSubstrate)` declaration when that relation is being made. |
| Declaration-stack wording | Keep the declaration being made separate from neighboring measurement, normalization, comparison, ontology, or bridge relations. | Continue through the declaration relation that changes this P2W move. |
| Work-facing, temporal, or result wording | Recover the concrete mechanism-position, method-position, bounded-transformation, temporal, planning, performed-work, or result-related relation. | Continue through the matching application; split one source phrase only when several relations are being made. |
| Another governed relation appears inside the source phrase | Preserve the cue as source material, but do not import its governing law into P2W. | Continue only through the relation that changes this P2W move; leave the other cue stopped until its governing relation is being made. |

#### E.18.1:4.5 - Return and refresh rule

P2W can reopen earlier applications without becoming a required work procedure. Reopen only the smallest application whose assumption changed:

| Changed assumption | Smallest reopened application |
|---|---|
| measurement value, unit, scale, reference plane, or transport relation | measurement, normalization, bridge, or comparison application |
| source record, source edition, source reference, or publication-use relation | work-relevant source restoration, publication-use, or refresh application |
| result artifact, telemetry, acceptance, done-state, or role-enactability record | result-related split plus the evidence named by value, measurement, quality, role, or refresh relation |
| method set, comparator, selector, retained set, or selected record | method-comparison, selector, retained-set, or selected-record application |
| problem-side statement or accepted carried distinction | problem-side correction in the problem-card application |

The earlier dated `U.Work` occurrence remains a dated occurrence. P2W may cite it during return, but the changed assumption determines which application is reopened.

#### E.18.1:4.6 - Relation selection aid

Use this aid after the carry-through record when several cues compete for the continuing FPF application. It names the relation family P2W must recover before another pattern can govern the claim; pattern names for those families are listed once in `E.18.1:12`.

| What the source phrase makes current | Relation to recover before continuation | Local P2W move |
|---|---|---|
| accepted problem-side distinction | accepted `ProblemCard@Context` material plus one unsettled next relation | State what is carried and what question remains. |
| preserved or lost structure, invariant, near-sameness, formal payoff, or formal stop condition | mathematical-lens use or `U.Signature(profile=FormalSubstrate)` declaration | Name preserved structure, lost structure, payoff, and stop condition. |
| postulate, observability, unit, plane, comparator, threshold, ontology edition, CHR edition, normalization, bridge, or measurement | the declaration or measurement-family relation being made | Write or cite only that relation. |
| mechanism position, method position, method candidate set, comparator, selector, retained set, or selected record | the mechanism, method, comparison, selector, retained-set, or selected-record relation being made | Keep these relation positions distinct and continue only through the recovered one. |
| bounded transformation, temporal aspect, dynamics episteme, or temporal supported-use claim | `A.3.4`, `C.27.TA`, `A.3.3`, or `C.27` relation according to the claim being made | Split one phrase when it carries several of these relations. |
| planning record, plan item, performed work, launch value, result artifact, telemetry, acceptance, measurement, refresh, or role enactability | `A.15.2 U.WorkPlan`, plan-item, dated `U.Work`, or the result-related relation being made | Write or cite the record being made; do not let generic result wording guide the next move. |
| structure, transformation-flow cue, diagram, scenario, view, graph expression, publication, module-interface, function, evidence-looking, gate-looking, or decision-looking wording | the relation named by value in the source phrase, or no continuation if none is recoverable | Use the material only as classification until the relation is recovered. |

#### E.18.1:4.7 - Lowering and reopen block

Use this block when the carry-through record cannot preserve and continue the stronger-looking source cue. P2W succeeds when it leaves one relation-governed move. If the move is not recoverable by value, lower the cue, stop, or reopen the smallest affected application.

| Claim family | Lowering or stop condition | Reopened or continuing relation |
|---|---|---|
| Problem-side material | No accepted `ProblemCard@Context`, or the accepted problem-side statement changes the carried distinction. | Stop before P2W begins, or return to the problem-side record named by value that changed. |
| First-principles, mathematical, formal, or declaration-stack claim | Preserved structure, lost structure, payoff, stop condition, declaration relation, measurement relation, normalization relation, bridge relation, or comparison relation cannot be named. | Lower to a reduced-use source cue; continue only after the recovered declaration, mathematical-lens, measurement, normalization, bridge, or comparison relation is being made. |
| Mechanism, method, selected-set, transformation, temporal, dynamics, planning, performed-work, or result claim | The source phrase blurs relation positions that change different P2W moves. | Split to the recovered relation and continue only through that relation. |
| Another governed relation is only signaled by a label, diagram, port, module-interface phrase, publication, view, approval word, readiness word, or wording phrase | The source material classifies a possible relation but does not name the relation being made. | Preserve the cue and stop local continuation until the governed relation is recoverable by value. |

#### E.18.1:4.8 - Replay and currentness record

Use this compact record after source restoration, changed measurement, changed problem-side material, FPF pattern change, or a use-found defect. The record keeps replay local: it says what changed, what still carries, what no longer carries, and which application reopens.

```text
P2W replay and currentness check:
  OriginalRecordRef:
  ChangedInput:
  ChangedAssumptionKind:
  StillCarried:
  NoLongerCarried:
  SmallestReopenedApplication:
  GoverningRelationChecked:
  CurrentnessResult:
  NextMove:
```

`ChangedAssumptionKind` names the assumption kind, such as measurement, unit, reference plane, source record, problem-side statement, method set, comparator, module-interface relation, publication-use relation, or FPF pattern change. `StillCarried` and `NoLongerCarried` prevent a source-currentness change from silently rewriting the whole carry-through slice. `SmallestReopenedApplication` keeps the repair local, and `NextMove` states whether to continue, stop, split, lower to a reduced-use cue, or return to the problem-side pattern.


---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "Principles-to-Work Transduction Path"
section_id: "E.18.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__005_solution.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "E.18.1 — Principles-to-Work Transduction Path"
  - "E.18.1:4 — Solution"
line_start: 66878
line_end: 67030
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
  - "carried distinction"
  - "carry-through record"
  - "first-principles cue"
  - "principles-to-work"
  - "result carry-through"
  - "return trigger"
  - "selected application"
  - "source-currentness"
  - "stop condition"
---

### E.18.1:4 - Solution

Use P2W as a declarative graph of admissible carry-through moves from an accepted `ProblemCard@Context` to accepted FPF applications. The graph is not a prescribed FPF-development workflow. It can describe or join project workflows only when the workflow is the EntityOfConcern of the TGA use being made: a `U.MethodDescription`, `U.WorkPlan`, `U.TransductionFlow`, or flow valuation over `U.TransductionGraph`. It shows what can be carried, split, written, stopped, or reopened after a problem-side result becomes useful for work.

#### E.18.1:4.0 - P2W declarative graph

The graph has eight recurring node classes. A concrete use can skip nodes, branch into several applications, split one source phrase into several records, stop with a reduced-use cue, or reopen an earlier node when measurement or source currentness changes.

| Node | Question answered | Output of the P2W move |
|---|---|---|
| `AcceptedProblemSideOutput` | What accepted problem-side material is being carried? | Problem-card reference plus carried distinction. |
| `NextFPFUseQuestion` | What is the next unsettled FPF kind or relation? | One question stated in FPF vocabulary. |
| `FirstPrinciplesLens` | What structure, invariant, loss, or payoff makes the next move worth formal treatment? | Preserved structure, lost structure, payoff, and stop condition. |
| `DeclarationStack` | Which `U.Signature(profile=FormalSubstrate)`, `PrincipleFrame`, ontology, CHR, measurement, normalization, or bridge relation is needed? | Declaration or reference to the declaration relation named by value. |
| `MechanismMethodCandidate` | Is the next work-facing issue mechanism meaning, mechanism-method stabilization, method selection, or retained-set handling? | Mechanism cue, comparison cue, selector cue, or retained-set cue. |
| `WorkPreparation` | Is a planning record, slot-filling plan item, feasibility note, evidence hook, or freshness request needed? | `U.WorkPlan`, PlanItem, or `SlotFillingsPlanItem` application. |
| `PerformedWorkAndResult` | Has dated `U.Work` occurred, and what result-related records appeared? | Work occurrence plus unpacked artifact, telemetry, acceptance, measurement, source, or role-enactability relation. |
| `ReturnAndRefresh` | Did measurement, source currentness, reference plane, or problem-side wording change an earlier assumption? | Return to the affected application with the changed relation named. |

Admissible edges are `carry`, `recover`, `write`, `split`, `stop`, and `return`. `Carry` preserves a distinction from the problem side. `Recover` names the FPF kind or relation. `Write` creates or amends the governed record. `Split` separates one source phrase into several applications. `Stop` preserves a reduced-use cue when no admissible continuation is available. `Return` reopens the smallest earlier application whose assumption changed.

#### E.18.1:4.1 - Carry-through record

For first-minute use, fill only `ProblemCardRef`, `CarriedDistinction`, `NextFPFUseQuestion`, and either `RecoveredFPFKindOrRelation` or `StopCondition`. Use the remaining fields only when the move continues, splits, writes a record, or returns after a changed assumption.

Use one filled record when applying P2W. It is the local work product of the pattern. Do not copy an empty form into project material; if a field cannot be filled with recovered claim content, state the stop condition or leave the field out.

```text
P2W carry-through record:
  ProblemCardRef: ProblemCard@Context PC-FAB-042, accepted for a cooling-fixture deformation problem.
  CarriedDistinction: the deformation is not one more tuning defect; the problem card identifies a conserved heat-flow structure that must survive method choice.
  NextFPFUseQuestion: does the team need mathematical-lens use or a `U.Signature(profile=FormalSubstrate)` declaration before method selection?
  P2WNode: FirstPrinciplesLens -> DeclarationStack.
  RecoveredFPFKindOrRelation: mathematical-lens use plus `U.Signature(profile=FormalSubstrate)` and `PrincipleFrame` declaration relation.
  SelectedApplication: `C.29` for preserved and lost structure; `A.6.0` for `U.Signature(profile=FormalSubstrate)` and `PrincipleFrame` when the declaration is written.
  WrittenRecordOrApplication: a short `U.Signature(profile=FormalSubstrate)` declaration naming the heat-flow invariant, the boundary conditions being preserved, the deformation factors left outside the model, and the payoff for later method comparison.
  NotCarried: no method is selected by this record.
  StopCondition: stop before method selection until comparator, measurement, and selected-set relations are named.
  ReturnTrigger: later result measurement shows that the planned interface constraint used the wrong reference plane.
  SourceCurrentnessCheck: source restoration and refresh reopen the measurement, normalization, planning, and method-comparison applications; the earlier U.Work occurrence is cited but not rewritten by P2W.
```

`ProblemCardRef` and `CarriedDistinction` locate the accepted problem-side material and the distinction being carried. `NextFPFUseQuestion`, `P2WNode`, and `RecoveredFPFKindOrRelation` keep the next FPF kind or relation explicit before the path continues. `SelectedApplication` and `WrittenRecordOrApplication` name what is actually used or written.

`NotCarried` is a compact field, not a place to repeat boundary doctrine from other governing patterns. It names only the local overread that would change this P2W move. `StopCondition`, `ReturnTrigger`, and `SourceCurrentnessCheck` keep stopping and reopening tied to a changed relation, measurement, source-currentness, or problem-side assumption.

This record shows the complete P2W mechanism: problem-side distinction, first-principles value, selected FPF application, written record, stop condition, and return after measurement and source-currentness change.

#### E.18.1:4.2 - Positive action spine

| Node reached | P2W action | Record or continuation |
|---|---|---|
| Accepted problem-side output | State what is carried from the problem card and what question under repair remains. | P2W carry-through record begins. |
| First-principles or mathematical cue | Name preserved structure, lost structure, payoff, and stop condition. | Mathematical-lens use or `U.Signature(profile=FormalSubstrate)` declaration. |
| Ontology, UTS, CHR, or `PrincipleFrame` cue | Order ontology, UTS, characteristic, measurement, and principle-frame declarations before downstream use. | Declaration-stack application. |
| Mechanism or method cue | Separate mechanism meaning from method selection and retained-set handling. | Mechanism, method-comparison, selector, or retained-set application. |
| Planning cue | Write or amend a planning record, plan item, evidence hook, freshness request, or planned constraint. | WorkPlanning application. |
| Dated performed `U.Work` | Record the work occurrence and relation to plan, gate, launch values, provenance, and later result records. | Performed-work application plus any separate entry or provenance relation. |
| Result phrase | Split the phrase into artifact, resource, launch-value, telemetry, acceptance, quality, done-state, feedback, measurement, parity, refresh, source, or role-enactability relation. | One or more result-related applications. |
| Changed measurement or source currentness | Return to the smallest earlier application whose assumption changed. | Measurement, normalization, source-restoration, refresh, planning, method-comparison, or problem-side correction. |

#### E.18.1:4.3 - Node use details

Problem-side input: P2W starts only from accepted problem-side material. The record carries the distinction that matters for the next move, not the whole problem-side pattern.

First-principles and declarations: mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, ontology, UTS, CHR, measurement, normalization, bridge, and `PrincipleFrame` material are handled as declaration-stack work. The P2W record names which declaration or neighboring relation is being written or cited, what structure is preserved, what is lost, and which downstream relation is still unsettled.

When mathematical wording points both to a formal declaration and to a mathematical lens, P2W does not decide by vocabulary. Use the slot discipline in `A.6.0:10a.1`: `A.6.0` owns `U.Signature(profile=FormalSubstrate)` declaration, `C.29` owns mathematical-lens use, `A.6.1` owns mechanism consumption or realization, and `E.18.1` owns only the carry-through cue and next-relation selection.
Mechanism and method: mechanism wording names operation algebra, law set, admissibility condition, effect realization, or mechanism-description need. Method wording names candidate sets, comparison, selector, retained-set, or selected-record need. P2W keeps the question visible until the method or mechanism application is actually used.

Planning and performed work: WorkPlanning writes planning records, plan items, evidence hooks, feasibility notes, freshness requests, and planned constraints. Performed work is a dated `U.Work` occurrence. P2W records which side of that boundary the carry-through record uses and which later result records have appeared.

Result carry-through: a result phrase is treated as a bundle of possible records. The P2W action is to unpack it before it guides any next move.

Graph, publication, function, interface, and integration cues: a graph or publication can help classify the P2W move. A functional description, interface constraint, protocol, port, connection, resource limit, or integration statement can shape the next relation. The P2W record names the recovered relation and then uses the relation selection aid in `E.18.1:4.6`.

#### E.18.1:4.4 - Boundary and relation discipline

P2W is not a catalogue of boundary doctrines from other governing patterns. It has one local boundary rule: carry only the distinction accepted on the problem side, recover the next FPF kind or relation, and stop everything else as named source material until that relation is being made.

| Source pressure | Local P2W decision | Admissible continuation |
|---|---|---|
| Problem-side material | Carry only the accepted distinction and the next FPF-use question. | Continue when the next FPF kind or relation is named; otherwise stop before P2W begins. |
| First-principles or mathematical wording | State preserved structure, lost structure, payoff, and stop condition. | Continue as mathematical-lens use through `C.29`, or as a `U.Signature(profile=FormalSubstrate)` declaration through `A.6.0`, only when those relations are being made. |
| Declaration-stack wording | Keep `PrincipleFrame`, ontology, UTS, CHR, measurement, normalization, bridge, and comparison declarations separate. | Continue through the declaration whose relation changes the P2W move being made. |
| Mechanism, method, planning, work, or result wording | Recover the concrete mechanism, selection, planning, performed-work, or result-related relation. | Continue through the matching work-facing application; split one source phrase when several relations are being made. |
| Evidence, assurance, gate, release, decision, publication, architecture, interface, function, or wording-use wording | Preserve the cue without importing law from the governing pattern for that relation into P2W. | Continue only through the relation that changes the P2W move being made; leave the rest as stopped cues. |

#### E.18.1:4.5 - Return and refresh rule

P2W can reopen earlier work without becoming a required work procedure. Reopen only the smallest application whose assumption changed:

| Changed assumption | Smallest reopened application |
|---|---|
| measurement value, unit, scale, reference plane, or transport relation | measurement, normalization, bridge, or comparison application |
| source record, source edition, source reference, or publication-use relation | work-relevant source restoration, publication-use, or refresh application |
| result artifact, telemetry, acceptance, done-state, or role-enactability record | result-related split plus the evidence named by value, measurement, quality, role, or refresh relation |
| method set, comparator, selector, retained set, or selected record | method-comparison, selector, retained-set, or selected-record application |
| problem-side statement or accepted carried distinction | problem-side correction in the problem-card application |

The earlier dated `U.Work` occurrence remains a dated occurrence. P2W may cite it during return, but the changed assumption determines which application is reopened.

#### E.18.1:4.6 - Relation selection aid

Use this aid after the carry-through record when several cues compete for the continuing FPF application. It names the relation family P2W must recover before another pattern can carry the claim.

| Cue family | Relation to recover before continuation | Local P2W action |
|---|---|---|
| accepted problem-side output | accepted `ProblemCard@Context` material plus one unsettled next relation | State what is carried and what question remains. |
| first-principles or mathematical wording | mathematical-lens use, near-sameness condition, or `U.Signature(profile=FormalSubstrate)` declaration | Name preserved structure, lost structure, payoff, and stop condition. |
| postulate or observability wording | `PrincipleFrame`, ontology, UTS, CHR, measurement, normalization, bridge, comparison, or threshold declaration | Write or cite only the declaration relation that changes the P2W move being made. |
| mechanism or method wording | mechanism law, mechanism-method stabilization, candidate set, comparator, selector, retained set, or selected record | Keep mechanism meaning distinct from method selection and set return. |
| planning or performed-work wording | `U.WorkPlan`, PlanItem, `SlotFillingsPlanItem`, dated `U.Work`, launch value, gate, release, or provenance relation | Write or cite the work-family record that is actually being made. |
| result wording | artifact, telemetry, acceptance, done-state, feedback, measurement, parity, source, quality-evaluation, or role-enactability relation | Split generic result wording before it guides the next move. |
| evidence, assurance, gate, release, decision, publication, architecture, interface, function, or wording-use wording | the relation named by value carried by the source phrase | Preserve the cue, recover the relation, and stop any relation not used by this P2W move. |
| graph, flow, diagram, scenario, view, or publication wording | graph law, path note, flow valuation, description episteme, publication face, or work occurrence | Use the source as classification material; do not let the artifact type select the next relation by itself. |

Pattern names for these relation families are listed once in `E.18.1:12`.

#### E.18.1:4.7 - Lowering and reopen block

Use this block when the carry-through record cannot carry the stronger-looking source cue. P2W succeeds when it leaves one admissible move. If the move is not recoverable by value, lower the cue, stop, or reopen the smallest affected application.

| Claim family | Lowering or stop condition | Reopen or continue target |
|---|---|---|
| Problem-side material | No accepted `ProblemCard@Context`, or the accepted problem-side statement changes the carried distinction. | Stop before P2W begins, or return to the problem-side record named by value that changed. |
| First-principles, mathematical, or formal claim | Preserved structure, lost structure, payoff, or stop condition cannot be named. | Lower to a reduced-use source cue; continue only after mathematical-lens use or `U.Signature(profile=FormalSubstrate)` declaration is being made. |
| Declaration-stack claim | Postulates, CHR observability, units, planes, comparators, thresholds, ontology editions, or CHR editions are merged into one container. | Split the declaration-stack relations; reopen the declaration, measurement, normalization, bridge, ontology, or CHR application named by value that changed. |
| Mechanism, method, or selected-set claim | Mechanism meaning, candidate set, comparison relation, selector, retained set, or selected record cannot be separated. | Stop before method choice; continue only for the recovered relation. |
| Planning or performed-work claim | Planned constraint, plan item, dated `U.Work`, launch value, actual, substitution, variance, telemetry, or result record is blurred. | Split planning, plan-item, performed-work, and source-restoration relations; do not rewrite the earlier dated `U.Work` occurrence unless the work record itself changed. |
| Result or source claim | A generic result phrase or source cue cannot recover artifact, telemetry, acceptance, measurement, refresh, evidence, role-enactability, architecture, or source-reference relation. | Treat the phrase as source material for restoration; continue only through the result-related or source-restoration relation named by value recovered. |
| Evidence, gate, assurance, conformance, release, entry, or decision claim | The source gives only a label, signal, color, approval word, or readiness phrase. | Preserve the cue and stop local authority; continue only when the governed relation is being made. |
| Graph, interface, architecture-description, publication, or wording-use claim | A diagram, port, interface phrase, architecture view, publication, or wording phrase does not name the relation it carries. | Use it as classification material; continue only after relation recovery. |

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

`ChangedAssumptionKind` names the assumption kind, such as measurement, unit, reference plane, source record, problem-side statement, method set, comparator, interface relation, publication-use relation, or FPF pattern change. `StillCarried` and `NoLongerCarried` prevent a source-currentness change from silently rewriting the whole path. `SmallestReopenedApplication` keeps the repair local, and `NextMove` states whether to continue, stop, split, lower to a reduced-use cue, or return to the problem-side pattern.


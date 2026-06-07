---
chunk_kind: "parent"
pattern_id: "E.18.1"
pattern_title: "Principles-to-Work Transduction Path"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/E.18.1.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "E.18.1 — Principles-to-Work Transduction Path"
line_start: 66424
line_end: 66765
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

## E.18.1 - Principles-to-Work Transduction Path

> **Tech-name:** `PrinciplesToWorkTransductionPath`
> **Plain-name:** principles-to-work carry-through path
> **Type:** Architectural pattern (E)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part E -> E.18 child pattern
> **Builds on:** `E.18` Transduction Graph Architecture, `C.22.2` ProblemCard@Context, `A.6.0` U.Signature, `A.6.1` U.Mechanism, the A.15 work family, `C.29`, `C.16`, `F.9`, `A.20`, `A.21`, and Part G comparison, selection, and refresh patterns.
> **Purpose:** carry an accepted problem-side output toward the next exact FPF kind, relation, record, or pattern application while preserving the useful first-principles move.

### E.18.1:1 - Problem frame

Use this pattern when an accepted `ProblemCard@Context` is ready enough to guide work, but the next FPF use is not yet settled. The practitioner has a live carry-through question: which problem-side distinction can be carried into the next exact FPF relation or record?

The primary EntityOfConcern is the P2W carry-through relation: the relation between accepted problem-side material and the next admissible FPF use. P2W keeps first-principles material usable by turning it into one recoverable next move instead of letting an inspiring explanation become an all-purpose project claim.

#### E.18.1:1.1 - Use this when

- an accepted `ProblemCard@Context` names a working problem and the team needs a disciplined next move toward method, planning, performed work, or result interpretation;
- a first-principles, `U.Signature(profile=FormalSubstrate)`, `PrincipleFrame`, mechanism, method, WorkPlanning, performed-work, result-record, or source-currentness cue is present, but the FPF kind or relation to use next is still unsettled;
- a TGA graph, P2W path, flow diagram, principle scheme, scenario, functional description, or source publication helps the team think, while the live next move must still be recovered as a current FPF kind or relation;
- a result artifact, telemetry line, acceptance record, quality-evaluation record, done-state update, feedback pin, or integration claim needs to be unpacked before it can guide the next move.

#### E.18.1:1.2 - What goes wrong if missed

The team jumps from a convincing problem-side formulation into downstream language without naming the FPF relation being used. The work then looks connected to first principles, but the next record is unclear, the result phrase becomes too broad, and measurement or source-currentness changes have no honest return path.

#### E.18.1:1.3 - What this buys

The practitioner gets one admissible next move: write a P2W carry-through record, recover the next FPF kind or relation, write or use the governed record, stop with a reduced-use cue, or return to the earlier application whose assumption changed. The payoff is practical: first-principles thinking remains action-guiding without becoming a hidden project authorization.

#### E.18.1:1.4 - Not this pattern when

- there is no accepted problem-side record; use `C.22.2` or the exact problem-side pattern first;
- the live FPF kind, relation, and record to write are already settled; use that pattern directly and do not add a P2W layer;
- the requested work product is a local project procedure, schedule, or work-management method; use the relevant work, planning, method, gate, or operational-management pattern;
- the requested record or claim is an evidence case, assurance case, gate record, decision record, architecture description, publication-use claim, or wording-use repair; use the recovered relation and its governing pattern directly.

### E.18.1:2 - Problem

First-principles work often becomes useful exactly when a problem-side formulation is ready to move toward work. The accepted problem card may expose an invariant, mathematical lens, functional role, mechanism candidate, method family, planning constraint, result cue, or changed measurement assumption. Without P2W, that useful material is either overcompressed into "we have a solution" or scattered across several related FPF patterns before the working distinction is preserved.

P2W solves a carry-through problem. It takes accepted problem-side material, states the distinction it can carry, selects the next admissible FPF node, and records what was written, stopped, split, or reopened. The pattern succeeds only when a practitioner can replay the move from source problem to next record without importing the law of another pattern into P2W.

### E.18.1:3 - Forces

| Force | What P2W must preserve | Pressure to manage |
|---|---|---|
| First-principles usefulness | A strong problem-side insight may guide method, planning, work, or result interpretation. | The insight is tempting to treat as a completed downstream claim. |
| Governing-kind precision | The next FPF kind or relation must be recoverable before the path continues. | Path words, diagrams, and sources can look sufficient without a record to write. |
| Practical readability | First use needs a compact record and a quick next action. | Too much boundary prose can hide the actual P2W move. |
| Non-linear use | P2W may skip, branch, split, stop, or reopen nodes. | A readable graph can be mistaken for a required project sequence. |
| Result usefulness | Result phrases often point to artifacts, telemetry, acceptance, measurement, refresh, or role enactability. | One broad result word can hide several different records. |
| Neighbor economy | Neighboring patterns keep their own law. | Repeating their non-use doctrine inside P2W creates content fanout. |

### E.18.1:4 - Solution

Use P2W as a declarative graph of admissible carry-through moves from an accepted `ProblemCard@Context` to current FPF applications. The graph is not a prescribed FPF-development workflow. It can describe or join project workflows only when the workflow is the EntityOfConcern of the current TGA use: a `U.MethodDescription`, `U.WorkPlan`, `U.TransductionFlow`, or flow valuation over `U.TransductionGraph`. It shows what can be carried, split, written, stopped, or reopened after a problem-side result becomes useful for work.

#### E.18.1:4.0 - P2W declarative graph

The graph has eight recurring node classes. A concrete use can skip nodes, branch into several applications, split one source phrase into several records, stop with a reduced-use cue, or reopen an earlier node when measurement or source currentness changes.

| Node | Question answered | Output of the P2W move |
|---|---|---|
| `AcceptedProblemSideOutput` | What accepted problem-side material is being carried? | Problem-card reference plus carried distinction. |
| `LiveP2WQuestion` | What is the next unsettled FPF kind or relation? | One question stated in FPF vocabulary. |
| `FirstPrinciplesLens` | What structure, invariant, loss, or payoff makes the next move worth formal treatment? | Preserved structure, lost structure, payoff, and stop condition. |
| `DeclarationStack` | Which `U.Signature(profile=FormalSubstrate)`, `PrincipleFrame`, ontology, CHR, measurement, normalization, or bridge relation is needed? | Declaration or reference to the exact declaration relation. |
| `MechanismMethodCandidate` | Is the next work-facing issue mechanism meaning, mechanism-method stabilization, method selection, or retained-set handling? | Mechanism cue, comparison cue, selector cue, or retained-set cue. |
| `WorkPreparation` | Is a planning record, slot-filling plan item, feasibility note, evidence hook, or freshness request needed? | `U.WorkPlan`, PlanItem, or `SlotFillingsPlanItem` application. |
| `PerformedWorkAndResult` | Has dated `U.Work` occurred, and what result-related records appeared? | Work occurrence plus unpacked artifact, telemetry, acceptance, measurement, source, or role-enactability relation. |
| `ReturnAndRefresh` | Did measurement, source currentness, reference plane, or problem-side wording change an earlier assumption? | Return to the affected application with the changed relation named. |

Admissible edges are `carry`, `recover`, `write`, `split`, `stop`, and `return`. `Carry` preserves a distinction from the problem side. `Recover` names the FPF kind or relation. `Write` creates or amends the governed record. `Split` separates one source phrase into several applications. `Stop` preserves a reduced-use cue when no admissible continuation is available. `Return` reopens the smallest earlier application whose assumption changed.

#### E.18.1:4.1 - Carry-through record

For first-minute use, fill only `ProblemCardRef`, `CarriedDistinction`, `LiveP2WQuestion`, and either `RecoveredFPFKindOrRelation` or `StopCondition`. Use the remaining fields only when the move continues, splits, writes a record, or returns after a changed assumption.

Use one filled record when applying P2W. It is the local work product of the pattern. Do not copy an empty form into project material; if a field cannot be filled with live content, state the stop condition or leave the field out.

```text
P2W carry-through record:
  ProblemCardRef: ProblemCard@Context PC-FAB-042, accepted for a cooling-fixture deformation problem.
  CarriedDistinction: the deformation is not one more tuning defect; the problem card identifies a conserved heat-flow structure that must survive method choice.
  LiveP2WQuestion: does the team need mathematical-lens use or a `U.Signature(profile=FormalSubstrate)` declaration before method selection?
  CurrentNode: FirstPrinciplesLens -> DeclarationStack.
  RecoveredFPFKindOrRelation: mathematical-lens use plus `U.Signature(profile=FormalSubstrate)` and `PrincipleFrame` declaration relation.
  SelectedApplication: `C.29` for preserved and lost structure; `A.6.0` for `U.Signature(profile=FormalSubstrate)` and `PrincipleFrame` when the declaration is written.
  WrittenRecordOrApplication: a short `U.Signature(profile=FormalSubstrate)` declaration naming the heat-flow invariant, the boundary conditions being preserved, the deformation factors left outside the model, and the payoff for later method comparison.
  NotCarried: no method is selected by this record.
  StopCondition: stop before method selection until comparator, measurement, and selected-set relations are named.
  ReturnTrigger: later result measurement shows that the planned interface constraint used the wrong reference plane.
  SourceCurrentnessCheck: source restoration and refresh reopen the measurement, normalization, planning, and method-comparison applications; the earlier U.Work occurrence is cited but not rewritten by P2W.
```

`ProblemCardRef` and `CarriedDistinction` locate the accepted problem-side material and the distinction being carried. `LiveP2WQuestion`, `CurrentNode`, and `RecoveredFPFKindOrRelation` keep the next FPF kind or relation explicit before the path continues. `SelectedApplication` and `WrittenRecordOrApplication` name what is actually used or written.

`NotCarried` is a compact field, not a place to repeat boundary doctrine from other governing patterns. It names only the local overread that would change this P2W move. `StopCondition`, `ReturnTrigger`, and `SourceCurrentnessCheck` keep stopping and reopening tied to a changed relation, measurement, source-currentness, or problem-side assumption.

This record shows the complete P2W mechanism: problem-side distinction, first-principles value, selected FPF application, written record, stop condition, and return after measurement and source-currentness change.

#### E.18.1:4.2 - Positive action spine

| Node reached | P2W action | Record or continuation |
|---|---|---|
| Accepted problem-side output | State what is carried from the problem card and what live question remains. | P2W carry-through record begins. |
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

Planning and performed work: WorkPlanning writes planning records, plan items, evidence hooks, feasibility notes, freshness requests, and planned constraints. Performed work is a dated `U.Work` occurrence. P2W records which side of that boundary is active and which later result records have appeared.

Result carry-through: a result phrase is treated as a bundle of possible records. The P2W action is to unpack it before it guides any next move.

Graph, publication, function, interface, and integration cues: a graph or publication can help classify the P2W move. A functional description, interface constraint, protocol, port, connection, resource limit, or integration statement can shape the next relation. The P2W record names the recovered relation and then uses the relation selection aid in `E.18.1:4.6`.

#### E.18.1:4.4 - Boundary and relation discipline

P2W is not a catalogue of boundary doctrines from other governing patterns. It has one local boundary rule: carry only the distinction accepted on the problem side, recover the next FPF kind or relation, and stop everything else as named source material until its own relation is live.

| Source pressure | Local P2W decision | Admissible continuation |
|---|---|---|
| Problem-side material | Carry only the accepted distinction and the live P2W question. | Continue when the next FPF kind or relation is named; otherwise stop before P2W begins. |
| First-principles or mathematical wording | State preserved structure, lost structure, payoff, and stop condition. | Continue as mathematical-lens use through `C.29`, or as a `U.Signature(profile=FormalSubstrate)` declaration through `A.6.0`, only when those relations are live. |
| Declaration-stack wording | Keep `PrincipleFrame`, ontology, UTS, CHR, measurement, normalization, bridge, and comparison declarations separate. | Continue through the declaration whose relation changes the current move. |
| Mechanism, method, planning, work, or result wording | Recover the concrete mechanism, selection, planning, performed-work, or result-related relation. | Continue through the matching work-facing application; split one source phrase when several relations are live. |
| Evidence, assurance, gate, release, decision, publication, architecture, interface, function, or wording-use wording | Preserve the cue without importing law from the governing pattern for that relation into P2W. | Continue only through the relation that changes the current P2W move; leave the rest as stopped cues. |

#### E.18.1:4.5 - Return and refresh rule

P2W can reopen earlier work without becoming a required work procedure. Reopen only the smallest application whose assumption changed:

| Changed assumption | Smallest reopened application |
|---|---|
| measurement value, unit, scale, reference plane, or transport relation | measurement, normalization, bridge, or comparison application |
| source record, source edition, source reference, or publication-use relation | work-relevant source restoration, publication-use, or refresh application |
| result artifact, telemetry, acceptance, done-state, or role-enactability record | result-related split plus the exact evidence, measurement, quality, role, or refresh relation |
| method set, comparator, selector, retained set, or selected record | method-comparison, selector, retained-set, or selected-record application |
| problem-side statement or accepted carried distinction | problem-side correction in the problem-card application |

The earlier dated `U.Work` occurrence remains a dated occurrence. P2W may cite it during return, but the changed assumption determines which application is reopened.

#### E.18.1:4.6 - Relation selection aid

Use this aid after the carry-through record when several cues compete for the continuing FPF application. It names the relation family P2W must recover before another pattern can carry the claim.

| Cue family | Relation to recover before continuation | Local P2W action |
|---|---|---|
| accepted problem-side output | accepted `ProblemCard@Context` material plus one live next relation | State what is carried and what question remains. |
| first-principles or mathematical wording | mathematical-lens use, near-sameness condition, or `U.Signature(profile=FormalSubstrate)` declaration | Name preserved structure, lost structure, payoff, and stop condition. |
| postulate or observability wording | `PrincipleFrame`, ontology, UTS, CHR, measurement, normalization, bridge, comparison, or threshold declaration | Write or cite only the declaration relation that changes the current move. |
| mechanism or method wording | mechanism law, mechanism-method stabilization, candidate set, comparator, selector, retained set, or selected record | Keep mechanism meaning distinct from method selection and set return. |
| planning or performed-work wording | `U.WorkPlan`, PlanItem, `SlotFillingsPlanItem`, dated `U.Work`, launch value, gate, release, or provenance relation | Write or cite the work-family record that is actually live. |
| result wording | artifact, telemetry, acceptance, done-state, feedback, measurement, parity, source, quality-evaluation, or role-enactability relation | Split generic result wording before it guides the next move. |
| evidence, assurance, gate, release, decision, publication, architecture, interface, function, or wording-use wording | the exact relation carried by the source phrase | Preserve the cue, recover the relation, and stop any relation not used by this P2W move. |
| graph, flow, diagram, scenario, view, or publication wording | graph law, path note, flow valuation, description episteme, publication face, or work occurrence | Use the source as classification material; do not let the artifact type select the next relation by itself. |

Pattern names for these relation families are listed once in `E.18.1:12`.

#### E.18.1:4.7 - Lowering and reopen block

Use this block when the carry-through record cannot carry the stronger-looking source cue. P2W succeeds when it leaves one admissible move. If the exact move is not recoverable, lower the cue, stop, or reopen the smallest affected application.

| Claim family | Lowering or stop condition | Reopen or continue target |
|---|---|---|
| Problem-side material | No accepted `ProblemCard@Context`, or the accepted problem-side statement changes the carried distinction. | Stop before P2W begins, or return to the exact problem-side record that changed. |
| First-principles, mathematical, or formal claim | Preserved structure, lost structure, payoff, or stop condition cannot be named. | Lower to a reduced-use source cue; continue only after mathematical-lens use or `U.Signature(profile=FormalSubstrate)` declaration is live. |
| Declaration-stack claim | Postulates, CHR observability, units, planes, comparators, thresholds, ontology editions, or CHR editions are merged into one container. | Split the declaration-stack relations; reopen the exact declaration, measurement, normalization, bridge, ontology, or CHR application that changed. |
| Mechanism, method, or selected-set claim | Mechanism meaning, candidate set, comparison relation, selector, retained set, or selected record cannot be separated. | Stop before method choice; continue only for the recovered relation. |
| Planning or performed-work claim | Planned constraint, plan item, dated `U.Work`, launch value, actual, substitution, variance, telemetry, or result record is blurred. | Split planning, plan-item, performed-work, and source-restoration relations; do not rewrite the earlier dated `U.Work` occurrence unless the work record itself changed. |
| Result or source claim | A generic result phrase or source cue cannot recover artifact, telemetry, acceptance, measurement, refresh, evidence, role-enactability, architecture, or source-reference relation. | Treat the phrase as source material for restoration; continue only through the exact result-related or source-restoration relation recovered. |
| Evidence, gate, assurance, conformance, release, entry, or decision claim | The source gives only a label, signal, color, approval word, or readiness phrase. | Preserve the cue and stop local authority; continue only when the governed relation is live. |
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

### E.18.1:5 - Archetypal Grounding

`E.18.1` is grounded in a simple System and Episteme contrast. In System-facing work, accepted problem-side material may lead toward method choice, planning, performed work, result records, and result measurement. In Episteme-facing work, the same material may lead toward a `U.Signature(profile=FormalSubstrate)` declaration, mathematical-lens use, description, publication, evidence, or gate-related claims. The P2W move asks one question in both cases: which FPF kind or relation can carry the next live claim?

| Archetype | System-side grounding | Episteme-side grounding |
|---|---|---|
| Tell | A manufacturing team accepts a problem card showing that a fabrication issue is caused by a missing functional constraint. | A research team accepts a problem card showing that two descriptions may be almost the same only under a declared `U.Signature(profile=FormalSubstrate)`. |
| Show without P2W | The team treats the principle scheme as method selection, work plan, performed work, and acceptance evidence at once. | The team treats mathematical equivalence as real-world identity, measurement validation, evidence, and decision authority. |
| Show with P2W | The team writes a carry-through record, separates method comparison from WorkPlanning, records dated `U.Work`, and unpacks result records. | The team writes a carry-through record, separates mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, bridge, measurement, evidence, and provenance relations, and keeps equivalence bounded by the declared formal relation. |

#### E.18.1:5.1 - Worked slices

1. **Thin first-principles start.** An accepted `ProblemCard@Context` says the problem is not one more local tuning task because a conserved structure is being ignored. P2W records the carried distinction, recovers mathematical-lens use and `U.Signature(profile=FormalSubstrate)` declaration only if needed, and stops before method selection until comparator, measurement, and selected-set relations are named.

2. **Planning from selected enough method.** A method family is selected enough for planning. P2W carries the planning relation; the plan records planned constraints, planned fillers, evidence-reference hooks, and freshness requests.

3. **Performed work after planning.** A dated work occurrence is live. P2W carries the performed-work relation and records which gate, release, provenance, or launch-value relation is separate from the occurrence.

4. **Result interpretation without generic result.** A source says the work result proves that the approach worked. P2W unpacks artifact, telemetry, measurement, evidence, acceptance, quality-evaluation, refresh, and role-enactability candidates before any one of them guides the next move.

5. **Functional explanatory order.** A source diagram places `U.Signature(profile=FormalSubstrate)`, principle frame, mechanism, normalization, method selection, planning, performed work, and result measurement in one readable order. P2W uses the diagram to classify applications while keeping material time and performed-work chronology with their own patterns.

6. **Interface split before P2W use.** A source says a port-throughput limit makes a solution feasible after integration. P2W first splits the phrase: module-interface relation (`A.6.M`), flow or throughput relation (`E.18` or `A.6.F` when function is live), WorkPlan constraint (`A.15.2`), performed-work actual (`A.15.1`), evidence or gate claim (`A.10`, `G.6`, `A.20`, or `A.21`), or architecture and structural-view claim (`C.30` family). The carry-through record writes only the relation that changes the current move and leaves the other readings as stopped cues.

7. **Result measurement returns to planning.** A performed `U.Work` occurrence produced telemetry and an artifact. Later measurement shows that the planned interface constraint was interpreted against the wrong reference plane. P2W splits measurement, reference-plane repair, source restoration, refresh, planning revision, and method-comparison claims. If the original `ProblemCard@Context` no longer states the right problem, the problem-side correction returns to the problem-side pattern.

#### E.18.1:5.2 - Additional worked situations

| Situation | P2W move | What changes |
|---|---|---|
| First-minute use | A practitioner has only an accepted `ProblemCard@Context` and the sentence "the cooling fixture violates the heat-flow invariant." Fill `ProblemCardRef`, `CarriedDistinction`, `LiveP2WQuestion`, and `RecoveredFPFKindOrRelation` or `StopCondition`. | The next action becomes a `C.29` and `A.6.0` application, not method selection or evidence writing. |
| Diagram and approval note in the same source | The same source contains a diagram, a test photo, and a manager note saying "approved." Keep P2W focused on the distinction carried from the problem-side result. | Diagram, evidence-looking material, and gate-looking material are separated by relation recovery; the P2W record keeps only the carried distinction and next relation. |
| Principle story without accepted problem-side material | A source has an inspiring principle story but no accepted `ProblemCard@Context`. | P2W stops before it begins; the material remains a reduced-use cue until `C.22.2` or the exact problem-side pattern accepts problem-side material. |
| Acceptance label hides wrong measurement | A dashboard shows a green acceptance label, but the measurement used the wrong reference plane. | Acceptance color does not guide the next move; P2W returns to measurement, normalization, source restoration, planning, and method comparison. |
| Changed unit after source restoration | Later source restoration changes only the unit and reference plane used by the planning constraint. | P2W reopens the smallest affected applications; the earlier dated `U.Work` occurrence is cited, not rewritten. |
| Near-sameness under a formal declaration | A mathematical near-sameness claim preserves heat-flow structure but loses deformation factors outside the model. | P2W uses `C.29` for mathematical-lens use and `A.6.0` for `U.Signature(profile=FormalSubstrate)`, names preserved and lost structure, and prevents the lens from settling empirical truth or work authorization. |
| FPF relation law changes after a P2W record | A governing FPF pattern changes the boundary for architecture-description, evidence, or source-restoration use. Fill the replay and currentness check: changed law, still-carried distinction, no-longer-carried cue, smallest reopened application, and next move. | The earlier carry-through record is replayed rather than trusted by age; only the affected architecture-description, evidence, source-restoration, or P2W field changes. |
| Relation selection would over-select from one phrase | A source says "the new port contract proves integration readiness." P2W splits module-interface relation, flow relation, performed-work actual, evidence cue, gate cue, and architecture-description cue. | Only the relation that changes the current move is written; the remaining readings stop as named cues until their governed relations are live. |
| Formal claim loses payoff | A `U.Signature(profile=FormalSubstrate)` declaration preserves a neat invariant, but no practical payoff or downstream stop condition can be stated for the accepted problem-side material. | The mathematical phrase lowers to a reduced-use cue; P2W does not open method selection, evidence, gate, or work planning from mathematical prestige alone. |
| Result source becomes stale | A result-looking source is later replaced by a fresher source with a different artifact reference and measurement reference. | P2W uses `A.15.4`-style source restoration before result carry-through; stale result wording cannot continue as evidence, acceptance, or quality evaluation. |

#### E.18.1:5.3 - Pilot examples for coupled development and application flows

The old TGA assignment supplied a broad example bank. Use these pilots as grounding checks, not as old terminology to import. They exercise the same common shape: one graph can join several transduction flows, one flow may develop or select a usable product, another flow may apply it, and an evaluation or refresh flow may return to the smallest affected development or application locus. The joined graph does not merge the flow objects, `DesignRunTag` boundaries, evidence, gates, work occurrences, or the relation position that the carried object fills inside each flow. Use each pilot to check whether the current P2W use can name the joined flows, the carried object's flow-local relation position, the `DesignRunTag` boundary, and the smallest reopened slice.

| Pilot | Current P2W use | What it tests |
|---|---|---|
| Coffee service STF | An accepted service-quality problem carries heat or mass-balance structure through `U.Signature(profile=FormalSubstrate)`, declaration-stack, mechanism, normalization, method-selection, WorkPlanning, dated `U.Work`, telemetry, measurement, and refresh relations. | Positive whole-chain readability, freshness, set-return selection, launch values only in performed work, and path-local refresh. |
| Compiler design and run | Toolchain construction, compiler use, and product execution are separate applications; design and run changes pass through current gate and work relations. | `DesignRunTag`, launch gate, reproducible build currentness and source currentness, and no collapse of build, run, and product work. |
| TAMP and MPC robotics | Selection and WorkPlanning may iterate under a declared progress or budget condition before performed work. | Branching and cycle use without imposing one mandatory workflow, and no launch-value binding before performed work. |
| AutoML and QD | Method selection returns a Pareto, QD, front, or archive set under comparator and descriptor editions, not a hidden scalar winner. | Set-return discipline, comparator currentness, no hidden scalarization, and retained-set refresh. |
| Freshness or material-transport case | Work planning and execution depend on freshness windows, transport relations, units, reference planes, and source-currentness. | No implicit `latest`, no unbridged unit or plane comparison, and smallest affected refresh. |
| Integration under interface constraints | After assembly, a result phrase may mean role-enactability under interface constraints, evidence, gate, architecture, function, or work relation. | Result carry-through is not artifact-only or telemetry-only; interface and integration wording must recover the exact current relation. |
| Tool-product-use chain | A design-tagged flow makes a tool; a later run or use flow uses the tool to make a chair; another flow uses the chair as context for writing a text. | One graph can unite all flows, but the same carried object may fill a run-result position in one flow and a design-side input, tool, context, or constraint position in another. The relation-position shift is explicit, tied to the current flow relation and any live `DesignRunTag`, and does not change the object's kind by wording. |
| FPF pattern-development / self-evolving specification | A development flow creates or repairs a pattern, specification, or process description through drafting, quality evaluation, publication projection, and admitted publication; a later use flow applies that product to its own `EntityOfConcern`; a defect found in use returns to the smallest development slice for repair. | Development, application, and evaluation flows are joined by transfer and return relations while keeping objects and `DesignRunTag` boundaries separate; evaluation records or use-found evidence change the product through edits to the smallest development slice, not by entering the used publication's practitioner-facing prose. |

### E.18.1:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Ontological and epistemic**, **Prag**, **Did**. Scope: **accepted problem-side output moving toward FPF applications**.

- **Governance bias (Gov):** permission, gate, release, assurance, and decision cues are preserved only as local cues until the relevant FPF relation is recovered.
- **Architectural bias (Arch):** diagrams, selected structures, and interface language help classify the next move; they do not displace the P2W carry-through relation.
- **Ontological and epistemic bias:** `U.Signature(profile=FormalSubstrate)`, near-sameness, source publication, and evidence-looking language are turned into recovered FPF kinds and relations.
- **Pragmatic bias (Prag):** the graph is useful for action without becoming a required project procedure.
- **Didactic bias (Did):** the positive graph and filled record come before the boundary table, so precision does not bury the working move.

### E.18.1:7 - Conformance Checklist

- `CC-E18.1-1` The P2W use starts from an accepted `ProblemCard@Context` or stops before P2W begins.
- `CC-E18.1-2` The carry-through record states `ProblemCardRef`, `CarriedDistinction`, `LiveP2WQuestion`, `RecoveredFPFKindOrRelation`, `SelectedApplication`, `WrittenRecordOrApplication`, `NotCarried`, `StopCondition`, `ReturnTrigger`, and `SourceCurrentnessCheck`.
- `CC-E18.1-3` The positive graph is recoverable: accepted problem-side output, live question, first-principles lens, declaration stack, mechanism or method, planning, performed work, result records, and return or refresh.
- `CC-E18.1-4` One source phrase may split into several FPF applications; the record does not compress them into one generic token.
- `CC-E18.1-5` Result wording is unpacked into concrete result-related relations; a generic `WorkResult` kind is not admitted.
- `CC-E18.1-6` `PrincipleFrame` material keeps postulates and CHR observability distinct from units, planes, comparators, thresholds, ontology editions, CHR editions, plans, work, evidence, and gates.
- `CC-E18.1-7` Measurement, source currentness, reference-plane, method-set, comparator, or problem-side changes return to the smallest affected application.
- `CC-E18.1-8` Non-P2W governing law appears only as a recovered relation in `E.18.1:4.6` and as a pattern list in Relations, not as repeated local doctrine.
- `CC-E18.1-9` Local boundary wording remains only where it names a near-miss that changes the next P2W action.
- `CC-E18.1-10` The pattern leaves one useful admissible action: write the carry-through record, write or use the governed record, split a source phrase, stop with a reduced-use cue, or return to a changed application.
- `CC-E18.1-11` Archetypal grounding can replay at least one coupled-flow pilot from `E.18.1:5.3`; the pilot joins development, application, evaluation, and repair flows in one graph while keeping their objects, flow-local relation positions, `DesignRunTag` boundaries, and evidence distinct. The self-evolving-spec pilot keeps development-flow or use-found evidence outside the used pattern, specification, or process description.
- `CC-E18.1-12` Every carried claim family can be lowered, stopped, split, or reopened through `E.18.1:4.7`; a source cue that cannot name the recovered FPF kind or relation remains a reduced-use cue.
- `CC-E18.1-13` Every replay after changed source, measurement, problem-side material, or FPF relation law names the changed assumption kind, what is still carried, what is no longer carried, the smallest reopened application, the governing relation checked, and the next move.

### E.18.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Boundary fanout.** The pattern repeats long lists of what P2W is not. | Keep relation discipline in `E.18.1:4.4`; make local sections state the next P2W action. |
| **Path-as-procedure.** The graph is read as a required project sequence. | Treat the graph as carry-through over FPF applications; use `stop`, `split`, and `return` edges. |
| **ProblemCard-as-solution.** The accepted problem card is treated as method, plan, work, evidence, or result. | Write the carried distinction and live P2W question before selecting an application. |
| **Math-as-authority.** A `U.Signature(profile=FormalSubstrate)` declaration, mathematical lens, or near-sameness does all downstream work. | Record preserved structure, lost structure, payoff, and stop condition; continue through the recovered relation. |
| **Generic result token.** "Result" becomes one local kind. | Split the phrase into artifact, telemetry, acceptance, quality, measurement, refresh, source, evidence, or role-enactability relation. |
| **Interface shortcut.** Interface, port, protocol, connection, resource, or integration wording selects function, method, work, evidence, gate, or architecture by itself. | Recover the FPF relation before continuing. |

### E.18.1:9 - Consequences

| Consequence | Benefit | Cost or mitigation |
|---|---|---|
| The carry-through record becomes the local work product. | A practitioner can replay the move from problem-side output to continuing FPF application. | The record adds a small step before downstream work. |
| Positive graph comes before boundary. | First use is readable before the heavier relation aid. | Boundary checks are still available in one canonical section. |
| Result language becomes unpackable. | Artifacts, telemetry, acceptance, measurement, refresh, and role enactability can be handled by their own records. | More than one application may be needed for one source phrase. |
| P2W stays non-procedural. | The pattern can be used in many project situations without prescribing one local procedure. | Teams that want a work procedure must add method or work-planning material outside P2W. |
| Related patterns keep their authority. | P2W avoids duplicating evidence, gate, decision, architecture, publication, mechanism, and work-family doctrine. | Users consult the pattern named by the recovered relation when that relation is live. |

### E.18.1:10 - Rationale

`E.18.1` is a child of `E.18` because P2W uses inherited transduction-graph architecture as its setting. It does not define graph law. It defines a local carry-through pattern for turning accepted problem-side material into a next admissible FPF use.

The design puts the positive mechanism first because repeated negative distinction sets can make a pattern whose primary EntityOfConcern is P2W behave like reference policing. P2W needs precision, but precision is useful here only when it leaves a surviving action: write the carry-through record, recover the FPF kind or relation, use the governed record, stop, split, or return.

### E.18.1:11 - SoTA-Echoing

**SoTA alignment rule.** P2W borrows useful distinctions from practice traditions only after they can be stated as a P2W carry-through move: accepted problem-side material, carried distinction, recovered FPF relation, written record, stop condition, and local return. Currentness has two sources. A project source can become stale or be replaced. An FPF pattern can also change the relation law used by the carry-through record. In both cases P2W reopens only the smallest affected application.

| Practice tradition | Distinction kept for P2W | P2W invariant | Practitioner implication | Reopen if |
|---|---|---|---|---|
| Model-based engineering and systems practice separates model, view, requirement, evidence, and execution records because each has different authority. | A useful diagram or view can classify the next relation without changing the governed kind. | P2W separates graph, view, publication, evidence, gate, and work applications before the next move. | The practitioner can use a diagram as thinking material without letting the diagram authorize work, prove readiness, or settle evidence. | The project source, architecture-description relation, evidence relation, gate relation, or release relation changes. |
| Traceability and digital-thread practice values continuity from problem, rationale, method, plan, work, and result while keeping record kinds distinct. | A trace is useful only when each record kind remains named. | P2W carries problem-side material through a replayable carry-through record while keeping problem card, work plan, performed work, evidence, provenance, result, and refresh relations distinct. | The team can replay a path from problem to work without treating trace continuity as evidence, approval, or performed work. | Source restoration, provenance, refresh, or work-family law changes the currentness relation. |
| Formal-methods and mathematical-modeling practice uses `U.Signature(profile=FormalSubstrate)` declarations to preserve invariants, expose lost structure, and make equivalence conditions explicit. | Mathematical value is recoverable only through preserved structure, lost structure, payoff, and stop condition. | P2W separates mathematical-lens use from the `U.Signature(profile=FormalSubstrate)` declaration and from empirical, work, evidence, or authorization claims. | A mathematical idea helps choose the next disciplined move without becoming proof of real-world identity or permission to act. | Mathematical-lens, signature, bridge, measurement, normalization, comparison, or source-currentness assumptions change. |
| Assurance, safety, evidence, gate, and decision practice treats confidence, acceptance, validation, approval, and release as distinct relations. | Labels and readiness phrases are cues, not local authority. | P2W preserves the cue, recovers the relation, and stops local authority until the governed relation is live. | A warning, green label, or approval note remains useful without becoming an evidence case, gate record, decision, or release. | Evidence, assurance, gate, conformance, release, work-entry, or decision relation changes. |

### E.18.1:12 - Relations

- `E.18` governs inherited transduction graph architecture, transfer annotations, flow valuation, `ConstraintValidity`, `GateFit`, gate profile, design tags, and run tags.
- `C.22.2` governs the accepted problem-side record and problem-side claims related to the carried distinction.
- `C.29`, `A.6.0`, `E.14`, `F.17`, `F.9`, `C.16`, `A.19.UNM`, and Part G govern mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, principle-frame, ontology, UTS, bridge, measurement, normalization, and comparison relations.
- `A.6.1` and `E.20` govern mechanism and mechanism-method stabilization relations.
- `G.5`, `G.9`, `A.19.SelectorMechanism`, `C.18`, and `C.19` govern candidate-set, comparison, selector, retained-set, and selected-record relations.
- `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, and `A.15.4` govern role-method-work alignment, performed work, planning, planned baselines, and work-relevant source restoration.
- `A.10`, `B.3`, `G.6`, `E.19`, `A.20`, `A.21`, and `C.11` govern evidence, assurance, provenance, conformance, gate, release, work-entry, and decision claims.
- `C.30`, `C.30.AD`, `C.30.ASV`, `C.31`, `A.6.M`, `A.6.F`, `E.10`, `E.17`, and `E.17.EFP` govern architecture, architecture-description, structural-view, reusable-structure, module-interface, function, wording-use, publication, and publication-use claims.

### E.18.1:End


---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "Principles-to-Work Carry-Through"
section_id: "E.18.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__005_solution.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "E.18.1 — Principles-to-Work Carry-Through"
  - "E.18.1:4 — Solution"
line_start: 75659
line_end: 75893
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.20"
  - "A.21"
  - "A.6.0"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.22.2"
  - "C.29"
  - "E.10"
  - "E.11.PUR"
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

The solution has two parts: use the declarative carry-through structure below to select one relation-governed P2W application, then fill the carry-through or replay record only for the relation being made. The locus and relation vocabulary names which distinction can be preserved, which FPF relation is recovered, which record is written, which cue is stopped, and which earlier application reopens after a problem-side result becomes useful for work.

#### E.18.1:4.0 - P2W Declarative Carry-Through Structure

Use P2W as a declarative carry-through structure of relation-governed applications from an accepted `ProblemCard@Context` to accepted FPF applications. The structure is not a prescribed FPF-use procedure. It can be expressed as a graph-shaped description or joined with project method-description or work-plan material only when that description or plan is the current EntityOfConcern of a governed use: a `U.MethodDescription`, `U.WorkPlan`, `TransformationFlowStructure`, flow valuation, or `E.18.2` mathematical description. P2W itself shows which distinction can be preserved, which FPF relation is recovered, which record is written, which cue is stopped, and which earlier application reopens after a problem-side result becomes useful for work.

The carry-through structure has nine recurring loci. A concrete P2W application selects a carry-through slice: it may use one locus, branch into several applications, split one source phrase into several records, stop with a reduced-use cue, or reopen an earlier locus when measurement or source currentness changes.

| Locus | Question answered | Output of the P2W application |
|---|---|---|
| `AcceptedProblemSideOutput` | What accepted problem-side material is being preserved for the next use? | Problem-card reference plus carried distinction. |
| `NextFPFUseQuestion` | What is the next unsettled FPF kind or relation? | One question stated in FPF vocabulary. |
| `FirstPrinciplesLens` | What structure, invariant, loss, or payoff makes the next use worth formal treatment? | Preserved structure, lost structure, payoff, and stop condition. |
| `DeclarationStack` | Which `U.Signature(profile=FormalSubstrate)`, `PrincipleFrame`, ontology, CHR, measurement, normalization, or bridge relation is needed? | Declaration or reference to the declaration relation named by value. |
| `MechanismMethodCandidate` | Is the next work-facing issue mechanism-position meaning, method-position meaning, method comparison, or retained-set handling? | Mechanism cue, method cue, comparison cue, selector cue, or retained-set cue. |
| `TransformationTemporalAspect` | Is the next issue a bounded transformation under conditions, a temporal aspect of a governed object or claim, or the adequacy of an authored temporal claim? | `A.3.4`, `C.27.TA`, or `C.27` application. |
| `WorkPreparation` | Is a planning record, planned slot-filling baseline, feasibility note, evidence-reference pin, or freshness request needed? | `U.WorkPlan`, PlanItem, or the `A.15.3` planned slot-filling ontic through `SlotFillingsPlanItem`. |
| `PerformedWorkAndResult` | Has dated `U.Work` occurred, and what result-related records appeared? | Work occurrence plus unpacked artifact, telemetry, acceptance, measurement, source, or role-enactability relation. |
| `ReturnAndRefresh` | Did measurement, source currentness, reference plane, or problem-side wording change an earlier assumption? | Return to the affected application with the changed relation named. |

P2W relation labels are `carry`, `recover`, `write`, `split`, `stop`, and `return`. `Carry` preserves a distinction from the problem side. `Recover` names the FPF kind or relation. `Write` creates or amends the governed record. `Split` separates one source phrase into several applications. `Stop` preserves a reduced-use cue when no relation-governed continuation is available. `Return` reopens the smallest earlier application whose assumption changed. These are carry-through relation labels for P2W use, not a project-work procedure.

#### E.18.1:4.1 - Carry-through record

For first-minute use, fill only `ProblemCardRef`, `CarriedDistinction`, `NextFPFUseQuestion`, and either `RecoveredFPFKindOrRelation` or `StopCondition`. Use the remaining fields only when the application continues, splits, writes a record, or returns after a changed assumption.

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

`NotCarried` is a compact field, not a place to repeat boundary doctrine from other governing patterns. It names only the local overread that would change this P2W application. `StopCondition`, `ReturnTrigger`, and `SourceCurrentnessCheck` keep stopping and reopening tied to a changed relation, measurement, source-currentness, or problem-side assumption.

This record shows the complete P2W relation structure: problem-side distinction, first-principles value, selected FPF application, written record, stop condition, and return after measurement and source-currentness change.

#### E.18.1:4.1a - Development-loop first-application record

Use this record when cheap generation, open-ended search, or evolutionary-engineering work makes many possible variants easy to produce before the project has a clear problem, characteristic set, comparison basis, selected set, work entry, or refresh rule.

```text
DevelopmentLoopFirstApplicationRecord@Project:
  ProblemCardRef:
  ImprovementConcern:
  CharacteristicOrDescriptorSetRef:
  VariantSetOrArchiveRef:
  ComparisonOrFrontRef:
  SelectedSetOrChoiceRuleRef:
  AutonomyBudgetRef:
  EvidenceAssuranceOrConfidenceUseRef?:
  ArchitectureCandidateRef:
  WorkPlanOrWorkRef:
  EffectMeasurementRef:
  RefreshOrResidualTriageRef:
  NextGoverningRelation:
```

The record does not create a development-factory kind, portfolio kind, or archive authority. It is a P2W carry-through record shape: the accepted problem-side distinction is preserved until one next governing relation can be named. If `NextGoverningRelation` is generation, retention, comparison, selection, architecture-candidate work, planning, performed work, effect measurement, residual triage, or refresh, continue in the pattern that governs that relation.

In development-for-developed work, cheap variant generation shifts effort toward problem production, characterization, archive stewardship, fair comparison, choice rule, decision record, autonomy boundary, trust and confidence use, evidence, assurance, performed work, effect measurement, currentness, and refresh. P2W keeps that shift usable by carrying the problem-side distinction into exactly one next relation instead of treating an archive, front, selected set, confidence phrase, or choice rule as work authorization.

Source wording such as "trust budget" is recovered to existing FPF relations: evidence support, assurance-sensitive confidence use, gate or release conditions, source-currentness, autonomy boundaries, `A.15.5` work-entry readiness, or decision records. It is not a new `U.TrustBudget`.

Field-compression map:

| Development concern | Record field | Governing continuation |
|---|---|---|
| Problem factory or problem production | `ProblemCardRef` and `ImprovementConcern` | `C.22.2` when the problem statement, opportunity, anomaly, or accepted problem-side material is current. |
| Solution variants, stepping stones, archives, or retained populations | `VariantSetOrArchiveRef` | `C.18` for archive, front, descriptor, retained-value, lineage, and generation records; `C.19` when live-pool or explore-exploit treatment is current. |
| Acceptance criteria, descriptors, parity expressions, and value dimensions | `CharacteristicOrDescriptorSetRef` | `C.16` when a characteristic space, descriptor set, indicator expression, or acceptance expression is being selected or repaired. |
| Fair comparison and front treatment | `ComparisonOrFrontRef` | `A.19.CPM` for comparison mechanism and `C.18` or `C.19` for front or pool records. |
| Selected set or explicit choice rule | `SelectedSetOrChoiceRuleRef` | `G.5` for selected-set publication or set-returning dispatch; `A.19.SelectorMechanism` when selector construction is current. |
| Local choice and decision record | `SelectedSetOrChoiceRuleRef` plus a separate decision reference when filled | `C.11` only when one local choice, commitment, or decision record is being made. |
| Autonomy budget or permitted generator action | `AutonomyBudgetRef` | `E.16` when an autonomy declaration or boundary is current. |
| Trust, evidence, assurance, or confidence use | `EvidenceAssuranceOrConfidenceUseRef?` | `A.10`, `B.3`, `G.6`, `A.20`, `A.21`, or another direct evidence, assurance, gate, release, or provenance pattern when confidence is used to support action, publication, selection, work entry, or acceptance. |
| Architecture candidate | `ArchitectureCandidateRef` | `C.30`, `C.30.ASV`, `C.30.AD`, or `C.30.ILC` when the candidate changes architecture, structural view, architecture description, or interlevel residual treatment. |
| Planning and performed work | `WorkPlanOrWorkRef` | A.15-family patterns when a plan, plan item, work occurrence, or work-result relation is current. |
| Measurement, result, residual, and refresh | `EffectMeasurementRef` and `RefreshOrResidualTriageRef` | Measurement and result patterns by value, `G.11` for refresh or currentness, and the governing level-and-residual pattern when an interlevel residual is current. |

#### E.18.1:4.1b - Development-for-developed first-minute slice

Use this slice when a project source says that AI agents or cheap generators make solution variants easy while problem setting, characteristic choice, fair comparison, selected-set choice, and effect measurement become the expensive work.

```text
DevelopmentLoopFirstApplicationRecord@Project:
  ProblemCardRef: accepted problem-side material for the development cycle.
  ImprovementConcern: what must become better, easier to change, easier to test, or more valuable.
  CharacteristicOrDescriptorSetRef: the characteristic, descriptor, indicator, acceptance, or parity expression being selected now.
  VariantSetOrArchiveRef: `C.18` archive, front, Q-front, or retained variant set.
  ComparisonOrFrontRef: `A.19.CPM` comparison relation or `C.19` live-pool or front treatment.
  SelectedSetOrChoiceRuleRef: `G.5` selected-set publication or explicit choice rule.
  EvidenceAssuranceOrConfidenceUseRef: `A.10`, `B.3`, evidence, provenance, gate, release, or confidence-use relation when current.
  ArchitectureCandidateRef: `C.30` family relation only when architecture of a holon or episteme is the object being changed.
  WorkPlanOrWorkRef: `A.15` plan or dated work when action is actually planned or performed.
  EffectMeasurementRef: measurement or result relation named by value.
  RefreshOrResidualTriageRef: `G.11` refresh or currentness relation, or the governing residual-triage pattern.
  NextGoverningRelation: one relation from the filled fields above.
```

```text
DevelopmentLoopFirstApplicationRecord@Project:
  ProblemCardRef: PC-DEV-041, "cheap generator produces many cooling-module layouts, but the project lacks a fair problem and comparison basis"
  ImprovementConcern: keep more maintainable low-energy module variants alive before choosing a product-family direction
  CharacteristicOrDescriptorSetRef: energy use, service access, manufacturability, thermal margin, test cost
  VariantSetOrArchiveRef: C.18 retained cooling-module candidate archive
  ComparisonOrFrontRef: A.19.CPM comparator over energy use and maintainability plus C.18 front record
  SelectedSetOrChoiceRuleRef: no selected-set publication yet; G.5 is next only after the comparator and front are accepted
  AutonomyBudgetRef: E.16 generator boundary for allowed layout search and test spending
  EvidenceAssuranceOrConfidenceUseRef: B.3 confidence-use relation plus A.10 evidence refs for prototype tests; no trust-budget kind is minted
  ArchitectureCandidateRef: C.30 candidate architecture relation for retained layouts that change selected structure
  WorkPlanOrWorkRef: empty until an A.15 work-plan relation is made
  EffectMeasurementRef: thermal and serviceability measurement relation to be named before any work-entry, gate, or authorization relation is relied on
  RefreshOrResidualTriageRef: G.11 refresh when descriptor, test, competitor, or source-currentness changes
  NextGoverningRelation: C.18 front record now; C.30 or G.5 only after the front and comparator are current
```

If a source calls these "problem factory", "solution factory", or "factory of factories", treat the phrase as a project label for work-organization slices: problem-setting work, variant-production work, and capability-building work. The phrase does not add a new FPF kind. Continue only through the filled field named by `NextGoverningRelation`.

#### E.18.1:4.2 - Positive carry-through table

| Locus reached | P2W application | Record or continuation |
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

Problem-side input: P2W starts only from accepted problem-side material. The record carries the distinction that matters for the next FPF use, not the whole problem-side pattern.

First-principles and declarations: mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, ontology, UTS, CHR, measurement, normalization, bridge, and `PrincipleFrame` material are handled as declaration-stack applications. The P2W record names which declaration or direct governing relation is being written or cited, what structure is preserved, what is lost, and which downstream relation is still unsettled.

When mathematical wording points both to a formal declaration and to a mathematical lens, P2W does not decide by vocabulary. Use the slot discipline in `A.6.0:10a.1`: `A.6.0` governs `U.Signature(profile=FormalSubstrate)` declaration, `C.29` governs mathematical-lens use, `A.6.1` governs mechanism consumption or realization, and `E.18.1` governs only the carry-through cue and next-relation selection.

Mechanism and method: do not decide by noun. Recover the claim position. A mechanism-position claim names operation algebra, law set, applicability predicates, effect realization, or mechanism-description need. A method-position claim names a context-defined semantic way of doing work, candidate set, comparison, selector, retained set, or selected-record need. A shared source label, project-side name, or recognizable change concern may require linked method and mechanism typed values, but P2W records only which relation is being carried through and leaves the other typed value as a stopped cue unless its governing pattern is applied.

Transformation and temporal aspects: a problem-side distinction may point to a bounded transformation, a temporal aspect, and a temporal-claim adequacy question at once. Do not fold these into method, mechanism, plan, or work. `A.3.4` governs bounded transformation under conditions, including transformed object, pre-state, post-state, condition set, and admissible effect claim. `C.27.TA` governs temporal aspects such as interval, deadline, cadence, rhythm, synchronization, currentness window, recovery timing, or stabilization timing when the aspect itself is being named. `C.27` governs adequacy, supported use, unsupported use, or source-currentness use of authored temporal claims.

Planning and performed work: planning records are `A.15.2 U.WorkPlan` values or plan-item records, including evidence-reference pins, feasibility notes, freshness requests, and planned constraints. Performed work is a dated `U.Work` occurrence. P2W records which side of that boundary the carry-through record uses and which later result records have appeared.

Result carry-through: a result phrase is treated as a bundle of possible records. The P2W application is to unpack it before it guides any next FPF use.

Structure, publication, function, module-interface, and integration cues: a transformation-flow structure, mathematical graph description, diagram, or publication can help classify the P2W application. Function wording continues only as an `A.6.F` function or functional-relation claim; interface, port, protocol, connection, resource limit, or integration wording continues only as a module-interface, signature-slot, reusable-structure, or architecture relation named by value through `A.6.M`, `A.6.5`, `C.31`, or the `C.30` family. Otherwise the wording remains classification material for the P2W record.

#### E.18.1:4.4 - Boundary and relation discipline

P2W is not a catalogue of boundary doctrines from other governing patterns. It has one local boundary rule: carry only the distinction accepted on the problem side, recover the next FPF kind or relation, and stop anything that would require a different governing relation until that relation is being made.

| Source pressure | Local P2W decision | Continuation |
|---|---|---|
| Problem-side material | Carry only the accepted distinction and the next FPF-use question. | Continue when the next FPF kind or relation is named; otherwise stop before P2W begins. |
| First-principles or mathematical wording | State preserved structure, lost structure, payoff, and stop condition. | Continue only as mathematical-lens use or as a `U.Signature(profile=FormalSubstrate)` declaration when that relation is being made. |
| Declaration-stack wording | Keep the declaration being made separate from measurement, normalization, comparison, ontology, or bridge relations. | Continue through the declaration relation that changes this P2W application. |
| Work-facing, temporal, or result wording | Recover the concrete mechanism-position, method-position, bounded-transformation, temporal, planning, performed-work, or result-related relation. | Continue through the matching application; split one source phrase only when several relations are being made. |
| Another governed relation appears inside the source phrase | Preserve the cue as source material, but do not import its governing law into P2W. | Continue only through the relation that changes this P2W application; leave the other cue stopped until its governing relation is being made. |

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

| What the source phrase makes current | Relation to recover before continuation | Local P2W application |
|---|---|---|
| accepted problem-side distinction | accepted `ProblemCard@Context` material plus one unsettled next relation | State what is carried and what question remains. |
| preserved or lost structure, invariant, near-sameness, formal payoff, or formal stop condition | mathematical-lens use or `U.Signature(profile=FormalSubstrate)` declaration | Name preserved structure, lost structure, payoff, and stop condition. |
| postulate, observability, unit, plane, comparator, threshold, ontology edition, CHR edition, normalization, bridge, or measurement | the declaration or measurement-family relation being made | Write or cite only that relation. |
| mechanism position, method position, method candidate set, comparator, selector, retained set, or selected record | the mechanism, method, comparison, selector, retained-set, or selected-record relation being made | Keep these relation positions distinct and continue only through the recovered one. |
| bounded transformation, temporal aspect, dynamics episteme, or temporal supported-use claim | `A.3.4`, `C.27.TA`, `A.3.3`, or `C.27` relation according to the claim being made | Split one phrase when it carries several of these relations. |
| planning record, plan item, performed work, launch value, result artifact, telemetry, acceptance, measurement, refresh, or role enactability | `A.15.2 U.WorkPlan`, plan-item, dated `U.Work`, or the result-related relation being made | Write or cite the record being made; do not let generic result wording guide the next FPF use. |
| structure, transformation-flow cue, diagram, scenario, view, graph expression, publication, module-interface, function, evidence-looking, gate-looking, or decision-looking wording | the relation named by value in the source phrase, or no continuation if none is recoverable | Use the material only as classification until the relation is recovered. |

#### E.18.1:4.7 - Lowering and reopen block

Use this block when the carry-through record cannot preserve and continue the stronger-looking source cue. P2W succeeds when it leaves one relation-governed application. If the application is not recoverable by value, lower the cue, stop, or reopen the smallest affected application.

| Claim family | Lowering or stop condition | Reopened or continuing relation |
|---|---|---|
| Problem-side material | No accepted `ProblemCard@Context`, or the accepted problem-side statement changes the carried distinction. | Stop before P2W begins, or return to the problem-side record named by value that changed. |
| First-principles, mathematical, formal, or declaration-stack claim | Preserved structure, lost structure, payoff, stop condition, declaration relation, measurement relation, normalization relation, bridge relation, or comparison relation cannot be named. | Lower to a reduced-use source cue; continue only after the recovered declaration, mathematical-lens, measurement, normalization, bridge, or comparison relation is being made. |
| Mechanism, method, selected-set, transformation, temporal, dynamics, planning, performed-work, or result claim | The source phrase blurs relation positions that change different P2W applications. | Split to the recovered relation and continue only through that relation. |
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
  NextFPFUse:
```

`ChangedAssumptionKind` names the assumption kind, such as measurement, unit, reference plane, source record, problem-side statement, method set, comparator, module-interface relation, publication-use relation, or FPF pattern change. `StillCarried` and `NoLongerCarried` prevent a source-currentness change from silently rewriting the whole carry-through slice. `SmallestReopenedApplication` keeps the repair local, and `NextFPFUse` states whether to continue, stop, split, lower to a reduced-use cue, or return to the problem-side pattern.


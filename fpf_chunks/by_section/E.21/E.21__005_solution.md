---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__005_solution.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:4 — Solution"
line_start: 86286
line_end: 86587
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.11"
  - "E.19"
  - "E.2.DA"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.21:4 - Solution

`E.21` declares the FPF pattern-quality `U.CharacteristicSpace`, its object-specific `A.19.ECS` evaluation specification, ordinal scale, complete result-shape rules, the local non-arithmetic `PatternQualityQBundle` result payload, and local result-status meanings. It does not itself inspect a pattern, perform assessment work, assign coordinate values, create evidence use, issue assurance, admit a pattern, or repair it.

For one actual pattern-quality evaluation, keep independently recoverable:

1. one exact authored FPF pattern edition or bounded version as the checked object;
2. the declared `ClaimScope`, working reader, intended receiving use, qualification window, evidence basis, and evaluation configuration;
3. the selected `U.CharacteristicSpace`, this E.21 evaluation-specification episteme, every coordinate/scale binding, and the local result-form and status-value rules;
4. one separately identified semantic evaluation `U.Method`;
5. the evaluator `U.System`, obtaining `U.RoleAssignment`, dated assessment `U.Work`, enacted method, and exact A.6.1 evaluation application/bindings;
6. every coordinate-result claim, their same-bearer non-arithmetic `PatternQualityQBundle` ClaimGraph payload, and one C.2.1 aggregate pattern-quality-result episteme when a durable result is needed;
7. witnesses, comparator/source/case refs, exact A.10 evidence-use/provenance relations, and any B.3 assurance or reliance result;
8. an optional evaluation-record episteme that packages those refs without performing assessment or creating the result;
9. the local `PatternQualityStatus` value and any separate F.10 status use/interpretation, E.19 admission or refresh decision, project gate or authority decision, publication, and currentness relation; and
10. later E.23 improvement or other repair work and its changed pattern edition.

Each coordinate-result claim is one quality ascription about the exact checked pattern edition. It keeps recoverable the bearer, effective ReferenceScheme, characteristic, scale value, evaluation rule or probe, comparison/calibration frame when used, `U.ClaimScope`, intended use, qualification window, assessment application, short rationale, and evidence locus. The complete same-bearer coordinate set forms the non-arithmetic `PatternQualityQBundle` payload carried by the aggregate result episteme; it is not an average, score, characteristic space, or second result. The evaluator system, evaluator viewpoint episteme if any, witness set, optional record, and receiving status or admission use remain separate.

One conforming assessment/result shape applies:

1. configure the checked pattern edition, scope, use, reader, window, characteristic space/specification, semantic evaluation method, and evidence basis;
2. let dated evaluator work enact that method through the exact A.6.1 application/bindings and apply the ordinal scale to every required coordinate;
3. constitute every coordinate-result claim with `ShortRationale` and the aggregate result episteme;
4. assert the local `PatternQualityStatus` in that result;
5. state its stop, repair, architecture-hold, or refresh condition; and
6. when improvement is requested, return distinct finding or proposal claims without changing the coordinate result into a work plan or making the evaluation specification perform repair.

There is no separate pre-check result. If a pattern lacks frame, first move, source basis, mature comparison, or naming clarity, the relevant coordinates fall.

#### E.21:4.1 - Local names and kind settlement

| Local name | Kind and function |
|---|---|
| `PatternQualityEvaluation` | Compatibility compound label for the configured evaluation package. Any use resolves to the exact characteristic space/specification, configuration, assessment application/work, result episteme, witnesses/evidence-use relations, and optional record rather than treating this label as one kind or actor. |
| `PatternQualityCharacteristicSpaceRef` | Reference to the exact A.19 `U.CharacteristicSpace` whose slots are the required E.21 coordinates and whose bindings use the E.21 ordinal scale; not an assessment, result, or record. |
| `PatternQualityEvaluationSpecRef` | Reference to this object-specific A.19.ECS evaluation-specification episteme: applicability, coordinate and scale meanings, evidence/missingness rules, calibration, result shape, local status meanings, and reopen conditions. |
| `PatternOfConcernRef` | Exact authored FPF pattern edition or bounded version named by value as the checked object, with its host path or monolith section and edition, commit, hash, or other pinned version basis recoverable. `PatternOfConcern` is relation-relative: the same pattern can also be the concern in another use, review, or evaluation flow. This row does not create a special kind of pattern or a second text. The evaluated pattern also has its own primary `EntityOfConcern`: the subject that its Problem, Solution, or guidance is about. FPF patterns are applied to situations, claims, texts, or work objects. Use `governing pattern` only in the typed form `governing pattern for <claim, relation, or boundary>` when the pattern actually governs that specific item; use `related pattern` for a looser pattern relation; use `relation` only for the relation itself. |
| `ClaimScope` | Quality claim boundary recovered from the governing frame: ordinary use, authoring input, landing input, release input, external-review input, high-assurance reuse input, canonization input, or another explicitly requested pattern-quality use. It is not chosen by the evaluator to make a failing request pass. |
| `WorkingReaderScope` | Working-reader family, viewpoint, and first-use situation the pattern must serve. |
| `IntendedUse` | Action that may use the result: continue drafting, admit for declared use, repair, refresh, or compare candidates. |
| `QualificationWindow` | Edition, SoTA, related-pattern, release, time, or comparison window in which the evaluation is current. |
| `EvaluationEvidenceBasis` | Checked evidence loci named by value for the evaluation: pattern body version, host or monolith section, README scenario, ToC row, `E.11` entry-distribution locus, `I.2` expanded entry-disambiguation case when corpus-facing, card or retrieval cue when claimed, source-currentness locus when SoTA/currentness is valued, mature comparator set when maturity is valued, and worked case or absence of worked case when case coverage is valued. Inclusion here is neither a witness claim nor an evidence-use relation. |
| `QualityEvaluationQuestionFrameRef` | `E.22` frame when purpose, floor, trade-offs, absorption, or proposal expectation needs to be declared. |
| `PatternQualityEvaluationConfiguration` | Local input tuple binding the exact checked pattern, scope/use/reader/window, characteristic space/specification, semantic evaluation method, question frame when used, and evidence basis. It is neither a new U-kind nor performed work. |
| `SemanticPatternQualityEvaluationMethodRef` | Reference to the exact semantic `U.Method` enacted by assessment work; the E.21 specification and coordinate table do not become that method merely by being consulted. |
| `PatternQualityAssessmentWorkRef` | Exact dated A.15.1 `U.Work` performed by the evaluator system under an obtaining role assignment and enacted semantic evaluation method. |
| `PatternQualityEvaluationApplicationRef` | Exact A.6.1 application and actual bindings connecting assessment work, checked pattern, evaluation configuration, and returned coordinate/result refs. |
| `CoordinateValueRationales` | One result claim for every required coordinate: `Coordinate`, `Value`, `ShortRationale`. |
| `CoordinateEvidenceRefs` | Per-coordinate text, case, relation, SoTA, mature comparator, projection, or review refs where the short rationale depends on evidence outside the pattern body row being discussed. Reference presence does not itself establish a coordinate value. |
| `PrecisionRestorationProfile` | Compact result profile over six precision-restoration layers: word, head, and use precision; phrase-level apparatus; repeated or distributed material; ontic and slot-relation clarity; description, publication, and source boundary separation; and pattern-application ontology. It collapses those layers into one scalar effect for the E.21 result, not one coordinate per defect. The profile names present or bounded issues, checked absence scope when clean, affected coordinates, and the selected restoration or governing pattern such as `E.10`, `E.10.ARCH`, `F.18`, `F.19`, `E.24.CD`, `E.24.PUB`, or an object-specific pattern. |
| `PatternQualityQBundle` | E.21-local non-arithmetic bundle-shaped ClaimGraph payload for one exact pattern edition, effective ReferenceScheme, `ClaimScope`, intended use, and qualification window. It contains the complete coordinate-result claims/rationales, `PrecisionRestorationProfile`, local `PatternQualityStatus`, stop condition, and bounded non-use. The aggregate C.2.1 result episteme carries this payload; it is not a general C.25 engineering `Q-Bundle`, characteristic space, evaluation specification, method, work/application, evidence use, assurance, admission decision, or second record. |
| `DominanceSet` | Coordinates used to compare already evaluated candidate versions. It never changes the required coordinate set. |
| `PatternQualityResultRef` | One C.2.1 result episteme whose EntityOfConcern is the exact checked pattern edition and whose ClaimGraph carries the same-bearer `PatternQualityQBundle`: declared use/window, every coordinate-result claim, `PrecisionRestorationProfile`, local status value, stop/repair condition, and bounded overread. It is not the bundle payload alone, assessment work, witness set, record, admission, or authority. |
| `PatternQualityWitnessRefs` | Exact pattern loci, cases, comparators, sources, traces, or projection loci cited by result claims; witness presence is neither a value nor evidence use. |
| `PatternQualityEvidenceUseRefs` | Exact A.10 evidence-use/provenance relations supporting reliance on result claims; they do not create those claims or the checked pattern. |
| `PatternQualityEvaluationRecordRef` | Optional C.2.1 record episteme packaging configuration, work/application, result, witness/evidence, non-use, and reopen refs. It performs no assessment and grants no status, admission, assurance, or authority. |
| `PatternQualityStatus` | Local admissible-use value asserted by the aggregate E.21 result episteme. It is not an E.19 admission or refresh decision; any F.10 status use or interpretation by a receiver is a separate relation. |
| `StopCondition` | Why improvement may stop, continue, refresh, or hold. |

Names are local to pattern-quality evaluation unless `F.18` promotes a durable name. They are not project evidence, release state, review state, assurance, work, publication, or gate authority.

#### E.21:4.2 - Evaluation configuration, application, result, and optional record

```text
PatternQualityEvaluationConfiguration:
  PatternOfConcernRef: <exact authored FPF pattern edition or bounded version>
  ClaimScope: <declared quality claim>
  WorkingReaderScope: <reader and first-use situation>
  IntendedUse: <what may consume the result>
  QualificationWindow: <edition, source, neighbour, release, or comparison window>
  PatternQualityCharacteristicSpaceRef: <exact A.19 characteristic space>
  PatternQualityEvaluationSpecRef: <this E.21 specification edition>
  SemanticPatternQualityEvaluationMethodRef: <exact U.Method used by assessment work>
  QualityEvaluationQuestionFrameRef: <E.22 frame when used>
  EvaluationEvidenceBasis: <checked pattern, corpus, source, comparator, case, and projection loci; missing or unchecked loci named explicitly when they affect values>

PatternQualityAssessmentApplication:
  AssessmentWorkRef: <dated U.Work>
  EvaluatorSystemRef: <exact U.System>
  EvaluatorRoleAssignmentRef: <exact obtaining U.RoleAssignment>
  EnactedMethodRef: <same SemanticPatternQualityEvaluationMethodRef>
  A6_1ApplicationAndBindingRefs: <exact application, checked-object/configuration inputs, and returned-result bindings>
  EvaluationConfigurationRef:
  ReturnedCoordinateResultRefs:
  AggregateResultRef:

PatternQualityResultEpisteme:
  EntityOfConcern: <same exact PatternOfConcernRef>
  EffectiveReferenceScheme:
  ClaimGraph:
    PatternQualityQBundle:
      ClaimScope:
      WorkingReaderScope:
      IntendedUse:
      QualificationWindow:
      PrecisionRestorationProfile: <collapsed profile: word, head, and use; phrase-apparatus; repetition-and-distribution; ontic-slot clarity; description-publication-source boundary; pattern-application; scalar effect, affected coordinates, and selected restoration or governing pattern>
      CoordinateValueRationales: <all required coordinates, values, short rationales>
      CoordinateEvidenceRefs:
      PatternQualityStatus: <local result value>
      StopCondition: <local stop, first repair, hold, or refresh>
      BoundedNonUse:
  AssessmentApplicationRef:
  PatternQualityWitnessRefs:
  PatternQualityEvidenceUseRefs:
PatternQualityEvaluationRecord: <optional packaging of configuration, application/work, result, witness/evidence, non-use, and reopen refs only>
```

An unfinished table, prose summary, or record with missing coordinate claims remains assessment material, not an E.21 result. The evaluation specification, characteristic space, method description, checklist, evidence-basis list, favorable local status, and optional record perform no work, constitute no coordinate value by themselves, and grant no admission, assurance, gate crossing, publication truth, or authority.

#### E.21:4.3 - Ordinal scale, result row, and adjacent-value rationale

| Value | Label | Meaning |
|---:|---|---|
| 0 | `absent` | The characteristic is not expressed for the declared scope. |
| 1 | `namedOnly` | It is named or implied but not usable as quality evidence. |
| 2 | `partiallyExpressedForDeclaredUse` | It is present but incomplete, fragile, or insufficient for the declared use. |
| 3 | `sufficientlyExpressedForDeclaredUse` | It is usable for the declared scope, with limits visible. |
| 4 | `wellExpressedForDeclaredUse` | It is clear, evidenced, and bounded for the declared scope. |
| 5 | `exceptionallyExpressedForDeclaredUse` | It is exceptional for the declared use across reinforcing loci and cases, without hidden cost or neighbour loss. |

Values are ordinal content evaluations. They are not `U.Measure`s, averages, percentages, maturity-ladder steps, review votes, or landing status.

The result-bearing coordinate row has exactly this shape:

| Coordinate | Value | ShortRationale |
|---|---:|---|
| `<E.21 coordinate>` | `<0..5>` | `<assigned-value basis; why the lower adjacent value would understate the evidence; why the higher adjacent value would overstate the evidence, or for 5 what evidence makes 4 too weak and what would lower or reopen>` |

A two-column coordinate-and-value table, a narrative paragraph, a table whose comment lacks adjacent-value comparison, or a result whose value depends on unchecked external loci is not an `E.21` result. It is only draft evaluation material until every coordinate has a `ShortRationale` row and the result names the `EvaluationEvidenceBasis` used for values that depend on source, comparator, corpus, projection, or worked-case evidence.

A `ShortRationale` is allowed to be compact, but it is not allowed to be evidenceless. When the value depends on a source-currentness row, mature comparator, README scenario, ToC row, `E.11` entry-distribution locus, `I.2` expanded entry-disambiguation case, card, retrieval cue, monolith section, worked slice, near-miss, or anti-case, the rationale names that locus by value or says that the locus was missing or unchecked. "By value" means a recoverable section, row, case, checklist item, relation, source row, projection row, comparator id plus selected ingredient, or specific absent locus; a category list such as "entry, first move, boundaries, SoTA, checklist, relations" is not by-value discharge. Missing or unchecked evidence lowers the value for the coordinate that needs it; it does not create a separate "not evaluated" result.

A `5` is not a reward for clear early wording, named neighbour relations, or a well-formed field set alone. It needs exceptional expression for the declared use: reinforcing loci, a worked or otherwise replayable slice where the coordinate demands one, and no hidden cost or neighbour loss. When the evaluator cannot say why `4` would understate the evidence, assign `4` or lower.

When a coordinate's `5` meaning names a filled case, replayable slice, near-miss, anti-case, worked comparison, projection evidence, currentness basis, or selected-neighbour replay, absence of that evidence caps that coordinate at `4` even if the prose is otherwise strong. Do not hide the same absence only in `CaseCountercaseAndTransferCoverage`; lower every coordinate whose own `5` meaning needs that missing evidence. A `5` rationale names the reinforcing evidence loci that make `4` too weak.

For `MaturePatternParityAndSelectedContentSufficiency`, the rationale names a mature-pattern comparison set and the selected mature ingredients being claimed. For non-epistemic patterns, include at least one mature non-epistemic comparator when one exists: work, method, role, system, control, architecture, selection, engineering-action, or another pattern whose primary `EntityOfConcern` is not an episteme or publication. Value `4` requires by-value discharge of selected ingredients in the body or neighboring pattern governing the claims; comparator IDs plus a generic "main ingredients are present" sentence are only value `3`. The comparison is not a length target and not permission to copy semio apparatus.

For a `4` or `5` on `MaturePatternParityAndSelectedContentSufficiency`, include a compact maturity-discharge payload in the rationale or `CoordinateEvidenceRefs`: `comparator=<pattern id>; selectedIngredient=<ingredient name>; currentLocus=<section, row, case, checklist item, relation, or neighboring pattern governing the claim>; missingOrLowering=<absent or weak ingredient, if any>`. A category list such as "frame, first move, neighbour relations, CC, SoTA, relations" without current loci is still value `3`, even when the listed categories are plausible mature ingredients.

#### E.21:4.3a - Precision-restoration profile

Before assigning the coordinate table, record one `PrecisionRestorationProfile`. This is not an optional scan and not a lexical grep result. It is a pattern-text-use attention discharge: the evaluator asks which governed object, claim, relation, and reader use the sentence, table, section, or repeated content family serves in the pattern of concern.

Use this compact shape:

```text
PrecisionRestorationProfile:
  overallEffect: <clean | boundedLocal | lowersCoordinates | repairBeforeUse>
  wordHeadUsePrecision: <clean | E.10, E.10.ARCH, F.18, or governing pattern needed | lowers coordinates>
  mgdaColdReaderRecoverability: <clean | broad replacement | hidden specialization | governing pattern missing | lowers coordinates>
  kindRestorationCheck: <pre-repair kind, relation, current ontic slot, relation position, use relation, or claim kind, and admissible use -> proposed post-repair kind, relation, current ontic slot, relation position, use relation, or claim kind, and admissible use; preserved | split | intentionally changed | blocker>
  phraseApparatus: <clean | F.19 needed | lowers coordinates>
  repetitionAndNegativeDistribution: <clean | bounded-local | lowers coordinates>
  onticAndSlotRelationClarity: <clean | hidden candidate ontic or slot-relation drift | lowers coordinates>
  descriptionPublicationSourceBoundary: <clean | description-publication-source boundary leakage | lowers coordinates>
  patternApplicationOntology: <clean | application relation unclear | lowers coordinates>
  checkedLoci: <sections, rows, cases, and relations checked>
  affectedCoordinates: <coordinates lowered or protected>
  repairProposal: <repair, no-repair disposition with loci, or owning locus>
```

This profile deliberately collapses several small diagnostic checks into one scalar effect. The scalar is the strongest quality effect that any layer requires: clean, bounded local repair, coordinate lowering, or repair-before-use. The layers are diagnostic, not extra coordinates, checklists, or proposal quotas. A new precision-restoration symptom is classified into one of these layers or assigned to the selected restoration or governing pattern; it does not mint a new `E.21` coordinate. Details belong in the patterns that govern those objects: word, head, and name problems apply `E.10`, `E.10.ARCH`, or `F.18`; phrase-level boilerplate and plain-technical rewriting apply `F.19`; hidden candidate ontics and ontic-vs-description-vs-publication boundaries apply `E.24.CD`, `E.24.PUB`, or the direct subject pattern when the governed object is already clear; claim, relation, evidence, work, decision, assurance, publication, or pattern-application problems apply the pattern that governs that object. `E.21` consumes only the result: which coordinates fall, which stay protected, and what repair would make the quality claim true. The `mgdaColdReaderRecoverability` layer asks whether a reader without the `DRR`, campaign notes, or evaluator memory can recover the object, kind or ordinary status, relation or claim position, admissible use, and next governing pattern. If a repair replaces a specific phrase with `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, or unqualified `specialization` and the reader cannot recover what specializes what, which relation is live, or which governing pattern receives the claim, this layer is not clean.

When this layer finds a hidden candidate ontic or publication-form confusion, the E.21 result records only the quality effect and affected coordinates. Candidate detection, ontic placement, slot-relation design, and publication-boundary repair remain with `E.24.CD`, `E.24.PUB`, or the direct governing pattern. The evaluation specification does not become an ontic-discovery pattern, and assessment work does not acquire ontic-authoring authority by noticing that defect.
The `kindRestorationCheck` is required whenever a precision-restoration finding or repair proposal changes wording. It records the meaning-bearing object, kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope before and after the proposed repair, then names the governing pattern when another pattern governs the affected kind, relation, claim, or position (`A.6.0`, `A.6.5`, `A.6.P`, `C.29`, `A.15`, `E.24.CD`, `E.24.PUB`, `E.10.ARCH`, or another governing pattern). `E.21` does not restate slot discipline, ontic architecture, publication-form discipline, or mathematical-lens ontology; it only checks that the repair preserved or deliberately changed them by value. The check is a bounded complete preservation proof, not a blanket demand to formalize every sentence and not a license to do the least visible work. Complete means every field whose value can drift because of the changed wording receives one explicit disposition: `not triggered`, `ordinary prose`, or `no FPF-governed phrase changed` with checked loci, `preserved`, `split`, `intentionally changed by accepted decision`, or `blocker`. A no-repair result is valid only as one of those dispositions with loci; "nothing to do" without that discharge is a missing repair. Expand the row only when a kind, relation, claim, current ontic slot, relation position, use relation, or claim kind, or admissible use can drift. A lexical replacement is not a repair when it only removes a trigger word, substitutes one umbrella for another, narrows a graph or method into a work sequence, widens a work occurrence into a method, turns a publication form or evidence source into the object itself, or otherwise changes kind or current ontic slot, relation position, use relation, or claim kind without an accepted decision. If the kind or current ontic slot, relation position, use relation, or claim kind cannot be recovered, the profile is at least `lowersCoordinates`; if the proposed repair would change kind or current ontic slot, relation position, use relation, or claim kind and no accepted DRR or governing pattern justifies that change, the result is `repairBeforeUse` or `holdForArchitectureDecision`.

When the profile is not clean, lower every affected coordinate named by the profile. Do not hide a present precision-restoration issue only in `EntityOfConcernPrimacyAndSemioBiasResistance`, and do not raise the result through related-pattern-boundary praise, projection evidence, or "correct but true" guards when those materials compete with the pattern's own `EntityOfConcern`, first useful move, practitioner action, practical delta, and bounded non-use.

#### E.21:4.4 - RequiredPatternQualityCoordinates

For every conforming E.21 result, dated assessment work applies the evaluation specification to every coordinate below, and the result episteme states every coordinate value and rationale.

| Coordinate | What it evaluates |
|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | Whether the reader recognises the situation, ordinary use, non-use, harm if missed, and boundary early. |
| `EntityOfConcernAndClaimScopeStability` | Whether the primary `EntityOfConcern` and quality-claim scope stay stable across title, Problem frame, Solution, cases, checklist, relations, and status. |
| `PatternApplicationGuidance` | Whether the Solution gives usable pattern-application guidance after the first move is recovered. |
| `ClosureAndBoundedNonUseRecoverability` | Whether stop conditions, repair conditions, bounded non-use, and any `governing pattern for <claim, relation, or boundary>` statements are recoverable. |
| `SemanticKindAndNameRecoverability` | Whether names, kinds, relations, qualifiers, and claim boundaries recover the same FPF interpretation. |
| `NeighborAuthorityAndBoundedUseFit` | Whether evidence, assurance, measurement, naming, work, gate, decision, publication, release, and project claims stay with the pattern that governs each claim, relation, or boundary. |
| `EntityOfConcernPrimacyAndSemioBiasResistance` | Whether the pattern leads with its own `EntityOfConcern`, first useful move, practitioner action, practical delta, and bounded non-use instead of letting description, publication, source, evidence, review talk, standard non-use warnings, precision-repair material, quality or projection evidence, package rationale, or cross-pattern reference boilerplate take over. The `PrecisionRestorationProfile` supplies the collapsed diagnosis across word, head, and use precision; phrase apparatus; repetition-and-distribution; ontic-slot clarity; description-publication-source boundary separation; and pattern-application ontology. This coordinate consumes that profile by lowering the value when those auxiliary materials compete with the pattern's positive subject and action guidance or ordered first-use actions. Semio-bias is one special case when the displaced content concerns descriptions, sources, publications, notes, records, diagrams, or evidence-like publications. |
| `PracticalUseDeltaAndHarmPrevention` | Whether the pattern changes a real reader use, prevents a named misuse, reduces a named cost, or preserves a named boundary. |
| `UseAffordabilityAndApparatusProportionality` | Whether ordinary first use stays affordable and heavier apparatus appears only when it buys admissible use. |
| `RepairLocalityAndChangeImpactPredictability` | Whether repairs have the smallest locus and predictable downstream impact. |
| `ProxyForValueSubstitutionResistance` | Whether the assessment question and coordinate-result rationale state what became worse when visible quality coordinates improved, and keep any use of a visible quality value, metric, review result, or release cue as practical value under an exact `E.13` application/result. |
| `ClaimJustificationTraceabilityCurrentnessAndReplayability` | Whether the claim is replayable from pinned text, scope, evidence, currentness basis, limitations, status, and stop reason. |
| `CaseCountercaseAndTransferCoverage` | Whether positive cases, near-misses, anti-cases, and transfer cases match the breadth claimed. |
| `MaturePatternParityAndSelectedContentSufficiency` | Whether selected mature-pattern ingredients are present in the body or related patterns for this `EntityOfConcern` and use. |
| `SoTABindingAndCurrentness` | Whether current best-known practice changes the pattern and has reopen and currentness discipline. |
| `FormalClaimAdmissibilityAndLensFit` | Whether measurement, scale, comparison, formal model, simulation, causal, mathematical, QL, or learned-lens claims are admissible for their stated use, bounded to the governing pattern that owns the claim, or correctly absent. |
| `FalsifiabilityAndLoweringCondition` | Whether coordinate values, status, and stop claims say what would raise, lower, or reopen the evaluation. |
| `CorpusEntryProjectionAndEcologyFit` | Whether README scenarios, ToC query cues, Preface cues, `E.11` entry-distribution loci, `I.2` expanded entry-disambiguation cases, cards, summaries, retrieval snippets, durable names, relations, and corpus ecology preserve the scoped quality result without becoming authority-bearing publication faces, stale echoes, or pattern content. Corpus-entry and projection evidence belongs in the `E.21` result, `E.19` run record, README, ToC, `E.11`, `I.2`, retrieval or card publication locus, or other quality evaluation locus unless the pattern of concern's own `EntityOfConcern` and user-facing action are that projection or evaluation work. |
| `EvolutionFrontAndRefreshDiscipline` | Whether variants, fronts, archives, refresh windows, and smallest-reopen rules preserve open-ended evolution without endless polishing. |

Constraint, harm, safety, security, compliance, deontic, self-application, recursion, and high-assurance questions do not add a second coordinate family. Evaluate them through the coordinate that owns the content: related-pattern authority, traceability, formal-claim admissibility, falsifiability, affordability, corpus ecology, evolution, or refresh.

**Coupled-flow unity and separation for pattern quality.** Dated E.21 assessment work evaluates one exact `PatternOfConcernRef` inside a development, refresh, or admission flow. Another flow may make the same pattern a pattern of concern for a different use relation, for example a practitioner selecting and using it, a reviewer applying it to another text, or subsequent assessment work reopening it. One `TransformationFlowStructure` may join pattern development, pattern use, use-found evaluation, and repair or refresh flows through transfer, feedback, return, edition-change, or projection relations. Keep three positions distinct in each sentence: the pattern as concern of the current flow, the intended reader addressed by the pattern, and the pattern's own primary `EntityOfConcern` inside its Problem, Solution, or guidance. E.21 and E.19 are specifications; dated assessment and review work are the checking operations; handoffs, ledgers, README, ToC, `E.11`, `I.2`, retrieval outputs, and landing evidence are distinct records, publications, or evidence loci in the development/evaluation flow. Those objects may support edits to the pattern, but they are not automatically user-facing content for the reader addressed by it. `DesignRunTag` stays on the subject-context, claim, work, trace, publication-form relation, or source relation inside the transformation-flow structure; it does not decide whether a pattern is current, obsolete, under development, or being used. Treat FPF pattern development as the local pilot case: quality-loop proof supports separately performed edits; copying that proof into the pattern does not change the pattern by itself.

#### E.21:4.4a - Frequent value-3, value-4, and value-5 calibration points

These rows calibrate common disagreements. They do not replace the coordinate definitions above.

| Coordinate family | 3 is typical when | 4 is typical when | 5 is typical when |
|---|---|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | The use situation is recoverable but late, abstract, or missing harm, payoff, or non-use detail. | The situation, first move, harm, payoff, and non-use are early and clear. | Early recognition is reinforced by a filled or replayable first-use slice showing that a cold practitioner can enter correctly. |
| `EntityOfConcernAndClaimScopeStability` | The primary object is named but related record, evidence, lens, or project claims keep pulling the scope. | The primary `EntityOfConcern` and claim scope stay stable, with bounded related-pattern material. | Scope stability is reinforced across title, recognition text, Solution, worked or replayable case material, checklist, relations, and non-use without any local apparatus stealing attention. |
| `PatternApplicationGuidance` | The first action is named but only partly executable, or the Solution mostly assigns governing loci instead of giving this pattern's own action. | The first action and continuation are executable in this pattern's own subject terms; related-pattern statements are declarative, compact, and late. | The application guidance is demonstrated by a filled worked slice or equivalent replayable evidence. |
| `ClosureAndBoundedNonUseRecoverability` | Non-use or related-pattern statements are present but not tied to stop, repair, or lowering conditions. | Stop, repair, bounded non-use, and governing-pattern statements for specific claims, relations, or boundaries are recoverable for declared use. | A worked stop, overturn, or non-use case shows how closure changes status or the next applicable pattern relation. |
| `NeighborAuthorityAndBoundedUseFit` | Related patterns are named but some authority split remains generic, future-pattern-like, ambiguous, role-nicknamed, or too early in the Solution. | Related patterns named by value and limited declarative relations are clear enough for declared use and do not replace the pattern's own content. | Related-pattern authority is replayable across examples, relations, and overread cases, with pattern application and authority kept explicit. |
| `EntityOfConcernPrimacyAndSemioBiasResistance` | The pattern is about its object but one or more precision-restoration layers lead or leak into the pattern in a developer, reviewer, or evaluator role. | The pattern leads with its own object and application guidance; auxiliary material is compact, declarative, and late; role, slot, publication-form, source, locus, flow, and status words are used only when they add a real kind, relation, evidence value, or user-facing action; quality or projection evidence about the pattern stays outside the pattern. | The primary object and application guidance are first recoverable across recognition text, Solution, cases, and checks even when auxiliary material is present, and any precision-restoration, quality, or projection material is in its proper evaluation, projection, or publication locus rather than in the pattern. |
| `PracticalUseDeltaAndHarmPrevention` | The prevented harm is named but not demonstrated. | The pattern changes a recoverable use and blocks named misuse for declared use. | A worked or near-miss case shows the practical delta, cost of the missed pattern, and prevented harm. |
| `UseAffordabilityAndApparatusProportionality` | The first move exists but apparatus is heavy for ordinary readers. | Ordinary first use is affordable and heavier apparatus opens only when useful. | A minimal first-use example shows the thin ordinary use works before heavy apparatus. |
| `RepairLocalityAndChangeImpactPredictability` | Repair conditions or related-pattern relations are named but downstream impact is not shown. | Repairs have local loci and predictable impact for declared use. | A worked repair or downstream-impact slice shows the smallest locus and changed related-pattern relation. |
| `ProxyForValueSubstitutionResistance` | Proxy risks are named but "what got worse" is not applied. | The pattern blocks visible proxy substitutions and asks what worsened. | A proxy-failure case shows a visible improvement damaging intended value, and the pattern prevents that stop. |
| `ClaimJustificationTraceabilityCurrentnessAndReplayability` | Fields or sources exist but replayability and currentness basis are incomplete. | The claim can be replayed from pinned text, evidence, currentness basis, status, and stop reason. | A filled evidence and currentness slice shows how the claim is replayed and when it reopens. |
| `CaseCountercaseAndTransferCoverage` | Archetypes are listed, but no filled worked case or near-miss exercises the claim. | At least one filled worked case plus a near-miss or anti-case covers the declared use. | Heterogeneous cases, countercases, and transfer slices cover the breadth claimed. |
| `MaturePatternParityAndSelectedContentSufficiency` | Mature comparators are named or implied, but selected mature ingredients are not discharged by value. | Mature comparators are named and selected ingredients are discharged by value in the body or related patterns named by value. | Mature parity is shown across reinforcing body sections, related patterns, omissions, cases, and lowering conditions without copying irrelevant apparatus. |
| `SoTABindingAndCurrentness` | Sources are relevant and not decorative, but currentness, source-use status, or reopen conditions are compact or incomplete. | Decision-governing sources state adopt, adapt, or reject disposition, content mutation, currentness window, and reopen condition. | The pattern compares current best-known practice against popular, official, or lineage alternatives and carries the resulting source decisions into solution, cases, boundaries, and refresh. |
| `FormalClaimAdmissibilityAndLensFit` | Formal, scale, lens, or measurement terms are bounded but not exercised. | Formal, lens, and measurement claims are admissible for their stated use, bounded, and governed by the related pattern that owns the claim when the evaluated pattern makes such claims. | A worked formal, lens, or scale comparison shows what is preserved, lost, admissible, and not proved. |
| `FalsifiabilityAndLoweringCondition` | Stop, waiver, or non-use fields exist, but lowering and reopen triggers for the main claims are mostly implicit. | The pattern states explicit lowering and reopen triggers for its main claims; named fields alone do not reach `4` unless they say what evidence change lowers, overturns, rejects, or reopens the claim. | Worked lowering or overturn cases show how values, status, or use change. |
| `CorpusEntryProjectionAndEcologyFit` | Host text is coherent, but README, ToC, `E.11`, `I.2`, card, retrieval, monolith, or projection evidence is absent for a corpus-facing claim, or that evidence is placed anywhere in the pattern as method, note, appendix, relation, rationale, or quality-status content about the pattern. | Corpus-facing entry or projection loci are named and aligned enough for the declared use, and their evidence stays in the evaluation, result, or projection locus rather than entering the pattern. | Retrieval, stale-projection, cold-reader, or projection-update evidence shows corpus ecology stays aligned after change without leaking into the pattern. |
| `EvolutionFrontAndRefreshDiscipline` | Reopen is delegated to related patterns or implied by source-return. | The smallest reopen locus, source or currentness trigger, or variant or front condition is explicit. | Variant, front, archive, or ongoing refresh discipline is replayable for the declared use. |

For `EntityOfConcernPrimacyAndSemioBiasResistance`, do not compensate a bad `PrecisionRestorationProfile` with `NeighborAuthorityAndBoundedUseFit` or `CorpusEntryProjectionAndEcologyFit`. This is a pattern-text-use evaluation, not a lexical search: ask which governed object, claim, relation, and reader use the sentence serves. Material about developing, reviewing, projecting, landing, evaluating, or proving this pattern's quality belongs in the evaluation, projection, release, or publication locus that owns that work, not in the pattern. Related-pattern statements named by value can be true and still damage the pattern of concern when they appear before the pattern's own `EntityOfConcern` and application guidance are recoverable. If the opening Problem frame or Solution starts with precision-restoration material before the pattern's own subject and move, this coordinate is at most `2`; if a positive action exists but the reader must traverse that material across sections to find it, it is at most `3`. Compact related-pattern statements belong in `Relations` or short late boundary rows and must preserve kind. Local boundary prose is admissible only when it states a documented local confusion and local stop condition not already carried by the owning pattern for that specific distinction or claim boundary. Also lower `PatternApplicationGuidance`, `WorkingSituationAndUseBoundaryRecognizability`, `PracticalUseDeltaAndHarmPrevention`, and `UseAffordabilityAndApparatusProportionality` when the profile shows that precision-restoration issues displace first-use content.
If the declared use is `Stable`, landing-input, release-input, external-review-ready, or another corpus-facing use, assessment work must inspect the applicable corpus-entry and projection evidence and the result's `EvaluationEvidenceBasis` must name it. A host-only body assessment can still produce values about the pattern body, but it cannot silently turn missing README, ToC, `E.11`, `I.2`, card, retrieval, monolith, or projection evidence into a high `CorpusEntryProjectionAndEcologyFit` value.

#### E.21:4.5 - Status and stop condition

| Status | Meaning |
|---|---|
| `admissibleForDeclaredUse` | Every coordinate meets the declared floor for the scoped use, and bounded non-use is stated. |
| `repairBeforeUse` | One or more coordinate floors fail for the declared use. |
| `holdForArchitectureDecision` | The defect is not local prose; `EntityOfConcern`, neighbour authority, split, merge, or placement must be decided. |
| `refreshNeeded` | A SoTA, neighbour, terminology, retrieval, telemetry, use-scope, or corpus change invalidates a previous evaluation. |

Default floor is `4 wellExpressedForDeclaredUse` on every coordinate for ordinary practitioner use, authoring-input use, landing-input use, `Stable`, external-review-ready, release-input, canonization-input, stop-improving claims, and ordinary improvement-loop use. A diagnostic or exploratory request still measures every coordinate and reports values; it does not create an admissible-use shortcut. If the assignment asks for corpus-facing, landing-input, `Stable`, release, or external-review use, the evaluator measures that required use and returns `repairBeforeUse`, `holdForArchitectureDecision`, or `refreshNeeded` when the floor is missed.

An all-`5` result is a local exceptional result under the declared scope and qualification window. It is not a permanent end of development. `E.23` can reopen improvement when use, source, comparison set, front, affordability, or payoff changes.

#### E.21:4.5.1 - Consume Pattern-Edition Use-Value Evidence Noncompensatorily

When an `E.19:4.3.3` replay is current, the E.21 assessment application carries every probe separately by its branch, exact basis, working use or relying work, expected first useful result, boundary, necessity, disposition or outcome, checked loci, and evidence basis into the complete E.21 result. Dated assessment work applies every existing coordinate required by the declared scope. The result does not replace the coordinate set with one use-value score, average replay results, or copy an E.19 outcome into a coordinate value or `PatternQualityStatus`. Put the replay loci in `EvaluationEvidenceBasis` and justify each affected coordinate in its ordinary rationale.

Apply these consequences:

| Use-review condition | Mandatory E.21 consequence |
| --- | --- |
| A required prior-edition use probe is `regressed` | Set status to `repairBeforeUse`. Every affected coordinate is at most `2 partiallyExpressedForDeclaredUse`. Include at least `PatternApplicationGuidance` and `PracticalUseDeltaAndHarmPrevention` when action or result was lost; also include each of `ClosureAndBoundedNonUseRecoverability`, `NeighborAuthorityAndBoundedUseFit`, `UseAffordabilityAndApparatusProportionality`, and `ClaimJustificationTraceabilityCurrentnessAndReplayability` when that coordinate's claim depended on the use. |
| A required new intended-use check is **absent or insufficient for the candidate-only use** | Set status to `repairBeforeUse`. Every affected coordinate is at most `2`. Include at least `PatternApplicationGuidance` and `PracticalUseDeltaAndHarmPrevention`. Additionally cap each of `EntityOfConcernPrimacyAndSemioBiasResistance`, `ClosureAndBoundedNonUseRecoverability`, `NeighborAuthorityAndBoundedUseFit`, `UseAffordabilityAndApparatusProportionality`, `CaseCountercaseAndTransferCoverage`, and `ClaimJustificationTraceabilityCurrentnessAndReplayability` only when the missing evidence affects that coordinate's claim. |
| An optional new intended-use check is **absent or insufficient for the candidate-only use** | Do not create a status blocker merely from absent optional breadth. The missing case cannot support a breadth, transfer, or value-`5` claim. Reflect the absence in `CaseCountercaseAndTransferCoverage` and every coordinate whose declared scope actually includes that use. |
| A new intended-use check is **adequate for the candidate-only use** | No blocker follows from that check. Its evidence may support affected existing coordinates but establishes neither their values nor status by itself. |
| The pattern's positive subject, problem, action, and result guidance is absent or unusable: its own `EntityOfConcern`, first useful move, practitioner action, practical delta, or bounded non-use cannot be recovered | Set status to `repairBeforeUse`. `PatternApplicationGuidance`, `EntityOfConcernPrimacyAndSemioBiasResistance`, `PracticalUseDeltaAndHarmPrevention`, and `UseAffordabilityAndApparatusProportionality` are each at most `2`. |
| A required enumeration has an unresolved hidden kind, alien member, hidden proposition, or false closure claim | Set status to `repairBeforeUse`. `SemanticKindAndNameRecoverability` is at most `2`; each of `EntityOfConcernAndClaimScopeStability`, `NeighborAuthorityAndBoundedUseFit`, `FormalClaimAdmissibilityAndLensFit`, and `PatternApplicationGuidance` is also at most `2` when the unresolved member affects that coordinate's claim. |
| A required prior-edition use is discoverably `transferred` | No regression blocker follows. The handoff evidence may support `NeighborAuthorityAndBoundedUseFit`, `PatternApplicationGuidance`, and `ClosureAndBoundedNonUseRecoverability` but establishes none of their values by itself. |
| A harmful or false prior-edition use is `intentionally retired` with a positive corrected action or boundary | No regression blocker follows. Evaluate the corrected use and harm prevention on their own evidence. |
| The material-change trigger is false | Apply no new use-review cap. The ordinary complete coordinate, rationale, and result requirements still apply whenever an E.21 result claim is requested. |

The cap is `2`, not `3`, because `3 sufficientlyExpressedForDeclaredUse` already means usable for the declared scope while the required action or semantic member here is unusable. Unrelated strengths, source count, formal cleanliness, or corpus projection cannot compensate for the failed required use. Conversely, `preserved`, `improved`, `transferred`, `intentionally retired`, or adequate candidate-only evidence can support only the existing coordinates whose claims it actually tests; it cannot raise unrelated coordinates or determine status by label.

#### E.21:4.6 - Compact result form

An `E.21` result uses this result-bearing form:

```text
E.21 result:
  Pattern of concern: <PatternOfConcernRef>
  Declared scope, use, reader, and window: <ClaimScope, IntendedUse, WorkingReaderScope, QualificationWindow>
  Evidence basis checked: <EvaluationEvidenceBasis>
  Status: <PatternQualityStatus>
```

| PrecisionRestorationProfile | OverallEffect | KindRestorationCheck | Loci | AffectedCoordinates | RepairProposal |
|---|---|---|---|---|---|
| `<word, head, and use; phrase-apparatus; repetition-and-distribution; ontic-slot; description-publication-source; pattern-application profile>` | `<clean | boundedLocal | lowersCoordinates | repairBeforeUse>` | `<pre-repair and post-repair kind, relation, current ontic slot, relation position, use relation, or claim kind, and not-triggered, ordinary, preserved, split, changed, or blocker disposition>` | `<by-value loci or absence scope>` | `<affected coordinates or none>` | `<repair, no-repair disposition with loci, or owning locus>` |

| Coordinate | Value | ShortRationale |
|---|---:|---|
| `<all RequiredPatternQualityCoordinates rows>` | `<0..5>` | `<assigned-value basis; why not lower; why not higher or what would lower or reopen>` |

```text
First repair or stop: <repair | hold | local stop>
Reopen if: <smallest changed locus or condition>
```

Status is not assigned from a two-column table, a prose summary, a checklist count, an E.19 pass or fail row, a table missing `ShortRationale`, a result missing the required `PrecisionRestorationProfile`, or a result missing the evidence basis needed for its values. Such material can support later assessment work, but it is not the E.21 result episteme. Conversely, the local `PatternQualityStatus` asserted by that result is not a release crossing: separate E.19 review work and result, plus the authority-bearing release or admission work/decision named by value, govern gate-specific carry-through, projection, monolith, packaging, authority, and non-overread conditions.

#### E.21:4.7 - Finding and proposal rows

```text
E.21 finding:
  Pattern of concern: <PatternOfConcernRef>
  Coordinate or status affected: <coordinate | status | stop>
  Pattern locus: <section, row, example, relation, source row, projection>
  Value or status effect: <value, status, floor, or stop impact>
  Correction direction: <what should change>
  Closure test: <what changed pattern text would show>
```

When `E.22`, `E.23`, returned-finding absorption, or `exceptionalImprovementEvaluation` asks for improvements, add finding rows for every below-floor coordinate and proposal rows only for substantive non-dominated improvement opportunities inside the declared scope. Do not treat every value below `5` as a defect. For above-floor coordinates, the evaluator still searches by value when exceptional improvement is requested, but the proposal must name a content improvement such as stronger positive action guidance, a worked slice, case or countercase, source-currentness carry-through, mature-content discharge, relation cleanup, deletion of displaced apparatus, split of overloaded content, or another content gain. A `4` can be the correct stop value only with a checked no-proposal disposition showing why further content movement is dominated, unavailable, or outside scope.


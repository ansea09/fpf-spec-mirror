---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__005_solution.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:4 — Solution"
line_start: 67384
line_end: 67603
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.19"
  - "E.2.DA"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "J.4"
keywords:
---

### E.21:4 - Solution

`E.21` is the FPF pattern-quality specialization of `A.19.ECS`. It evaluates one pattern of concern under one declared quality claim.

There is one evaluation shape:

1. frame the object and use;
2. apply the ordinal scale to every required coordinate;
3. justify each value with `ShortRationale`;
4. assign `PatternQualityStatus`;
5. state stop, repair, architecture hold, or refresh condition;
6. when improvement is requested, return proposal rows without changing the coordinate result into a work plan.

There is no separate pre-check result. If a pattern lacks frame, first move, source basis, mature comparison, or naming clarity, the relevant coordinates fall.

#### E.21:4.1 - Local names and kind settlement

| Local name | Kind and role |
|---|---|
| `PatternQualityEvaluation` | Authored quality evaluation record over one pattern of concern. |
| `PatternOfConcernRef` | Exact FPF pattern that this `E.21` evaluation makes the pattern of concern: host, monolith section, edition, or pinned version. `PatternOfConcern` is role-relative: the same pattern can also be the pattern of concern for another role in another flow, for example when a reader selects, applies, or reviews that pattern. This row names the concern of the quality-evaluation flow, not a special kind of pattern and not a second text. The evaluated pattern also has its own primary `EntityOfConcern`: the subject that its Problem/Solution/guidance is about. FPF patterns are applied to situations, claims, texts, or work objects. Use `governing pattern` only in the typed form `governing pattern for <claim/relation/boundary>` when the pattern actually governs that specific item; use `related pattern` for a looser pattern relation; use `relation` only for the relation itself. |
| `ClaimScope` | Quality claim boundary recovered from the governing frame: ordinary use, authoring input, landing input, release input, external-review input, high-assurance reuse input, canonization input, or another explicitly requested pattern-quality use. It is not chosen by the evaluator to make a failing request pass. |
| `WorkingReaderScope` | Reader role and first-use situation the pattern must serve. |
| `IntendedUse` | Action that may use the result: continue drafting, admit for declared use, repair, refresh, or compare candidates. |
| `QualificationWindow` | Edition, SoTA, related-pattern, release, time, or comparison window in which the evaluation is current. |
| `EvaluationEvidenceBasis` | Exact checked evidence loci for the evaluation: pattern body version, host or monolith section, ToC or `J.4` row when corpus-facing, card or retrieval cue when claimed, source-currentness locus when SoTA/currentness is valued, mature comparator set when maturity is valued, and worked case or absence of worked case when case coverage is valued. |
| `QualityEvaluationQuestionFrameRef` | `E.22` frame when purpose, floor, trade-offs, absorption, or proposal expectation needs to be declared. |
| `CoordinateValueRationales` | One row for every required coordinate: `Coordinate`, `Value`, `ShortRationale`. |
| `CoordinateEvidenceRefs` | Per-coordinate text, case, relation, SoTA, mature comparator, projection, or review refs where the short rationale depends on evidence outside the pattern body row being discussed. |
| `PrecisionRestorationProfile` | Compact profile over five precision-restoration layers: word/head/use precision, phrase-level apparatus, repeated or distributed material, role/carrier separation, and pattern-application ontology. It collapses those layers into one scalar effect for the `E.21` result, not one coordinate per defect. The profile names present or bounded issues, checked absence scope when clean, affected coordinates, and the exact restoration or governing pattern such as `E.10`, `E.10.ARCH`, `F.18`, `F.19`, or an object-specific pattern. |
| `DominanceSet` | Coordinates used to compare already evaluated candidate versions. It never changes the required coordinate set. |
| `PatternQualityStatus` | Scoped pattern-quality result assigned by `E.21`; it is not an `E.19` admission or refresh decision by itself. |
| `StopCondition` | Why improvement may stop, continue, refresh, or hold. |
Names are local to pattern-quality evaluation unless `F.18` promotes a durable name. They are not project evidence, release state, review state, or assurance.

#### E.21:4.2 - Evaluation record

```text
PatternQualityEvaluation:
  PatternOfConcernRef: <exact pattern of concern>
  ClaimScope: <declared quality claim>
  WorkingReaderScope: <reader and first-use situation>
  IntendedUse: <what may consume the result>
  QualificationWindow: <edition/source/neighbour/release/comparison window>
  EvaluationEvidenceBasis: <checked pattern, corpus, source, comparator, case, and projection loci; missing or unchecked loci named explicitly when they affect values>
  PrecisionRestorationProfile: <collapsed profile: word/head/use, phrase-apparatus, repetition/distribution, role-carrier, pattern-application; scalar effect, affected coordinates, and exact restoration or governing pattern>
  CoordinateValueRationales: <all required coordinates, values, short rationales>
  PatternQualityStatus: <status>
  StopCondition: <local stop, first repair, hold, or refresh>
```

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
| `<E.21 coordinate>` | `<0..5>` | `<assigned-value basis; why the lower adjacent value would understate the evidence; why the higher adjacent value would overstate the evidence, or for 5 what evidence makes 4 too weak and what would lower/reopen>` |

A two-column coordinate/value table, a narrative paragraph, a table whose comment lacks adjacent-value comparison, or a result whose value depends on unchecked external loci is not an `E.21` result. It is only draft evaluation material until every coordinate has a `ShortRationale` row and the result names the `EvaluationEvidenceBasis` used for values that depend on source, comparator, corpus, projection, or worked-case evidence.

A `ShortRationale` is allowed to be compact, but it is not allowed to be evidenceless. When the value depends on a source-currentness row, mature comparator, ToC or `J.4` projection, card, retrieval cue, monolith section, worked slice, near-miss, or anti-case, the rationale names that locus by value or says that the locus was missing or unchecked. "By value" means a recoverable section, row, case, checklist item, relation, source row, projection row, comparator id plus selected ingredient, or exact absent locus; a category list such as "entry, first move, boundaries, SoTA, checklist, relations" is not by-value discharge. Missing or unchecked evidence lowers the value for the coordinate that needs it; it does not create a separate "not evaluated" result.

A `5` is not a reward for clear early wording, named neighbour relations, or a well-formed field set alone. It needs exceptional expression for the declared use: reinforcing loci, a worked or otherwise replayable slice where the coordinate demands one, and no hidden cost or neighbour loss. When the evaluator cannot say why `4` would understate the evidence, assign `4` or lower.

When a coordinate's `5` meaning names a filled case, replayable slice, near-miss, anti-case, worked comparison, projection evidence, currentness basis, or exact-neighbour replay, absence of that evidence caps that coordinate at `4` even if the prose is otherwise strong. Do not hide the same absence only in `CaseCountercaseAndTransferCoverage`; lower every coordinate whose own `5` meaning needs that missing evidence. A `5` rationale names the reinforcing evidence loci that make `4` too weak.

For `MaturePatternParityAndSelectedContentSufficiency`, the rationale names a mature-pattern comparison set and the selected mature ingredients being claimed. For non-epistemic patterns, include at least one mature non-epistemic comparator when one exists: work, method, role, system, control, architecture, selection, engineering-action, or another pattern whose primary `EntityOfConcern` is not an episteme or publication. Value `4` requires by-value discharge of selected ingredients in the body or exact neighbours; comparator IDs plus a generic "main ingredients are present" sentence are only value `3`. The comparison is not a length target and not permission to copy semio apparatus.

For a `4` or `5` on `MaturePatternParityAndSelectedContentSufficiency`, include a compact maturity-discharge payload in the rationale or `CoordinateEvidenceRefs`: `comparator=<pattern id>; selectedIngredient=<ingredient name>; currentLocus=<section, row, case, checklist item, relation, or exact neighbour>; missingOrLowering=<absent or weak ingredient, if any>`. A category list such as "frame, first move, neighbour relations, CC, SoTA, relations" without current loci is still value `3`, even when the listed categories are plausible mature ingredients.

#### E.21:4.3a - Precision-restoration profile

Before assigning the coordinate table, record one `PrecisionRestorationProfile`. This is not an optional scan and not a lexical grep result. It is a role-based attention discharge: the evaluator asks what work the sentence, table, section, or repeated content family is doing in the pattern of concern.

Use this compact shape:

```text
PrecisionRestorationProfile:
  overallEffect: <clean | boundedLocal | lowersCoordinates | repairBeforeUse>
  wordHeadUsePrecision: <clean | E.10/E.10.ARCH/F.18/exact-pattern needed | lowers coordinates>
  kindRestorationCheck: <pre-repair kind/relation/slot-or-use-position/admissible use -> proposed post-repair kind/relation/slot-or-use-position/admissible use; preserved | split | intentionally changed | blocker>
  phraseApparatus: <clean | F.19 needed | lowers coordinates>
  repetitionAndNegativeDistribution: <clean | bounded-local | lowers coordinates>
  roleCarrierSeparation: <clean | quality/development/projection carrier leakage | lowers coordinates>
  patternApplicationOntology: <clean | application relation unclear | lowers coordinates>
  checkedLoci: <sections/rows/cases/relations checked>
  affectedCoordinates: <coordinates lowered or protected>
  repairProposal: <repair, no-repair disposition with loci, or owning locus>
```

This profile deliberately collapses several small subreadings into one scalar effect. The scalar is the strongest quality effect that any layer requires: clean, bounded local repair, coordinate lowering, or repair-before-use. The layers are diagnostic, not extra coordinates, checklists, or proposal quotas. A new precision-restoration symptom is classified into one of these layers or assigned to the exact restoration or governing pattern; it does not mint a new `E.21` coordinate. Details belong in the patterns that govern those objects: word/head/name problems apply `E.10`, `E.10.ARCH`, or `F.18`; phrase-level boilerplate and plain-technical rewriting apply `F.19`; claim, relation, evidence, work, decision, assurance, publication, or pattern-application problems apply the exact pattern that governs that object. `E.21` consumes only the result: which coordinates fall, which stay protected, and what repair would make the quality claim true.

The `kindRestorationCheck` is required whenever a precision-restoration finding or repair proposal changes wording. It records the meaning-bearing object, kind, relation, slot or use-position, admissible use, and scope before and after the proposed repair, then names the exact governing pattern when another pattern governs the live kind, relation, claim, or position (`A.6.0`/`A.6.5`, `A.6.P`, `C.29`, `A.15`, `E.10.ARCH`, or another exact pattern). `E.21` does not restate slot discipline or mathematical-lens ontology; it only checks that the repair preserved or deliberately changed them by value. The check is a bounded complete preservation proof, not a blanket demand to formalize every sentence and not a license to do the least visible work. Complete means every live field that can drift because of the changed wording receives one explicit disposition: `not triggered/ordinary prose/no FPF-governed phrase changed` with checked loci, `preserved`, `split`, `intentionally changed by accepted decision`, or `blocker`. A no-repair result is valid only as one of those dispositions with loci; "nothing to do" without that discharge is a missing repair. Expand the row only when a live kind, relation, claim, slot/use-position, or admissible use can drift. A lexical replacement is not a repair when it only removes a trigger word, substitutes one umbrella for another, narrows a graph or method into a work sequence, widens a work occurrence into a method, turns a publication or evidence carrier into the object itself, or otherwise changes kind or slot/use-position without an accepted decision. If the kind or slot/use-position cannot be recovered, the profile is at least `lowersCoordinates`; if the proposed repair would change kind or slot/use-position and no accepted DRR or exact governing pattern justifies that change, the result is `repairBeforeUse` or `holdForArchitectureDecision`.

When the profile is not clean, lower every affected coordinate named by the profile. Do not hide a present precision-restoration issue only in `EntityOfConcernPrimacyAndSemioBiasResistance`, and do not raise the result through related-pattern-boundary praise, projection evidence, or "correct but true" guards when the profile shows that those materials compete with the positive subject/action spine.

#### E.21:4.4 - RequiredPatternQualityCoordinates

Every `E.21` evaluation of an FPF pattern of concern evaluates every coordinate below.

| Coordinate | What it evaluates |
|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | Whether the reader recognises the situation, ordinary use, non-use, harm if missed, and boundary early. |
| `EntityOfConcernAndClaimScopeStability` | Whether the primary `EntityOfConcern` and quality-claim scope stay stable across title, Problem frame, Solution, cases, checklist, relations, and status. |
| `ActionPathGuidance` | Whether the Solution gives a usable action path after the first move is recovered. |
| `ClosureAndBoundedNonUseRecoverability` | Whether stop conditions, repair conditions, bounded non-use, and any `governing pattern for <claim/relation/boundary>` statements are recoverable. |
| `SemanticKindAndNameRecoverability` | Whether names, kinds, relations, qualifiers, and claim boundaries recover the same FPF interpretation. |
| `NeighborAuthorityAndBoundedUseFit` | Whether evidence, assurance, measurement, naming, work, gate, decision, publication, release, and project claims stay with the exact pattern that governs each claim, relation, or boundary. |
| `EntityOfConcernPrimacyAndSemioBiasResistance` | Whether the pattern leads with its own `EntityOfConcern` and action move instead of letting description, publication, source, evidence, review talk, standard non-use warnings, precision-repair material, quality/projection evidence, package rationale, or cross-pattern reference apparatus take over. The `PrecisionRestorationProfile` supplies the collapsed diagnosis across word/head/use precision, phrase apparatus, repetition/distribution, role/carrier separation, and pattern-application ontology. This coordinate consumes that profile by lowering the value when those materials compete with the positive subject/action spine. Semio-bias is one special case when the displaced content concerns descriptions, sources, publications, notes, records, diagrams, or evidence-like artifacts. |
| `PracticalUseDeltaAndHarmPrevention` | Whether the pattern changes a real reader move, prevents a named misuse, reduces a named cost, or preserves a named boundary. |
| `UseAffordabilityAndApparatusProportionality` | Whether ordinary first use stays affordable and heavier apparatus appears only when it buys admissible use. |
| `RepairLocalityAndChangeImpactPredictability` | Whether repairs have the smallest locus and predictable downstream impact. |
| `ProxyForValueSubstitutionResistance` | Whether the evaluation asks what became worse when visible quality coordinates improved. |
| `ClaimJustificationTraceabilityCurrentnessAndReplayability` | Whether the claim is replayable from pinned text, scope, evidence, currentness basis, limitations, status, and stop reason. |
| `CaseCountercaseAndTransferCoverage` | Whether positive cases, near-misses, anti-cases, and transfer cases match the breadth claimed. |
| `MaturePatternParityAndSelectedContentSufficiency` | Whether selected mature-pattern ingredients are present in the body or exact related patterns for this `EntityOfConcern` and use. |
| `SoTABindingAndCurrentness` | Whether current best-known practice changes the pattern and has reopen/currentness discipline. |
| `FormalClaimLegalityAndLensFit` | Whether measurement, scale, comparison, formal model, simulation, causal, mathematical, QL, or learned-lens claims are legal and bounded, or correctly absent. |
| `FalsifiabilityAndLoweringCondition` | Whether coordinate values, status, and stop claims say what would raise, lower, or reopen the evaluation. |
| `CorpusEntryProjectionAndEcologyFit` | Whether ToC, `J.4`, Preface cues, cards, summaries, retrieval snippets, durable names, relations, and corpus ecology preserve the scoped quality result without becoming authority faces, stale echoes, or pattern content. Corpus-entry and projection evidence belongs in the `E.21` result, `E.19` run record, ToC/J.4, retrieval/card carrier, or other quality carrier unless the pattern of concern's own `EntityOfConcern` and user move are that projection or evaluation work. |
| `EvolutionFrontAndRefreshDiscipline` | Whether variants, fronts, archives, refresh windows, and smallest-reopen rules preserve open-ended evolution without endless polishing. |

Constraint, harm, safety, security, compliance, deontic, self-application, recursion, and high-assurance questions do not add a second coordinate family. Evaluate them through the coordinate that owns the content: related-pattern authority, traceability, formal legality, falsifiability, affordability, corpus ecology, or evolution/refresh.

**Coupled-flow unity/separation for pattern quality.** An `E.21` run evaluates a `PatternOfConcernRef` inside a development, refresh, or admission flow. Another flow may make the same pattern a pattern of concern for a different role, for example a practitioner selecting and using it, a reviewer applying it to another text, or a later evaluator reopening it. One `TransductionGraph` may join pattern development, pattern use, use-found evaluation, and repair or refresh flows through transfer, feedback, return, edition-change, or projection relations. Keep three roles distinct in each sentence: the pattern as concern of the current flow, the intended reader addressed by the pattern, and the pattern's own primary `EntityOfConcern` inside its Problem/Solution/guidance. `E.21`, `E.19`, handoffs, ledgers, ToC/J.4/retrieval checks, and landing evidence are checking operations or carriers in the development or evaluation flow. They can cause edits to the pattern, but they are not automatically user-facing content for the role addressed by the pattern. `DesignRunTag` stays on the subject-context, claim, work, trace, or artifact relation inside the TGA graph; it does not decide whether a pattern is current, obsolete, under development, or being used. Treat FPF pattern development as the local pilot case: quality-loop proof changes the pattern through edits, not by being copied into the pattern.

#### E.21:4.4a - Frequent 3/4/5 calibration points

These rows calibrate common disagreements. They do not replace the coordinate definitions above.

| Coordinate family | 3 is typical when | 4 is typical when | 5 is typical when |
|---|---|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | The use situation is recoverable but late, abstract, or missing harm/payoff/non-use detail. | The situation, first move, harm, payoff, and non-use are early and clear. | Early recognition is reinforced by a filled or replayable first-use slice showing that a cold practitioner can enter correctly. |
| `EntityOfConcernAndClaimScopeStability` | The primary object is named but related record, evidence, lens, or project claims keep pulling the scope. | The primary `EntityOfConcern` and claim scope stay stable, with bounded related-pattern material. | Scope stability is reinforced across title, recognition text, Solution, worked or replayable case material, checklist, relations, and non-use without any local apparatus stealing attention. |
| `ActionPathGuidance` | The move is named but only partly executable, or the Solution mostly assigns governing loci instead of giving this pattern's own action. | The first move and continuation are executable in this pattern's own subject terms; related-pattern statements are declarative, compact, and late. | The action path is demonstrated by a filled worked slice or equivalent replayable evidence. |
| `ClosureAndBoundedNonUseRecoverability` | Non-use or related-pattern statements are present but not tied to stop, repair, or lowering conditions. | Stop, repair, bounded non-use, and governing-pattern statements for specific claims, relations, or boundaries are recoverable for declared use. | A worked stop, overturn, or non-use case shows how closure changes status or the next applicable pattern relation. |
| `NeighborAuthorityAndBoundedUseFit` | Related patterns are named but some authority split remains generic, future-pattern-like, ambiguous, role-nicknamed, or too early in the Solution. | Exact related patterns and limited declarative relations are clear enough for declared use and do not replace the pattern's own content. | Related-pattern authority is replayable across examples, relations, and overread cases, with pattern application and authority kept explicit. |
| `EntityOfConcernPrimacyAndSemioBiasResistance` | The pattern is about its object but one or more precision-restoration layers lead or leak into the pattern in a developer/reviewer/evaluator role. | The pattern leads with its own object and action path; auxiliary material is compact, declarative, and late; role/carrier/locus/flow/status words are used only when they add a real kind, relation, evidence value, or user move; quality/projection evidence about the pattern stays outside the pattern. | The primary object and action spine are first recoverable across recognition text, Solution, cases, and checks even when auxiliary material is present, and any precision-restoration or quality/projection material is in its proper carrier rather than in the pattern. |
| `PracticalUseDeltaAndHarmPrevention` | The prevented harm is named but not demonstrated. | The pattern changes a recoverable move and blocks named misuse for declared use. | A worked or near-miss case shows the practical delta, cost of the missed pattern, and prevented harm. |
| `UseAffordabilityAndApparatusProportionality` | The first move exists but apparatus is heavy for ordinary readers. | Ordinary first use is affordable and heavier apparatus opens only when useful. | A minimal first-use example shows the thin path works before heavy apparatus. |
| `RepairLocalityAndChangeImpactPredictability` | Repair conditions or related-pattern relations are named but downstream impact is not shown. | Repairs have local loci and predictable impact for declared use. | A worked repair or downstream-impact slice shows the smallest locus and changed related-pattern relation. |
| `ProxyForValueSubstitutionResistance` | Proxy risks are named but "what got worse" is not applied. | The pattern blocks visible proxy substitutions and asks what worsened. | A proxy-failure case shows a visible improvement damaging intended value, and the pattern prevents that stop. |
| `ClaimJustificationTraceabilityCurrentnessAndReplayability` | Fields or sources exist but replayability/currentness basis is incomplete. | The claim can be replayed from pinned text, evidence, currentness basis, status, and stop reason. | A filled evidence/currentness slice shows how the claim is replayed and when it reopens. |
| `CaseCountercaseAndTransferCoverage` | Archetypes are listed, but no filled worked case or near-miss exercises the claim. | At least one filled worked case plus a near-miss or anti-case covers the declared use. | Heterogeneous cases, countercases, and transfer slices cover the breadth claimed. |
| `MaturePatternParityAndSelectedContentSufficiency` | Mature comparators are named or implied, but selected mature ingredients are not discharged by value. | Mature comparators are named and selected ingredients are discharged by value in the body or exact related patterns. | Mature parity is shown across reinforcing body sections, related patterns, omissions, cases, and lowering conditions without copying irrelevant apparatus. |
| `SoTABindingAndCurrentness` | Sources are relevant and not decorative, but currentness, source-use status, or reopen conditions are compact or incomplete. | Load-bearing sources state adopt/adapt/reject, content mutation, currentness window, and reopen condition. | The pattern compares current best-known practice against popular, official, or lineage alternatives and carries the resulting source decisions into solution, cases, boundaries, and refresh. |
| `FormalClaimLegalityAndLensFit` | Formal, scale, lens, or measurement terms are bounded but not exercised. | Formal/lens/measurement claims are legal, bounded, and governed by exact related patterns when the pattern makes those claims. | A worked formal/lens/scale comparison shows what is preserved, lost, admissible, and not proved. |
| `FalsifiabilityAndLoweringCondition` | Stop, waiver, or non-use fields exist, but lowering and reopen triggers for the main claims are mostly implicit. | The pattern states explicit lowering/reopen triggers for its main claims; named fields alone do not reach `4` unless they say what evidence change lowers, overturns, rejects, or reopens the claim. | Worked lowering or overturn cases show how values, status, or use change. |
| `CorpusEntryProjectionAndEcologyFit` | Host text is coherent, but ToC, `J.4`, card, retrieval, monolith, or projection evidence is absent for a corpus-facing claim, or that evidence is placed anywhere in the pattern as method, note, appendix, relation, rationale, or quality-status content about the pattern. | Corpus-facing entry/projection loci are named and aligned enough for the declared use, and their evidence stays in the evaluation/result/projection carrier rather than entering the pattern. | Retrieval, stale-projection, cold-reader, or projection-update evidence shows corpus ecology stays aligned after change without leaking into the pattern. |
| `EvolutionFrontAndRefreshDiscipline` | Reopen is delegated to related patterns or implied by source-return. | The smallest reopen locus, source/currentness trigger, or variant/front condition is explicit. | Variant/front/archive or ongoing refresh discipline is replayable for the declared use. |

For `EntityOfConcernPrimacyAndSemioBiasResistance`, do not compensate a bad `PrecisionRestorationProfile` with `NeighborAuthorityAndBoundedUseFit` or `CorpusEntryProjectionAndEcologyFit`. This is a role-based evaluation, not a lexical search: ask what role the sentence plays. Material about developing, reviewing, projecting, landing, evaluating, or proving this pattern's quality belongs in the carrier that owns that work, not in the pattern. Exact related-pattern statements can be true and still damage the pattern of concern when they appear before the pattern's own `EntityOfConcern` and action spine are recoverable. If the opening Problem frame or Solution starts with precision-restoration material before the pattern's own subject and move, this coordinate is at most `2`; if a positive action exists but the reader must traverse that material across sections to find it, it is at most `3`. Compact related-pattern statements belong in `Relations` or short late boundary rows and must preserve kind. Local boundary prose is admissible only when it states a documented local confusion and exact stop condition not already carried by the owning pattern for that specific distinction or claim boundary. Also lower `ActionPathGuidance`, `WorkingSituationAndUseBoundaryRecognizability`, `PracticalUseDeltaAndHarmPrevention`, and `UseAffordabilityAndApparatusProportionality` when the profile shows that precision-restoration issues displace first-use content.
If the declared use is `Stable`, landing-input, release-input, external-review-ready, or another corpus-facing use, the evaluation must use evidence for corpus entry and projection coordinates. A host-only body evaluation can still evaluate the pattern body, but it cannot silently turn missing ToC, `J.4`, card, retrieval, monolith, or projection evidence into a high `CorpusEntryProjectionAndEcologyFit` value.

#### E.21:4.5 - Status and stop condition

| Status | Meaning |
|---|---|
| `admissibleForDeclaredUse` | Every coordinate meets the declared floor for the scoped use, and bounded non-use is stated. |
| `repairBeforeUse` | One or more coordinate floors fail for the declared use. |
| `holdForArchitectureDecision` | The defect is not local prose; `EntityOfConcern`, neighbour authority, split, merge, or placement must be decided. |
| `refreshNeeded` | A SoTA, neighbour, terminology, retrieval, telemetry, use-scope, or corpus change invalidates a previous evaluation. |

Default floor is `4 wellExpressedForDeclaredUse` on every coordinate for ordinary practitioner use, authoring-input use, landing-input use, `Stable`, external-review-ready, release-input, canonization-input, stop-improving claims, and ordinary improvement-loop use. A diagnostic or exploratory request still measures every coordinate and reports values; it does not create an admissible-use shortcut. If the assignment asks for corpus-facing, landing-input, `Stable`, release, or external-review use, the evaluator measures that required use and returns `repairBeforeUse`, `holdForArchitectureDecision`, or `refreshNeeded` when the floor is missed.

An all-`5` result is a local exceptional result under the declared scope and qualification window. It is not a permanent end of development. `E.23` can reopen improvement when use, source, comparison set, front, affordability, or payoff changes.

#### E.21:4.6 - Compact result form

An `E.21` result uses this result-bearing form:

```text
E.21 result:
  Pattern of concern: <PatternOfConcernRef>
  Declared scope/use/reader/window: <ClaimScope, IntendedUse, WorkingReaderScope, QualificationWindow>
  Evidence basis checked: <EvaluationEvidenceBasis>
  Status: <PatternQualityStatus>
```

| PrecisionRestorationProfile | OverallEffect | KindRestorationCheck | Loci | AffectedCoordinates | RepairProposal |
|---|---|---|---|---|---|
| `<word/head/use / phrase-apparatus / repetition-distribution / role-carrier / pattern-application profile>` | `<clean | boundedLocal | lowersCoordinates | repairBeforeUse>` | `<pre/post kind, relation, slot/use-position, and not-triggered/ordinary/preserved/split/changed/blocker disposition>` | `<by-value loci or absence scope>` | `<affected coordinates or none>` | `<repair, no-repair disposition with loci, or owning locus>` |

| Coordinate | Value | ShortRationale |
|---|---:|---|
| `<all RequiredPatternQualityCoordinates rows>` | `<0..5>` | `<assigned-value basis; why not lower; why not higher or what would lower/reopen>` |

```text
First repair or stop: <repair | hold | local stop>
Reopen if: <smallest changed locus or condition>
```

Status is not assigned from a two-column table, a prose summary, a checklist count, an `E.19` pass/fail row, a table missing `ShortRationale`, a result missing the required `PrecisionRestorationProfile`, or a result missing the evidence basis needed for the values it claims. Such material can support a later evaluation, but it is not the `E.21` result. Conversely, an `E.21` status is a pattern-quality status, not a release crossing: `E.19` or the exact release/admission process still checks gate-specific carry-through, projection, monolith, packaging, authority, and non-overread conditions.

#### E.21:4.7 - Finding and proposal rows

```text
E.21 finding:
  Pattern of concern: <PatternOfConcernRef>
  Coordinate or status affected: <coordinate | status | stop>
  Pattern locus: <section, row, example, relation, source row, projection>
  Value or status effect: <value/status/floor/stop impact>
  Correction direction: <what should change>
  Closure test: <what changed pattern text would show>
```

When `E.22`, `E.23`, returned-finding absorption, or `exceptionalImprovementEvaluation` asks for improvements, add proposal rows for every below-target coordinate, status weakness, stop-condition weakness, or open question that can be improved within the declared scope. One proposal may cover several coordinates only when it names all affected coordinates and the shared repair.


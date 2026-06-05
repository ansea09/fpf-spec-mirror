---
chunk_kind: "parent"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/E.21.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
line_start: 67284
line_end: 67590
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
  - "J.4"
keywords:
---

## E.21 - FPF Pattern-Quality Evaluation CharacteristicSpace

Status: Core.

### E.21:1 - Problem frame

Use `E.21` when one authored FPF pattern version must be evaluated for quality under a declared use: ordinary practitioner use, authoring input, landing input, release input, external-review input, high-assurance reuse input, canonization input, or a narrower named use.

Not this pattern when the evaluated object is one `DRR`, an FPF-level corpus object, a single wording repair, a source-use decision, or a project-side evidence, assurance, gate, release, safety, compliance, work, or decision claim. Use `E.9.DA`, `E.2.DA`, `E.10` and exact precision-restoration neighbours, or the exact project-side pattern for those objects.

First useful move: name the exact pattern version, declared scope, working reader, intended use, and qualification window; then evaluate every coordinate in `RequiredPatternQualityCoordinates` with a value and short rationale.

`floorEvaluation` changes the declared floor and evidence depth. It does not remove coordinates. Fragmentary, wrong-shaped, or weak pattern text is still evaluated; weakness receives low coordinate values, repair status, narrowed-use status, or architecture hold.

What goes wrong if missed: pattern quality becomes taste, checklist closure, source count, review state, landing state, or length. Short patterns can pass while missing mature content; long patterns can pass while hiding the first user move; semio material can take over a non-semio pattern.

Primary EntityOfConcern in plain terms: the quality claim of one exact FPF pattern version for a declared use.

### E.21:2 - Problem

FPF patterns need a quality evaluation that is stronger than a style checklist and lighter than a project assurance audit. Earlier review habits produced two opposite failures:

1. **Too weak.** A reviewer marks a pattern "ready" because no blocker is obvious, because it landed, or because headings exist.
2. **Too heavy.** A reviewer adds more warnings, evidence cards, source rows, boundary notes, and process residues until the pattern becomes harder to use.

`E.21` solves this by measuring the pattern version against one complete coordinate set. The coordinates ask whether the pattern is usable, coherent, current, precise, affordable, mature enough for its claim, and safe from proxy improvement.

### E.21:3 - Forces

| Force | Tension |
|---|---|
| Comparability vs false precision | Pattern versions must be comparable, but ordinal qualities cannot be averaged. |
| Completeness vs affordability | Every coordinate is evaluated; rationale and evidence can stay compact. |
| Maturity vs length | A short pattern is mature only when selected mature-pattern ingredients are present in the body or exact neighbours. |
| Ontology vs usability | Names and kinds must be exact without burying the first user move. |
| Semio precision vs semio-bias | Episteme and publication distinctions matter, but non-semio patterns still lead with their own `EntityOfConcern`. |
| Open-ended improvement vs stop | Improvement can continue forever, while one version needs a scoped stop condition. |

### E.21:4 - Solution

`E.21` is the FPF pattern-quality specialization of `A.19.ECS`. It evaluates one pattern version under one declared quality claim.

There is one evaluation shape:

1. frame the object and use;
2. apply the ordinal scale to every required coordinate;
3. justify each value with `ShortRationale`;
4. assign `PatternQualityStatus`;
5. state stop, repair, narrowed use, architecture hold, or refresh condition;
6. when improvement is requested, return proposal rows without changing the coordinate result into a work plan.

There is no separate pre-check result. If a pattern lacks frame, first move, source basis, mature comparison, or naming clarity, the relevant coordinates fall.

#### E.21:4.1 - Local names and kind settlement

| Local name | Kind and role |
|---|---|
| `PatternQualityEvaluation` | Authored quality evaluation record over one pattern version. |
| `PatternVersionRef` | Exact host, monolith section, edition, or pinned pattern version. |
| `ClaimScope` | Quality claim boundary: ordinary use, authoring input, landing input, release input, external-review input, high-assurance reuse input, canonization input, or narrower use. |
| `WorkingReaderScope` | Reader role and first-use situation the pattern must serve. |
| `IntendedUse` | Neighbouring action that may consume the result: continue drafting, admit for declared use, narrow use, repair, refresh, or compare candidates. |
| `QualificationWindow` | Edition, SoTA, neighbour, release, time, or comparison window in which the evaluation is current. |
| `EvaluationEvidenceBasis` | Exact checked evidence loci for the evaluation: pattern body version, host or monolith section, ToC or `J.4` row when corpus-facing, card or retrieval cue when claimed, source-currentness locus when SoTA/currentness is valued, mature comparator set when maturity is valued, and worked case or absence of worked case when case coverage is valued. |
| `QualityEvaluationQuestionFrameRef` | `E.22` frame when purpose, floor, trade-offs, absorption, or proposal expectation needs to be declared. |
| `CoordinateValueRationales` | One row for every required coordinate: `Coordinate`, `Value`, `ShortRationale`. |
| `CoordinateEvidenceRefs` | Per-coordinate text, case, relation, SoTA, mature comparator, projection, or review refs where the short rationale depends on evidence outside the pattern body row being discussed. |
| `DominanceSet` | Coordinates used to compare already evaluated candidate versions. It never changes the required coordinate set. |
| `PatternQualityStatus` | Scoped use result. |
| `StopCondition` | Why improvement may stop, continue, narrow, refresh, or hold. |
Names are local to pattern-quality evaluation unless `F.18` promotes a durable name. They are not project evidence, release state, review state, or assurance.

#### E.21:4.2 - Evaluation record

```text
PatternQualityEvaluation:
  PatternVersionRef: <exact pattern version>
  ClaimScope: <declared quality claim>
  WorkingReaderScope: <reader and first-use situation>
  IntendedUse: <what may consume the result>
  QualificationWindow: <edition/source/neighbour/release/comparison window>
  EvaluationEvidenceBasis: <checked pattern, corpus, source, comparator, case, and projection loci; missing or unchecked loci named explicitly when they affect values>
  CoordinateValueRationales: <all required coordinates, values, short rationales>
  PatternQualityStatus: <status>
  StopCondition: <local stop, first repair, narrowed use, hold, or refresh>
```
#### E.21:4.3 - Ordinal scale, result row, and adjacent-value rationale

| Value | Label | Meaning |
|---:|---|---|
| 0 | `absent` | The characteristic is not expressed for the declared scope. |
| 1 | `namedOnly` | It is named or implied but not usable as quality evidence. |
| 2 | `partiallyExpressedForDeclaredUse` | It is present but incomplete, fragile, or too narrow. |
| 3 | `sufficientlyExpressedForDeclaredUse` | It is usable for the declared scope, with limits visible. |
| 4 | `wellExpressedForDeclaredUse` | It is clear, evidenced, and bounded for the declared scope. |
| 5 | `exceptionallyExpressedForDeclaredUse` | It is exceptional for the declared use across reinforcing loci and cases, without hidden cost or neighbour loss. |

Values are ordinal content evaluations. They are not `U.Measure`s, averages, percentages, maturity-ladder steps, review votes, or landing status.

The result-bearing coordinate row has exactly this shape:

| Coordinate | Value | ShortRationale |
|---|---:|---|
| `<E.21 coordinate>` | `<0..5>` | `<assigned-value basis; why the lower adjacent value would understate the evidence; why the higher adjacent value would overstate the evidence, or for 5 what evidence makes 4 too weak and what would lower/reopen>` |

A two-column coordinate/value table, a narrative paragraph, a table whose comment lacks adjacent-value comparison, or a result whose value depends on unchecked external loci is not an `E.21` result. It is only draft evaluation material until every coordinate has a `ShortRationale` row and the result names the `EvaluationEvidenceBasis` used for values that depend on source, comparator, corpus, projection, or worked-case evidence.

A `ShortRationale` is allowed to be compact, but it is not allowed to be evidenceless. When the value depends on a source-currentness row, mature comparator, ToC or `J.4` projection, card, retrieval cue, monolith section, worked slice, near-miss, or anti-case, the rationale names that locus by value or says that the locus was missing or unchecked. "By value" means a recoverable section, row, case, checklist item, relation, source row, projection row, comparator id plus selected ingredient, or exact absent locus; a category list such as "entry, first move, boundaries, SoTA, checklist, relations" is not by-value discharge. Missing or unchecked evidence lowers the value for the coordinate that needs it; it does not create a separate "not evaluated" route.

A `5` is not a reward for clear early wording, named exits, or a well-formed field set alone. It needs exceptional expression for the declared use: reinforcing loci, a worked or otherwise replayable slice where the coordinate demands one, and no hidden cost or neighbour loss. When the evaluator cannot say why `4` would understate the evidence, assign `4` or lower.

When a coordinate's `5` meaning names a filled case, replayable slice, near-miss, anti-case, worked comparison, projection evidence, currentness basis, or exact-neighbour replay, absence of that evidence caps that coordinate at `4` even if the prose is otherwise strong. Do not hide the same absence only in `CaseCountercaseAndTransferCoverage`; lower every coordinate whose own `5` meaning needs that missing evidence. A `5` rationale names the reinforcing evidence loci that make `4` too weak.

For `MaturePatternParityAndSelectedContentSufficiency`, the rationale names a mature-pattern comparison set and the selected mature ingredients being claimed. For non-epistemic patterns, include at least one mature non-epistemic comparator when one exists: work, method, role, system, control, architecture, selection, engineering-action, or another pattern whose primary `EntityOfConcern` is not an episteme or publication. Value `4` requires by-value discharge of selected ingredients in the body or exact neighbours; comparator IDs plus a generic "main ingredients are present" sentence are only value `3`. The comparison is not a length target and not permission to copy semio apparatus.

For a `4` or `5` on `MaturePatternParityAndSelectedContentSufficiency`, include a compact maturity-discharge payload in the rationale or `CoordinateEvidenceRefs`: `comparator=<pattern id>; selectedIngredient=<ingredient name>; currentLocus=<section, row, case, checklist item, relation, or exact neighbour>; missingOrLowering=<absent or weak ingredient, if any>`. A category list such as "frame, first move, exits, CC, SoTA, relations" without current loci is still value `3`, even when the listed categories are plausible mature ingredients.
#### E.21:4.4 - RequiredPatternQualityCoordinates

Every `E.21` evaluation of an FPF pattern version evaluates every coordinate below.

| Coordinate | What it evaluates |
|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | Whether the reader recognises the situation, ordinary use, non-use, harm if missed, and boundary early. |
| `EntityOfConcernAndClaimScopeStability` | Whether the primary `EntityOfConcern` and quality-claim scope stay stable across title, Problem frame, Solution, cases, checklist, relations, and status. |
| `ActionPathGuidance` | Whether the Solution gives a usable action path after the first move is recovered. |
| `ClosureAndBoundedNonUseRecoverability` | Whether stop, repair, narrower use, and neighbouring-pattern exits are recoverable. |
| `SemanticKindAndNameRecoverability` | Whether names, kinds, relations, qualifiers, and claim boundaries recover the same FPF interpretation. |
| `NeighborAuthorityAndBoundedUseFit` | Whether evidence, assurance, measurement, naming, work, gate, decision, publication, release, and project claims stay with exact neighbours. |
| `EntityOfConcernPrimacyAndSemioBiasResistance` | Whether the pattern leads with its own `EntityOfConcern` and action move instead of letting description, publication, source, evidence, review talk, standard non-use warnings, or precision-repair material take over. |
| `PracticalUseDeltaAndHarmPrevention` | Whether the pattern changes a real reader move, prevents a named misuse, reduces a named cost, or preserves a named boundary. |
| `UseAffordabilityAndApparatusProportionality` | Whether ordinary first use stays affordable and heavier apparatus appears only when it buys admissible use. |
| `RepairLocalityAndChangeImpactPredictability` | Whether repairs have the smallest locus and predictable downstream impact. |
| `ProxyForValueSubstitutionResistance` | Whether the evaluation asks what became worse when visible quality coordinates improved. |
| `ClaimJustificationTraceabilityCurrentnessAndReplayability` | Whether the claim is replayable from pinned text, scope, evidence, currentness basis, limitations, status, and stop reason. |
| `CaseCountercaseAndTransferCoverage` | Whether positive cases, near-misses, anti-cases, and transfer cases match the breadth claimed. |
| `MaturePatternParityAndSelectedContentSufficiency` | Whether selected mature-pattern ingredients are present in the body or exact neighbours for this `EntityOfConcern` and use. |
| `SoTABindingAndCurrentness` | Whether current best-known practice changes live pattern content and has reopen/currentness discipline. |
| `FormalClaimLegalityAndLensFit` | Whether measurement, scale, comparison, formal model, simulation, causal, mathematical, QL, or learned-lens claims are legal and bounded, or correctly absent. |
| `FalsifiabilityAndLoweringCondition` | Whether coordinate values, status, and stop claims say what would raise, lower, or reopen the evaluation. |
| `CorpusEntryProjectionAndEcologyFit` | Whether ToC, `J.4`, Preface cues, cards, summaries, retrieval snippets, durable names, relations, and corpus ecology preserve the scoped quality result without becoming authority faces or stale echoes. |
| `EvolutionFrontAndRefreshDiscipline` | Whether variants, fronts, archives, refresh windows, and smallest-reopen rules preserve open-ended evolution without endless polishing. |

Constraint, harm, safety, security, compliance, deontic, self-application, recursion, and high-assurance questions do not add a second coordinate family. Evaluate them through the coordinate that owns the content: neighbour authority, traceability, formal legality, falsifiability, affordability, corpus ecology, or evolution/refresh.

#### E.21:4.4a - Frequent 3/4/5 calibration points

These rows calibrate common disagreements. They do not replace the coordinate definitions above.

| Coordinate family | 3 is typical when | 4 is typical when | 5 is typical when |
|---|---|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | The use situation is recoverable but late, abstract, or missing harm/payoff/non-use detail. | The situation, first move, harm, payoff, and non-use are early and clear. | Early recognition is reinforced by a filled or replayable first-use slice showing that a cold practitioner can enter correctly. |
| `EntityOfConcernAndClaimScopeStability` | The primary object is named but neighbouring record, evidence, lens, or project claims keep pulling the scope. | The primary `EntityOfConcern` and claim scope stay stable, with bounded neighbour material. | Scope stability is reinforced across title, recognition text, Solution, worked or replayable case material, checklist, relations, and non-use without any local apparatus stealing attention. |
| `ActionPathGuidance` | The move is named but only partly executable. | The first move and continuation are executable for declared use. | The action path is demonstrated by a filled worked slice or equivalent replayable evidence. |
| `ClosureAndBoundedNonUseRecoverability` | Exits or non-use are present but not tied to stop, repair, or lowering conditions. | Stop, repair, narrower use, and neighbour exits are recoverable for declared use. | A worked stop, overturn, or non-use case shows how closure changes status or next admissible pattern. |
| `NeighborAuthorityAndBoundedUseFit` | Neighbours are named but some authority split remains generic, future-receiver-like, or ambiguous. | Exact neighbours and limited relations are clear enough for declared use. | Neighbour authority is replayable across examples, relations, and overread cases, with no generic future receiver or unnamed neighbour carrying live authority. |
| `EntityOfConcernPrimacyAndSemioBiasResistance` | The pattern is about its object but semio, review, source, lens, or warning material often leads. | The pattern leads with its own object and action path; auxiliary material stays bounded. | The primary object remains dominant across recognition text, Solution, cases, and checks even when semio/lens/source material is present. |
| `PracticalUseDeltaAndHarmPrevention` | The prevented harm is named but not demonstrated. | The pattern changes a recoverable move and blocks named misuse for declared use. | A worked or near-miss case shows the practical delta, cost of the missed pattern, and prevented harm. |
| `UseAffordabilityAndApparatusProportionality` | The first move exists but apparatus is heavy for ordinary readers. | Ordinary first use is affordable and heavier apparatus opens only when useful. | A minimal first-use example shows the thin path works before heavy apparatus. |
| `RepairLocalityAndChangeImpactPredictability` | Repair exits are named but downstream impact is not shown. | Repairs have local loci and predictable impact for declared use. | A worked repair or downstream-impact slice shows the smallest locus and changed neighbour. |
| `ProxyForValueSubstitutionResistance` | Proxy risks are named but "what got worse" is not applied. | The pattern blocks visible proxy substitutions and asks what worsened. | A proxy-failure case shows a visible improvement damaging intended value, and the pattern prevents that stop. |
| `ClaimJustificationTraceabilityCurrentnessAndReplayability` | Fields or sources exist but replayability/currentness basis is incomplete. | The claim can be replayed from pinned text, evidence, currentness basis, status, and stop reason. | A filled evidence/currentness slice shows how the claim is replayed and when it reopens. |
| `CaseCountercaseAndTransferCoverage` | Archetypes are listed, but no filled worked case or near-miss exercises the claim. | At least one filled worked case plus a near-miss or anti-case covers the declared use. | Heterogeneous cases, countercases, and transfer slices cover the breadth claimed. |
| `MaturePatternParityAndSelectedContentSufficiency` | Mature comparators are named or implied, but selected mature ingredients are not discharged by value. | Mature comparators are named and selected ingredients are discharged by value in the body or exact neighbours. | Mature parity is shown across reinforcing body sections, neighbours, omissions, cases, and lowering conditions without copying irrelevant apparatus. |
| `SoTABindingAndCurrentness` | Sources are relevant and not decorative, but currentness, source-use status, or reopen conditions are compact or incomplete. | Load-bearing sources state adopt/adapt/reject, content mutation, currentness window, and reopen condition. | The pattern compares current best-known practice against popular, official, or lineage alternatives and carries the resulting source decisions into solution, cases, boundaries, and refresh. |
| `FormalClaimLegalityAndLensFit` | Formal, scale, lens, or measurement terms are bounded but not exercised. | Formal/lens/measurement claims are legal, bounded, and sent to exact neighbours when live. | A worked formal/lens/scale comparison shows what is preserved, lost, admissible, and not proved. |
| `FalsifiabilityAndLoweringCondition` | Stop, waiver, or non-use fields exist, but lowering and reopen triggers for the main claims are mostly implicit. | The pattern states explicit lowering/reopen triggers for its main claims; named fields alone do not reach `4` unless they say what evidence change lowers, overturns, narrows, or reopens the claim. | Worked lowering or overturn cases show how values, status, or use change. |
| `CorpusEntryProjectionAndEcologyFit` | Host text is coherent, but ToC, `J.4`, card, retrieval, monolith, or projection evidence is absent for a corpus-facing claim. | Corpus-facing entry/projection loci are named and aligned enough for the declared use. | Retrieval, stale-projection, cold-reader, or projection-update evidence shows corpus ecology stays aligned after change. |
| `EvolutionFrontAndRefreshDiscipline` | Reopen is delegated to neighbours or implied by source-return. | The smallest reopen locus, source/currentness trigger, or variant/front condition is explicit. | Variant/front/archive or ongoing refresh discipline is replayable for the declared use. |

If the declared use is `Stable`, landing-input, release-input, external-review-ready, or another corpus-facing use, the evaluation must use evidence for corpus entry and projection coordinates. A host-only body evaluation can still evaluate the pattern body, but it cannot silently turn missing ToC, `J.4`, card, retrieval, monolith, or projection evidence into a high `CorpusEntryProjectionAndEcologyFit` value.
#### E.21:4.5 - Status and stop condition

| Status | Meaning |
|---|---|
| `admissibleForDeclaredUse` | Every coordinate meets the declared floor for the scoped use, and bounded non-use is stated. |
| `admissibleWithNarrowerUse` | The pattern can serve only a narrower reader, use, scope, or claim. |
| `repairBeforeUse` | One or more coordinate floors fail for the declared use. |
| `holdForArchitectureDecision` | The defect is not local prose; `EntityOfConcern`, neighbour authority, split, merge, or placement must be decided. |
| `refreshNeeded` | A SoTA, neighbour, terminology, retrieval, telemetry, use-scope, or corpus change invalidates a previous evaluation. |

Default corpus-facing floor is `4 wellExpressedForDeclaredUse` on every coordinate for ordinary practitioner use, authoring-input use, landing-input use, `Stable`, external-review-ready, release-input, canonization-input, or stop-improving claims. A floor of `3` is admissible only for an explicitly narrowed diagnostic, exploratory, expert-only, source-basis, or local-reference use, and the status names the excluded broader use.

An all-`5` result is a local exceptional result under the declared scope and qualification window. It is not a permanent end of development. `E.23` can reopen improvement when use, source, comparison set, front, affordability, or payoff changes.

#### E.21:4.6 - Compact result form

An `E.21` result uses this result-bearing form:

```text
E.21 result:
  Pattern version: <PatternVersionRef>
  Declared scope/use/reader/window: <ClaimScope, IntendedUse, WorkingReaderScope, QualificationWindow>
  Evidence basis checked: <EvaluationEvidenceBasis>
  Status: <PatternQualityStatus>
```

| Coordinate | Value | ShortRationale |
|---|---:|---|
| `<all RequiredPatternQualityCoordinates rows>` | `<0..5>` | `<assigned-value basis; why not lower; why not higher or what would lower/reopen>` |

```text
First repair or stop: <repair | narrowed use | hold | local stop>
Reopen if: <smallest changed locus or condition>
```

Status is not assigned from a two-column table, a prose summary, a checklist count, a table missing `ShortRationale`, or a result missing the evidence basis needed for the values it claims. Such material can support a later evaluation, but it is not the `E.21` result.
#### E.21:4.7 - Finding and proposal rows

```text
E.21 finding:
  Pattern version: <PatternVersionRef>
  Coordinate or status affected: <coordinate | status | stop>
  Pattern locus: <section, row, example, relation, source row, projection>
  Value or status effect: <value/status/floor/stop impact>
  Correction direction: <what should change>
  Closure test: <what changed pattern text would show>
```

When `E.22`, `E.23`, returned-finding absorption, or `exceptionalImprovementEvaluation` asks for improvements, add proposal rows for every below-target coordinate, status weakness, stop-condition weakness, or open question that can be improved within the declared scope. One proposal may cover several coordinates only when it names all affected coordinates and the shared repair.

### E.21:5 - Worked slices

**Exact names, no first move.** A pattern has precise Tech names and current source rows but no first user move. `WorkingSituation...`, `ActionPathGuidance`, and `PracticalUseDelta...` fall; source currentness does not rescue ordinary use.

**Short architecture pattern.** A compact pattern has a triage form but no worked slice and no mature-pattern comparison. It can be admissible for a narrow expert use, but `MaturePatternParity...` and `CaseCountercase...` stay below exceptional until selected mature content is present.

**Semio-biased non-semio pattern.** A pattern about architecture, work, system levels, or method starts by saying what its description is not: not proof, not evidence, not decision. `EntityOfConcernPrimacyAndSemioBiasResistance` falls until the pattern leads with the primary object and action path, with standard non-use material moved to exact neighbours or a late boundary note.

**Quality table without rationale.** A result gives values but no adjacent-value rationale. Values are unsupported. Add `ShortRationale` or lower/narrow.

**Goodharted improvement.** A rewrite improves source refs and proof sketches but becomes hard to use. Re-evaluate affordability, repair locality, proxy-for-value, and corpus ecology before stopping.

### E.21:6 - Conformance checklist

| Check | Requirement |
|---|---|
| `CC-E21-1` | Name `PatternVersionRef`, `ClaimScope`, `WorkingReaderScope`, `IntendedUse`, `QualificationWindow`, and `EvaluationEvidenceBasis`. |
| `CC-E21-2` | Evaluate the full `RequiredPatternQualityCoordinates` set. |
| `CC-E21-3` | Use the result-bearing three-column table: coordinate, value, and `ShortRationale`; a two-column coordinate/value table is not an `E.21` result. |
| `CC-E21-4` | Let `floorEvaluation` change floor and evidence cost only, not the coordinate set. |
| `CC-E21-5` | Assign values from checked pattern content and named content evidence, not review, landing, popularity, praise, or absence of prior use. |
| `CC-E21-6` | For corpus-facing values, name the checked ToC, `J.4`, card, retrieval, monolith, or projection loci, or lower the affected coordinate when those loci are missing or unchecked. |
| `CC-E21-7` | For any `5`, name the reinforcing evidence loci required by that coordinate's `5` meaning; otherwise lower the coordinate to `4` or below. |
| `CC-E21-8` | For `MaturePatternParityAndSelectedContentSufficiency = 4` or `5`, include a compact maturity-discharge payload: comparator id, selected ingredient, current locus, and missing/lowering item if any; category lists without loci cap the coordinate at `3`. |
| `CC-E21-9` | Make SoTA rows adopt, adapt, or reject current practice and change live pattern content. |
| `CC-E21-10` | Send measurement, score, scale, formal, causal, mathematical, QL, simulation, representation, or learned-lens claims to `C.16`, `A.17`, `A.18`, `A.19`, or exact neighbours when live. |
| `CC-E21-11` | State floor satisfaction, remaining bounded non-use, and lowering or reopen conditions in any stop claim. |
| `CC-E21-12` | Keep coordinate rationale separate from improvement proposal rows. |
| `CC-E21-13` | Keep quality results out of project evidence, assurance, gate, work, safety/compliance, release, and publication truth claims. |
### E.21:7 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **Score illusion.** `Pattern quality = 87/100`. | Use ordinal coordinate values; no arithmetic aggregation. |
| **Two-column table.** Coordinate/value table has no rationale. | Add `ShortRationale` for every coordinate. |
| **Floor as omission.** A floor evaluation omits maturity, SoTA, formal, corpus, or evolution coordinates. | Keep floor low if needed; evaluate all coordinates. |
| **Administrative proxy.** "4 because landed" or "3 because not externally reviewed". | Evaluate pattern content. |
| **Comparator-free or locus-free maturity.** `MaturePatternParity... = 4` by impression, comparator IDs only, or category list such as "frame, first move, exits, CC, SoTA, relations". | Name mature comparison patterns and use the maturity-discharge payload: comparator, selected ingredient, current locus, and missing/lowering item. Without that payload, cap at `3`. |
| **Omission account as maturity.** A note explaining absence raises the value. | Add content to body/exact neighbour, lower value, or narrow use. |
| **Semio-biased maturity.** Non-semio pattern is judged by episteme/publication exemplars only. | Include non-epistemic mature comparators and score action on the primary `EntityOfConcern`. |
| **Apparatus maximalism.** Every pattern gets evidence cards, telemetry, archives, and companions. | Keep evidence compact unless it changes value, status, stop, or candidate comparison. |
| **Quality veto theatre.** "Not ready" has no exact E.21 locus, evidence, status effect, and repair. | Rewrite as an `E.21` finding or remove the veto. |

### E.21:8 - Consequences

| Benefit | Trade-off or mitigation |
|---|---|
| Pattern quality becomes inspectable without a fake score. | Authors must name scope and all coordinate values. |
| Compact evidence remains possible. | The coordinate table is still complete. |
| Maturity claims become harder to fake. | Mature-pattern comparison adds cost where maturity or corpus-facing use is claimed. |
| Semio-bias becomes visible. | Semio distinctions remain auxiliary unless they are the pattern's own `EntityOfConcern`. |
| Stop decisions become less taste-based. | Open-ended improvement remains possible through `E.23` when a stronger aim is live. |

### E.21:9 - Rationale

`E.21` keeps the measuring device simple: one object kind, one ordinal scale, one required coordinate set, one status set, and one stop condition. The evaluation never asks whether a coordinate is active. It asks what value the current pattern text earns under the declared use.

The mature-pattern parity coordinate is deliberately strict because recent short patterns looked formally clean while lacking the worked slices, source carry-through, lowering conditions, and transfer coverage present in mature FPF patterns. The repair is not "make everything long"; it is "carry the selected mature ingredients that the declared use needs."

### E.21:10 - SoTA-Echoing

| Claim | Source-use disposition | Concrete E.21 effect |
|---|---|---|
| Feedback connects desired state, current state, and next action. | Adopt from feedback-for-learning lineage such as Sadler and Hattie/Timperley. | `ShortRationale` and proposal rows are separated: value now, next improvement when live. |
| Questions and metrics derive from the goal. | Adopt from GQM-style measurement discipline. | Scope, reader, use, and window precede coordinate values. |
| Multi-criteria improvement needs explicit trade-offs. | Adopt from MCDA, Pareto, ATAM, and current QD/OEE lines. | Dominance comparisons and protected trade-offs replace one-score closure. |
| Proxy optimization can make intended value worse. | Adopt from Goodhart/proxy-risk lines. | `ProxyForValueSubstitutionResistance` and stop condition ask what got worse. |
| Evaluation results are not governance, safety, or compliance proof. | Adopt as non-overread boundary from current evaluation-governance practice. | Neighbour authority and status boundaries keep project claims outside `E.21`. |

### E.21:11 - Relations

| Neighbour | Relation |
|---|---|
| `A.19.ECS` | Constructs or repairs the general evaluation `CharacteristicSpace`; `E.21` is one specialization. |
| `E.8.ECSPF` | Publishes an evaluation `CharacteristicSpace` as an FPF pattern when that form is selected. |
| `E.8` | Authors the pattern body whose quality `E.21` evaluates. |
| `E.19` | Runs review profiles; findings are content evidence only when they name pattern-content defects or strengths. |
| `E.22` | Frames purpose, floor, trade-offs, and proposal expectation before an evaluation. |
| `E.23` | Runs repeated improvement using `E.21` values and stop meanings for pattern versions. |
| `E.9.DA` | Evaluates upstream `DRR` decision adequacy when pattern-quality defects trace to decisions. |
| `C.16`, `A.17`, `A.18`, `A.19` | Govern scale, coordinate, and measurement legality. |
| `F.18`, `E.10`, `A.6.P`, `C.2.P`, `C.16.P`, `C.16.Q` | Govern naming and wording-use precision when quality defects are lexical or ontological. |
| `A.10`, `B.3`, `A.20`, `A.21`, `A.15` | Govern project evidence, assurance, local CV state, gates, and work authority. |
| `J.4` and `E.11` | Govern entry and projection cues; `E.21` supplies only the scoped quality result. |

### E.21:End


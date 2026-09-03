---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:5"
section_title: "Archetypal Grounding - worked slices"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__006_archetypal-grounding-worked-slices.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:5 — Archetypal Grounding - worked slices"
line_start: 89423
line_end: 89530
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.1"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.11"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.21:5 - Archetypal Grounding - worked slices

#### E.21:5.0 - Complete compact evaluation

**Exact example edition `EX.1@source-pin-1`.** The quoted text below is the whole pattern edition being evaluated; no campaign note or unstated appendix is part of it.

> **EX.1 - Pin a reused rule to its source edition.**
>
> Use this when a team relies on a rule from a source that can change.
>
> First move: beside the decision, record the source title, exact edition or date, the exact rule used, and what that rule changes in the decision.
>
> If the edition or rule cannot be recovered, stop that reuse and retrieve it.
>
> Not this pattern when the source is background reading and no claim or decision relies on it.
>
> The pin lets a reader recover which source rule changed the decision.
>
> Example: a team records `Cooling Guide, edition 3, rule 7` beside the chosen inspection interval and notes that rule 7 sets the maximum interval; a mention of the guide in a reading list is outside this use.
>
> Reopen the decision whenever the source publishes any new edition.


The final sentence is deliberately defective: an unrelated editorial revision would trigger the same reopen as a change to rule 7. Everything below evaluates that exact text, including the defect.

**Configuration and evidence basis.**

- `PatternOfConcernRef`: the complete quoted `EX.1@source-pin-1` edition.
- `ClaimScope`: diagnostic rehearsal of E.21 on one small pattern; declared floor `3 sufficientlyExpressedForDeclaredUse` for this rehearsal only.
- `WorkingReaderScope`: a new evaluator who has E.21 and the quoted text but no campaign history.
- `IntendedUse`: learn whether this edition is coherent enough for the diagnostic rehearsal and identify the first repair; if EX.1 is later proposed for publication or ordinary authoring use, that receiving use requires its own admission decision.
- `QualificationWindow`: until the quoted edition, E.21 scale, or named comparison evidence changes.
- `EvaluationEvidenceBasis`: all seven sentences of the quoted edition; its filled `Cooling Guide` case; its background-reading non-use boundary; the absent material-change test in the last sentence; E.2.DA's pinned source-use discipline and G.11's bounded currentness contribution as mature comparators; no README, ToC, retrieval, external SoTA, observed-use, or corpus-projection evidence.
- Ordinary path only: the evaluator reads and judges the text; this diagnostic use needs no additional reliance-bearing identity or receiving decision.

```text
PrecisionRestorationProfile:
  overallEffect: clean
  checkedLoci: all seven quoted sentences, the filled case, the grounded background-reading boundary, the pin's traceability use, and the last-sentence reopen rule
  affectedCoordinates: none — the overbroad refresh rule is evaluated in the coordinate table and finding, not through a precision-restoration layer
```

| Coordinate | Value | ShortRationale |
|---|---:|---|
| `WorkingSituationAndUseBoundaryRecognizability` | `3` | The edition states the rule-reuse situation, first move, stop, and grounded background-reading boundary, so `2` understates recognition; `4` would require the missed harm and practical payoff to be early and explicit rather than inferred from the later case. |
| `EntityOfConcernAndClaimScopeStability` | `4` | Every sentence stays on a source rule reused by one decision, so `3` understates stability; `5` would overstate one small case with no second receiving use. |
| `PatternApplicationGuidance` | `4` | The reader can record four exact items and knows when to stop, so `3` understates executability; `5` would require observed first use or a second case. |
| `ClosureAndBoundedNonUseRecoverability` | `3` | Stop, return, the grounded background-reading boundary, and reopen are explicit, so `2` is too low; `4` would hide that the reopen condition is materially overbroad. |
| `SemanticKindAndNameRecoverability` | `4` | Source, edition, rule, decision, and pin remain distinct, so `3` understates the text; `5` lacks a hard ambiguity countercase. |
| `NeighborAuthorityAndBoundedUseFit` | `4` | The pin supplies a recoverable source return for the relying decision; the text asks the reader to record reliance and keeps the decision itself separate, so `3` understates the boundary; `5` would require replay across evidence, assurance, and publication uses. |
| `EntityOfConcernPrimacyAndSemioBiasResistance` | `4` | The pattern opens with the working rule-reuse problem and action, not source apparatus, so `3` is too low; `5` lacks observed cold-reader evidence. |
| `PracticalUseDeltaAndHarmPrevention` | `4` | The case shows how a decision stays traceable to rule 7 and the stop prevents unsupported reuse, so `3` understates the gain; `5` lacks an observed before-and-after project case. |
| `UseAffordabilityAndApparatusProportionality` | `4` | First use asks for four nearby facts and opens no optional apparatus, so `3` understates affordability; `5` would require observed first-use effort or repeated project use rather than this text-only rehearsal. |
| `RepairLocalityAndChangeImpactPredictability` | `4` | One last-sentence condition is the exact repair locus and its effect is predictable, so `3` understates locality; `5` lacks a replay through several dependent decisions. |
| `ProxyForValueSubstitutionResistance` | `3` | The source pin has a stated traceability use, so `2` understates proxy resistance; `4` would require a near-miss where a visible pin is wrongly treated as approval. |
| `ClaimJustificationTraceabilityCurrentnessAndReplayability` | `4` | Title, edition, rule, effect, decision, and stop are recoverable, so `3` understates replayability; `5` lacks an actual replay across two source editions. |
| `CaseCountercaseAndTransferCoverage` | `4` | The filled inspection-interval case and background-reading near-miss meet the declared small use, so `3` understates coverage; `5` would require heterogeneous transfer cases. |
| `MaturePatternParityAndSelectedContentSufficiency` | `3` | `comparator=E.2.DA and G.11; selectedIngredient=pinned source use plus bounded currentness; currentLocus=sentences 2-3 and 7; missingOrLowering=sentence 7 lacks a material-change test`; this makes `2` too low, while the missing selected ingredient prevents `4`. |
| `SoTABindingAndCurrentness` | `3` | The edition makes no positive SoTA claim and supplies no `E.8:11` comparison, so its source pin and currentness rule cannot raise this coordinate; `2` would understate the explicit source-use scope, while `4` requires one complete comparison result that this diagnostic example expressly lacks. |
| `FormalClaimAdmissibilityAndLensFit` | `4` | The edition makes no measurement, scalar, causal, or formal-model claim and assigns the pin only its traceability use, so `3` understates the fit; `5` lacks a formal near-miss. |
| `FalsifiabilityAndLoweringCondition` | `3` | Edition publication is an observable reopen trigger, so `2` is too low; `4` would overstate a trigger that does not distinguish material from irrelevant change. |
| `CorpusEntryProjectionAndEcologyFit` | `3` | The declared diagnostic use is explicitly non-corpus-facing and the whole checked text is present, so `2` is too low; `4` would require the absent entry or projection evidence for a corpus-facing claim. |
| `EvolutionFrontAndRefreshDiscipline` | `2` | The edition states a refresh trigger, so `1` understates it; any new edition triggers refresh without testing whether the used rule changed, so `3` would overstate usable evolution discipline. |

The profile, complete table, status, stop and reopen, plus the quoted pattern's grounded background-reading boundary, constitute this example's non-arithmetic `PatternQualityQBundle`; the single value of `2` is the one below-floor defect, not an arithmetic penalty or a reason to lower unrelated qualities.

```text
E.21 result:
  Pattern of concern: EX.1@source-pin-1, exactly as quoted
  Declared scope, use, reader, and window: diagnostic rehearsal; teach one new evaluator; floor 3; current until the quoted edition, E.21 scale, or evidence basis changes
  Evidence basis checked: seven quoted sentences, filled case, background-reading near-miss, absent material-change test, E.2.DA and G.11 comparators, and the explicitly absent corpus, observed-use, and external-source evidence
  Status: repairBeforeUse

First repair: narrow the final sentence to a change in the used rule, its applicability, or a stated limitation.
Receiving use: if EX.1 is proposed for admission or publication, use a separate receiving decision; this diagnostic result supplies its quality finding and repair.
Reopen if: EX.1's exact text, E.21's scale, the stated floor, or any named evidence locus changes.
BoundedNonUse: EX.1's evaluated use excludes background reading on which no claim or decision relies.
```

```text
E.21 finding:
  Pattern of concern: EX.1@source-pin-1
  Coordinate or status affected: EvolutionFrontAndRefreshDiscipline; repairBeforeUse
  Pattern locus: final sentence
  Value or status effect: EvolutionFrontAndRefreshDiscipline = 2 below the declared floor 3
  Correction direction: reopen only for a material change to the used rule, its applicability, or a stated limitation
  Closure test: an unrelated new-edition change no longer triggers work, while a changed rule 7 still reopens the relying decision
```

This is the ordinary path. The evaluator needed no dated-Work account or operation-application record to produce a complete result.

**Names named by value, no first move.** A pattern has precise Tech names and current source rows but no first user-facing action. `WorkingSituation...`, `PatternApplicationGuidance`, and `PracticalUseDelta...` fall; source currentness does not rescue ordinary use.

**Short architecture pattern.** A compact pattern has a triage form but no worked slice and no mature-pattern comparison. It can be useful as local expert reference material, but `MaturePatternParity...` and `CaseCountercase...` stay below exceptional until selected mature content is present.

**Precision-restoration profile in a non-semio pattern.** A pattern tries to introduce a non-semio `EntityOfConcern` through a catalog of other claim kinds or objects outside its own subject. That catalog is unbounded because every EoC is outside infinitely many other EoCs. If copied boundary doctrine leads the Problem frame or Solution, `EntityOfConcernPrimacyAndSemioBiasResistance` falls to `2` or `3` even when every individual boundary is true. Lead with this pattern's own subject, first useful move, practitioner action, practical delta, and positive guidance. Add one local explanation, stop, or non-use boundary only when it passes F.19:4's full independent-ground, plausible-reader, contribution, and smallest-clear-correction test. Replace other copied doctrine with the relevant pattern ID and its concrete contribution. If the doctrine is distributed across sections, repair that distribution rather than only its sentences.

**Reference apparatus before Solution content.** A pattern's first Solution paragraph assigns other patterns or related-pattern mappings before it unfolds the ontology, method, norm, worked action, or other positive solution for the pattern of concern's own `EntityOfConcern`. Even if the related pattern id is correct, `PatternApplicationGuidance`, `EntityOfConcernPrimacyAndSemioBiasResistance`, `PracticalUseDeltaAndHarmPrevention`, and sometimes `NeighborAuthorityAndBoundedUseFit` fall. Move discoverability to README, ToC, `E.11`, `I.2`, or retrieval loci; put compact pattern references and their concrete contributions in `Relations` or a late boundary row; put architecture-placement rationale in a `DRR` or architecture document; and make the Solution answer “what do I do with this pattern's EoC?” first.

**Overformalized precision.** A pattern uses correct FPF kinds, slots, references, and cross-pattern pointers so densely that the working reader cannot recover the first useful move, practical delta, or generalizing insight without doing an internal audit. Precision is then present but not usable. Lower `UseAffordabilityAndApparatusProportionality`, `WorkingSituationAndUseBoundaryRecognizability`, and sometimes `PatternApplicationGuidance`. Repair by keeping the ontology named by value only where it carries a current FPF-governed claim, moving restoration evidence to the evaluation result or DRR, and adding a short worked slice or plain recognition sentence that preserves the same kind without extra apparatus.

**QualityEvidenceLeakage in the pattern.** The pattern says that corpus projection, README, ToC, `E.11`, or `I.2` alignment, retrieval or cold-reader evidence, monolith parity, external-review readiness, landing evidence, `PatternQualityStatus`, all-`4` or all-`5` result framing, or another quality-result locus is what the user should do with the pattern's `EntityOfConcern`, or records developer, reviewer, or executor correspondence as if it were pattern content. The defect is not limited to `Problem frame`, `Solution`, examples, or checklist; notes, appendices, `Relations`, `Rationale`, `SoTA-Echoing`, tables, and conformance rows are also parts of the pattern in hosts and the monolith. That evidence may be required for `E.21`, `E.19`, landing, or retrieval loci, but it is not automatically a user action in the pattern of concern. Lower `EntityOfConcernPrimacyAndSemioBiasResistance`, `PatternApplicationGuidance`, `UseAffordabilityAndApparatusProportionality`, and `CorpusEntryProjectionAndEcologyFit` when this evidence enters the pattern. Repair by moving the evidence to the `E.21` result, `E.19` run record, README, ToC, `E.11`, `I.2`, card, retrieval, projection, or release or landing evidence locus, and keeping in the pattern only the user-facing move or boundary that follows from that evidence.


**Quality table without rationale.** A result gives values but no adjacent-value rationale. Values are unsupported. Add `ShortRationale` or lower.

**Goodharted improvement.** A rewrite improves source refs and proof sketches but becomes hard to use, or treats every non-`5` coordinate as a defect to be fixed with more apparatus. Re-evaluate affordability, repair locality, proxy-for-value, and corpus ecology before stopping. When exceptional improvement is requested, keep searching for content movement, not proof movement; the aggregate no-proposal disposition in E.21:4.7 needs loci showing that further content change is dominated, unavailable, or outside scope.


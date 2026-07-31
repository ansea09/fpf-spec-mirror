---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__005_solution.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:4 — Solution"
line_start: 72226
line_end: 72375
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "F.19"
keywords:
---

### E.9.DA:4 - Solution

`E.9.DA` is the `DRR` decision-adequacy specialization of `A.19.ECS`. It evaluates whether one `DRR` version carries enough decision content for the declared authoring use.

There is no partial `E.9.DA` result. Once invoked, the evaluator assigns a value, short rationale, and evidence locus to every coordinate in `E.9.DA:4.4`, and states the evidence basis used for the result. If the `DRR` lacks a field, source row, selected-locus map, architecture decision, comparator, or currentness basis needed by a coordinate, the relevant coordinate receives a low value and the status states the repair, split, or hold.

#### E.9.DA:4.1 - Local names and kind settlement

| Local name | Kind and function |
|---|---|
| `DRRDecisionAdequacyEvaluation` | Authored adequacy-evaluation record for one scoped `DRR` decision-adequacy claim. |
| `DRRVersionRef` | `DRR` version named by value for the evaluation. |
| `DRRDeclaredAuthoringUse` | Downstream FPF authoring use the `DRR` is expected to carry. |
| `DRRSelectedLocusDispositionMap` | Map from selected loci named by value to selected content responsibilities, explicit non-responsibilities, sibling decisions, or outside-decision dispositions. |
| `DRRDecisionAdequacyQualificationWindow` | Edition, source set, accepted-decision record, neighbour condition, and currentness window for which the evaluation holds. |
| `DRRDecisionAdequacyCoordinateSet` | The required coordinates in this pattern. |
| `DRRDecisionAdequacyEvidenceBasis` | `DRR`, source, accepted-decision, selected-locus, architecture, currentness, and neighbour loci named by value for coordinate values. |
| `DRRCoordinateValueRationales` | Required result rows: coordinate, value, short rationale, and evidence locus named by value. |
| `DRRCoordinateLocusRefs` | `DRR` loci used as value evidence. |
| `DRRSourceUseDischargeMap` | Source-use relation, source-currentness, selected payload, rejected payload, and selected locus when a source publication, source pack, or source-use record governs a decision. |
| `DRRPrecisionRestorationProfile` | Compact scalar profile for DRR wording-use precision: word-use precision, phrase apparatus, repetition-and-distribution, ontic-slot clarity, description-publication-source boundary separation, and pattern-application ontology. It records overall effect, affected coordinates, selected governing pattern, and no-repair disposition with loci when clean. |
| `DRRKindRestorationCheck` | Required pre-repair and post-repair object-kind, relation-or-claim-kind, current ontic slot, relation position, use relation, or claim kind, admissible-use, and scope check, or `not triggered`, `ordinary prose`, `already satisfied`, or `blocker` disposition with loci, for any DRR wording, naming, or precision-restoration repair proposal. |
| `DRROnticCandidateDisposition` | If the `DRR` selects, rejects, splits, or declines a candidate ontic, this names the candidate `EntityOfConcern`, sufficiency rationale, rejected alternatives, broad candidate-universe sanity sweep when the claim is broad, slot-relation boundary, description-publication boundary, and selected pattern placement by value. |
| `CampaignProblemSolutionUnfoldingCheck` | Triggered carry-through check for DRRs that create or modify README entries, path-shaped patterns, pattern families, DPF entries, first-practical routes, or constraint-governed unfolding structures. It names admitted problem-side record refs or cues, accepted starting records, current starting structures, entry cues, selected solution architecture, affected unfolding families, loci and governing-pattern map added or changed, blocked overreads, and residue that must move from DRR or README into patterns or unfolding structures. |
| `DRRDecisionAdequacyStatus` | Admissible-use status for the scoped `DRR` decision-adequacy claim. |

These names are local evaluation fields. They are not release state, review status, project evidence, gate result, assurance, or pattern-quality values.

#### E.9.DA:4.2 - Evaluation record

```text
DRRDecisionAdequacyEvaluation:
  DRRVersionRef: <DRR version named by value>

  DRRDeclaredAuthoringUse: <drafting | amendment | distribution | source-use carry-through | accepted-decision carry-through | split or hold decision>
  DRRSelectedLocusDispositionMap: <locus -> selected responsibility, explicit non-responsibility, sibling decision, or outside-decision disposition>
  DRRDecisionAdequacyQualificationWindow: <source, edition, neighbour, currentness window>
  DRRDecisionAdequacyEvidenceBasis: <checked DRR, source, accepted-decision, selected-locus, architecture, currentness, and neighbour loci; missing or unchecked loci named when they affect values>
  DRRDecisionAdequacyCoordinateTable: <all coordinates, values, short rationales, evidence loci>
  DRRPrecisionRestorationProfile: <word-use precision, phrase apparatus, repetition-and-distribution, ontic-slot clarity, description-publication-source boundary, and pattern-application profile; overall effect, affected coordinates, selected governing pattern, and no-repair or repair disposition with loci>
  DRRKindRestorationCheck: <required for each wording, naming, or precision-restoration repair proposal; pre kind, relation, claim, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope -> post kind, relation, claim, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope; not triggered | ordinary prose | already satisfied | preserved | split | intentionally changed | blocker, with loci>
  DRROnticCandidateDisposition: <if ontic or pattern-set architecture is at issue: selected, rejected, split, or declined candidate, sufficiency rationale, rejected alternatives, candidate-universe sanity sweep if broad, slot-relation boundary, description-publication boundary, and selected pattern placement>
  CampaignProblemSolutionUnfoldingCheck: <when triggered: admitted problem-side record refs or cues, accepted starting records, current starting structures, and entry cues -> selected solution architecture -> affected families and loci -> governing-pattern map -> residue that must move to patterns or unfolding structures>
  DRRDecisionAdequacyStatus: <status>
  StopOrRepairCondition: <local stop, first repair, split, or architecture hold>
```

`E.22` may frame whether the evaluation is floor-only, exceptional-improvement, trade-off, open-question, absorption, or proposal-producing. `E.23` governs repeated improvement of the `DRR` after evaluation findings exist.

#### E.9.DA:4.3 - Ordinal coordinate scale

| Value | Label | Meaning for a `DRR` decision-adequacy coordinate |
|---:|---|---|
| 0 | `absent` | The coordinate is not expressed for the declared authoring use. |
| 1 | `namedOnly` | The coordinate is named or implied, but cannot carry decision reliance. |
| 2 | `partiallyExpressedForDeclaredUse` | The coordinate is present but incomplete, fragile, or too narrow. |
| 3 | `sufficientlyExpressedForDeclaredUse` | The coordinate can carry the declared authoring use, with limits visible. |
| 4 | `wellExpressedForDeclaredUse` | The coordinate is clearly expressed with direct evidence and boundary protection. |
| 5 | `exceptionallyExpressedForDeclaredUse` | The coordinate is exceptionally expressed across reinforcing loci and cases without hiding cost or neighbour loss. |

The value is a content evaluation of the `DRR` text and accepted source-use payload, not a reward for review, landing, popularity, citation volume, or absence of visible defects.

#### E.9.DA:4.4 - Required decision-adequacy coordinates

| Coordinate | Evaluation question |
|---|---|
| `BoundedDecisionQuestionRecoverability` | Can the reader recover the FPF content decision question named by value and adjacent questions outside it? |
| `SelectedAnswerDecisiveness` | Does the `DRR` decide the selected answer now rather than leave it for drafting? |
| `SourceUseAndDecisionInheritanceCarryThrough` | Does needed source use or accepted decision inheritance change selected answers, boundaries, obligations, cases, architecture choices, stops, or reopen conditions by value? |
| `AlternativeDispositionCompleteness` | Are selected, rejected, inherited, lineage-only, rationale-only, and outside-decision options closed for the declared use? |
| `SelectedLocusObligationClosure` | Are selected content responsibilities and explicit non-responsibilities assigned to selected loci named by value without unclassified selected loci, hidden ontic-candidate decisions, or precision-restoration profile defects that would become pasteable pattern prose? |
| `FPFContentArchitectureSelectionAdequacy` | Is the selected FPF content architecture substantively adequate: existing pattern, new pattern, candidate ontic, direct-pattern repair, publication-boundary repair, split, merge, selected content object, branch, and governing pattern for each outside claim, relation, or boundary? |
| `ArchitectureSourceAndViewLossClosure` | Are affected structures, structure kinds, structural views, view losses, missing-structure return conditions, source-use relations, and splits among architecture decision, architecture description, publication, and ontic description decided when the decision uses them? |
| `DraftingActionability` | Can a pattern author recover the first substantive drafting content as this pattern's positive subject-kind and action spine, without mining copied boundary doctrine, reference boilerplate, phrase apparatus, or architecture-placement rationale for pattern prose? |
| `LexicalAndNamingClosure` | Are durable names, trigger words, and relation-like heads repaired through `E.10`, `F.18`, `A.6.P`, `C.2.P`, or the pattern that governs the relevant kind, claim, relation, or name? |
| `SoTAAndEvidenceUseInDecision` | Does each decision-governing source change a decision payload, and are non-SoTA source uses bounded? |
| `ScopeBoundaryAndNonOverread` | Are outside-decision items, inadmissible overreads, source-use or missing-structure return conditions, and lost distinctions explicit without letting precision-restoration defects or architecture-memo leakage displace the selected answer? |
| `ConsequencesAndRegressionCoverage` | Are consequences, costs, validation obligations, source-loss regressions, regression cases, and near-misses enough to protect drafting? |
| `SiblingDecisionCoordination` | Is coordination with other `DRR`s, accepted decisions, or evaluation patterns explicit without duplication or weakening? |
| `AdministrativeStateAndAuthoringHistorySeparation` | Are review logistics, packet state, landing, monolith placement, chat history, and authoring history kept out of decision evidence? |
| `CorpusEcologyAndShadowSpecResistance` | Does the `DRR` assign repeated doctrine to governing patterns and avoid duplicate local variants or shadow specs? |

Coordinate separation is by repair question. One `DRR` section may support several coordinates, but the rationale must state the distinct property supported for each. When two heads always fail and repair together, the `DRR` or the evaluation pattern needs characteristic-space repair through `A.19.ECS`.

#### E.9.DA:4.4a - Result-row discipline and calibration

An `E.9.DA` result uses this table shape:

| Coordinate | Value | ShortRationale | EvidenceLocus |
|---|---:|---|---|
| `<E.9.DA coordinate>` | `<0..5>` | `<assigned-value basis; why the lower adjacent value would understate the DRR evidence; why the higher adjacent value would overstate it, or for 5 what would lower or reopen>` | `<DRR section, row, alternative, source-use row, selected-locus row, accepted-decision row, architecture decision, or missing locus named by value>` |

A prose summary, heading checklist, two-column coordinate-and-value table, or table without an `EvidenceLocus` named by value is not an `E.9.DA` result. It is draft evaluation material. Missing or unchecked evidence lowers the coordinate that needs it; it does not make the coordinate inactive.

Common calibration points:

| Coordinate family | `3` | `4` | `5` |
|---|---|---|---|
| Decision question and selected answer | The decision can guide limited drafting, but unsettled or ambiguous material remains visible. | The selected answer and outside questions are directly recoverable for declared authoring use. | The decision is reinforced across question, alternatives, consequences, selected loci, and first drafting action without hidden unsettled branches. |
| Source-use and inheritance | Sources or inherited decisions are relevant, but payload mutation or rejection is compact or incomplete. | Source-use relation, adopted payload, rejected payload, currentness, and selected-locus obligation are explicit. | Source distinctions are replayable across selected answer, cases, boundaries, and first drafting action. |
| Selected-locus and architecture closure | Loci are named, but some obligation, non-obligation, split, architecture choice, ordinary reference relation, or phrase apparatus remains generic. | Loci named by value and content obligations are closed for declared use without precision-restoration defects or architecture-memo prose in the future pattern body. | The split, merge, governing pattern for outside claim, relation, or boundary, and lost-structure or source-use distinctions are replayable across cases and consequences while product prose remains positive-subject first. |
| Drafting actionability | A skilled author can proceed, but must infer some first move, subject spine, boundary disposition, selected-locus relation, or reference or architecture disposition from scattered material. | The first substantive drafting content is the positive subject-kind and action spine; copied distinctions owned by other patterns are classified as pointers named by value or non-carried fanout; ordinary references stay as references; architecture rationale and phrase apparatus stay out of pattern prose; and pattern application remains explicit. | Drafting can proceed across heterogeneous selected loci without inventing decisions, final prose, local negative catalogs, reference boilerplate, phrase apparatus, or architecture-memo leakage. |

#### E.9.DA:4.5 - Status and stop condition

| Status | Meaning |
|---|---|
| `admissibleForDeclaredAuthoringUse` | The `DRR` can be used for the declared drafting, amendment, distribution, source-use, or accepted-decision carry-through. |
| `newFrameRequired` | The DRR appears useful only for a different decision, authoring use, selected-locus set, source-use claim, or qualification window than the declared one. This is not an admissible result for the current request; open a new `E.22` frame or repair the DRR. |
| `repairBeforeDrafting` | One or more coordinate floors fail for the declared authoring use. |
| `splitDecisionRequired` | Several coupled questions need separate decision records or explicit convergence. |
| `holdForArchitectureDecision` | Content object, branch, neighbour boundary, selected locus, structural view relation, missing-structure return condition, source-use relation, or publication split must be decided before adequacy can close. |

`admissibleForDeclaredAuthoringUse` states the first drafting action and the most expansive non-admissible overread. `newFrameRequired` is not a pass for the current declared use. Non-ready statuses state the first repair, split boundary, or architecture question.

#### E.9.DA:4.6 - Compact result form

```text
E.9.DA result:
  DRR version: <DRRVersionRef>
  Declared authoring use: <DRRDeclaredAuthoringUse>
  Qualification window: <window>
  Evidence basis checked: <DRRDecisionAdequacyEvidenceBasis>
  Precision-restoration profile: <DRRPrecisionRestorationProfile>
  Status: <DRRDecisionAdequacyStatus>
  Coordinate table: <Coordinate | Value | ShortRationale | EvidenceLocus for every required coordinate>
  First drafting action or first repair: <...>
  Most expansive non-admissible overread: <...>
  Reopen if: <smallest changed locus or condition>
```

The coordinate table may be short. It is still complete. Status is not assigned from a prose summary, two-column table, applied-finding count, review acceptance, or result missing evidence loci needed by its values.

#### E.9.DA:4.7 - Finding row

```text
E.9.DA finding:
  DRR version: <DRRVersionRef>
  Declared authoring use: <DRRDeclaredAuthoringUse>
  Coordinate or status affected: <coordinate | status | stop condition>
  DRR locus: <section, row, alternative, source-use row, accepted-decision row>
  Value or status effect: <value, status, floor, or stop impact>
  Correction direction: <selected answer | selected locus | source-use payload | architecture choice | example | boundary | stop or reopen>
  Closure test: <what changed DRR text would show>
```

Vague labels such as `weak DRR`, `needs more evidence`, or `architecture unclear` are not findings until rewritten into this row.

When `E.22`, `E.23`, absorption, or exceptional-improvement framing asks for improvement, below-floor coordinates return findings or repair. Above-floor coordinates receive proposal rows only for substantive non-dominated decision-content opportunities inside the declared authoring use: a more decisive selected answer, source payload mutation, selected-locus obligation, architecture split or merge decision, rejected-alternative closure, first drafting action, regression case, or deletion or relocation of apparatus that would otherwise become pattern prose. Do not treat every value below `5` as a defect. A `4` may be the correct stop value only with loci showing why further decision-content movement is dominated, unavailable, or outside scope.


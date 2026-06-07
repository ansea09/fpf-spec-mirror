---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__005_solution.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:4 — Solution"
line_start: 57622
line_end: 57761
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

| Local name | Kind and role |
|---|---|
| `DRRDecisionAdequacyEvaluation` | Authored adequacy-evaluation record for one scoped `DRR` decision-adequacy claim. |
| `DRRVersionRef` | Exact `DRR` version being evaluated. |
| `DRRDeclaredAuthoringUse` | Downstream FPF authoring use the `DRR` is expected to carry. |
| `DRRSelectedLocusDispositionMap` | Map from exact selected loci to content obligations, non-obligations, sibling decisions, or outside-decision dispositions. |
| `DRRDecisionAdequacyQualificationWindow` | Edition, source set, accepted-decision record, neighbour condition, and currentness window for which the evaluation holds. |
| `DRRDecisionAdequacyCoordinateSet` | The required coordinates in this pattern. |
| `DRRDecisionAdequacyEvidenceBasis` | Exact checked `DRR`, source, accepted-decision, selected-locus, architecture, currentness, and neighbour loci used for coordinate values. |
| `DRRCoordinateValueRationales` | Required result rows: coordinate, value, short rationale, and exact evidence locus. |
| `DRRCoordinateLocusRefs` | Exact `DRR` loci used as value evidence. |
| `DRRSourceUseDischargeMap` | Source-use role, source-currentness, selected payload, rejected payload, and selected locus when source material is load-bearing. |
| `DRRKindRestorationCheck` | Required pre-repair/post-repair object-kind, relation-or-claim-kind, slot-or-use-position, admissible-use, and scope check, or `not triggered`/`ordinary prose`/`already satisfied`/`blocker` disposition with loci, for any DRR wording, naming, or precision-restoration repair proposal. |
| `DRRDecisionAdequacyStatus` | Admissible-use status for the scoped `DRR` decision-adequacy claim. |

These names are local evaluation fields. They are not release state, review status, project evidence, gate result, assurance, or pattern-quality values.

#### E.9.DA:4.2 - Evaluation record

```text
DRRDecisionAdequacyEvaluation:
  DRRVersionRef: <exact DRR version>
  DRRDeclaredAuthoringUse: <drafting | amendment | distribution | source-use carry-through | accepted-decision carry-through | split/hold decision>
  DRRSelectedLocusDispositionMap: <locus -> obligation/non-obligation/sibling/outside>
  DRRDecisionAdequacyQualificationWindow: <source, edition, neighbour, currentness window>
  DRRDecisionAdequacyEvidenceBasis: <checked DRR, source, accepted-decision, selected-locus, architecture, currentness, and neighbour loci; missing or unchecked loci named when they affect values>
  DRRDecisionAdequacyCoordinateTable: <all coordinates, values, short rationales, evidence loci>
  DRRKindRestorationCheck: <required for each wording/naming/precision-restoration repair proposal; pre kind/relation/claim/slot-or-use-position/admissible use/scope -> post kind/relation/claim/slot-or-use-position/admissible use/scope; not triggered | ordinary prose | already satisfied | preserved | split | intentionally changed | blocker, with loci>
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
| `BoundedDecisionQuestionRecoverability` | Can the reader recover the exact FPF content decision question and adjacent questions outside it? |
| `SelectedAnswerDecisiveness` | Does the `DRR` decide the selected answer now rather than defer it to drafting? |
| `SourceUseAndDecisionInheritanceCarryThrough` | Does needed source use or accepted decision inheritance change selected answers, boundaries, obligations, cases, architecture choices, stops, or reopen conditions by value? |
| `AlternativeDispositionCompleteness` | Are selected, rejected, inherited, lineage-only, rationale-only, and outside-decision options closed for the declared use? |
| `SelectedLocusObligationClosure` | Are obligations and non-obligations assigned to exact selected loci without unclassified selected loci or precision-restoration/profile defects that would become pasteable pattern prose? |
| `FPFContentArchitectureSelectionAdequacy` | Is the selected FPF content architecture substantively adequate: existing pattern, new pattern, split, merge, selected content object, branch, and exact pattern for each outside claim, relation, or boundary? |
| `ArchitectureSourceAndViewLossClosure` | Are affected structures, structure kinds, structural views, view losses, source-return conditions, and splits among architecture decision, architecture description, and publication decided when the decision uses them? |
| `DraftingActionability` | Can a pattern author recover the first substantive drafting content as this pattern's positive subject-kind/action spine, without mining copied boundary doctrine, reference boilerplate, phrase apparatus, or architecture-placement rationale for pattern prose? |
| `LexicalAndNamingClosure` | Are durable names, trigger words, and relation-like heads repaired through `E.10`, `F.18`, `A.6.P`, `C.2.P`, or the exact pattern that governs the relevant kind, claim, relation, or name? |
| `SoTAAndEvidenceUseInDecision` | Does each load-bearing source change a decision payload, and are non-SoTA source uses bounded? |
| `ScopeBoundaryAndNonOverread` | Are outside-decision items, inadmissible overreads, source-return paths, and lost distinctions explicit without letting precision-restoration defects or architecture-memo leakage displace the selected answer? |
| `ConsequencesAndRegressionCoverage` | Are consequences, costs, validation obligations, source-loss regressions, regression cases, and near-misses enough to protect drafting? |
| `SiblingDecisionCoordination` | Is coordination with other `DRR`s, accepted decisions, or evaluation patterns explicit without duplication or weakening? |
| `AdministrativeStateAndAuthoringHistorySeparation` | Are review logistics, packet state, landing, monolith placement, chat history, and authoring history kept out of decision evidence? |
| `CorpusEcologyAndShadowSpecResistance` | Does the `DRR` assign repeated doctrine to governing patterns and avoid duplicate local variants or shadow specs? |

Coordinate separation is by repair question. One `DRR` section may support several coordinates, but the rationale must state the distinct property supported for each. When two heads always fail and repair together, the `DRR` or the evaluation pattern needs characteristic-space repair through `A.19.ECS`.

#### E.9.DA:4.4a - Result-row discipline and calibration

An `E.9.DA` result uses this table shape:

| Coordinate | Value | ShortRationale | EvidenceLocus |
|---|---:|---|---|
| `<E.9.DA coordinate>` | `<0..5>` | `<assigned-value basis; why the lower adjacent value would understate the DRR evidence; why the higher adjacent value would overstate it, or for 5 what would lower/reopen>` | `<DRR section, row, alternative, source-use row, selected-locus row, accepted-decision row, architecture decision, or exact missing locus>` |

A prose summary, heading checklist, two-column coordinate/value table, or table without exact `EvidenceLocus` is not an `E.9.DA` result. It is draft evaluation material. Missing or unchecked evidence lowers the coordinate that needs it; it does not make the coordinate inactive.

Common calibration points:

| Coordinate family | `3` | `4` | `5` |
|---|---|---|---|
| Decision question and selected answer | The decision can guide limited drafting, but deferred or ambiguous material remains visible. | The selected answer and outside questions are directly recoverable for declared authoring use. | The decision is reinforced across question, alternatives, consequences, selected loci, and first drafting move without hidden deferral. |
| Source-use and inheritance | Sources or inherited decisions are relevant, but payload mutation or rejection is compact or incomplete. | Source-use role, adopted payload, rejected payload, currentness, and selected-locus obligation are explicit. | Source distinctions are replayable across selected answer, cases, boundaries, and first drafting move. |
| Selected-locus and architecture closure | Loci are named, but some obligation, non-obligation, split, architecture choice, ordinary reference relation, or phrase apparatus remains generic. | Exact loci and content obligations are closed for declared use without precision-restoration defects or architecture-memo prose in the future pattern body. | The split, merge, exact pattern for outside claim/relation/boundary, and lost/source-return distinctions are replayable across cases and consequences while product prose remains positive-subject first. |
| Drafting actionability | A skilled author can proceed, but must infer some first move, subject spine, boundary disposition, selected-locus relation, or reference/architecture disposition from scattered material. | The first substantive drafting content is the positive subject-kind/action spine; copied distinctions owned by other patterns are classified as exact pointers or non-carried fanout; ordinary references stay as references; architecture rationale and phrase apparatus stay out of pattern prose; and pattern application remains explicit. | Drafting can proceed across heterogeneous selected loci without inventing decisions, final prose, local negative catalogs, reference boilerplate, phrase apparatus, or architecture-memo leakage. |

#### E.9.DA:4.5 - Status and stop condition

| Status | Meaning |
|---|---|
| `admissibleForDeclaredAuthoringUse` | The `DRR` can be used for the declared drafting, amendment, distribution, source-use, or accepted-decision carry-through. |
| `newFrameRequired` | The DRR appears useful only for a different decision, authoring use, selected-locus set, source-use claim, or qualification window than the declared one. This is not an admissible result for the current request; open a new `E.22` frame or repair the DRR. |
| `repairBeforeDrafting` | One or more coordinate floors fail for the declared authoring use. |
| `splitDecisionRequired` | Several coupled questions need separate decision records or explicit convergence. |
| `holdForArchitectureDecision` | Content object, branch, neighbour boundary, selected locus, structural view relation, source-return condition, or publication split must be decided before adequacy can close. |

`admissibleForDeclaredAuthoringUse` states the first drafting move and the most expansive non-admissible overread. `newFrameRequired` is not a pass for the current declared use. Non-ready statuses state the first repair, split boundary, or architecture question.

#### E.9.DA:4.6 - Compact result form

```text
E.9.DA result:
  DRR version: <DRRVersionRef>
  Declared authoring use: <DRRDeclaredAuthoringUse>
  Qualification window: <window>
  Evidence basis checked: <DRRDecisionAdequacyEvidenceBasis>
  Status: <DRRDecisionAdequacyStatus>
  Coordinate table: <Coordinate | Value | ShortRationale | EvidenceLocus for every required coordinate>
  First drafting move or first repair: <...>
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
  Exact DRR locus: <section, row, alternative, source-use row, accepted-decision row>
  Value or status effect: <value/status/floor/stop impact>
  Correction direction: <selected answer | selected locus | source-use payload | architecture choice | example | boundary | stop/reopen>
  Closure test: <what changed DRR text would show>
```

Vague labels such as `weak DRR`, `needs more evidence`, or `architecture unclear` are not findings until rewritten into this row.


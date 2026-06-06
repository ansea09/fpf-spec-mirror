---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: "E.22:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__005_solution.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
  - "E.22:4 — Solution"
line_start: 67624
line_end: 67713
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.25"
  - "E.10"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.22:4 - Solution

`E.22` gives one compact declaration for improvement-oriented quality evaluation questions. It keeps the question from replacing the evaluation and keeps the evaluation result from becoming a decision or work product beyond its authority.

#### E.22:4.1 - Local names and kind settlement

| Local name | Kind and role |
|---|---|
| `QualityEvaluationQuestionFrame` | Compact declaration of the requested quality evaluation before it runs. |
| `ObjectVersionUnderQualityEvaluation` | Exact object version being evaluated. |
| `ObjectUnderImprovementEvaluationRef` | Exact evaluation pattern, characteristic space, scale set, rubric, review profile, or quality bundle that supplies values. |
| `QualityEvaluationPurposeSelection` | Requested evaluation purpose or combined purposes. |
| `DeclaredQualityFloor` | Minimum acceptable coordinate or status floor when a floor claim is live. |
| `DesiredImprovementAim` | Requested movement beyond the floor when live. |
| `TradeoffProtectionSet` | Qualities that must not silently worsen while visible values improve. |
| `ExpectedEvaluationEvidenceBasis` | Evidence loci the named evaluation must check or name for the requested purpose: object version, corpus/projection loci, source-currentness loci, comparator loci, worked cases, returned findings, or exact missing loci. |
| `ExpectedQualityEvaluationResultForm` | The result-row shape required by the named evaluation, including coordinate/value/short-rationale rows and any evidence-locus or coordinate-specific payload fields. |
| `QualityReviewFindingRow` | Actionable row for a returned finding, expected movement, correction direction, and closure test. |
| `CandidateImprovementProposalPortfolio` | Bounded set of proposal rows returned by the evaluation when alternatives are useful. |
| `NextAdmissibleMoveHypothesis` | Stop, repair, proposal, trade-off warning, outside-evaluation assignment, new-frame assignment, or exact-neighbour assignment suggested by the evaluation. |

These names frame and report quality evaluation. They do not select candidates, publish sets, plan work, certify evidence, approve release, or create new values.

#### E.22:4.2 - Quality evaluation purposes

| Purpose value | Use when | Expected result |
|---|---|---|
| `floorEvaluation` | The question is whether the object reaches a declared floor. | Values below floor, first repair, architecture hold, refresh, new-frame assignment, or admissible stop. |
| `exceptionalImprovementEvaluation` | The floor is reached and the requester wants non-dominated improvement toward exceptional expression. | Per-coordinate proposal or no-candidate disposition. |
| `paretoTradeoffEvaluation` | A candidate change may improve some values while worsening protected qualities. | Trade-off account and non-dominated comparison. |
| `candidateImprovementProposalEvaluation` | The requester needs candidate-change proposals before changing the object or generating variants. | Proposal row or bounded proposal portfolio with expected evaluation movement. |
| `openQuestionDiscoveryEvaluation` | The requester wants important unasked questions surfaced. | Question classified as existing-coordinate issue, candidate future coordinate, or outside-evaluation issue. |
| `absorptionEvaluation` | Returned findings or suggestions have been applied or rejected. | Quality-impact account over the changed object. |

Purposes can be combined, but the result keeps them distinguishable. A floor result does not answer exceptional improvement. Absorption count is not quality movement. A proposal is not a selected work item.

#### E.22:4.3 - Question frame

```text
QualityEvaluationQuestionFrame:
  Object version under quality evaluation: <exact object version>
  Object-under-improvement evaluation: <exact evaluation>
  Evaluation purpose selection: <floor | exceptional | tradeoff | proposal | open-question | absorption | combined>
  Declared quality floor: <floor and scope, or evaluation default>
  Desired improvement aim: <floor-only | raise toward exceptional | compare variants | propose candidate changes | discover questions | absorption impact>
  Protected trade-offs: <usability | affordability | locality | corpus ecology | neighbour fit | source preservation | other exact property>
  Expected evidence basis: <object, corpus, source, comparator, worked-case, returned-finding, projection, or exact missing loci required by the named evaluation and purpose>
  Expected result form: <named evaluation's result-row shape | finding rows | proposal rows | trade-off table | open-question list | absorption-impact account | next-move hypotheses>
  Non-use boundary: <what this result must not decide, certify, publish, plan, execute, or prove>
```

The shortest floor frame may name only object version, object-under-improvement evaluation, purpose `floorEvaluation`, and declared floor. The named evaluation still runs its required coordinate set and returns the result-row shape, evidence basis, rationales, and coordinate-specific payloads required by that evaluation.

The frame does not authorize post-hoc scope replacement. If the requested floor is landing-input, corpus-facing, `Stable`, release, external-review, or another stated use, the evaluator measures that use. If a different use becomes interesting, open a new `QualityEvaluationQuestionFrame`; do not report the current request as passed under an easier scope.

#### E.22:4.4 - Finding and proposal rows

An actionable finding has this shape:

```text
QualityReviewFindingRow:
  Review locus: <where the issue was found>
  Object locus: <where the object would change>
  Evaluation effect: <coordinate/status/floor/protected quality/outside evaluation>
  Current value or status: <if known>
  Expected movement: <repair floor | raise toward exceptional | prevent loss | classify outside>
  Correction direction: <what should change>
  Closure test: <what evidence would close the row>
```

A proposal row uses the same shape plus expected trade-offs and neighbour exit. One edit may close several rows, but each row keeps its own disposition and closure evidence.

#### E.22:4.5 - Absorption impact values

| Absorption impact | Meaning |
|---|---|
| `coordinateImproved` | A named coordinate or status has stronger content evidence after the change. |
| `floorOnlyClosure` | A below-floor defect was repaired enough for the floor but not exceptional expression. |
| `unchangedBecauseAlreadySatisfied` | The suggestion was already satisfied by value. |
| `tradeoffIntroduced` | A repair raised one property and damaged another. |
| `qualityLossDetected` | The applied or proposed change lowers a value or protected quality. |
| `outsideObjectUnderImprovementEvaluation` | The suggestion belongs under another exact evaluation or pattern. |
| `notAdmissibleForDeclaredUse` | The suggestion is rejected for the declared purpose and boundary. |

The absorption result is quality movement under the object-under-improvement evaluation, not a count of accepted rows.

#### E.22:4.6 - OEE/NQD and proposal portfolios

When the object is a candidate, archive/front member, selected set, parity report, refresh report, or declared transduction result, `E.22` can frame the quality question and return proposal rows. `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` keep authority over candidate characteristics, archive/front semantics, pool policy, selected-set publication, parity, and refresh.


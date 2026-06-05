---
chunk_kind: "parent"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality Evaluation Question Framing"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/E.22.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.22 — Improvement-Oriented Quality Evaluation Question Framing"
line_start: 67591
line_end: 67792
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

## E.22 - Improvement-Oriented Quality Evaluation Question Framing

Status: Core.

### E.22:1 - Problem frame

Use `E.22` when someone is about to ask for a quality evaluation, quality review, returned-finding absorption, improvement proposal, or next-move hypothesis over an exact object version, and the question needs to say what kind of evaluation is wanted before the evaluator starts.

`E.22` frames the question. It does not evaluate the object. The values, coordinates, statuses, and stop meanings come from the named object-under-improvement evaluation: for example `E.21` for one pattern version, `E.9.DA` for one `DRR`, `E.2.DA` for an FPF-level object, `E.19` for an admission or refresh review profile, `C.25` for an engineering quality bundle, or another declared characteristic space, scale set, rubric, or review profile.

Not this pattern when the question is already scoped and one direct evaluation is enough. Run the object-under-improvement evaluation directly. Use `E.23` when repeated improvement across passes is live.

First useful move: write a `QualityEvaluationQuestionFrame` naming the object version, the object-under-improvement evaluation, the purpose, the floor or improvement aim, protected trade-offs, expected evidence basis, and expected result form.

What goes wrong if missed: "review this" can mean too many different things. A floor check may be mistaken for exceptional improvement, a review may suggest work without naming quality movement, absorption may count closed rows without re-evaluating the changed object, or a next-move suggestion may be overread as a decision, work plan, gate, evidence, assurance, or release.

Primary EntityOfConcern in plain terms: the framed quality-evaluation question for one object version.

### E.22:2 - Problem

Quality evaluations fail when the evaluator has to infer the question. The same object can be checked for floor adequacy, improved toward exceptional expression, compared across trade-offs, mined for open questions, or evaluated after finding absorption. Those purposes produce different findings.

The defect is not that reviewers need more ceremony. The defect is that an unframed question hides the object under improvement, the evaluation that supplies values, and the allowed shape of returned work.

### E.22:3 - Forces

| Force | Tension |
|---|---|
| Cheap readiness vs ambitious improvement | A floor evaluation should be short; exceptional improvement needs richer proposals. |
| Explicit purpose vs reviewer discovery | The request names the purpose, while the reviewer can still report important unasked questions. |
| Evaluation vs next move | A useful evaluation may suggest a next move, but the suggestion remains a hypothesis until another exact pattern receives it. |
| Multi-coordinate gain vs Goodhart risk | Raising one visible value can damage usability, affordability, locality, source preservation, or corpus ecology. |
| Proposal portfolio vs selected result | Several candidate improvements may be useful without becoming a selected set, pool policy, front insertion, parity, or refresh result. |

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
| `NextAdmissibleMoveHypothesis` | Stop, repair, narrow, proposal, trade-off warning, outside-evaluation assignment, or exact-neighbour assignment suggested by the evaluation. |

These names frame and report quality evaluation. They do not select candidates, publish sets, plan work, certify evidence, approve release, or create new values.

#### E.22:4.2 - Quality evaluation purposes

| Purpose value | Use when | Expected result |
|---|---|---|
| `floorEvaluation` | The question is whether the object reaches a declared floor. | Values below floor, first repair, narrowed use, or admissible stop. |
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

### E.22:5 - Worked slices

**Floor evaluation.** A reviewer is asked whether one pattern is ready for ordinary use. The frame names `E.21`, purpose `floorEvaluation`, the declared floor, and the expected `E.21` result form. The result is a complete `E.21` coordinate table with `ShortRationale` and `EvaluationEvidenceBasis`, not a narrative "looks fine."

**Exceptional improvement.** A pattern already passes the floor. The frame asks for non-dominated improvements toward `5` while protecting usability and neighbour fit. The result returns proposal rows for missing worked cases and source-currentness, plus no-candidate dispositions for coordinates already strongly expressed.

**Absorption.** External review returns many suggestions. The frame asks for `absorptionEvaluation`. The result says which changes improved coordinates, which were already satisfied, which introduced trade-offs, and which belong outside the evaluation.

**Proposal portfolio.** A candidate improvement campaign needs alternatives before editing. The frame asks for `candidateImprovementProposalEvaluation`. The result returns bounded proposal rows; selection or generation stays with exact neighbours.

### E.22:6 - Bias annotation

This pattern biases FPF toward asking the quality question by value. The bias is useful because unframed review requests often produce plausible but wrong answers.

The bias is bounded. `E.22` does not supply quality values, run repeated improvement, publish selected sets, decide work, or certify project claims.

### E.22:7 - Conformance checklist

| Check | Requirement |
|---|---|
| `CC-E22-1` | Name the exact object version and object-under-improvement evaluation. |
| `CC-E22-2` | State purpose, declared floor or improvement aim, protected trade-offs, and expected result form. |
| `CC-E22-3` | Keep the object-under-improvement evaluation as the source of values and required coordinates. |
| `CC-E22-4` | Represent actionable returned work as row-level findings or proposal rows with expected quality movement and closure tests. |
| `CC-E22-5` | For absorption, report quality impact on the changed object, not only applied/not-applied disposition. |
| `CC-E22-6` | State non-use boundary when the result might be overread as decision, work, evidence, assurance, gate, release, certification, publication, parity, refresh, or selected-set authority. |
| `CC-E22-7` | State what became worse when a proposed or applied improvement raises visible values. |
| `CC-E22-8` | Send repeated improvement to `E.23` after one framed evaluation returns findings or proposals. |
| `CC-E22-9` | Name the expected evidence basis and result-row shape from the object-under-improvement evaluation; `E.22` cannot authorize omitted coordinates, missing rationales, unchecked loci, or a weaker result form. |

### E.22:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **"Review this" prompt.** The evaluator infers purpose. | Add a `QualityEvaluationQuestionFrame`. |
| **Floor pass sold as excellence.** Readiness is mistaken for exceptional improvement. | State `exceptionalImprovementEvaluation` if wanted. |
| **Frame replaces result.** The question frame names a purpose but returns prose, a two-column value table, or proposal rows without the named evaluation's result form. | Re-run the named evaluation and return its required coordinates, evidence basis, rationales, and payload fields. |
| **Applied-count absorption.** Closure count replaces quality movement. | Re-evaluate the changed object and classify impact. |
| **Goodharted improvement.** Visible values rise while protected qualities worsen. | Add trade-off protection and reject dominated changes. |
| **Recommendation as decision.** A next-move hypothesis is treated as chosen work. | Open the exact decision, work, publication, parity, refresh, evidence, or assurance pattern if that claim is needed. |

### E.22:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Review requests become typed. | Evaluators answer the intended quality question. | Requesters must name the object and evaluation. |
| Exceptional improvement becomes explicit. | Reviews can propose non-dominated improvements rather than stopping at floor defects. | Protected trade-offs must be named. |
| Absorption becomes quality-aware. | Follow-up says what improved or worsened. | Row discharge alone is not enough. |

### E.22:10 - Rationale

There is no neutral generic request when a quality result is wanted. The useful artifact is the framed question: object version, evaluation, purpose, expected evidence basis, expected result form, and boundary. This keeps review helpful without turning it into process control or project authority.

### E.22:11 - SoTA-Echoing

| Claim | Current or retained source line | Local adoption |
|---|---|---|
| Quality evaluation should be multidimensional, diagnostic, and actionable. | Current rubric and long-form evaluation work, including multidimensional LLM rubric evaluation and meta-evaluation lines, treats rubric validity and actionable feedback as live problems. | Findings name evaluation effects, expected movement, correction direction, and closure tests. |
| Feedback needs desired condition, current condition, and next action. | Hattie/Timperley and Sadler lineage, retained through current feedback-evaluation work. | The frame states floor or desired aim, current evaluation object, and expected result form. |
| Evaluation questions must derive from purpose. | GQM lineage and current task-specific rubric evaluation work. | `QualityEvaluationPurposeSelection` precedes values. |
| Multi-criteria improvement needs trade-offs and non-dominated alternatives. | MCDA, Pareto, ATAM lineage plus current architecture trade-off evaluation work. | `paretoTradeoffEvaluation` and `TradeoffProtectionSet` prevent one-score closure. |
| Proxy optimization can degrade intended value. | Goodhart taxonomy and current proxy/reward/rubric failure work. | Findings ask what became worse and keep popularity, review count, and discharge count out of values. |
| OEE/NQD needs proposal-shaped quality pressure before candidate change. | Current quality-diversity and open-ended exploration lines. | Proposal rows name expected quality movement before generation or selection neighbours consume them. |

### E.22:12 - Relations

| Pattern | Relation |
|---|---|
| `E.21` | Supplies pattern-quality values and required coordinates. |
| `E.9.DA` | Supplies `DRR` decision-adequacy values and required coordinates. |
| `E.2.DA` | Supplies FPF Pillar-adequacy values. |
| `E.19` | Supplies admission or refresh review profiles when that is the evaluation. |
| `E.23` | Governs repeated improvement after framed evaluations return findings or proposal rows. |
| `E.10`, `A.6.P`, `C.2.P`, `F.18` | Repair load-bearing wording and names introduced by frames or findings. |
| `C.16`, `A.17`, `A.18`, `A.19`, `C.25` | Govern characteristics, scales, measurements, characteristic spaces, and quality bundles. |
| `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, `G.11` | Govern OEE/NQD candidate, archive/front, pool, selected-set, parity, and refresh claims. |
| `C.11`, `C.24`, `A.15`, `A.20`, `A.21`, `A.10`, `B.3` | Receive decision, call-planning, work, gate, release, evidence, and assurance claims when a quality result is reused beyond evaluation. |

### E.22:End


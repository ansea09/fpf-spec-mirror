---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality-Read Question Framing"
section_id: "E.22:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__005_solution.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "E.22 — Improvement-Oriented Quality-Read Question Framing"
  - "E.22:4 — Solution"
line_start: 67382
line_end: 67646
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

State a `QualityReadQuestionFrame` before running a substantive improvement-oriented quality read.

`QualityReadQuestionFrame := <ObjectVersionUnderQualityRead, ObjectUnderImprovementEvaluationRef, QualityReadPurposeSelection, DeclaredQualityFloor?, DesiredImprovementAim?, TradeoffProtectionSet?, OpenQuestionClassificationRule?, AbsorptionImpactClassificationRule?, CandidateImprovementProposalRule?, NextAdmissibleMoveHypothesisRule?, ExpectedResultForm, NonUseBoundary>`

`QualityReadQuestionFrame` is a local question-framing record. It is not a review result, gate, assurance record, evidence record, release condition, work item, score sheet, discharge-count result, checklist-count result, candidate-pool policy, selector publication, refresh plan, unguided candidate-change policy, or second quality characteristic space.

#### E.22:4.1 - Local names and kind settlement

| Local name | Role | Non-use boundary |
|---|---|---|
| `QualityReadQuestionFrame` | Compact declaration of the requested quality read before the read runs. | Not the quality read itself, not a review packet, not a gate, not an ordered execution plan. |
| `ObjectVersionUnderQualityRead` | Exact object version whose quality is being read. | Not a vague object label, source bundle, campaign, chat thread, or unnamed candidate pool. For OEE/NQD material, name the candidate, front, archive, shortlist, parity report, refresh report, or declared transduction result and the governing pattern that gives it that object kind. |
| `ObjectUnderImprovementEvaluationRef` | The exact evaluation that supplies the read values: for example `E.21`, `E.9.DA`, `E.19`, `C.25`, `C.16`, `A.19`, `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, `G.11`, a declared characteristic space, scale set, rubric, review profile, or another local quality pattern. | Does not let `E.22` borrow that evaluation's values or invent coordinates when no object-under-improvement evaluation is declared. |
| `QualityReadPurposeSelection` | Declared subset of read purposes requested now. | Not an ordered execution sequence and not a maturity ladder. |
| `DeclaredQualityFloor` | Minimum acceptable coordinate or status floor for this request, when a floor claim is live. | Not a release gate or proof of quality by itself. |
| `DesiredImprovementAim` | The requested improvement aim beyond the floor, if any. | Not permission to optimize visible values while damaging protected qualities. |
| `TradeoffProtectionSet` | Quality properties that must not be silently degraded while other coordinates improve. | Not a hidden score and not a substitute for the object-under-improvement evaluation's coordinates or values. |
| `OpenQuestionClassificationRule` | How unasked but important questions are classified. | Not an invitation to open unrelated FPF work. |
| `AbsorptionImpactClassificationRule` | How returned-finding absorption classifies coordinate movement and trade-offs. | Not a count of accepted suggestions and not a reviewer-answer log. |
| `CandidateImprovementProposalRule` | Allowed shape for one proposal or a bounded proposal portfolio returned by the read: expected object-under-improvement evaluation movement, affected locus, protected trade-offs, closure test, and neighbour exit. | Not a candidate generator, mutation policy, candidate-pool policy, front or archive insertion rule, selected-set publication, work plan, or proof that any proposed change should be applied. |
| `NextAdmissibleMoveHypothesisRule` | Allowed shapes for next-move hypotheses returned by the read: stop, repair, narrow, candidate improvement proposal, trade-off warning, outside-evaluation assignment, or assignment to an exact neighbouring pattern. | Not a decision result, `CallPlan`, work plan, execution order, gate, release, evidence, assurance, selector publication, pool policy, parity report, or refresh plan. |
| `CandidateImprovementProposalPortfolio` | Bounded set of proposal rows returned by the read when the requester needs alternatives for generation, comparison, selection, or later loop work. | Not a candidate pool, archive, front, shortlist, selected-set publication, parity result, refresh plan, or decision that any proposal wins. |
| `QualityReviewFindingRow` | Stable actionable row for one returned finding that requires repair, narrowing, or explicit non-use. | Not a narrative review paragraph, not a grouped range, and not quality closure by itself. |

These local names remain local to `E.22` unless a separate FPF naming decision promotes one through `F.18`. The word `frame` here means a declared question boundary; it is not a publication face, UI frame, architecture frame, review phase, or generic container.

#### E.22:4.1a - Placement and specialization boundary

`E.22` is not limited to FPF pattern review or `DRR` review. It applies when a quality-bearing object has a declared object-under-improvement evaluation: pattern version, `DRR`, architecture description, engineering work result, method, policy, text, benchmark result, declared transduction result, or other object whose quality values are supplied by an explicit characteristic space, scale set, rubric, review profile, quality bundle, or exact FPF pattern.

`E.22` belongs in Part E because it governs how an FPF-side quality review question is asked before the object-under-improvement evaluation runs. It does not belong inside `E.21` or `E.9.DA`, because those patterns supply object-specific characteristic spaces. It does not belong inside `C.16`, `A.17`, `A.18`, `A.19`, or `C.25`, because it does not define characteristics, scales, measures, characteristic spaces, or quality bundles. It is also not an engineering evaluation method: concrete engineering, design, architecture, or product-review methods stay in the object-under-improvement evaluations that govern them.

Object-specific specializations are not required merely because the object version under quality read is a pattern, `DRR`, engineering work result, architecture, policy, or text. The ordinary shape is: use `E.22` for the question frame; use the exact object-under-improvement evaluation for coordinates, floors, values, dominance, status, and repair. A specialization is admissible only when a recurring object family needs additional read purposes, result forms, or protected trade-offs that cannot be expressed by this generic frame plus the object-under-improvement evaluation.

If no object-under-improvement evaluation is named, `E.22` can only repair the question by requiring one. It cannot turn a bare "review anything" request into quality values.

#### E.22:4.1b - OEE/NQD read placement

`E.22` can frame a quality read over OEE/NQD material, but it does not become OEE/NQD doctrine.

When the object version under quality read is a generated candidate, `Front`, `Q-Front`, `Archive`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, parity report, refresh report, or declared transduction result, the frame names both:

1. the exact candidate, object version, or set-result family under quality read; and
2. the governing pattern that carries the live semantics.

Typical assignments:

When the declared object-under-improvement evaluation is also the `Q` side of an NQD or OEE comparison, the read may return a bounded portfolio of candidate improvement proposals, not one chosen improvement. Each proposal row states the `Q` movement sought, affected locus, protected trade-offs, closure test, and neighbour exit. The front is set by the object-under-improvement evaluation's declared comparison set, external candidate set, `SoTA` line, front, or archive; it is not inferred from the reader's preference that the object feels better. The portfolio can aim the object version under quality read, generated candidate, or candidate family toward that current non-dominated front, beyond the current front under one declared `Q` component without damaging protected components, or into a not-yet-covered high-`Q` region under declared `Q` components. Choosing which proposals to generate or retain, inserting candidates into a front or archive, publishing a shortlist, and refreshing parity stays with `C.18`, `C.19`, `G.5`, `G.9`, or `G.11`.

| Live read question | Object-under-improvement evaluation or governing pattern |
|---|---|
| Candidate novelty, use-value, surprise, constraint fit, diversity, originality, or resource efficiency | `C.17` or its declared characteristic space |
| NQD generation, descriptor/distance/insertion pins, front/archive semantics, illumination telemetry | `C.18` |
| Live candidate-pool treatment: widen, keep frontier, narrow, sunset, or reroute | `C.19` |
| Public selected-set result: `Shortlist`, `RankedShortlist`, narrowed selected-set transfer, abstain, or escalation | `G.5` |
| Benchmark or parity comparison over selected sets, archives, fronts, or method families | `G.9` |
| Refresh of shipped set results, archive telemetry, parity reports, or OEE/NQD pins | `G.11` |

`E.22` then selects the read purpose: `floorRead`, `exceptionalImprovementRead`, `paretoTradeoffRead`, `openQuestionDiscoveryRead`, `absorptionRead`, or a declared combination. It may ask whether the selected governing pattern has enough information to run, whether the read found a blocker, whether one candidate or set result can improve under the declared evaluation, whether a candidate-change proposal is worth generating, or whether a returned finding changed the object-under-improvement evaluation's result.

The same portfolio rule applies to the ordinary FPF self-use cases. When `E.21` or `E.9.DA` is the object-under-improvement evaluation and the requested purpose is exceptional improvement, the read should not stop at the first defect. It may return a bounded portfolio of non-dominated proposal rows across active coordinates: for example first-use usability, source-content preservation, relation precision, examples, decision-bearing content, and protected trade-offs. The external comparison may be current FPF neighbour practice, accepted `SoTA`, competing pattern candidates, prior front members, or an explicit declared use frontier supplied by the object-under-improvement evaluation. In this use, `SoTA` is the working external front assigned by the object-under-improvement evaluation or accepted source posture. An exceptional proposal may try to reach, maintain, or improve that externally assigned front, but the read itself does not assign `SoTA` to the object. `E.23` governs any repeated application and re-read of those rows.

This is the entry point that keeps OEE/NQD candidate changes from becoming unguided candidate changes. The read proposes candidate changes from object-under-improvement evaluation pressure: what quality movement is expected, what trade-off must be protected, what closure test would make the proposal worth retaining, and which neighbouring pattern must govern generation, pool policy, set-result publication, parity, or refresh.

It must not replace OEE/NQD semantics. In particular, an `E.22` frame must not treat `IlluminationSummary`, coverage, regret, review count, popularity, or one benchmark headline as a quality value unless the governing pattern and policy explicitly promote that signal. It must not rename a `Front`, `Archive`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, or `ParityReport` as a generic portfolio. It must not collapse candidate quality, archive/front relation, selected-set publication, parity, and refresh into one result.

#### E.22:4.1c - Front-like vocabulary harmonization

Different practices arrive with different words for nearly the same working question: "raise it to all `5`s", "make it exceptional", "reach `SoTA`", "move to the Pareto front", "improve the NQD `Q` side", "return a portfolio", or "publish a shortlist." `E.22` does not make those words synonyms. It turns them into one framed read question and names the object-under-improvement evaluation that supplies the exact meaning.

| Incoming vocabulary | First `E.22` question | Governing pattern or object-under-improvement evaluation |
|---|---|---|
| all `5`s, exceptional, high-coordinate quality | Which object-under-improvement evaluation supplies the coordinates and value meanings? | `E.21`, `E.9.DA`, `C.25`, or another exact quality evaluation |
| `SoTA`, current best, frontier practice | Who assigns the current external front, and what source posture makes it admissible? | object-under-improvement evaluation plus `E.8` source posture and exact `SoTA` rows |
| Pareto front, non-dominated option, no forced winner | Which dominance relation and comparison set are declared? | `E.21`, `E.9.DA`, `C.18`, `G.5`, or exact local characteristic-space pattern |
| NQD, Q-front, archive, open-ended search | Is the live claim candidate quality, novelty, diversity, archive/front semantics, pool policy, or refresh? | `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, `G.11` |
| improvement portfolio, proposal portfolio | Is this only proposal rows, or a selected set publication? | `E.22` for proposal rows; `E.23` for repeated application; `G.5` for selected-set publication |
| shortlist, ranked shortlist, selected set | Is a public set result being published? | `G.5`, with parity or refresh through `G.9` or `G.11` when live |

The practical first path is: name the vocabulary used by the requester, translate it to the first object-under-improvement evaluation question, then assign any claim that exceeds the quality-read frame to the governing pattern. This preserves discoverability without letting familiar words import a second ontology.

#### E.22:4.2 - Quality read purposes

`QualityReadPurposeSelection` uses these values:

| Purpose value | Use when | Required result shape |
|---|---|---|
| `floorRead` | The question is whether the object reaches a declared floor for the intended use. | blockers below floor, first repair locus, narrowed use or admissible stop. |
| `exceptionalImprovementRead` | Active coordinates already meet the floor, and the requester wants non-dominated improvements toward exceptional expression where feasible. | per-coordinate improvement candidate from current value toward `exceptionallyExpressedForDeclaredUse`, or a by-value no-candidate disposition saying why no non-dominated edit is feasible, needed, or admissible for that coordinate under the declared use. |
| `paretoTradeoffRead` | A candidate improvement may raise some coordinates while degrading usability, affordability, locality, corpus ecology, neighbour fit, or another quality. | non-dominated candidate comparison, protected-quality losses, and whether a variant should be ordinary-use, high-assurance, narrowed, or rejected. |
| `candidateImprovementProposalRead` | The requester needs one evaluation-shaped proposal or a bounded proposal portfolio before changing an object or generating OEE/NQD variants. | candidate-change proposal row or proposal portfolio with expected object-under-improvement evaluation movement, affected object locus or set-result locus, protected trade-offs, closure test, and neighbour exit when generation, pool policy, front or archive handling, publication, parity, or refresh is live. |
| `openQuestionDiscoveryRead` | The requester wants important unasked questions made visible rather than only answered checklist items. | questions classified as existing-coordinate issue, candidate new coordinate or overlay, or outside the current object-under-improvement evaluation with the exact object-under-improvement evaluation named. |
| `absorptionRead` | Returned review findings or suggested improvements are being absorbed. | applied or not-applied disposition plus coordinate-impact account: improved, floor-only, unchanged, worsened, trade-off introduced, or outside object-under-improvement evaluation. |

The purposes may be combined, but the result must keep them distinguishable. A floor blocker does not answer exceptional improvement. A trade-off warning does not by itself lower a coordinate unless the object-under-improvement evaluation says that the protected quality is active. Open-question discovery does not become permission to rewrite the object outside the declared object-under-improvement evaluation.

If no purpose is declared, the default is `floorRead` under the object-under-improvement evaluation's default floor. Absence of an explicit `exceptionalImprovementRead` means the reviewer is not obligated to propose every plausible edit toward `5`.

#### E.22:4.3 - Prompt grammar

A conforming request has this shape:

```text
Quality-read question:
  Object version under quality read: <exact object version>
  Object-under-improvement evaluation: <E.21 | E.9.DA | E.19 | C.16, A.19, or C.25 | C.17, C.18, C.19, G.5, G.9, or G.11 for OEE/NQD reads | declared characteristic space | scale set | rubric | review profile | other exact evaluation>
  Read purpose selection: <floorRead | exceptionalImprovementRead | paretoTradeoffRead | candidateImprovementProposalRead | openQuestionDiscoveryRead | absorptionRead | combined>
  Declared quality floor: <floor and scope, or "object-under-improvement evaluation default">
  Desired improvement aim: <floor-only | raise non-dominated coordinates toward exceptional | compare variants | propose candidate changes | discover missing questions | absorption impact>
  Protected trade-offs: <usability | affordability | repair locality | corpus ecology | neighbour fit | source-content loss under the object-under-improvement evaluation | entry and projection integrity | other exact properties>
  Open-question classification rule: <classify by existing coordinate | candidate coordinate or overlay | outside object-under-improvement evaluation>
  Candidate improvement proposal rule: <single proposal | bounded proposal portfolio | expected movement | affected locus | protected trade-offs | closure test | neighbour exit>
  Next-admissible-move hypothesis rule: <stop | first repair | narrow use | candidate improvement proposal | trade-off warning | outside-evaluation assignment | assignment to an exact neighbouring pattern>
  Expected result form: <blockers | per-coordinate improvement candidates | candidate-change proposal rows | bounded proposal portfolio | Pareto trade-off table | open-question classification | absorption impact account | next-move hypothesis list>
  Non-use boundary: <what this read must not certify, decide, plan, execute, publish, or rewrite>
```

The short form is admissible when only the floor is live:

```text
Quality-read question:
  Object version under quality read: <exact object version>
  Object-under-improvement evaluation: <exact evaluation>
  Read purpose selection: floorRead
  Declared quality floor: <floor>
```

If the short `floorRead` finds no blocker, a compact admissible-stop statement is enough. If it returns blockers, repairs, narrowed-use requirements, or outside-evaluation assignments, each actionable item becomes a `QualityReviewFindingRow` with exact locus, correction direction, and closure test. The short form makes the question cheap; it does not permit narrative returned work that cannot be discharged row by row.

#### E.22:4.4 - Purpose-specific reviewer questions

| Purpose | Ask the reviewer |
|---|---|
| `floorRead` | Which active coordinates, eligibility rows, statuses, or declared floors fail? What is the first repair, narrowed use, or admissible stop? |
| `exceptionalImprovementRead` | For each active coordinate already at the floor, what non-dominated edit could raise it toward exceptional expression, or why is no non-dominated edit feasible, needed, or admissible for that coordinate under the declared use? What exact text, case, relation, SoTA row, boundary, or example would have to change if a candidate exists? |
| `paretoTradeoffRead` | What became worse while visible coordinates improved? Which protected qualities changed: first-use cost, authoring cost, maintenance cost, neighbour cost, source-loss risk, entry and projection integrity, corpus ecology, or practical payoff? |
| `candidateImprovementProposalRead` | What candidate change or bounded proposal portfolio should be proposed, what object-under-improvement evaluation movement is expected for each row, what trade-off must be protected, what closure test would confirm the movement, and which neighbour governs generation, pool policy, selected-set publication, parity, refresh, decision, planning, or work if a proposal leaves the read? |
| `openQuestionDiscoveryRead` | What important question was not asked? Is it an issue under an existing coordinate, a candidate new coordinate or overlay, or outside this object-under-improvement evaluation under another exact object-under-improvement evaluation? |
| `absorptionRead` | After applying findings, which coordinates improved, which remained floor-only, which stayed unchanged, which worsened, which trade-offs appeared, and which issues moved to another exact object-under-improvement evaluation? |
| any declared purpose with next-move output | Given the object-under-improvement evaluation read, what next admissible move is only a hypothesis: stop, repair, narrow, candidate improvement proposal, outside-evaluation assignment, or assignment to an exact neighbouring pattern? What claim would require `C.11`, `C.24`, `A.15`, `A.20`, `A.21`, `A.10`, `B.3`, `C.18`, `C.19`, `G.5`, `G.9`, or `G.11` before it can be used? |

These are question forms, not mandatory result sections. A reviewer may answer compactly when the object is small and the declared purpose is narrow.

When any purpose returns work for the object version under quality read, the result uses `QualityReviewFindingRow` and names the affected object-under-improvement evaluation coordinate, eligibility row, status, protected quality, or outside object-under-improvement evaluation. Findings such as "improve wording", "make clearer", "add examples", or "tighten rationale" are nonconforming until they state the expected quality movement and the object-under-improvement evaluation effect.

#### E.22:4.5 - Result classification for absorption

`absorptionRead` does not end at "accepted", "applied", "not applied", or "done." Each material finding receives one of these quality-impact classifications:

| Absorption impact | Meaning |
|---|---|
| `coordinateImproved` | A named coordinate or eligibility row has better content evidence under the object-under-improvement evaluation. |
| `floorOnlyClosure` | A blocker or ambiguity was removed enough to carry the declared floor, but not enough to justify exceptional expression. |
| `unchangedBecauseAlreadySatisfied` | The returned suggestion was already satisfied by value in the object version under quality read. |
| `tradeoffIntroduced` | The applied change improved one property while introducing a cost, ripple, or protected-quality risk. |
| `qualityLossDetected` | The applied or proposed change would lower one active coordinate or protected quality. |
| `outsideObjectUnderImprovementEvaluation` | The suggestion belongs under another exact FPF pattern, evaluation, or decision object. |
| `notAdmissibleForDeclaredUse` | The suggestion is rejected for the declared quality-read purpose and non-use boundary. |

The absorption record may stay as a checklist, but the checklist is not the quality result. The quality result is the impact on the object-under-improvement evaluation's characteristic space, status, stop condition, non-use boundary, or assignment to another exact object-under-improvement evaluation.

#### E.22:4.5a - Actionable quality-review finding rows

When a quality read or quality review returns actionable findings, each actionable finding is represented as one `QualityReviewFindingRow`.

`QualityReviewFindingRow := <QualityReviewFindingRowId, ReviewFindingLocus, ObjectLocusUnderRepair, QualityReadPurposeEffect, ObjectUnderImprovementEvaluationEffect, ExpectedQualityMovement, CandidateImprovementProposalSet?, NextAdmissibleMoveHypothesis?, CorrectionDirection, ClosureTest, RowDisposition, DischargeEvidenceRef?>`

The row shape is active for any returned blocker, repair, narrowing, trade-off warning, open question assigned to the object version under quality read, or absorption item that requires executor action. It is not required for a clean `floorRead` that returns only an admissible-stop statement.

| Field | Meaning |
|---|---|
| `QualityReviewFindingRowId` | Stable row id such as `QR-E22-001`; not a range and not "all findings". |
| `ReviewFindingLocus` | Exact locus in the quality review or returned finding. |
| `ObjectLocusUnderRepair` | Exact section, row, name, example, relation, checklist item, SoTA row, or entry cue in the object version under quality read. |
| `QualityReadPurposeEffect` | Which purpose produced the row: `floorRead`, `exceptionalImprovementRead`, `paretoTradeoffRead`, `openQuestionDiscoveryRead`, `absorptionRead`, or a declared combination. |
| `ObjectUnderImprovementEvaluationEffect` | Object-under-improvement evaluation coordinate, eligibility row, status, protected quality, or outside object-under-improvement evaluation affected by the row. |
| `ExpectedQualityMovement` | Expected movement such as blocker removal, coordinate improvement, floor-only closure, quality-loss prevention, trade-off exposure, bounded non-use, or outside-evaluation assignment. |
| `CandidateImprovementProposalSet?` | Optional single proposal or bounded proposal portfolio, with expected object-under-improvement evaluation movement, affected locus, protected trade-offs, closure test, and neighbour exit for each row when generation, pool policy, front or archive handling, selected-set publication, parity, refresh, decision, planning, or work is live. |
| `NextAdmissibleMoveHypothesis?` | Optional stop, repair, narrow, candidate improvement proposal, outside-evaluation assignment, or assignment to an exact neighbouring pattern suggested by the read. |
| `CorrectionDirection` | The concrete repair, narrowing, non-use statement, or object-under-improvement evaluation assignment requested. |
| `ClosureTest` | What must be true in the changed object for the row to close. |
| `RowDisposition` | `open`, `applied`, `alreadySatisfied`, `notAdmissibleForDeclaredUse`, `movedToObjectUnderImprovementEvaluation`, or another local disposition with narrower meaning. |
| `DischargeEvidenceRef?` | Optional exact changed locus or unchanged-by-value locus used by the executor to show what was done. |

"Closed in general", "handled overall", "all rows done", and range closure are nonconforming. If one edit closes several rows, each row still keeps a separate `QualityReviewFindingRowId`, object-under-improvement evaluation effect, closure test, disposition, and discharge evidence.

#### E.22:4.5b - Quality-review record separation

A quality review keeps four records distinct:

1. `QualityReadQuestionFrame` states the question being asked.
2. The reviewer quality result states the object-under-improvement evaluation reading, returned findings, coordinate and value effects, protected-quality trade-offs, bounded non-use, and outside-evaluation assignments.
3. Executor discharge evidence states what changed, which row disposition was selected, and which changed or unchanged object locus is cited for each `QualityReviewFindingRow`.
4. The next reviewer re-read states whether the changed object now satisfies the object-under-improvement evaluation for the declared purpose.

Executor discharge evidence is not the reviewer quality result and is not quality closure by itself. An impact account may show intended or observed movement, but closure comes only from re-running the object-under-improvement evaluation on the changed object or from a reviewer statement that a row was already satisfied by value.

#### E.22:4.6 - Work order for using this pattern

One `quality review` is one framed read of one exact object version.

For one quality review:

1. Name the object version under quality read.
2. Name the quality-read object-under-improvement evaluation.
3. Select one or more quality read purposes.
4. State the declared floor and improvement aim for this read.
5. State protected trade-offs, open-question classification rule, candidate improvement proposal rule, and next-admissible-move hypothesis rule when they are live.
6. Ask the reviewer for the purpose-specific result shape.
7. Run the object-under-improvement evaluation.
8. If absorbing findings, record coordinate impact and trade-offs, not only disposition.
9. If proposing candidate changes, state expected object-under-improvement evaluation movement, protected trade-offs, closure test, and neighbour exit before changing the object or generating variants.
10. State any next admissible move only as a hypothesis unless the exact neighbouring pattern is also opened.
11. Stop that read when the result answers the declared purpose and states any remaining bounded non-use or outside object-under-improvement evaluation.

When the goal is repeated improvement of the object beyond this one read, use `E.23`. `E.23` invokes `E.22` for each review pass and governs row-atomic absorption across passes, object-under-improvement evaluation re-read of the changed object version, method-family or operation-family selection, and the stop, narrow, continue, switch method, or hold decision. `E.22` does not govern the repeated method.

`QualityReviewFindingRow` remains the row shape for returned actionable findings. Executor discharge evidence is not a quality value until the object-under-improvement evaluation re-reads the changed object or states that the row was already satisfied by value.

An all-`5` claim requires an explicit coordinate-value table over the changed object. It cannot be inferred from a floor-pass capsule, a clean discharge table, an external-review absorption pass, landing, popularity, adoption, or the absence of blockers.

#### E.22:4.7 - Self-application boundary

`E.22` may be used to frame a quality read of the `E.22` pattern text. In that case, the object-under-improvement evaluation remains `E.21`; `E.22` supplies only the question frame. A self-read may ask for `floorRead`, `exceptionalImprovementRead`, `paretoTradeoffRead`, `openQuestionDiscoveryRead`, or `absorptionRead`, but the coordinate values, stop result, and repair result still come from `E.21`.

A minimal `E.22` self-application frame is:

```text
Quality-read question:
  Object version under quality read: E.22 authored pattern version
  Object-under-improvement evaluation: E.21
  Read purpose selection: floorRead + exceptionalImprovementRead + paretoTradeoffRead + openQuestionDiscoveryRead
  Declared quality floor: 4 wellExpressedForDeclaredUse on active E.21 coordinates
  Desired improvement aim: raise non-dominated coordinates toward 5 where feasible
  Protected trade-offs: ordinary-use affordability; row-atomic discharge; no object-under-improvement evaluation replacement; no gate, release, or work overread; no reputation-medal scoring
  Open-question classification rule: existing E.21 coordinate | candidate E.21 overlay | outside E.21 under another exact object-under-improvement evaluation
  Expected result form: stable QualityReviewFindingRows plus E.21 coordinate capsule
  Non-use boundary: not a gate, release, assurance, project certificate, or self-certifying quality result
```

Do not create a second quality space in which `E.22` grades the `E.22` question frame. If the self-read exposes a weak question frame, repair the `E.22` text or narrow the declared use; if it exposes a problem in the object-under-improvement evaluation, use the exact object-under-improvement evaluation that governs that problem.

#### E.22:4.8 - Sufficient frame, lowering conditions, and reopen conditions

A `QualityReadQuestionFrame` is sufficient when another reader can recover the object version under quality read, the object-under-improvement evaluation, the selected read purpose, the declared floor or improvement aim, the protected trade-offs when improvement is requested, the classification rule for unasked questions when discovery is requested, the impact classification for absorption when returned findings are being applied, the candidate improvement proposal rule when proposals are requested, the next-admissible-move hypothesis rule when next moves are requested, and the non-use boundary for overread-prone results.

Lower the quality read of an `E.22` use, or repair the frame before running the object-under-improvement evaluation, when any of these is true:

1. object version under quality read is missing or depends on chat memory;
2. object-under-improvement evaluation is missing, so `E.22` would have to invent coordinates;
3. a bare request such as "review this" is later interpreted as `exceptionalImprovementRead` without having declared that purpose;
4. `exceptionalImprovementRead` lacks an active coordinate menu or expected per-coordinate improvement result;
5. `paretoTradeoffRead` lacks protected qualities even though the proposed change can affect usability, affordability, repair locality, corpus ecology, neighbour fit, or entry and projection integrity;
6. `openQuestionDiscoveryRead` lacks classification into existing coordinate, candidate coordinate or overlay, or outside object-under-improvement evaluation;
7. `absorptionRead` records accepted or applied disposition without coordinate-impact classification;
8. the frame lets the resulting quality read be overread as project evidence, assurance, gate, release, certification, safety, compliance, work authority, general approval, checklist-count closure, or discharge-count closure;
9. the frame asks the reviewer to treat popularity, adoption, prior use, absence of use, review count, reviewer praise, external-review completion, landing, release, or award-like signals as quality values rather than as possible pointers to content evidence under the object-under-improvement evaluation.
10. the frame asks for next action, recommendation, reassign, shortlist, refresh, plan, release, work, evidence, assurance, or gate result without saying whether the read may return only a candidate improvement proposal or next-admissible-move hypothesis, or must be assigned to the exact neighbouring pattern.
11. the frame asks for OEE/NQD candidate changes but does not state the object-under-improvement evaluation pressure that makes each proposal worth generating;
12. the frame asks for a proposal portfolio but does not name which neighbouring pattern governs generation, pool policy, front or archive handling, selection, selected-set publication, parity, or refresh.

Reopen or restate the frame when the object version, object-under-improvement evaluation, declared floor, active coordinate menu, protected trade-off set, external findings being absorbed, or expected result form changes. An object-under-improvement evaluation finding may also show that the requested purpose was too narrow; then the extra result is either added to the frame or marked outside the declared frame.


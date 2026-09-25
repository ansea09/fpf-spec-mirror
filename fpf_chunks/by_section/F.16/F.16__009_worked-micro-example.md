---
chunk_kind: "child"
pattern_id: "F.16"
pattern_title: "Worked-Example Template (Cross-Domain)"
section_id: "F.16:8"
section_title: "Worked micro-example"
source_path: "FPF-Spec.md"
output_path: "by_section/F.16/F.16__009_worked-micro-example.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "F.16 — Worked-Example Template (Cross-Domain)"
  - "F.16:8 — Worked micro-example"
line_start: 107898
line_end: 107931
dependencies:
  - "A.10"
  - "A.15"
  - "A.3"
  - "A.6.1"
  - "A.6.RCD"
  - "B.1.5"
  - "B.3"
  - "C.16.P"
  - "E.10.D1"
  - "E.13"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.12"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "actual values"
  - "boundary"
  - "direct relations"
  - "evidence"
  - "exact sources"
  - "optional cell"
  - "optional comparison table"
  - "practical gain"
  - "working situation"
---

### F.16:8 - Worked micro-example

#### F.16:8.0 - A complete constructed availability case

**Question and gain.** Does the supplied June observation support the service promise's 99.9% availability threshold? The example separates the measurement and acceptance result from a runbook's approval.

**Inputs and direct rules.** This is a constructed case, not a report of observed service performance. Take as independently admitted inputs the service-delivery Work `Delivery-June` and evaluation Work `Evaluation-July-1`, with their performers' A.13 cores and A.15.1 admissions already established. The exact A.2.3 promise clause `Availability-June` concerns the delivery Work's outcome. Its acceptance specification uses all 43,200 minutes in the 30-day June window, no exclusions, and the rule `availability = availableMinutes / 43200`; `Met` means at least 0.999 and `NotMet` means less. These two values are the declared result scale.

**Observation and basis.** The supplied C.16 observation `Availability-Trace-June` directly concerns the promised available/unavailable characteristic of `Delivery-June`. Under its stipulated complete-coverage measurement basis, exactly the first 40 minutes are unavailable and the remaining 43,160 minutes are available. The observation's subject, characteristic, window, unit and complete coverage are premises of this case; an alarm log without that measurement basis could not replace it. No distinct indicator relation or F.9 correspondence is needed.

**Application and result.** During `Evaluation-July-1`, the declared evaluation Method uses the exact A.6.1 application `Availability-Application-June` with `availableMinutes=43160`, `totalMinutes=43200` and `threshold=0.999`. It returns `43160/43200 = 0.999074074...` and binds `Met` as the acceptance result. If a separately recovered F.10 rule maps `Met` to `RequirementStatus=Satisfied` for this clause and window, that status can be reported; the application result alone is already the worked conclusion.

**Evidence and bounded use.** The descriptive A.10 account cites the exact observation-subject/measurement basis, promise-outcome fit, evaluation application and result-binding facts. Those independently established premises supply the evidence demanded by this acceptance rule, so `pass` is limited to explaining this June result. There is no separately named assurance claim, future-availability conclusion or permission claim.

**Replay and boundary.** The available and unavailable minutes sum to 43,200; 40 unavailable minutes is below the permitted 43.2; and the computed ratio exceeds 0.999. With 50 unavailable minutes the same rule would return `NotMet`. If complete coverage were missing, this worked evidence basis would not support either conclusion; return the rule's missing-evidence question instead of inventing coverage or a pass.

#### F.16:8.1 - Applying the canvas to a multi-source availability case

The following is an application sketch. Supply the named source passages, exact relations, observations and result before claiming it is a completed worked example.

**Title and situation.** *An alarm log does not by itself prove monthly uptime.* Operations has an approved runbook and a month of IEC task and alarm logs; a service report must judge the exact ITIL promise-content claim.

**Worked claim.** June uptime is judged from admissible observations of the promised service outcome over the stated population and window. Alarm and command records may contribute evidence only through explicit relations and coverage limits.

**Actual subjects and routes.** The ITIL promise content and its promise-use, delivery, and fulfilment relations use A.2.3; the service-delivery Work and separate evaluation Work use A.15.1; the exact observations, availability characteristic, scale, and values use C.16; A.6.1 identifies the evaluation application and result binding; F.12 supplies the evaluation shape; A.10 describes the independently established evidence relations and qualifies the bounded reliance; and B.3 applies only when an actual named assurance claim is current. The runbook is a MethodDescription under A.3.2 only when its claims concern one admitted Method, and its edition is surfaced here only if it changes the evaluation result or replay.

**Source basis.** Cite the ITIL edition and promise passage, IEC edition and task and alarm passages, observation source and procedure, and any source-local meaning needed to interpret *availability* or *alarm*.

**Relations and limits.** State which observations concern which Work. First ask whether the observation and measurement model directly concerns the promised availability characteristic. If it does, use C.16 and A.10 and add no proxy. If alarm-state intervals instead indicate a distinct unavailable-service characteristic, name both participants and the pattern that defines or tests that relation, with covered modes and blind spots. Use C.16.P to recover the relation and stop at A.6.RCD `missing-governor` when no such rule exists. Use E.13 only when the indicator is optimized or drives a target, incentive, gate, release argument, reputation signal, repair, or decision. F.9 is needed only if the exact local meanings of *alarm state* and *unavailable service* are themselves related.

**Result.** A System performs evaluation Work, enacts the evaluation Method, and applies the declared availability rule to June's in-scope observations. The A.6.1 application binds those inputs and returns a result on the declared acceptance scale. Map it to `RequirementStatus=Satisfied` or `RequirementStatus=Violated` only through the exact F.10 rule. If the evidence is inadequate, use `EvidenceStatus=Inconclusive` and leave `RequirementStatus=Pending`, or return the exact local result declared by the scale. Create a verdict episteme only if another use needs it. Plainly: met, not met, or cannot judge. The approved runbook establishes none of these results or statuses.

**Checks.** Actual subjects; a defining or testing pattern for each relation; direct-measurement-before-proxy; evaluation Work, application and result binding; declared result scale; separate EvidenceStatus and RequirementStatus; matching window and population; visible indicator limit; and no row-created fact.


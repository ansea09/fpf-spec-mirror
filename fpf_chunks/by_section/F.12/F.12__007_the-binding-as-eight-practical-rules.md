---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
section_id: "F.12:6"
section_title: "The binding, as eight practical rules"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__007_the-binding-as-eight-practical-rules.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "F.12 — Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
  - "F.12:6 — The binding, as eight practical rules"
line_start: 131486
line_end: 131527
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.3.2"
  - "A.6.1"
  - "A.6.RCD"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.2"
  - "E.13"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.9"
  - "U.PromiseContent"
keywords:
  - "EvidenceStatus"
  - "PromiseContent"
  - "RequirementStatus"
  - "declared result scale"
  - "delivery Work"
  - "evaluation Work"
  - "indicator recovery"
  - "measured value"
  - "observation"
  - "operation result binding"
---

### F.12:6 - The binding, as eight practical rules

**R1 — Match the promise to delivery.**
Recover what the recipient was owed and identify the outcome that would discharge it. Was one service due for each recipient, or did the results have to work together? A signed receipt can settle a promise to deliver an existing report. A separately promised new review requires grounds that it took place. If the order leaves the method of judgement to the evaluator, select evidence that distinguishes the outcomes permitted by the terms. Keep the exact promise content, `PromiseContentUse`, delivery and fulfilment distinct under A.2.3. An abstract service label or lexical cell is not enough, and the later evaluation does not make those delivery-side relations obtain.

**R2 — Establish what the evidence concerns.**
Ask whether the evidence directly concerns the promised outcome in its window. A receipt naming the recipient and the promised edition may establish delivery. For a measured characteristic, check whether the observation and measurement model directly concern that characteristic. If they do, use C.16 for measurement and A.10 for evidence use. Commands, approvals and MethodDescriptions can establish a separately promised command, approval or document when the evidence supports it. A claim about a subsequent outcome needs grounds for that outcome.

**R3 — Recover an indicator relation when one is needed.**
If a distinct observed indicator stands in for the promised characteristic or outcome, name both participants and cite the pattern that defines or tests that exact relation. Use C.16.P to recover the construction and distortion risk. If no current rule supplies the relation, stop with A.6.RCD `missing-governor`; do not treat the word *proxy*, A.10 evidence use, or B.3 reliance as its substitute.

Use E.13 only when the indicator is optimized or used as a target, incentive, gate, release argument, reputation signal, repair target, or decision driver.

**R4 — Perform the evaluation.**
Select the delivery facts, affected-state references and measured values required by the acceptance rule. Apply its comparison or aggregation with the specified population, exclusions, uncertainty treatment and result scale, then state the supported result. For example, an incident rule can bind observed start and restoration times and compare their difference with the allowed duration. If an input is missing, establish that at least one history fits the evidence. If all such histories give the same result under the rule, use it. Incompatible premises may need correction, or independent sufficient grounds may settle the verdict directly. An established bound may settle a threshold. One failure can defeat a promise made to every member. When different results remain possible, state what is unresolved. A separately required observation or procedure keeps its own fulfilment condition.

When the claim or receiving use consumes a dated evaluation occurrence, recover each evaluator's A.13 core and let A.15.1 independently admit that Work before asserting that it enacts the evaluation Method, as A.2.3:4.3 requires. Add F.6 only for precise assignment-bound attribution.

Recover an exact A.6.1 application and its argument/result binding when claimed or required by the rule. Cite a particular MethodDescription edition when its content changes the evaluation or replay.

**R5 — Use the declared result scale.**
Read the admissible results from the acceptance specification’s `verdictScaleDescriptionRef`. For a measured promise, recover the characteristic, scale, unit, aggregation and comparison used by its rule. Typical calculation shapes include:

* a value at or above, or at or below, a threshold;
* a stated percentile at or below a target;
* a share such as good time divided by total time;
* an event count within a limit;
* all relevant values remaining inside a band.

The calculation shape does not select a verdict scale. Use the exact scale declared by the acceptance specification.

**R6 — State every needed relation directly.**
Use A.2.3 for promise use, delivery, and fulfilment; C.16 for observation and measurement; the defining or testing pattern for any indicator relation; A.10 for the descriptive evidence-provenance path and bounded reliance on independently established direct relations; B.3 only for an actual named assurance claim; and F.9 only when distinct local meanings themselves require a semantic relation.

One generic Bridge cannot establish clause–Work fit, measurement, indicator validity, evidence, evaluation, status, or fulfilment. A passing reliance disposition requires the evidence demanded by the acceptance claim and its direct rule; a descriptive path alone is insufficient.

**R7 — Keep the window and population explicit.**
A monthly verdict, a batch verdict, and an incident verdict are different claims. A new promise, monitor, or window does not rewrite an earlier verdict.

**R8 — Preserve result, status, and assertion boundaries.**
Keep the result on its declared acceptance scale. When the evidence leaves more than one fulfilment outcome open, state the unresolved decision and its grounds. Assert a RequirementStatus such as `Satisfied`, `Violated` or `Pending`, or an EvidenceStatus such as `Inconclusive`, only under its applicable F.10 rule. Create a verdict episteme when another use needs that durable assertion.


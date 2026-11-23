---
chunk_kind: "child"
pattern_id: "C.11"
pattern_title: "Decision Theory (Decsn-CAL)"
section_id: "C.11:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11/C.11__006_archetypal-grounding.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "C.11 — Decision Theory (Decsn-CAL)"
  - "C.11:5 — Archetypal Grounding"
line_start: 59928
line_end: 59978
dependencies:
  - "A.10"
  - "A.13"
  - "A.18"
  - "A.19"
  - "A.6.5"
  - "A.6.P"
  - "C.11.CRC"
  - "C.11.DUA"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.26"
  - "C.38"
  - "C.39"
  - "C.40"
  - "C.9"
  - "E.10.LRN"
  - "G.5"
keywords:
  - "ChoiceResult"
  - "ChoiceRule"
  - "DecisionSubject"
  - "OptionSet"
  - "ValueOfComputation"
  - "ValueOfInformation"
  - "choose now"
  - "comparison basis"
  - "decision theory"
  - "non-shared comparison frame"
  - "probe again"
  - "probe-worthiness"
  - "question order"
  - "reject current set"
  - "reroute"
---

### C.11:5 - Archetypal Grounding

#### C.11:5.1 - System grounding

**Tell.** A research team already has three experiment plans on the table. The option set exists. The question is to decide which plan to run and whether one more measurement is worth the delay.

**Comparison.** The team can choose among three feasible plans. It first minimizes the predicted number of missed defects per 100 reference cases. It breaks ties by schedule. Its current estimates use two equally likely calibration states.

| Calibration state | Plan A | Plan B | Plan C |
| --- | ---: | ---: | ---: |
| First | 4 | 2 | 5 |
| Second | 6 | 5 | 3 |

On this basis, A averages 5 misses, B averages 3.5 and C averages 4. If the team must choose now, its rule selects B.

**Probe.** A one-day calibration run can identify the state before the plan is fixed. The team could then choose B in the first state and C in the second, for 2.5 expected misses per 100. The improvement over choosing B now is one expected miss per 100. The day fits the budget, and the team judges that avoiding this loss is worth the delay.

**Result.** The current `ChoiceResult` is `probe again`. Once the run identifies a state, apply the comparison in that row. If the run becomes unavailable while the estimates and rule still hold, B remains the supported choice on the present evidence.

**Show.** Use `C.38` if the team must turn labels or fragments into complete ways of obtaining one result. Use `C.39` if a plan still lacks an explanation of how to obtain that result, or `C.40` if the team can vary a plan and needs to examine the difference. Use `C.18` when the team needs a generation account or archive/front claim; `C.19` for exploration policy over the plan pool; and `C.24` for the run sheet and execution order after choice.

#### C.11:5.2 - Episteme grounding

**Tell.** A planning team has three models for predicting restart delays. It needs one forecast for the staffing decision due tomorrow. For this use the team judges a model by its mean absolute timing error on comparable held-out shifts.

**Comparison.** Under the agreed mix of shifts the three models miss restart time by 6, 3 and 5 minutes on average. All three can supply the forecast in time. The current comparison supports model 2. Choosing it for staffing does not establish which mechanism caused the delays.

**When another comparison matters.** Suppose tomorrow’s roster includes a previously unrepresented shift. Applying all three models to the same set of comparable logged shifts could change their order. Check whether those logs can be obtained before the roster is fixed and whether the resulting change in staffing would justify the effort.

**Result.** For the original mix, choose model 2 on its lower error. For the changed mix, return `probe again` if the log comparison is feasible and worth doing. If the logs are unavailable and the previous order cannot be supported for the new mix, report that limit to the planner.

**Show.** This pattern governs neither open-ended hypothesis generation nor operational rollout. Those questions stay outside this pattern even when the decision later feeds them.

#### C.11:5.3 - Collective and contextual grounding

**Tell.** A clinical board must decide whether to escalate a patient now or order one more test. The board is the chooser, not one isolated individual, and the result shifts when the case is discussed in prognosis-first versus risk-first order.

**Show.** `C.11` keeps the case legible by typing the chooser as one `DecisionSubject` at explicit `DecisionSubjectGranularity`, keeping the available actions as one current `OptionSet`, keeping one explicit `BeliefState` and `OutcomeModel` around those actions, and asking whether another test belongs in the `ProbeActionSet` with enough expected value to justify its `CostToProbe`.

**Show.** The changing patient state and the board's update process matter when they change feasible actions or estimated consequences. The observed order effect requires an explicit comparison-order account. Neither collective choice nor an order effect alone establishes that active-inference or quantum-like formalism is needed; use a branch only for the remaining limitation it addresses.

**Show.** If the order effect still changes which option survives, the comparison should say that directly and keep the comparison unfinished. The next comparison move is then either one framing-stabilizing probe or declaring the comparison order under which the current result will be judged. The record should identify that comparison instability instead of describing it only as mixed intuitions.

**Show.** An admissible output here therefore looks like one of three concrete records:

- `ChoiceResult = probe again with a comparison under both stated question orders because it can distinguish a missing prognosis premise from a framing-dependent ranking; the expected decision gain justifies the feasible delay`;
- `ChoiceResult = choose now and escalate because the receiving decision accepts the declared risk-first comparison, and no further feasible test offers enough expected decision gain to justify the harmful delay`;
- `ChoiceResult = reroute to C.24 because the board has already chosen escalation and the next task is now treatment sequencing rather than local choice`.

**Show.** Record which comparison the board used, its conclusion and whether the board acted on it. When the ranking still depends on an unresolved framing choice, retain that uncertainty.


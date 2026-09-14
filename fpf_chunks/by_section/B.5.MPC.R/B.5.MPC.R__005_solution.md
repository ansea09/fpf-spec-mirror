---
chunk_kind: "child"
pattern_id: "B.5.MPC.R"
pattern_title: "Repair a Physical-Mathematical-Computational Connection"
section_id: "B.5.MPC.R:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MPC.R/B.5.MPC.R__005_solution.md"
commit_sha: "f965ffb27d69ec5e4ae94f1bb0092c15fa13c991"
heading_path:
  - "B.5.MPC.R — Repair a Physical-Mathematical-Computational Connection"
  - "B.5.MPC.R:4 — Solution"
line_start: 43015
line_end: 43092
dependencies:
  - "A.15.9"
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5"
  - "B.5.MPC"
  - "B.5.RR"
  - "C.16"
  - "C.29.1"
  - "C.29.2"
  - "C.29.3"
keywords:
---

### B.5.MPC.R:4 - Solution

Keep the receiving physical question in view while tracing the failed connection:

**State the changed result or disagreement → recover the contributing relations → locate the incompatible use → construct a sufficient repair → carry it through the affected contributions → use the revised physical consequence.**

These are dependencies of the repair. A known physical change, a failed calculation or a surprising observation can each be the starting point.

#### B.5.MPC.R:4.1 - Compare results for the same physical question

Name the physical difference that the answer must resolve and the conditions under which it is wanted. Put the attempted result beside the changed request or observation. Recover the participants, units, times and operating regime needed to compare them.

For instance, a predicted displacement during eight seconds of motor operation and a measured displacement during eleven seconds concern different durations. Aligning the comparison may already explain the discrepancy.

If the question changed, say which quantities are now supplied and which must be determined. Keep the physical relation available while choosing its new use. A velocity-to-duration calculation can become a duration-to-command calculation.

If the comparison concerns a performance claim, recover the observation and its measurement relation. An acknowledgement can supply information about command reception while leaving physical completion unobserved.

#### B.5.MPC.R:4.2 - Recover what each contribution supplies to the next

Start at the mismatch and follow the needed relations in both directions. Ask what the receiving operation takes as input, what the supplied result actually represents and which condition permits that use.

The following questions distinguish common repair locations. Use the ones that can explain the disagreement.

| Connection to inspect | Question that can locate a repair |
| --- | --- |
| Physical account to mathematical formulation | Which interaction, boundary or operating assumption licenses this equation or constraint? |
| Mathematical formulation to computation | Does the procedure obtain the quantity or property now requested, with the required constraints and approximation? |
| Representation to another representation | Which distinction or operation must survive, and does the correspondence preserve it? |
| Computation to executing arrangement | Can the arrangement prepare the input, perform the operation and finish with the state or result being used? |
| Observation to physical inference | Which physical possibilities can produce this indication under this measurement procedure? |

Explain an unresolved connection in the working notation. Use B.5.RA to recover a needed argument and B.5.RC to recover a construction. C.29.1 compares mathematical transfers; C.29.2 constructs a computation; C.29.3 compares a computation with its realization. Their results answer the corresponding rows, while the physical question determines which row matters.

Keep a common premise visible across different contributions. An analytical calculation and a simulation that both assume no slip leave the same question open when slipping is suspected. A different algorithm is a sufficient alternative only if its premises and output interpretation fit the receiving use.

#### B.5.MPC.R:4.3 - Locate the incompatibility without guessing its cause

Work a small instance or derive a consequence that distinguishes the competing accounts. If a command is outside the admitted range, its value and range already establish that incompatibility. If two physical inputs produce the same represented data but require different answers, exhibit those two inputs and their common representation.

When several explanations remain, compare what each would require you to change. A motion discrepancy might come from calibration, a retained command or an incorrectly interpreted position. Recover an available observation that distinguishes those accounts, or choose a worthwhile further observation through C.11.DUA. An investigation is unnecessary when a sufficient bound or conditional answer already settles the present decision.

Account for what the observation does. Identify which processes continue during measurement or debugging, which input remains applied and which state is changed by the probe. Use A.3.3 for the state and C.16 for the measurement relation when that construction is unresolved.

A mathematical account may support several physical interpretations. Compare their additional physical assumptions and the observations or interventions that distinguish them. Retain an unresolved difference when the available observations do not decide it; use the consequences shared by those interpretations when they suffice.

#### B.5.MPC.R:4.4 - Construct the repair that the receiving use needs

Choose the contribution that can remove the located incompatibility. The choice follows its cause and the wanted result.

- If the requested unknown changed, retain the interpreted relations, release the former fixed value where appropriate and derive the new computational direction.
- If a representation merged cases that the question must distinguish, retain the missing information, obtain a different observation or use a result that the merged representation still supports.
- If the procedure uses the wrong operation, constraint or approximation, replace that part and establish the property the receiving use needs.
- If the physical or measurement account omits a consequential interaction, model that interaction or change the arrangement so that the retained account applies.
- If execution differs in preparation, range, state or completion, revise that part of the realization or choose an available realization that supplies the required behavior.

An expression of an equation states a relation; an assignment or solver performs a chosen operation. Keep the equation's meanings when generating or editing that operation. A modelling environment can help transform the equation system, but the physical interpretation and the requested result still guide the choice.

Compare the repair with a sufficient alternative. Changing a deadline may be cheaper than replacing an actuator. A useful ambiguity result may suffice before changing measurement equipment. Present a changed requirement as a choice for the receiving work.

#### B.5.MPC.R:4.5 - Carry the repair through its dependents

Use B.5.RR to derive the affected consequences. Reuse contributions whose conditions and meanings still fit; revise each needed use of a changed shared premise.

Compare the repaired contributions on the same input or physical case. For a mathematical change, derive the needed property. For numerical work, carry the error relevant to the physical question. For an execution claim, compare the prepared state, operation and interpreted observation with the intended result.

Keep the comparison at the claim's scope. A conditional calculation can establish what a proposed arrangement would do under its assumptions. Actual performance requires the observations and inference appropriate to that use.

If the comparison still fails, follow the remaining disagreement. Do not repeat a test that leaves the live alternatives indistinguishable. Change the question or obtain the missing contribution when the present means cannot settle it.

#### B.5.MPC.R:4.6 - Return the physical consequence and the next useful action

State what can now be understood, constructed or changed. Return a usable command, corrected interpretation, realizability bound or a remaining ambiguity with its effect on the receiving decision.

When work is divided, give the next contributor the quantities and conditions at the unresolved connection, the result needed and how it will be used. The receiver must be able to reconnect the supplied contribution to the physical question. A.15.9 helps obtain that contribution.

The repaired reasoning may reveal another worthwhile problem: extending an operating regime, constructing a more informative measurement or developing an operation for a changed class of questions. Carry that possibility into B.5's next inquiry when pursuing it would enable further work.


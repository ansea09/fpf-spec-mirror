---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__012_sota-echoing.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:11 — SoTA-Echoing"
line_start: 9341
line_end: 9364
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.27"
  - "C.27.TA"
  - "C.29"
keywords:
  - "calibration"
  - "configuration"
  - "constraints"
  - "dynamics"
  - "initial data"
  - "observation relation"
  - "permitted alternatives"
  - "prediction"
  - "predictive memory"
  - "probability law"
  - "simulation"
  - "state construction"
  - "transition law"
---

### A.3.3:11 - SoTA-Echoing

**Choose a predictive description for the question being asked.** In :5.6 the available observation is the total mass, but the next total depends on its hidden composition. Compare the descriptions under the same fixed retention law and exact-reading premises:

| Available description | What it answers | Added effort and limit |
| --- | --- | --- |
| One present total | Bounds the next total between one quarter and one half of the present total. | Cheapest when that interval settles the question; it cannot select one exact next value under unequal retention. |
| The two component masses | Determines the next state and total directly. | Requires observing or otherwise establishing the composition. |
| Two consecutive exact totals | Recovers the two masses, then predicts by the derived second-order recurrence. | Replaces a composition observation with a second timed reading; noisy readings require an error account. |

For a present total of 1 kg, the interval [0.25, 0.5] kg already settles whether the next total is at most 0.6 kg. It leaves an at-most-0.4 kg question unresolved. Acquire composition or a sufficiently informative history only when that remaining uncertainty matters. Equal retention restores a one-total transition law, so the extra state or reading becomes unnecessary.

[Lin and Lu, §§2.1–2.2](https://arxiv.org/html/1908.07725v5) supplies the methodological comparison line: selected observables can discard information that reappears as memory in a reduced description. Its exact projection identity still requires closure choices for a usable reduced model; its statistical treatment uses a stationary-process setting. The elementary calculation above is an authored construction. It selects the state–observation distinction in :4.1–:4.2 and the question-dependent choice in :5.6, with a measurable cost: additional coordinates or observations only when the cheaper description is insufficient.

**Strengthen support when the use changes.** For data-driven predictive control, [de Jong and colleagues, §§I–IV, especially III and Theorem IV.2](https://arxiv.org/html/2405.01292v1), compare iterated one-step lifted models with directly learned multi-step predictors. They choose the latter to avoid propagating one-step prediction errors across the horizon, at the cost of learning horizon-dependent prediction matrices and observables. Their constrained controller adds an interpolated initial state and terminal ingredients; recursive feasibility depends on the stated terminal-set assumption and a feasible preceding problem. These are contributions to a particular control problem.

Accordingly, :4.6 makes the intended consumer specify the prediction conditions and properties it relies on. A control decision that relies on recursive feasibility must establish the relevant model, constraints and feasibility conditions. An ordinary comparison can finish with the state, law, observation and applicability information sufficient for its question. The extra cost of a stronger guarantee is incurred by the use that needs it.

Reopen the chosen description when the observation error, retention law, horizon or question changes enough to defeat its information or error bound. Reopen a control use when its measured prediction errors or operating conditions defeat the assumptions supporting its selected guarantee.

**Construct before reducing.** Tong's [generalized-coordinate construction, §2.3](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) supplies a way to represent configurations satisfying constraints. His [field-theory discussion, §1.1.2](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S1.html) shows that the interpretation and time order of a field law determine its initial data. Section :4.4.1 adopts the common sequence from participants and constraints to predictive information; the particular forces, field equations and solving Methods remain subject contributions. Retaining an implicit constraint can be preferable to eliminating it when the elimination obscures the relation being investigated.

The deterministic comparison in :5.6 and stochastic comparison in :5.8 ask which distinctions prediction needs. Long-run averaging answers a separate question about repeated evolution. In :5.9, a range over allowed executions is available before their probabilities are known. Choose the transition representation that answers the present question with the information available.


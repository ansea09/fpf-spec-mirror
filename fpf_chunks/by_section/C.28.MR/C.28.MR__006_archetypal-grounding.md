---
chunk_kind: "child"
pattern_id: "C.28.MR"
pattern_title: "Derive an Intervention Consequence by Mechanism Replacement"
section_id: "C.28.MR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28.MR/C.28.MR__006_archetypal-grounding.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "C.28.MR — Derive an Intervention Consequence by Mechanism Replacement"
  - "C.28.MR:5 — Archetypal Grounding"
line_start: 72289
line_end: 72330
dependencies:
  - "A.3.3.TR"
  - "B.5.MPC"
  - "B.5.RR"
  - "C.28"
  - "C.29.1"
keywords:
---

### C.28.MR:5 - Archetypal Grounding

#### C.28.MR:5.1 - Observing an alarm and forcing its output

Let H mean binary high load and S mean a binary alarm. Take independent uniform inputs `U_H,U_S` on [0,1] and the supplied mechanisms

`H = 1[U_H < 0.5]`

`S = 1[U_S < 0.1 + 0.8 H].`

Here `1[condition]` is one when the condition holds and zero otherwise. In high-load cases, the alarm sounds with probability 0.9. In low-load cases, it sounds with probability 0.1.

The observational probability of no alarm is `0.5*0.1 + 0.5*0.9 = 0.5`. High load with no alarm has probability `0.5*0.1 = 0.05`. Thus `P(H=1 | S=0)=0.05/0.5=0.1`: the observation changes what we infer about the load.

For `do(S=0)`, replace the second mechanism by `S=0`. The equation for H and the input law are retained. Therefore `P(H=1 | do(S=0))=0.5`. Forcing this indicator removes its information about H without changing H in the supplied model.

For a particular past episode the answer uses what was observed *in that episode*. Suppose the alarm sounded and load was unobserved. The factual mechanisms give `P(H=1 | S=1)=0.45/(0.45+0.05)=0.9`. In the alternative where the alarm was silenced at that instant, its replacement leaves H unchanged for each compatible underlying input. The probability of high load in that alternative given the original alarm is therefore 0.9. Drawing a fresh episode from the population would give 0.5. Treating the imposed silence as an observation of a naturally silent alarm would give 0.1. Each number answers a different question.

All three calculations concern current load under the stated absence of an S-to-H influence at that instant. If alarm output controls subsequent cooling, a later-load query needs that later mechanism and the duration of the override.

#### C.28.MR:5.2 - Change a display or a supply command

Consider an ideal regulated supply and a resistive load. C is the command in volts, V the delivered voltage, D the displayed voltage, R a fixed resistance, I the load current and W its power. In the operating region being modeled,

`C=12 V; V=C; D=V; R=6 ohm; I=V/R; W=V I.`

The natural result is `I=2 A` and `W=24 W`.

Replacing the display equation by `D=6 V` leaves `V=12 V`; current and power remain 2 A and 24 W. Replacing the command equation by `C=6 V` instead gives `V=6 V`, `I=1 A` and `W=6 W`. The two changes share a numeral but replace different mechanisms.

Suppose the supply's current limit is now relevant. Use the revised positive-command model `V=min(C, I_max R)` with `I_max=1.5 A`. The 12 V command now gives 9 V at the load and 13.5 W. The 6 V command still gives 6 W. Relative to natural behavior, the calculated power reduction is now 7.5 W, instead of 18 W in the earlier operating-region model.

To use this comparison for a physical supply, establish its regulation, load and limiting behavior. Editing a displayed number can be a real change to the display. The calculated effect on load current applies to a change of supply command. Establish which mechanism the interface changes and whether a controller later acts on its reading.

#### C.28.MR:5.3 - A definite intervention answer with an indefinite baseline

Take real-valued variables with mechanisms `X=Y` and `Y=X`. Every equal pair satisfies the baseline equations. Without another condition, the model does not determine the baseline value of Y.

Replace the first mechanism by `X=1`. The retained equation now gives `Y=1`. That intervention consequence is determined. A difference from the baseline remains undetermined because the baseline's value or distribution has not been supplied.

If the requested result is only Y under the intervention, return one. If the requested result is its change from natural behavior, return the missing baseline condition. Resolving the first question does not require inventing that condition.


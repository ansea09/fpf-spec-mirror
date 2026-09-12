---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__006_archetypal-grounding.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:5 — Archetypal Grounding"
line_start: 9214
line_end: 9283
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

### A.3.3:5 - Archetypal Grounding

#### A.3.3:5.1 - Reactor control

A reactor team models temperature and concentration with a nonlinear ODE and disturbances. Identify the reactor as the changing subject, specify the two state coordinates, and declare the ODE, disturbances and applicable operating region. The resulting episteme meets :4.1 when those state-space and law claims are present under its reference scheme.

For a thermocouple comparison, the observation relation selects temperature from the modeled state. Align the observed and predicted temperatures over the comparison window, then use the tolerance and validation conditions required by :4.6. Changes to a control policy change the model's input; selecting and describing that policy uses the Method contributions in :4.3.

If the question concerns an actual regeneration of the catalyst bed, recover that event's boundary, observed bed conditions and continuity or reidentification under A.3.4. A proposed trajectory remains available for prediction; the actual-change claim needs the occurrence facts.

#### A.3.3:5.2 - Reliability and operations

A service platform models backlog, arrival rate and incident recovery with a queueing or birth-death model. Compare its predicted behavior with the stipulated service objective under the model's operating assumptions. If that comparison is used for a release decision, apply :4.6.

#### A.3.3:5.3 - Evolutionary architecture

An architecture group tracks latency, coupling, operational cost, and change lead time across releases. An episteme about that architecture can be `U.Dynamics` when its `ClaimGraph` declares a state space over those characteristics and a discrete-time transition map as the transition law.

#### A.3.3:5.4 - Knowledge dynamics

A claim portfolio uses belief, evidence weight, source currentness, and contestability as state coordinates. An episteme declaring a Bayesian or likelihood update as the transition law over that claim-state space is `U.Dynamics`. Identify which incoming observation changes a belief coordinate under the update rule. Name the source content used to support or challenge the specified claim for that update.

#### A.3.3:5.5 - Natural physical evolution

A `U.Dynamics` episteme can model the Moon's motion around Earth using an orbital state space and transition law.

#### A.3.3:5.6 - When the observed total is not enough to predict

A team wants to predict how much of two removable substances will remain after treatment. For this worked model, let `a_n` and `b_n` be their nonnegative remaining masses in kilograms after `n` cycles. Assume that each cycle leaves half of the first substance and a quarter of the second, with no new material added:

`a_(n+1) = a_n/2`, `b_(n+1) = b_n/4`.

The instrument reports only their total, `y_n = a_n + b_n`. The model's state is `(a_n, b_n)`; its observation relation maps that pair to the total. The states `(1, 0)` and `(0, 1)` both give `y_0 = 1 kg`, but their next totals are `1/2 kg` and `1/4 kg`. No deterministic law using only the current total can reproduce the next total for every admitted state.

Retain the two masses when they are available. If only totals are observed, two successive exact readings recover the composition in this model: solve `a_0 + b_0 = y_0` and `a_0/2 + b_0/4 = y_1`, giving `a_0 = 4y_1 - y_0` and `b_0 = 2y_0 - 4y_1`. These masses must be nonnegative. Substitution into the next-cycle law gives `y_2 = (3/4)y_1 - (1/8)y_0`; the same recurrence applies at every later cycle. The prediction now uses one previous total as well as the current one. Equivalently, take that pair of totals as the predictive state.

If only the initial total is available, the model still gives a range: for integer `n ≥ 0`, `y_0/4^n ≤ y_n ≤ y_0/2^n`. Each extreme is attained by putting all the initial mass in one substance. Use this range when it answers the working question; otherwise obtain information about the composition. If the two substances instead have the same known retention factor `r` with `0 ≤ r ≤ 1`, the total alone obeys `y_(n+1) = r y_n`. Thus whether aggregation preserves the needed law depends on the modeled operations.

The calculation assumes exact readings and fixed retention factors. Applying it to treatment data requires accounting for measurement error and establishing the retention law over the intended operating range. [Lin and Lu, §§2.1–2.2](https://arxiv.org/html/1908.07725v5) explain the broader state/observation and model-reduction problem; the two-substance case here supplies an elementary construction.

#### A.3.3:5.7 - A constraint changes the state description

Two endpoints move in a plane and are connected by a rigid link of length `l > 0`. Four Cartesian coordinates obey `(x2-x1)^2+(y2-y1)^2=l^2`. One configuration description uses three coordinates: place the first endpoint at `(X,Y)` and the second at `(X+l*cos(phi),Y+l*sin(phi))`, with `phi` taken modulo a full turn. The construction makes the length constraint hold. To predict motion under an ordinary second-order mechanical law, also supply the required velocities and the forces or other interactions.

Change the question to longitudinal vibration of an elastic link. Fixed `l` has removed the extension that matters. Replace it with variable length `r`, keep its rate of change when required, and obtain the restoring interaction from the physical model. A rigid-link calculation remains useful for its earlier premise; the elastic question needs another state and law. [Tong, Classical Dynamics, §2.3](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) supplies the generalized-coordinate method; the two-endpoint comparison here applies it.

In another practice, two queues share a fixed total of `N` items. Retain `q1` and recover `q2=N-q1`, with `0<=q1<=N`. If external arrivals are admitted, the state must retain the changing total or both queue sizes. The source of the constraint changes, while the construction still identifies which values can vary independently.

#### A.3.3:5.8 - A long-run average can coexist with predictive memory

Consider a three-state Markov model with this transition matrix. A readout reports 0 for A or B and 1 for C.

| Present state | Next A | Next B | Next C |
| --- | --- | --- | --- |
| A | 0.7 | 0.2 | 0.1 |
| B | 0.1 | 0.2 | 0.7 |
| C | 0.2 | 0.3 | 0.5 |

A present readout of 0 merges states with next-1 probabilities 0.1 and 0.7. The readout alone therefore leaves predictive information unresolved. The stationary distribution is `(19/54,13/54,22/54)`. At stationarity, after readouts `1,0`, the current A/B weights are `2/5,3/5`, so the next-1 probability is `23/50`. After `0,0`, those weights are `73/105,32/105`, giving `99/350`. A decision that changes above probability 0.4 takes different actions after these histories. Keeping only the present 0 and the stationary A/B mixture gives `11/32` and loses that difference.

Condition on the available history or retain the resulting predictive distribution. With no information beyond the current 0, the range `[0.1,0.7]` may already answer a weaker question. The full finite chain is irreducible and aperiodic, and its long-run proportion of readout 1 converges to `22/54`. That long-run result leaves the history-dependent prediction above intact. The finite-chain results are given in [Cambridge's Markov Chains notes, §§9-10](https://www.statslab.cam.ac.uk/~rrw1/markov/M.pdf); the matrix and conditional calculations here are an authored example.

#### A.3.3:5.9 - Possible execution orders do not supply a probability law

Two participants A and B each read shared integer `x` into a local saved value, then write that saved value plus one. Each read or write is atomic, and each participant's read precedes its write. Initially `x=0`. To follow the permitted reads and writes, use `x`, each participant's position in its two-step procedure and any value already read.

There are six interleavings that preserve those local orders. Only `readA,writeA,readB,writeB` and its A/B reversal finish at 2. The other four finish at 1: both reads occur before either write, so each participant later writes 1. This enumeration identifies allowed histories that defeat the intended two-increment result.

The six histories have no assigned execution probabilities. Inferring a probability of 2/3 for a lost increment from these counts requires a scheduler model that justifies equal likelihood for the six histories. To obtain the intended result for every allowed history, serialize the read-and-write pairs or supply an indivisible increment operation. If that repair introduces waiting, separately check the progress condition required by the use.


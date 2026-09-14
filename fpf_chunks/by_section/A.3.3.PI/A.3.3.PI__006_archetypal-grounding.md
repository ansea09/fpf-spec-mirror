---
chunk_kind: "child"
pattern_id: "A.3.3.PI"
pattern_title: "Retain the Information Needed for Prediction"
section_id: "A.3.3.PI:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.PI/A.3.3.PI__006_archetypal-grounding.md"
commit_sha: "f965ffb27d69ec5e4ae94f1bb0092c15fa13c991"
heading_path:
  - "A.3.3.PI — Retain the Information Needed for Prediction"
  - "A.3.3.PI:5 — Archetypal Grounding"
line_start: 10168
line_end: 10233
dependencies:
  - "A.3.3"
  - "A.3.3.CC"
  - "A.3.3.TR"
  - "B.5.FM"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.29.1"
keywords:
---

### A.3.3.PI:5 - Archetypal Grounding

#### A.3.3.PI:5.1 - Recover a treatment forecast from component masses or a short history

Let a_n and b_n be nonnegative masses in kilograms after n treatment cycles. Each cycle leaves half of the first substance and a quarter of the second, with no new material:

    a_(n+1) = a_n/2
    b_(n+1) = b_n/4
    y_n = a_n + b_n

The instrument reports only y_n. States (a_0,b_0) = (1,0) and (0,1) both report y_0 = 1 kg but give next totals 1/2 kg and 1/4 kg. The aggregate has lost the composition needed for a unique next total.

One repair retains the two masses and updates them separately. Another uses two successive readings without measurement error. From y_0 = a_0 + b_0 and y_1 = a_0/2 + b_0/4,

    a_0 = 4*y_1 - y_0
    b_0 = 2*y_0 - 4*y_1
    y_2 = (3/4)*y_1 - (1/8)*y_0

The recovered masses must be nonnegative, requiring y_0/4 <= y_1 <= y_0/2. For y_0 = 1 kg and y_1 = 0.35 kg, the masses are 0.4 kg and 0.6 kg, and y_2 = 0.1375 kg.

The recurrence applies at later cycles under the same law. A rolling pair (previous total, current total) can replace the hidden component values for predicting future totals. On receiving a new total, retain it and the former current total. If no new measurement arrives, the recurrence can propagate the pair as a conditional model prediction.

With only y_0, nonnegativity yields the bound

    y_0/4^n <= y_n <= y_0/2^n, for integer n >= 0.

For y_0 = 1 kg, the next total is at most 0.5 kg. This settles a requirement at most 0.6 kg without learning the composition. A limit of 0.4 kg remains unresolved by that bound.

Now suppose the two readings each have absolute error at most epsilon kilograms while the retention law is fixed. The reconstructed a_0 can err by at most 5*epsilon, and b_0 by at most 6*epsilon. The formula for y_2 has error at most (7/8)*epsilon from those two reading errors: add the absolute contributions (3/4)*epsilon and (1/8)*epsilon. At epsilon = 0.01 kg this gives 0.00875 kg. A marginal threshold decision must account for that interval; a recovered negative mass calls for checking the measurement uncertainty and the model assumptions.

If both substances instead have the same fixed retention factor r, the total obeys y_(n+1) = r*y_n. Composition is then unnecessary for predicting totals under that law. The needed information changes with the operations and the question.

#### A.3.3.PI:5.2 - Preserve predictive memory under a coarse readout

A modeled device has hidden states A, B and C, with fixed transition probabilities:

| Present state | Next A | Next B | Next C |
| --- | --- | --- | --- |
| A | 0.7 | 0.2 | 0.1 |
| B | 0.1 | 0.2 | 0.7 |
| C | 0.2 | 0.3 | 0.5 |

The readout is 0 in A or B and 1 in C. A current 0 leaves next-1 probabilities from 0.1 to 0.7, depending on the hidden state. A single value such as their unweighted mean would add an unsupported assumption about which state is present.

For this calculation, take the initial distribution to be the stationary distribution (19/54,13/54,22/54). After observing 1, the current state is C. Its next-state weights are (0.2,0.3,0.5). Observing 0 next removes C and gives current A/B weights (2/5,3/5). The probability of the following 1 is

    (2/5)*0.1 + (3/5)*0.7 = 23/50 = 0.46.

For the history 0,0, the first 0 gives weights (19/32,13/32,0). Apply the matrix, retain A and B after the next 0, and normalize. Their weights become (73/105,32/105), giving

    (73/105)*0.1 + (32/105)*0.7 = 99/350, about 0.283.

A decision that changes when next-1 probability exceeds 0.4 takes different actions after those histories. Keeping only the latest 0 with the stationary A/B mixture would give 11/32, about 0.344, and lose the relevant difference. The distribution conditioned on history is the useful retained information.

The same matrix also gives a long-run fraction of readout 1 equal to 22/54. This finite positive chain has the conditions for that ergodic average. The average answers an aggregate question; the conditional probabilities answer the next-event question.

Initial weights other than the stationary distribution can give different finite-history predictions. If only a current 0 is known and no mixture is justified, the range [0.1,0.7] remains available. A probabilistic estimate requires its initial and transition account.

#### A.3.3.PI:5.3 - Distinguish a next output from an updatable state

A processor emits and removes the head bit of a pending finite queue once per step. Two possible queues are (0,1) and (0,0). In both cases the next output is 0, so retaining the next bit answers the immediate output question.

After emitting that bit, the next outputs are respectively 1 and 0. The retained next bit cannot update itself without information about the remaining queue. To predict the next two outputs, retain both pending bits. To keep predicting after later steps and arrivals, retain the relevant queue and arrival account, or a summary proved adequate for the selected output question.

The difference is between knowing one output and carrying information that can be updated for further prediction. A description can be economical and sufficient for a short task. Increasing the horizon changes the information it must supply.


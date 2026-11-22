---
chunk_kind: "child"
pattern_id: "A.3.3.TR"
pattern_title: "Construct a Rule for State Change"
section_id: "A.3.3.TR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.TR/A.3.3.TR__006_archetypal-grounding.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "A.3.3.TR — Construct a Rule for State Change"
  - "A.3.3.TR:5 — Archetypal Grounding"
line_start: 13109
line_end: 13170
dependencies:
  - "A.22.CGUS"
  - "A.3.3"
  - "A.3.3.CC"
  - "B.5.FM"
  - "B.5.MPC"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.TR:5 - Archetypal Grounding

#### A.3.3.TR:5.1 - Two correct local increments can lose a global increment

Participants A and B each read an integer counter and later write the saved value plus one. Individual reads and writes are atomic. Each participant reads before it writes. Initially x = 0.

Use the state x, positions pA and pB in the two local procedures, and saved values rA and rB after their reads. Positions 0, 1 and 2 mean before read, after read and finished. Initially pA = pB = 0 and rA = rB = 0; each participant overwrites its saved value before using it.

The four action rules are:

| Action | Enabled when | Changed values | Other values |
| --- | --- | --- | --- |
| ReadA | pA = 0 | rA' = x; pA' = 1 | x, pB and rB retain their values |
| WriteA | pA = 1 | x' = rA + 1; pA' = 2 | rA, pB and rB retain their values |
| ReadB | pB = 0 | rB' = x; pB' = 1 | x, pA and rA retain their values |
| WriteB | pB = 1 | x' = rB + 1; pB' = 2 | rB, pA and rA retain their values |

The next step is any one enabled action. From pA = pB = 0, six complete histories respect the local orders. ReadA, WriteA, ReadB, WriteB and its A/B reversal finish at x = 2. In the other four, both reads precede either write; both saved values are zero, so the final value is one.

The result identifies how interference defeats the intended total. Serializing the two read-and-write pairs or supplying an indivisible increment changes the transition rule and removes these lost-increment histories. If serialization introduces waiting, a claim of eventual completion still needs its scheduling conditions.

The ordering rules already suffice to exhibit failure. If a scheduler chooses uniformly among enabled actions at each step, the two serialized histories each have probability 1/4 and the other four each have probability 1/8; the lost-increment probability is 1/2. Uniform choice among the six complete histories instead gives 2/3. Choose and justify a scheduler model when a likelihood estimate is needed.

#### A.3.3.TR:5.2 - A fixed connection and two force equations determine acceleration

This example compares two commissions for the same pair of carts. One asks for the acceleration of the pair. The other asks what force the connector must carry. Two carts of positive masses m1 and m2 move on an ideal frictionless straight track. A massless rigid connector keeps their positions q1 and q2 at q2 - q1 = L. Signed external forces along the track are F1 and F2. The connector exerts equal and opposite signed forces, written -lambda on cart 1 and +lambda on cart 2.

The positional constraint alone permits many common motions. Differentiating the constant-separation condition gives v2 = v1 and a2 = a1 = a for compatible motion. To predict that motion, draw the boundary around both carts and the connector. The connector forces cancel within it, so the net external force gives the centre-of-mass acceleration `a = (F1 + F2)/(m1 + m2)`. Rigidity makes this the acceleration of each cart.

For the load, draw a boundary around either cart. The respective force balances under the stated sign convention are

    m1*a = F1 - lambda
    m2*a = F2 + lambda

Substituting `a` into either balance gives `lambda = (m2*F1 - m1*F2)/(m1 + m2)`. The split between the external forces matters to this answer even at the same total force.

For m1 = 1 kg, m2 = 3 kg, F1 = 4 N and F2 = 0, the result is a = 1 m/s² and lambda = 3 N. If instead F1 = 0 and F2 = 4 N, the acceleration stays 1 m/s² while lambda becomes −1 N under the same sign convention. Start with q1 = 0, q2 = L and both velocities zero. While the forces remain constant, q1(t) = t²/2 and q2(t) = L + t²/2 in metres when t is in seconds; both velocities are t metres/second.

For changing forces, the whole-pair acceleration depends on the resultant at the time in question. Its time dependence, or a law for it and suitable initial conditions, can determine the motion. For the final velocity alone, the initial velocity and the net impulse over the interval suffice. Divide that impulse by the total mass and add the resulting change in velocity. A bound on the quantity in question can settle a threshold. For the signed connector load, use a component balance as above or other evidence that determines or sufficiently bounds the load. If the connector is elastic or has consequential mass, its constitutive and interaction account changes the rule. Choosing smaller numerical time steps cannot supply that missing physical relation.

For another state-change question, first name the observable the next decision needs. Hold the proposed model’s retained quantities fixed and vary the information it omits within the allowed conditions. Here shifting the same applied force from one cart to the other preserves whole-pair acceleration and changes the connector load. The whole-system balance suffices for the former question. The latter needs a component balance or other grounds establishing the internal force.

#### A.3.3.TR:5.3 - Preserving a value and making progress require different arguments

For nonnegative integers a and b with `a >= b > 0`, use integer division `a = k*b + r`, where k and r are integers and `0 <= r < b`. Take the transition `(a,b) -> (b,r)`. Every common divisor of a and b divides `r = a - k*b`; every common divisor of b and r divides `a = k*b + r`. The integer quotient makes both implications valid. The transition therefore preserves the common divisors and hence the greatest common divisor. At `b = 0`, stop and return a.

From (30,18), the successive states are (18,12), (12,6), (6,0). The terminal result is 6. The second component is a nonnegative integer and decreases at every nonterminal step, establishing termination.

Keep the same inputs and stopping condition. A rule that returns `(a,b)` unchanged whenever `b > 0` preserves every common divisor at every step. From any such input it runs forever. What establishes termination for the Euclidean rule is the decrease of `b` within the nonnegative integers.

This is a transition account for a mathematical construction. An implementation must supply integer operations with the assumed meanings; using a bounded machine representation introduces its own arithmetic conditions.

#### A.3.3.TR:5.4 - A switch changes the law within the prediction interval

Consider a temperature model with T in degrees Celsius and heater mode OFF or ON. While OFF, temperature falls at 1 degree/minute; while ON, it rises at 2 degrees/minute. OFF at T<=18 switches immediately to ON. ON at T>=20 switches immediately to OFF. A switch changes the mode and preserves T.

Start at T=19, OFF. The requested result is temperature and mode at 1.5 minutes. In OFF mode, flow is permitted while T>18. The trajectory T(t)=19-t reaches 18 at minute 1; the event then switches the mode to ON. The new law gives T(t)=18+2\*(t-1) until T reaches 20. At 1.5 minutes the result is **19 degrees, ON**.

At minute 2, the upper-threshold event switches to OFF; the next segment uses T(t)=20-(t-2). This continuation follows from retaining the mode and restarting the evolution after each event.

Keeping the initial OFF law through the whole first interval would give 17.5 degrees. Checking the switch only at the interval's end describes a controller that samples at those times, with different behavior from the supplied immediate-event model. A real controller's sampling or delay therefore belongs in its modeled timing.


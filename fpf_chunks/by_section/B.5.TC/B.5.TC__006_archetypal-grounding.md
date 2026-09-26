---
chunk_kind: "child"
pattern_id: "B.5.TC"
pattern_title: "Compare Theoretical Accounts for a Working Question"
section_id: "B.5.TC:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.TC/B.5.TC__006_archetypal-grounding.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "B.5.TC — Compare Theoretical Accounts for a Working Question"
  - "B.5.TC:5 — Archetypal Grounding"
line_start: 45499
line_end: 45530
dependencies:
  - "B.5.RA"
  - "B.5.RR"
  - "B.5.TU"
  - "C.11.DUA"
  - "C.28"
  - "C.29.1"
  - "C.29.2"
  - "C.29.3"
  - "F.0.2"
keywords:
---

### B.5.TC:5 - Archetypal Grounding

#### B.5.TC:5.1 - Routes, reachability and minimum cost

A mathematical account keeps routes as distinct objects. Routes p and q go from X to Y and cost 1 and 4. A route r goes from Y to Z and costs 2. Routes with matching endpoints can be concatenated; the cost of a concatenation is the sum of its costs. The two routes from X through Y to Z therefore cost 3 and 6.

A second account keeps only whether travel between endpoints is possible. Both X-to-Y routes become the answer “yes”. Joining that answer to Y-to-Z reachability gives “yes” for X-to-Z. This account answers whether travel is possible. It cannot give the cost of the route actually taken: p followed by r and q followed by r have the same reachability summary and different costs.

A third account keeps minimum costs. For finite nonempty sets of allowed first and second segments, assume every first segment can be followed by every second segment and costs add. Then the least combined cost is the sum of the two least costs. Every combined cost is at least that sum, and combining the two minimizing segments attains it. Here the answer is 1 + 2 = 3. The calculation can therefore answer the minimum-cost question without retaining every route. Choosing an actual route also requires the minimizing segments to be recoverable.

Now change the allowed combinations. Let the second segments be r with cost 2 and s with cost 10. Only p followed by s, and q followed by r, are allowed. The true minimum is min(1 + 10, 4 + 2) = 6. Independently minimizing the two stages gives 3, which no allowed route attains. The failure is the omitted compatibility relation. Retain the incoming-route distinction or calculate over the allowed pairs.

The comparison yields three useful accounts with different retained information. Its changed case also identifies a condition for the minimum-cost composition rule. No physical interpretation is needed for this mathematical result. Using cost as travel time or expenditure adds the corresponding interpretation and additivity conditions.

#### B.5.TC:5.2 - The same oscillator, different formulation and computation

Consider an ideal one-dimensional mass on a linear spring, with mass m > 0, spring constant k > 0, displacement q and velocity v. Friction and external forcing are absent. The question is its motion from q(0) = a and v(0) = 0.

The force account gives m q'' = -k q. The variational account uses L(q,v) = m v²/2 - k q²/2. Its Euler-Lagrange equation is d/dt(∂L/∂v) - ∂L/∂q = 0; substitution gives m q'' + k q = 0. Both therefore give q(t) = a cos(√(k/m) t) under these premises. For this motion question, the two constructions agree. The variational formulation can become preferable when another coordinate choice simplifies constraints; the force formulation may be the quicker account for this simple case.

Suppose a computation appears to disagree. Take m = k = a = 1 and use the forward Euler updates q_next = q + h v and v_next = v - h q. From q = 1, v = 0 and h = 0.1, it returns q_next = 1, v_next = -0.1. The energy (q² + v²)/2 rises from 0.5 to 0.505. In fact these updates multiply energy by 1 + h² at each step, whereas the differential equation conserves it.

The discrepancy is produced by the approximation used in the computation. Compare an adequate step size or another numerical method under C.29.2 for the requested horizon and error. If the real oscillator loses energy, examine friction and other physical interactions; that changes the model question. The equality of the two ideal derivations remains available within its premises.

#### B.5.TC:5.3 - Agreement in observation, disagreement under intervention

An indicator X and an output Y always follow a binary controller command U. Two causal hypotheses explain the observed pairs: A uses X := U and Y := X; B uses X := U and Y := U. In A, the indicator drives the output. In B, the controller drives both directly. Both yield X = Y = U in ordinary operation.

The question is now what happens when X is forced to 1 while U remains 0. Represent this intervention by replacing the assignment to X. A gives Y = 1; B gives Y = 0. The same observed pairs leave that difference unresolved.

The next contribution could be the circuit description, an already available intervention result or a worthwhile discriminating test. If the work only predicts the observed indicator from U in unchanged operation, this causal difference need not be settled for that use. If it proposes controlling Y through X, retain the unresolved consequence until the needed causal premise is supplied. C.28 governs that intervention claim.


---
chunk_kind: "child"
pattern_id: "C.29.1"
pattern_title: "Mathematical Result Transfer"
section_id: "C.29.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.1/C.29.1__006_archetypal-grounding.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.29.1 — Mathematical Result Transfer"
  - "C.29.1:5 — Archetypal Grounding"
line_start: 60302
line_end: 60434
dependencies:
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5"
  - "B.5.MPC"
  - "C.29"
keywords:
---

### C.29.1:5 - Archetypal Grounding

The following constructions use stated mathematical models. Their conclusions show what follows from those models and correspondences. Applying them to an actual store, transport arrangement or thermal system also depends on the relevant accounting, compatibility or physical premises.

#### C.29.1:5.1 - Transfer a reservation update to available stock

**Situation and question.** A reservation account stores on-hand quantity n and reserved quantity r. Both are integers, with 0 ≤ r ≤ n. One reservation is allowed when n − r ≥ 1. While this operation is performed, there are no deliveries, shipments or cancellations. The question is whether a smaller display can both decide that operation's availability and calculate its effect.

The source reservation update is:

~~~
U(n,r) = (n,r+1), defined when n−r ≥ 1.
~~~

Start with the proposed display H(n,r) = n, labelled “available.” The allowed states (1,0) and (1,1) have the same display, one. In (1,0), another reservation is allowed; in (1,1), it is not. Thus availability is not a function of H alone. Moreover, a permitted reservation leaves H unchanged, whereas the amount still reservable decreases.

The first result is that the total on hand omits a distinction needed by the reservation question. H remains useful as the on-hand total.

Construct the repaired display F(n,r) = a = n − r. Define its receiving reservation operation by V(a) = a − 1 for integer a ≥ 1. Now compare both orders:

~~~
F(U(n,r)) = F(n,r+1) = n−(r+1)
          = (n−r)−1 = V(F(n,r)).
~~~

The operation conditions also agree: U is defined exactly when F(n,r) ≥ 1, which is the condition for V. After an allowed update, 0 ≤ r + 1 ≤ n and a − 1 ≥ 0, so the result remains inside each account's domain.

For n = 5 and r = 2, the source becomes (5,3), and the display moves from 3 to 2. After k reservations, the same reasoning gives available stock a − k, for integer 0 ≤ k ≤ a. Each intermediate reservation is allowed; the next reservation at k = a is not.

**Returned result.** Available stock is sufficient to decide and update this reservation operation. It does not determine n and r separately: (5,2) and (7,4) both give a = 3. If the next question asks how many items are reserved, retain that distinction. If the next operation is shipment or cancellation, recover its definition and compare it separately. Correct transfer of the reservation equation does not establish that a physical stock count is accurate.

#### C.29.1:5.2 - Separate route cost, minimum cost and a relaxation bound

**Situation and assumptions.** Two routes p and q go from A to B, with costs 1 and 4. A route r goes from B to C, with cost 2. These are the only elementary routes considered, costs add when routes are composed, and initially either p or q may be followed by r. The question is the least cost from A to C.

First examine a coarser, different question: whether A can reach B. Both p and q answer yes. A summary that records only their endpoints can answer this reachability question. It cannot define “the cost of the route” by choosing a representative: choosing p gives 1 and choosing q gives 4.

To answer the least-cost question, construct a different operation. Take the minimum over alternatives, and add the cost of a permitted continuation. In the stated case:

~~~
cost(p followed by r) = 1 + 2 = 3
cost(q followed by r) = 4 + 2 = 6

min(1+2,4+2) = min(1,4)+2 = 3.
~~~

The equality holds because the same continuation is available after both alternatives and adds the same amount. For arbitrary finite costs a and b and common continuation cost c, adding c preserves their order, so min(a+c,b+c) = min(a,b)+c. This explains why the lower-cost prefix can be retained for this continuation. The source witness p followed by r has cost 3.

**Change the compatibility premise.** Now r is allowed only after q; taking p consumes a permission needed for r. The two arrivals at B have the same location but different permitted continuations. The allowed complete route is q followed by r, with cost 6.

The arithmetic min(1,4)+2 = 3 still holds. Its use as the attainable minimum fails because its selected prefix p cannot be followed by r. Equality of locations did not preserve route composition.

Repair the state at B by retaining whether the continuation permission remains. Let p arrive at (B,0) and q at (B,1). Only (B,1) has the r transition to C. Minimizing over the allowed complete routes in this expanded account yields 4 + 2 = 6. Returning q followed by r supplies an allowed source witness.

There is also a useful result from the coarser account. If it deliberately ignores the permission restriction, its feasible route set contains the real feasible routes. Costs of retained routes remain unchanged. Its minimum 3 is therefore a lower bound on the true minimum, here 6. The bound rules out a source route costing at most 2. It cannot establish that a source route costing at most 4 exists; that would need an allowed witness.

**Returned result.** Endpoint reachability, the cost of a selected route and the minimum over compatible routes are different questions. Retain history only insofar as it changes future compatibility or cost. When a coarser account is cheaper to use, its lower bound may still answer the receiving question without constructing the optimal source route.

#### C.29.1:5.3 - Change temperature coordinates, then choose what can be forgotten

**Situation and physical meaning.** Consider two bodies with equal, constant heat capacity C > 0, each represented by one uniform temperature, T₁ or T₂. The bodies exchange heat only with each other. For one chosen sampling interval, stipulate a heat transfer from body 1 to body 2 of Q = αC(T₁ − T₂), with fixed 0 ≤ α ≤ 1/2. Negative Q means transfer in the opposite direction. Temperature differences use kelvins; temperature values below are expressed in degrees Celsius.

This is a supplied discrete model. Equal heat capacities and the opposite heat changes give:

~~~
T₁' = T₁ − Q/C = (1−α)T₁ + αT₂
T₂' = T₂ + Q/C = αT₁ + (1−α)T₂.
~~~

The range of α makes each new temperature a convex combination of the old temperatures, without reversing which body is warmer. The model does not prescribe the continuous temperature history inside an interval.

The working question is whether the warmer body's modeled temperature is at most 60 °C after two intervals. Direct iteration is possible. A coordinate change can also expose which information the answer needs.

Construct the coordinates:

~~~
m = (T₁+T₂)/2
d = (T₁−T₂)/2

T₁ = m+d
T₂ = m−d.
~~~

The inverse recovers both temperatures. Thus (m,d) loses no distinction between admitted temperature pairs. Substitute the source updates and compare:

~~~
m' = (T₁'+T₂')/2 = (T₁+T₂)/2 = m
d' = (T₁'−T₂')/2 = (1−2α)(T₁−T₂)/2 = (1−2α)d.
~~~

The receiving operation preserves the mean and scales the contrast. It is a simpler expression of the same discrete update. Equal heat capacities explain the physical significance of the preserved mean: the two heat changes cancel. The warmer temperature is M = max(T₁,T₂) = m + |d|.

Now consider discarding d and retaining only m. The identity update m' = m is still exact, but the warmer temperature is no longer determined. The states (0,100) and (50,50) both have m = 50. For α = 1/4, the first becomes (25,75), then (37.5,62.5); the second stays at (50,50). They give opposite answers to the 60 °C threshold question after two intervals. Mean preservation alone is insufficient.

For α = 1/4, the contrast halves each interval. Starting from (20,80) gives this trajectory:

| Sampling instant | T₁ in °C | T₂ in °C | m in °C | d in K | M in °C |
|---|---:|---:|---:|---:|---:|
| Initial | 20 | 80 | 50 | −30 | 80 |
| After one interval | 35 | 65 | 50 | −15 | 65 |
| After two intervals | 42.5 | 57.5 | 50 | −7.5 | 57.5 |

**A bound on the contrast suffices after two intervals.** Suppose the individual temperatures are unknown, but m = 50 °C and |d₀| ≤ 30 K are known. Repeatedly applying the receiving update yields dₖ = 2⁻ᵏd₀. Therefore:

~~~
50 °C ≤ Mₖ ≤ 50 °C + 2⁻ᵏ × 30 K.
~~~

Temperature differences are added to a temperature on the same scale. At k = 1 the upper bound is 65 °C, leaving the 60 °C question unresolved. At k = 2 it is 57.5 °C, so every compatible initial pair has warmer temperature at most 60 °C at that sampling instant. No choice of a representative pair is needed.

If an exact maximum is wanted, retaining (m,|d|) is sufficient under this symmetric update. The sign of d is needed only for questions distinguishing which body is warmer. Retain the distinction needed by the question, rather than restoring both coordinates automatically.

**Returned result and return condition.** The bound answers the stated question at the second sampling instant under the supplied model. It does not assert that the bodies were always below 60 °C: the initial pair (20,80) was not. Unequal heat capacities, external heat exchange or a changed transfer rule require a new update and a new comparison. Establishing that this discrete model predicts an actual pair of bodies requires physical and measurement work; B.5.MPC connects that work to the mathematical result.

#### C.29.1:5.4 - Return a rational result from a real-number construction

A calculation accepts positive rational settings x and needs `|x² − 2| ≤ 0.01`. If a rational candidate is already supplied, substituting it can settle this question. The following construction uses an available positive real root of `x² = 2` to obtain a rational candidate.

The inclusion of the rationals in the reals retains their equality, order, addition and multiplication. The larger domain also contains limits of rational sequences that have no rational limit. This supplies new mathematical objects without merging distinct rational inputs. The needed return is still a rational setting satisfying the original inequality.

Compute rational bounds:

~~~text
1.414² = 1.999396 < 2
1.415² = 2.002225 > 2
~~~

Squaring is increasing on the positive reals, so the root lies between those endpoints. Choose the rational setting `x = 1.414` and check the requested result: `|x² − 2| = 0.000604 ≤ 0.01`. The returned setting and its error calculation answer the original question. C.29.2 develops a procedure when obtaining such bounds requires one.

Now change the requirement to a rational setting with `x² = 2`. Suppose `x = p/q` is in lowest terms, with integers p and nonzero q. Then `p² = 2q²`, so p is even. Substituting `p = 2r` shows that q is also even, contradicting lowest terms. The real root therefore has no rational counterpart. Return that obstruction; the requester can retain a tolerance or change the allowed number domain.

The extension supports a useful approximation and an existence argument in the larger domain. Which result can be returned depends on the requested property and the allowed source settings.


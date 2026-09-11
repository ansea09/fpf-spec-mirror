---
chunk_kind: "child"
pattern_id: "B.5"
pattern_title: "Canonical Reasoning Cycle"
section_id: "B.5:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5/B.5__006_archetypal-grounding.md"
commit_sha: "cda9087f48e0bce2c5f9d5f4389e7e025c7678f5"
heading_path:
  - "B.5 — Canonical Reasoning Cycle"
  - "B.5:5 — Archetypal Grounding"
line_start: 41051
line_end: 41138
dependencies:
  - "A.10"
  - "B.5.1"
  - "B.5.2"
  - "B.5.4"
  - "C.29"
keywords:
---

### B.5:5 - Archetypal Grounding

#### B.5:5.1 - A counterexample becomes a constructive mathematical question


An engineer models pairwise incompatibilities with a finite simple undirected graph and asks, “Does connectedness let us divide the vertices into two groups with every edge crossing between groups?”

A triangle is a counterexample: putting the first two adjacent vertices in different groups forces the third to conflict with one of them. This refutes the universal statement but leaves a useful question: **which obstruction prevents such a partition, and can we construct either the partition or a witness of failure?**

Build the tree by keeping an ordered waiting list. The neighbours of a vertex are the vertices joined to it by an edge.

1. Choose any unseen vertex as a root, mark it seen, give it depth 0 and put it on the waiting list.
2. Remove the first waiting vertex. For each of its unseen neighbours, mark that neighbour seen, record the removed vertex as its parent, give it the parent's depth plus 1, and append it to the waiting list. A vertex already seen keeps its first parent and depth.
3. Repeat step 2 until the list is empty. If an unseen vertex remains, start a new root and repeat; this covers disconnected components and isolated vertices.

This is breadth-first search: a discovered vertex waits behind the vertices already waiting. The recorded parent edges form a tree in each component. Assign even-depth vertices to one group and odd-depth vertices to the other. If every graph edge joins opposite parities, these groups give the partition. If an edge joins equal parities, write each endpoint's chain of parents back to the root. Keep the two paths up to their common vertex of greatest depth, discarding the shared part beyond it. The retained paths have an even total length; the extra edge closes a simple odd cycle. An odd cycle cannot alternate between two groups all the way around. Thus the procedure returns either a two-colouring or an odd-cycle witness.

For a worked traversal, take vertices A–F and edges AB, AC, BD, CE, DF and EF. Start at A and inspect neighbours alphabetically. The waiting list changes as follows; the processed vertex is the parent of each newly found vertex in that row.

| Processed vertex | Newly found vertices and depth | Waiting list after processing |
| --- | --- | --- |
| A | B, C at depth 1 | B, C |
| B | D at depth 2 | C, D |
| C | E at depth 2 | D, E |
| D | F at depth 3 | E, F |
| E | None; F was already seen | F |
| F | None | Empty |

A has depth 0, so the groups are {A,D,E} and {B,C,F}; each of the six edges crosses between them. Now add DE. Its endpoints both have depth 2. Their parent paths D–B–A and E–C–A, joined by DE, give the five-edge cycle D–B–A–C–E–D. The added edge therefore prevents the requested two-group partition.

The decisive idea is parity plus a tree-path construction, not the enumeration of many successful examples. The result answers a mathematical question without an empirical test. To use it for allocation, separately establish that vertices represent the relevant items and edges the actual pairwise incompatibilities. If three-way constraints matter, that application question must change.

The concrete practice targets are to explain the obstruction, construct a partition or failure witness for another finite graph, and handle disconnected components. Assess those capabilities on a changed graph with the references and assistance permitted in the intended work.

#### B.5:5.2 - A physical question changes the representation

In a constructed engineering case, a cabinet contains two components. The intended question concerns the hottest component, but a proposed lumped model reports only their arithmetic mean temperature.

Let the modeled component temperatures be T1 and T2, with mean m = (T1 + T2)/2. The states (20,80) and (50,50), in degrees Celsius, both give m = 50. Their maxima are 80 and 50. A stipulated threshold of 60 therefore gives different classifications. On a state set containing both pairs, no function of m alone can recover the maximum or that classification.

A constructive repair retains the signed contrast d = (T1 − T2)/2. Then T1 = m + d, T2 = m − d, and max(T1,T2) = m + |d|. If an independently supported bound |d| ≤ Δ holds for the physical conditions, m + Δ is an upper bound within that model. Otherwise the contrast has to be estimated or measured, or the inference restricted.

The next physical inquiry is concrete: which temperature differences are possible under the actual loading, coupling and time window; how well does one temperature represent each component; and what measurements and error bounds cover the hottest relevant region? Compare a direct measurement, a two-state model and a qualified conservative bound by the evidence each requires and the decision each can support. Use existing adequate physical knowledge before selecting another experiment.

The mathematical argument exposes the lost information. For physical use, justify the two-temperature approximation. A more accurate fit to the same mean cannot settle that lost distinction. The first useful return is the changed quantity and representation question plus the physical premise that would distinguish the continuations.

#### B.5:5.3 - The hypothesis-led route remains short

A service has unexplained latency spikes. B.5.2 supplies a qualified backup-interaction conjecture and serious rivals. Derive an observable contrast between backup and comparison intervals, accounting for traffic and other relevant conditions. If the requisite observations exist, compare them under the domain's inference Method. If they do not, the result can finish as a qualified conjecture and a specified missing test.

A separately qualified operational workaround may already answer the immediate service question. Using it does not require pretending that the causal explanation is established or rerunning a sufficient result through every reasoning contribution.

#### B.5:5.4 - A relaxed problem supports a different use

A planner must choose whole jobs for one worker's four-hour window. At most one A-job is available; it takes three hours and has stipulated value 5. At most two B-jobs are available; each takes two hours and has stipulated value 3. For this constructed problem the values and durations add, and the question is which choice satisfying the stated availability and time limits has greatest value. The reader needs elementary algebra and can enumerate the few integer choices.

Let x and y count A- and B-jobs. The intended constraints are x in {0,1}, y in {0,1,2}, and 3x + 2y <= 4; maximize V = 5x + 3y. An AI-assisted calculation instead allows real x and y with 0 <= x <= 1 and 0 <= y <= 2. It returns x = 1, y = 0.5, V = 6.5.

Recover what that calculation establishes. From the relaxed time constraint, y <= (4 - 3x)/2, so V <= 6 + 0.5x <= 6.5. The returned real-valued pair attains this bound. This is an optimum of the relaxation. The proposed half B-job is excluded by the intended whole-job condition.

For the whole-job question, x = 0 permits at most y = 2 and value 6. With x = 1, the remaining hour permits y = 0 and value 5. Two B-jobs therefore attain the integer optimum 6. The human or tool doing this reasoning can check both feasibility and the comparison directly.

The relaxation still answers a useful question: can any permitted whole-job choice reach value 7? Every integer choice is also feasible for the relaxation, whose proved upper bound is 6.5, so the answer is no. Choosing a realizable assignment needs the integer result; ruling out value 7 needs only the upper bound. With five hours instead, the same argument gives V <= 7.5 + 0.5x <= 8. The choice x = 1, y = 1 attains value 8 in both formulations. The planner can use that relaxed optimum as the whole-job answer because this returned choice satisfies the integer conditions.

Here the human–AI division follows the contribution being sought. A planner can use assisted optimization while being able to state what counts as a whole job, recover the constraints actually solved, and distinguish an attainable choice from an upper bound. If the required work is to develop the optimization Method, its construction and proof become additional capability targets. An exercise can change the time window or divisibility condition and ask the learner to choose the formulation and explain which result answers the question.

#### B.5:5.5 - Understand which composition a theory permits

A practitioner wants one input to feed two operations. Let `X`, `Y` and `Z` be distinct atomic types, with available operations `f: X → Y` and `g: X → Z`. A cartesian account supplies copying, `Δ_X(x) = (x,x)`. The composite `(f × g) ∘ Δ_X` returns `(f(x),g(x))` from one input.

Compare an account generated only by `f`, `g`, identities, serial composition, tensoring and exchange of factors. Here `f ⊗ g` runs the two operations on separately supplied inputs, `X ⊗ X`. Every permitted generator preserves the number of atomic factors; composition and tensoring preserve that property. Therefore those operations cannot construct `X → Y ⊗ Z`. The missing contribution is a second input or an additional copying operation.

The receiving work determines whether copying its input is admissible. The comparison exposes that requirement before selecting an implementation. [Baez and Stay, §2.3](https://arxiv.org/pdf/0903.0340), supplies the cartesian/monoidal distinction; the generated-operation case above makes its use explicit.

#### B.5:5.6 - Choose a first physical model before commissioning a calculation

An engineer is asked whether a stronger external fan can bring an overheating component below 65 °C. In this constructed case, inspection finds the component attached to a metal case through a pad; the fan blows over the outside of the case.

Begin by tracing where heat is generated and how it could leave. The pad suggests a path from component to case, followed by transfer to the surrounding air. Keep the component, the case at the attachment and the air distinguishable: they can have different temperatures, and the proposed fan change acts at the case–air part of that path. Treating the whole device as one temperature would hide the difference relevant to this decision.

Try a steady heat-transfer account first. Assume constant component heating and approximate all generated heat as passing through the pad to the case, with an unchanged linear conductance along that path. The physical premise is that, for a fixed conductance, carrying the same heat per second requires the same temperature difference. [OpenStax, University Physics volume 2, §1.6, equation 1.9](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer) explains that relation for a uniform conducting layer. Approximating this assembly by such a path is the engineer's model choice; inspect bypass paths and contact behavior when assessing it.

Model the case as losing heat only to that air through temperature-driven transfer. At equal case and air temperatures this outward transfer is zero, so a steady case receiving positive heat must remain warmer than the air. The fan increases exchange with the air; air temperature is the ideal lower limit for the case in this model. The same [OpenStax section, introduction and “Convection”](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer) explains the temperature-difference dependence and fan-driven exchange.

Suppose the steady readings are 80 °C at the component, 25 °C at the case attachment and 20 °C in the surrounding air. Take these values as exact for the first conditional calculation. The component–case difference is 55 °C. Under the proposed model it remains 55 °C when only external cooling changes. Even ideal cooling of the case to the 20 °C air therefore leaves the component at 75 °C. Improving only this part of the heat path cannot meet the 65 °C target under those assumptions.

This result redirects the design question toward the component–case path, a new direct heat path or reduced heating. It also identifies what could invalidate the estimate: direct airflow onto the component changes the assumed path, while temperature-dependent heating or conductance changes the fixed-difference argument. For the real device, check measurement uncertainty and those assumptions before relying on the bound. A useful specialist request is now: 'Given this assembly and load, can the component stay below 65 °C after improving its contact to the case; which additional observations would settle that?' The engineer can request that model and calculation without first specifying its equations.


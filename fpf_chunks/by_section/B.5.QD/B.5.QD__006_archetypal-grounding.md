---
chunk_kind: "child"
pattern_id: "B.5.QD"
pattern_title: "Develop a New Question from a Result or Construction"
section_id: "B.5.QD:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.QD/B.5.QD__006_archetypal-grounding.md"
commit_sha: "f965ffb27d69ec5e4ae94f1bb0092c15fa13c991"
heading_path:
  - "B.5.QD — Develop a New Question from a Result or Construction"
  - "B.5.QD:5 — Archetypal Grounding"
line_start: 44504
line_end: 44543
dependencies:
  - "B.5.MPC"
  - "B.5.RA"
  - "B.5.RR"
  - "C.11.DUA"
  - "C.39"
  - "C.40"
  - "E.10.INT"
keywords:
---

### B.5.QD:5 - Archetypal Grounding

#### B.5.QD:5.1 - From a false graph claim to a construction or obstruction

An engineer represents pairwise incompatibilities by a finite simple undirected graph. The proposed claim is that connectedness suffices to divide the vertices into two groups so every edge crosses between groups.

A triangle refutes the claim. Assign A to the first group and its neighbour B to the second. The third vertex C is adjacent to both, so neither group is available. The failure concerns the universal claim, not the ability to divide any graph: a four-vertex cycle A-B-C-D-A admits groups {A,C} and {B,D}.

Follow the failed operation. Along a path, successive vertices can alternate between the two groups. Returning around an odd cycle forces its final edge to join vertices assigned to the same group. That identifies an obstruction worth seeking.

The next question is: **For a given finite simple undirected graph, can we construct the division or return an odd cycle that explains why it is impossible?** The answer form now serves both allocation and diagnosis.

B.5:5.1 supplies the broader construction. Traverse each component by breadth-first search and assign groups by even or odd depth. If every edge joins opposite parities, the assignment works. An edge joining equal parities combines with the two parent paths up to their last shared vertex to give a simple odd cycle. The construction therefore answers the new question for the stated graph class.

The earlier connectedness requirement can be dropped: work through each component, including isolated vertices. For a real allocation, establish that the graph represents the relevant pairwise incompatibilities. Three-way constraints would change that application question.

#### B.5.QD:5.2 - From a position to a sufficient state or useful bound

A model describes a point moving along one line in an inertial frame. During the next two seconds there is no net force; use the classical relation q(t) = q(0) + v(0)t. The supplied position is q(0) = 0. Someone asks where the point will be two seconds later.

Construct two cases allowed by this description. With v(0) = +1 metre per second, q(2) = +2 metres. With v(0) = -1 metre per second, q(2) = -2 metres. Position alone leaves the requested answer undetermined.

One next question is **what information completes the state for this prediction?** Under this model, initial velocity together with position suffices. Obtaining velocity could use an already available displacement over a known interval of constant velocity. A.3.3 and C.16 develop state and measurement when those contributions are needed.

Another question is cheaper if the current decision only asks whether the point stays within three metres of its starting position for the next two seconds. Suppose the available information bounds the initial velocity between -1 and +1 metre per second. Then the displacement magnitude is at most (1 metre per second)t throughout that interval, so the point stays within two metres. The bound answers the decision without acquiring a more specific velocity.

The two questions support different uses. If an actuator must meet the point at a specified position, the bound can be insufficient and the state question becomes useful. If the net force becomes nonzero during the interval, revise the model and its prediction. The construction of the question has located the relevant missing contribution in each case.

#### B.5.QD:5.3 - A successful cumulative computation opens an interval question

A program can construct cumulative totals for an integer array a. It starts with S[0] = 0 and sets S[i+1] = S[i] + a[i]. For a = [2,-1,3,4], the result is S = [0,2,1,4,8].

The original task needed the total 8. Recovering the operation reveals that each S[i] already gives the sum before position i. This opens the question: **Can we answer many interval-sum queries from the same cumulative totals?**

Specify an interval by indices l and r, with 0 ≤ l ≤ r ≤ n; it includes l and ends just before r. Splitting the first r elements at l gives S[r] = S[l] + sum(a[l],...,a[r-1]). Hence the interval sum is S[r] - S[l]. For the last two elements, l = 2 and r = 4, so the answer is 8 - 1 = 7. For l = r the answer is 0.

This is a general derivation under integer arithmetic with enough capacity to avoid overflow. Each query uses two stored totals and one subtraction after the array has been prepared. Whether preparation is worthwhile depends on how many queries and changes the application requires.

If a[i] changes by d, every S[j] with j > i changes by d. Frequent changes therefore open a further question: which data organization supports the required mixture of updates and interval queries? That question can be developed when the workload makes it relevant. The successful cumulative operation already answers the unchanged-array question.


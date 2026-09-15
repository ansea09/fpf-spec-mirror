---
chunk_kind: "child"
pattern_id: "C.16.IR"
pattern_title: "Determine What an Indication Can Resolve"
section_id: "C.16.IR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.IR/C.16.IR__005_solution.md"
commit_sha: "98777b284b6a41fa3481a1230a16182d0f323c2a"
heading_path:
  - "C.16.IR — Determine What an Indication Can Resolve"
  - "C.16.IR:4 — Solution"
line_start: 52907
line_end: 52973
dependencies:
  - "A.3.3.PI"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.16.MR"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### C.16.IR:4 - Solution

Construct the cases compatible with the indication and relevant conditions. Obtain the sought values represented by those cases, retaining the distinction between feasible examples and bounds that contain all solutions. Use that result to answer the current question.

#### C.16.IR:4.1 - Fix the sought distinction and available relation

State the quantity or property being sought, its subject and conditions, and the question that depends on it. Distinguish the state before measurement, the state during interaction and the reported indication when they differ. For the voltmeter case in :5.1, the target is open-circuit source voltage, while the reading is the voltage with the instrument connected.

Recover the relation used to interpret the indication, including the domain of each unknown, relevant calibration, influences and error assumptions. Keep a known input as known and an unknown influence as a variable. Derive a missing contribution with C.16.MR before treating it as part of the available relation.

A domain restriction needs its subject meaning. Positive length, a known rotation range and a passive resistance bound can exclude mathematical solutions when those conditions hold. An inconvenient branch is a reason to inspect the model, not a reason to drop that branch.

State whether the receiving question needs a point value, an interval, a threshold decision or a comparison. This selects which remaining differences matter.

#### C.16.IR:4.2 - Construct the jointly compatible cases

Substitute the obtained indication into the relation. Combine that condition with the admitted domains and available information about influences. For repeated or multiple readings, state which subject values and parameters are shared and which may change between them.

With bounded error, include the unknown error in its stated range. If a relation gives an ideal indication f(x,z), x is the sought value, z contains influential unknowns and r is the reported reading, a common model is:

`r = f(x,z) + e, with e in the supplied error range.`

Use that equation only when additive error describes the actual indication convention. An error before clipping, an error after clipping and a missed event can require different relations.

A compact mathematical expression for the compatible sought values is:

`S(r) = {x : there exist admitted z and e for which r = f(x,z) + e}.`

An implicit relation can be used in the same way without converting it to a single-valued function. Retain dependencies among unknowns: independently combining their separate ranges can introduce cases excluded by their joint relation.

A probability model supplies a different additional contribution. Values inside a bounded-error range have no assigned likelihood merely from membership in that range. A confidence interval or posterior distribution requires its corresponding statistical method and assumptions.

#### C.16.IR:4.3 - Obtain values or bounds without losing alternatives

Choose the lightest adequate computation. Solve a small equation, eliminate an influential variable, enumerate a finite domain, or obtain a bound. A numerical formulation can use C.29.2 when its construction is nontrivial.

During elimination, preserve the conditions of each operation. Dividing by an unknown expression can discard its zero case. Squaring an equation can admit additional roots. Test the retained cases in the original relation and domains. Finding one root establishes a possible case; uniqueness requires an argument covering the admitted domain or a sufficient justified restriction.

For several unknowns, obtain the sought value from each compatible joint case. The other unknowns can remain unresolved when every compatible case gives the same sought answer. Section :5.1 gives a source voltage determined while its internal resistance remains unknown.

When a complete solution is costly, distinguish two useful computational results:

- A **feasible example** is one case that satisfies the original relations and conditions. Two such cases can establish a consequential ambiguity.
- An **outer bound** contains every compatible sought value but can also contain values that no case realizes. If the whole bound satisfies an inequality, that inequality holds for every compatible value. A bound spanning both sides of a threshold alone does not establish that both outcomes are possible.

For example, let an ideal indication obey r = x² with x ≥ 0, and let r = 9. A computation that has retained only the outer bound 0 ≤ x ≤ 4 leaves values on both sides of the threshold x = 2. The original relation, however, admits only x = 3. Thus x > 2 is resolved, and no feasible witness with x ≤ 2 exists. The coarse bound left the calculation unfinished; it did not establish ambiguity in the indication.

Use a validated enclosure method when the conclusion depends on retaining every solution through numerical calculation. Ordinary sampling can discover a counterexample but can miss another branch. When computation has not established existence, completeness or a needed bound, retain that limitation in the answer instead of interpreting solver termination as the missing result.

#### C.16.IR:4.4 - Test what is resolved for the receiving question

For a point-value question, test whether all compatible cases agree on that value. For a threshold or other condition, test whether it holds throughout the compatible set or a sufficient outer bound. Establish that the premises admit a case before using such a bound as the interpretation of a measurement; substitution of an available feasible case may suffice.

If the question remains unresolved, construct two compatible cases with different answers. Check both against all readings, shared parameters and domain conditions. These witnesses identify what an additional relation or observation would have to distinguish.

Separate a proved empty compatible set from a search that has not found a case. An empty set shows that the combined readings, model and conditions are inconsistent. Locate a consequential conflict; the cause may be a recording error, a changed subject, an unsuitable error bound or an inadequate measurement relation. A failed search instead limits the computational result.

A point result under ideal data can broaden when input uncertainty is restored. Recompute the relevant range when a reading, calibration coefficient or domain changes. Numerical sensitivity and branch ambiguity can require different remedies.

#### C.16.IR:4.5 - Choose the useful return

Return the value, range or comparison with the conditions that support it. Stop when it is sufficient for the intended use. A lower bound can be more useful than an unnecessarily precise estimate.

For an unresolved decision, use the differing cases to choose a potentially useful next contribution: an available second reading, a different operating range, a better bound, a changed instrument or a narrower conclusion. Examine what that contribution could distinguish before obtaining it. In :5.3, another counter using a different modulus distinguishes alternatives that repeating the same remainder preserves.

Use C.11.DUA when the value and effort of reducing the ambiguity need comparison. It can be reasonable to act with the remaining uncertainty or leave the question unresolved. B.5.MPC.R coordinates a needed revision across the physical, mathematical and computational contributions.


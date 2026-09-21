---
chunk_kind: "child"
pattern_id: "C.29.BB"
pattern_title: "Construct a Balance across a Boundary"
section_id: "C.29.BB:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.BB/C.29.BB__005_solution.md"
commit_sha: "453144eda2870a14d47fd9c066deeb0405eee86f"
heading_path:
  - "C.29.BB — Construct a Balance across a Boundary"
  - "C.29.BB:4 — Solution"
line_start: 65047
line_end: 65114
dependencies:
  - "A.3.3.TR"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
  - "E.18.2"
keywords:
---

### C.29.BB:4 - Solution

Choose the quantity and boundary, account for changes in each included part, and combine only matching transfers. Use the resulting balance to answer the question at the needed resolution.

#### C.29.BB:4.1 - Choose an additive quantity and a common interval

Name the quantity Q, its unit or counting rule, the included parts S, and the start and end conditions. Define who or what belongs to each part. Use disjoint parts, or otherwise account for their overlap before summing.

For disjoint parts with amounts q_i, additivity means that Q(S) = sum q_i. The rule needs a basis in the selected model or counting definition. For a population, assigning each included job to one stage can provide it. For physical storage, use the appropriate physical quantity and law.

An average temperature is not an additive heat store. If the question concerns stored thermal energy, construct that quantity from the material and state relations; if it concerns the maximum temperature, preserve the local temperatures needed to obtain the maximum. Choosing a convenient sum changes the question unless the required result can be recovered from it.

Keep all amounts on the same interval. A transfer that leaves one store before the endpoint but reaches another afterward requires an in-transit store or separate boundary crossings. For snapshots at different times, first recover their relation to the requested interval.

#### C.29.BB:4.2 - Identify transfers and internal production or removal

For each included part, distinguish the amount crossing into it, the amount crossing out, and the change created or removed within it under the chosen quantity definition.

Orient each transfer once. When a transfer from part i to part j removes amount f from i and adds the same amount to j over the common interval, use -f and +f in their accounts. If a connector stores some of the quantity, its incoming and outgoing amounts can differ; represent that store or retain both crossings.

Production and removal depend on the quantity. A reaction can change the amount of one chemical species within a vessel. Completing a job removes it from the population of unfinished jobs. Determine those terms from the relevant physical or counting rule. Assign each contribution once: classify completion as a crossing out of the population or as removal under its counting rule, and use that convention throughout.

Do not set an unobserved term to zero merely because the first diagram omitted it. Use a supplied law, a justified approximation, a bound, or an unresolved term according to what the answer needs.

#### C.29.BB:4.3 - Combine the local balances

Write each included part's change using the selected terms. Sum those equations. Matching internal transfers cancel, leaving

    Q(S, t1) - Q(S, t0)
        = total inward transfer - total outward transfer
          + internal production - internal removal.

The transfer terms are amounts over the interval. A rate must be integrated over that interval, or multiplied by its duration when the rate is constant. The signs follow the chosen boundary.

For a differentiable rate model, the corresponding instantaneous relation is

    dQ(S,t)/dt = inward rate - outward rate + production rate - removal rate.

Use the finite-interval form for discrete events or when a rate description adds no help. If the selected boundary moves, count crossings relative to that moving boundary using the appropriate transport relation.

A closed boundary eliminates crossing terms only when the model excludes those exchanges. Constancy of Q additionally requires net internal production and removal to cancel. Preserve that premise in any conservation conclusion.

#### C.29.BB:4.4 - Redraw the boundary by reclassifying the same exchanges

When enlarging S, include the added stores and their changes. Transfers between the old and added parts become internal only if both sides now refer to the same amount over the interval. The new exterior crossings remain.

When shrinking S, formerly internal transfers can become inputs or outputs. Recompute the requested total from the retained stores. A balance for a larger region supplies its total; obtaining a smaller region's value still needs the removed region's amount or a sufficient bound.

Check the two descriptions against each other: the larger total equals the sum of its disjoint parts, and their changes agree after shared transfers cancel. This comparison can expose an omitted connecting store without resolving every internal rate.

Changing the parts over time can also change membership. Include that effect through boundary crossings or a suitable population rule; keep it visible when comparing successive totals.

#### C.29.BB:4.5 - Use uncertainty or discrepancy to choose the next move

Substitute the available amounts and compute the requested consequence. If some terms are bounded, propagate the bounds through the signed sum. Preserve dependencies when independently combining endpoints would admit impossible combinations.

For observed values, define the discrepancy as observed change minus the change predicted by the included terms. A nonzero discrepancy establishes disagreement between those accounts. Its cause can lie in an omitted store or transfer, incompatible timing or units, a faulty observation, or an inadequate law. Use the working situation to choose a discriminating next observation or model change.

Resolve a remaining term only when it can change the answer enough to justify the work. A supported bound that settles the current decision is already a usable result. An unresolved cause can remain open when the decision tolerates the resulting uncertainty.

#### C.29.BB:4.6 - Preserve the balance in a computation and return its result

When implementing a partitioned calculation, represent a shared transfer consistently on both sides. Use the same orientation, interval and quantity conversion. Recover total amounts with the appropriate cell volumes or population weights before comparing them.

Derive the aggregate change from the proposed updates. If a numerical approximation changes the balance, determine whether the discrepancy fits the receiving use or repair the update. Balance preservation addresses one property of the computation; accuracy of the local solution requires its own approximation argument.

Return the total, bound or identified missing contribution with the quantity, boundary and assumptions needed to use it. A subsequent question about a local maximum, delay or possible action may require the retained component account. Keep that account available rather than treating the total as a substitute for every question.


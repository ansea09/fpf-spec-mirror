---
chunk_kind: "child"
pattern_id: "C.29.BB"
pattern_title: "Construct a Balance across a Boundary"
section_id: "C.29.BB:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.BB/C.29.BB__005_solution.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "C.29.BB — Construct a Balance across a Boundary"
  - "C.29.BB:4 — Solution"
line_start: 74595
line_end: 74662
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

Start from where and when the recipient needs the result. Identify what would count there and which things belong to that total. Choose the quantity Q, its unit or counting rule and the interval. When the boundary is yours to choose, try treating a consequential exchange as an internal transfer by including both sides. Can you then recover the requested total from the larger amount and what was added? At a smaller boundary, net transfers and internal production or removal can establish the change in stock. To obtain an ending stock from that change, also establish the starting stock or a sufficient bound. An observation of the ending stock can settle the question directly. Choose the boundary whose terms and return to the requested quantity can be established. Let S consist of disjoint included parts, or account for overlap before summing.

For disjoint parts with amounts q_i, additivity means that Q(S) = sum q_i. The rule needs a basis in the model or counting definition. For a population, assigning each included job to one stage can provide it. For physical storage, use the physical quantity and law.

For stored thermal energy, construct an additive quantity from the material and state relations. A question about the maximum temperature needs a measured maximum, the local temperatures or another relation from which that maximum follows. If the question asks only whether a temperature limit holds everywhere, a suitable upper bound can suffice. Use a sum when its relation to the requested result supports the inference.

Keep all amounts on the same interval. A transfer that leaves one store before the endpoint but reaches another afterward requires an in-transit store or separate boundary crossings. For snapshots at different times, first recover their relation to the requested interval.

#### C.29.BB:4.2 - Identify transfers and internal production or removal

For each included part, distinguish the amount crossing into it, the amount crossing out, and the change created or removed within it under the quantity definition.

Orient each transfer once. When a transfer from part i to part j removes amount f from i and adds the same amount to j over the common interval, use -f and +f in their accounts. If a connector stores some of the quantity, its incoming and outgoing amounts can differ; represent that store or retain both crossings.

Production and removal depend on the quantity. A reaction can change the amount of one chemical species within a vessel. Completing a job removes it from the population of unfinished jobs. Determine those terms from the physical or counting rule. Assign each contribution once: classify completion as a crossing out of the population or as removal under its counting rule, and use that convention throughout.

Do not set an unobserved term to zero merely because the first diagram omitted it. Use a supplied law, a justified approximation, a bound, or an unresolved term according to what the answer needs.

#### C.29.BB:4.3 - Combine the local balances

Write each included part's change using the terms. Sum those equations. Matching internal transfers cancel, leaving

    Q(S, t1) - Q(S, t0)
        = total inward transfer - total outward transfer
          + internal production - internal removal.

The transfer terms are amounts over the interval. A rate must be integrated over that interval, or multiplied by its duration when the rate is constant. The signs follow the boundary.

For a differentiable rate model, the corresponding instantaneous relation is

    dQ(S,t)/dt = inward rate - outward rate + production rate - removal rate.

Use the finite-interval form for discrete events or when a rate description adds no help. If the boundary moves, count crossings relative to that moving boundary using the transport relation.

A closed boundary eliminates crossing terms only when the model excludes those exchanges. Constancy of Q additionally requires net internal production and removal to cancel. Preserve that premise in any conservation conclusion.

#### C.29.BB:4.4 - Redraw the boundary by reclassifying the same exchanges

When enlarging S, include the added stores and their changes. Transfers between the old and added parts become internal only if both sides now refer to the same amount over the interval. The new exterior crossings remain.

When shrinking S, formerly internal transfers can become inputs or outputs. A direct balance around the smaller region uses those crossings. To recover its amount by subtraction, use the larger total and the amount in the removed region at the same time under compatible counting conventions. A direct reading or a justified bound can also settle what the recipient asks.

Check the two descriptions against each other: the larger total equals the sum of its disjoint parts, and their changes agree after shared transfers cancel. This comparison can expose an omitted connecting store without resolving every internal rate.

Changing the parts over time can also change membership. Include that effect through boundary crossings or a population rule; keep it visible when comparing successive totals.

#### C.29.BB:4.5 - Use uncertainty or discrepancy to choose the next move

Substitute the available amounts and compute the requested consequence. If some terms are bounded, propagate the bounds through the signed sum. Combining separate extremes can give an outer bound even when those extremes cannot occur together. Use it when it settles the requested threshold. For an attainable value or a guarantee that the outer bound leaves open, use the jointly allowed transfers and stores. A permitted case can refute the guarantee.

For observations, subtract the change predicted by the recorded transfers and internal terms from the observed change in storage. Propagate their uncertainties and shared constraints into a range for this discrepancy. If the range excludes zero, the records and balance cannot agree under those assumptions. If it contains zero, establish whether jointly admissible values actually give zero before claiming agreement is possible. Equal unrecorded inflow and outflow can cancel even when the discrepancy is exactly zero. To locate a fault, examine a term or an independent observation that could distinguish its possible causes.

Resolve a remaining term only when it can change the answer enough to justify the work. A bound that settles the decision is a usable result. An unresolved cause can remain open when the decision tolerates the resulting uncertainty.

#### C.29.BB:4.6 - Preserve the balance in a computation and return its result

When implementing a partitioned calculation, represent a shared transfer consistently on both sides. Use the same orientation, interval and quantity conversion. Recover total amounts with the cell volumes or population weights before comparing them.

Derive the aggregate change from the proposed updates. If a numerical approximation changes the balance, determine whether the discrepancy fits the receiving use or repair the update. Balance preservation addresses one property of the computation; accuracy of the local solution requires its own approximation argument.

Return the total, bound or identified missing contribution with the quantity, boundary and assumptions needed to use it. For a further question about a local maximum, delay or available action, retain or recover the component information or other grounds that the new question requires. A direct law or bound can already settle it.


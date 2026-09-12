---
chunk_kind: "child"
pattern_id: "C.29.1"
pattern_title: "Mathematical Result Transfer"
section_id: "C.29.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.1/C.29.1__005_solution.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.29.1 — Mathematical Result Transfer"
  - "C.29.1:4 — Solution"
line_start: 60165
line_end: 60301
dependencies:
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5"
  - "B.5.MPC"
  - "C.29"
keywords:
---

### C.29.1:4 - Solution

**Recover the intended conclusion and its source → construct the correspondence → compare the relevant operations and their conditions → determine what merged cases can still answer → derive the exact or bounded consequence → return it, or repair the particular lost connection.**

The arrows show dependencies. An existing map or proof can supply several steps. A counterexample can send the work back to the choice of representation. A sufficient bound can end the inquiry before an exact answer is constructed.

#### C.29.1:4.1 - Recover the result and the direction in which it will be used

Start with the receiving question. Say what is to be determined and what difference the answer makes: whether another reservation is allowed, the cost of a chosen route, the least possible route cost, or a temperature bound at a specified time. These questions can concern the same objects and require different retained information.

Recover the source result together with the ingredients that produced it:

- the allowed inputs and the meaning of their quantities;
- the operations or relations used in the inference;
- the premises and operation conditions on which the conclusion depends.

Use an existing derivation when these ingredients are available. If an explanation gives only a final formula, recover the missing construction or argument through B.5:4.2 and B.5:4.3. The transfer comparison begins once the required source step is clear enough to reproduce.

Then name the direction of use. There are several common possibilities.

| Intended use | Correspondence to establish |
|---|---|
| Represent a source result in another account | Source inputs and steps have receiving counterparts, with the needed conclusion preserved. |
| Calculate in another account and answer about a source input | The receiving calculation, applied to that input's representation, returns the sought source quantity or a justified bound on it. |
| Choose a receiving solution and carry it back as an action | The selected receiving solution has an allowed source counterpart, and the returned counterpart has the claimed properties. |
| Transfer a theorem to an entire receiving domain | The theorem's premises and inference steps survive, and the domain claimed in the conclusion is covered. |

The last two uses are stronger than merely mapping source cases forward. Keeping the direction explicit prevents an answer about a relaxed problem from becoming an unsupported action recommendation.

#### C.29.1:4.2 - Construct the correspondence from the required distinctions

Choose a source domain X and a receiving domain Y. Construct a map F from the allowed source cases to their receiving representations. Explain its action in the working terms before relying on its notation: F(n,r) = n − r retains available stock and forgets the separate totals; a route endpoint summary forgets which route was taken.

A correspondence can use several maps. An operation may take one kind of input and return another, so its input map and output map can differ. For an operation with several inputs, say how each input is mapped and which combinations are permitted. Where the intended account relates one case to several possible representations, use that relation explicitly. Selecting one representation for each source case defines another construction; establish that the selection supports the intended conclusion.

Construct the correspondence by asking what the receiving question needs. Identify a candidate variable, relation or operation that carries that information. Compute its value on source cases. Determine which cases it combines. Try to express the receiving operation using only what remains. If the expression still depends on an omitted quantity, either retain that quantity or establish why it cancels for this use.

For a change of coordinates, construct the inverse when returning a complete source state is intended. For a summary, identify the source cases compatible with each receiving value. A many-to-one map can answer a particular question exactly even though it cannot reconstruct the whole source state.

Keep the domain visible. A division requires a nonzero denominator; a square-root substitution may impose a sign choice; a route may exist only for certain endpoints or histories. A map justified on one part of X supports conclusions on that part. A receiving value outside F(X), the set of represented source cases, needs a further argument before it is used as a source possibility.

The first result of this step is a usable correspondence with an explained meaning. It may be a formula, a small table, a diagram, or an already defined mathematical map. Its form follows the work.

#### C.29.1:4.3 - Compare performing and representing in both orders

For a source operation U and a proposed receiving operation V, carry out two constructions on the same allowed input:

1. Perform U in the source account, then represent its output.
2. Represent the source input, then perform V in the receiving account.

With input map F and output map G, the exact comparison is:

~~~
G(U(x)) = V(F(x)).
~~~

Read this as an equality of the outcomes relevant to the question. The letters can denote numbers, states, paths or other mathematical objects. For a state update with the same representation before and after, G is F. Use different maps when input and output representations differ.

Derive the equality from the definitions or use an applicable preservation theorem. Numerical examples can discover an error or make the relation understandable. For a general claim, establish the comparison throughout its declared domain. Exhaustive enumeration can establish a claim about a specified finite domain when every permitted case has been included.

Also compare where each operation is available. For a forward representation of a source operation, every source step used by the claim has a defined receiving counterpart. If the receiving account is to decide whether a particular source step is allowed, its answer agrees with the source condition for the represented case. If a receiving action is to be returned to the source, construct an allowed source action with the required outcome.

An equality on inputs where both sides happen to be defined leaves those availability questions open. This matters in reservations and in routes with restricted continuations.

For a sequence of operations, follow the intermediate representations. If each step has the required correspondence and passes an allowed intermediate result to the next, composing the equalities transfers the sequence. If a later operation depends on a distinction discarded earlier, the stepwise construction exposes where the summary has become insufficient.

An invertible coordinate change offers a constructive route. Given F and its inverse, define the receiving update by V = F ∘ U ∘ F⁻¹ on the represented domain. This definition yields the commuting comparison there. If V was proposed independently, compare it with this expression. A bijection between states alone does not determine whether that proposed update agrees.

#### C.29.1:4.4 - Determine whether a merged representation defines the answer

Suppose the source question has answer q(x), and you want a receiving function g with:

~~~
q(x) = g(F(x)).
~~~

Such a g is well-defined on F(X) exactly when all allowed source cases having the same representation give the same answer:

~~~
F(x₁) = F(x₂)  implies  q(x₁) = q(x₂).
~~~

If g exists, both source answers equal g of the same receiving value. Conversely, if the source answer is the same for every case represented by y, define g(y) to be that common answer. Choosing another representative then changes nothing.

Use this as a construction, not only as a test. First try to rewrite q in terms of the retained variables. If the unwanted variables disappear, derive the resulting g. If they remain, look for two permitted source cases with the same representation and different q values. That pair proves that the requested answer cannot be recovered from that representation alone. One such pair is enough to refute the proposed function. Failure to find a pair is not a proof of independence.

For an update, ask whether cases sharing the current summary have the same required next summary. For a summary that is also to decide availability, compare the operation conditions across those cases. For a prediction after several steps, compare what the permitted continuations can do. The relevant comparison follows the requested result; it does not require preserving every property of the original object.

Distinguish defining a value on a merged class from changing the question. “The cost of this route” requires the chosen route's cost. “The least cost among these routes” deliberately combines several costs by taking a minimum. The second is a new, potentially useful function; it does not make the first independent of its representative.

#### C.29.1:4.5 - Derive the consequence in the strength that survives

Derive the receiving consequence from the comparison.

For an exact calculation, substitute the represented inputs and derive the receiving output. When returning an answer, express it in the quantity originally asked for. For a transported derivation, identify which premises and inference steps are covered. For example, an identity built from compositions of the compared operations gives the corresponding receiving identity on represented inputs. If a proof also uses order, division or an existence premise, establish how that contribution applies in the receiving account. A quantified claim depends on the cases over which it ranges.

A map that combines source cases can erase differences; equality of their images does not establish equality of the original cases. A receiving domain can contain cases outside the map's image; a result proved only for represented cases does not cover those additional cases. Use an inverse, a separate argument, or a narrower conclusion when the receiving claim requires it.

When the exact queried value is not determined, construct the values compatible with the retained information. For a represented value y, these arise from source cases satisfying F(x) = y and the stated premises. Prove a lower bound L(y), an upper bound U(y), or another relation that holds for all those cases. The resulting interval can answer a threshold question even when it cannot identify one value.

For a decision q ≤ b:

- an upper bound U(y) ≤ b establishes the decision for every compatible case;
- a lower bound L(y) > b rules it out for every compatible case;
- a bound spanning b leaves the decision unresolved.

These are consequences of the bound, so retain its domain, units and relevant time or parameter range. A bound for a sampled instant does not by itself answer what happened between samples.

A relaxation offers another useful transfer. Let S be the allowed source solutions, let T be receiving solutions, and suppose every solution in S has an image in T with the same cost. If the receiving account permits additional solutions, minimizing there can give a lower bound on the source minimum. When the minima exist:

~~~
min over T of receiving cost ≤ min over S of source cost.
~~~

The reason is that the receiving search includes a cost-preserving image of every source option. Maximization gives an upper bound under the analogous assumptions. An optimal receiving solution that has no source counterpart still supports the bound; it does not supply a feasible source plan. A returned plan requires an allowed source witness.

Where the comparison is approximate, derive the error relation for the needed operation and propagate it through later steps. For example, if a later scalar operation h satisfies |h(a) − h(b)| ≤ K|a − b|, with K ≥ 0, on the relevant interval, an input error at most ε contributes at most Kε at its output. Any additional error introduced by computing h is added to that contribution. Merely adding the errors of successive steps without accounting for amplification can understate the final error.

#### C.29.1:4.6 - Return a sufficient result or repair the failed correspondence

Return the conclusion together with the assumptions that change its use. A short calculation can contain the complete transfer. When another person or later use needs to recover the reasoning, preserve the source result, correspondence, comparison and conclusion in the smallest adequate form. C.29:4.4 supplies recording options when a receiving use calls for them.

If the comparison fails, use the failure to choose the next construction.

| What the comparison reveals | Useful next move |
|---|---|
| An omitted variable changes the needed answer | Retain that variable, or retain a derived quantity sufficient for the question. |
| The receiving operation admits a step unavailable in the source | Retain its enabling condition, restrict the receiving operation, or use the enlarged problem only for the bound it supports. |
| Two representatives give different values | Change the representation or ask for a class property, such as a minimum or interval, and establish that new property's use. |
| Agreement holds only on part of the domain | State and use that restriction if it includes the intended cases; otherwise seek another correspondence. |
| A missing source premise prevents the comparison | Recover or establish that premise before repairing the receiving calculation. |
| A sound bound is too broad for the decision | Find which retained uncertainty spans the threshold and obtain a discriminating premise or observation. |

After a repair, repeat the affected comparison and the later steps that depend on it. Keep conclusions whose premises and correspondences remain applicable.

Stop when the exact consequence or bound answers the working question. A located failure can also settle the immediate question: “This summary cannot determine availability; retain reserved stock or use available stock.” If the missing contribution is a physical model, a measurement relation, a numerical method or a new proof, name that contribution and return to its practice. B.5.MPC handles the wider coordination when several of those contributions must agree.


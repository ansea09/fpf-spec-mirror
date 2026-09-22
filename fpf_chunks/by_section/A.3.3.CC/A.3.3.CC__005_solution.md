---
chunk_kind: "child"
pattern_id: "A.3.3.CC"
pattern_title: "Construct a Configuration Description under Constraints"
section_id: "A.3.3.CC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.CC/A.3.3.CC__005_solution.md"
commit_sha: "acc387fc7a206495eabe07f1953849217f291715"
heading_path:
  - "A.3.3.CC — Construct a Configuration Description under Constraints"
  - "A.3.3.CC:4 — Solution"
line_start: 9677
line_end: 9738
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5.FM"
  - "B.5.MPC"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.CC:4 - Solution

Construct the description from the working question, then choose a representation in which the needed combinations can be expressed and used. If the calculation becomes inconvenient, reconsider the representation. If a premise changes, revisit the variables and constraints it affects.

#### A.3.3.CC:4.1 - Select the participants and retained differences

State what the reader must find: a fitting arrangement, a compatible assignment, a range of positions or the configurations to which a law will later apply. Identify the participants and the differences that can change this answer.

Give each variable a meaning and a value range. For a physical position, include the reference frame and unit needed to interpret it. For a relation, identify its participants: a distance needs the two endpoints; a job count needs the particular buffer. A.17 and A.18 supply the Characteristic and Scale vocabulary when the variables are declared as FPF characteristics.

Separate quantities held fixed in the present model from variables to be found. A link length may be a parameter in a rigid-body model and a changing quantity in an elastic model. The distinction follows the modeled use, so a later revision can change it.

Ask whether two arrangements described by the same values can require different answers to the current question. If they can, retain the missing distinction. For example, a pair of queue lengths suffices for occupancy but loses the order of differently treated jobs. State the needed order before attempting the receiving calculation.

#### A.3.3.CC:4.2 - Express compatible combinations

Start with the product of the separate value sets. Write the conditions selecting the combinations admitted by the model. In a finite problem this may be a table of allowed tuples. In an algebraic description it may use equalities, inequalities or other predicates.

In A.19 terms, `CS = product_i ValueSet(Scale_i)` is the CharacteristicSpace. A constraint predicate `P` selects a subset `Q = {q in CS : P(q)}` used as the represented configuration set. A point in CS supplies a value for every selected slot; membership in Q additionally satisfies the constraints. The same method can be used in ordinary mathematical notation without creating a separate FPF record.

Explain what each condition represents. Fixed distance, conserved stock, nonpenetration and an imposed operating limit can all constrain the calculation, but changing each condition changes a different premise. Keep a condition imposed by the intended use recognizable so that revising a preference does not appear to alter a physical law.

When time or an external parameter changes which combinations are admitted, make that dependence recoverable, for example `Q(t; p)`. A moving wall changes a position constraint even before its interaction law is known.

Place restrictions on rates, operations or transitions with those relations. The car constraint in :5.4 limits instantaneous velocity; it leaves the corresponding configuration variables available. A.3.3 uses both kinds of restriction when constructing allowed continuations.

#### A.3.3.CC:4.3 - Choose a representation that supports the operation

Compare the following forms using the operation the reader actually needs.

| Form | How to construct and use it | When it becomes inconvenient |
| --- | --- | --- |
| Variables with implicit constraints | Keep the participant values and equations or predicates between them. Test a proposed tuple by substitution. | Finding a satisfying tuple can require solving coupled conditions. |
| Parametrization | Choose parameters u and a reconstruction q = f(u) that satisfies the constraints. Perform the calculation in u and reconstruct the required participant values. | The chosen parameters may cover only part of the admitted set, repeat a configuration or become singular. |
| Explicit finite set | Generate candidate tuples, retain those satisfying the conditions and inspect or compare the resulting set. | The product of value sets can become too large to enumerate. |

For a parametrization, establish the coverage its use needs. If the task claims to represent every admitted configuration, explain how each can be obtained, possibly using several charts or cases. State when two parameter values represent the same configuration. A full turn of an angle repeats an orientation; treating its endpoints as unrelated can break a continuity calculation.

Keep redundant coordinates when they preserve useful structure or avoid a difficult elimination. If the task instead uses a local count of freely variable coordinates, establish independence and regularity of the active equality constraints before subtracting their number. A count alone supplies neither a parametrization nor its global coverage.

When replacing one representation with another, reconstruct the participant values and compare the receiving result. C.29.1 supplies a fuller transfer comparison when the replacement can change an operation or lose information. Group configurations as equivalent only when every member gives the same required answer and the required operations preserve that grouping. This mathematical construction is called a quotient. For an operation on the groups, check that choosing another member of the same group gives an equivalent result. Keep differently labeled endpoints distinct when exchanging them changes the answer.

#### A.3.3.CC:4.4 - Obtain the configuration result the question needs

Apply the description to the receiving question. If one fitting arrangement is enough, finding a satisfying tuple can finish the search. If the question asks for all arrangements, a range or impossibility, supply the corresponding enumeration, argument or solver result.

For a small finite product, generate a tuple, evaluate the conditions and retain it when they hold. A partial assignment can already be rejected when it violates a constraint whose participating values are known. Otherwise it may still have no satisfying completion: local checks leave the remaining constraints to be solved. For a large search, use a suitable constraint-solving Method; the explicit variables, domains and conditions provide its input.

For equations or inequalities, solve them to the extent needed and substitute the result into the retained relations. If numerical computation is used, interpret its tolerance against the modeled condition. A small residual has a different use from a proof of equality or an established margin from a collision boundary.

A configuration rejected by one condition identifies a concrete premise to inspect. An empty admissible set under the chosen premises is also useful: it can return the task to a size, capacity, connection or requirement decision. Failure of an incomplete search to find a tuple leaves the existence question open.

#### A.3.3.CC:4.5 - Carry the result into use and revise it when needed

Return the participant meanings, chosen variables, constraints and interpretation needed to use the result. Keep the representation as small as the receiving operation allows. The equations beside a design or the meanings attached to solver input may already carry everything needed; no additional report is required.

For a later prediction, recover the extra state information and transition rules under A.3.3. A linkage configuration may need velocities; an occupied-buffer configuration may need service or arrival information. An arrangement that fits now gives a starting point for planning, while reaching it from another arrangement needs an allowed-transition account.

When the question or premises change, revisit the affected part. A variable length replaces the fixed-length constraint; arrivals change a stock constraint; a job-order question needs more than counts. B.5.MPC.R coordinates a revision when that change also affects the physical interpretation, calculation or actual execution.

Recognition of the Method's result concerns whether the description expresses the selected configurations and supports the receiving operation. Reliance on its physical accuracy uses the subject premises and whatever calibration or uncertainty account that decision needs. C.11.DUA helps decide whether obtaining further information can change the action enough to justify its cost.


---
chunk_kind: "child"
pattern_id: "C.29.SC"
pattern_title: "Derive a Consequence from a Symmetry"
section_id: "C.29.SC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.SC/C.29.SC__005_solution.md"
commit_sha: "bbfb5347013400e9a895fa4b0f66992e931c0ece"
heading_path:
  - "C.29.SC — Derive a Consequence from a Symmetry"
  - "C.29.SC:4 — Solution"
line_start: 64867
line_end: 64928
dependencies:
  - "A.3.3.TR"
  - "C.29.1"
  - "C.29.2"
  - "C.29.AV"
keywords:
---

### C.29.SC:4 - Solution

**Specify the transformation → follow every relevant condition → transform the answer → derive the consequence → use it within those premises.**

#### C.29.SC:4.1 - Name what must stay the same and what may transform

Recover the problem: admitted candidates, supplied data, conditions, criterion if there is one, and the required kind of answer.

Choose a transformation g and say how it acts on those participants. A permutation can exchange components; a rotation can change coordinates or rotate a physical configuration. Explain which operation is intended. For a symmetry claim, the transformation must be invertible on the relevant domain and retain the stated structure.

Several transformations may form a group: they include doing nothing, composing transformations and undoing each transformation. Name the action on the objects used by the problem. A familiar group name alone leaves that action unspecified.

Keep supplied data in the comparison. If swapping two components also swaps their different costs, the result can be an equivalent problem with transformed data. It is a symmetry of the fixed original problem only if the data required to remain fixed are preserved.

#### C.29.SC:4.2 - Establish the problem-to-solution relation

Apply the transformation to the conditions. Show that an admitted solution is taken to an admitted solution of the stated target problem.

For an optimization problem, check feasibility and the criterion. If g maps the feasible set onto itself and `J(g(x))=J(x)`, it maps every minimizer to a minimizer of that same problem.

For a rule `f:X->Y`, specify the input action g and the corresponding output action r(g). The relation

`f(g(x))=r(g)(f(x))`

is called *equivariance*: transforming the input and then computing agrees with computing and then transforming the output. *Invariance* is the case where the output stays unchanged. Classification of an object and prediction of its position can require these different relations.

For a dynamics law, transform the state, parameters and initial or boundary data. A transformed trajectory may solve the law with transformed data. Establish that correspondence before claiming anything about the solution with the original fixed data.

Use a mathematical argument for the range claimed. A few successful transformations can reveal or test a candidate symmetry; a conclusion covering an entire stated family requires the corresponding preservation argument.

#### C.29.SC:4.3 - Obtain the useful consequence

Follow the consequence needed by the question.

**Transfer a solution.** From a known solution x, obtain g(x) and use the preservation argument from :4.2 to establish what problem it solves. Compositions can generate further related solutions. These are distinct answers only when the transformed objects differ under the problem's equality.

**Restrict a unique solution.** If the fixed problem has exactly one solution x, every symmetry g of that problem must satisfy `g(x)=x`: g(x) is a solution, so uniqueness identifies it with x. Solve this fixed-point condition to restrict or find the candidate.

If uniqueness has not been established, retain the weaker result: symmetries move solutions within the solution set. A symmetric candidate may be worth testing, but the existence of asymmetric solutions remains possible.

**Test a requested deterministic answer.** Suppose an input x is fixed by g and the requested rule must be equivariant. Then `f(x)=r(g)(f(x))`. Check whether any permitted output can satisfy that condition for every transformation fixing x. If none can, the requested deterministic rule cannot answer that input under the stated requirements. The missing distinction or incompatible output requirement is a useful result.

These deductions use preservation and, where stated, uniqueness or equivariance. A conservation law along physical time evolution is a different conclusion. Obtain it from the dynamics or the applicable theorem, including its conditions.

#### C.29.SC:4.4 - Preserve the information needed for use

When symmetry reduces a calculation, state what the reduced answer means in the original problem.

An invariant output can often be calculated from a representative of a symmetry class. An equivariant output may need the transformation used to choose that representative so the answer can be returned to the original coordinates. If several transformations give the same representative, their different output actions must agree on the returned answer, or the result remains ambiguous.

For example, rotating an image to a standard orientation can help classify the object. Reporting a location in the original image additionally requires the corresponding inverse coordinate transformation. If the task distinguishes orientations, the normalization must retain that information.

Use C.29.1 when establishing this representation-and-return relation is itself the difficulty. Use C.29.2 to construct the actual computation; the existence of a symmetric formulation does not supply an efficient algorithm.

#### C.29.SC:4.5 - Return a failed symmetry to its decisive premise

When the comparison in :4.2 fails, identify what changed: an allowed candidate, supplied datum, criterion, output meaning or modeled law. Use that difference to revise the symmetry claim or the problem formulation.

An approximate symmetry can still help, but the allowed discrepancy must be related to the requested result. Establish the bound needed by that use. Small-looking changes are insufficient when they reverse a selection or destroy uniqueness.

After obtaining the consequence, continue with the reduced calculation, transferred solution or revised requirement. Stop when it answers the current question. Add observations or input distinctions only when they can resolve the remaining choice; C.11.DUA supplies the cost-sensitive decision about further work.


---
chunk_kind: "child"
pattern_id: "C.29.2"
pattern_title: "Computational Formulation"
section_id: "C.29.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.2/C.29.2__005_solution.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.2 — Computational Formulation"
  - "C.29.2:4 — Solution"
line_start: 60189
line_end: 60275
dependencies:
  - "A.10"
  - "A.3.1"
  - "A.3.3"
  - "A.6.1"
  - "A.6.3.RT"
  - "B.1.5"
  - "B.1.6"
  - "B.3"
  - "B.5"
  - "C.16"
  - "C.2.1"
  - "C.29.1"
  - "C.29.3"
  - "C.39"
  - "C.40"
keywords:
---

### C.29.2:4 - Solution

Establish how the computation obtains the requested result and why that result has the required meaning. Read the following steps as connected work with returns: an unaffordable state, an unavailable operation or a failed argument can change an earlier choice. Begin with any contribution already available.

#### C.29.2:4.1 - Specify the answer before selecting its representation

State the admitted inputs and the answer the receiver needs. Say whether the result is a value, a witness satisfying a condition, a bound, an approximation or a continuing response to inputs. These are illustrative result forms; choose the one used by the task.

Distinguish the answer condition from the proposed calculation. For a value, ask how it will be obtained. For a witness, ask how candidates will be constructed and tested. For a negative answer, ask what establishes that no admitted witness was missed. A search that eventually finds a witness need not decide the cases in which none exists.

Make an approximation requirement operational. `|y_hat - y| <= epsilon` means an absolute error bound on the requested quantity; relative error uses a different comparison and needs care near zero. A probability guarantee must state what is random and the event whose probability is bounded. Neither a small residual in a different equation nor a favorable average automatically supplies the required result.

For stochastic computation, distinguish a requested distribution, samples from it and an estimated statistic. Those outputs require different constructions and resources. For an approximate distribution, name the events, statistics or distance over which accuracy is required. A distribution's definition does not by itself supply a sampler; a sample average needs an argument connecting it with the requested population quantity.

Identify an input distinction that would change the answer. If two such inputs have the same proposed representation, retain the missing information, add an obtainable input, restrict the admitted cases, or obtain agreement to answer a weaker question. C.29.1 develops the preservation argument when that comparison is itself the difficulty.

#### C.29.2:4.2 - Choose represented state and operations together

Choose data in which the relevant next operation can be expressed. Explain what each stored value means, how an input initializes it, and how a returned value will be interpreted. The same mathematical quantity may be represented by an integer, an interval, a symbolic expression or another subject-appropriate object; the operations must match that choice.

Construct the state from what the continuation needs. In a sequential procedure this often includes a control position and intermediate values. For each proposed next step, ask what it reads, changes and preserves. If two histories reach the same stored state but require different continuations, recover the omitted condition or summary. Use A.3.3 for the underlying state-and-continuation construction; keeping every past observation is only one possible repair.

Specify the meaning of an elementary operation at the level used by the argument. An exact integer addition is different from modular word addition. A comparison of exact rational numbers is different from comparing rounded observations. If an operation is available only through another procedure, expose that dependency when its conditions or cost can change this computation.

A formulation can specify equations or constraints without choosing an evaluation order. Identify the supplied quantities or boundary conditions, admissible solutions and the output the receiver needs. An applicable solver or modeled computational process must connect those relations to obtaining a result; its execution order may remain an implementation choice. When restructuring the equations, preserve the required solutions under the stated conditions and retain expressions that recover requested quantities removed from the computational state. If no such construction is available, the equations still characterize answers and the missing way remains a task under :4.3.

The available operations can also be the starting contribution. A collaborator working under C.29.3 may supply preparable inputs, controllable changes, readable outputs and their limits for a candidate system. Use those capabilities to propose computational states and operations that can answer a useful question; do not force them into an unsuitable instruction set. Keep the physical model and the experimental or conditional basis of that contribution visible. A new computational model or language needs meanings for its expressions as well as formation rules. A.6.3.RT helps construct expressions under available notation rules; designing missing rules is separate notation or language-design work.

#### C.29.2:4.3 - Obtain the computational construction

If a known construction answers the question, recover its inputs, operative rules or steps and assumptions from its explanation and use it. B.5 supports that recovery. Check that the available operations can perform those steps and that their result has the required interpretation. A library or solver can supply the construction, but its accepted input class, result guarantee and failure behavior must fit the present use.

When the connection is not yet known, work on the missing operation rather than rewriting the output condition:

1. Calculate a small instance with enough detail to see what is being produced.
2. Identify what remains to be obtained after one available operation. Try to express that remainder using the same kind of problem or a known subproblem.
3. Retain the intermediate information needed to join the contributions. If an operation overwrites a value still needed later, save it or change the ordering.
4. State how the joined result satisfies the original answer condition, then try a case that changes a material assumption.

This is a way to expose and develop a construction, not a universal algorithm-discovery guarantee. Recurrence construction, search, optimization, numerical discretization and other techniques have their own subject methods. Use C.39 to find or develop a missing way; use C.40 when a workable change-and-test operation is already available and branching search is the live difficulty.

For a still-missing contribution, return a substantive task: the available inputs and operations, the result or intermediate relation needed, the conditions it must preserve, and what would count as a useful solution. “Find a better algorithm” is usually too weak. After a dense-state rejection, for example: “Given this circuit family and this requested observable, provide a representation and update/readout procedure with a justified error bound and a peak-memory estimate below the stated budget; do not materialize the full amplitude array in a hidden conversion.”

#### C.29.2:4.4 - Explain the result and progress

For a proposed computation, follow a small case from supplied inputs through the available construction to the interpreted output. Show the changing values or solved relations, and expose operation order when it affects the result. This catches missing state, ambiguous instruction order and an output interpreted under the wrong convention.

Then supply the argument appropriate to the claimed range. For a loop, find a statement relating the current state to the work already completed and the answer still sought. Show that initialization establishes it, each iteration preserves it, and the stopping condition makes the desired conclusion follow. This statement is the loop invariant. Separately explain why the loop reaches that condition, for example through a nonnegative integer that decreases at every iteration. For a recursive construction, explain its initial cases, the smaller calls and how their results give the caller's answer.

These are useful proof forms, not compulsory syntax for every computation. A direct finite composition may need only substitution through its operations. A randomized procedure needs its probability argument. For an estimated statistic, state the sampling assumptions and connect the claimed error or uncertainty to the sample count. For a continuing interaction, state the preservation or response property required and the assumptions under which progress is claimed; global termination may be the wrong requirement.

Keep the extent of the conclusion honest. A trace establishes that traced case. A proof using exact arithmetic establishes the stated abstract procedure under exact arithmetic. A finite precision implementation or an executing device requires the relevant additional comparison. Tests can expose failures and support selected empirical claims; a few passing tests do not prove an unrestricted input claim.

#### C.29.2:4.5 - Resolve accuracy and computational limits that affect the use

A well-defined mathematical object need not have the finite representation or uniform procedure being assumed. Ask what information the input representation actually provides and which operations are effective on it. Replacing “all real numbers” by finite strings, an evaluation oracle or a family of increasingly accurate approximations changes the computational problem. If a computability or impossibility claim matters, obtain the applicable subject argument rather than inferring it from a failed attempt.

For a finite search domain with an effective test, explicit enumeration can provide a terminating baseline. It may be too expensive, but it separates an obtainable procedure from an open construction. For an unbounded search, failure to find an answer in the allotted time leaves a different result; it does not establish nonexistence.

For numerical work, connect the stopping test to error in the requested output. Locate relevant errors in input representation, algorithmic approximation, arithmetic and output conversion. Allocate tolerance among them only under a justified rule for combining their effects. Physical-model and measurement uncertainty remain separate inputs from the relevant modeling and C.16 methods; numerical convergence does not settle them.

If finite precision can reverse a decisive comparison, increase precision, use a justified enclosure, reformulate the test or return that comparison as unresolved. If an iteration no longer changes its stored state, a limit of the ideal iteration does not show that the implementation will reach the requested tolerance. Return to the representation or stopping rule. Narrow the claim only when the narrower answer remains useful and the change is explicit.

#### C.29.2:4.6 - Calculate costs from the chosen representation

Begin with the resource that can decide the choice. For a stored array, derive how many elements the representation requires and how much storage each element occupies:

`payload storage = element count × bytes per element`.

For several simultaneously live arrays, add their payloads and the workspace, indices, temporary copies and other storage used by the proposed algorithm. Peak memory concerns what must coexist, not the total amount ever allocated. A payload lower bound may already reject a design; a payload that fits is not yet a complete fit argument.

In a model of discrete operations, count how often each operation is performed and what each performance costs. State the size parameters. An instruction count with one unit per arithmetic operation answers a different question from bit operations on growing integers, memory transfers or elapsed time on a particular machine. Explain the dominant term before using asymptotic notation. A bound for one representation is not a lower bound for every algorithm solving the mathematical problem.

A computation described by continuous dynamics may need a cost relation for duration and accuracy rather than an instruction count; obtain the relevant estimate with C.29.3.

Include input conversion, preparation computation and output production when they can dominate the result. Precomputation can be worthwhile across many uses, but say how many uses amortize it. A compact internal state does not make an explicitly requested exponential-size output cheap to enumerate.

When resources fail, change one of the actual causes: represented structure, stored precision, retained data, procedure, admitted problem class, requested answer or proposed execution resources. Recompute for the chosen alternative. An exact structural reduction, a lossy approximation and a different cost model are different changes. C.29.1 supplies a needed consequence-transfer argument; C.29.3 assesses whether the resulting execution arrangement supports the selected computation.

#### C.29.2:4.7 - Return the sufficient result and its next use

Return the formulation and its obtaining construction when available, with enough representation and output meaning to use them, the conditions of the argument, and the resource or accuracy limit that can change the decision. Reuse an existing explanation where it supplies these connections.

If a contribution is absent, identify it at the failing connection. A missing state distinction returns to formulation; an unavailable algorithm returns to its construction; an unsupported numerical bound returns to the numerical method; an execution mismatch returns to C.29.3, which may in turn supply a reason to revise this formulation. The iteration can change both model and executing arrangement.

A conditional procedure, a restricted result or an obstruction can be sufficient. Keep “no procedure obtained”, “this representation exceeds the budget”, “no algorithm exists in the stated model”, and “the implementation failed on this case” as different conclusions, each with its own basis.


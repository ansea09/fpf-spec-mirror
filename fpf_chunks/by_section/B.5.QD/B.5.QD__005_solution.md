---
chunk_kind: "child"
pattern_id: "B.5.QD"
pattern_title: "Develop a Question from a Result or Construction"
section_id: "B.5.QD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.QD/B.5.QD__005_solution.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "B.5.QD — Develop a Question from a Result or Construction"
  - "B.5.QD:4 — Solution"
line_start: 51491
line_end: 51566
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

### B.5.QD:4 - Solution

**Recover what changed → find the consequential dependency or new operation → formulate the question it opens → use a case, construction or argument to establish a useful point of entry → choose how to continue.**

Enter with the result that changed the inquiry. Reuse a known formulation or derivation when it supplies the needed step. Return to an earlier step if an attempted answer reveals that the question is ambiguous, underdetermined or more expensive than its use warrants.

#### B.5.QD:4.1 - Recover the contribution of the earlier work

State the earlier question and what the work obtained. Identify the part that matters: a counterexample, an unresolved inference, a constructed object, a computational operation or a distinction the earlier description omitted.

For a failure, locate its scope. A counterexample to a lemma can expose a defect in one argument while leaving the main conjecture undecided. A counterexample satisfying the main conjecture's premises refutes that conjecture. A program's failure on a case may instead concern its implementation. Recover the relevant reasoning under B.5.RA or B.5.RR when this difference is unclear.

For a success, recover what can be done with the result. Explain its inputs, output and application conditions. A computation that produces cumulative totals, for example, may provide a way to answer many interval questions. Its reusable contribution is the relation between those totals and the intervals.

Keep independently supported results available. They can supply the construction, limiting case or partial answer for the next question.

#### B.5.QD:4.2 - Find the relation that can change the question

Follow the earlier result back to a consequential dependency, or forward to an operation it enables.

If a description gives the same information for cases that need different answers, construct two such cases. Their difference identifies information a stronger question may need. If an inference depends on an unproved step, state the missing step as a possible question. If an operation succeeds, ask which other inputs, outputs or combinations preserve its useful relation.

Use variations that have a reason in the work. The following are common ways to construct them.

| What the work reveals | How to form the next question |
|---|---|
| A counterexample identifies a failed condition. | Ask which condition would support the needed conclusion, or which construction identifies the cases where it fails. |
| A successful construction produces more information than the first answer used. | Ask what further result can be obtained from that information and by which operation. |
| Different cases collapse to one description. | Ask what additional distinction determines the answer, or what bound remains possible without it. |
| An argument needs an unavailable intermediate result. | Ask for a lemma, witness or construction that supplies that step; state how it would be used. |
| A familiar operation becomes available in another setting. | Ask whether its required relations hold there and what receiving task it can serve. |

Ask what the variation preserves for the earlier question. A counterexample on a tree can refute a claim about all graphs. A theorem for trees can settle a request about all graphs if a valid reduction carries its conclusion back to every graph at issue. Without such a connection, keep the broader claim open. When research direction is yours to choose, you can pursue the tree question for its own mathematical interest. When the broader answer was requested, identify what remains due or obtain agreement to a different result.

These variations can be combined or repeated. Their purpose is to expose a useful answer.

When requirements appear incompatible, B.5.QD.CF recovers the premises producing the conflict and asks what other construction could satisfy the retained need. It distinguishes changing an assumed means or representation from changing a requirement, and can return a useful impossibility when the conditions must remain.

#### B.5.QD:4.3 - Give the question an answer form

Say what would answer the question: for example, a construction, an explanatory relation, a bound, a counterexample or a condition under which an operation works. State the objects, allowed changes and premises that can alter the answer.

Connect that answer to its possible use. “Find a partition” and “return a partition or an odd-cycle witness” make different contributions: the second also explains failure. “Predict the position” and “bound the reachable positions” may serve the decision at different effort.

Separate a proposed answer from the question. “Does this procedure always terminate on finite inputs?” remains a useful question when the proposed positive answer is false. The failing case can open the question of a termination condition or another procedure.

If a question combines several missing contributions, make the dependency visible. For a physical calculation, you may first need a model that determines a quantity, then a computation of that model, then an interpretation for action. B.5.MPC coordinates those contributions. Name the first unresolved connection so a person, AI agent or group can work on it using the available subject knowledge and tools.

#### B.5.QD:4.4 - Find an entry that reveals what the question requires

Choose an entry that exposes what must be done. A small case is useful when changing one condition reveals an obstruction or a lost distinction. If the relevant dependence already follows from an argument or a construction over arbitrary admissible inputs, use that reasoning directly. To distinguish two possible explanations of an occurrence, seek grounds about that occurrence. A new hypothetical case can show how the explanations differ.

Use the result to improve the question. A successful case can expose a reusable relation. A failed case can identify a missing premise, an incompatible demand or an operation to be developed. If two admissible cases give different answers from the same supplied information, ask for the missing distinction or a result valid for both.

A case establishes its result. A broader mathematical claim needs its derivation, and applying a physical model needs the relevant physical basis. The question can be useful before those answers are established: the first attempt should make the next contribution more identifiable.

Begin with available reasoning and information. Obtain further evidence only when its possible answers can change the useful inquiry enough to justify the effort under C.11.DUA. An existing bound or conditional answer may settle the use.

#### B.5.QD:4.5 - Choose an attainable inquiry

Compare the few questions that remain candidates. Ask what each answer would enable and where work could begin with the available capabilities, collaborators and resources. Include the cost of learning or obtaining a missing operation when it affects the choice.

A worthwhile first question may be narrower than the eventual aim: establish a limiting case, find one witness, recover a missing lemma or test a proposed connection. Explain how that result would contribute to the larger question. If the contribution is available, use it and select the next unresolved step.

E.10.INT helps distinguish useful interest from novelty, surprise or a local scoring heuristic. A question can be worth pursuing because it opens further constructions, changes what can be explained or makes another question approachable. Its eventual practical destination may remain unknown. When problems and ways of solving them must develop together, use C.40; retain a promising alternative when its prospective use justifies doing so.

Continue with the chosen question, the contribution that makes it attainable and the dependency it is meant to resolve. Stop when the requested result is in hand. In an open inquiry, a better use of the available effort can justify changing direction. For a fixed assignment, a reason to stop investigating identifies a limit on the answer unless the work already meets the assignment or its holder has changed it.

#### B.5.QD:4.6 - Separate question recognition from answer assurance

Recognize the opening from a changed possibility of inquiry. One worked counterexample or a useful new operation can be sufficient to begin developing the question.

Judge the question by whether it has a recoverable meaning, a possible contribution and a workable point of entry. Judge its proposed answer by the claim it makes. A conjecture, a proven relation, a simulated result and an observed physical effect support different uses. Apply their subject Methods and B.3 when the receiving use needs that assurance.

Reuse the question while its purpose and conditions remain applicable. Reopen it when a result changes its premises, available operations, attainable scope or intended use. A solved question can open another valuable one; an adequate answer can also end the present work.


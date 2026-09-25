---
chunk_kind: "child"
pattern_id: "B.5.QD"
pattern_title: "Develop a New Question from a Result or Construction"
section_id: "B.5.QD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.QD/B.5.QD__005_solution.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "B.5.QD — Develop a New Question from a Result or Construction"
  - "B.5.QD:4 — Solution"
line_start: 45626
line_end: 45701
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

**Recover what changed → locate the dependency or new operation → construct a consequential question → work a revealing case → choose the next inquiry and keep what remains useful.**

Enter with the result that actually changed the inquiry. Reuse a known formulation or derivation when it already supplies the needed step. Return to an earlier step if an attempted answer reveals that the question is ambiguous, underdetermined or more expensive than its use warrants.

#### B.5.QD:4.1 - Recover the contribution of the earlier work

State the earlier question and what the work actually obtained. Identify the part that matters now: a counterexample, an unresolved inference, a constructed object, a computational operation or a distinction the earlier description omitted.

For a failure, locate its scope. A counterexample to a lemma can expose a defect in one argument while leaving the main conjecture undecided. A counterexample satisfying the main conjecture's premises refutes that conjecture. A program's failure on a case may instead concern its implementation. Recover the relevant reasoning under B.5.RA or B.5.RR when this difference is unclear.

For a success, recover what can now be done with the result. Explain its inputs, output and application conditions. A computation that produces cumulative totals, for example, may provide a way to answer many interval questions. Its reusable contribution is the relation between those totals and the intervals.

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
| A familiar operation becomes available in another setting. | Ask whether its required relations hold there and what receiving task it can now serve. |

A variation can change the original task. Preserve that change explicitly: restricting a claim to trees may give a valid result while leaving the original request about all graphs unanswered. If the broader request still matters, keep it as an unresolved question.

These variations can be combined or repeated. Their purpose is to expose a useful answer, not to fill a catalogue of question types.

When requirements appear incompatible, B.5.QD.CF recovers the premises producing the conflict and asks what other construction could satisfy the retained need. It distinguishes changing an assumed means or representation from changing a requirement, and can return a useful impossibility when the conditions must remain.

#### B.5.QD:4.3 - Give the new question an answer form

Say what would answer the question: for example, a construction, an explanatory relation, a bound, a counterexample or a condition under which an operation works. State the objects, allowed changes and premises that can alter the answer.

Connect that answer to its possible use. “Find a partition” and “return a partition or an odd-cycle witness” make different contributions: the second also explains failure. “Predict the position” and “bound the reachable positions” may serve the same present decision at different effort.

Separate a proposed answer from the question. “Does this procedure always terminate on finite inputs?” remains a useful question when the proposed positive answer is false. The failing case can open the question of a termination condition or another procedure.

If a question combines several missing contributions, make the dependency visible. For a physical calculation, you may first need a model that determines a quantity, then a computation of that model, then an interpretation for action. B.5.MPC coordinates those contributions. Name the first unresolved connection so a person, AI agent or group can work on it using the available subject knowledge and tools.

#### B.5.QD:4.4 - Work a case that reveals the difficulty

Choose a small case that exercises the changed condition or new operation. Attempt the requested construction or inference and explain where it succeeds or stops.

Use the result to improve the question. A successful case can expose a reusable relation. A failed case can identify a missing premise, an incompatible demand or an operation still to be developed. If two admissible cases give different answers from the same supplied information, ask for the missing distinction or a result valid for both.

A case establishes its own result. A broader mathematical claim needs its derivation, and applying a physical model needs the relevant physical basis. The question can already be useful before those answers are established: the first attempt should make the next contribution more identifiable.

Begin with available reasoning and information. Obtain further evidence only when its possible answers can change the useful inquiry enough to justify the effort under C.11.DUA. An existing bound or conditional answer may settle the current use.

#### B.5.QD:4.5 - Choose an attainable inquiry

Compare the few questions that remain serious candidates. Ask what each answer would enable and where work could begin with the available capabilities, collaborators and resources. Include the cost of learning or obtaining a missing operation when it affects the choice.

A worthwhile first question may be narrower than the eventual aim: establish a limiting case, find one witness, recover a missing lemma or test a proposed connection. Explain how that result would contribute to the larger question. If the contribution is already available, use it and select the next unresolved step.

E.10.INT helps distinguish useful interest from novelty, surprise or a local scoring heuristic. A question can be worth pursuing because it opens further constructions, changes what can be explained or makes another question approachable. Its eventual practical destination may remain unknown. When problems and ways of solving them must develop together, use C.40; retain a promising alternative when its prospective use justifies doing so.

Continue with the chosen question, its first attempt and the dependency that attempt is meant to resolve. A short explanation in the work can carry this result. Stop when the current need is answered, or when another inquiry is the better use of the available effort.

#### B.5.QD:4.6 - Separate question recognition from answer assurance

Recognize the opening from a changed possibility of inquiry. One worked counterexample or a useful new operation can be sufficient to begin developing the question.

Judge the question by whether it has a recoverable meaning, a possible contribution and a workable point of entry. Judge its proposed answer by the claim it makes. A conjecture, a proven relation, a simulated result and an observed physical effect support different uses. Apply their subject Methods and B.3 when the receiving use needs that assurance.

Reuse the question while its purpose and conditions remain applicable. Reopen it when a result changes its premises, available operations, attainable scope or intended use. A solved question can open another valuable one; an adequate answer can also end the present work.


---
chunk_kind: "child"
pattern_id: "B.5.MR"
pattern_title: "Compare Models by Refinement and Abstraction"
section_id: "B.5.MR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MR/B.5.MR__005_solution.md"
commit_sha: "e230eef4f6955116bf697ca9ba5e79247af1843e"
heading_path:
  - "B.5.MR — Compare Models by Refinement and Abstraction"
  - "B.5.MR:4 — Solution"
line_start: 50784
line_end: 50845
dependencies:
  - "B.1"
  - "B.5.FM"
  - "B.5.TC"
  - "C.2.1"
  - "C.37.MM"
keywords:
---

### B.5.MR:4 - Solution

A model states something about a system, method or another modeled entity, and can leave several answers open. First say which inquiry is being answered and recover the assertions that govern those answers. Refining a model determines something it leaves open while preserving what it already establishes. Abstracting a model leaves determinations open while retaining what the receiving inquiry needs. Compare the admitted answers to establish either relation.

#### B.5.MR:4.1 - Recover the assertions and the answers left open

Identify the modeled entity or the range of candidate applications left open, the inquiry, and the conditions under which each answer will be read. Keep the force of the claims explicit when it matters. Permitted values, predicted values and observed values answer different questions. For a claim-bearing model recover its content, EntityOfConcern and effective interpretation under C.2.1. For a physical model establish which observations on it warrant which inference about the target. PHY.1 in Physical Thinking gives the similarity conditions for transferring a selected observable across changes of scale or operating conditions.

Recover what the model asserts about the participants: which quantities may vary, which relationships must hold, which designs qualify or which performances a Method permits. The relevant subject Method supplies their types and grounds. A stated condition may be an assertion of the model or an assumption under which it applies; distinguish these when they change the answer. If the expression leaves its assertion unrecoverable, use F.19 before treating it as a model at a higher abstraction level.

A **completion** settles what the model leaves open for this inquiry while satisfying its assertions. It can be a candidate design satisfying specified relationships, a behavior compatible with observations, or a structure satisfying stated axioms. An admitted completion need not have been observed, built or authorized for use. A list of observed instances therefore need not exhaust the completions. Choose what the inquiry can distinguish. When likelihoods matter, include the probability claims being compared. Two models can allow the same outcomes and assign them different probabilities.

#### B.5.MR:4.2 - Test preservation and strictness

Identify the completions each model admits. Call the proposed refined model C and the model whose assertions it must preserve A. When their languages or detail differ, explain how every completion of C is read in the terms used for A's answer, and why that reading serves the inquiry. Test that a completion of C exists and that each completion of C, so read, satisfies A's assertions. When these tests hold, **C refines A**, and **A is an abstraction of C**, for this inquiry and interpretation. The two names give converse directions of the same comparison.

This relation includes equivalent answers. To establish **strict refinement**, also identify an answer admitted by A that no completion of C can produce. Only with this strict difference call C **more concrete** than A and A **more abstract** than C. Show a surviving completion of C so that exclusion cannot be attributed to inconsistent assertions.

If a model admits no completion, examine which assertions make it infeasible. If both models admit none, neither supplies a feasible answer. When each admits at least one completion, equal sets of observable answers establish agreement for this inquiry. If each admits an answer the other excludes, the models are incomparable by refinement. They may still share answers. If they share none, their assertions conflict under the common reading. When feasibility or the correspondence is unknown, identify what would settle it.

Under a fixed common reading, the admitted answers order comparable models, with equivalent answers sharing a position. An inquiry that distinguishes additional features can give a different comparison. Before composing comparisons across languages, establish how their interpretations compose. The names do not impose a single ranking on all models.

A claim of greater accuracy needs a reference and an error criterion. A bound can establish accuracy against a mathematical reference. For a claim about accuracy on an actual system, use observations under the relevant conditions. Refinement alone supplies neither empirical accuracy nor evidence of actual performance.

##### B.5.MR:4.2.1 - Refine a model for a further decision

Identify what the next decision needs determined: a value, a construction choice, a permitted performance or another answer left open. Obtain the subject grounds for that determination. Add or bind the corresponding assertion and compare the resulting model with the starting model by section 4.2. Explain the preserved assertions, show a surviving completion and identify any excluded answer.

An added assertion can merely repeat what already follows; then it does not establish a more concrete position for the inquiry. If the resulting model admits a formerly excluded answer or the added assertion contradicts the starting model, report the changed assertion or conflict and reconsider the model. Greater length or a local label does not settle this comparison.

##### B.5.MR:4.2.2 - Construct or select an abstraction

Identify the conclusion the receiving work still needs and the determinations on which it depends. Decide which other determinations may be left open. Construct a model that leaves them open, or select an existing model that does so.

Compare the starting model as C with the proposed abstraction as A under section 4.2: C must have a completion, and every completion of C must satisfy A under the established interpretation. Then check the needed conclusion over the answers A admits. Identify any prior conclusion that no longer follows and the determination on which it depended; report when no conclusion is lost for the inquiry. If the needed conclusion is lost, retain that determination or choose a different abstraction.

Several abstractions can serve different inquiries about the same starting model; several concrete models can refine one abstraction. The comparison supplies no unique inverse construction. Leaving a variable open also does not prove that a result observed at one value holds at every newly admitted value. Wider empirical or methodological claims need their subject grounds. Retaining the same assertions in clearer wording is clarification of their expression; it does not change this model order.

#### B.5.MR:4.3 - Locate levels of model abstraction in an application chain

A **level of model abstraction** is a relative position under the comparison in section 4.2. When the inquiry concerns which applications are eligible, a chain may leave open or determine the interpretation of a formal construction, the discipline, the local conditions and the individual. Five useful names locate these possible restrictions.

| Position | What can be fixed while preserving earlier assertions |
| --- | --- |
| L4, foundational | A formal or computational construction and the choices its own conditions permit. |
| L3, transdisciplinary | A principle interpreted across eligible disciplines. Bind it to the construction wherever that interpretation is warranted. |
| L2, disciplinary | A subject discipline and the professional method, constraints or interpretation used there. |
| L1, local | Conditions shared by a particular setting or recurrent local population. |
| L0, individual | The identity of the particular entity or occurrence being modeled. Its unobserved characteristics can remain open. |

Read L0 toward L4 as abstraction, and L4 toward L0 as refinement, where the comparisons establish those relations. At each step identify the assertions retained and the warranted interpretation. For a strict step, show which answer the more abstract model admits and the more concrete model excludes, together with a surviving completion. The position's name alone establishes neither preservation nor strictness.

Two successive application positions can admit exactly the same answers, as when a local setting adopts a professional rule unchanged for the inquiry at hand. They then occupy the same abstraction position for that inquiry. Specializing an application keeps the general rule as a premise. Merely discarding inconvenient cases from a purported universal result weakens its support. Use the steps the inquiry needs. Several consequential determinations may fall within one named application position; if the individual was fixed at the outset, binding its identity again removes no possibility.

When the entity is a method, a professional rule can be applied locally and a performed work occurrence can be compared with it. Establishing that the work occurred and followed the rule needs its own evidence. When the entity is a system, a more restrictive model can concern the very same system at the same scale. Moving to a constituent invokes the relevant constructive relation under B.1; its effect on the inquiry needs to be established separately.

Core, DPFs and LPFs supply models that can participate in such comparisons. A publication or discipline does not itself have one abstraction level. Binding a parameter can refine a model without changing its language; changing professional vocabulary can preserve all its admitted answers. A richer representation language can also express a model applicable to more situations. Compare the interpreted assertions for the inquiry.

#### B.5.MR:4.4 - Compare models of models by the same test

A metamodel states conditions on admissible models, such as which field or relation can occur and how it is interpreted. Conformance asks whether a particular model satisfies those conditions. Refinement **of a metamodel** compares two such sets of conditions for the same inquiry about admissible models. A model can conform to both editions. A model conforming to a metamodel and that metamodel conforming to higher-order construction rules gives two separate conformance judgements. C.37.MM helps keep their participants and governing editions recoverable when the models are passed on.


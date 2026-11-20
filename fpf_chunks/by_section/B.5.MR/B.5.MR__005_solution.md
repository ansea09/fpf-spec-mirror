---
chunk_kind: "child"
pattern_id: "B.5.MR"
pattern_title: "Compare Models by Refinement and Abstraction"
section_id: "B.5.MR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MR/B.5.MR__005_solution.md"
commit_sha: "5e9f4d868afa1f9db90d4c7ff6840bd55f3b8d18"
heading_path:
  - "B.5.MR — Compare Models by Refinement and Abstraction"
  - "B.5.MR:4 — Solution"
line_start: 50815
line_end: 50878
dependencies:
  - "B.1"
  - "B.5.FM"
  - "B.5.TC"
  - "C.2.1"
  - "C.37.MM"
keywords:
---

### B.5.MR:4 - Solution

Begin with one question that both models answer. Which designs, executions or other alternatives does each model admit? To refine a model, choose something it leaves open. Show that at least one alternative remains and that every remaining alternative satisfies the earlier assertions under the chosen interpretation. To abstract a model, decide what to leave open and apply the same test with the starting model on the concrete side. The answers tell you whether the difference is strict and which conclusions still hold.

#### B.5.MR:4.1 - Recover the assertions and the answers left open

Identify the modeled entity or the range of candidate applications left open, the inquiry, and the conditions under which each answer will be read. Keep the force of the claims explicit when it matters. Permitted values, predicted values and observed values answer different questions. For a claim-bearing model recover its content, EntityOfConcern and effective interpretation under C.2.1. For a physical model establish which observations on it warrant which inference about the target. PHY.1 in Physical Thinking gives the similarity conditions for transferring a selected observable across changes of scale or operating conditions.

Recover what the model asserts about the participants: which quantities may vary, which relationships must hold, which designs qualify or which performances a Method permits. The relevant subject Method supplies their types and grounds. A stated condition may be an assertion of the model or an assumption under which it applies; distinguish these when they change the answer. If the expression leaves its assertion unrecoverable, use F.19 before treating it as a model at a higher abstraction level.

A **completion** is one way of settling what the model leaves open for this inquiry while satisfying its assertions. A candidate design, a possible behavior or a structure satisfying stated axioms can serve as a completion. The inquiry determines what answer can be read from it. Several different designs can give the same answer. A completion need not have been observed, built or authorized for use. Include probability claims when the inquiry concerns likelihood. Two models can allow the same outcomes and assign them different probabilities.

#### B.5.MR:4.2 - Test preservation and strictness

Identify the completions each model admits. Call the proposed refined model C and the model whose assertions it must preserve A. When their languages or detail differ, explain how every completion of C is read in the terms used for A's answer, and why that reading serves the inquiry. Test that a completion of C exists and that each completion of C, so read, satisfies A's assertions. When these tests hold, **C refines A**, and **A is an abstraction of C**, for this inquiry and interpretation. The two names give converse directions of the same comparison.

This relation includes equivalent answers. To establish **strict refinement**, also identify an answer admitted by A that no completion of C can produce. Only with this strict difference call C **more concrete** than A and A **more abstract** than C. Show a surviving completion of C so that exclusion cannot be attributed to inconsistent assertions.

If a model admits no completion, examine which assertions make it infeasible. If both models admit none, neither supplies a feasible answer. When each admits at least one completion, equal sets of observable answers establish agreement for this inquiry. If each admits an answer the other excludes, the models are incomparable by refinement. They may still share answers. If they share none, their assertions conflict under the common reading. When feasibility or the correspondence is unknown, identify what would settle it.

Within a chain of models that pass the feasibility and preservation tests under a common interpretation, models that admit the same answers share a level for this inquiry. On different branches, models can give the same answer and impose incompatible constraints. Test preservation separately for the pair in question. A different inquiry can distinguish models the first one treated alike. Before composing comparisons across languages, establish how their interpretations compose.

A claim of greater accuracy needs a reference and an error criterion. A bound can establish accuracy against a mathematical reference. For a claim about accuracy on an actual system, use observations under the relevant conditions. Refinement alone supplies neither empirical accuracy nor evidence of actual performance.

##### B.5.MR:4.2.1 - Refine a model for a further decision

Identify what the next decision needs determined: a value, a construction choice, a permitted performance or another answer left open. Obtain the subject grounds for that determination. Add or bind the corresponding assertion and compare the resulting model with the starting model by section 4.2. Explain the preserved assertions, show a surviving completion and identify any excluded answer.

An added assertion can repeat what already follows. For that inquiry the two models then admit the same answers. If the new model admits a previously excluded answer or contradicts an earlier assertion, identify what changed and reconsider the claim of refinement.

##### B.5.MR:4.2.2 - Construct or select an abstraction

Identify the conclusion the receiving work still needs and the determinations on which it depends. Decide which other determinations may be left open. Construct a model that leaves them open, or select an existing model that does so.

Compare the starting model as C with the proposed abstraction as A under section 4.2: C must have a completion, and every completion of C must satisfy A under the established interpretation. Then check the needed conclusion over the answers A admits. Identify any prior conclusion that no longer follows and the determination on which it depended; report when no conclusion is lost for the inquiry. If the needed conclusion is lost, retain that determination or choose a different abstraction.

Several abstractions can serve different inquiries about the same starting model; several concrete models can refine one abstraction. The comparison supplies no unique inverse construction. Leaving a variable open also does not prove that a result observed at one value holds at every newly admitted value. Wider empirical or methodological claims need their subject grounds. Retaining the same assertions in clearer wording is clarification of their expression; it does not change this model order.

#### B.5.MR:4.3 - Read the levels of model abstraction and refinement

Read **L0 → L4 as levels of model abstraction** and **L4 → L0 as levels of model refinement**. Both names describe one order. A more concrete model preserves the earlier assertions and rules out an answer the more abstract model allowed. Abstracting a model or refining a model is the work of constructing or selecting the model on the chosen side of that comparison. In a chain of applications the five names below identify what each model specifies.

| Level, from more abstract towards more concrete models | What the model specifies |
| --- | --- |
| L4, foundational | A formal or computational construction and the choices its own conditions permit. |
| L3, transdisciplinary | A principle interpreted across eligible disciplines. Bind it to the construction wherever that interpretation is warranted. |
| L2, disciplinary | A subject discipline and the professional method, constraints or interpretation used there. |
| L1, local | Conditions shared by a particular setting or recurrent local population. |
| L0, individual | The identity of the particular entity or occurrence being modeled. Its unobserved characteristics can remain open. |

**Use the levels when deciding what a result establishes.** State the decision and what the model for that decision must specify. Identify the model actually available. An L0 model that identifies a delivery can contain its planned arrival. To decide whether that delivery met its deadline, compare the verified actual arrival with the deadline in force. To decide whether a scheduling rule at L2 guarantees all its deadlines, examine why the rule covers every permitted schedule. One admissible schedule that misses a deadline defeats the claim that every permitted schedule meets its deadline. For a target of 95 percent of actual deliveries on time, assess the eligible deliveries in the specified population and period. Count a late arrival when it occurred there. A calculation using the rule can check its consequences while leaving open who designed it. Carry the result to the decision through the grounds for that particular inference in C.39.QR:4.2–4.3. Accept the conclusion those grounds support and identify what would settle the outstanding claim.

Check each pair for one inquiry under §4.2. Establish which earlier assertions every remaining design or permitted performance satisfies. Show that at least one remains. If the step is strict, name an answer that can no longer be obtained. The same test applies to two models of one design or method, including when both are disciplinary models.

If a site adopts a disciplinary rule with the same interpretation and adds no constraint on the action in question, write “the site uses the L2 rule unchanged.” The L1 practice model records the site's adoption of the rule for recurring work. If asked at what level the rule specifies the permitted action, keep L2. Claim a further level of refinement for that action only when the local model excludes a previously permitted answer. Several strict refinements can occur within one named level. If a rule permits a check at either site, specifying the first site excludes the second answer to “Where may this check take place?” If both sites have to be checked, dropping one abandons an obligation.

A disciplinary model can prescribe a method, a local model can specify how it may be used at one site, and an individual model can describe a particular performance. Evidence that the work occurred and followed the rule must come from that performance. Two models of a system can also stand in strict refinement at the same physical scale. Moving to a constituent invokes the constructive relation under B.1.

Core, DPFs and LPFs supply models that can participate in such comparisons. A publication or discipline does not itself have one abstraction level. Binding a parameter can refine a model without changing its language; changing professional vocabulary can preserve all its admitted answers. A richer representation language can also express a model applicable to more situations. Compare the interpreted assertions for the inquiry.

#### B.5.MR:4.4 - Compare models of models by the same test

A metamodel states conditions on admissible models, such as which field or relation can occur and how it is interpreted. Conformance asks whether a particular model satisfies those conditions. Refinement **of a metamodel** compares two such sets of conditions for the same inquiry about admissible models. A model can conform to both editions. A model conforming to a metamodel and that metamodel conforming to higher-order construction rules gives two separate conformance judgements. C.37.MM helps keep their participants and governing editions recoverable when the models are passed on.


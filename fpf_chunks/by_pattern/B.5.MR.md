---
chunk_kind: "parent"
pattern_id: "B.5.MR"
pattern_title: "Compare Models for Refinement"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/B.5.MR.md"
commit_sha: "eaef57bb8e4f119376cf48dc8f9b5297beb4559b"
heading_path:
  - "B.5.MR — Compare Models for Refinement"
line_start: 50766
line_end: 50858
dependencies:
  - "B.1"
  - "B.5.FM"
  - "B.5.TC"
  - "C.2.1"
  - "C.37.MM"
keywords:
---

## B.5.MR - Compare Models for Refinement

> **Type:** Method pattern
> **Status:** Stable

### B.5.MR:1 - Problem frame

**Use this when** someone proposes to rely on a later model because it is said to refine an earlier one. The practical question is which earlier conclusions still hold and which choice, state or behavior the later model now excludes. Two specifications of a design, two accounts of a method or two editions of the rules for constructing a model can each raise that question.

A useful first result is a sentence explaining what was open, what still qualifies, and what has become impossible under the new conditions. When deciding between theories that answer different questions, B.5.TC helps identify a comparable use. When the change is in the actual system, examine the changed system directly.

### B.5.MR:2 - Problem

More detail can narrow a choice, leave the answer unchanged, or contradict an earlier commitment. A change of wording, a new unit or a newly chosen discipline may also change what the reader takes the question to mean. How can the reader establish what a proposed refinement actually permits them to infer?

### B.5.MR:3 - Forces

A practitioner needs a quick comparison in ordinary terms. A consequential claim of preservation must cover all remaining possibilities. Model editions can use different representations. An apparent exclusion can arise from dropping a difficult case, changing the meaning of a quantity or switching from a design condition to a report of actual performance.

### B.5.MR:4 - Solution

#### B.5.MR:4.1 - State what the two models must answer

Identify the modeled entity or the range of candidate applications left open, the inquiry, and the conditions under which each answer will be read. Keep the force of the claims explicit when it matters. Permitted values, predicted values and observed values answer different questions. For a claim-bearing model recover its content, EntityOfConcern and effective interpretation under C.2.1. For a physical model establish which observations on it warrant which inference about the target. PHY.1 in Physical Thinking gives the similarity conditions for transferring a selected observable across changes of scale or operating conditions.

A **completion** settles what the model leaves open for this inquiry. It can be a candidate design satisfying some conditions, a behavior compatible with observations, or a structure satisfying some stated axioms. Choose what the inquiry can distinguish. When likelihoods matter, include the probability claims being compared. Two models can allow the same outcomes and assign them different probabilities.

#### B.5.MR:4.2 - Test preservation and strictness

Identify the completions each model admits. When their languages or detail differ, explain how every later completion is read in the terms used for the earlier answer, and why that reading serves the inquiry. Test that a later completion exists and that each later completion, so read, satisfies the earlier commitments. This establishes preservation. To establish **strict refinement**, also identify an earlier possibility that none of the remaining completions can produce. Show a surviving possibility so that exclusion cannot be attributed to inconsistent conditions.

If a model admits no completion, examine which of its conditions make it infeasible. If both models admit none, neither supplies a feasible answer. When each admits at least one completion, equal sets of observable answers establish agreement for this inquiry. If each admits an answer the other excludes, the models are incomparable by refinement. They may still share answers. If they share none, their commitments conflict under the common reading. When feasibility or the correspondence is unknown, identify what would settle it.

A claim of greater accuracy needs a reference and an error criterion. A bound can establish accuracy against a mathematical reference. For a claim about accuracy on an actual system, use observations under the relevant conditions.

#### B.5.MR:4.3 - Follow a chain to an application

When the inquiry concerns which applications are eligible, the starting model may leave open the interpretation of a formal construction, the discipline, the local conditions and the individual. Five useful names locate these possible restrictions.

| Position | What can be fixed while preserving earlier conditions |
| --- | --- |
| L4, foundational | A formal or computational construction and the choices its own conditions permit. |
| L3, transdisciplinary | A principle interpreted across eligible disciplines. Bind it to the construction wherever that interpretation is warranted. |
| L2, disciplinary | A subject discipline and the professional method, constraints or interpretation used there. |
| L1, local | Conditions shared by a particular setting or recurrent local population. |
| L0, individual | The identity of the particular entity or occurrence being modeled. Its unobserved characteristics can remain open. |

At each step identify the earlier commitments that still hold. For a strict step, show which earlier candidate drops out and which survives. Two successive positions can admit exactly the same answers, as when a local setting adopts a professional rule unchanged for the inquiry at hand. Specializing an application keeps the general rule as a premise. Merely discarding inconvenient cases from a purported universal result weakens its support. Use the steps the inquiry needs. Several consequential restrictions may fall within one position; if the individual was fixed at the outset, binding its identity again removes no possibility.

When the entity is a method, a professional rule can be applied locally and a performed work occurrence can be compared with it. Establishing that the work occurred and followed the rule needs its own evidence. When the entity is a system, a more restrictive model can concern the very same system at the same scale. Moving to a constituent invokes the relevant constructive relation under B.1; its effect on the inquiry needs to be established separately.

#### B.5.MR:4.4 - Compare models of models by the same test

A metamodel states conditions on admissible models, such as which field or relation can occur and how it is interpreted. Conformance asks whether a particular model satisfies those conditions. Refinement **of a metamodel** compares two such sets of conditions for the same inquiry about admissible models. A model can conform to both editions. A model conforming to a metamodel and that metamodel conforming to higher-order construction rules gives two separate conformance judgements. C.37.MM helps keep their participants and governing editions recoverable when the models are passed on.

### B.5.MR:5 - Archetypal Grounding

A project commissions a temperature recorder for one installation. The earlier specification permits records at whole-minute intervals of one or two minutes. The new specification permits only one-minute intervals and preserves the units, clock and operating conditions. A one-minute record is still eligible. A two-minute record is excluded. For the inquiry about permitted sampling intervals, this is strict refinement. If the recipient asks only whether every hour contains a reading, both specifications give the same answer. Whether the installed recorder met its specification last night requires observations of that recorder.

A work method screens requests under a criterion and then refers unresolved ones for a second judgement. A local revision adds a deadline to the referral while preserving the screening rule. A referral after the deadline was admissible under the earlier timing rule and now falls outside the local prescription. A second revision silently accepts some requests previously requiring referral. Compare that changed decision with the original rule before relying on it. An excellent record of one compliant case cannot settle the claim for the newly admitted cases.

### B.5.MR:6 - Bias-Annotation

A vivid individual case can conceal what the earlier condition covered. Start with the intended inquiry and an admissible alternative. Looking only for a stricter result can also hide agreement, a real conflict or uncertainty.

### B.5.MR:7 - Conformance Checklist

- The inquiry, participants, force, conditions and common reading are recoverable.
- A preservation claim has at least one admissible later completion and covers every later completion for the inquiry. A strict step also has an earlier possibility excluded by all the later completions.
- Claims of conformance, parthood, occurrence or empirical accuracy use the grounds for their own relations.

### B.5.MR:8 - Common Anti-Patterns and How to Avoid Them

A longer document may repeat the same commitments in a more useful form. Test which answers have changed. A project can also specify an individual that does not exist. If no candidate survives an attempted binding, reopen the identification.

### B.5.MR:9 - Consequences

A receiving practitioner can reuse preserved commitments, name the new restriction, and locate the premise that must be revisited when a model, correspondence or inquiry changes. A teacher can ask a learner to exhibit the exclusion on an unfamiliar application.

### B.5.MR:10 - Architectural Rationale

One comparison serves many kinds of modeled entity because it concerns the commitments a model makes for an inquiry. Kind-specific composition, physical similarity and performed work retain their own tests. This division lets the same model answer questions at different scales without assigning its file or language a single level.

### B.5.MR:11 - SoTA-Echoing

Specification theory compares models that satisfy stated sentences. It supports comparison across signatures when an interpretation specifies how a later model yields an earlier one. Under ordinary set inclusion, an empty class is included in every class. If the task is to show that a specification is infeasible, emptiness can settle it. A practitioner relying on a refined model to select a feasible design or action also needs a surviving completion. Section 4.2 therefore tests existence and preservation and asks which earlier possibility is lost when strictness matters. If the receiving inquiry changes what counts as the same answer, reconsider the interpretation and the comparison under it. [Sannella and Tarlecki, *Specifications in an Arbitrary Institution*, §§2 and 8](https://homepages.inf.ed.ac.uk/dts/pub/inst-asl.pdf)

### B.5.MR:12 - Relations

Use B.5.TC for comparisons of theoretical accounts, C.2.1 for the identity and grounding of epistemes, C.29 for a mathematical representation and its correspondence, B.1 for reasoning across holonic scales, and C.37.MM for coordinating and handing on models. E.10.D2 governs the use of a description as a specification.

### B.5.MR:End


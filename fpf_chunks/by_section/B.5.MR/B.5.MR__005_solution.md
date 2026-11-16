---
chunk_kind: "child"
pattern_id: "B.5.MR"
pattern_title: "Compare Models for Refinement"
section_id: "B.5.MR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MR/B.5.MR__005_solution.md"
commit_sha: "eaef57bb8e4f119376cf48dc8f9b5297beb4559b"
heading_path:
  - "B.5.MR — Compare Models for Refinement"
  - "B.5.MR:4 — Solution"
line_start: 50785
line_end: 50820
dependencies:
  - "B.1"
  - "B.5.FM"
  - "B.5.TC"
  - "C.2.1"
  - "C.37.MM"
keywords:
---

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


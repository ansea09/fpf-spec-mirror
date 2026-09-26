---
chunk_kind: "child"
pattern_id: "E.12"
pattern_title: "Didactic Primacy & Cognitive Ergonomics"
section_id: "E.12:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.12/E.12__005_solution.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "E.12 — Didactic Primacy & Cognitive Ergonomics"
  - "E.12:4 — Solution"
line_start: 89785
line_end: 89822
dependencies:
  - "C.11.DUA"
  - "E.13"
  - "E.2"
  - "E.9"
  - "F.19"
keywords:
  - "HF-Loop"
  - "Rationale Mandate"
  - "cognitive load"
  - "didactic"
  - "ergonomics"
  - "usability"
---

### E.12:4 - **Solution**

FPF elevates **Didactic Primacy (Pillar P-2)** to a normative architectural principle, operationalized through two conceptual mechanisms designed to act as a permanent counterbalance to excessive formalism.

#### E.12:4.1 - The Principle of Didactic Primacy (Expanded Definition)

The primary purpose of the FPF is to enhance the cognitive capabilities (qualified holder ability under A.2.2) of a reasoning system, team, organization, or other acting holon in service of its objectives. The creation of assurance-bearing epistemes or publications with high assurance levels and epistemic scores is a *means to that end, not the end itself*. Any architectural decision that increases formal rigor at the cost of clarity or usability must be explicitly justified by a demonstrable gain in that holder's ability to reason effectively.

#### E.12:4.2 - Mechanism 1: The Rationale Mandate

Every key assurance episteme or publication (such as a `U.AssuranceCase` or `Proof`) **MUST** contain a mandatory, human-readable **`rationale`** component.

*   **Nature:** The `rationale` is a narrative explanation of the cognitive benefit.
*   **Content:** It **MUST** answer the question: *"How does achieving this level of formal assurance tangibly help the agent better understand the problem or make a more reliable decision?"*
*   **Purpose:** This mandate requires the author to explain how the formal assurance serves its pragmatic, cognitive purpose. An empty or perfunctory rationale indicates that the assurance work may be an exercise in formalism for its own sake.

> **Didactic Note for Managers: The "So What?" Test**
>
> The Rationale Mandate is FPF's built-in "So What?" test. When your team presents a complex, formally checked episteme or publication, the `rationale` is where they answer your fundamental question: "This is impressive, but so what? How does this help us ship a better product, make a smarter investment, or avoid a critical risk?" If the answer is not clear in the `rationale`, the formal work's claimed practical benefit remains unexplained. Use this question to keep the team's formal work focused on the value it is meant to create. Any assurance-level claim needs its own applicable `B.3.3` profile and result.

#### E.12:4.3 - Mechanism 2: The Human-Factor Loop (HF-Loop)

Use this bounded inquiry when an intended reader encounters a specific consequential obstruction in a named passage or workflow under its stated prerequisites, or when a concrete work demand may cost more than it contributes to the receiving value. A workload report can identify a concern; it does not diagnose its cause or establish a psychometric threshold.

1. **Recover the working question.** Name the reader's task, passage or workflow, stated preparation/access prerequisites, failed or costly action, and the result it should support. Preserve the relevant assurance and control conditions. If the suspected demand cannot change a worthwhile result, C.11.DUA can justify stopping the inquiry at that limit.
2. **Inspect the initial attempt before explaining.** For an actual reading inquiry, retain what the reader initially understood and tried with the public passage and stated task inputs, including where the action stopped or went wrong. Distinguish an implicit condition, a missing stated prerequisite and an unavoidable subject question. Choose the inquirer for this question; profession, competence, assignment and amendment authority remain distinct.
3. **Compare a meaning-preserving alternative.** Make an implicit condition explicit, reduce an unnecessary demand or change the expression only where the suspected obstruction warrants that comparison. Hold task, prerequisites and assurance constant. Check the full connected passage under F.19; a shorter text that removes a needed condition has not preserved the method. Evaluate the attainable inquiry's burden under C.11.DUA.
4. **Qualify the evidence.** An expert walkthrough judges recovery from the public text; it is not an observed reader response. Preserve an actual reader's unassisted first attempt. A repeat after explanation is assisted and familiar, not another independent first reading or proof of reduced workload. Psychometric or causal conclusions require their own selected domain methods and data.
5. **Stop with the supported result.** Return a justified wording/content repair, no change, or the exact evidence limit and any worthwhile next question. The inquiry proposes; the applicable content/amendment authority decides. Use E.9 for a substantive FPF decision and its lighter wording route for ordinary editorial repair. Neither a role title nor a DRR implements or authorizes an amendment by itself.

#### E.12:4.4 - A result-reuse passage examined at equal conditions

The actual E.11.PUR §4.2.1 asks whether an earlier result answers the present concern, using the direct result pattern to compare its EntityOfConcern/edition, question/use, source/dependency conditions and qualification/currentness boundary. It then says: “When those values still match, cite and use the earlier result.” Its following instructions retain any needed A.10 reliance and G.11 currentness account, and reopen the smallest affected result question when a value changes.

For the same task and prerequisites, compare that connected passage with this alternative sentence: “Cite and reuse the earlier result only when its subject and edition, question and use, relied sources and dependencies, and qualification/currentness still answer the present concern.” Keep the surrounding reliance and reopen rules in both versions. This makes the antecedent explicit without relaxing any assurance condition.

An expert walkthrough can recover all four comparison duties from the actual passage's preceding list; on that basis alone, no change is required. No reader observation or workload measurement is asserted by this example. If an actual initial attempt instead misses the reuse condition, retain that response and examine whether the explicit alternative repairs that miss. If the reader lacks an expressly required subject prerequisite, or the difficult step is deciding whether the source remains applicable, making the sentence shorter does not justify deleting that condition. A second attempt after explaining the list can support only a qualified assisted-reading result. Stop at the demonstrated repair, no-change result or exact limit of that comparison.


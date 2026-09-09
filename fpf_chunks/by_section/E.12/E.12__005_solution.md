---
chunk_kind: "child"
pattern_id: "E.12"
pattern_title: "Didactic Primacy & Cognitive Ergonomics"
section_id: "E.12:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.12/E.12__005_solution.md"
commit_sha: "f4bad21274b54b57071afb2210a8bdb9f61a1c95"
heading_path:
  - "E.12 — Didactic Primacy & Cognitive Ergonomics"
  - "E.12:4 — Solution"
line_start: 80983
line_end: 81011
dependencies:
  - "E.13"
  - "E.2"
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

The primary purpose of the FPF is to enhance the cognitive capabilities (`U.Capability`/`Mastery`) of a reasoning system, team, organization, or other acting holon in service of its objectives. The creation of assurance-bearing epistemes or publications with high assurance levels and epistemic scores is a *means to that end, not the end itself*. Any architectural decision that increases formal rigor at the cost of clarity or usability must be explicitly justified by a demonstrable gain in that holder's ability to reason effectively.

#### E.12:4.2 - Mechanism 1: The Rationale Mandate

Every key assurance episteme or publication (such as a `U.AssuranceCase` or `Proof`) **MUST** contain a mandatory, human-readable **`rationale`** component.

*   **Nature:** The `rationale` is a narrative explanation of the cognitive benefit.
*   **Content:** It **MUST** answer the question: *"How does achieving this level of formal assurance tangibly help the agent better understand the problem or make a more reliable decision?"*
*   **Purpose:** This mandate requires the author to explain how the formal assurance serves its pragmatic, cognitive purpose. An empty or perfunctory rationale indicates that the assurance work may be an exercise in formalism for its own sake.

> **Didactic Note for Managers: The "So What?" Test**
>
> The Rationale Mandate is FPF's built-in "So What?" test. When your team presents a complex, formally checked episteme or publication (`AssuranceLevel:L2`), the `rationale` is where they answer your fundamental question: "This is impressive, but *so what*? How does this help us ship a better product, make a smarter investment, or avoid a critical risk?" If the answer isn't clear and compelling in the `rationale`, the formal work may have been a waste of resources. Use this question to keep the team's formal work focused on the value it is meant to create.

#### E.12:4.3 - Mechanism 2: The Human-Factor Loop (HF-Loop)

To provide a continuous, self-correcting mechanism against cognitive overload, FPF introduces a conceptual feedback loop.

*   **Core Concept:** The HF-Loop is a formal method of inquiry designed to distinguish between the *essential complexity* of the problem being solved and the *incidental complexity* introduced by the FPF itself.
*   **Trigger Concept:** A review is triggered when the **subjective cognitive workload**—the perceived mental effort required to use FPF's concepts and structures—exceeds a conceptual threshold.
*   **Review Concept:** When triggered, a formal review is conducted by individuals in roles that specialize in human-centric perspectives, such as the **`Ethicist`** and **`UX Design Critic`**.
*   **Output Concept:** The review produces a set of proposed **conceptual simplifications** or **didactic improvements** to the framework's patterns. These are then submitted as formal change proposals (DRRs).


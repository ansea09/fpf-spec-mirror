---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__005_solution.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:4 — Solution"
line_start: 20452
line_end: 20507
dependencies:
  - "A.12"
  - "A.2"
  - "A.2.1"
  - "C.9"
  - "E.16"
keywords:
  - "agency as role"
  - "agency spectrum"
  - "autonomy grading"
  - "contextual role assignment"
  - "substrate-neutral autonomy"
---

### A.13:4 - Solution

FPF's solution is threefold: it defines agential participation via `U.RoleAssignment` (A.2.1), makes agency measurable with a dedicated Characterization, and provides a didactic summary via a graded scale.

#### A.13:4.1 - The Core Definition: Agential participation as contextual role assignment

An ordinary-language **"agent"** in FPF is not a fundamental type. When the term is admitted, it is a convenience term (a Register 1 / Register 2 label) for a specific **Contextual Role Assignment (`U.RoleAssignment`)**:

> `AgentialParticipation ≍ U.RoleAssignment(holderRef: U.System, roleRef: AgentialRole@Context, boundedContextRef: U.BoundedContext)`

This means the acting holder is a **`U.System`** that currently bears **`AgentialRole@Context`** within a specific **`U.BoundedContext`**.

*   **No root Agent kind:** To be clear, FPF does not add a base kind for "agent" beside `U.System` and `U.Episteme`. This avoids type inflation and preserves the dynamic nature of roles.
*   **Epistemes Cannot Hold Work-Facing Agential Roles:** As the `holderRef` must name a `U.System`, this definition constitutionally forbids `U.Episteme`s from being acting holders, preventing the "episteme-as-actor" category error.
*   **Canonical Syntax:** The technical notation is `System#AgentialRole:Context`.

#### A.13:4.2 - The `AgentialRole` and its Specializations

*   **`AgentialRole@Context`:** This is the abstract role value for goal-directed action within a context. It is not a separate root kind.
*   **Specialized Roles:** More specific behavioral role values like `TransformerRole@Context` and `ObserverRole@Context` specialize `AgentialRole@Context`. They describe *what kind* of agential action is being performed at a given moment.
    *   A system holding `TransformerRole@Context` is currently modifying another holon.
    *   A system holding `ObserverRole@Context` is currently gathering information.
    This creates a clean role-value hierarchy: a `TransformerRole@Context` assignment is agential, but an agential assignment is not always transformational; it could be observing, planning, or idle.

#### A.13:4.3 - Measuring Agency: The Agency Characteristic Profile and the Spectrum

Agency is not a binary switch; it is a multi-dimensional spectrum of capabilities. FPF models this using **C.9 Agency Characteristic Profile**, a characterization pattern that attaches a set of measurable properties to a `U.RoleAssignment`.

The agency-characteristic profile is grounded in contemporary research (e.g., Active Inference, Basal Cognition) and includes the following key characteristics. Each is measured for a specific holder system in a specific context and must be backed by evidence (A.10).

1.  **Boundary Maintenance Capacity (BMC):** The ability of the system to maintain its structural and functional integrity against perturbations. *(How robust is it?)*
2.  **Predictive Horizon (PH):** The temporal or causal depth of the holder's internal model. *(How far ahead can it "see"?)*
3.  **Model Plasticity (MP):** The rate at which the agent can update its internal model (`U.GenerativeModel`) in response to prediction errors (`U.Error`). *(How quickly can it learn?)*
4.  **Policy Enactment Reliability (PER):** The probability that the agent will successfully execute its chosen `U.Method` under operational conditions. *(How reliably does it do what it decides to do?)*
5.  **Objective Complexity (OC):** A measure of the complexity of the `U.Objective` the holder can pursue, from simple set-points to abstract, multi-scale goals.

##### A.13:4.3.1 - Context-bounded task-family specialization claims

When work shifts to a new `TaskFamily`, describe the holder as acquiring **context-bounded task-family specialization** rather than as becoming more generally intelligent in the abstract. The same holder may carry different task-family specializations across different task families without becoming a new U-kind. Breadth across unrelated task families is not the adaptation-signature claim here; the adaptation-signature claim is **time-to-usable specialization** on the declared task family and work target under a named work-measure threshold, adaptation budget, and freshness or provenance basis.

Low-human-overlap or newly discovered task families remain admissible when the task family, evidence basis, and reuse window are explicit by value.

#### A.13:4.4 - The Agency Grade (Didactic Layer)

While the multi-dimensional agency-characteristic profile is essential for formal assurance, engineers and managers need a simpler, at-a-glance summary. The **Agency Grade** is a **non-normative, didactic** scale from 0 to 4 that synthesizes the profile into an intuitive autonomy grade.

| Grade | Label | Typical agency-characteristic profile (Conservative Lower Bound) | Archetypal Example |
| :--- | :--- | :--- | :--- |
| **0** | **Non-Agential** | `BMC ≈ 0`, `PH ≈ 0`, `MP ≈ 0` | A rock, a document, a passive structural component. |
| **1** | **Reactive** | `BMC > 0`, `PH ≈ 0`, `MP ≈ 0` | A thermostat; a simple feedback controller. Follows fixed rules. |
| **2** | **Predictive** | `BMC > 0`, `PH > 0`, `MP ≈ 0` | A model-predictive controller with a fixed model; a chess engine that plans moves but doesn't learn new strategies. |
| **3** | **Adaptive** | `BMC > 0`, `PH > 0`, `MP > 0` | A self-calibrating sensor system; a machine learning agent that updates its model with new data. |
| **4** | **Reflective/Strategic** | High `BMC`, `PH`, `MP`, `PER`, and `OC`. Capable of meta-cognition (reasoning about its own reasoning) and pursuing abstract goals. | An autonomous R&D system; a cohesive, self-organizing DevOps team. |

**Crucial Distinction:** The agency-characteristic profile is the **normative evidence**. The Grade is a **pedagogical shortcut**. A holder cannot claim an Agency Grade without having a corresponding, auditable characteristic profile to back it up.


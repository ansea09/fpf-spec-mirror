---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__005_solution.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:4 — Solution"
line_start: 24115
line_end: 24166
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "C.16"
  - "C.9"
  - "E.16"
  - "F.6"
keywords:
  - "autonomy grading"
  - "classification"
  - "conditional characteristic profile"
  - "evidence-backed core"
  - "exact System"
  - "local agential system-role kind and criterion"
  - "obtaining assignment"
  - "scope"
  - "window"
  - "working situation"
---

### A.13:4 - Solution

FPF's solution is threefold: establish agential participation through an obtaining system-role assignment, measure agency with a dedicated Characterization, and provide a didactic summary through a graded scale.

#### A.13:4.1 - The Core Definition: Agential participation through an exact system-role assignment

An ordinary-language **"agent"** is not a fundamental FPF type. When a precise agency claim is needed, name four things:

1. the acting holder recognized as a `U.System`;
2. the exact local agential system-role kind whose membership criterion the holder satisfies;
3. an occurrence of a directly declared `U.SystemRoleAssignment` species that assigns that kind to the holder and actually obtains; and
4. any claim scope, working situation, and time window needed by the intended use, kept separate from the assignment's identity.

This keeps a useful ordinary word without creating a universal `Agent` or `AgentialRole` kind. Classification by the local kind does not by itself establish an assignment or performed Work. Because the holder must be a `U.System`, an episteme cannot become the acting holder of this assignment.

#### A.13:4.2 - Local Agential System-Role Kinds and Their Specializations

*   **Local agential system-role kind:** A practice or source may define a local kind whose stable work-facing contribution is goal-directed action. The kind classifies candidate Systems under its own criterion; it is not a universal root kind, an assignment occurrence, or Work.
*   **Specialized agential system-role kinds:** A local practice may distinguish transformation, observation, planning, or another contribution when it supplies a real criterion for the distinction. An assignment to one such kind establishes only that assignment; any transformation, observation, plan, or performed Work still needs its own claim.

#### A.13:4.3 - Measuring Agency: The Agency Characteristic Profile and the Spectrum

Agency is not a binary switch; it is a multi-dimensional spectrum of capabilities. A.13 defines the current domain profile and attaches its measurable characteristics to the exact holder and agency claim; A.17, A.18, A.19, C.16, and A.10 govern characterization, measurement, and evidence. Planned **C.9 Agency Characteristic Profile** may later consolidate that profile but supplies no current definitions or governing force.

The agency-characteristic profile is grounded in contemporary research (e.g., Active Inference, Basal Cognition) and includes the following key characteristics. Each measurement names its exact holder and, where relevant, its task family or work target, claim scope, working situation, and time window; A.10 supplies the evidence basis.

1.  **Boundary Maintenance Capacity (BMC):** The ability of the system to maintain its structural and functional integrity against perturbations. *(How robust is it?)*
2.  **Predictive Horizon (PH):** The temporal or causal depth of the holder's internal model. *(How far ahead can it "see"?)*
3.  **Model Plasticity (MP):** The rate at which the agent can update its internal model (`U.GenerativeModel`) in response to prediction errors (`U.Error`). *(How quickly can it learn?)*
4.  **Policy Enactment Reliability (PER):** The probability that the agent will successfully execute its chosen `U.Method` under operational conditions. *(How reliably does it do what it decides to do?)*
5.  **Objective Complexity (OC):** A measure of the complexity of the `U.Objective` the holder can pursue, from simple set-points to abstract, multi-scale goals.

##### A.13:4.3.1 - Task-family specialization claims

When Work shifts to a new `TaskFamily`, describe evidence-backed specialization for that task family and work target rather than greater intelligence in general. Keep the task family, work target, claim scope, working situation, measurement window, work-measure threshold, adaptation budget, and provenance basis as separate values. The same holder may show different specializations for different task families without becoming a new U-kind; the claim here is **time-to-usable specialization** for the stated task family and target.

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


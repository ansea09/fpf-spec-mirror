---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__006_solution.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:4 — Solution"
line_start: 24308
line_end: 24359
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

Establish the agency core first. Add the characteristic profile when the receiving claim requires it; use a Grade only as its didactic summary.

#### A.13:4.1 - The Core Definition: Agential participation through an exact system-role assignment

An ordinary-language **"agent"** is not a fundamental FPF type. When a precise agency claim is needed, name four things:

1. the acting holder recognized as a `U.System`;
2. the exact local agential system-role kind whose membership criterion the holder satisfies;
3. an occurrence of a directly declared `U.SystemRoleAssignment` species that assigns that kind to the holder and actually obtains; and
4. any claim scope, working situation, and time window needed by the intended use, kept separate from the assignment's identity.

This keeps a useful ordinary word without creating a universal `Agent` or `AgentialRole` kind. Classification by the local kind does not establish an assignment or performed Work. An episteme cannot be this assignment’s holder because the holder must be a `U.System`. Evidence supports the core facts independently of any profile; a characteristic-only claim about an admitted System need not add an assignment.

#### A.13:4.2 - Local Agential System-Role Kinds and Their Specializations

*   **Local agential system-role kind:** A practice or source may define a local kind whose stable work-facing contribution is goal-directed action. The kind classifies candidate Systems under its own criterion; it is not a universal root kind, an assignment occurrence, or Work.
*   **Specialized agential system-role kinds:** A local practice may distinguish transformation, observation, planning, or another contribution when it supplies a real criterion for the distinction. An assignment to one such kind establishes only that assignment; any transformation, observation, plan, or performed Work still needs its own claim.

#### A.13:4.3 - Measuring Agency: The Agency Characteristic Profile and the Spectrum

The agency-characteristic profile describes distinct capabilities of the holder. Use it for a consumed Grade/autonomy/profile claim, a characteristic-dependent local criterion or a named assurance use that requires it. A.13 defines this domain profile; A.17, A.18, A.19, C.16 and A.10 govern characterization, measurement and evidence.

The following descriptions state what the five characteristics concern. A measured value also needs its declared characteristic definition, scale, measurement method and evidence basis under the patterns above. Each measurement names its holder and, where relevant, task family or work target, claim scope, situation and time window. A.10 governs the claim’s evidence and provenance.

1. **Boundary Maintenance Capacity (BMC):** The ability of the System to maintain its own structural and functional integrity against perturbations. The maintained property is the holder’s integrity, not merely the value it controls.
2. **Predictive Horizon (PH):** The temporal or causal depth of the holder’s internal model. State which depth the claim uses; the horizon is distinct from prediction accuracy.
3. **Model Plasticity (MP):** The rate at which the holder can update its internal model (`U.GenerativeModel`) in response to prediction errors (`U.Error`). Describe the model update and its rate; evaluate capability acquisition separately under E.10.LRN.
4. **Policy Enactment Reliability (PER):** The probability that the holder will successfully execute its chosen `U.Method` under operational conditions. The event is successful Method execution; a result or safety claim needs its own basis.
5. **Objective Complexity (OC):** A measure of the complexity of the `U.Objective` the holder can pursue, from simple set-points to abstract, multi-scale goals. These examples distinguish objectives; a complexity comparison needs a declared criterion and scale.

##### A.13:4.3.1 - Task-family specialization claims

When assessing a holder’s **time-to-usable specialization**, name the holder, `TaskFamily` and work target. Use C.22 for the task anchor and C.22.1 for adaptation time or budget to the declared work-measure threshold. Keep task family, work target, claim scope, situation, measurement window, threshold, adaptation budget and provenance basis distinct where the claim uses them. The same holder can show different specializations for different task families; this does not establish greater intelligence in general or a new U-kind.

Low-human-overlap or newly discovered task families remain admissible when the task family, evidence basis, and reuse window are explicit by value.

#### A.13:4.4 - The Agency Grade (Didactic Layer)

Engineers and managers can use the **Agency Grade** as a **non-normative, didactic** summary of a profile. The scale runs from 0 to 4; an assurance use that consumes agency characteristics needs their supported values, not this summary.

| Grade | Label | Typical agency-characteristic profile (Conservative Lower Bound) | Archetypal Example |
| :--- | :--- | :--- | :--- |
| **0** | **Non-Agential** | `BMC ≈ 0`, `PH ≈ 0`, `MP ≈ 0` | A rock, a document, a passive structural component. |
| **1** | **Reactive** | `BMC > 0`, `PH ≈ 0`, `MP ≈ 0` | A thermostat; a simple feedback controller. Follows fixed rules. |
| **2** | **Predictive** | `BMC > 0`, `PH > 0`, `MP ≈ 0` | A model-predictive controller with a fixed model; a chess engine that plans moves but doesn't learn new strategies. |
| **3** | **Adaptive** | `BMC > 0`, `PH > 0`, `MP > 0` | A self-calibrating sensor system; a machine learning agent that updates its model with new data. |
| **4** | **Reflective/Strategic** | High `BMC`, `PH`, `MP`, `PER`, and `OC`. Capable of meta-cognition (reasoning about its own reasoning) and pursuing abstract goals. | An autonomous R&D system; a cohesive, self-organizing DevOps team. |

The profile states characteristic claims and their supporting evidence; the Grade is a pedagogical summary. A claim about a holder’s Agency Grade requires a corresponding auditable profile under CC-A13.3. The Grade remains unavailable as a normative premise under CC-A13.4.


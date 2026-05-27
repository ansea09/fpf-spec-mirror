---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__005_solution.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:4 — Solution"
line_start: 32422
line_end: 32449
dependencies:
  - "A.12"
  - "A.4"
  - "B.4.1-B.4.3"
keywords:
  - "DesignRunTag feedback"
  - "drift repair"
  - "evolution loop"
  - "observe-notice-stabilize-route"
  - "open-ended evolution"
---

### B.4:4 - **Solution**

FPF defines the **Canonical Evolution Loop**, a four-phase cycle that serves as the universal engine for all principled, open-ended evolution. This loop is a direct implementation of the **Explore → Shape → Evidence → Operate** state machine (Pattern B.5.1) and is powered by the **Canonical Reasoning Cycle** (Pattern B.5).

The loop creates a closed, auditable circuit between the two temporal scopes. Crucially, transitions between phases are performed by an **external `Transformer`** (Pattern A.12). A holon does not evolve itself; it is evolved by an external agent acting upon it.

*A diagram showing a cycle: Operate (Run-time) → Observe (Run-time to Design-time bridge, performed by a Transformer) → Refine (Design-time) → Deploy (Design-time to Run-time bridge, performed by a Transformer) → Operate.*

**The Four Phases of the Loop:**

| Phase | Core Activity | Role of the External `Transformer` | Key FPF Patterns Used |
| :--- | :--- | :--- | :--- |
| **1. Operate** | The holon exists in its `run-time` context, fulfilling its purpose. | **The `Transformer` observes the holon.** It does not act *on* it, but gathers data about its performance or state. For a `U.System`, this could be a sensor. For a `U.Episteme`, this could be a researcher applying the theory and noting its predictions. | `A.4 Temporal Duality` |
| **2. Observe** | The `Transformer` compares the observed reality with an expected model, identifying an **anomaly** or an **opportunity**. This is the bridge from `run-time` back to `design-time`. | **The `Transformer` generates a new insight.** Based on the observation, the `Transformer` (e.g., the research team, an automated analysis system) formulates a new hypothesis about how to improve the holon. | `B.5.2 Abductive Loop`, `A.10 Evidence Graph Referring` |
| **3. Refine** | The `design-time` model of the holon is updated by the `Transformer`. A new hypothesis is shaped (Deduction) and tested against evidence (Induction). | **The `Transformer` modifies the blueprint.** It alters the `design-time` episteme—the specification, the theory, the source code—to incorporate the new insight. | `B.5 Canonical Reasoning Cycle`, `B.3 Trust & Assurance Calculus` |
| **4. Deploy** | The `Transformer` instantiates the refined `design-time` model as a new `run-time` version of the holon. This is the bridge that carries improvements from the blueprint back into the real world. | **The `Transformer` builds and releases the new version.** This could be a compiler building new software, a 3D printer creating a new physical part, or an editor publishing a revised version of a scientific paper. | `A.3 Transformer Constitution`, `A.4 Temporal Duality` |

> **Didactic Note: The "Learn and Adapt" engine**
>
> The Canonical Evolution Loop is a formal account of repeated adaptation. It keeps four durable questions explicit:
>
> 1.  **Operate:** "What is the holon doing in use or in the field?"
> 2.  **Observe:** "What anomaly, opportunity, or mismatch is now visible to a responsible `Transformer`?"
> 3.  **Refine:** "What design-time change would better fit what has been observed?"
> 4.  **Deploy:** "How is that refined design-time content instantiated back into run-time reality?"
>
> The point is not managerial uplift. The point is to keep adaptation legible: every refinement has an observed basis, an external `Transformer`, and an auditable return from design-time into run-time.


---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__005_solution.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:4 — Solution"
line_start: 39669
line_end: 39696
dependencies:
  - "A.12"
  - "A.4"
  - "B.4.1"
keywords:
  - "DesignRunTag feedback"
  - "drift repair"
  - "evolution loop"
  - "knowledge refinement"
  - "method refinement"
  - "observe-notice-stabilize-route"
  - "open-ended evolution"
---

### B.4:4 - **Solution**

FPF defines the **Canonical Evolution Loop**, a four-phase cycle that serves as the universal engine for all principled, open-ended evolution. This loop is a direct implementation of the **Explore → Shape → Evidence → Operate** state machine (Pattern B.5.1) and is powered by the **Canonical Reasoning Cycle** (Pattern B.5).

The loop creates a closed, auditable circuit between the two temporal scopes. Its phase changes are realized by dated Work performed by an admitted external acting System. Use F.6 to identify the assignment under which each performer acted; classify the System under `TransformerSystemRole@Context` only when that local distinction matters. A short loop account may omit an unused assignment identifier. The kind and assignment do not act: the admitted System performs the Work that changes the holon.

*A diagram showing a cycle: Operate (run-time) → observation Work performed by an admitted System (run-time to design-time bridge) → refinement Work performed by an admitted System (design-time) → deployment Work performed by an admitted System (design-time to run-time bridge) → Operate.*

**The Four Phases of the Loop:**

| Phase | Core activity | Work and performing System | Key FPF Patterns Used |
| :--- | :--- | :--- | :--- |
| **1. Operate** | The holon exists in its `run-time` context, fulfilling its purpose. | An admitted external System performs observation Work and records relevant performance or state. It may be, for example, a sensor System observing an operating `U.System`, or a researcher System applying a theory and recording its predictions. | `A.4 Temporal Duality` |
| **2. Observe** | Observation and comparison Work relates run-time records to an expected model and may identify an anomaly or opportunity. This is the bridge from `run-time` back to `design-time`. | A named research team or automated analysis System performs the comparison and hypothesis Work; the resulting insight or hypothesis is an episteme, not an act by a role label. | `B.5.2 Abductive Loop`, `A.10 Evidence Graph Referring` |
| **3. Refine** | Revision and testing Work changes the `design-time` episteme in response to the observed basis. | An admitted System performs the Work that changes the specification, theory, source code, or other design-time description. | `B.5 Canonical Reasoning Cycle`, `B.3 Trust & Assurance Calculus` |
| **4. Deploy** | Build, release, installation, or publication Work carries the refined design-time content toward renewed run-time use. | An admitted System performs that Work. The resulting version, its acceptance or admission, and later use remain separate facts rather than actions by a `Transformer` label. | `A.3 Transformer Constitution`, `A.4 Temporal Duality` |

> **Didactic Note: The "Learn and Adapt" engine**
>
> The Canonical Evolution Loop is a formal account of repeated adaptation. It keeps four durable questions explicit:
>
> 1.  **Operate:** "What is the holon doing in use or in the field?"
2.  **Observe:** "What anomaly, opportunity, or mismatch is now visible through observation Work performed by an admitted external System?"
> 3.  **Refine:** "What design-time change would better fit what has been observed?"
> 4.  **Deploy:** "How is that refined design-time content instantiated back into run-time reality?"
>
> The point is not managerial uplift. The point is to keep adaptation legible: every refinement has an observed basis, named Systems and dated Work, and an auditable return from design-time into run-time.


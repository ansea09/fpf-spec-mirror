---
chunk_kind: "child"
pattern_id: "B.5"
pattern_title: "Canonical Reasoning Cycle"
section_id: "B.5:5"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5/B.5__006_conformance-checklist.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "B.5 — Canonical Reasoning Cycle"
  - "B.5:5 — Conformance Checklist"
line_start: 32810
line_end: 32827
dependencies:
  - "A.10"
  - "B.4"
  - "B.5.x"
keywords:
  - "Abduction-Deduction-Induction"
  - "problem-solving"
  - "reasoning"
  - "scientific method"
---

### B.5:5 - **Conformance Checklist**

To ensure the reasoning cycle is applied consistently and rigorously, the following criteria are normative:

*   **CC-B5.1 (Abductive Primacy):** Any discipline that introduces a new, non-derivable claim or design element into a working model **MUST** document it as an abductive step. The resulting claim or design element **SHALL** initially be assigned `AssuranceLevel:L0` as a hypothesis episteme or equivalent working-model element.
*   **CC-B5.2 (Deductive Mandate):** An abductively generated hypothesis **SHALL NOT** be subjected to inductive testing (Validation Assurance) until its key logical consequences have been derived and documented through a deductive process.
*   **CC-B5.3 (Inductive Grounding):** A claim **SHALL NOT** be promoted to `AssuranceLevel:L1` or higher on the basis of a successful inductive test unless that test is explicitly linked to a prediction derived in the deductive phase.
*   **CC-B5.4 (Cycle Closure):** The outcome of an inductive test (whether corroboration or refutation) **MUST** be formally recorded as an evidence carrier (Pattern A.10), and that evidence carrier **MUST** be used as an input for the next iteration of the reasoning cycle.
*   **CC-B5.5 (State Machine Alignment):** The Abductive–Deductive–Inductive Loop is the cognitive engine that drives state transitions in the **Explore → Shape → Evidence → Operate** state machine (Pattern B.5.1). Abduction dominates the *Explore* phase; Deduction dominates the *Shape* phase; and Induction is the core of the *Evidence* phase.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It |
| :--- | :--- | :--- |
| **The "Solution in Search of a Problem"** | A team builds a technically impressive feature (deduction/induction) but cannot clearly state what user problem it solves. | **CC-B5.1** forces the process to start with an abductive hypothesis that is explicitly framed as a solution to a stated problem or anomaly. |
| **The "Ready, Fire, Aim" Approach** | A team jumps directly from an idea to expensive prototyping and testing, without a clear model of what they expect to happen. | **CC-B5.2** mandates a deductive analysis phase *before* inductive testing. This ensures that every test is designed to confirm or refute a specific, well-defined prediction. |
| **The "Data Dredging" Exercise** | A team gathers massive amounts of data and looks for correlations, hoping a solution will emerge. | The cycle requires a hypothesis *first*. Data is gathered to test that hypothesis, not in the hope of stumbling upon one. This makes the process more focused and cost-effective. |


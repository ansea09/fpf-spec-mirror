---
chunk_kind: "child"
pattern_id: "B.5"
pattern_title: "Canonical Reasoning Cycle"
section_id: "B.5:5"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5/B.5__006_conformance-checklist.md"
commit_sha: "aa10af7e8221518114822d00bb9cf11e6c41f6b2"
heading_path:
  - "B.5 — Canonical Reasoning Cycle"
  - "B.5:5 — Conformance Checklist"
line_start: 40952
line_end: 40969
dependencies:
  - "A.10"
  - "B.4"
  - "B.5"
keywords:
  - "Abduction-Deduction-Induction"
  - "problem-solving"
  - "reasoning"
  - "scientific method"
---

### B.5:5 - **Conformance Checklist**

To ensure the reasoning cycle is applied consistently and rigorously, the following criteria are normative:

*   **CC-B5.1 (Abductive Primacy):** Any discipline that introduces a new, non-derivable claim or design element into a working model **MUST** document it as an abductive step. The resulting claim or design element **SHALL** retain its conjectural status, grounds and limitations. An assurance level, when needed by a receiving use, **SHALL** follow B.3.3 rather than be assigned from its abductive origin.
*   **CC-B5.2 (Deductive Mandate):** An abductively generated hypothesis **SHALL NOT** be subjected to inductive testing (Validation Assurance) until its key logical consequences have been derived and documented through a deductive process.
*   **CC-B5.3 (Inductive Grounding):** A positive support claim based on an inductive test **MUST** link the actual result to the derived prediction and establish its relevance, coverage and limitations for the receiving claim. Passing a test **SHALL NOT** by itself assign an assurance level; an elected B.3.3 profile retains its applicable evidence criteria.
*   **CC-B5.4 (Cycle Closure):** The actual outcome of an inductive test (whether corroboration or refutation) **MUST** be recorded through an evidence carrier (Pattern A.10). If a further iteration relies on that result, it **MUST** use the recorded result with its scope and limitations. Recording a sufficient result does not itself require another iteration.
*   **CC-B5.5 (State Machine Alignment):** When the B.5.1 development cycle is used, abduction commonly contributes to *Exploration*, deduction to *Shaping*, and empirical evaluation to *Evidence*. Actual transitions **MUST** meet their applicable project and domain conditions. A completed reasoning contribution or sufficient bounded use is not by itself a project-state transition or an assurance level.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It |
| :--- | :--- | :--- |
| **The "Solution in Search of a Problem"** | A team builds a technically impressive feature (deduction/induction) but cannot clearly state what user problem it solves. | **CC-B5.1** forces the process to start with an abductive hypothesis that is explicitly framed as a solution to a stated problem or anomaly. |
| **The "Ready, Fire, Aim" Approach** | A team jumps directly from an idea to expensive prototyping and testing, without a clear model of what they expect to happen. | **CC-B5.2** mandates a deductive analysis phase *before* inductive testing. This ensures that every test is designed to confirm or refute a specific, well-defined prediction. |
| **The "Data Dredging" Exercise** | A team gathers massive amounts of data and looks for correlations, hoping a solution will emerge. | The cycle requires a hypothesis *first*. Data is gathered to test that hypothesis, not in the hope of stumbling upon one. This makes the process more focused and cost-effective. |


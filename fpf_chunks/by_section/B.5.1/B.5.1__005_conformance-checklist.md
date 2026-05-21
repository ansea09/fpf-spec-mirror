---
chunk_kind: "child"
pattern_id: "B.5.1"
pattern_title: "Explore → Shape → Evidence → Operate"
section_id: "B.5.1:4"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.1/B.5.1__005_conformance-checklist.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "B.5.1 — Explore → Shape → Evidence → Operate"
  - "B.5.1:4 — Conformance Checklist"
line_start: 31967
line_end: 31972
dependencies:
  - "B.5"
keywords:
  - "Evidence"
  - "Explore"
  - "Operate"
  - "Shape"
  - "development state cycle"
  - "open-ended progression"
  - "state machine"
---

### B.5.1:4 - **Conformance Checklist**

*   **CC-B5.1.1 (State Explicitness):** Every state-bearing `U.Episteme` or `U.System` in a project **MUST** be tagged with its current state from the set {Exploration, Shaping, Evidence, Operation}.
*   **CC-B5.1.2 (Sequential Progression):** A state-bearing `U.Episteme` or `U.System` **SHALL** progress through the states in sequence. Skipping a state (e.g., moving directly from Exploration to Evidence without Shaping) is a process violation and must be explicitly justified in the evidence carrier's rationale.
*   **CC-B5.1.3 (Reasoning Cycle Alignment):** The transition between states **MUST** be triggered by the completion of the corresponding phase of the Canonical Reasoning Cycle (Pattern B.5). For example, the transition from *Shaping* to *Evidence* requires the completion of the deductive analysis.


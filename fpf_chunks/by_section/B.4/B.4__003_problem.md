---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__003_problem.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:2 — Problem"
line_start: 40447
line_end: 40454
dependencies:
  - "A.12"
  - "A.15.1"
  - "A.4"
  - "B.3"
  - "B.4"
  - "B.4.1"
  - "B.5"
  - "B.5.1"
keywords:
  - "DesignRunTag feedback"
  - "drift repair"
  - "evolution loop"
  - "knowledge refinement"
  - "method refinement"
  - "observe-notice-stabilize-route"
  - "open-ended evolution"
---

### B.4:2 - **Problem**

Without a canonical, shared model for evolution, projects fall into predictable and costly failure modes:

1. **Design-Reality Divergence (The "Drift"):** The run-time subject in use slowly diverges from its design-time account. Formal models become elegant fictions, assurance cases become irrelevant, and the project loses the ability to reason reliably about what it uses.
2. **Learning Stagnation (The "Ivory Tower"):** Observation produces valuable findings, but no explicit change path carries them into a revised design or renewed use. "Lessons learned" remain static documents.
3. **Chaotic Change (The "Whack-a-Mole"):** Reactive patches have no stated observed basis, identity decision, or return-to-use condition. Hidden dependencies and unintended consequences accumulate.


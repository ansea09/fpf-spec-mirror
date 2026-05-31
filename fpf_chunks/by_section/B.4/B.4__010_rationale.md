---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__010_rationale.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:9 — Rationale"
line_start: 32031
line_end: 32036
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

### B.4:9 - **Rationale**

This pattern operationalizes the **Open-Ended Evolution Principle (P-10)** by providing its core engine. It is the FPF's formalization of proven iterative cycles like the Deming Cycle (Plan-Do-Check-Act) and the OODA Loop (Observe-Orient-Decide-Act), but it enriches them with the strong semantic distinctions of the FPF, such as `design-time` vs. `run-time` and the formal role of the external `Transformer`.

By making the `Transformer`'s role explicit in every phase, the pattern avoids the common conceptual error of treating systems or theories as if they evolve on their own. Evolution is always an *action* performed by an agent on a holon. This rigorous, externalist stance is critical for clear causal reasoning and auditable accountability. By making this loop canonical, FPF ensures that all holons within its ecosystem are not just designed and built, but are designed *to be evolved* in a principled, traceable manner.


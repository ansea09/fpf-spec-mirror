---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__007_bias-annotation.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:6 — Bias-Annotation"
line_start: 39755
line_end: 39762
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

### B.4:6 - **Bias-Annotation**

| Bias | Symptom | Correction |
| :--- | :--- | :--- |
| Self-evolution bias | The holon is said to observe, refine, or deploy itself, so the acting-side transformer disappears. | Name the external holder acting under `TransformerRole@Context`, even when that holder is an automated system. |
| Design-time/run-time smear | A live operational change is treated as if it had already updated the design-time episteme, or a design-time edit is treated as if it had already changed the holon in operation. | Keep the design-time episteme, run-time holon occurrence, deploy relation, and evidence relation distinct. |
| Method-as-holon shortcut | A method update is described as if the method itself were the evolving holon. | Treat the method through `U.Method`, method description, work use, and evidence relations; use B.4 only when a holon-evolution claim is live. |


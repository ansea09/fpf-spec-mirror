---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__007_bias-annotation.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:6 — Bias-Annotation"
line_start: 21122
line_end: 21133
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
  - "E.8"
  - "U.WorkPlan"
keywords:
  - "P2W seam"
  - "WorkPlanning"
  - "edition pins"
  - "guard pins"
  - "planned baseline"
  - "planned filler"
  - "slot-bearing description"
  - "variance trail"
  - "Γ_time selector"
---

### A.15.3:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal**.

| Lens | Bias / limitation introduced by the pattern | Mitigation |
| --- | --- | --- |
| Gov | Baseline immutability and variance recording can be misread as bureaucracy rather than epistemic hygiene. | Keep the baseline minimal; use suite-specialized refinements only when a suite description truly requires them. |
| Arch | Enforces a clean P2W seam and discourages “configuration hidden in mechanisms”. This can expose underspecified slot-maintenance assignments earlier. | Treat that friction as an architectural signal; refine the slot-maintenance interface rather than hiding choices in prose. |
| Onto/Epist | Biases toward explicit context/time/edition pinning; exploratory reasoning may feel constrained. | Use minimal variants (context + rows + time selector) for exploration; graduate to pinned editions only when reproducibility is required. |
| Prag | Increases upfront authoring cost (explicit context, time, edition pins). | Use derived indices as projections for reader navigation; avoid duplicating content on views/cards. |
| Did | Biases against “one true card” habits by treating views as projections; may clash with existing documentation culture. | Provide a TechCard/PlainView projection explicitly, but keep the PlanItem as the governing work-plan record. |


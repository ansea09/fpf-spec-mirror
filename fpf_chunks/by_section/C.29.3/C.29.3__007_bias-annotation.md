---
chunk_kind: "child"
pattern_id: "C.29.3"
pattern_title: "Computational Realization"
section_id: "C.29.3:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.3/C.29.3__007_bias-annotation.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.29.3 — Computational Realization"
  - "C.29.3:6 — Bias-Annotation"
line_start: 61174
line_end: 61183
dependencies:
  - "A.3.3"
  - "A.6.1"
  - "B.5.MPC"
  - "C.16"
  - "C.29.2"
keywords:
---

### C.29.3:6 - Bias-Annotation

| Bias | Action-changing consequence | Correction |
| --- | --- | --- |
| A correct program is taken to settle its execution | A valid count is changed by preparation or readout. | Follow a required input through the actual encoding and interpretation. |
| Input and output are assumed to use one scale | The analog sum is read as half its value. | Derive the output interpretation from the executing relation. |
| Logical atomicity is projected onto physical actions | Reservations and unfinished returns are counted as occupants. | Represent the intermediate states or establish why they leave the required property intact. |
| Local success hides a shared resource | Two locally correct stocks exceed one room's capacity. | Recover the common stock or state and how each participant changes it. |
| Numerical precision dominates the account | Command-rounding error hides a larger physical uncertainty. | Express the consequential losses in the receiving quantity before selecting a refinement. |


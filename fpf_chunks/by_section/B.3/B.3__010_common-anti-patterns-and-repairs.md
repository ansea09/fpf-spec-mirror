---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus"
section_id: "B.3:8"
section_title: "Common anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__010_common-anti-patterns-and-repairs.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "B.3 — Trust and Assurance Calculus"
  - "B.3:8 — Common anti-patterns and repairs"
line_start: 38971
line_end: 38983
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.6"
keywords:
---

### B.3:8 - Common anti-patterns and repairs

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Universal weakest-link formula | `min` can be an upper bound for a conjunction and can ignore alternatives or dependence. | Use the exact dependency model and domain rule; otherwise report inputs separately. |
| Ordinal penalty subtraction | An ordinal label is subtracted from a probability or ratio quantity. | Use a calibrated mapping to the same quantity when one exists, or keep the values separate. |
| Formality raises assurance | A more formal wrong model receives a better result. | State the inspectability gain and the uncertainty it closes; keep truth and empirical adequacy separate. |
| Same letter, different property | `R` names system reliability in one row and evidence quality in another. | Give each characteristic its own bearer and definition. |
| Safety-case inflation | A warning, access value, or consequential display triggers a generic B.3 package. | Use the direct domain pattern; apply B.3 only to an actual assurance claim. |
| Evidence creates truth | New evidence is said to make the target fact obtain. | Revise the warrant or disposition unless the world-side facts changed. |
| Assessment-record collapse | A checklist, trace, witness, or note is treated as the assessment Work or result. | Identify each object separately and add only what the use consumes. |
| Design/run chimera | Blueprint evidence and runtime observations are merged into one score. | Produce separate results and compare them. |


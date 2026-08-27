---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__010_consequences.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:9 — Consequences"
line_start: 42431
line_end: 42440
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.21"
  - "A.6.3.RT"
  - "B.1.3"
  - "B.3"
  - "B.3.3"
  - "B.3.4"
  - "C.16"
  - "C.2"
  - "C.2.3"
  - "C.21"
  - "C.29"
  - "C.3"
  - "C.3.3"
  - "C.3.A"
  - "E.14"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.2"
  - "G.6"
  - "G.7"
keywords:
  - "ClaimScope (G)"
  - "Congruence Level (CL / CL^k / CL^plane)"
  - "F–G–R"
  - "Reliability (R)"
  - "TA/VA/LA lanes"
  - "direct relation"
  - "evidence-bound"
  - "no implicit averaging"
  - "pathwise justification (PathId)"
  - "warrant"
  - "weakest-link"
---

### C.2.2:9 - Consequences

Informative; non-binding.

| Benefits                                                                                                     | Trade-offs and mitigations                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Comparability.** Different claims can be compared in a disciplined way when F and G are explicit.          | **Conservatism.** Weakest-link propagation can feel pessimistic; mitigate by making support structure explicit and improving the weakest evidence. |
| **Auditability.** Relation-specific reuse loss is visible and localised to R.                                | **Overhead.** Declaring the relations actually traversed and the evidence links is work; mitigate with templates and reuse of standard lane schemas. |
| **Upgradeable knowledge.** R can improve incrementally as evidence accumulates, without rewriting the claim. | **Scalar temptation.** People still want one number; mitigate by requiring lane breakdown visibility behind the number.                            |


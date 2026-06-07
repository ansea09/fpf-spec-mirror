---
chunk_kind: "child"
pattern_id: "B.5.3"
pattern_title: "Role-Projection Bridge"
section_id: "B.5.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.3/B.5.3__003_problem.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "B.5.3 — Role-Projection Bridge"
  - "B.5.3:2 — Problem"
line_start: 33610
line_end: 33617
dependencies:
  - "A.2"
  - "C.3"
keywords:
  - "concept bridge"
  - "domain-specific vocabulary"
  - "mapping"
  - "terminology"
---

### B.5.3:2 - **Problem**

How can FPF bridge this gap between its universal core and the specific language of a domain without either polluting the kernel with domain-specific terms or forcing experts to abandon their familiar vocabulary? A simple alias mechanism (e.g., a dictionary mapping `U.System` to "Thermodynamic System") is insufficient because:

1.  **It's brittle:** It assumes a one-to-one mapping, which often breaks down. A single domain concept can play multiple universal roles in different contexts.
2.  **It's semantically poor:** It only captures naming, not the rich constraints and relationships that a domain-specific concept entails. We can't express that a "Thermodynamic System" is a *special kind* of `U.System` with specific properties related to temperature and pressure.
3.  **It's not integrated:** The mappings live outside the formal model, making them difficult to govern, version, and use in automated reasoning.


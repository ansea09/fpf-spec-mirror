---
chunk_kind: "child"
pattern_id: "B.3.3"
pattern_title: "Assurance Subtypes & Levels"
section_id: "B.3.3:6"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.3/B.3.3__007_consequences.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "B.3.3 — Assurance Subtypes & Levels"
  - "B.3.3:6 — Consequences"
line_start: 38069
line_end: 38076
dependencies:
  - "A.10"
  - "A.19"
  - "A.4"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.2.1"
  - "D.4"
  - "U.Episteme"
keywords:
  - "L0-L2"
  - "LA"
  - "TA"
  - "VA"
  - "assurance levels"
  - "typing"
  - "validation"
  - "verification"
---

### B.3.3:6 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Objective Gatekeeping:** The rules provide a clear, objective, and falsifiable basis for an assurance target's assurance status, eliminating subjective judgment and "assurance theater." | **Risk of Over-stringency:** The rules might feel too strict for rapid prototypes. *Mitigation:* The requirements for `L1` are deliberately lightweight, demanding only one piece of evidence and basic typing, making the first evidence-support transition accessible. |
| **Balanced Assurance:** The Standard requires a mix of evidence types for higher levels, preventing teams from over-investing in one area (e.g., testing) while neglecting another (e.g., formal specification). | **Risk of Evidence Inflation:** Teams might add trivial evidence just to meet the criteria. *Mitigation:* The quality of evidence is assessed via the epistemic scores (FV, EV, CL); merely linking to low-quality evidence will not significantly raise the scores needed for L2. |
| **Clear Progress Tracking:** The assurance-level progression provides a clear roadmap for maturing an assurance target from an idea to a fully assured component, making planning and progress monitoring transparent. | **Overhead for Complex Holons:** A holon with many ToAs may require significant assurance work. *Mitigation:* The framework allows grouping, where a parent claim's evidence can satisfy the coverage requirements for its children if explicitly declared. |


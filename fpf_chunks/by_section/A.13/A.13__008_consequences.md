---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__008_consequences.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:7 — Consequences"
line_start: 22933
line_end: 22941
dependencies:
  - "A.10"
  - "A.12"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "C.16"
  - "C.9"
  - "E.16"
keywords:
  - "U.SystemRoleAssignment"
  - "agency spectrum"
  - "agential participation"
  - "autonomy grading"
  - "local system-role kind"
  - "substrate-neutral autonomy"
---

### A.13:7 - Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Category Safety & Clarity:** The pattern provides a clear, unambiguous definition of agency that prevents common modeling errors and is consistent across all of FPF. | **Increased Modeling Granularity:** Requires practitioners to distinguish the local system-role kind, classification, obtaining assignment, and any performed Work, and to state scope or window only when it changes the claim. *Mitigation:* Use the short ordinary-language claim first; expose identifiers only when a receiving use needs them. |
| **Falsifiable & Measurable Agency:** By grounding agency in the agency-characteristic profile, the framework transforms a vague philosophical concept into a set of concrete, evidence-backed engineering properties. | **Measurement Effort:** Populating the profile requires real work (testing, analysis, data gathering). *Mitigation:* The profile can be built iteratively. An initial estimate can be used, with the understanding that its `Reliability (R)` score is low until backed by evidence. |
| **Scalable Autonomy Model:** The graded scale provides a sophisticated language for describing and comparing different Agency Grades, from simple automation to strategic intelligence. | **Risk of Misinterpreting Grades:** The simple 0-4 scale could be misused as a simplistic marketing label. *Mitigation:* The normative requirement (**CC-A13.4**) to always link a grade to its underlying CHR profile acts as a guardrail against this. |
| **Elegant Handling of Collectives:** The pattern provides a clean way to model the agency of teams, swarms, and organizations without violating ontological principles. | - |


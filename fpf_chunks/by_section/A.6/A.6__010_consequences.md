---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__010_consequences.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:9 — Consequences"
line_start: 10568
line_end: 10576
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
  - "U.View"
keywords:
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "Work versus non-Work effect"
  - "acceptance"
  - "actual occurrence"
  - "and evidence"
  - "atomic L/A/D/E claims"
  - "delivery"
  - "in invariants"
  - "publication face"
  - "reference predicate IDs from CC when needed"
  - "separate result"
  - "signature and mechanism declarations"
  - "six-way authority-word branch"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:9 - Consequences

| Benefits                                                                                                           | Trade‑offs / Mitigations                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **Evolvable boundaries.** Implementations can change while signatures remain stable.                               | More upfront structure; mitigated by MVPK faces that present only relevant slices per audience. |
| **Reduced category mistakes.** Object, description, and carrier confusion becomes detectable.                            | Requires discipline in writing; mitigated by the “Where statements go” classification examples.        |
| **Auditability and reproducibility.** Effect claims name their exact Work, transformation, interaction, evaluation, or other actual occurrence and use evidence carriers only through the needed evidence relation. | Requires direct-occurrence and evidence relations to be designed; mitigated by a compact `AssuranceLane` evidence map. |
| **Clearer cross‑disciplinary communication.** Legal and compliance deontics no longer compete with math invariants.    | Teams must align on viewpoint responsibilities; mitigated by explicit viewpointRef in MVPK.     |


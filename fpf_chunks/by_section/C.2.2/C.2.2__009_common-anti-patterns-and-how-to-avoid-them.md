---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "14f263bd90d449803a2ec6cb57ee7f620cc41bed"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 43330
line_end: 43343
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

### C.2.2:8 - Common Anti-Patterns and How to Avoid Them

Informative; non-binding.

| Anti-pattern               | Symptom                                                                                       | Why it fails                                                     | How to avoid / repair                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Unsupported assurance fold** | A mean, minimum, maximum, or weighted sum is reported as confidence without its model | Boundedness and monotonicity do not warrant the input scale or dependency interpretation | Identify support roles and a justified receiving model; otherwise return separate support and a bounded synthesis. |
| **Truth-by-score**         | `R=0.9` is treated as “the claim is true.”                                                    | R is warrant strength, not ontological truth.                    | Require explicit evidence links and scope; treat R as decision warrant only.                             |
| **Scope laundering**       | The claim’s applicability grows by wording changes while `G` is unchanged.                    | It silently widens scope, making comparisons meaningless.        | Use A.2.6 operators and treat scope changes as explicit revisions.                                       |
| **Relation laundering**    | A claim or its evidence is reused after a changed scope, kind, plane, notation, local meaning, model use, or evidence basis, while `R` is carried over unchanged. | It hides the actual change and its relation-specific loss. | Name the direct relation or scope operation and recompute `R_eff` from its declared loss; stop if that relation is missing. |
| **DesignRunTag chimera**     | Design-time proofs and run-time telemetry are mixed as if they were the same evidence object. | Evidence belongs to different stances and decays differently.    | Separate lanes and validity windows; treat crossings explicitly.                                         |
| **Ordinal arithmetic** | F or CL ranks become a probability or loss merely by tagging, tabulating, or rescaling them | Ordered categories are not calibrated ratio quantities | Retain the ordinal meaning; any receiving conversion needs its actual model, meaning, scale, and assumptions. |
| **Counting support labels** | More reports are treated as independent confirmation, or one weak additional study automatically defeats the whole | Duplicates, shared bias, complementary information, and counterevidence contribute differently | Recover their actual dependencies and effects on the claim; use neither study count nor a universal min/max fallback. |


---
chunk_kind: "child"
pattern_id: "A.6.Q"
pattern_title: "U.QualityTermPrecisionRestoration — Quality Term Precision Restoration (Q-TERM)"
section_id: "A.6.Q:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.Q/A.6.Q__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.6.Q — U.QualityTermPrecisionRestoration — Quality Term Precision Restoration (Q-TERM)"
  - "A.6.Q:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 13405
line_end: 13417
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "A.6.A"
  - "A.6.B"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "E.17.0"
  - "E.17.2"
  - "F.9"
  - "F.9.1"
keywords:
  - "bridge reading"
  - "endpoint classification"
  - "evaluative ascription"
  - "language-state seam"
  - "quality senses"
  - "quality-term precision restoration"
---

### A.6.Q:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | How to avoid / repair |
| --- | --- | --- | --- |
| **Magic scalar quality** | one number silently stands for several evaluative families | collapses senses, carriers, and scoring legality | publish one explicit `QualitySense` and an admissible normal form |
| **Preconceptual-as-metric** | felt fit is presented as if it were already a measured characteristic | erases articulation stage and overstates evidence | keep it as `SignalPack` until an admissible proxy is declared |
| **Engineering adjective drift** | *reliable / maintainable / high-quality* appear with no explicit Characteristic or Q-Bundle | hides measurement shape and scope | rewrite to one `U.Characteristic` or one `Q-Bundle` |
| **Selector ambiguity** | *quality in QD/NQD* is left undefined | breaks comparability and selection semantics | default to `QS.UseValue` unless another objective head is declared explicitly |
| **Model-quality collapse** | latent fit, explanatory merit, and control adequacy are merged under one phrase | destroys carrier and frame distinctions | split into separate `evaluativeAscription(...)` records |
| **Architecture-vs-description collapse** | *architecture quality* is used with no explicit bearer lane | collapses the described system into its description, carrier, or publication face | publish the bearer lane explicitly and select `QS.EngineeringQualityFamily` or `QS.ArchitecturalDescriptionFitness` |
| **Action-invitation-as-quality** | action invitations are narrated as if they were evaluations | wrong relation family; the rewrite hides action semantics instead of clarifying them | stop the Q-rewrite and `changeRelationKind(...)` into the appropriate action-invitation family |
| **Bridge-by-label** | two traditions both use *quality*, so the draft implies they are the same | creates false identity and silent loss | publish one bridge stance with loss notes |


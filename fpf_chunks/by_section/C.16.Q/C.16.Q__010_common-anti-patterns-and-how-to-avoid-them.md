---
chunk_kind: "child"
pattern_id: "C.16.Q"
pattern_title: "Quality-Term Precision Restoration"
section_id: "C.16.Q:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.Q/C.16.Q__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "C.16.Q — Quality-Term Precision Restoration"
  - "C.16.Q:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 41916
line_end: 41928
dependencies:
  - "A.10"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.6"
  - "A.6.A"
  - "A.6.B"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16"
  - "C.16.P"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.17.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### C.16.Q:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | How to avoid or repair |
| --- | --- | --- | --- |
| **Magic scalar quality** | one number silently stands for several evaluative families | collapses senses, carriers, and scoring legality | publish one explicit `QualitySense` and an admissible normal form |
| **Preconceptual-as-metric** | felt fit is presented as if it were already a measured characteristic | erases articulation stage and overstates evidence | keep it as `SignalPack` until an admissible proxy is declared |
| **Engineering adjective drift** | *reliable, maintainable, or high-quality* appear with no explicit Characteristic or Q-Bundle | hides measurement shape and scope | rewrite to one `U.Characteristic` or one `Q-Bundle` |
| **Selector ambiguity** | *quality in QD and NQD* is left undefined | breaks comparability and selection semantics | default to `QS.UseValue` unless another objective head is declared explicitly |
| **Model-quality collapse** | latent fit, explanatory merit, and control adequacy are merged under one phrase | destroys carrier and frame distinctions | split into separate `qualityTermAscription(...)` records |
| **Architecture-vs-description collapse** | *architecture quality* is used with no explicit bearer lane | collapses the system-side bearer into its description, carrier, or publication face | publish the bearer lane explicitly and select `QS.EngineeringQualityFamily` or `QS.ArchitecturalDescriptionFitness` |
| **Action-invitation-as-quality** | action invitations are narrated as if they were evaluations | wrong governing pattern; the rewrite hides action semantics instead of clarifying them | stop the Q-rewrite and use `assignToGoverningPattern(...)` into `A.6.A` or another action-invitation governing pattern; keep source-tradition `affordance` wording only as a quoted cue |
| **Bridge-by-label** | two traditions both use *quality*, so the draft implies they are the same | creates false identity and silent loss | publish one bridge stance with loss notes |


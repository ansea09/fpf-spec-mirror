---
chunk_kind: "child"
pattern_id: "C.16.Q"
pattern_title: "Quality-Term Precision Restoration"
section_id: "C.16.Q:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.Q/C.16.Q__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "C.16.Q — Quality-Term Precision Restoration"
  - "C.16.Q:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 48378
line_end: 48393
dependencies:
  - "A.10"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
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
  - "C.30.AD"
  - "C.30.ASV"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.17.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
  - "U.ClaimScope"
  - "U.ContextSlice"
  - "U.ViewpointRef"
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
| **Action-invitation-as-quality** | action invitations are narrated as if they were evaluations | the rewrite hides action semantics instead of clarifying them | stop the Q-rewrite and apply `A.6.A` or another applicable action-invitation pattern; name the action invitation and its relevant relation when later use depends on them; keep source-tradition `affordance` wording only as a quoted cue |
| **Generic-frame collapse** | one `evaluationFrame` or context label is expected to supply probe, model, comparison, scope, and scheme semantics | hides independently governed choices and makes a changed comparison look like the same claim | name the effective ReferenceScheme, probe/model frame, A.19.CPM comparison frame, and ClaimScope separately |
| **Embedded viewpoint** | the record stores a viewpoint-looking value as evaluator or generic context | collapses reference, viewpoint episteme, evaluator, and result | store one governed `U.ViewpointRef` or `none`; resolve it under E.17.0 and keep evaluator separate |
| **Witness-is-grounding** | a test report, trace, score, or filled record is cited as empirical grounding | presence of a carrier or result label establishes no direct relation | name witness refs and A.10 path separately; cite an exact obtaining `EpistemeEmpiricalGroundingRelation` or `none` |
| **Bridge-by-label or overlay** | shared *quality* wording or a F.9.1 stance is treated as the cross-local relation or as use authority | creates false identity, silent loss, and unauthorized substitution | resolve exact F.17 cells, test and cite the F.9 Bridge, then state the separate bounded-use claim; add a Card or overlay only when independently present |


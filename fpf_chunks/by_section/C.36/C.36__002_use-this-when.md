---
chunk_kind: "child"
pattern_id: "C.36"
pattern_title: "Cultural Evolution and Cultural-Evolution Engineering"
section_id: "C.36:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.36/C.36__002_use-this-when.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.36 — Cultural Evolution and Cultural-Evolution Engineering"
  - "C.36:0 — Use This When"
line_start: 67861
line_end: 67925
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.6"
  - "A.15.PROD"
  - "A.2.1"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
  - "A.6.RCD"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.20"
  - "C.23"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32"
  - "C.35"
  - "C.36.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.18"
  - "E.18.1"
  - "F.17"
  - "F.18"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.5"
keywords:
---

### C.36:0 - Use This When

Use this pattern when the current project question is about how a culture, style, tradition, discipline practice, method family, work family, canon, recognition regime, selection regime, or mediating system changes and can be deliberately influenced.

Typical first-use situations:

- an engineering group treats its product family, toolchain, platform family, research program, or AI-agent framework as an evolving set of variants rather than one fixed system;
- a scientific, medical, pedagogical, engineering, music, dance, organizational, or AI-agent discipline is changing through related methods, work products, training forms, memory epistemes, recognition regimes, and selected variants;
- a music or dance steward needs to compare style, genre, technique, scene, canon, platform, or tradition labels without assuming that the label names one root kind;
- a project lead wants an intervention that changes generation, transmission, selection, recognition, memory, method-family, work-family, system-role-assignment, mediation, architecture, measurement, or refresh relations.

#### C.36:0.1 - What Goes Wrong If Missed

The team treats culture as shared vocabulary, treats style as a genre tree, treats a platform as the cultural object, treats a QD archive as the decision, or treats one scalar popularity or quality score as cultural development. The project can then generate many variants but still lose the relations that make those variants transmissible, recognizable, selectable, retained, refreshed, or turned into work.

#### C.36:0.2 - What This Buys

The practitioner gets one small cultural-evolution case that names the collective holons, exact local system-role kinds and any obtaining assignments that matter, work families, method families, canon or memory epistemes, recognition and selection regimes, mediation systems or architectures, variant sets, term bridges, current intervention, measurement, and refresh relation. After that, the project can apply the subject pattern for the next claim.

#### C.36:0.3 - First Useful Move

Write a compact `CulturalEvolutionCaseCard@Context`. It names what is changing, which FPF values and exact subject assertions are current, and which candidate pattern description locates the defining or constraining `ClaimGraph` for the next question.

```text
CulturalEvolutionCaseCard@Context:
  CaseRef:
  BoundedContext:
  CollectiveHolonRefs:
  RoleWordRecoveryRefs?: E.10.ROLE results for every role-like source label used by the case
  DirectParticipationOrPositionRelationRefs?: obtaining direct relations when a label resolves to a participant or organization or representation position
  SystemRoleKindRefs?: U.KindRef, each resolving to one exact local system-role kind
  SystemRoleClassificationJudgmentRefs?: U.RelationRef, each resolving a separate judgment about an admitted System
  SystemRoleAssignmentSpeciesRefs?: U.RelationKindRef, each resolving to one directly declared species under U.SystemRoleAssignment
  SystemRoleAssignmentOccurrenceRefs?: U.RelationRef, each resolving to one obtaining occurrence of a cited species
  WorkFamilyRefs:
  MethodFamilyRefs:
  MethodRelationStructureRefs?:
  MethodDescriptionRefs?:
  CanonOrMemoryEpistemeRefs:
  DisciplineRefs?:
  SelectionOrRecognitionRegimeRefs:
  MediationSystemOrArchitectureRefs?:
  MeasurementOrVisibilityRelationRefs?:
  VariantSetRefs:
  CharacteristicSpaceRefs?:
  LevelOrScopeRefs?:
  StyleOrTraditionTermRows?:
  CurrentEvolutionaryQuestion:
  CurrentPatternLocators:
  RefreshRefs?:
```

Field glosses for first use:

| Field | Meaning in the card |
|---|---|
| `VariantSetRefs` | Generated, retained, inherited, or observed variants whose cultural or engineering evolution is being considered; archive or front authority still comes from `C.18` or `C.19`. |
| `CharacteristicSpaceRefs` | The feature, descriptor, quality, constraint, or value space in which variation and selection become comparable; several feature spaces may be current in one style or tradition case. |
| `LevelOrScopeRefs` | The holon level, discipline scope, scene, product-family scope, team scope, or publication scope in which the case is being judged; this prevents one local trend from becoming the whole culture by wording. |
| `StyleOrTraditionTermRows` | Bridge rows for labels such as style, tradition, genre, school, canon, technique, scene, or platform format; these rows keep familiar terms usable without making them root kinds. |
| `CurrentEvolutionaryQuestion` | The live question. Examples include generation, transmission, recognition, selection, retention, mediation, method-family change, work-family change, architecture-candidate treatment, measurement, intervention, and refresh. |
| `CurrentPatternLocators` | The FPF patterns that define or constrain the current values. Use C.36 to keep the cultural-evolution case together; use the applicable patterns for archive, front, selected-set result declaration, actual publication, decision, work, evidence, architecture, term bridge, or refresh. |

The card is optional and thin. It is not a root U-kind, lifecycle step, evidence record, decision record, publication authority, or replacement for the named subject patterns.


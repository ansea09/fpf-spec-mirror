---
chunk_kind: "child"
pattern_id: "C.36"
pattern_title: "Cultural Evolution and Cultural-Evolution Engineering"
section_id: "C.36:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.36/C.36__006_solution.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "C.36 — Cultural Evolution and Cultural-Evolution Engineering"
  - "C.36:4 — Solution"
line_start: 63289
line_end: 63373
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
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
  - "C.36.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.18"
  - "E.18.1"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "G.5"
keywords:
---

### C.36:4 - Solution

Recover the cultural-evolution case first, then identify the governing FPF pattern for each current value.

A cultural-evolution case is a collective-holon and discipline-facing situation in which systems in roles perform related work families by related method families, while memory or canon epistemes, recognition and selection regimes, mediation systems or architectures, measurement or visibility relations, and publication forms preserve, transmit, select, suppress, or refresh variants.

Cultural-evolution engineering is deliberate intervention into one or more of those relations. The intervention may change generation, transmission, selection, recognition, memory, method-family, work-family, role-assignment, mediation, architecture, work-plan, performed-work, measurement, or refresh relations.

Keep three record forms available:

- `CulturalEvolutionCaseCard@Context` names the case.
- `StyleTraditionTermBridgeTable@Context` maps local labels to governed FPF values and bridges.
- `CulturalEvolutionInterventionCard@Project` names the intervention and the next governing pattern.

These forms assemble current FPF values. They do not mint `U.Culture`, `U.Style`, `U.Tradition`, `U.Practice`, `U.Genre`, `U.Scene`, `U.Technique`, `U.Platform`, `U.PlatformRegime`, `U.MeasurementRegime`, or `U.DevelopmentalMachine`.

#### C.36:4.1 - Style And Tradition Term Bridge

Use a term bridge when a source or project label must remain usable across contexts.

```text
StyleTraditionTermBridgeTable@Context:
  SourceLabel:
  SourceContext:
  GovernedFPFValueOrSlot:
  DirectGoverningPatternRef:
  SenseCellRefs:
  BridgeRefs:
  AdmissibleUse:
  BlockedUse:
  CurrentnessCondition:
```

The table is a term-and-bridge table. `F.17` governs durable term rows, `F.18` governs naming restoration, and `F.9` governs bridge relations. C.36 uses the table only to keep cultural-evolution work connected to those governing patterns.

For music and dance, a label such as `prog`, `post-prog`, `contemporary`, `hip-hop`, `battle`, `TikTok dance`, `canon`, `school`, or `technique` may point to different FPF values in different contexts. The bridge row says which one is current before the project relies on the label.

#### C.36:4.2 - Intervention Card

Use an intervention card when the project deliberately changes part of the cultural-evolution case.

```text
CulturalEvolutionInterventionCard@Project:
  InterventionRef:
  CulturalEvolutionCaseRef:
  ProblemCardRef?:
  TargetedRelation:
  AffectedMethodFamilyRefs?:
  AffectedWorkFamilyRefs?:
  AffectedRoleAssignmentRefs?:
  AffectedCanonOrMemoryEpistemeRefs?:
  AffectedSelectionOrRecognitionRegimeRefs?:
  AffectedMediationSystemOrArchitectureRefs?:
  VariantSetOrPortfolioRefs?:
  TransformationFlowStructureRef?:
  P2WCarryThroughRef?:
  WorkPlanRef?:
  WorkOccurrenceRef?:
  MeasurementOrEffectRef?:
  RefreshRef?:
```

The intervention card does not authorize work. It names the relation being changed and the next governing pattern: `E.18.1` for P2W carry-through, `A.15.2` for work planning, `A.15.1` for performed work, `C.18` or `C.19` for archive and pool treatment, `G.5` for selected-set publication, `C.11` for local choice, `C.30` for architecture, or `G.11` for refresh.

#### C.36:4.3 - Evolution Sense Split

Use this split before applying the pattern:

| Current question | Use |
|---|---|
| A bounded entity changes under conditions. | `A.3.4 U.Transformation`. |
| A temporal aspect, currentness window, rhythm, cadence, or authored temporal claim is current. | `C.27.TA`, `C.27`, or `A.3.3` according to the claim. |
| An engineering project manages an evolving archive, front, current pool, selected set, edition lineage, or family of variants. | `C.18`, `C.19`, `G.5`, `G.11`, and `E.18.1`. |
| A collective-holon or discipline-facing method, work, role, canon, memory, recognition, selection, mediation, style, tradition, or intervention relation is current. | `C.36`. |

An engineering development loop may use C.36, but it does not automatically become cultural evolution. It becomes C.36 work only when the collective-holon or discipline-facing cultural-evolution relations above are current.

#### C.36:4.4 - Platform, Regime, And Attractor Wording

Recover the current object before accepting platform, regime, or attractor wording.

- Platform, recommendation environment, visibility infrastructure, algorithmic mediator, or platform-regime wording may name a system, holon-in-role value, system architecture, product architecture, recognition regime, selection regime, measurement relation, visibility relation, publication relation, bounded context, or source-currentness relation.
- Measurement regime wording may name a characteristic space, measurement relation, visibility relation, publication relation, dashboard relation, source-currentness relation, or comparison setup.
- Attractor, basin, stable-dynamics, state-transition-law, and mathematical-model wording uses `A.3.3`, `C.27`, and `C.29` when that claim is current. Loose style metaphor remains term and bridge work through `F.17`, `F.18`, and `F.9`.


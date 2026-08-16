---
chunk_kind: "child"
pattern_id: "C.36"
pattern_title: "Cultural Evolution and Cultural-Evolution Engineering"
section_id: "C.36:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.36/C.36__006_solution.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.36 — Cultural Evolution and Cultural-Evolution Engineering"
  - "C.36:4 — Solution"
line_start: 67961
line_end: 68061
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

### C.36:4 - Solution

Recover the cultural-evolution case first, then identify the governing FPF pattern for each current value.

A cultural-evolution case is a collective-holon and discipline-facing situation. Admitted Systems may perform independently identified dated Work, and those Work occurrences may enact exact Methods. Separately identified work and method families may organize comparison. Memory or canon epistemes, recognition and selection regimes, mediation systems or architectures, measurement or visibility relations, and publication forms preserve, transmit, select, suppress, or refresh variants. Keep all facts required by A.15.1, A.2.1, and F.6 recoverable for each Work occurrence. The case card records the constellation without making a family, assignment, Method, episteme, or selected structure act.

Cultural-evolution engineering proposes or performs deliberate intervention concerning one or more of those relations. The intended intervention may target generation, transmission, selection, recognition, memory, method-family, work-family, system-role-assignment, mediation, architecture, work-plan, performed-Work, measurement, or refresh relations. A card or intention establishes none of the performed Work, actual transformation, effect, measurement, selected structure, responsibility, or authority; each positive claim needs its direct predicate or the exact missing-governor result.

Keep three record forms available:

- `CulturalEvolutionCaseCard@Context` names the case.
- `StyleTraditionTermBridgeTable@Context` maps local labels to governed FPF values and bridges.
- `CulturalEvolutionInterventionCard@Project` names the intervention and the next subject pattern.

These forms assemble current FPF values. They do not mint `U.Culture`, `U.Style`, `U.Tradition`, `U.Practice`, `U.Genre`, `U.Scene`, `U.Technique`, `U.Platform`, `U.PlatformRegime`, `U.MeasurementRegime`, or `U.DevelopmentalMachine`.

#### C.36:4.1 - Style And Tradition Term Bridge

Use a term bridge when a source or project label must remain usable across contexts.

```text
StyleTraditionTermBridgeTable@Context:
  SourceLabel:
  SourceContext:
  GovernedFPFValueOrSlot:
  SubjectPatternLocator:
  SenseCellRefs:
  BridgeRefs:
  AdmissibleUse:
  BlockedUse:
  CurrentnessCondition:
```

The table is a term-and-bridge table. `F.17` governs durable term rows, `F.18` governs naming restoration, and `F.9` governs bridge relations. C.36 uses the table only to keep cultural-evolution work connected to those subject patterns.

For music and dance, a label such as `prog`, `post-prog`, `contemporary`, `hip-hop`, `battle`, `TikTok dance`, `canon`, `school`, or `technique` may point to different FPF values in different contexts. The bridge row says which one is current before the project relies on the label.

#### C.36:4.2 - Intervention Card

Use an intervention card when one project proposes or performs a deliberate intervention concerning part of the cultural-evolution case. Keep proposal and performance separate. If actual performance is claimed, name the `U.Work` occurrence and keep all facts required by A.15.1, A.2.1, and F.6 recoverable; add actual change and a direct Work-to-change relation only when each independently obtains. If only an effect is claimed, use its own direct predicate and participants without manufacturing a performer, assignment, or Work. Recover unresolved claim-bearing *role* wording through `E.10.ROLE`; keep a local system-role kind and any separate System-classification judgment independently optional.

```text
CulturalEvolutionInterventionCard@Project:
  ProjectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  InterventionCardProjectUseRelationRef?: U.RelationRef governed by the exact intervention-use or work-use pattern
  InterventionRef:
  CulturalEvolutionCaseRef:
  ProblemCardRef?:
  TargetedRelation:
  AffectedMethodFamilyRefs?:
  AffectedWorkFamilyRefs?:
  AffectedAssignmentSpeciesRefs?: U.RelationKindRef, each constrained under U.SystemRoleAssignment
  AffectedAssignmentOccurrenceRefs?: U.RelationRef, each constrained to U.SystemRoleAssignment and paired with its species
  AffectedCanonOrMemoryEpistemeRefs?:
  AffectedSelectionOrRecognitionRegimeRefs?:
  AffectedMediationSystemOrArchitectureRefs?:
  VariantSetOrPortfolioRefs?:
  TransformationFlowStructureRef?: exact independently selected E.18 TransformationFlowStructure
  P2WCarryThroughRef?:
  WorkPlanRef?:
  InterventionSystemRoleKindRef?: U.KindRef resolving to one exact local system-role kind
  InterventionSystemRoleClassificationJudgmentRef?: U.RelationRef
  InterventionAssignmentSpeciesRef?: U.RelationKindRef constrained under U.SystemRoleAssignment
  InterventionAssignmentOccurrenceRef?: U.RelationRef constrained to U.SystemRoleAssignment
  PerformedInterventionWorkRef?: U.EntityRef constrained to U.Work
  ActualTransformationRefs?:
  WorkToTransformationOrEffectClaimRefs?:
  MeasurementRefs?:
  EffectClaimOrRelationRefs?:
  RefreshRef?:
```

Here `@Project` is a compatibility and retrieval cue only. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood. When the intervention card is genuinely used in one actual project, `ProjectWorkOccurrenceRef` identifies the exact composite `U.Work` and `InterventionCardProjectUseRelationRef` identifies the direct relation by which that exact project Work uses the card. The suffix or either reference alone establishes no project locality. The intended intervention, card, and composite project Work remain separately identifiable.

When performed intervention Work is current, `PerformedInterventionWorkRef` names the independently identified `U.Work` occurrence. All facts required by A.15.1, A.2.1, and F.6 remain recoverable. A short card may omit only an unused assignment identifier. The local system-role kind and any System-classification judgment remain separate optional facts. Assignment establishes no Work, capability, functioning, authority, or responsibility.

A positive responsibility claim uses an admitted domain predicate through `TargetedRelation` or `EffectClaimOrRelationRefs`; without one, return the A.6.RCD missing-governor result. `ActualTransformationRefs` may cite only independently identified A.3.4 bounded changes. `TransformationFlowStructureRef` instead cites one E.18 transformation-flow structure selected under A.22; adjacency or membership in it proves neither actual change nor Work-to-change. Any positive link from intervention Work to an actual transformation or other effect must cite its declared predicate, an admitted A.6.RCD local claim, or the relevant A.15.PROD branch; otherwise return `missing-governor`. An effect that does not require Work stays on its own direct relation; observing a value neither creates nor proves it.

The intervention card does not authorize Work, and its targeted relation is not an obtaining-effect claim. It names the proposed intervention, the relation being targeted, and the next applicable pattern. Use `E.18.1` for P2W carry-through, `A.15.2` for work planning, `A.15.1` and `F.6` for performed Work, `A.3.4` for actual change, `A.15.PROD` or a direct local claim for production or Work-to-change, `C.18` or `C.19` for archive and pool treatment, `G.5` for selected-set result declaration, `C.11` for local choice, `C.35` when a generated or discovered structure-bearing carrier needs admission before architecture use, `C.30` for a direct architecture question, or `G.11` for refresh. If audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability.

#### C.36:4.3 - Evolution Sense Split

Use this split before applying the pattern:

| Current question | Use |
|---|---|
| A bounded entity changes under conditions. | `A.3.4 U.Transformation`. |
| A temporal aspect, currentness window, rhythm, cadence, or authored temporal claim is current. | `C.27.TA`, `C.27`, or `A.3.3` according to the claim. |
| An engineering project manages an evolving archive, front, current pool, selected set, edition lineage, or family of variants. | `C.18`, `C.19`, `G.5`, `G.11`, and `E.18.1`. |
| A collective-holon or discipline-facing method, Work, system-role kind or assignment, canon, memory, recognition, selection, mediation, style, tradition, or intervention relation is current. | `C.36`. |

An engineering development loop may use C.36, but it does not automatically become cultural evolution. It becomes C.36 work only when the collective-holon or discipline-facing cultural-evolution relations above are current.

#### C.36:4.4 - Platform, Regime, And Attractor Wording

Recover the current object before accepting platform, regime, or attractor wording.

- Platform, recommendation environment, visibility infrastructure, algorithmic mediator, or platform-regime wording may name a system, a system classified under an exact local system-role kind, another governed relation participant, a system architecture, product architecture, recognition regime, selection regime, measurement relation, visibility relation, publication relation, bounded context, or source-currentness relation.
- Measurement regime wording may name a characteristic space, measurement relation, visibility relation, publication relation, dashboard relation, source-currentness relation, or comparison setup.
- Attractor, basin, stable-dynamics, state-transition-law, and mathematical-model wording uses `A.3.3`, `C.27`, and `C.29` when that claim is current. Loose style metaphor remains term and bridge work through `F.17`, `F.18`, and `F.9`.


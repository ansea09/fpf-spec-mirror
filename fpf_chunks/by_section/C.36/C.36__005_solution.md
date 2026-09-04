---
chunk_kind: "child"
pattern_id: "C.36"
pattern_title: "Cultural Evolution and Cultural-Evolution Engineering"
section_id: "C.36:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.36/C.36__005_solution.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "C.36 — Cultural Evolution and Cultural-Evolution Engineering"
  - "C.36:4 — Solution"
line_start: 67653
line_end: 67780
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
  - "A.6.1"
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
  - "E.10.DEV"
  - "E.10.MOVE"
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

First state the cultural-evolution case in ordinary language: what collective or discipline-facing activity is changing, which variants are in play, which relations transmit, recognize, select, retain, or mediate them, and what next action follows. Then use the applicable FPF pattern only for a claim whose definition or test matters.

An admitted System may perform dated Work, and that Work may enact a Method. Work and Method families may organize comparison. Canon or memory epistemes, recognition and selection relations, mediation systems or architectures, measurement or visibility relations, and publication forms may preserve, transmit, select, suppress, or refresh variants.

These are separate facts. For every claimed Work occurrence, recover each exact actual performer through A.13 and let A.15.1 independently admit the Work. Add assignment and F.6 only when the case or receiving use expressly represents precise assignment-bound attribution. A case card does not make a family, assignment, Method, episteme, or selected structure act.

Cultural-evolution engineering proposes or performs a deliberate change to one or more of these relations. Proposal, performed Work, actual transformation, measured effect, responsibility, authority, selected structure, and publication are different claims. Name each only when its own predicate obtains.

Keep a project choice separate from what happens across a practice or population. A project may choose or authorize an intervention, but that does not show that variants were transmitted, recognized, selected, retained, or lost. Conversely, observed spread or persistence does not authorize the project action or show that it succeeded. When both questions matter, record the project choice and performed intervention through their own patterns, then record the cultural relations and their observed change here.

When the question is how the practice may develop, keep more than one serious hypothesis and name an observation that would distinguish them. Use `B.5` and `B.5.2` for hypotheses and their testable consequences. Use `A.3.3` when the claim states a state space and transition law, and use `C.28` when the current use relies on a causal claim. During ongoing Work, use `A.15.7` to choose the next action. Use `C.11` only when a named deciding System already knows what it is deciding, has an already formed set of options, and another observation can change the choice. Without that bounded choice, use the applicable DPF or field Method for experiment or probe design. Use `A.10`, `C.16`, and `C.27` for evidence, measurement, and time limits.

Use only the smallest form the current task needs:

- `CulturalEvolutionCaseCard@Context` keeps a multi-relation case together;
- `StyleTraditionTermBridgeTable@Context` keeps a familiar local label connected to the recovered FPF value or relation;
- `CulturalEvolutionInterventionCard@Project` retains an intervention when proposal, Work, effect, or later comparison needs explicit identity.

These forms assemble existing FPF values. They do not mint `U.Culture`, `U.Style`, `U.Tradition`, `U.Practice`, `U.Genre`, `U.Scene`, `U.Technique`, `U.Platform`, `U.PlatformRegime`, `U.MeasurementRegime`, or `U.DevelopmentalMachine`.

#### C.36:4.1 - Style And Tradition Term Bridge

Use a term bridge when a source or project label must remain usable across contexts.

```text
StyleTraditionTermBridgeTable@Context:
  SourceLabel:
  SourceContext:
  RecoveredFPFValueOrRelation:
  ApplicablePatternRef:
  SenseCellRefs:
  BridgeRefs:
  AdmissibleUse:
  BlockedUse:
  CurrentnessCondition:
```

The table records term use and any actual bridge. F.17 supplies durable term rows, F.18 supplies naming restoration, and F.9 defines bridge relations. C.36 uses the result only to keep the cultural-evolution case connected to those exact contributions.

For music and dance, a label such as `prog`, `post-prog`, `contemporary`, `hip-hop`, `battle`, `TikTok dance`, `canon`, `school`, or `technique` may point to different FPF values in different contexts. The bridge row says which one is current before the project relies on the label.

#### C.36:4.2 - Intervention Card

Use an intervention card when a project must retain the identity of a proposed or performed intervention. First write the ordinary claim: what relation will change, by what proposed action, what effect is expected, how it will be measured, and what would stop or redirect the attempt. For example: `The festival will change jury feedback timing; adoption in the next teaching cycle is the measured effect; use A.15.2 for the plan and A.3.4 only if an actual change later obtains.`

Keep proposal and performance separate. The full card below is an assurance expansion, not a first-use form.

Open its Work, assignment, transformation, effect, architecture, and publication fields only when those identities matter. `AffectedMediationSystemOrArchitectureRefs` names actual mediating Systems or architectures only. Publication refs name only the exact objects needed by the intervention; omit them otherwise. Actual access, reliance, use, and Work stay outside this field unless separately current. If actual performance is claimed, recover each exact performer through A.13 and let A.15.1 independently admit the `U.Work`. Add assignment and F.6 only when the card or receiving use expressly represents precise assignment-bound attribution; missing or failed F.6 leaves the Work intact. Add actual change and a Work-to-change relation only when each independently obtains. An effect can obtain without manufacturing a performer, assignment, or Work. Recover unresolved claim-bearing *role* wording through E.10.ROLE; a local system-role kind and classification judgment remain independently optional.

```text
CulturalEvolutionInterventionCard@Project:
  ProjectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  InterventionCardProjectUseRelationRef?: U.RelationRef, only when a named pattern defines this project-use relation and the occurrence obtains
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
  PublicationRefs?: refs to the exact E.17 source-backed face or E.24.PUB publication occurrence, publication form, presentation carrier, audience-declaration episteme, bounded-use-declaration episteme, or availability claim needed by this intervention
  VariantSetOrPortfolioRefs?:
  TransformationFlowStructureRef?: exact independently selected E.18 TransformationFlowStructure
  P2WCarryThroughRef?:
  WorkPlanRef?:
  InterventionSystemRoleKindRef?: U.KindRef resolving to one exact local system-role kind
  InterventionSystemRoleClassificationJudgmentRef?: U.RelationRef
  InterventionAssignmentSpeciesRef?: U.RelationKindRef constrained under U.SystemRoleAssignment
  InterventionAssignmentOccurrenceRef?: U.RelationRef constrained to U.SystemRoleAssignment
  PerformedInterventionWorkRef?: U.EntityRef constrained to U.Work
  PerformedInterventionWorkAttributionRefs?: refs to obtaining F.6 performedUnderAssignment relations only when the card or receiving use expressly represents attribution
  ActualTransformationRefs?:
  WorkToTransformationOrEffectClaimRefs?:
  MeasurementRefs?:
  EffectClaimOrRelationRefs?:
  RefreshRef?:
```

`@Project` is part of the card's retrieval name. It establishes no project entity, composite-work identity, context, authority, viewpoint, or parthood.

When the card is used in an actual project, `ProjectWorkOccurrenceRef` identifies the composite `U.Work`, and `InterventionCardProjectUseRelationRef` identifies the direct relation by which that Work uses the card. The suffix or either reference alone establishes no project locality. The proposed intervention, card, and project Work remain separate.

Use the expanded identity fields only when a later claim or comparison needs them. For performed intervention Work, recover each exact actual performer through A.13 and let `PerformedInterventionWorkRef` name an independently admitted A.15.1 `U.Work`. `PerformedInterventionWorkAttributionRefs`, assignment species, and assignment occurrence are optional and appear only when the card or receiving use expressly represents precise assignment-bound attribution through the same obtaining A.13 assignment. A proposal omits Work and attribution fields. A local system-role kind and classification judgment remain optional and separate. Assignment establishes no classification, Work, capability, functioning, authority, or responsibility.

**Responsibility and change.** A positive responsibility claim needs an admitted domain predicate through `TargetedRelation` or `EffectClaimOrRelationRefs`; otherwise return A.6.RCD's `missing-governor`. `ActualTransformationRefs` may cite only changes independently identified under A.3.4.

**Flow representation.** `TransformationFlowStructureRef` may cite an E.18 transformation-flow structure selected under A.22. Membership or adjacency in that structure proves neither actual change nor a Work-to-change link.

**Work-to-change.** A positive link from intervention Work to an actual transformation or effect needs a direct predicate that obtains for those participants, an exact A.6.1 application binding when that declaration supplies the link, or an admitted A.6.RCD local claim. If none applies, return the reason-specific non-assertability result.

**Effects and production.** A.15.PROD answers only its production-work, entity-inception, or completion question; it does not supply the Work-to-change link. An effect that does not require Work stays on its own direct relation. Observing a value neither creates nor proves the effect.

The intervention card does not authorize Work, and its targeted relation does not assert that an effect obtains. It keeps the proposed intervention, targeted relation, and next applicable pattern together.

For planning and performance, use E.18.1 for P2W carry-through, A.15.2 for work planning, A.13 and A.15.1 for exact actual performers and independently admitted Work, and A.2.1/F.6 only when precise assignment-bound attribution is expressly consumed. Use A.3.4 for actual change. A.15.PROD may answer one current production-work, entity-inception, or completion question; the Work-to-change link still uses the direct predicate, A.6.1 binding, A.6.RCD local claim, or non-assertability result above.

For archive or pool treatment use C.18 or C.19; for a selected-set result use G.5; for local choice use C.11; for carrier admission before architecture use C.35; for an architecture question use C.30; and for refresh use G.11. If audience availability is current, use E.17 for a source-backed publication face and return to source, and E.24.PUB for the publication occurrence, form, carrier, audience, bounded use, and availability.

#### C.36:4.3 - Evolution Sense Split

When generic *development* or *evolution* wording still hides the changed or represented subject, needed continuity or membership, posture, direction or value basis, or direct owner, enter through `E.10.DEV` before this split. A recovered cultural-population or discipline-facing variant claim may continue here. A non-cultural population or lineage without an admitted owner remains the exact architecture gap returned by `E.10.DEV`; do not substitute C.36. Open `E.10.MOVE` afterward only when a separately relied-on trajectory, route, path, ordering, posture, or representation ambiguity remains.

Then use this cultural split:

| Current question | Use |
|---|---|
| Generic development or evolution wording still hides the changed or represented subject, continuity or membership, posture, direction or value basis, or direct owner. | Use `E.10.DEV` first; return to C.36 only if the recovered claim is cultural-population or discipline-facing cultural evolution. |
| A bounded entity changes under conditions. | `A.3.4 U.Transformation`. |
| A temporal aspect, currentness window, rhythm, cadence, or authored temporal claim is current. | `C.27.TA`, `C.27`, or `A.3.3` according to the claim. |
| An engineering project manages an evolving archive, front, current pool, selected set, edition lineage, or family of variants. | `C.18`, `C.19`, `G.5`, `G.11`, and `E.18.1`. |
| A collective-holon or discipline-facing method, Work, system-role kind or assignment, canon, memory, recognition, selection, mediation, style, tradition, or intervention relation is current. | `C.36`. |

An engineering development loop may use C.36, but it does not automatically become cultural evolution. It becomes C.36 work only when the collective-holon or discipline-facing cultural-evolution relations above are current.

#### C.36:4.4 - Platform, Regime, And Attractor Wording

Recover the current object before accepting platform, regime, or attractor wording.

- Platform, recommendation environment, visibility infrastructure, algorithmic mediator, or platform-regime wording may name a System, a System classified under a local system-role kind, another relation participant, a system or product architecture, recognition or selection relation, measurement or visibility relation, publication relation, model-use boundary, project scope, or source-currentness relation.
- Measurement regime wording may name a characteristic space, measurement relation, visibility relation, publication relation, dashboard relation, source-currentness relation, or comparison setup.
- Attractor, basin, stable-dynamics, state-transition-law, and mathematical-model wording uses `A.3.3`, `C.27`, and `C.29` when that claim is current. Loose style metaphor remains term and bridge work through `F.17`, `F.18`, and `F.9`.

